# ⚪⚫ White and Black Dot Detection using OpenCV

This project detects and counts **white and black dots** in images using **OpenCV (cv2)**.  
It uses image thresholding and contour detection techniques to separate dots by color and count them individually.

---

## 📌 Features
- Detects **white dots** in an image  
- Detects **black dots** in an image  
- Counts the number of dots separately  
- Highlights detected dots with contours  
- Simple and easy to extend for other shapes/colors  

---

## 🛠️ Requirements
Install the required dependency before running the project:

```bash
pip install opencv-python
```

---

## 📂 Project Structure
```bash
DotDetection/
│── WhiteDots.png       # Example input image
│── BlackDots.jpg      # Example input image
│── Output.png          # Output with detected dots
│── dot_detector.py     # Main script
│── README.md           # Project documentation
```

---

## 🚀 Usage

### 1. Run the Script
```bash
python dot_detector.py
```

### 2. Code Explanation
```python
# Convert image to grayscale
gray = cv2.imread(path, 0)

# Thresholding for separating dots
_, threshed = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

# Find contours
cnts = cv2.findContours(threshed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]
```

- `cv2.threshold()` → Separates dots from the background  
- `cv2.findContours()` → Finds outlines of the dots  
- You can filter small noise using contour area checks  

---

## 🎯 Output
- The program draws contours around each dot  
- Console prints the number of **white** and **black** dots detected  

Example:
```text
White Dots: 583
Black Dots: 23
```


