# ❤️ HeartPulseMonitor – Real-Time BPM Monitor with Logger

This project tracks a user's heart rate in real-time using a Pulse Sensor connected to an Arduino. It streams live BPM (beats per minute) values over serial and logs them to a CSV using Python.

---

## 🔧 Hardware Components
- Arduino Uno
- Pulse Sensor (e.g., Pulse Sensor Amped)
- 16x2 LCD (optional, for live display)
- USB cable
- Jumper wires

---

## 📦 Folder Structure
```
HeartPulseMonitor/
├── firmware/
│   └── pulse_monitor.ino
├── logger/
│   └── bpm_logger.py
├── data/
│   └── bpm_log.csv
├── hardware/
│   ├── schematic.pdf
│   └── wiring_diagram.png
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Arduino Code – `pulse_monitor.ino`
Reads analog pulse sensor data, calculates BPM, and prints it to serial.

---

## 🐍 Python Script – `bpm_logger.py`
- Reads BPM values from serial
- Appends timestamped data to `data/bpm_log.csv`
- Shows real-time plot (optional)

---

## 🧪 How It Works
1. Pulse sensor detects pulse and sends analog signal
2. Arduino calculates BPM and prints to serial every 1 second
3. Python reads serial stream and logs BPM + time to a CSV

---

## 📊 Output Example
```
Timestamp,BPM
2025-07-20 13:42:01,78
2025-07-20 13:42:02,80
2025-07-20 13:42:03,79
```

---

## ✅ Applications
- Basic heart rate monitor for telemedicine
- Remote health monitoring
- Fitness applications

---

## 📄 License
MIT License – free to use and modify.

---

## 🙋‍♂️ Author
Built with ❤️ by [Your Name], combining Arduino and Python for real-world biosensing.

