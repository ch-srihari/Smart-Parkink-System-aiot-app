# 🚗 Smart-Parkink-System-aiot-app

A Smart Parking System that uses an Android IP Webcam, Python-based vehicle detection, and MIT App Inventor to display real-time parking slot information. This project was built using AIoT techniques and visualized through a mobile application with Google Sheets integration.

---

## 📌 Features

- Real-time car detection using IP Webcam stream
- Vehicle counting with Haar Cascade Classifier
- Slot occupancy status (Occupied / Available)
- Live data logging to Google Sheets
- Mobile app to display parking status (created with MIT App Inventor)
- Cost-effective and scalable for small parking lots

---

## 🎥 Demo Video

Watch the execution and results of the Smart Parking System in action:

📽️ [Click here to watch the demo video](./Recording%202024-06-21%20202947%20(1)%20(1).mp4)

### 🔎 Video Highlights:

- Capturing video from Android IP Webcam
- Detecting cars using Haar Cascades in real-time
- Updating available/occupied count in Google Sheets
- Mobile app view displaying live parking status

---

## 🧠 Technologies Used

| Category         | Tools/Technologies                          |
|------------------|---------------------------------------------|
| Programming      | Python                                      |
| Image Processing | OpenCV, Haar Cascade                        |
| Webcam Stream    | Android IP Webcam App                       |
| Cloud Storage    | Google Sheets API (via gspread)             |
| App Development  | MIT App Inventor                            |
| OS               | Windows                                     |

---

## 📁 Project Structure

```bash
Smart-Parkink-System-aiot-app/
│
├── app_screenshots/                        # MIT App Inventor interface screenshots
├── cardetectionthrowipcam.py               # Python code for vehicle detection via IP Webcam
├── Recording 2024-06-21 202947 (1) (1).mp4  # Screen recording of project execution and results
├── README.md                               # Project documentation

