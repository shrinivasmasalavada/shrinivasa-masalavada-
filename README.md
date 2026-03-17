<!DOCTYPE html>
<html lang="kn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fun Search Bar</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            background-color: #f0f2f5;
        }
        .container {
            text-align: center;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        input {
            padding: 10px;
            width: 250px;
            border: 2px solid #ddd;
            border-radius: 5px;
            font-size: 16px;
        }
        #message {
            margin-top: 20px;
            font-size: 20px;
            font-weight: bold;
            color: #e74c3c;
            height: 30px; /* ಜಾಗ ಖಾಲಿ ಇರಲು */
        }
    </style>
</head>
<body>

    <div class="container">
        <h2>ಏನನ್ನಾದರೂ ಟೈಪ್ ಮಾಡಿ...</h2>
        <input type="text" id="searchBar" placeholder="ಇಲ್ಲಿ ಟೈಪ್ ಮಾಡಿ..." oninput="showMessage()">
        <div id="message"></div>
    </div>

    <script>
        function showMessage() {
            const inputVal = document.getElementById('searchBar').value;
            const messageDiv = document.getElementById('message');

            // ಸರ್ಚ್ ಬಾರ್‌ನಲ್ಲಿ 'hi' ಎಂದು ಟೈಪ್ ಮಾಡಿದರೆ ಮಾತ್ರ ಬರಬೇಕೆಂದರೆ ಈ ಕೆಳಗಿನ 'if' ಬಳಸಿ
            // ಇಲ್ಲದಿದ್ದರೆ ಯಾವುದಾದರೂ ಅಕ್ಷರ ಟೈಪ್ ಮಾಡಿದ ತಕ್ಷಣ ಮೆಸೇಜ್ ಬರುತ್ತದೆ.
            if (inputVal.toLowerCase() === 'hi') {
                messageDiv.innerText = "hello gaandu na kano";
            } else if (inputVal === "") {
                messageDiv.innerText = "";
            }
        }
    </script>

</body>
</html>
