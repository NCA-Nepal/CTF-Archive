<?php
if (isset($_GET["username"])) {
    $encodedUsername = str_replace("=", "", $_GET["username"]);

    if ($encodedUsername === "YWRtaW4") {
        $decodedUsername = "";
    } else {
        $decodedUsername = base64_decode($encodedUsername);

        if (!preg_match('/^[a-zA-Z0-9_]+$/', $decodedUsername)) {
            $decodedUsername = "";
        }
    }
}

$flagContents = file_get_contents("123po12n4p358y23kjriu3grip395k23b4i2_flag_23k45gi2nekjh2e8h02ek4325b4uro892304j4h2ygjsfsuy2394kqdli49.txt");
$flagMessage = "<pre>" . htmlspecialchars($flagContents) . "</pre>";
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mero Kitab</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
    <style>
        body {
            background-color: #121212;
            color: #ffffff;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .container {
            margin-top: 50px;
            text-align: center;
        }
        a {
            color: #ffffff;
        }
        h1 {
            color: #00ff6f;
        }
        p {
            color: #d3d3d3;
        }
        .error {
            color: #ff4c4c;
        }
        .btn-custom {
            background-color: #00ff6f;
            color: #121212;
        }
    </style>
</head>
<body>
    <div class="container">
        <?php if (!isset($_GET["username"])): ?>
            <h1>Mero Kitab</h1>
            <p>Specify a username in base64 to access your kitab.</p>
            <p>Example: <a href="/?username=<?php echo base64_encode("haribahadur"); ?>" class="btn btn-custom"><i class="fas fa-user"></i> haribahadur</a></p>
            <p><i class="fas fa-exclamation-triangle"></i> Admin kitab are restricted to view</p>
        
        <?php else: ?>
            <?php if ($decodedUsername === ""): ?>
                <h1>Error</h1>
                <p class="error">Invalid username</p>

            <?php elseif ($decodedUsername === "admin"): ?>
                <h1>Welcome admin!</h1>
                <p><?php echo $flagMessage; ?></p>

            <?php else: ?>
                <h1>Welcome <?php echo htmlspecialchars($decodedUsername); ?>!</h1>
                <p>No kitab available for you!</p>
                
            <?php endif; ?>
        <?php endif; ?>
    </div>
</body>
</html>
