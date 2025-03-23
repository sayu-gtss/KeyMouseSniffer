# KeyMouseSniffer
A Python-based input monitoring tool that includes a keylogger, mouse listener, keyboard and mouse controller. Designed for automation, user activity tracking, and low-level input analysis on Windows systems. Ideal for ethical testing, research, or building security-focused utilities.

> ⚠️ **Disclaimer:** This project is for **educational and ethical purposes only**. Do not use it on systems or networks without explicit permission.

---

## 1.keyLogger.py
- Records every key you press and appends it to keyLogFile.txt.
- To use:
  - python keyLogger.py
- Open any window and type — then check keyLogFile.txt to see the logged keystrokes.

## 2.keyController.py
- Automatically types "Hello World" at the active cursor location.
- To use:
  - python keyController.py

## 3.mouseListener.py
- Prints the current mouse pointer coordinates in real time.
- To use:
  - python mouseListener.py
- Move the mouse around and see the coordinates logged in the terminal.

## 4.mouseController.py
- Moves the mouse to coordinates entered by the user.
- To use:
  - python mouseController.py
- Enter x and y values when prompted. The mouse will jump to that position.

## Listener 
- #### Keyboard Listener:
  - _Listener(on_press=function_name)_
  - Captures keystrokes and logs them.
  - Uses .replace() to clean characters and convert special keys (e.g., Key.space, Key.enter) to readable text.
- #### Mouse  Listener:
  - _Listener(on_move=function_name)_
  - Captures mouse movement and logs coordinates.

---

## 🚀 How to Use

### 🔧 Prerequisite
Make sure you have Python installed. Then install the required library:
```bash
pip install -r requirements.txt


