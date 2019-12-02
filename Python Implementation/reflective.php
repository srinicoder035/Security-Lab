<!DOCTYPE html>
<html>
<head>
<title> aishd</title>
</head>
<body>
<form action='reflective.php' method='post'>
name:<input type=text name='name' id='name'>
<input type=submit value='submit'>
</form>
<?php
    if($_SERVER['REQUEST_METHOD'] == 'POST')
    {
        if(strpos($_POST['name'],'<script>') !== false)
            echo 'XSSSSS';
        else
            echo 'not xsssss';
    }
?>
</body>
</html>
