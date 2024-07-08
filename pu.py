import sys
print(sys.path)

print("HELLO")
import platform
import cv2
import mediapipe as mp
import pyautogui

print(cv2.__version__)  # Check OpenCV version
print(mp.__version__)   # Check MediaPipe version

if platform.system() == "Windows":
    try:
        import pydirectinput
        # Example usage of pydirectinput on Windows
        print("pydirectinput imported successfully.")
    except ImportError:
        print("Failed to import pydirectinput on Windows.")
else:
    print("pydirectinput is not supported on this operating system.")
    # Example usage of pyautogui on macOS or Linux
    pyautogui.moveTo(100, 100)
    pyautogui.click()
