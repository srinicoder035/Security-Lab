<html>
<head>
    <title>SQL Injection</title>
</head>
<body>
    <form action="sql_injection1.php" method="post">
        Enter the id:&nbsp;<input type=text id="id" name="id"><br>
        <input type="submit" value="Submit">
    </form>
    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $servername = "localhost";
        $username = "root";
        $password = "srini1998";
        $dbname = "Base1";

        $conn = new mysqli($servername, $username, $password, $dbname);

        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }

        $user = $_POST["id"];
        $sql = "SELECT * FROM Data where age = " .$user;
        if ($conn->multi_query($sql)) {
            echo "Login Successful";
        } else {
            echo "Failed Login";
        }
    }
    ?>
</body>
</html>