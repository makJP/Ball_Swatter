# Ball Swatter - Hand Gesture Ball Game 🎮🖐🏻
  College project

# Overview
This is a Python-based game that utilizes OpenCV and MediaPipe for hand tracking and image processing. The game features a stadium-themed user interface where balls of two colors RED and GREEN appear on the screen. The player controls the game using hand gestures, specifically closing their hand to catch the balls, as tracked by their camera.

# Key Features:
1. Stadium Background: A dynamic UI featuring a stadium backdrop.
2. Hand Tracking: The camera tracks hand movements using MediaPipe's hand-tracking functionality.
3. Two Ball Types:
    - Green Ball: Catching increases your score by 1.
    - Red Ball: Catching decreases your score by 1.
4. Difficulty Scaling: Over time, more balls appear on the screen.
5. Time Limit: The game lasts for 1 minute.

# How to Play
1. Install the necessary dependencies (OpenCV, MediaPipe):
   - pip install opencv-python mediapipe
2. Run the game by executing main.py in the source code directory.
3. A stadium-themed window will open where green and red balls start to appear.
4. Using your camera, close your hand to "catch" the balls:
   - Catch green balls to increase your score.
   - Avoid catching red balls, or your score will decrease.
5. The game ends after 1 minute, and your score is displayed.

# Requirements
- Python 3.x
- OpenCV for image processing
- MediaPipe for hand tracking
- Install all dependencies using: -> pip install -r requirements.txt

# Future Improvements
- Adding levels or increasing difficulty modes.
- Introducing different types of gestures for more interactive gameplay.
- High-score tracking and leaderboards.



