# 🎓 Face Attendance System using Python & OpenCV

A simple face-recognition based attendance management system built with **Python**, **OpenCV**, and **Tkinter**.  
The system captures face images, trains them, and automatically marks attendance in CSV files.

---

## 🚀 Features
- Register new students with ID & Name
- Capture multiple face samples (default: 50 images per student)
- Train images using **LBPH Face Recognizer**
- Automatic face recognition & attendance marking
- Attendance records stored as `.csv` files (one per subject)
- View attendance in tabular format
- Simple GUI with **Tkinter**

---

## 📂 Project Structure

---

## ⚙️ Requirements
- Python 3.6+
- OpenCV (`opencv-python`, `opencv-contrib-python`)
- Tkinter (comes with Python)
- Pillow
- Pandas
- Numpy
- Pyttsx3 (for text-to-speech)

Install all dependencies:
```bash
pip install -r requirements.txt
```
Setup folders (if not already created)

mkdir TrainingImage TrainingImageLabel StudentDetails


Run the system

Open attendance.py (main file for UI)

Register a new student → Take Images → Train Images

Start Automatic Attendance
⚠️ Notes

High processing power recommended (8GB RAM & GPU helps)

Image quality matters – noisy images reduce accuracy

Haarcascade models required: Download here

⭐ Contribution

Fork the repo

Create a new branch (feature-xyz)

Commit your changes

Open a pull request

📜 License

MIT License © 2025 Nguyen Duc Dung
