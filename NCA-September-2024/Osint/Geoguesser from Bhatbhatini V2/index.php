<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Geoguesser V2</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet" />
    <link rel="stylesheet" href="style.css" />
    <style>
        body {
            background-color: #1e1e1e;
            color: #0f0;
            font-family: 'Courier New', Courier, monospace;
        }
        .container {
            max-width: 1200px;
        }
        .center-content {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .picture-item {
            max-width: 100%;
            width: 300px;
            margin: 10px;
            border: 2px solid #0f0;
            border-radius: 5px;
            padding: 10px;
        }
        .picture-item img {
            border: 1px solid #0f0;
            border-radius: 5px;
        }
        .form-control {
            background-color: #333;
            color: #0f0;
            border: 1px solid #0f0;
        }
        .form-control::placeholder {
            color: #0f0;
        }
        .btn-primary {
            background-color: #0f0;
            border: none;
        }
        .btn-primary:hover {
            background-color: #0c0;
        }
        .text-success {
            color: #0f0;
        }
        .text-danger {
            color: #f00;
        }
    </style>
</head>
<body>
    <div class="container mt-5 center-content">
        <h1 class="text-center mb-4">Guess the Picture Name!</h1>

        <div id="result" class="text-center mb-4">
            <?php
            if ($_SERVER["REQUEST_METHOD"] == "POST") {
                $answers = [
                    1 => ["Mendelssohn-Haus", "bmNhe"],
                    2 => ["Son Kol", "2czMF8"],
                    3 => ["Shark Pit", "1bTQ1a"],
                    4 => ["Oslo Cathedral", "F9iM"],
                    5 => ["Vatnajökull National Park", "DBtX"],
                    6 => ["Gold Coast beach", "0Mwbm"],
                    7 => ["Shey Phoksundo National Park", "dyNH"],
                    8 => ["Sanam Luang", "Q1fQ"]
                ];

                for ($i = 1; $i <= 8; $i++) {
                    if (isset($_POST['submit' . $i])) {
                        $userGuess = strtolower(trim($_POST['guess' . $i]));

                        if (array_key_exists($i, $answers)) {
                            list($correctAnswer, $code) = $answers[$i];
                            $result = $userGuess === strtolower($correctAnswer)
                                ? "Correct! Your code is: $code"
                                : "Incorrect. Try again!";
                            echo "<div class='text-center mb-2'>";
                            echo "<strong>Picture $i: </strong>";
                            echo "<span class='" . ($userGuess === strtolower($correctAnswer) ? 'text-success' : 'text-danger') . "'>$result</span>";
                            echo "</div>";
                        }
                    }
                }
            }
            ?>
        </div>

        <div class="row justify-content-center">
            <?php
            $pictures = [
                ["src" => "imgs/pic1.jpg", "alt" => "Picture 1", "number" => 1, "hint" => "Image 1"],
                ["src" => "imgs/pic2.jpg", "alt" => "Picture 2", "number" => 2, "hint" => "Image 2"],
                ["src" => "imgs/pic3.jpg", "alt" => "Picture 3", "number" => 3, "hint" => "Image 3"],
                ["src" => "imgs/pic4.jpg", "alt" => "Picture 4", "number" => 4, "hint" => "Image 4"],
                ["src" => "imgs/pic5.jpg", "alt" => "Picture 5", "number" => 5, "hint" => "Image 5"],
                ["src" => "imgs/pic6.jpg", "alt" => "Picture 6", "number" => 6, "hint" => "Image 6"],
                ["src" => "imgs/pic7.jpg", "alt" => "Picture 7", "number" => 7, "hint" => "Image 7"],
                ["src" => "imgs/pic8.jpg", "alt" => "Picture 8", "number" => 8, "hint" => "Image 8"],
            ];

            foreach ($pictures as $pic) {
                echo '<div class="col-md-3 d-flex justify-content-center">';
                echo '<div class="picture-item">';
                echo "<img src='{$pic['src']}' alt='{$pic['alt']}' class='img-fluid' />";
                echo "<h3>{$pic['hint']}</h3>";
                echo "<form method='post' action=''>";
                echo "<input type='text' name='guess{$pic['number']}' class='form-control mb-2' placeholder='Your Guess' />";
                echo "<button type='submit' class='btn btn-primary' name='submit{$pic['number']}'>Submit</button>";
                echo "</form>";
                echo '</div>';
                echo '</div>';
            }
            ?>
        </div>
    </div>

    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
