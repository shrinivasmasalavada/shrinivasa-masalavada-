<!DOCTYPE html>
<html lang="kn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ವಿದ್ಯಾರ್ಥಿ ಇನ್ನೋವೇಶನ್ ಹಬ್ | Student Innovation Platform</title>
    <style>
        /* ಮೂಲಭೂತ ವಿನ್ಯಾಸ (Reset & Base Styles) */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: #f4f7f6;
            color: #333;
            overflow-x: hidden;
        }

        /* ಬಣ್ಣಗಳು (Colors) */
        :root {
            --primary-color: #2575fc; /* ನೀಲಿ - ತಂತ್ರಜ್ಞಾನದ ಸಂಕೇತ */
            --secondary-color: #6a11cb; /* ನೇರಳೆ - ಸೃಜನಶೀಲತೆಯ ಸಂಕೇತ */
            --accent-color: #ff9f43; /* ಕಿತ್ತಳೆ - ಆಕರ್ಷಣೆಗೆ */
            --text-light: #ffffff;
        }

        /* ಹೆಡರ್ (Header/Navigation) */
        header {
            background: linear-gradient(135deg, var(--secondary-color) 0%, var(--primary-color) 100%);
            padding: 20px 50px;
            color: white;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
            box-shadow: 0 2px 10px rgba(0,0,0,0.2);
        }

        header .logo {
            font-size: 24px;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        nav ul {
            list-style: none;
            display: flex;
            gap: 20px;
        }

        nav a {
            text-decoration: none;
            color: white;
            font-weight: 500;
            transition: color 0.3s;
        }

        nav a:hover {
            color: var(--accent-color);
        }

        /* ಹೀರೋ ಸೆಕ್ಷನ್ (Hero Section) - ಮುಖ್ಯ ಆಕರ್ಷಣೆ */
        .hero {
            height: 100vh;
            background: linear-gradient(135deg, rgba(106, 17, 203, 0.9) 0%, rgba(37, 117, 252, 0.9) 100%), 
                        url('https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?q=80&w=2070') no-repeat center center/cover;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            color: white;
            padding: 0 20px;
            margin-top: 60px; /* Header space */
        }

        .hero h1 {
            font-size: 3.5rem;
            margin-bottom: 20px;
            animation: fadeInDown 1s ease;
        }

        .hero p {
            font-size: 1.5rem;
            margin-bottom: 40px;
            max-width: 700px;
            animation: fadeInUp 1s ease 0.5s;
            animation-fill-mode: both;
        }

        .btn-primary {
            padding: 15px 30px;
            background-color: var(--accent-color);
            color: white;
            text-decoration: none;
            border-radius: 50px;
            font-size: 1.2rem;
            font-weight: bold;
            transition: transform 0.2s, box-shadow 0.2s;
            box-shadow: 0 4px 15px rgba(255, 159, 67, 0.4);
            animation: zoomIn 1s ease 1s;
            animation-fill-mode: both;
        }

        .btn-primary:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(255, 159, 67, 0.6);
        }

        /* ಇನ್ನೋವೇಶನ್ ಗ್ಯಾಲರಿ (Innovation Gallery) */
        .gallery {
            padding: 80px 50px;
            background-color: white;
        }

        .gallery h2 {
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 10px;
            color: var(--secondary-color);
        }

        .gallery p.subtitle {
            text-align: center;
            color: #666;
            margin-bottom: 50px;
            font-size: 1.1rem;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
        }

        .gallery-item {
            background: #fff;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }

        .gallery-item:hover {
            transform: scale(1.05);
        }

        .gallery-item img {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }

        .gallery-item .content {
            padding: 20px;
        }

        .gallery-item h3 {
            font-size: 1.3rem;
            margin-bottom: 10px;
            color: var(--primary-color);
        }

        .gallery-item p {
            color: #555;
            font-size: 0.95rem;
            line-height: 1.5;
        }

        /* ಜಾಯಿನ್ ಸೆಕ್ಷನ್ (Join Us / Sign Up) */
        .join-us {
            padding: 80px 50px;
            background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .form-container {
            background: white;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            width: 100%;
            max-width: 500px;
        }

        .form-container h2 {
            text-align: center;
            color: var(--secondary-color);
            margin-bottom: 30px;
        }

        .form-group {
            margin-bottom: 20px;
        }

        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
        }

        .form-group input, .form-group textarea {
            width: 100%;
            padding: 12px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 1rem;
        }

        .form-group input:focus, .form-group textarea:focus {
            border-color: var(--primary-color);
            outline: none;
        }

        .btn-submit {
            width: 100%;
            padding: 15px;
            background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 1.2rem;
            font-weight: bold;
            cursor: pointer;
            transition: opacity 0.3s;
        }

        .btn-submit:hover {
            opacity: 0.9;
        }

        /* ಫುಟರ್ (Footer) */
        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 30px;
        }

        /* ಅನಿಮೇಷನ್ ವ್ಯಾಖ್ಯಾನಗಳು (Animations) */
        @keyframes fadeInDown {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @keyframes zoomIn {
            from { opacity: 0; transform: scale(0.8); }
            to { opacity: 1; transform: scale(1); }
        }

        /* ಮೊಬೈಲ್ ರೆಸ್ಪಾನ್ಸಿವ್ (Responsive) */
        @media (max-width: 768px) {
            .hero h1 { font-size: 2.5rem; }
            .hero p { font-size: 1.1rem; }
            header { padding: 15px 20px; }
            nav ul { gap: 10px; font-size: 0.9rem; }
            .gallery, .join-us { padding: 50px 20px; }
        }
    </style>
</head>
<body>

    <header>
        <div class="logo">ಇನ್ನೋವೇಶನ್ ಹಬ್</div>
        <nav>
            <ul>
                <li><a href="#home">ಮುಖಪುಟ</a></li>
                <li><a href="#gallery">ಸಾಧನೆಗಳು</a></li>
                <li><a href="#join">ನೋಂದಣಿ</a></li>
            </ul>
        </nav>
    </header>

    <section class="hero" id="home">
        <h1>ನಿಮ್ಮ ಐಡಿಯಾ, ಜಗತ್ತನ್ನು ಬದಲಿಸಬಲ್ಲದು!</h1>
        <p>ನೀವು ಶಾಲಾ-ಕಾಲೇಜು ವಿದ್ಯಾರ್ಥಿಯೇ? ನಿಮ್ಮ ಬಳಿ ಅದ್ಭುತವಾದ ನಾವೀನ್ಯತೆಯ ಐಡಿಯಾ ಇದೆಯೇ? ಅದನ್ನು ನನಸಾಗಿಸಲು ನಾವು ಸಹಾಯ ಮಾಡುತ್ತೇವೆ.</p>
        <a href="#join" class="btn-primary">ನಿಮ್ಮ ಐಡಿಯಾ ಹಂಚಿಕೊಳ್ಳಿ</a>
    </section>

    <section class="gallery" id="gallery">
        <h2>ವಿದ್ಯಾರ್ಥಿಗಳ ಸಾಧನೆಯ ಹಾದಿ</h2>
        <p class="subtitle">ನಮ್ಮ ಪ್ಲಾಟ್‌ಫಾರ್ಮ್ ಮೂಲಕ ಮೂಡಿಬಂದ ಕೆಲವು ಅದ್ಭುತ ಪ್ರಾಜೆಕ್ಟ್‌ಗಳು</p>
        
        <div class="grid">
            <div class="gallery-item">
                <img src="https://images.unsplash.com/photo-1581092921461-39b9d08a9b21?q=80&w=600" alt="ರೋಬೋಟಿಕ್ಸ್ ಪ್ರಾಜೆಕ್ಟ್">
                <div class="content">
                    <h3>ಸ್ಮಾರ್ಟ್ ಕೃಷಿ ರೋಬೋಟ್</h3>
                    <p>8ನೇ ತರಗತಿಯ ಸುರೇಶ್ ತಯಾರಿಸಿದ, ಹೊಲದಲ್ಲಿ ಕಳೆ ತೆಗೆಯುವ ಮತ್ತು ನೀರುಣಿಸುವ ಸ್ವಯಂಚಾಲಿತ ರೋಬೋಟ್.</p>
                </div>
            </div>

            <div class="gallery-item">
                <img src="https://images.unsplash.com/photo-1531297484001-80022131f5a1?q=80&w=600" alt="AI ಪ್ರಾಜೆಕ್ಟ್">
                <div class="content">
                    <h3>ವನ್ಯಜೀವಿ ಸಂರಕ್ಷಣಾ ಸರಣಿ</h3>
                    <p>ಕಾಲೇಜು ವಿದ್ಯಾರ್ಥಿನಿ ರಮ್ಯಾ ಅಭಿವೃದ್ಧಿಪಡಿಸಿದ, ರೈಲ್ವೆ ಹಳಿಗಳ ಮೇಲೆ ಪ್ರಾಣಿಗಳನ್ನು ಗುರುತಿಸಿ ಅಪಘಾತ ತಪ್ಪಿಸುವ AI ವ್ಯವಸ್ಥೆ.</p>
                </div>
            </div>

            <div class="gallery-item">
                <img src="https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=600" alt="ಎಲೆಕ್ಟ್ರಾನಿಕ್ಸ್ ಪ್ರಾಜೆಕ್ಟ್">
                <div class="content">
                    <h3>ಕಡಿಮೆ ವೆಚ್ಚದ ಈಸಿಜಿ (ECG)</h3>
                    <p>ಹಳ್ಳಿಯ ಜನರಿಗಾಗಿ 10ನೇ ತರಗತಿಯ ತಂಡವೊಂದು ಸಿದ್ಧಪಡಿಸಿದ ಪೋರ್ಟಬಲ್ ಈಸಿಜಿ ಯಂತ್ರ.</p>
                </div>
            </div>
            
            <div class="gallery-item">
                <img src="https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=600" alt="ಸೈಬರ್ ಭದ್ರತೆ">
                <div class="content">
                    <h3>ಸುರಕ್ಷಿತ ಚಾಟ್ ಆಪ್</h3>
                    <p>ವಿದ್ಯಾರ್ಥಿಗಳ ಡೇಟಾ ಸೋರಿಕೆಯಾಗದಂತೆ ತಡೆಯುವ ಎನ್‌ಕ್ರಿಪ್ಟೆಡ್ ಮೆಸೇಜಿಂಗ್ ಅಪ್ಲಿಕೇಶನ್.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="join-us" id="join">
        <div class="form-container">
            <h2>ನಮ್ಮೊಂದಿಗೆ ಕೈಜೋಡಿಸಿ</h2>
            <form>
                <div class="form-group">
                    <label for="name">ಹೆಸರು:</label>
                    <input type="text" id="name" placeholder="ನಿಮ್ಮ ಪೂರ್ಣ ಹೆಸರು">
                </div>
                <div class="form-group">
                    <label for="email">ಇಮೇಲ್:</label>
                    <input type="email" id="email" placeholder="ನಿಮ್ಮ ಇಮೇಲ್ ವಿಳಾಸ">
                </div>
                <div class="form-group">
                    <label for="idea">ನಿಮ್ಮ ಐಡಿಯಾ (ಸಂಕ್ಷಿಪ್ತವಾಗಿ):</label>
                    <textarea id="idea" rows="5" placeholder="ನಿಮ್ಮ ಇನ್ನೋವೇಶನ್ ಬಗ್ಗೆ ಬರೆಯಿರಿ..."></textarea>
                </div>
                <button type="submit" class="btn-submit">ಸಲ್ಲಿಸಿ</button>
            </form>
        </div>
    </section>

    <footer>
        <p>&copy; 2023 ವಿದ್ಯಾರ್ಥಿ ಇನ್ನೋವೇಶನ್ ಪ್ಲಾಟ್‌ಫಾರ್ಮ್. ಎಲ್ಲ ಹಕ್ಕುಗಳನ್ನು ಕಾಯ್ದಿರಿಸಲಾಗಿದೆ.</p>
    </footer>

</body>
</html>
