# Apply monkey patch first
import eventlet
eventlet.monkey_patch() # Patch standard libraries for eventlet compatibility

import base64
import logging
import cv2
import numpy as np
from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import SocketIO, emit
from deepface import DeepFace

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_very_secret_key!' # Change this in production!
socketio = SocketIO(app, async_mode='eventlet')

# Configure logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_app', methods=['POST'])
def start_app():
    username = request.form.get('username')
    if not username:
        return redirect(url_for('index')) # Or show an error
    session['username'] = username
    return render_template('app.html', username=username)

@app.route('/live')
def live():
    if 'username' not in session:
        return redirect(url_for('index'))
    return render_template('live.html')

@app.route('/end')
def end():
    session.pop('username', None) # Clear username on exit
    return render_template('end.html')

@socketio.on('connect')
def handle_connect():
    log.info('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    log.info('Client disconnected')

@socketio.on('image')
def handle_image(data_url):
    try:
        # Decode the base64 image
        header, encoded = data_url.split(',', 1)
        image_data = base64.b64decode(encoded)
        nparr = np.frombuffer(image_data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if img is None:
            log.warning("Received empty image frame.")
            return

        # Analyze emotions using deepface
        # enforce_detection=False prevents errors if no face is detected
        results = DeepFace.analyze(
            img_path=img,
            actions=['emotion'],
            enforce_detection=False, # Changed back from True for robustness
            # detector_backend='mtcnn' # Changed to potentially more accurate backend
            detector_backend='opencv' # Reverted back to faster backend
        )

        # log.info(f"Raw DeepFace results: {results}") # Remove logging line

        # Ensure results is always a list
        if isinstance(results, dict):
            results = [results]

        # Prepare data for the client
        processed_data = []
        for result in results:
            if result.get('face_confidence', 0) > 0: # Check if a face was detected
                processed_data.append({
                    'box': result['region'], # {'x': ..., 'y': ..., 'w': ..., 'h': ...}
                    'emotion': result['dominant_emotion'],
                    'confidence': result.get('emotion', {}).get(result['dominant_emotion'], 0) # Get confidence score
                })

        # Send results back to the client
        emit('processed_image', processed_data)

    except Exception as e:
        log.error(f"Error processing image: {e}")
        # Optionally emit an error event to the client
        # emit('processing_error', {'error': str(e)})

if __name__ == '__main__':
    log.info("Starting Flask-SocketIO server...")
    # Use 0.0.0.0 to make it accessible on your local network
    # Set debug=False for production generally, but True is fine for development
    socketio.run(app, host='0.0.0.0', port=5000, debug=True) 