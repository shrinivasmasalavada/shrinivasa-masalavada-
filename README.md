<!DOCTYPE html>
<html>
<head>
    <title>Hand Gesture Detection</title>
    <script src="https://cdn.jsdelivr.net/npm/@mediapipe/hands"></script>
    <script src="https://cdn.jsdelivr.net/npm/@mediapipe/drawing_utils"></script>
    <script src="https://cdn.jsdelivr.net/npm/@mediapipe/camera_utils"></script>
</head>
<body>
    <div style="position: relative;">
        <video id="webcam" style="position: absolute; transform: scaleX(-1);" autoplay></video>
        <canvas id="output_canvas" style="position: absolute; transform: scaleX(-1);"></canvas>
    </div>

    <script>
        const videoElement = document.getElementById('webcam');
        const canvasElement = document.getElementById('output_canvas');
        const canvasCtx = canvasElement.getContext('2d');

        function onResults(results) {
            canvasElement.width = videoElement.videoWidth;
            canvasElement.height = videoElement.videoHeight;
            canvasCtx.clearRect(0, 0, canvasElement.width, canvasElement.height);
            
            if (results.multiHandLandmarks) {
                for (const landmarks of results.multiHandLandmarks) {
                    // ಕೈ ಮೇಲೆ ಗೆರೆ ಮತ್ತು ಚುಕ್ಕೆಗಳನ್ನು ಬಿಡಿಸಲು
                    drawConnectors(canvasCtx, landmarks, HAND_CONNECTIONS, {color: '#00FF00', lineWidth: 5});
                    drawLandmarks(canvasCtx, landmarks, {color: '#FF0000', lineWidth: 2});
                }
            }
        }

        const hands = new Hands({locateFile: (file) => {
            return `https://cdn.jsdelivr.net/npm/@mediapipe/hands/${file}`;
        }});

        hands.setOptions({
            maxNumHands: 2,
            modelComplexity: 1,
            minDetectionConfidence: 0.5,
            minTrackingConfidence: 0.5
        });

        hands.onResults(onResults);

        const camera = new Camera(videoElement, {
            onFrame: async () => {
                await hands.send({image: videoElement});
            },
            width: 640,
            height: 480
        });
        camera.start();
    </script>
</body>
</html>
