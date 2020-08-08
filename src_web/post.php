
<html>
  <head>
  </head>
  <body>
    <?php
        $mood = $_POST['mood'];
        $unique = $_POST['unique'];
        $harmony = $_POST['harmony'];

        session_start();
        $storeName = $_SESSION['storeName'];
        $phoneNum = $_SESSION['phoneNum'];
        $store_divisionName3 = $_SESSION['store_divisionName3'];
        $store_industryName = $_SESSION['store_industryName'];

        require $_SERVER['DOCUMENT_ROOT'].'/dbconnection.php';
        $connect=dbconn();

        $query = "INSERT INTO identity(phoneNumber) VALUES ('$phoneNum')";
        mysqli_query($connect,$query);
        $query="UPDATE store SET  survey_check = 1, question1 = $mood, question2= $unique, question3 = $harmony WHERE store_name = '$storeName' AND store_divisionName3 = '$store_divisionName3' AND store_industryName = '$store_industryName'";
        mysqli_query($connect, $query);

        /*$query="SELECT survey_check, question1, question2, question3 FROM store WHERE store_name = '$storeName'";
        $result = mysqli_query($connect,$query);
        while($row = mysqli_fetch_row($result)){
          echo $row[0].'<br>'.$row[1].'<br>'.$row[2].'<br>'.$row[3].'<br>';
          echo '<br>';
          , store_divisionName3 = '$store_divisionName3',store_industryName = '$store_industryName'
        }
        */
        //echo $store_divisionName3.'<br>'.$store_industryName.'<br>';
        mysqli_close($connect);
        echo "<script>alert('{$storeName}를 DB로 전송합니다.');</script>";
        echo "<b><font size = '6em'>".'참여해주셔서 감사합니다.'.'</b></font>';
        echo "<script>location.href='./main.php'</script>";
    ?>
    <br>
  </form>
  <body/>
</html>
