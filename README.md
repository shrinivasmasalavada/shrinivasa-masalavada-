<!DOCTYPE html>
<html lang="kn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ಗೋರಕ್ಷ (Goraksha)</title>
    <style>
        /* ವಿನ್ಯಾಸ (Styling) */
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f9f9f9;
            text-align: center;
        }

        header {
            background-color: #2e7d32;
            color: white;
            padding: 20px;
            font-size: 24px;
            font-weight: bold;
        }

        .search-container {
            margin: 30px auto;
        }

        #searchInput {
            padding: 12px;
            width: 80%;
            max-width: 400px;
            border: 2px solid #2e7d32;
            border-radius: 25px;
            outline: none;
            font-size: 16px;
        }

        #result {
            margin-top: 20px;
            font-size: 20px;
            color: #d32f2f;
            font-weight: bold;
            height: 30px;
        }

        /* ಹಸುಗಳ ಫೋಟೋ ಮೂಮೆಂಟ್ (Animation) */
        .cow-slider {
            width: 100%;
            overflow: hidden;
            background: #fff;
            padding: 20px 0;
            margin-top: 50px;
            border-top: 2px solid #eee;
        }

        .cow-track {
            display: flex;
            width: calc(250px * 6);
            animation: scroll 15s linear infinite;
        }

        .cow-track img {
            width: 200px;
            height: 150px;
            margin: 0 20px;
            border-radius: 10px;
            object-fit: cover;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }

        @keyframes scroll {
            0% { transform: translateX(0); }
            100% { transform: translateX(calc(-250px * 3)); }
        }
    </style>
</head>
<body>

    <header>ಗೋರಕ್ಷ</header>

    <div class="search-container">
        <input type="text" id="searchInput" onkeyup="searchDoctor()" placeholder="ನಿಮ್ಮ ಊರಿನ ಹೆಸರು ಟೈಪ್ ಮಾಡಿ (ಉದಾ: ಹಮ್ಮಿಗಿ)...">
        <div id="result"></div>
    </div>

    <div class="cow-slider">
        <div class="cow-track">
            <img src="https://images.unsplash.com/photo-1546445317-29f4545e9d53?auto=format&fit=crop&w=200&q=80" alt="Cow 1">
            <img src="https://images.unsplash.com/photo-1500595046743-cd271d694d30?auto=format&fit=crop&w=200&q=80" alt="Cow 2">
            <img src="https://images.unsplash.com/photo-1527153358354-fbd18df09b55?auto=format&fit=crop&w=200&q=80" alt="Cow 3">
            <img src="https://images.unsplash.com/photo-1546445317-29f4545e9d53?auto=format&fit=crop&w=200&q=80" alt="Cow 1">
            <img src="https://images.unsplash.com/photo-1500595046743-cd271d694d30?auto=format&fit=crop&w=200&q=80" alt="Cow 2">
            <img src="https://images.unsplash.com/photo-1527153358354-fbd18df09b55?auto=format&fit=crop&w=200&q=80" alt="Cow 3">
        </div>
    </div>

    <script>
        function searchDoctor() {
            let input = document.getElementById('searchInput').value.trim();
            let resultDiv = document.getElementById('result');

            // ಹಮ್ಮಿಗಿ ಅಥವಾ Hammigi ಎಂದು ಟೈಪ್ ಮಾಡಿದಾಗ ಕೆಲಸ ಮಾಡುತ್ತದೆ
            if (input === "ಹಮ್ಮಿಗಿ" || input.toLowerCase() === "hammigi") {
                resultDiv.innerHTML = "ಡಾಕ್ಟರ್ ಮೊಬೈಲ್ ಸಂಖ್ಯೆ: 7090593584";
            } else if (input === "") {
                resultDiv.innerHTML = "";
            } else {
                resultDiv.innerHTML = "ಮಾಹಿತಿ ಲಭ್ಯವಿಲ್ಲ";
            }
        }
    </script>

</body>
</html>
