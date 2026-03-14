<!DOCTYPE html>
<html lang="kn">
<head>
    <meta charset="UTF-8">
    <title>Object Detection - ಕನ್ನಡ</title>
    <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs"></script>
    <script src="https://cdn.jsdelivr.net/npm/@tensorflow-models/coco-ssd"></script>
    <style>
        body { font-family: sans-serif; display: flex; flex-direction: column; align-items: center; }
        video { border: 2px solid #333; border-radius: 10px; }
        canvas { position: absolute; left: 50%; transform: translateX(-50%); }
        #status { color: red; font-weight: bold; }
    </style>
</head>
<body>

    <h2>AI ಆಬ್ಜೆಕ್ಟ್ ಡಿಟೆಕ್ಷನ್ (Webcam)</h2>
    <p id="status">ಮಾಡೆಲ್ ಲೋಡ್ ಆಗುತ್ತಿದೆ, ದಯವಿಟ್ಟು ಕಾಯಿರಿ...</p>
    
    <div style="position: relative;">
        <video id="webcam" autoplay muted width="640" height="480"></video>
        <canvas id="canvas" width="640" height="480"></canvas>
    </div>

    <script>
        const video = document.getElementById('webcam');
        const canvas = document.getElementById('canvas');
        const ctx = canvas.getContext('2d');
        const status = document.getElementById('status');

        let model;

        // 1. ವೆಬ್‌ಕ್ಯಾಮ್ ಆನ್ ಮಾಡುವುದು
        async function setupWebcam() {
            const stream = await navigator.mediaDevices.getUserMedia({ video: true });
            video.srcObject = stream;
            return new Promise((resolve) => {
                video.onloadedmetadata = () => resolve();
            });
        }

        // 2. ಆಬ್ಜೆಕ್ಟ್ ಡಿಟೆಕ್ಟ್ ಮಾಡುವ ಫಂಕ್ಷನ್
        async function detectObjects() {
            const predictions = await model.detect(video);
            
            // ಕ್ಯಾನ್ವಾಸ್ ಕ್ಲಿಯರ್ ಮಾಡುವುದು
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            predictions.forEach(prediction => {
                // ಬಾಕ್ಸ್ ಬಿಡಿಸುವುದು
                ctx.beginPath();
                ctx.rect(...prediction.bbox);
                ctx.lineWidth = 2;
                ctx.strokeStyle = '#00FF00';
                ctx.fillStyle = '#00FF00';
                ctx.stroke();

                // ವಸ್ತುವಿನ ಹೆಸರು ಬರೆಯುವುದು
                ctx.font = '18px Arial';
                ctx.fillText(
                    `${prediction.class} (${Math.round(prediction.score * 100)}%)`,
                    prediction.bbox[0], 
                    prediction.bbox[1] > 10 ? prediction.bbox[1] - 5 : 10
                );
            });

            // ನಿರಂತರವಾಗಿ ಡಿಟೆಕ್ಟ್ ಮಾಡಲು ಲೂಪ್
            requestAnimationFrame(detectObjects);
        }

        // 3. ಮುಖ್ಯ ಪ್ರಕ್ರಿಯೆ ಆರಂಭ
        async function run() {
            model = await cocoSsd.load();
            status.innerText = "ಮಾಡೆಲ್ ರೆಡಿಯಾಗಿದೆ! ಕ್ಯಾಮರಾ ನೋಡಿ.";
            await setupWebcam();
            detectObjects();
        }

        run();
    </script>
</body>
</html>
