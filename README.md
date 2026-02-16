# Canny Edge Detection (From Scratch)

This project implements the **Canny Edge Detection algorithm from scratch in Python**, without using OpenCV’s built-in Canny function.  
It follows the complete Canny pipeline including:

- Gaussian smoothing
- Gradient computation (Sobel filters)
- Non-Maximum Suppression
- Double Thresholding
- Edge Tracking by Hysteresis

Additionally, the project includes scripts to compare outputs using:

- Mean Squared Error (MSE)
- Structural Similarity Index (SSIM)

---

## 📁 Project Structure

```

Canny_Edge_Detection/
│
├── main.py              # Full Canny edge detection pipeline
├── direct.py            # Alternative / direct implementation
├── mse_comp.py          # MSE comparison script
├── mse_direct.py        # MSE comparison for direct implementation
├── ssim_gra.py          # SSIM comparison for gradient stage
├── ssim_nms.py          # SSIM comparison for non-max suppression
├── ssim_th.py           # SSIM comparison for threshold stage
│
├── images/              # Input images
│   ├── Lenna.png
│   ├── boy.PNG
│   ├── cameraman.jpg
│   └── ...
│
└── output/              # Generated outputs for each stage

````

---

## 🧠 Algorithm Pipeline (Implemented in `main.py`)

The program performs the following steps:

### 1️⃣ Grayscale Conversion
Images are loaded in grayscale using OpenCV.

### 2️⃣ Gaussian Smoothing
A 5×5 Gaussian kernel is applied manually using a custom convolution function.

### 3️⃣ Gradient Calculation
Sobel filters are applied:
- Gx (horizontal)
- Gy (vertical)

Gradient magnitude and direction are computed.

### 4️⃣ Non-Maximum Suppression
Edges are thinned by suppressing non-maximum pixels along the gradient direction.

### 5️⃣ Double Thresholding
Pixels are classified into:
- Strong edges
- Weak edges
- Non-edges

### 6️⃣ Hysteresis
Weak edges connected to strong edges are preserved; others are removed.

---

## 🚀 How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/Vidhi1999/Canny_Edge_Detection.git
cd Canny_Edge_Detection/Canny_Edge_Detection
````

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run Main Canny Edge Detection

```bash
python main.py
```

### What Happens Next?

1. The program lists all images inside the `images/` folder.
2. Enter the image number when prompted.
3. The program runs the full Canny pipeline.
4. Each stage result is:

   * Displayed using matplotlib
   * Saved inside the `output/` folder
5. Press `c` to continue with another image.

---

## 📊 Comparing Results (MSE & SSIM)

The project includes scripts for image similarity comparison.

### 🔹 Run MSE Comparison

```bash
python mse_comp.py
```

### 🔹 Run SSIM Comparison

```bash
python ssim_gra.py
python ssim_nms.py
python ssim_th.py
```

⚠️ Note:
Some comparison scripts contain hardcoded file paths (Windows paths).
Update the image paths inside these scripts to match your local `output/` folder before running.

Example fix:

```python
original = cv2.imread("output/ground.JPG")
contrast = cv2.imread("output/owl_can.png")
```

---

## 📌 Key Features

* Manual convolution implementation
* Custom Gaussian kernel
* Manual Sobel gradient computation
* Complete Non-Maximum Suppression logic
* Configurable threshold ratios
* MSE and SSIM evaluation support
* Step-by-step output visualization

---

## 🛠 Technologies Used

* Python
* NumPy
* OpenCV
* Matplotlib
* scikit-image

---

## 📷 Sample Outputs

The `output/` folder contains:

* Smoothed images
* Gradient images
* Non-maximum suppressed images
* Threshold results
* Final Canny edge output

---

## 🎯 Educational Purpose

This project is designed to:

* Understand how Canny Edge Detection works internally
* Learn manual convolution implementation
* Study gradient-based edge detection
* Compare image similarity metrics (MSE & SSIM)

---

## 📜 License

This project is for academic and educational use.