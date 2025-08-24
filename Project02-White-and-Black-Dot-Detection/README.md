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


---

## 📂 Project Structure
```bash
DotDetection/
│── WhiteDots.png       # Example input image
│── BlackDots.jpg      # Example input image
│── output.png          # Output with detected dots
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
fps = int(cap.get(cv2.CAP_PROP_FPS))   # Get video FPS
frame_interval = int(fps * 2)          # Save every ~2 seconds
```

- `fps` → Frames per second of the video  
- `frame_interval` → Number of frames to skip before saving the next one  
- `count > fps * 45` → Stops after **45 seconds** (can be changed)  

### 3. Output
- Extracted frames will be saved in the **current folder** as:
  ```
  Frame0.jpg, Frame1.jpg, Frame2.jpg, ...
  ```
- Console will display the total number of saved frames.
---

## 📌 Customization
- Change `frame_interval` to control how frequently frames are saved.
- Adjust the stopping condition (`fps * 45`) to extract frames for a different duration.
- Modify the filename in `cv2.imwrite()` to save frames in a custom folder.
