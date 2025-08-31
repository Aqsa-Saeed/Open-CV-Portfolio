# ✂️ Interactive Image Cropper using OpenCV

This project allows you to **interactively crop a region of interest
(ROI)** from an image using **OpenCV (cv2)** and mouse events.\
You can click and drag on the image to select a rectangular area, and
the selected region will be cropped and displayed.

------------------------------------------------------------------------

## 📌 Features

-   Load an image and crop a selected region interactively\
-   Use mouse drag to select the cropping area\
-   Cropped region is displayed in a new window\
-   Easily extendable for more advanced image editing tasks

------------------------------------------------------------------------

## 🛠️ Requirements

Make sure you have the following installed:

``` bash
pip install opencv-python
```

------------------------------------------------------------------------

## 📂 Project Structure

    Interactive-Image-Cropper/
    │── Cat2.jpg                 # Sample input image
    │── main.py                  # Main script
    │── README.md                # Project documentation

------------------------------------------------------------------------

## 🚀 Usage

### 1. Run the Script

``` bash
python main.py --image Cat2.jpg
```

### 2. Instructions

-   Left-click and drag to select a region of interest (ROI)\
-   Release the mouse to finalize selection\
-   The cropped portion of the image will appear in a new window

------------------------------------------------------------------------

## 🔎 Code Explanation

``` python
cv.setMouseCallback("image", shape_selection)
```

-   Sets mouse event handler for cropping.

``` python
roi = image[y:y+h, x:x+w]
```

-   Extracts the selected region of interest from the original image.

------------------------------------------------------------------------

## 📌 Customization

-   Replace `Cat2.jpg` with your own image path.\
-   Modify the script to save cropped regions instead of just displaying
    them.\
-   Extend functionality (e.g., multiple crops, shape-based cropping).

------------------------------------------------------------------------

## 🎯 Output

-   Original image window (for ROI selection)\
-   Cropped region displayed in a separate window after selection
