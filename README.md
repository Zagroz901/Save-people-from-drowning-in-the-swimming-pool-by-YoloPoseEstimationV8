# **Save People from Drowning Using YOLO POSE ESTIMATION V8**

![test](https://github.com/user-attachments/assets/187057fd-56fd-44cf-8315-32b6b9ea2931)

## **Overview**
This project utilizes the power of YOLOv8 (You Only Look Once) and Mediapipe to detect people in swimming pools and raise an alert if anyone is in a potentially dangerous posture (indicative of drowning). The system provides real-time video processing with bounding boxes, pose estimation, angle calculations, and an audible warning mechanism.

---

## **Features**
- **Person Detection**: Identifies individuals in the video using YOLOv8.
- **Pose Estimation**: Estimates body keypoints to monitor postures.
- **Danger Detection**: Calculates angles of body joints to identify potential drowning scenarios.
- **Audio Alerts**: Plays an alarm sound when a risky posture is detected.
- **Video Output**: Saves the processed video with all detections and alerts.
- **ID Tracking**: Tracks individuals across frames and assigns unique IDs.

---

## **Technologies Used**
- **YOLOv8**: For person detection and pose estimation.
- **OpenCV**: For video processing and visualization.
- **Miniaudio**: For playing real-time audio alerts.
- **Mutagen**: For handling MP3 metadata.
- **Python**: The programming language for development.

---

## **Installation**

### 1. Clone the Repository
```bash
git clone https://github.com/Zagroz901/Save-people-from-drowning-in-the-swimming-pool-by-YoloPoseEstimationV8.git
cd Save-people-from-drowning-in-the-swimming-pool-by-YoloPoseEstimationV8
```

### 2. Install Dependencies
Install the required Python libraries using `pip`:

> **Note:** Ensure you have Python 3.7 or higher installed.

### 3. Download YOLOv8 Weights
Download the YOLOv8 weights (`yolov8n-pose.pt`) and place them in the `Weights` directory:
- [YOLOv8 Pose Weights](https://github.com/ultralytics/yolov8)

### 4. Add Required Files
- Place the input video in the `Video` directory (e.g., `Video/vid.mp4`).
- Add the alarm sound in the `audio` directory (e.g., `audio/assets_alarm.mp3`).

---

## **Usage**

### Run the Program
```bash
python Yolo_Code.py
```

### Expected Output
1. **Real-Time Detection**: Displays bounding boxes, person count, and joint angles on the video.
2. **Alerts**: Raises an audible warning if dangerous postures are detected.
3. **Processed Video**: Saves the output video with detections in the project directory as `output_video.avi`.

---

## **Directory Structure**
```plaintext
├── Weights/
│   └── yolov8n-pose.pt
├── Video/
│   └── vid.mp4
├── audio/
│   └── assets_alarm.mp3
├── tracker.py
├── Yolo_Code.py
├── requirements.txt
└── README.md
```

---

## **Demo**

https://github.com/user-attachments/assets/012e78f8-65f3-4b0e-a81e-58b3de04660f

---

## **Customization**
- **Change Input Video**: Replace `Video/vid.mp4` with your custom video file.
- **Adjust Sensitivity**: Modify `frame_check` and angle thresholds in `Yolo_Code.py`.
- **Audio Alerts**: Replace `audio/assets_alarm.mp3` with your custom MP3 file.

---

## **Contributing**
Contributions are welcome! Please fork the repository and submit a pull request with your updates.

---

## **License**
This project is licensed under the MIT License. See `LICENSE` for more details.

---

## **Contact**
- **Author**: [Zagroz]
- **Email**: zako901zak@gmail.com
- **GitHub**: https://github.com/Zagroz901
