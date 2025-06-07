# Alarm Clock

A Python-based alarm clock application with a graphical user interface.

## Features

- Set alarms with hour, minute, and second precision
- AM/PM time format
- Play custom alarm sound when the set time is reached
- Clean GUI built with Tkinter
- Time display with current system time
- Pause/stop alarm functionality

## Screenshots

![Alarm Clock Screenshot](screenshots/alarm_clock.png)

## How to Use

1. Run the script:
   ```
   python AlarmClock.py
   ```

2. Set the alarm time:
   - Select hour, minute, and second using the dropdown menus
   - Choose AM or PM
   - Click "Set Alarm"

3. The alarm will sound when the current time matches your set time
4. Stop the alarm by clicking the appropriate button

## Customizing the Alarm Sound

The application uses "MyAlarm.wav" as the default alarm sound. To use a different sound:
1. Replace the "MyAlarm.wav" file with your preferred sound file (must be in WAV format)
2. Keep the same filename or update the filename in the code

## Requirements

- Python 3.x
- Tkinter (usually comes with Python)
- pygame or playsound library for audio playback
