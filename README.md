<!DOCTYPE html>
<html lang="kn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ಗೋರಕ್ಷ - Goraksha</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f4f7f6;
            margin: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .header {
            background-color: #2e7d32;
            color: white;
            width: 100%;
            padding: 20px 0;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        }
        .container {
            margin-top: 50px;
            width: 90%;
            max-width: 400px;
            text-align: center;
        }
        input[type="text"] {
            width: 100%;
            padding: 12px;
            font-size: 18px;
            border: 2px solid #2e7d32;
            border-radius: 5px;
            outline: none;
        }
        button {
            margin-top: 15px;
            padding: 10px 20px;
            background-color: #2e7d32;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #1b5e20;
        }
        #result {
            margin-top: 30px;
            padding: 20px;
            border-radius: 10px;
            font-size: 20px;
            display: none; /* ಆರಂಭದಲ್ಲಿ ಇದನ್ನು ಮರೆಮಾಡಲಾಗಿದೆ */
        }
        .success-card {
            background-color: #e8f5e9;
            border-left: 5px solid #2e7d32;
            color: #1b5e20;
        }
        .error-card {
            background-color: #ffebee;
            border-left: 5px solid #c62828;
            color: #b71c1c;
        }
    </style>
</head>
<body>

    <div class="header">ಗೋರಕ್ಷ (Goraksha)</div>

    <div class="container">
        <input type="text" id="townSearch" placeholder="ನಿಮ್ಮ ಊರಿನ ಹೆಸರು ಟೈಪ್ ಮಾಡಿ...">
        <button onclick="searchDoctor()">ಹುಡುಕಿ</button>

        <div id="result"></div>
    </div>

    <script>
        function searchDoctor() {
            const input = document.getElementById('townSearch').value.trim().toLowerCase();
            const resultDiv = document.getElementById('result');

            // ಹಮ್ಮಿಗಿ ಅಥವಾ Hammigi ಎಂದು ಟೈಪ್ ಮಾಡಿದಾಗ
            if (input === "ಹಮ್ಮಿಗಿ" || input === "hammigi") {
                resultDiv.style.display = "block";
                resultDiv.className = "success-card";
                resultDiv.innerHTML = "<strong>ಊರು:</strong> ಹಮ್ಮಿಗಿ <br> <strong>ಡಾಕ್ಟರ್ ನಂಬರ್:</strong> <a href='tel:7090593584'>7090593584</a>";
            } else if (input === "") {
                alert("ದಯವಿಟ್ಟು ಊರಿನ ಹೆಸರು ಟೈಪ್ ಮಾಡಿ.");
            } else {
                resultDiv.style.display = "block";
                resultDiv.className = "error-card";
                resultDiv.innerHTML = "ಕ್ಷಮಿಸಿ, ಈ ಊರಿನ ಮಾಹಿತಿ ಲಭ್ಯವಿಲ್ಲ.";
            }
        }
    </script>

</body>
</html>
