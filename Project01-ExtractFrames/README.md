# 🎥 Frame Extractor using OpenCV

This project extracts frames from a given video file using **OpenCV (cv2)**.  
It allows you to save frames at specific intervals and limit extraction up to a certain duration of the video.

---

## 📌 Features
- Extracts frames from a video file (`.mp4`, `.avi`, etc.)
- Adjustable **frame interval** (e.g., save every Nth frame)
- Option to stop after a fixed duration (e.g., first 15 seconds)
- Saves extracted frames as **.jpg** images
- Easy to modify and extend

---

## 🛠️ Requirements
Make sure you have the following installed:

```bash
pip install opencv-python
```

---

## 📂 Project Structure
```bash
FrameExtractor/
│── Video1.mp4         # Input video file
│── Frame0.jpg         # Extracted frame (example)
│── Frame1.jpg
│── ...
│── extractor.py       # Main script
│── README.md          # Project documentation
```

---

## 🚀 Usage

### 1. Run the Script
```bash
python extractor.py
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

## 🖼️ How it Works (Flowchart)
```mermaid
flowchart TD
    A[Start] --> B[Load video with OpenCV]
    B --> C[Get FPS of video]
    C --> D[Set frame interval]
    D --> E[Read next frame]
    E --> F{Frame read successful?}
    F -- No --> G[Stop & Release Video]
    F -- Yes --> H[Check if time exceeded (e.g., 45s)]
    H -- Yes --> G
    H -- No --> I{Is current frame at interval?}
    I -- Yes --> J[Save frame as JPG]
    I -- No --> K[Skip frame]
    J --> E
    K --> E
    G --> L[Print total saved frames]
    L --> M[End]
```

---

## 📌 Customization
- Change `frame_interval` to control how frequently frames are saved.
- Adjust the stopping condition (`fps * 45`) to extract frames for a different duration.
- Modify the filename in `cv2.imwrite()` to save frames in a custom folder.
