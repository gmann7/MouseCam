# MouseCam
## Overview
This Python program allows you to control your computer's mouse pointer using hand gestures captured by a webcam. By pointing your index finger upwards, you can move the mouse pointer, and by lifting both the index and middle fingers while moving them closer together, you can simulate a mouse click.

![Demo](https://github.com/gmann7/MouseCam/assets/55709373/a479675b-9595-46dc-968a-07ad1001373d)


## Features
- [x] **Real-time Hand Gesture Recognition:** The program uses computer vision techniques to recognize and track your hand in real-time through your webcam feed.
- [x] **Mouse Pointer Control:** Point your index finger upwards to control the movement of the mouse pointer on the screen.
- [x] **Mouse Click Simulation:** Lift both your index and middle fingers while moving them closer together to simulate a mouse click action.
- [ ] **TODO: Customizable Parameters:** You can adjust various parameters, such as sensitivity and gesture recognition thresholds, to suit your preferences.
- [x] **Cross-platform:** The program should work on Windows, macOS, and Linux, as long as you have Python and the necessary libraries installed.

## Getting Started
### Prerequisites
- Python 3.x
- OpenCV (for webcam access)
- NumPy (for numerical operations)
- PyAutoGUI (for controlling the mouse)

### Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/gmann7/MouseCam.git
2. Install the required Python packages using pip:
   ```bash
   pip install -r requirements.txt
3. Run the program:
   ```bash
   python VideoCapture.py
Ensure your webcam is enabled and properly positioned.
Point your index finger upwards to move the mouse pointer.
Lift both your index and middle fingers while moving them closer together to simulate a mouse click.

If you have more than one webcam connected ensure the script is reading the right one. You can change the integer value (n) within this line of code, in the VideoCapture.py file:
   ```bash![demo_gif_1](https://github.com/gmann7/MouseCam/assets/55709373/6c56afe0-ec4f-4db8-b221-8659483639ba)

   # Connect to Video Capture device (webcam or virtual cam)
		cap = cv2.VideoCapture(n)
