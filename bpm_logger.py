# bpm_logger.py – Python script to read BPM from Arduino and log to CSV

import serial
import csv
import time
from datetime import datetime

# Serial port settings (adjust COM port as needed)
SERIAL_PORT = 'COM3'  # Replace with your Arduino port
BAUD_RATE = 9600

# Output file
csv_file = 'data/bpm_log.csv'

# Create or open CSV file
with open(csv_file, mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "BPM"])

    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
        print("📡 Logging started... Press Ctrl+C to stop.")

        while True:
            line = ser.readline().decode('utf-8').strip()
            if line.isdigit():
                bpm = int(line)
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                writer.writerow([timestamp, bpm])
                print(f"{timestamp} - BPM: {bpm}")

    except KeyboardInterrupt:
        print("🛑 Logging stopped.")
        ser.close()
    except Exception as e:
        print(f"❌ Error: {e}")
