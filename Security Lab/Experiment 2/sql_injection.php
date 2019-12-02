<html>
<head>
    <title>SQL Injection</title>
</head>
<body>
    <form action="sql_injection.php" method="post">
        Enter the username:&nbsp;<input type=text id="username" name="username"><br>
        Enter the password:&nbsp;<input type=password id="password" name="password"><br>
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

        $user = $_POST["username"];
        $pass = $_POST["password"];
        $sql = "SELECT * FROM Login where userName = '$user' and passWord ='$pass' ";
        $result = $conn->query($sql);
        if ($result->num_rows > 0) {
            echo "Login Successful";
        } else {
            echo "Failed Login";
        }
    }
    ?>
</body>
</html>