<html>
    <head>
        <title>SQL Injection</title>
    </head>
    <body>
        <form action="sql_injection.php" method="post">
            Username:&nbsp<input type=text name="username" id="username">
            Password:&nbsp<input type=password name="password" id="password">
            <input type=submit value="login"> 
        </form>
        <?php
            if($_SERVER["REQUEST_METHOD"] == "POST")
            {
                $servername = "localhost";
                $username = "root";
                $password = "Susan@6298";
                $dbname = "security";
                
                $conn = new mysqli($servername, $username, $password, $dbname);
                
                if($conn->connect_error)
                {
                    die("Connection failed:" . $conn->connect_error);
                }
                
                $username = $_POST["username"];
                $password = $_POST["password"];
                
                $sql = "SELECT * from sql_injection where username = '$username' and password = '$password'";
                
                $result = $conn->query($sql);
                
                if($result->num_rows >0)
                {
                    while($row = $result->fetch_assoc())
                    {
                        echo "username: ". $row["username"]. " is lgged in";
                    }
                }
                else
                {
                    echo "Login failed";
                }
                   
            }
            
        ?>
    </body>
</html>
