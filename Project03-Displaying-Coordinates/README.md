# 🖱️ Mouse Event Handling in OpenCV

This project demonstrates how to use **mouse events** in OpenCV to interact with images.  
It allows you to click on an image (left or right click) and display the pixel coordinates directly on the image.  

---

## 📌 Features
- Detects **left mouse button clicks**  
- Detects **right mouse button clicks**  
- Displays the clicked coordinates on the image  
- Prints the coordinates in the console  
- Easy to extend for other mouse events (double-click, middle-click, etc.)  

---

## 🛠️ Requirements
Install the required dependency before running the project:

```bash
pip install opencv-python
```

---

## 📂 Project Structure
```bash
MouseEvents/
│── Cat.jpg            # Example input image
│── main.py     # Main script
│── README.md           # Project documentation
```

---

## 🚀 Usage

### 1. Run the Script
```bash
python mouse_events.py
```

### 2. Code Explanation
```python
cv2.setMouseCallback('image', click_event)
```
- Registers the function `click_event` as the **mouse handler** for the window named `'image'`.

```python
if event == cv2.EVENT_LBUTTONDOWN:
    cv2.putText(img, str(x)+','+str(y), (x,y), font, 1, (255,0,0), 2)
```
- On **left click**, the program prints and displays the coordinates on the image.

```python
if event == cv2.EVENT_RBUTTONDOWN:
    cv2.putText(img, str(x)+','+str(y), (x,y), font, 1, (255,0,0), 2)
```
- On **right click**, it does the same (can be customized to show pixel color values instead).  

---

## 📌 Customization
- Change the code inside `EVENT_RBUTTONDOWN` to display **BGR color values** of the clicked pixel.  
- Add other events like `cv2.EVENT_MOUSEMOVE` to track mouse movement.  
- Modify `cv2.putText()` to change font, color, or size of displayed coordinates.  

---

