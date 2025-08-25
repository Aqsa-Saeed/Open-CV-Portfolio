# 🎨 BGR Color Palette using OpenCV

This project demonstrates how to create a **color palette tool** using **OpenCV Trackbars**.  
Users can interactively adjust the **Blue, Green, and Red** sliders to mix colors and visualize the result in real-time.

---

## 📌 Features
- Interactive **trackbars** for Blue, Green, and Red channels (0–255).
- Window displays the combined BGR color instantly.
- Press **ESC (Escape key)** to exit the program.
- Simple demonstration of **OpenCV GUI features** and **NumPy array manipulation**.

---

## 🛠️ Requirements
Make sure you have the following installed:
- Python 3.x
- [OpenCV](https://pypi.org/project/opencv-python/)  
- NumPy  

Install dependencies using pip:
```bash
pip install opencv-python numpy
```

---

## 🚀 How to Run
1. Clone or download this repository.  
2. Run the script:
   ```bash
   python color_palette.py
   ```
3. A window will open with sliders for **Blue, Green, and Red**.  
4. Adjust sliders to mix colors and see the result.  
5. Press **ESC** to close the window.

---

## 🖼️ Demo
- Start with a black window.
- Use the trackbars:
  - Increase **Blue** → window turns bluish.  
  - Increase **Green** → window turns greenish.  
  - Increase **Red** → window turns reddish.  
- Mix sliders to generate any color.

---

## 📂 Project Structure
```
📦 BGR-Color-Palette
 ┣ 📜 color_palette.py   # Main script
 ┗ 📜 README.md          # Project documentation
```

---

## 📖 Concepts Used
- **cv2.namedWindow()** → Create a window for display.  
- **cv2.createTrackbar()** → Add trackbars (sliders) to a window.  
- **cv2.getTrackbarPos()** → Get current trackbar value.  
- **NumPy slicing (`[:]`)** → Update the entire image color at once.  

---

## 🎯 Use Cases
- Learning OpenCV GUI functions.  
- Understanding how to work with **BGR color spaces**.  
- Can be extended to build tools like a **color picker** or **image color adjustment utility**.

---

