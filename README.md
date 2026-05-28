# 🧥 Dark Blue Invisibility Cloak (OpenCV Project)

Turn yourself invisible on camera using a **dark blue cloak** and some computer vision magic!  
This project uses **OpenCV** and **NumPy** to detect a cloak of a specific color and replace it with the background, creating a Harry Potter–style invisibility effect. ✨

---

## 🚀 Features
- Captures a clean background automatically (no manual snapshots needed).
- Detects **dark blue cloak** using HSV color masking.
- Smooths mask with morphological operations for better accuracy.
- Real-time invisibility effect using webcam.
- Easy to quit with a single key press (`q`).

---

## 📦 Requirements
Make sure you have the following installed:

- Python 3.x  
- OpenCV → `pip install opencv-python`  
- NumPy → `pip install numpy`  

---

## ▶️ How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/invisibility-cloak.git
   cd invisibility-cloak
2. Run the script:
  ```bash
  python cloak.py
```
3. Steps:
- Stay out of the frame while background is being captured.
- Wear a dark blue cloak (or cloth).
- Watch yourself disappear in real-time!

---

## 🖼️ Demo
- Step 1: Background capture
- Step 2: Cloak detection
- Step 3: Invisibility effect applied

---

## ⚙️ Code Highlights
- Background Capture: Uses median of multiple frames for a clean background.
- Color Detection: HSV mask for dark blue range [100, 100, 50] → [130, 255, 255].
- Final Output: Combines cloak area (background) + visible area (current frame).
