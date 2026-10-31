#!/usr/bin/env python3
"""
Convert Markdown files to PDFs with a sleek dark theme UI.
Matches the dark mode preview styling:
- Dark background (#181818)
- White / light silver typography (#ffffff / #f0f0f0)
- Distinctive inline code badges (#292929)
- Clean dividers (#323232)
- High-fidelity tables, blockquotes, code blocks, and embedded images
- Zero modifications to original markdown files
"""

import os
import sys
import re
import base64
import tempfile
import subprocess
import shutil

# Target markdown files if none specified via command line arguments
DEFAULT_TARGET_FILES = [
    "THEORY-NOTES.md",
    "ANSWERS-CV-Mid-Term-Sample-Questions.md",
    "05-Practice-and-Project/ANSWERS-Week1-Questions.md",
    "05-Practice-and-Project/ANSWERS-Week2-and-Week3-Questions.md",
]

DARK_THEME_CSS = """
@page {
  size: A4;
  margin: 16mm 18mm;
  background-color: #181818;
}

* {
  box-sizing: border-box;
  -webkit-print-color-adjust: exact !important;
  print-color-adjust: exact !important;
}

html, body {
  background-color: #181818 !important;
  color: #dedede !important;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  font-size: 14.5px;
  line-height: 1.65;
  margin: 0;
  padding: 0;
}

/* Headings */
h1, h2, h3, h4, h5, h6 {
  color: #ffffff;
  font-weight: 600;
  line-height: 1.3;
  break-after: avoid;
  page-break-after: avoid;
}

h1 {
  font-size: 24px;
  font-weight: 700;
  margin-top: 26px;
  margin-bottom: 16px;
}

h2 {
  font-size: 20px;
  font-weight: 600;
  margin-top: 22px;
  margin-bottom: 12px;
}

h3 {
  font-size: 16.5px;
  font-weight: 600;
  margin-top: 18px;
  margin-bottom: 10px;
}

h4 {
  font-size: 15px;
  font-weight: 600;
  margin-top: 16px;
  margin-bottom: 8px;
}

/* Paragraphs and text */
p {
  margin-top: 0;
  margin-bottom: 12px;
  color: #dedede;
}

strong, b {
  color: #ffffff;
  font-weight: 600;
}

em, i {
  color: #cccccc;
  font-style: italic;
}

/* Dividers */
hr {
  border: none;
  height: 1px;
  background-color: #323232;
  margin: 22px 0;
  break-after: avoid;
  page-break-after: avoid;
}

/* Inline Code Badges */
code {
  background-color: #292929;
  color: #f0f0f0;
  padding: 2px 6px;
  border-radius: 4px;
  font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Monaco, Consolas, "Liberation Mono", monospace;
  font-size: 0.88em;
}

/* Code Blocks */
pre {
  background-color: #1e1e1e;
  border: 1px solid #303030;
  border-radius: 6px;
  padding: 12px 16px;
  overflow-x: auto;
  break-inside: avoid;
  page-break-inside: avoid;
  margin-top: 0;
  margin-bottom: 14px;
}

pre code {
  background-color: transparent;
  padding: 0;
  border-radius: 0;
  font-size: 13px;
  line-height: 1.45;
  color: #f0f0f0;
}

/* Lists */
ul, ol {
  margin-top: 0;
  margin-bottom: 12px;
  padding-left: 22px;
}

li {
  margin-bottom: 6px;
  color: #dedede;
}

li strong {
  color: #ffffff;
}

/* Blockquotes */
blockquote {
  border-left: 3px solid #4a5568;
  margin: 12px 0;
  padding: 6px 14px;
  color: #a0aec0;
  background-color: #1a1a1a;
  border-radius: 0 4px 4px 0;
  break-inside: avoid;
  page-break-inside: avoid;
}

/* Tables */
table {
  border-collapse: collapse;
  width: 100%;
  margin: 16px 0;
  break-inside: avoid;
  page-break-inside: avoid;
  font-size: 13.5px;
}

th, td {
  border: 1px solid #333333;
  padding: 8px 12px;
  text-align: left;
}

th {
  background-color: #242424;
  color: #ffffff;
  font-weight: 600;
}

tr:nth-child(even) {
  background-color: #1c1c1c;
}

/* Links */
a {
  color: #58a6ff;
  text-decoration: none;
}

/* Images */
img {
  max-width: 90%;
  height: auto;
  display: block;
  margin: 16px auto;
  border-radius: 6px;
  break-inside: avoid;
  page-break-inside: avoid;
}
"""


def find_chrome():
    """Find a Chrome / Chromium / Edge / Brave executable on the system."""
    candidates = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        "google-chrome",
        "google-chrome-stable",
        "chromium",
        "chromium-browser",
        "chrome",
    ]
    for c in candidates:
        if os.path.exists(c) and os.access(c, os.X_OK):
            return c
        resolved = shutil.which(c)
        if resolved:
            return resolved
    return None


def embed_local_images(html_text, base_dir):
    """Convert relative image URLs to base64 Data URIs so Chrome renders them reliably."""
    def replacer(match):
        src = match.group(1)
        if src.startswith(("http://", "https://", "data:")):
            return match.group(0)
        img_path = os.path.normpath(os.path.join(base_dir, src))
        if os.path.exists(img_path):
            ext = os.path.splitext(img_path)[1].lower().lstrip(".")
            if ext == "jpg":
                ext = "jpeg"
            elif ext == "svg":
                ext = "svg+xml"
            try:
                with open(img_path, "rb") as f:
                    data = base64.b64encode(f.read()).decode("utf-8")
                return f'src="data:image/{ext};base64,{data}"'
            except Exception:
                pass
        return match.group(0)

    return re.sub(r'src=["\'](.*?)["\']', replacer, html_text)


def markdown_to_html(md_text):
    """Convert markdown text to HTML body."""
    try:
        import markdown
        return markdown.markdown(
            md_text,
            extensions=["extra", "tables", "fenced_code"]
        )
    except ImportError:
        # Fallback to pandoc if markdown package is not available
        p = subprocess.run(
            ["pandoc", "-f", "gfm", "-t", "html"],
            input=md_text,
            text=True,
            capture_output=True,
            check=True
        )
        return p.stdout


def convert_file(md_path, chrome_bin, workspace_dir):
    """Convert a single Markdown file to PDF."""
    abs_md_path = os.path.abspath(md_path)
    if not os.path.exists(abs_md_path):
        print(f"[ERROR] File not found: {md_path}")
        return False

    pdf_path = os.path.splitext(abs_md_path)[0] + ".pdf"
    base_dir = os.path.dirname(abs_md_path)

    print(f"Converting: {os.path.relpath(abs_md_path, workspace_dir)}")

    # Read markdown without modifying it
    with open(abs_md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    # Parse markdown to HTML
    html_body = markdown_to_html(md_text)

    # Embed local images as base64
    html_body = embed_local_images(html_body, base_dir)

    title = os.path.splitext(os.path.basename(abs_md_path))[0]
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{title}</title>
  <style>
{DARK_THEME_CSS}
  </style>
</head>
<body>
{html_body}
</body>
</html>
"""

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_html = os.path.join(tmp_dir, "document.html")
        with open(tmp_html, "w", encoding="utf-8") as f:
            f.write(full_html)

        cmd = [
            chrome_bin,
            "--headless=new",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={pdf_path}",
            tmp_html,
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"[ERROR] Chrome failed to generate PDF for {md_path}:")
            print(result.stderr)
            return False

    if os.path.exists(pdf_path):
        file_size_kb = os.path.getsize(pdf_path) / 1024
        print(f"  -> Generated: {os.path.relpath(pdf_path, workspace_dir)} ({file_size_kb:.1f} KB)")
        return True
    else:
        print(f"[ERROR] Output PDF not created: {pdf_path}")
        return False


def main():
    chrome_bin = find_chrome()
    if not chrome_bin:
        print("[ERROR] Could not find Google Chrome or Chromium binary.")
        sys.exit(1)

    workspace_dir = os.path.dirname(os.path.abspath(__file__))

    # Target files passed as CLI arguments, or default 4 files
    if len(sys.argv) > 1:
        target_files = sys.argv[1:]
    else:
        target_files = [os.path.join(workspace_dir, rel) for rel in DEFAULT_TARGET_FILES]

    success_count = 0
    for md_file in target_files:
        if convert_file(md_file, chrome_bin, workspace_dir):
            success_count += 1

    print(f"\nFinished: {success_count}/{len(target_files)} PDF(s) successfully created.")


if __name__ == "__main__":
    main()
