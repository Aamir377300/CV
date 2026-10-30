# Computer Vision — Teaching Notes (for the exam)

Use this with [STUDY-ORDER.md](./STUDY-ORDER.md).  
That file is **what to open, in which order**. This file is **the actual teaching**.

Read one section. Close the laptop. Say it out loud in your own words. If you cannot, read that section again. That is how you pass a theory paper.

The exam wants **definitions, why it exists, how it works, compare two things, give one example**. Code is extra.

---

## How to read this

Each topic has the same shape:

1. **The idea** — what it is, like I am telling you in class
2. **Why we need it**
3. **How it works**
4. **Write this in the paper** — a ready answer in simple English

Do Step 1 first. Do not jump to YOLO.

---

# STEP 1 — Image foundations

This is Module 1 and the start of Module 2. If this is weak, later CNN answers will sound empty.

---

## 1. What is Computer Vision?

A computer does not “see” a photo the way you do. You see a face, a car, a tree. The computer only sees **numbers**.

**Computer Vision** is the part of AI that turns those numbers into meaning: “this is a face”, “the car is here”, “this pixel is road”.

Used in: self-driving cars, medical scans, CCTV, phone unlock, AR filters.

**Write this in the paper:**  
*Computer Vision is a field of AI that enables machines to understand visual information from images or video. A digital image is stored as numbers. CV algorithms process those numbers to do tasks like classification, detection and segmentation.*

---

## 2. An image is a matrix of pixels

Imagine a chessboard. Each square is one **pixel** (picture element). Each pixel holds a number for brightness or color.

### Grayscale (black and white)

One number per pixel, usually **0 to 255**.

- `0` = black
- `255` = white
- `128` = gray

So a grayscale image is a **2D matrix**: rows × columns.  
A 3×3 grayscale image can look like:

```
  0   128  255
 64   192  128
255   255    0
```

Shape: `(height, width)` example `(5472, 3648)`.

### Color

A color pixel needs **three** numbers: Red, Green, Blue.  
So a color image is a **3D matrix**: height × width × **3 channels**.

Shape: `(height, width, 3)`.

Pure red in RGB is `[255, 0, 0]` (red full, green off, blue off) and similar for green and blue.

### Where is (0, 0)?

In maths, origin is often bottom-left. **In images, origin (0, 0) is the top-left.**

## Mathematics Coordinate System

```
        +y
         ↑           .
         |
         |
         |
(0,0) ───┼────────→ +x
```

- The origin **(0,0)** is at the **bottom-left**.
- **Bottom-left** only tells you **where the origin (starting point)** is. it is shown when you put your eyes at dot(no-concept just menomics).
- It **does NOT** tell you the direction of the x-axis.
- From the origin:
  - Move **right** → **+x**
  - Move **up** → **+y**

---

## Image Coordinate System

```
(0,0) ───┼────────→ +x
         |
         |
         |
         ↓       .
        +y
```

- The origin **(0,0)** is at the **top-left**.
- **Top-left** only tells you **where the origin (starting point)** is. it is shown when you put your eyes at dot.(no-concept just menomics).
- It has their own mathmatics system.
- Images use their **own coordinate system**:
  - Move **right** → **+x**
  - Move **down** → **+y**

---

## Remember for the Exam

- **"Bottom-left"** and **"Top-left"** describe **where (0,0) is located**, **not** the direction of the axes.
- The **x-axis always increases to the right**.
- The only difference is the **y-axis**:
  - **Mathematics:** +y is **up**.
  - **Images:** +y is **down**.
- `x` grows to the **right**
- `y` grows **down**

To read a pixel you use `image[y, x]` — row first, then column. That is why `image[5, 10]` is “5 down, 10 across”, not the other way.

**Why top-left?** Screens and files are stored row by row starting from the first row at the top. 👈 👈 👈

### OpenCV vs Matplotlib (very common viva)

# What is OpenCV?

**OpenCV (Open Source Computer Vision Library)** is a **software library** that helps computers **read, understand, process, and analyze images and videos**.

It provides **thousands of ready-made functions**, so you don't have to write image-processing algorithms from scratch.

**Features:**

- Open source (free to use)
- Cross-platform (Windows, Linux, macOS)
- Supports Python, C++, Java, and other languages

---

# What is the use of OpenCV?

OpenCV is used whenever you want a computer to **work with images or videos**.

### Common Uses

- Read and display an image
- Capture video from a webcam
- Resize, crop, or rotate images
- Convert a color image to grayscale
- Detect edges, corners, and shapes
- Detect faces, eyes, or objects
- Track moving objects in a video
- Preprocess images before giving them to a deep learning model

---

# What does OpenCV do?

Think of **OpenCV as a toolbox for images and videos**.

Just as **NumPy** provides ready-made functions for working with **arrays**, **OpenCV** provides ready-made functions for working with **images and videos**.

For example, with a single OpenCV function, you can:

- Read an image
- Convert it to grayscale
- Resize it
- Detect edges
- Detect faces

Instead of writing these algorithms yourself, you simply call OpenCV's built-in functions.

---

- **OpenCV** stores color as **BGR** (Blue, Green, Red).
- **Matplotlib** (and most websites) use **RGB**.

Same three numbers, different order. If you display an OpenCV image in Matplotlib without converting, red and blue look swapped.

**Write this in the paper:**  
*A grayscale image is a 2D matrix of intensities 0–255. A color image is a 3D matrix with 3 channels. Origin is at the top-left. OpenCV uses BGR; Matplotlib uses RGB.*

---

## 3. Color spaces: RGB vs HSV

**RGB** is how screens mix light: turn red, green, blue lamps up or down. Fine for display. Bad for “find all yellow fruit”, because yellow in shade and yellow in sun have very different RGB numbers.

### Explanation

- **RGB** creates colors by mixing different amounts of **Red, Green, and Blue** light. Every pixel on a screen uses these three colors to display any color.
- It is **excellent for displaying images** because screens naturally emit red, green, and blue light.
- However, RGB is **not reliable for color detection** because the RGB values of the **same object change with lighting**.
- For example, a yellow banana in **bright sunlight [255, 255, 50]**  and the **same banana in shade [120, 120, 20]** are both yellow to our eyes, but their RGB values can be very different.
- Therefore, if we search for a fixed RGB value to detect yellow objects, many yellow objects may be missed and create a confusion.

**Exam Tip:** RGB is best for **displaying colors**, but not ideal for **detecting colors under different lighting conditions**.

**HSV** splits color the way humans talk about it:

| Letter | Meaning | Think of it as |
|--------|---------|----------------|
| **H** Hue | Which color family | the angle on a color wheel (0° red, 120° green, 240° blue) |
| **S** Saturation | How pure / washed | 0% = gray, 100% = vivid |
| **V** Value | How bright | 0% = black, 100% = bright |

## Why do we need HSV?

RGB is excellent for **displaying colors**, but it is **not reliable for color detection**.

For example, suppose you want to detect a **yellow banana**.

- In bright sunlight, its RGB values might be:
  ```text
  (255, 255, 50)
  ```
- In shade, the **same banana** might have:
  ```text
  (120, 120, 20)
  ```

Although the banana is still **yellow**, its RGB values change a lot because the lighting changes. Therefore, detecting colors using RGB is difficult.

---

## How does HSV solve this problem?

HSV separates **color** from **brightness**.

Instead of storing only Red, Green, and Blue, it stores three different properties that is Hue, saturaton and value and each represent different things.

## Example

### Banana in bright sunlight

```text
Hue = Yellow
Saturation = High
Value = High (Bright)
```

### Same banana in shade

```text
Hue = Yellow
Saturation = High
Value = Low (Dark)
```

### What changed?

- ✅ Hue stayed **Yellow**.
- ✅ Saturation stayed almost the same.
- ✅ Only Value (brightness) changed.

Since the **Hue remains almost the same**, the computer can still recognize the banana as **yellow**, even when the lighting changes.

---

## Why is HSV better than RGB for color detection?

HSV separates the **color** from the **brightness**.

When lighting changes, **Value (brightness)** changes the most, while **Hue (the actual color)** remains nearly the same. Therefore, the computer can detect the same color under different lighting conditions more reliably than with RGB.

---

## Exam Definition

> **HSV (Hue, Saturation, Value) is a color model that separates color from brightness. Hue represents the color, Saturation represents the purity of the color, and Value represents the brightness. HSV is preferred for color than RGB detection because changes in lighting mainly affect the Value, while the Hue remains relatively stable.**

---

## 4. Image transformations

Sometimes you do not change *what* is in the picture. You only **move, resize, or warp** it. That is a geometric transform.

| Name            | What it does                                                                                                                                                                                | Everyday example                                         |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Translation** | Shift left/right/up/down                                                                                                                                                                    | sliding a photo on a table                               |
| **Scaling**     | Make bigger or smaller                                                                                                                                                                      | zoom                                                     |
| **Rotation**    | Turn around a point                                                                                                                                                                         | rotate 45° around the center                             |
| **Affine**      | Stretch / shear, but **parallel lines stay parallel**                                                                                                                                       | a rectangle can become a parallelogram                   |
| **Perspective** | Perspective Transformation changes the viewing angle of an image. It is mainly used to remove perspective distortion, such as converting a tilted document into a flat, scanned-like image. | document scanner: a tilted page becomes a flat rectangle |

Example for perspective:

Before (Tilted (Quad))          After (Flat (rectangle))

   ________              _________

  /               /             |                |

 /               /     ->    |                 |

/___/               |_____|

Affine needs **3 point pairs**. Perspective needs **4 point pairs** (the four corners of a page).

These are also used as **data augmentation** when training a CNN (random rotate/scale so the model does not memorize one pose).

**Write this in the paper:**  
*Translation shifts the image, scaling resizes it, rotation turns it. Affine preserves parallelism. Perspective maps a quadrilateral to another and is used in document scanning.*

---

## 5. Kernel (filter) — the most important small idea

A kernel (filter or convolution matrix) is a small matrix of numbers (usually 3×3 or 5×5) that slides over an image. At each position, it combines the center pixel and its neighboring pixels to calculate a new pixel value. Different kernels perform different operations such as blurring, sharpening, and edge detection.

A **kernel** is a tiny grid of numbers, usually 3×3 or 5×5. Other names: filter, mask, convolution matrix.

You place it on a pixel and its neighbors, multiply matching cells, **add them up**. That sum becomes the **new** pixel.

Same image + different kernel = completely different result:

| Kernel job | What it does |
|------------|----------------|
| Identity | leave the image as is |
| Box / average blur | mix neighbors → smooth, less noise |
| Gaussian blur | same idea, but center counts more than far neighbors |
| Sharpen | boost the center, subtract neighbors → edges look crisper |
| Sobel X | highlight **vertical** edges |
| Sobel Y | highlight **horizontal** edges |

Larger kernel (7×7 vs 3×3) looks at a **wider** neighborhood: stronger blur, slower, more context, less tiny detail.

In **traditional image processing**, we manually design the kernel values for a specific task, such as blurring, sharpening, or edge detection. In a **Convolutional Neural Network (CNN)**, we still use kernels, but **we do not choose their values ourselves**. Instead, the CNN **learns the best kernel values automatically from training data**. During training, it adjusts the kernel values to detect useful patterns such as edges, textures, shapes, and eventually complex objects like faces or cars. This is why CNNs are much more flexible and powerful than manually designed filters.

**Write this in the paper:**  
*A kernel is a small matrix that slides over an image. At each position we multiply overlapping values and sum them to get a new pixel. Different kernels produce blur, sharpen or edges. In CNNs, kernels are learned automatically to detect patterns.*

---

## 6. Convolution

Convolution is a mathematical operation where a small matrix (kernel) slides over the image, multiplying and summing pixel values to produce a new output. its purpose is to Extracts features such as edges, textures, or smoothness.

Different kernels do different jobs:

- Blur kernel → smooths the image
- Sharpen kernel → makes edges clearer
- Edge detection kernel → finds boundaries

**Convolution** is the name of that sliding process.

1. Put the kernel on the top-left of the image.
2. Multiply + add.
3. Store the result in the output.
4. Slide the kernel by a step (that step is later called **stride**).
5. Repeat until the whole image is covered.

The output is a **feature map** — a new image that highlights whatever the kernel cares about (smoothness, edges, …).

Formula you may be asked to write (2D convolution):

\[
(I * K)(x, y) = \sum_m \sum_n I(x - m,\ y - n) \cdot K(m, n)
\]

`I` is the image, `K` is the kernel. Do not panic: it only says “look at neighbors, weight them with K, add”.

**Write this in the paper:**  
*Convolution is a sliding-window operation. A kernel moves across the image, computes a weighted sum of local pixels, and produces a feature map. It is the foundation of both classical filtering and CNNs.*

---

## 7. Edges: Sobel and Canny

An **edge** is a place where brightness jumps (the outline of an object).

**Sobel** is a pair of kernels:

- Sobel X finds vertical edges (left vs right change)
- Sobel Y finds horizontal edges (up vs down change)

Together they give an edge map. Sobel is simple but a bit noisy.

**Canny** is a full recipe, not one kernel:

1. Blur a little (reduce noise)
2. Compute gradients (like Sobel)
3. Keep only the strongest pixel along the edge (non-max suppression)
4. Use **two thresholds**: strong edges are kept, weak edges are kept only if they touch a strong one

Result: cleaner, thinner edges. Used in lane detection, document outlines, medical boundaries.

**Write this in the paper:**  
*Edge detection finds pixels where intensity changes sharply. Sobel uses gradient kernels for horizontal and vertical edges. Canny combines smoothing, gradient, non-max suppression and double thresholding, so edges are cleaner.*

---

## 8. Histogram

A **histogram** counts how many pixels have each intensity from 0 to 255.

- X-axis: intensity (dark → bright)
- Y-axis: how many pixels

example

Intensity →

0                              255

 │ ██████████

 │ ██████

 │ ██

└──────────────────────────────

What you can read from it:

- Peak on the **left** → image is dark (underexposed)
- Peak on the **right** → image is bright (overexposed)
- **Narrow** peak → low contrast (washed / foggy)
- **Spread** across 0–255 → good contrast

It does not tell you *what* objects are in the photo. It only tells you about brightness and contrast. That is still enough to decide “should I enhance this?”

**Write this in the paper:**  
*A histogram shows the distribution of pixel intensities. It helps judge brightness and contrast. A left-shifted histogram is underexposed; a right-shifted one is overexposed; a narrow histogram means low contrast.*

---

## 9. Histogram equalization (thin in class notes — still asked)

Suppose most pixels sit between 40 and 90. The photo looks dull because it is not using the full 0–255 range.

**Histogram equalization** stretches those values across 0–255 so darks get darker and brights get brighter. Contrast improves. Details become easier to see. Often done **before** thresholding or feature detection.

Limit: it can also boost **noise**.

**Write this in the paper:**  
*Histogram equalization remaps intensities so they use the full 0–255 range, which improves contrast. It is useful as a preprocessing step but can amplify noise.*

---

## 10. Thresholding — turn gray into black and white

Thresholding converts a grayscale image into a black-and-white (binary) image by choosing a cutoff value called the threshold (T).

Process:

- If pixel intensity > threshold → set to white (255).
- If pixel intensity ≤ threshold → set to black (0).

example:

Grayscale pixels:

50   120   180   240

T = 127

After thresholding:

0     0    255   255

This removes gray shades and leaves only **black and white**, making objects easier to separate from the background.

# Types of Thresholding

## 1. Global Thresholding

A **single threshold (T)** is used for the **entire image**.

Example:

```text
Whole image → T = 127
```

It works well when the lighting is **uniform**. If one part of the image is bright and another part is dark, one threshold cannot correctly separate the object everywhere.

---

## 2. Adaptive Thresholding

Instead of using one threshold for the whole image, it **calculates a different threshold for each small region**.

Example:

```text
Bright area  → T = 150
Dark area    → T = 80
```

This works well when the image has **uneven lighting**, because each region gets its own suitable threshold.

---

## 3. Otsu's Method

In Otsu's method, **you do not choose the threshold**.

The computer **automatically finds the best threshold** that separates the image into **foreground (object)** and **background** as clearly as possible. It works best when the histogram has **two distinct peaks**, such as black text on a white page.

# Why is Thresholding Used?

Thresholding simplifies an image by removing unnecessary gray levels, making it easier to detect or analyze objects. It is commonly used in **document scanning**, **object detection**, and **medical image analysis**.

---

# Exam Tip

- **Thresholding:** Converts grayscale → black & white using a threshold **T**.
- **Global:** One threshold for the whole image.
- **Adaptive:** Different threshold for different regions.
- **Otsu:** Computer automatically chooses the best threshold.

**Write this in the paper:**  
*Thresholding converts grayscale to binary. Global uses one cutoff and fails under uneven light. Adaptive uses local cutoffs. Otsu automatically chooses T by minimizing intra-class variance. Used in document scanning and medical segmentation.*

---

## 11. Morphological operations — edit shapes, not colors

Work mainly on **binary** images. You take a small shape called a **structuring element** (square, ellipse, cross) and probe the image with it. Size of that element controls how strong the effect is. Bigger = stronger (and you can destroy thin objects if it is too big).

Think of a marker and an eraser on a drawing:

| Operation | Recipe | Effect | Use |
|-----------|--------|--------|-----|
| **Dilation** | expand white | thicker strokes, gaps close | connect broken letters |
| **Erosion** | shrink white | thinner, small dots die | remove specks |
| **Opening** | **erode then dilate** | specks gone, main shape kept | noisy scan |
| **Closing** | **dilate then erode** | holes inside objects fill | broken characters |

Opening vs closing is a favourite compare question. Remember the **order**.

**Write this in the paper:**  
*Morphological operations modify object shape using a structuring element. Dilation expands foreground, erosion shrinks it. Opening = erosion then dilation (remove noise). Closing = dilation then erosion (fill holes).*

---

## 12. Contours and shapes

After thresholding, a white blob has a **boundary**. That boundary curve is a **contour**.

From a contour you can compute:

- **Bounding box** — smallest upright rectangle around the object (used to *localise* “the object is here”)
- **Convex hull** — like putting a rubber band around the shape; no dents. Simplifies the outline.
- **Area, perimeter, centroid** — numbers you can use to classify “big vs small”, “round vs long”
- **Polygon approximation** (Douglas–Peucker): simplify the contour to a few corners.  
3 corners → triangle, 4 → rectangle, many → circle.

**Write this in the paper:**  
*A contour is a curve joining continuous boundary points of the same intensity. Bounding boxes localise objects. A convex hull is the smallest convex polygon enclosing the contour. Vertex count after approximation can classify shapes.*

---

# STEP 2 — Features, motion, face, first CNN

Rest of Module 2, Module 5 (face), start of Module 3 (CNN words).

---

## 13. Four core challenges of Computer Vision

The same real object can look totally different in a photo. That is why CV is hard. Memorise **four words + one example each**.

| Challenge | Meaning | Example |
|-----------|---------|---------|
| **Viewpoint** | camera angle changes the silhouette | a cup from the top is a circle; from the side it is a U-shape |
| **Illumination** | light changes brightness and color | a face in sun vs in a room |
| **Occlusion** | part of the object is hidden | a person behind a car |
| **Scale** | near looks big, far looks small | the same dog filling the frame vs in the distance |

Hand-crafted features (SIFT) and later CNNs are both attempts to survive these changes.

**Write this in the paper:**  
*Core CV challenges are viewpoint variation, illumination changes, occlusion and scale variation. A robust system must recognise the same object under these changes.*

---

## 14. What is a “feature”?

You cannot compare two photos pixel by pixel. If the camera moved 2 cm, almost every pixel changed, even if it is the same room.

So we pick **special places** that are likely to be found again: corners, blobs, distinctive textures. Those places are **keypoints**. Around each keypoint we write a list of numbers that describe the neighborhood. That list is the **descriptor**.

- **Keypoint** = *where* (x, y, sometimes scale and orientation)
- **Descriptor** = *what it looks like nearby* (a vector)

A good feature is:

- **Distinctive** — not confused with other places
- **Repeatable** — found again after rotate / scale / light change
- **Compact** — a short vector, not the whole image

**Write this in the paper:**  
*A feature is a distinctive, repeatable pattern. A keypoint marks its location. A descriptor encodes the local neighborhood as a vector so two images can be matched without comparing every pixel.*

---

## 15. Harris, SIFT, ORB, HOG

### Harris corners

A **corner** is where intensity changes in **two** directions (an edge changes in only one; a flat wall changes in none).

Harris looks at gradients in a window and scores “how corner-like”. Good on buildings and chessboards. **Not** invariant to scale or rotation: if you zoom, the window no longer matches.

### SIFT (Scale-Invariant Feature Transform)

The classic strong descriptor. Pipeline (learn this order):

1. Build a **Gaussian scale space** (blur the image at many scales)
2. Find **extrema in Difference of Gaussians** (DoG) — those are candidate keypoints
3. Assign an **orientation** from local gradients (so rotation can be undone)
4. Write a **128-dimensional** descriptor of the neighborhood

Strength: survives scale, rotation, a fair amount of light change.  
Limit: **slow / heavy**. (It was patented; now free in modern OpenCV.)

### ORB (Oriented FAST and Rotated BRIEF)

A **fast, free** alternative. Uses FAST to find corners, BRIEF as a binary descriptor, plus orientation.

Strength: real-time, good enough for panorama / AR on a phone.  
Limit: weaker than SIFT when scale change is large.

### HOG (Histogram of Oriented Gradients)

Not a sparse keypoint method. It describes a **region** (a whole pedestrian, a face window):

1. Compute gradients
2. Split into cells (e.g. 8×8)
3. In each cell, make a histogram of gradient **directions**
4. Normalise over bigger blocks (helps with lighting)

Used for **pedestrians and faces**. Interpretable and fairly light. Sensitive to **scale** (person must be roughly the expected size).

**Write this in the paper:**  
*Harris detects corners but is not scale/rotation invariant. SIFT detects and describes keypoints robust to scale and rotation using Gaussian scale space, DoG extrema, orientation and a 128-D descriptor; it is computationally heavy. ORB is a faster free alternative. HOG builds histograms of edge directions in cells and is used for pedestrian/face detection.*

---

## 16. Matching, homography, RANSAC

Once you have descriptors in image A and image B:

1. For each descriptor in A, find the nearest descriptor in B (FLANN is a fast approximate search).
2. **Lowe’s ratio test**: keep a match only if the best neighbor is *clearly* better than the second best. This drops ambiguous matches.
3. From good matches, estimate a **homography** — a 3×3 matrix that maps one plane onto the other (logo onto a billboard, left photo onto right photo for a panorama).
4. Many matches are still wrong. **RANSAC** repeatedly picks a small random subset, fits a homography, and keeps the fit that agrees with the most points. Outliers are ignored.

That is also how a **logo detector** draws a box in a scene.

**Write this in the paper:**  
*Image matching finds correspondences between descriptors. Homography maps one image plane to another. RANSAC estimates that transform robustly by ignoring outlier matches.*

---

## 17. Optical flow and tracking

**Optical flow** = apparent motion of pixels from one video frame to the next.

Assumption: a pixel’s brightness stays the same as it moves (brightness constancy). If lighting flashes, this breaks.

Two flavours:

- **Sparse:** track only some good points (usually corners). Cheap. **KLT / Lucas–Kanade** does this.
- **Dense:** a motion vector at **every** pixel (Farneback). Heavier, nice for visualising “what moved”.

**Object tracking** means follow a target across frames. You can detect every frame (YOLO) and link boxes, or track by motion (optical flow), or both (DeepSORT). Hard cases: occlusion, fast jumps, scale change, many similar objects.

**Write this in the paper:**  
*Optical flow estimates pixel motion between consecutive frames under brightness constancy. Sparse flow tracks selected keypoints (Lucas–Kanade / KLT). Dense flow computes motion at every pixel. It is sensitive to lighting changes, large displacements and occlusion.*

Skip stereo, epipolar geometry, Kalman filter for this mid-term unless they appear in a stray question. They are not in the module list.

---

## 18. Classical ML on images (kNN, SVM, Bag of Visual Words)

Before CNNs, we extracted features by hand, then gave a vector to a classifier.

**kNN:** look at the *k* nearest training examples; majority label wins. Simple, no real “training”, slow on big data.

**SVM:** find a **hyperplane** (a dividing line in high dimension) with the **largest margin** between classes. Strong when features are good.

**Bag of Visual Words (BoVW):** like a word-count for images.

1. Extract local descriptors (SIFT/ORB) from many images
2. Cluster them (k-means) → each cluster center is a **visual word**
3. For a new image, assign each descriptor to the nearest word and build a **histogram**
4. That fixed-length histogram goes into SVM/kNN

Useful background. For this paper, one clean definition of each is enough.

**Write this in the paper:**  
*kNN classifies by majority vote of nearest neighbours. SVM finds a maximum-margin hyperplane. Bag of Visual Words clusters local descriptors into a vocabulary and represents each image as a histogram of those visual words.*

---

## 19. Face detector (Module 5) — Haar vs HOG

**Face detection** = “is there a face, and where is the box?”  
It is **not** face *recognition* (who is this person). Detection comes first.

**Haar cascades**

- Haar features are simple rectangular patterns (bright vs dark strips), like cheap edge/face templates.
- **AdaBoost** picks the useful ones and stacks them as a **cascade**: easy “not a face” windows are rejected early, so it is fast.
- Good for **frontal** faces in decent light. Weak on pose, occlusion, hard lighting.

**HOG for faces / pedestrians**

- Uses gradient histograms (shape of the head/shoulders).
- More robust to illumination than Haar.
- Heavier / slower.

This is the syllabus “build a face detector” lab. For theory, compare Haar vs HOG: **speed vs robustness**.

**Write this in the paper:**  
*Haar-cascade detection uses rectangular Haar features selected by AdaBoost and a cascade classifier. It is fast for frontal faces but sensitive to pose and lighting. HOG captures gradient orientation histograms, so it is more robust to illumination but computationally heavier.*

---

## 20. Why CNN? Stride, padding, pooling, flatten

A normal neural net (fully connected) treats every pixel as a separate input. For a 200×200 color image that is 120,000 numbers going into huge weight matrices. It also **throws away** the fact that nearby pixels belong together.

A **CNN** reuses a small kernel across the image (weight sharing) and keeps spatial layout.

### Words you must be able to define

**Stride**  
How many pixels the kernel jumps. Stride 1 = dense. Stride 2 = skip, output is about half as wide/tall.

**Padding**  
Extra border (usually zeros) around the image so the kernel can sit on edge pixels. Without padding the image **shrinks** every convolution and edges are under-used. “Same” padding can keep width/height unchanged.

**Pooling**  
Summarise a small window of the feature map:

- **Max pool** = keep the largest value (strongest detection)
- **Average pool** = keep the mean

Pooling **reduces dimensions**, makes the net a bit robust to small shifts, and cuts compute.

**Flatten**  
After conv/pool you still have a 3D block (height × width × channels). Fully connected layers want a **1D vector**. Flatten is just reshape. It is the bridge from “spatial features” to “final class scores”.

**ReLU**  
Activation: negative → 0, positive stays. Makes the net non-linear (without it, stacked layers collapse to one linear map). Faster than sigmoid; helps vanishing gradients.

Typical flow:

```
Input → Conv → ReLU → Pool → Conv → ReLU → Pool → Flatten → Fully connected → class scores
```

Early conv layers learn edges and blobs. Deeper layers learn object parts and whole objects.

**Write this in the paper:**  
*CNNs use convolution so filters detect local patterns with few parameters. Stride is the kernel step size. Padding preserves border information and controls output size. Pooling downsamples feature maps (max or average). Flatten converts maps to a vector for the classifier.*

---

# STEP 3 — Deep CV (architectures, detect, segment)

Module 3 + Module 4. Highest exam weight.

---

## 21. The architecture lineage (very likely long answer)

Each famous CNN was invented to **fix a problem** the previous one had. Tell it as a story.

### LeNet (1998) — Yann LeCun

Small network: conv → pool → fully connected. Trained on **MNIST** handwritten digits.

**Problem it solved:** proved CNNs work better than old ML on images. Used in banks for reading cheques. Proof of concept.

### AlexNet (2012)

Won **ImageNet** by a huge margin. 5 conv + 3 FC. Trained with **GPUs**.

Three ideas that stuck:

- **ReLU** instead of sigmoid/tanh → faster training, less vanishing gradient
- **Dropout** → randomly turn off neurons while training so the net cannot memorise
- **GPU** → finally possible to train this size

**Problem it solved:** “deep vision doesn’t scale.” After AlexNet, everyone used deep CNNs. Accuracy jumped (roughly ~70% → ~85%+ on that challenge).

### VGG (2014)

Very deep (16 or 19 layers) but **simple**: stack many **3×3** filters instead of one large filter.

Why small filters? Two 3×3 layers have a similar view as one 5×5, but more non-linearities and fewer parameters. Showed **depth + simple design** is a winning recipe. Became the default backbone in papers.

**Problem it solved:** how to go deeper without a messy design. Limit: still very heavy (many parameters).

### ResNet (2015)

If you keep stacking layers, training **dies**: gradients vanish, accuracy can even get *worse*.

ResNet adds **skip / residual connections**. The layer learns a **residual** (the difference to add), and the original signal is copied forward:

```
output = F(x) + x
```

Gradients can flow along the skip path. Now 50, 101, even **152** layers train. Became the default for transfer learning and medical imaging.

**Problem it solved: vanishing gradients / degradation in very deep nets.**

### EfficientNet (2019)

People used to make a net only **deeper**, or only **wider**, or only higher **resolution**. That wastes compute.

EfficientNet uses **compound scaling**: scale depth, width and resolution together with one coefficient. High accuracy with fewer parameters. Good on **phones**.

**Problem it solved: unbalanced, inefficient scaling.**

### Transfer learning (Module 4)

ImageNet already taught a ResNet to see edges, textures, objects. For your small hospital dataset you **reuse** those weights:

- freeze early layers (generic features)
- train / replace the last layers on your data

You need less data and less time than training from scratch. That is “using pre-trained models”.

**Write this in the paper:**  
*LeNet proved CNNs on digits. AlexNet introduced ReLU, dropout and GPU training and started the deep-learning boom. VGG showed depth with stacked 3×3 filters. ResNet’s skip connections solved vanishing gradients so very deep nets could train. EfficientNet’s compound scaling balances depth, width and resolution. Transfer learning reuses a pre-trained backbone and adapts the last layers to a new task.*

---

## 22. Dropout and skip connections (two easy extra marks)

**Dropout:** during training, randomly set some neurons to 0 (e.g. 30%). The net cannot rely on one “lucky” neuron, so it learns redundant, more general features. At test time dropout is off. Analogy: a team where random members sit out, so everyone must know the play.

**Skip connections appear twice — say how they differ:**

- **ResNet:** skip is for **training depth** (gradient flow, learn residuals).
- **U-Net:** skip is for **detail**. Encoder compressed the image; skip brings the original edges back to the decoder so boundaries stay sharp.

**Write this in the paper:**  
*Dropout is regularisation: random neurons are ignored during training to reduce overfitting. ResNet skips help gradient flow. U-Net skips copy high-resolution features to the decoder for precise masks.*

---

## 23. Four vision tasks (do not mix them)

| Task | Output | Example |
|------|--------|---------|
| **Classification** | one label for the **whole** image | “this photo is a cat” |
| **Object detection** | **box + class** for each object | “cat here, dog there” |
| **Semantic segmentation** | a class for **every pixel**; two cars are the same label | road / car / sky map |
| **Instance segmentation** | every object separately, even two cars | car-1 mask, car-2 mask |

Image **generation** (GAN / diffusion) is a fifth family: make a **new** image, not a label.

---

## 24. Object detection: R-CNN family, YOLO, SSD

Detection must answer **what** and **where**.

### R-CNN (2014) — Region-based CNN

1. Propose thousands of possible boxes (regions)
2. Run a CNN **on each region**
3. Classify + refine the box

Very accurate. **Very slow** (thousands of CNN runs per image). Fine for offline medical reading. Not for a car that must react now.

**Faster R-CNN** adds a **Region Proposal Network (RPN)** so proposals are learned, not a slow external step. Still two-stage (propose, then classify).

### YOLO (2016) — You Only Look Once

Treat detection as **one regression**: one forward pass predicts all boxes and classes together. **Real-time**. Weaker on **tiny** objects (a far pedestrian can be missed). Choose YOLO for driving, sports, CCTV live view.

### SSD (2016) — Single Shot MultiBox Detector

Also one shot, but predicts from **several feature maps at different scales**, so small and large objects are handled together. Balance of speed and accuracy. Common on mobile.

**How to choose (they love this):**

- Medical / tumour: **accuracy first** → R-CNN family  
- Self-driving / live camera: **speed first** → YOLO (or SSD)

**Write this in the paper:**  
*R-CNN classifies region proposals with a CNN: accurate but slow. YOLO predicts boxes and classes in one pass: fast, weaker on small objects. SSD is a single-shot detector that uses multi-scale feature maps. Choose R-CNN when accuracy matters more than speed, YOLO/SSD when real-time is required.*

---

## 25. Semantic segmentation: FCN and U-Net

Classification says “cat”. Segmentation says **which pixels are the cat**.

Old CNNs ended with fully connected layers, which **flatten** and destroy “where”. **FCN (Fully Convolutional Network)** replaces those with convolutions so the output is a **map** the size of the image. First big idea. Limit: masks are **coarse**, boundaries fuzzy.

**U-Net (2015)** is the one you must draw in your head:

```
Encoder (down):  image → smaller maps, rich meaning   ("what")
Decoder (up):    small maps → full size again         ("where")
Skip connections: copy encoder details into decoder   (sharp edges)
```

Encoder compresses for **context**. Decoder expands for **location**. Skips bring back edges lost during downsampling. That is why U-Net dominates **medical** images (tumour, cell, organ): you need millimetre boundaries, not a rough box.

**Write this in the paper:**  
*Semantic segmentation labels every pixel. FCN outputs a dense map by using only convolutions, but boundaries can be coarse. U-Net uses an encoder-decoder with skip connections so context and fine detail are combined, which is why it is standard in medical imaging.*

---

## 26. Instance segmentation: Mask R-CNN

Detection gives a **rectangle**. A tumour is not a rectangle. Overlapping people are not rectangles.

**Mask R-CNN (2017)** = Faster R-CNN **plus** a small branch that predicts a **binary mask** per object.

Three outputs per object:

1. Bounding box
2. Class
3. Pixel mask

**RoI Align** (improved from RoI Pool) samples features without rounding error, so the mask sits on the object, not shifted by a few pixels.

Why masks beat boxes in medicine: exact shape, area/volume, overlapping organs. Also used in driving (pedestrian silhouette) and crowd scenes.

**Write this in the paper:**  
*Mask R-CNN extends Faster R-CNN with a mask branch. After RPN proposals, RoI Align extracts aligned features, then the model outputs box, class and a pixel-level mask. Masks give precise shape, which bounding boxes cannot.*

---

## 27. Video: CNN + LSTM (class extra — still in the question PDF)

One image has no “waving”. A wave is a **sequence**.

- **CNN** on each frame → *what* is in the picture (a hand)
- **RNN/LSTM** across those feature vectors → *how it changes* (the wave)

**RNN** remembers recent steps in a hidden state. On long videos it **forgets** (vanishing gradient).

**LSTM** adds **gates**:

- **Input gate** — what new info to store  
- **Forget gate** — what old info to drop  
- **Output gate** — what to send forward

So LSTM keeps long-term context and handles videos of different length. Pipeline: CNN per frame → sequence of vectors → LSTM → action class (clap, throw, walk).

**Write this in the paper:**  
*CNNs extract spatial features from each frame but not time. LSTMs model the sequence with input, forget and output gates, which reduces vanishing gradients compared with vanilla RNNs. Together they recognise actions and gestures.*

---

## 28. Vision Transformer (ViT) and attention (class extra)

CNN looks through a **small window**. To relate the top-left of a zebra to the bottom-right, you need many layers.

**Attention** (from NLP) compares every item with every other item:

- **Query (Q)** — what I am looking for  
- **Key (K)** — what each item is  
- **Value (V)** — the content to mix in

Similarity of Q with K gives weights. Weighted sum of V is the output. Related distant pixels can talk in **one** step.

**ViT:**

1. Cut the image into **patches** (e.g. 16×16), flatten each patch, treat it like a **word token**
2. Run a Transformer encoder (attention) on the sequence of patches
3. A special **class token** summarises the image for classification

Patches keep local detail. Attention across patches gives **global** context. Needs a lot of data to beat CNNs. Hybrid CNN+Transformer models exist.

**Write this in the paper:**  
*Attention uses Query, Key and Value to weight which parts of the input matter. ViT splits an image into patches, embeds them as tokens, and applies a transformer. This captures long-range relations that local CNN filters miss.*

---

# STEP 4 — Generate new images (GANs + diffusion)

Module 6, and “image generation” in Module 3.

---

## 29. GAN — two networks in a fight

A classifier says “this is a 7”. A **generative** model **draws** a new 7 that never existed.

A **GAN** (Generative Adversarial Network, Goodfellow 2014) trains **two** nets with opposite jobs:

| Network | Nickname | Input | Output |
|---------|----------|--------|--------|
| **Generator G** | forger / counterfeiter | random noise vector `z` | a fake image |
| **Discriminator D** | police / inspector | an image (real or fake) | probability it is real (0 to 1) |

G never copies a real photo directly. It only learns from D’s feedback. D sees real MNIST digits **and** G’s fakes.

Story over time:

- Round 1: G paints noise. D catches everything.  
- Later: G learns “digits have strokes”. D looks harder.  
- If it works: G’s images look real. D can only **guess** → output about **0.5**.

After training we usually **throw D away and keep G**. G is the artist.

**Minimax / adversarial / zero-sum:** D wants to maximise “I am right about real vs fake”. G wants to minimise that — it wants D to fail. One’s gain is the other’s loss. That is the **minimax objective**.

**Write this in the paper:**  
*A GAN has a generator that maps noise to images and a discriminator that scores real vs fake. They train adversarially with a minimax objective. At success, generated data matches real data and D outputs about 0.5. After training we keep the generator.*

---

## 30. Nash equilibrium, instability, mode collapse

This is not like training a classifier where loss calmly goes down. Here each net is chasing a **moving** target (the other net is also learning).

**Nash equilibrium:** a point where **neither** player can do better by changing **only themselves**. For a GAN that ideal point is: G’s distribution equals the real data, and D = ½ everywhere.

In practice gradients often **circle** that point instead of landing on it (like a penalty kick: if you always shoot left, the keeper learns left, so you switch, they switch, you spin).

**Mode collapse:** G finds **one** image (or one digit) that fools D and repeats it. Every sample looks OK, but **variety is dead**. D looks at one image at a time, so the loss does not punish “you only draw 1s”.

**Instability:** losses jump, quality can get worse if you train longer, tiny setting changes break the run. **Do not trust GAN loss as a quality meter.** You look at a grid of samples.

Fixes you only need to *name* if asked: label smoothing, instance noise, different learning rates, minibatch statistics to punish missing variety.

**Write this in the paper:**  
*GAN training is a game, so the Nash equilibrium (G matches data, D=0.5) is hard to reach and training can oscillate. Mode collapse is when G produces only a few kinds of samples. Instability means losses and image quality swing. Loss value alone does not measure sample quality.*

---

## 31. DCGAN and Conditional GAN

**DCGAN (Deep Convolutional GAN):** replace dense layers with **convolutions**.

- D uses strided conv to shrink the image (like a CNN classifier)
- G uses **transposed convolution** to grow noise into a full image
- Often with BatchNorm

Result: sharper, more structured pictures (digits with clean background instead of grey speckle). Same game as Class 1, better architecture.

**Conditional GAN (cGAN):** both G and D also receive a **label** `y` (for example digit class 7 as a one-hot vector). Then you can **ask** “draw a 7” instead of hoping a 7 appears. The training game is unchanged; extra input is the class.

**Write this in the paper:**  
*DCGAN uses convolutional G and D (transposed conv in G) for more stable, sharper images. A conditional GAN feeds a class label to both networks so generation can be controlled.*

---

## 32. Diffusion models (syllabus says “overview” — not in your slides)

Second family of image generators.

Start from **pure noise**. Learn to **remove a little noise**, many times, until a clean image appears. No forger-vs-police fight.

| | GAN | Diffusion |
|---|-----|-----------|
| How | two nets compete | denoise step by step |
| Stability | often unstable, mode collapse | usually more stable |
| Control | cGAN uses a label | can also follow text |
| Today | still taught | what most modern “AI image” tools use |

Four or five lines in the paper is enough unless the whole question is generation.

**Write this in the paper:**  
*Diffusion models generate images by iteratively denoising random noise. They are generally more stable than GANs and currently dominate high-quality image generation, while GANs use an adversarial generator-discriminator game.*

---

## 33. Multimodal AI (in the subject name, almost no lecture)

**Unimodal:** only images, or only text.  
**Multimodal:** **more than one type of data together** — usually image + text.

**CLIP**-style idea: train so that a photo and its caption land **near each other** in one shared space, and a wrong caption lands far away. Then you can:

- search images by typing words
- do classification without a fixed list of classes (“this is a MRI of a liver”)
- feed into captioning / vision-language models

A CNN classifier maps image → class id. A multimodal model maps **image and text into the same space**.

If the paper never asks this, you lose nothing. If one short question appears, the paragraph above is enough.

**Write this in the paper:**  
*Multimodal AI jointly understands different data types, typically vision and language. Models like CLIP embed images and text in a shared space so photos can be searched or classified with natural language.*

---

# Quick compare table (last-night revision)

| If they ask | Answer in one breath |
|-------------|----------------------|
| RGB vs HSV | RGB for screens; HSV for color detection under light change |
| Global vs adaptive vs Otsu | one T vs local T vs auto T by variance |
| Opening vs closing | erode→dilate (noise) vs dilate→erode (holes) |
| Harris vs SIFT vs ORB | corners / robust slow / fast cheap |
| Haar vs HOG face | fast frontal vs slower, better lighting |
| Classification vs detection vs segmentation | label / box / every pixel |
| Semantic vs instance | all cars same vs each car separate |
| R-CNN vs YOLO | accurate slow vs real-time |
| FCN vs U-Net | first pixel-map vs encoder-decoder + skips |
| ResNet skip vs U-Net skip | train deep vs restore edges |
| RNN vs LSTM | short memory vs gated long memory |
| CNN vs ViT | local filters vs global attention on patches |
| GAN vs diffusion | fight two nets vs denoise noise |
| DCGAN vs cGAN | conv architecture vs add a class label |

---

# Suggested use with internship

| Sitting | Read in this file |
|---------|-------------------|
| 1 | Sections 1–7 (pixels to edges) |
| 2 | Sections 8–12 (histogram to contours) then Week 1 questions |
| 3 | Sections 13–17 (challenges, features, flow) |
| 4 | Sections 18–20 (ML, face, CNN words) |
| 5 | Sections 21–22 (lineage) — write it from memory |
| 6 | Sections 23–26 (tasks, detect, segment) |
| 7 | Sections 27–28 if time (video, ViT) |
| 8 | Sections 29–33 (GAN + extras) then Week 2–3 questions |

After each sitting, write 8 lines **without looking**. That is the exam skill.

When you want the original teacher PDF, open the matching link in [STUDY-ORDER.md](./STUDY-ORDER.md). You do not need those PDFs first if you actually understand this file.
