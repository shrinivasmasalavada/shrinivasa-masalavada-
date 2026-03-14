<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Real-Time Object Detection</title>
    <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs"></script>
    <script src="https://cdn.jsdelivr.net/npm/@tensorflow-models/coco-ssd"></script>
    <style>
        body { font-family: sans-serif; display: flex; flex-direction: column; align-items: center; background: #f0f0f0; }
        .container { position: relative; margin-top: 20px; }
        video, canvas { position: absolute; left: 0; top: 0; border-radius: 8px; }
        #status { margin-top: 10px; font-weight: bold; color: #555; }
    </style>
</head>
<body>

    <h2>AI Object Detection</h2>
    <p id="status">Loading Model... Please wait.</p>

    <div class="container">
        <video id="webcam" autoplay muted width="640" height="480"></video>
        <canvas id="canvas" width="640" height="480"></canvas>
    </div>

    <script>
        const video = document.getElementById('webcam');
        const canvas = document.getElementById('canvas');
        const ctx = canvas.getContext('2d');
        const status = document.getElementById('status');

        let model = undefined;

        // 1. Initialize the Webcam
        async function setupWebcam() {
            const stream = await navigator.mediaDevices.getUserMedia({ video: true });
            video.srcObject = stream;
            return new Promise((resolve) => {
                video.onloadedmetadata = () => resolve();
            });
        }

        // 2. Predict & Draw Boxes
        async function predict() {
            const predictions = await model.detect(video);
            
            // Clear previous drawings
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            predictions.forEach(prediction => {
                // Draw the bounding box
                ctx.strokeStyle = '#00FF00';
                ctx.lineWidth = 4;
                ctx.strokeRect(...prediction.bbox);

                // Draw the label background
                ctx.fillStyle = '#00FF00';
                const textWidth = ctx.measureText(prediction.class).width;
                ctx.fillRect(prediction.bbox[0], prediction.bbox[1], textWidth + 10, 20);

                // Draw the text
                ctx.fillStyle = '#000000';
                ctx.fillText(prediction.class + ' - ' + Math.round(prediction.score * 100) + '%', prediction.bbox[0] + 5, prediction.bbox[1] + 15);
            });

            // Keep detecting
            window.requestAnimationFrame(predict);
        }

        // 3. Start the App
        async function main() {
            model = await cocoSsd.load();
            status.innerText = "Model Loaded! Point your camera at something.";
            await setupWebcam();
            predict();
        }

        main();
    </script>
</body>
</html>
