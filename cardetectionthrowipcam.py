import cv2
from googleapiclient.discovery import build
from google.oauth2 import service_account
from datetime import datetime, timedelta
import time

# Google Sheets API setup
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SERVICE_ACCOUNT_FILE = 'keys.json'

creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID of the spreadsheet.
SAMPLE_SPREADSHEET_ID = "1np7s_-8gxvP3Diwc6iuyJbxgpAf3Q5CAM0r4LnQlf7k"

service = build("sheets", "v4", credentials=creds)
sheet = service.spreadsheets()

# OpenCV car detection setup
car_cascade = cv2.CascadeClassifier('haarcascade_car.xml')
total_slots = 14

# URL for the video feed
url = "http://192.168.66.8:8080/video"

# Open the video feed
capture = cv2.VideoCapture(url)

# Check if the video capture was successful
if not capture.isOpened():
    print("Error: Unable to connect to the camera.")
else:
    print("Camera connected successfully.")

last_update_time = datetime.now()

while True:
    # Capture frame-by-frame
    ret, frame = capture.read()

    # Check if the frame is valid
    if not ret:
        print("Error: Failed to capture frame.")
        break
    
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect cars
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    # Calculate the number of cars and available slots
    car_count = len(cars)
    available_slots = total_slots - car_count

    current_time = datetime.now()
    if (current_time - last_update_time).total_seconds() >= 10:
        # Get the current timestamp
        timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

        # Prepare the values to be updated in Google Sheets
        values = [
            [timestamp, car_count, available_slots]
        ]

        body = {
            "values": values
        }

        # Update the sheet in a specific range, e.g., "Sheet1!A:C" for appending data
        result = sheet.values().append(
            spreadsheetId=SAMPLE_SPREADSHEET_ID,
            range="Sheet1!A:C",  # Adjust the range to match your sheet structure
            valueInputOption="USER_ENTERED",
            body=body
        ).execute()

        print(f"{result.get('updates').get('updatedCells')} cells updated in the spreadsheet.")

        # Update the last update time
        last_update_time = current_time

    # Display the frame
    cv2.imshow('Live Stream', frame)

    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
capture.release()
cv2.destroyAllWindows()
