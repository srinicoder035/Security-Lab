<html>

<head>
    <title>XSS Attack</title>
</head>

<body>
    <form action="xss.php" method="POST">
        First name: <input type="text" name="firstname" value=""><br>
        Last name: <input type="text" name="lastname" value=""><br>
        <input type="submit" value="Submit">
    </form>
</body>

<?php
if (isset($_POST["firstname"]) && isset($_POST["lastname"])) {
    $firstname = $_POST["firstname"];
    $lastname = $_POST["lastname"];
    if ((strpos($firstname, "<script>") !== false) ||  (strpos($lastname, "<script>") !== false) ){
        echo "Cross Site Scripting";
    }else {
        if ($firstname == "" or $lastname == "") {
            echo "<font color=\"red\">Please enter both fields...</font>";
        } else {
            echo "Welcome " . $firstname . " " . $lastname;
        }
    }
}
?>

</html>