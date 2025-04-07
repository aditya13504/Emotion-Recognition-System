# Real-Time Emotion Recognition Web App

This project is a web application that performs real-time emotion recognition using a user's webcam feed. It leverages computer vision and machine learning to detect faces and classify their dominant emotions.

## Features

*   **User Authentication:** Simple username input to start.
*   **Real-Time Webcam Feed:** Captures video directly from the user's webcam via the browser.
*   **Face Detection:** Identifies faces within the video stream.
*   **Emotion Recognition:** Classifies the dominant emotion for each detected face (e.g., happy, sad, angry, neutral).
*   **Multi-Person Support:** Capable of detecting and analyzing emotions for multiple faces in the frame simultaneously.
*   **Visual Feedback:** Displays the webcam feed with bounding boxes around detected faces. Bounding boxes are color-coded based on the detected emotion. Emotion labels (as emojis) with confidence scores (indicated by opacity) are shown above the boxes.
*   **Interactive Controls:** Press 'q' to quit the live feed and return to an end screen.
*   **Stylish UI:**
    *   Custom 'Poppins' web font.
    *   Animated "starry night" background using HTML Canvas.
    *   "Glassmorphism" effect on content containers.
    *   Smooth fade transitions between pages.
    *   Subtle entrance animations and button hover effects.
    *   Username validation (requires at least one letter).

## Technology Stack

*   **Backend:**
    *   Python 3
    *   Flask (Web Framework)
    *   Flask-SocketIO (Real-time WebSocket Communication)
    *   DeepFace (Face Detection & Emotion Recognition Library)
    *   OpenCV (opencv-python-headless) (Image processing)
    *   Eventlet (WSGI Server for SocketIO)
*   **Frontend:**
    *   HTML5
    *   CSS3
    *   JavaScript (Vanilla)
    *   Socket.IO Client Library
    *   HTML Canvas (for background animation)

## Project Structure

```
/
├── static/
│   ├── css/
│   │   └── style.css         # Main CSS styles
│   └── js/
│       ├── background.js     # Starry background animation
│       └── script.js         # Frontend logic for webcam, SocketIO, results display
├── templates/
│   ├── index.html          # Initial username input page
│   ├── app.html            # Intermediate "Ready?" page
│   ├── live.html           # Live webcam feed and emotion display page
│   └── end.html            # Final "Goodbye" page
├── app.py                    # Flask application, SocketIO handling, DeepFace integration
└── requirements.txt          # Python dependencies
```

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone "https://github.com/aditya13504/Emotion-Recognition-System.git"
    cd https://github.com/aditya13504/Emotion-Recognition-System.git
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: DeepFace might download pre-trained model files on first run).*

## Running the Application

1.  **Start the Flask server:**
    ```bash
    python app.py
    ```

2.  **Open your web browser** and navigate to:
    `http://localhost:5000` (or `http://127.0.0.1:5000`)

3.  Enter a username (must contain letters) and click "Continue".
4.  Click "Continue" again on the "Ready?" page.
5.  Allow webcam access when prompted by the browser.
6.  The live feed will start, showing detected faces, bounding boxes, and emotions.
7.  Press 'q' to stop the feed and go to the end page.

## Notes

*   Emotion recognition accuracy depends heavily on lighting conditions, face angle, occlusions, and the chosen detector backend (`opencv` is currently used for speed).
*   Performance (frame rate) depends on the processing power of the server machine.
*   Ensure only one instance of the application is running to avoid port conflicts. 
