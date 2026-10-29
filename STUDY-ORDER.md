# Computer Vision & Multimodal AI — Study Order

Simple self-study guide for mid-term.  
Focus: **only** this subject from [Mid-Term-Sem5_.pdf](./Syllabus/Mid-Term-Sem5_.pdf).

**Click any blue file name to open that PDF, notebook, or slide.**

The paper is **theory**. So you study in this order every time:

1. Read the **PDF / PPTX / notes**
2. Write the **Must remember** points in your own words
3. Open the `.ipynb` **only if** you want to see a picture of the idea  
   Do **not** run or debug code for the exam.

Finish one step before the next. Numbers = order.

---

## How this folder is arranged

| Folder | What is inside |
|--------|----------------|
| [01-Foundations-Week1/](./01-Foundations-Week1/) | Pixels, color, filters, edges, histogram, morphology, shapes |
| [02-Features-ML-CNN-Week2/](./02-Features-ML-CNN-Week2/) | SIFT/HOG, matching, optical flow, kNN/SVM, face detect, first CNN |
| [03-Deep-CV-Week3/](./03-Deep-CV-Week3/) | Famous CNNs, detection, segmentation, video, ViT |
| [04-GANs/](./04-GANs/) | How images are generated (theory slides + explainers) |
| [05-Practice-and-Project/](./05-Practice-and-Project/) | Viva / paper-style questions + project brief |
| [Syllabus/](./Syllabus/) | Full 5th sem mid-term syllabus (ignore other subjects) |
| [_archives/](./_archives/) | Old zip copies. **Do not open.** |

Ignore [_archives/](./_archives/) completely. Same notebooks are already renamed in folders 01–03.

---

## The full flow (one line)

```
pixels → color → filters/edges → histogram/morphology
    → SIFT/HOG + matching + optical flow
    → why CNN exists (conv, stride, pad, pool)
    → LeNet → AlexNet → VGG → ResNet → EfficientNet
    → classify → detect (R-CNN / YOLO) → segment (U-Net / Mask R-CNN)
    → generate (GAN + short diffusion)
    → face detector (Haar / HOG)
```

That is the correct story. Do not jump to YOLO or GAN first.

```text
Week 1 foundations          Week 2 features + first CNN
-----------------          ---------------------------
image = matrix             keypoints (Harris, SIFT, ORB)
RGB / HSV                  matching + HOG
kernel + convolution       optical flow
Sobel / Canny              Haar face detector
histogram + threshold      CNN words: stride, pad, pool
dilate / erode             (then Week 3 architectures)

Week 3 deep CV             Week 4 generation
--------------             -----------------
LeNet → EfficientNet       Generator vs Discriminator
R-CNN / YOLO / SSD         minimax, Nash, mode collapse
FCN / U-Net / Mask R-CNN   DCGAN + Conditional GAN
(CNN+LSTM, ViT = extra)    diffusion = 1-page overview
```

---

## What the syllabus actually asks

From **Computer Vision & Multimodal AI** only (pages 6–7 of [Mid-Term-Sem5_.pdf](./Syllabus/Mid-Term-Sem5_.pdf)):

| Module | Topic | Your step |
|--------|--------|-----------|
| 1 | Image representation, pixels, color spaces, classical CV | Step 1 |
| 2 | Convolution, blur/sharpen, Sobel/Canny, morphology, histogram equalization, SIFT, HOG, matching, optical flow, 4 core challenges | Steps 1–2 |
| 3 | CNN mechanics, classify, detect, segment, generate (GAN + diffusion) | Steps 3–4 |
| 4 | Transfer learning + LeNet → AlexNet → VGG → ResNet → EfficientNet | Step 3 |
| 5 | Face detector lab | Step 2 (theory of Haar + HOG) |
| 6 | GAN: G/D, minimax, Nash, mode collapse, DCGAN, Conditional GAN | Step 4 |

Subject name also says **Multimodal AI**, but the mid-term modules almost do not cover it. See **Missing topics** at the end.

---

## How to use a notebook (for a theory paper)

Each `.ipynb` has markdown headings like “What is SIFT?” and then code.

- Read the **headings and 4–5 bullet points**
- Look at one output picture if it is already there
- Close the file
- Do **not** install packages, fix errors, or train models

If a lab asks for extra files (`Ganesh3.jpg`, `chaplin.mp4`, webcam), skip that part.

---

# STEP 1 — Image foundations (Week 1)

**Syllabus:** Module 1 + start of Module 2  
**Time if busy:** 3–4 sittings

### Read in this order

| # | File | Why |
|---|------|-----|
| 1 | [00-Week1-KeyConcepts-READ-FIRST.pdf](./01-Foundations-Week1/00-Week1-KeyConcepts-READ-FIRST.pdf) | Best theory notes. **Read pages on pixels, HSV, kernel, convolution, histogram, threshold, morphology, contours, edges only.** Stop when it starts SIFT / SURF / HOG / stereo / optical flow / Kalman. Those belong to Step 2. |
| 2 | [00-Week1-Lectures-Days1-2-3.pdf](./01-Foundations-Week1/00-Week1-Lectures-Days1-2-3.pdf) | Same ideas as class Days 1–3 (pixels, color, transform, filter, Sobel, Canny). This file was wrongly sitting in the GAN folder. It is **not** GAN. |
| 3 | [07-Notes-Histograms-and-Thresholding.pdf](./01-Foundations-Week1/07-Notes-Histograms-and-Thresholding.pdf) | Histogram, global / adaptive / Otsu |
| 4 | [08-Notes-Morphological-Operations.pdf](./01-Foundations-Week1/08-Notes-Morphological-Operations.pdf) | Dilate, erode, open, close |
| 5 | [09-Notes-Contours-and-Shapes.pdf](./01-Foundations-Week1/09-Notes-Contours-and-Shapes.pdf) | Contours, box, convex hull |

### Must remember (exam)

- Grayscale = 2D matrix. Color = 3D matrix `(height, width, 3)`.
- Pixel 0 = black, 255 = white.
- Image origin `(0,0)` is **top-left**. Access is `image[y, x]`.
- OpenCV uses **BGR**. Matplotlib uses **RGB**.
- RGB pixel for pure red = `[255, 0, 0]`.
- **HSV** = Hue (which color), Saturation (how pure), Value (how bright). Better than RGB for color detection because light can change but hue stays more stable.
- **Kernel** = small matrix (3×3, 5×5) that slides over the image.
- **Convolution** = multiply kernel × neighborhood, then sum → new pixel. This is also how a CNN starts.
- Blur kernel = average neighbors. Sharpen = boost center. Sobel X = vertical edges. Sobel Y = horizontal edges.
- **Canny** = cleaner edges (gradient + two thresholds).
- Histogram = count of each intensity 0–255. Dark image piles left. Bright image piles right. Low contrast = narrow peak.
- **Histogram equalization** = stretch values across 0–255 to improve contrast. (Thin in notes — see Missing topics.)
- **Threshold** = pixel > T → white, else black.
  - Global = one T for whole image (fails if lighting is uneven).
  - Adaptive = different T per region.
  - Otsu = computer picks T by minimizing intra-class variance.
- **Dilation** = make white thicker. **Erosion** = make white thinner.
- **Opening** = erode then dilate → remove specks.
- **Closing** = dilate then erode → fill holes.
- Structuring element = the small shape used for morphology (square, ellipse, cross). Bigger size = stronger effect.
- Contour = boundary of a shape. Bounding box = rectangle around it. Convex hull = tight rubber-band around it.

### Optional glance (do not code)

| Notebook | Only if you want to see |
|----------|-------------------------|
| [01-Lab-Image-as-Matrix.ipynb](./01-Foundations-Week1/01-Lab-Image-as-Matrix.ipynb) | Image = numbers |
| [02-Lab-RGB-Color.ipynb](./01-Foundations-Week1/02-Lab-RGB-Color.ipynb) | RGB pixels |
| [03-Lab-Intro-Pixels-Color-Spaces.ipynb](./01-Foundations-Week1/03-Lab-Intro-Pixels-Color-Spaces.ipynb) | HSV |
| [04-Lab-Image-Transformations.ipynb](./01-Foundations-Week1/04-Lab-Image-Transformations.ipynb) | Translate, rotate, resize, affine, perspective |
| [05-Lab-Convolution-Explained.ipynb](./01-Foundations-Week1/05-Lab-Convolution-Explained.ipynb) | One 3×3 convolution by hand |
| [06-Lab-Filtering-and-Convolution.ipynb](./01-Foundations-Week1/06-Lab-Filtering-and-Convolution.ipynb) | Blur / sharpen / Sobel / Canny |
| [07-Lab-Histograms-and-Thresholding.ipynb](./01-Foundations-Week1/07-Lab-Histograms-and-Thresholding.ipynb) | Same as notes 07 |
| [08-Lab-Morphological-Operations.ipynb](./01-Foundations-Week1/08-Lab-Morphological-Operations.ipynb) | Same as notes 08 |
| [09-Lab-Contours-and-Shapes.ipynb](./01-Foundations-Week1/09-Lab-Contours-and-Shapes.ipynb) | Same as notes 09 |

[sample.jpg](./01-Foundations-Week1/sample.jpg) and [sample.png](./01-Foundations-Week1/sample.png) stay here only for those labs.

### Practice after Step 1

Use **one** of these (they are almost the same paper):

- [01-Week1-Questions.pdf](./05-Practice-and-Project/01-Week1-Questions.pdf)
- [01-Week1-Questions-v2.pdf](./05-Practice-and-Project/01-Week1-Questions-v2.pdf)

Answer in writing. Easy + Medium first. Then try Hard.

---

# STEP 2 — Features, motion, face, first CNN (Week 2)

**Syllabus:** rest of Module 2 + Module 5 + start of Module 3  
**Time if busy:** 3 sittings

### Read in this order

| # | File | Why |
|---|------|-----|
| 1 | Finish leftover pages of [00-Week1-KeyConcepts-READ-FIRST.pdf](./01-Foundations-Week1/00-Week1-KeyConcepts-READ-FIRST.pdf) | Corners, SIFT, SURF, HOG, optical flow. Skip stereo / epipolar / Kalman (not in mid-term syllabus). |
| 2 | [00-Week2-KeyConcepts-READ-FIRST.pdf](./02-Features-ML-CNN-Week2/00-Week2-KeyConcepts-READ-FIRST.pdf) | **Main theory file for this step.** Features → matching → flow → kNN/SVM → BoVW → Haar/HOG face → CNN words. |

Then open notebooks **only to read the theory cells** at the top (usually 1 screen):

| # | File | Theory you need |
|---|------|-----------------|
| 3 | [01-Lab-Feature-Detection-SIFT-ORB.ipynb](./02-Features-ML-CNN-Week2/01-Lab-Feature-Detection-SIFT-ORB.ipynb) | Harris vs SIFT vs ORB |
| 4 | [02-Lab-Image-Matching.ipynb](./02-Features-ML-CNN-Week2/02-Lab-Image-Matching.ipynb) | Descriptor + matching + homography idea |
| 5 | [03-Lab-Optical-Flow-and-Tracking.ipynb](./02-Features-ML-CNN-Week2/03-Lab-Optical-Flow-and-Tracking.ipynb) | Sparse vs dense flow, KLT |
| 6 | [04-Lab-Classical-ML-kNN-SVM.ipynb](./02-Features-ML-CNN-Week2/04-Lab-Classical-ML-kNN-SVM.ipynb) | kNN = neighbors vote. SVM = best dividing line |
| 7 | [05-Lab-Bag-of-Visual-Words.ipynb](./02-Features-ML-CNN-Week2/05-Lab-Bag-of-Visual-Words.ipynb) | Features → visual words → histogram |
| 8 | [06-Lab-Face-Detection-Haar-HOG.ipynb](./02-Features-ML-CNN-Week2/06-Lab-Face-Detection-Haar-HOG.ipynb) | **Module 5.** Haar cascade vs HOG |
| 9 | [07-Lab-CNN-Basics-MNIST.ipynb](./02-Features-ML-CNN-Week2/07-Lab-CNN-Basics-MNIST.ipynb) | Conv → pool → flatten → dense |

### Must remember (exam)

**Features**

- Feature = a distinctive point or pattern you can find again in another image.
- Good feature: unique, repeatable (survives scale / rotate / light), compact.
- **Harris:** corners (intensity changes in 2 directions). Simple. Not scale/rotation invariant.
- **SIFT:** scale + rotation invariant. Pipeline: Gaussian scale space → DoG extrema → orientation → 128-D descriptor. Strong but slow.
- **ORB:** fast free alternative (FAST + BRIEF + orientation). Weaker on big scale change.
- **HOG:** histogram of edge directions in small cells. Used for pedestrians / faces. Sensitive to scale.
- Keypoint = where. Descriptor = the number vector that describes the neighborhood.
- Matching = compare descriptors. Homography = map one plane onto another. RANSAC = ignore bad matches.

**Motion**

- Optical flow = apparent pixel motion between two frames. Assumes brightness stays the same.
- Sparse flow = only some points (faster). Dense flow = every pixel (more detail).
- Lucas–Kanade / KLT = track good corners frame to frame.
- Fails on big jumps, light change, occlusion.

**CV core challenges (Module 2 — memorize with 1 example each)**

| Challenge | Meaning | Example |
|-----------|---------|---------|
| Viewpoint | Same object looks different from another angle | A cup from top vs side |
| Illumination | Light changes brightness / color | Face in sun vs shadow |
| Occlusion | Object is partly hidden | Person behind a car |
| Scale | Near = big, far = small | Same dog close vs far |

**Face detector (Module 5)**

- Haar: fast rectangular patterns + AdaBoost cascade. Good for frontal faces. Weak on pose / light.
- HOG: gradient shape. Slower, more robust to light.

**Why CNN (start of Module 3)**

- Fully connected net on a big image = too many weights, loses “nearby pixels matter”.
- Convolution keeps local structure. Same filter is reused everywhere.
- **Stride** = step size of the kernel. Bigger stride → smaller output.
- **Padding** = extra border so edges are not lost and size can stay same.
- **Max pool** = keep strongest value in a window. **Avg pool** = average.
- Pooling shrinks maps, adds a little shift-invariance, reduces compute.
- **Flatten** = turn feature maps into one long vector for the last classifier.
- Flow: Input → Conv → Activation (ReLU) → Pool → Flatten → Fully connected → Output.

kNN / SVM / BoVW are useful background. For this paper, one definition each is enough.

---

# STEP 3 — Deep CV tasks (Week 3)

**Syllabus:** Module 3 + Module 4  
**Time if busy:** 4 sittings. Do 3A then 3B. ViT / video last.

### 3A — Architectures + transfer learning (must)

**Read first:** [00-Week3-KeyConcepts-READ-FIRST.pdf](./03-Deep-CV-Week3/00-Week3-KeyConcepts-READ-FIRST.pdf)  
(pages on LeNet, AlexNet, VGG, ReLU, Dropout, ResNet, EfficientNet)

**Must remember — lineage (Module 4). This is a very likely long answer.**

| Model | Year | What it did | Problem it solved |
|-------|------|-------------|-------------------|
| **LeNet** | 1998, Yann LeCun | Conv → Pool → FC on **MNIST** digits | First proof CNN beats old ML on images |
| **AlexNet** | 2012 | 5 conv + 3 FC, won ImageNet | **ReLU**, **Dropout**, **GPU**. Started the deep-learning boom |
| **VGG** | 2014 | 16–19 layers, only **3×3** filters stacked | Showed **depth** + simple design works |
| **ResNet** | 2015 | Skip / residual connections | **Vanishing gradient** — can train 50–152 layers |
| **EfficientNet** | 2019 | Compound scaling of depth + width + resolution | High accuracy with fewer parameters (mobile) |

- Transfer learning = take a model trained on a big set (ImageNet), freeze early layers, train the last part on your small data.
- ReLU: negative → 0, positive stays. Faster than sigmoid, helps vanishing gradient.
- Dropout: randomly turn off neurons while training so the net does not memorize.

Glance (theory cells only):  
[01-Lab-CNN-Architectures-LeNet-AlexNet-VGG.ipynb](./03-Deep-CV-Week3/01-Lab-CNN-Architectures-LeNet-AlexNet-VGG.ipynb)  
[02-Lab-Modern-CNNs-ResNet-EfficientNet.ipynb](./03-Deep-CV-Week3/02-Lab-Modern-CNNs-ResNet-EfficientNet.ipynb)

### 3B — Detect and segment (must)

Same Week 3 PDF: [00-Week3-KeyConcepts-READ-FIRST.pdf](./03-Deep-CV-Week3/00-Week3-KeyConcepts-READ-FIRST.pdf) — object detection, FCN, U-Net, Mask R-CNN.

| Task | Output | Landmark models |
|------|--------|-----------------|
| Classification | one label for whole image | CNN / ResNet / EfficientNet |
| Detection | box + class | R-CNN family, YOLO, SSD |
| Semantic segmentation | class for **every pixel** (all cars = same color) | FCN, U-Net |
| Instance segmentation | every object separately, even two cars | Mask R-CNN |

**Detection**

- **R-CNN:** propose many regions → CNN on each → classify. Accurate, **very slow**.
- Faster R-CNN adds a Region Proposal Network (RPN).
- **YOLO (You Only Look Once):** one pass, boxes + classes together. **Fast / real-time.** Weaker on tiny objects.
- **SSD:** one shot, many feature-map scales. Balance of speed and size.
- Medical imaging → accuracy first → R-CNN family.  
  Self-driving → speed first → YOLO / SSD.

**Segmentation**

- FCN: replace last dense layers with conv so you get a pixel map. First idea. Boundaries are coarse.
- **U-Net:** encoder (what) + decoder (where) + **skip connections** (bring edges back). Standard in medical images.
- **Mask R-CNN:** Faster R-CNN + a mask branch. Outputs **box + class + pixel mask**. Uses **RoI Align** (more precise than RoI Pool).
- Why masks beat boxes in medicine: exact shape, area/volume, overlapping organs.

Glance:  
[03-Lab-Object-Detection-RCNN-YOLO.ipynb](./03-Deep-CV-Week3/03-Lab-Object-Detection-RCNN-YOLO.ipynb)  
[04-Lab-Semantic-Segmentation-UNet.ipynb](./03-Deep-CV-Week3/04-Lab-Semantic-Segmentation-UNet.ipynb)  
[05-Lab-Instance-Segmentation-MaskRCNN.ipynb](./03-Deep-CV-Week3/05-Lab-Instance-Segmentation-MaskRCNN.ipynb)

### 3C — Class extras (in notes + question PDF, not a named syllabus bullet)

Do these **after** 3A and 3B.

| File | Remember this much |
|------|--------------------|
| [00-Week3-KeyConcepts-READ-FIRST.pdf](./03-Deep-CV-Week3/00-Week3-KeyConcepts-READ-FIRST.pdf) + [06-Lab-Video-CNN-LSTM.ipynb](./03-Deep-CV-Week3/06-Lab-Video-CNN-LSTM.ipynb) | CNN sees **what** is in a frame. LSTM sees **how it changes**. LSTM gates: input / forget / output. RNN forgets long sequences (vanishing gradient). |
| [00-Week3-KeyConcepts-READ-FIRST.pdf](./03-Deep-CV-Week3/00-Week3-KeyConcepts-READ-FIRST.pdf) + [07-Lab-ViT-Patches-Demo.ipynb](./03-Deep-CV-Week3/07-Lab-ViT-Patches-Demo.ipynb) + [08-Lab-CNN-vs-ViT-Attention.ipynb](./03-Deep-CV-Week3/08-Lab-CNN-vs-ViT-Attention.ipynb) + [09-Lab-Vision-Transformer-CIFAR10.ipynb](./03-Deep-CV-Week3/09-Lab-Vision-Transformer-CIFAR10.ipynb) | Split image into patches = tokens. Attention uses Query, Key, Value. CNN = local. ViT = global relations. |

### Practice after Steps 2–3

[02-Week2-and-Week3-Questions.pdf](./05-Practice-and-Project/02-Week2-and-Week3-Questions.pdf)

This PDF is very close to a real theory paper. Write answers. Do not skip the Mask R-CNN / LSTM / ViT questions at the end.

---

# STEP 4 — GANs (generative models)

**Syllabus:** Module 6 + “image generation” in Module 3  
**Time if busy:** 2 sittings

There are **no GAN notebooks** in your downloads. That is fine for a theory paper. Use slides + the Word explainers.

| # | File | What to take |
|---|------|--------------|
| 1 | [01-Class1-GAN-Basics.pptx](./04-GANs/01-Class1-GAN-Basics.pptx) | G, D, adversarial game, minimax |
| 2 | [01-Class1-Notebook-Explained.docx](./04-GANs/01-Class1-Notebook-Explained.docx) | Same story in plain words. Read sections 1–2 (idea + words). Skip line-by-line code. |
| 3 | [02-Class2-3-Training-Dynamics.pptx](./04-GANs/02-Class2-3-Training-Dynamics.pptx) | Nash equilibrium, instability, mode collapse |
| 4 | [02-Class2-3-Notebook-Explained.docx](./04-GANs/02-Class2-3-Notebook-Explained.docx) | Same, plain words. Read “big picture” + word list. |
| 5 | [03-Class4-DCGAN-and-Conditional-GAN.pptx](./04-GANs/03-Class4-DCGAN-and-Conditional-GAN.pptx) | DCGAN + Conditional GAN |
| 6 | [03-Class4-Notebook-Explained.docx](./04-GANs/03-Class4-Notebook-Explained.docx) | Same. Read “big picture” + word list. |

### Must remember (exam)

- **Generator (G):** random noise `z` in → fake image out.
- **Discriminator (D):** image in → probability it is real.
- They train as opponents (forger vs police). This is **adversarial**.
- **Minimax:** D wants to catch fakes. G wants to fool D.
- At the ideal end (**Nash equilibrium**): G’s images match real data, and D outputs about **0.5** (only guessing). Nobody can improve by changing only themselves.
- After training we usually **keep only G**.
- **Mode collapse:** G finds one image D likes and repeats it. Variety dies.
- **Instability:** losses jump, quality can get worse, small setting changes break training. GAN loss is a **moving target**, so loss number ≠ image quality.
- **DCGAN:** G and D use convolutions (not only dense layers). G uses transposed conv to grow the image. Cleaner pictures.
- **Conditional GAN (cGAN):** both G and D also get a **label** (example: digit 7), so you can ask for a class.

**Diffusion (syllabus says “overview” — not in your files):**  
GAN = two nets fight. Diffusion = start from noise and slowly remove noise until an image appears. Diffusion is usually more stable and is what most modern image generators use. One paragraph is enough. See Missing topics.

---

# STEP 5 — Questions, then project

| File | When |
|------|------|
| [01-Week1-Questions.pdf](./05-Practice-and-Project/01-Week1-Questions.pdf) | After Step 1 |
| [02-Week2-and-Week3-Questions.pdf](./05-Practice-and-Project/02-Week2-and-Week3-Questions.pdf) | After Step 3 |
| [03-CV-Project-Assignment.pdf](./05-Practice-and-Project/03-CV-Project-Assignment.pdf) | After Step 3 (and Step 4 if the idea needs generation) |

Project choices (pick one if you still need to submit):

1. Face recognition door system  
2. License-plate OCR  
3. Classroom attendance by face  

The brief date was **20 October**. If that is already over, still keep the PDF so you know what they wanted.

---

## Suggested pace (internship weeks)

| Your week | Do this | Exam weight |
|-----------|---------|-------------|
| A | Step 1 + Week 1 questions | High |
| B | Step 2 (features, flow, face, CNN words) | High |
| C | Step 3A + 3B (lineage, detect, segment) | Highest |
| D | Step 4 GANs + Step 3C extras + Week 2–3 questions | High |

Do not skip 1 → 2 → 3. GAN needs CNN words first.

Daily habit that works with internship: **45–60 minutes**. One PDF section + write 8 bullets. That is enough.

---

## Missing or weak vs syllabus

These are in the syllabus (or in the subject name), but your downloads are thin. Short notes so you can still write answers.

### 1. Histogram equalization (Module 2)

**Not a full lecture.** Questions already ask it in [01-Week1-Questions.pdf](./05-Practice-and-Project/01-Week1-Questions.pdf).

- Problem: a dark or washed image uses only a small part of 0–255.
- Equalization spreads intensities across the full range.
- Result: more contrast, details easier to see.
- Used before thresholding or feature detection.
- Limit: it can also boost noise.

One line you can write: *“Histogram equalization remaps pixel intensities so they use the full range, which improves contrast.”*

### 2. CV core challenges (Module 2)

No separate file. Memorize the 4 words from Step 2: **viewpoint, illumination, occlusion, scale.**  
That is the whole topic.

### 3. Diffusion models (Module 3)

Not in your GAN slides.

| | GAN | Diffusion |
|---|-----|-----------|
| Idea | G fakes, D judges | Noise → step-by-step denoise |
| Stability | Often unstable, mode collapse | Usually more stable |
| Control | cGAN uses a label | Can also be guided by text |
| Today | Still taught, used in some apps | Main method for high-quality images |

Write 4–5 lines, not a full essay, unless the question is only on generation.

### 4. Multimodal AI (subject name, almost no notes)

Mid-term modules 1–6 do **not** list CLIP. Still prepare 8 lines because the paper title includes it.

- Multimodal = one model that understands **more than one kind of data** (image + text, or image + audio).
- Example: **CLIP** learns to match a photo with the right caption.
- Use: search images by typing words, image captioning, vision-language models.
- Difference from CNN classify: CNN maps image → class name. Multimodal maps image and text into a **shared space**.

If the paper ignores it, you lose nothing. If one short question appears, this is enough.

### 5. GAN lab notebooks

Slides mention `CV-Week4-Lecture1.ipynb`, `GAN-Class-2-3-Training-Dynamics.ipynb`, `GAN-Class-4-DCGAN-cGAN.ipynb`.  
**You do not have them.** Ask a classmate or faculty if you want to run code. For theory, use [01-Class1-GAN-Basics.pptx](./04-GANs/01-Class1-GAN-Basics.pptx) and the `.docx` files in [04-GANs/](./04-GANs/).

### 6. Extra assets for Week 2 labs

Labs mention images/videos that are not in the folder. Ignore. You are not coding for the paper.

### 7. Topics in Week 1 KeyConcepts that you can skip

In [00-Week1-KeyConcepts-READ-FIRST.pdf](./01-Foundations-Week1/00-Week1-KeyConcepts-READ-FIRST.pdf), skip stereo vision, epipolar geometry, Kalman filter, SURF (except “faster SIFT”).  
They are **not** in the mid-term module list.

---

## Old names → new names

Use only the new names. Old Drive / zip names are in [_archives/](./_archives/).  
Click the **New** name to open the file.

### Week 1

| Old | New |
|-----|-----|
| `CV-Week-1-KeyConcepts.pdf` | [00-Week1-KeyConcepts-READ-FIRST.pdf](./01-Foundations-Week1/00-Week1-KeyConcepts-READ-FIRST.pdf) |
| `CV-Week-1-Lectures.pdf` (was wrongly named GAN basics PDF) | [00-Week1-Lectures-Days1-2-3.pdf](./01-Foundations-Week1/00-Week1-Lectures-Days1-2-3.pdf) |
| `imagerepresentation.ipynb` | [01-Lab-Image-as-Matrix.ipynb](./01-Foundations-Week1/01-Lab-Image-as-Matrix.ipynb) |
| `colorimgrepresent.ipynb` | [02-Lab-RGB-Color.ipynb](./01-Foundations-Week1/02-Lab-RGB-Color.ipynb) |
| `CV-Week1-Day1.ipynb` | [03-Lab-Intro-Pixels-Color-Spaces.ipynb](./01-Foundations-Week1/03-Lab-Intro-Pixels-Color-Spaces.ipynb) |
| `CV-Week1-Day2.ipynb` | [04-Lab-Image-Transformations.ipynb](./01-Foundations-Week1/04-Lab-Image-Transformations.ipynb) |
| `Convolution.ipynb` | [05-Lab-Convolution-Explained.ipynb](./01-Foundations-Week1/05-Lab-Convolution-Explained.ipynb) |
| `CV-Week1-Day3.ipynb` | [06-Lab-Filtering-and-Convolution.ipynb](./01-Foundations-Week1/06-Lab-Filtering-and-Convolution.ipynb) |
| Day 4 notebook + PDF | [07-Lab-Histograms-and-Thresholding.ipynb](./01-Foundations-Week1/07-Lab-Histograms-and-Thresholding.ipynb) + [07-Notes-Histograms-and-Thresholding.pdf](./01-Foundations-Week1/07-Notes-Histograms-and-Thresholding.pdf) |
| Day 5 notebook + PDF | [08-Lab-Morphological-Operations.ipynb](./01-Foundations-Week1/08-Lab-Morphological-Operations.ipynb) + [08-Notes-Morphological-Operations.pdf](./01-Foundations-Week1/08-Notes-Morphological-Operations.pdf) |
| Day 6 notebook + PDF | [09-Lab-Contours-and-Shapes.ipynb](./01-Foundations-Week1/09-Lab-Contours-and-Shapes.ipynb) + [09-Notes-Contours-and-Shapes.pdf](./01-Foundations-Week1/09-Notes-Contours-and-Shapes.pdf) |

### Week 2

| Old | New |
|-----|-----|
| `CV-Week-2-KeyConcepts.pdf` | [00-Week2-KeyConcepts-READ-FIRST.pdf](./02-Features-ML-CNN-Week2/00-Week2-KeyConcepts-READ-FIRST.pdf) |
| `CV-Week2-Lecture1.ipynb` | [01-Lab-Feature-Detection-SIFT-ORB.ipynb](./02-Features-ML-CNN-Week2/01-Lab-Feature-Detection-SIFT-ORB.ipynb) |
| `CV-Week2-Lecture2.ipynb` | [02-Lab-Image-Matching.ipynb](./02-Features-ML-CNN-Week2/02-Lab-Image-Matching.ipynb) |
| `CV-Week2-Lecture3.ipynb` | [03-Lab-Optical-Flow-and-Tracking.ipynb](./02-Features-ML-CNN-Week2/03-Lab-Optical-Flow-and-Tracking.ipynb) |
| `CV-Week2-Lecture4.ipynb` | [04-Lab-Classical-ML-kNN-SVM.ipynb](./02-Features-ML-CNN-Week2/04-Lab-Classical-ML-kNN-SVM.ipynb) |
| `CV-Week2-Lecture5.ipynb` | [05-Lab-Bag-of-Visual-Words.ipynb](./02-Features-ML-CNN-Week2/05-Lab-Bag-of-Visual-Words.ipynb) |
| `CV-Week2-Lecture6.ipynb` | [06-Lab-Face-Detection-Haar-HOG.ipynb](./02-Features-ML-CNN-Week2/06-Lab-Face-Detection-Haar-HOG.ipynb) |
| `CV-Week2-Lecture7.ipynb` | [07-Lab-CNN-Basics-MNIST.ipynb](./02-Features-ML-CNN-Week2/07-Lab-CNN-Basics-MNIST.ipynb) |

### Week 3

| Old | New |
|-----|-----|
| `CV-Week3-KeyConcepts.pdf` | [00-Week3-KeyConcepts-READ-FIRST.pdf](./03-Deep-CV-Week3/00-Week3-KeyConcepts-READ-FIRST.pdf) |
| `CV-Week3-Lecture1.ipynb` | [01-Lab-CNN-Architectures-LeNet-AlexNet-VGG.ipynb](./03-Deep-CV-Week3/01-Lab-CNN-Architectures-LeNet-AlexNet-VGG.ipynb) |
| `CV-Week3-Lecture2.ipynb` | [02-Lab-Modern-CNNs-ResNet-EfficientNet.ipynb](./03-Deep-CV-Week3/02-Lab-Modern-CNNs-ResNet-EfficientNet.ipynb) |
| `CV-Week3-Lecture3.ipynb` | [03-Lab-Object-Detection-RCNN-YOLO.ipynb](./03-Deep-CV-Week3/03-Lab-Object-Detection-RCNN-YOLO.ipynb) |
| `CV-Week3-Lecture4.ipynb` | [04-Lab-Semantic-Segmentation-UNet.ipynb](./03-Deep-CV-Week3/04-Lab-Semantic-Segmentation-UNet.ipynb) |
| `CV-Week3-Lecture5.ipynb` | [05-Lab-Instance-Segmentation-MaskRCNN.ipynb](./03-Deep-CV-Week3/05-Lab-Instance-Segmentation-MaskRCNN.ipynb) |
| `CV-Week3-Lecture6.ipynb` | [06-Lab-Video-CNN-LSTM.ipynb](./03-Deep-CV-Week3/06-Lab-Video-CNN-LSTM.ipynb) |
| `CV-Week3-vit1.ipynb` | [07-Lab-ViT-Patches-Demo.ipynb](./03-Deep-CV-Week3/07-Lab-ViT-Patches-Demo.ipynb) |
| `CV-Week3-vit2.ipynb` | [08-Lab-CNN-vs-ViT-Attention.ipynb](./03-Deep-CV-Week3/08-Lab-CNN-vs-ViT-Attention.ipynb) |
| `CV-Week3-Lecture7.ipynb` | [09-Lab-Vision-Transformer-CIFAR10.ipynb](./03-Deep-CV-Week3/09-Lab-Vision-Transformer-CIFAR10.ipynb) |

### GANs and practice

| Old | New |
|-----|-----|
| `GAN_Class_1 Basics.pptx` | [01-Class1-GAN-Basics.pptx](./04-GANs/01-Class1-GAN-Basics.pptx) |
| `GAN-Class-1.docx` | [01-Class1-Notebook-Explained.docx](./04-GANs/01-Class1-Notebook-Explained.docx) |
| Class 2–3 pptx + Notes.docx | [02-Class2-3-Training-Dynamics.pptx](./04-GANs/02-Class2-3-Training-Dynamics.pptx) + [02-Class2-3-Notebook-Explained.docx](./04-GANs/02-Class2-3-Notebook-Explained.docx) |
| Class 4 pptx + notebook explained | [03-Class4-DCGAN-and-Conditional-GAN.pptx](./04-GANs/03-Class4-DCGAN-and-Conditional-GAN.pptx) + [03-Class4-Notebook-Explained.docx](./04-GANs/03-Class4-Notebook-Explained.docx) |
| Week 1 / Week 2–3 question PDFs + project | [01-Week1-Questions.pdf](./05-Practice-and-Project/01-Week1-Questions.pdf) · [02-Week2-and-Week3-Questions.pdf](./05-Practice-and-Project/02-Week2-and-Week3-Questions.pdf) · [03-CV-Project-Assignment.pdf](./05-Practice-and-Project/03-CV-Project-Assignment.pdf) |

---

## Start today

Open only these two files:

1. [00-Week1-KeyConcepts-READ-FIRST.pdf](./01-Foundations-Week1/00-Week1-KeyConcepts-READ-FIRST.pdf)  
   (stop before SIFT)
2. Then [00-Week1-Lectures-Days1-2-3.pdf](./01-Foundations-Week1/00-Week1-Lectures-Days1-2-3.pdf)

Write answers for the first 15 easy questions in  
[01-Week1-Questions.pdf](./05-Practice-and-Project/01-Week1-Questions.pdf).

That is the correct start. Everything else follows the step numbers.
