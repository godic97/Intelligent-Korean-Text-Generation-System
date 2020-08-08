<script>
function doOpenCheck1(chk){
          var obj = document.getElementsByName("mood");
          for(var i=0; i<obj.length; i++){
              if(obj[i] != chk){
                obj[i].checked = false;
          }
      }
}

function doOpenCheck2(chk){
          var obj = document.getElementsByName("unique");
          for(var i=0; i<obj.length; i++){
              if(obj[i] != chk){
                obj[i].checked = false;
          }
      }
}

function doOpenCheck3(chk){
          var obj = document.getElementsByName("harmony");
          for(var i=0; i<obj.length; i++){
              if(obj[i] != chk){
                obj[i].checked = false;
          }
      }
}


function doCheckForm(){
       var chk1=false;
       var chk2=false;
       var chk3=false;

       var obj = document.getElementsByName("mood");
       for(var i=0; i<obj.length; i++){
           if(obj[i].checked){
             chk1=true;
             break;
           }
       }
       var obj = document.getElementsByName("unique");
       for(var i=0; i<obj.length; i++){
           if(obj[i].checked){
             chk2=true;
             break;
           }
       }

       var obj = document.getElementsByName("harmony");
       for(var i=0; i<obj.length; i++){
           if(obj[i].checked){
             chk3=true;
             break;
           }
       }
       if(!chk1){
           alert('[질문 1]에 답해주세요');
           return false;
       }
       else if(!chk2) {
           alert('[질문 2]에 답해주세요');
           return false;
       }
       else if(!chk3) {
           alert('[질문 3]에 답해주세요');
           return false;
       }
       return true;
   }
</script>
<html>
<head>
<meta charset="utf-8">
<title>상호명 설문조사</title>
</head>
<body>

<br>
<br>
<CENTER><font size = "5em"><b>[상호명 설문조사]</b></font></div><br>
<br>
  <?php

      session_start();
      if (empty($_SESSION['phoneNum'])){
        if(empty($_POST['phoneNum'])){
            $_SESSION['phoneNum'] = 'default';
        }
        else $_SESSION['phoneNum'] = $_POST['phoneNum'];
      }

      require $_SERVER['DOCUMENT_ROOT'].'/dbconnection.php';
      $connect=dbconn();

      $query = "SELECT store_name, store_divisionName3, store_industryName FROM store WHERE survey_check = 0 ORDER BY RAND() LIMIT 1";
      $result = mysqli_query($connect,$query);
      while($row = mysqli_fetch_row($result)){
        echo "<b><font size = '6em'>{$row[0]}</b></font><br><font size = '4em'>({$row[1]}, {$row[2]})</font>";
        echo '<br>';
        $_SESSION['storeName'] = $row[0];
        $_SESSION['store_divisionName3'] = $row[1];
        $_SESSION['store_industryName'] = $row[2];
      }

      $query = "SELECT store_name FROM store";
      $result = mysqli_query($connect,$query);
      $all_store = mysqli_num_rows($result);

      $query = "SELECT store_name FROM store WHERE survey_check = 0" ;
      $result = mysqli_query($connect,$query);
      $part_store = mysqli_num_rows($result);

      echo '<font size="3em">'.'<br>'.$part_store.'/'.$all_store.'<br>'.'</font>';

      mysqli_close($connect);
  ?>
<br><br></CENTER>
<form id = "storeSurvey" action="./post.php" method="post" onsubmit="return doCheckForm();">

<font size="4em"><div><b>1. 상호명에서 느껴지는 바가 무엇입니까?</b><br></font></div>
<div style = "float: right;"><font size="4em">
<b>세련</b>되고 <b>모던함</b>이 느껴진다.
<input type = "checkbox" name = "mood" value= "1" onclick="doOpenCheck1(this);">
<b>정답고 친숙함</b>이 느껴진다.
<input type = "checkbox" name = "mood" value= "0" onclick="doOpenCheck1(this);">
</font></div>
<br><br><br>

<font size="4em"><div><b>2. 주변에서 흔히 볼 수 있는 이름입니까?</b><br></font></div>
<div style = "float: right;"><font size="4em">
흔하지 않고 <b>독특</b>하다.
<input type = "checkbox" name = "unique" value= "1" onclick="doOpenCheck2(this);">
<b>흔한</B> 상호명이다.
<input type = "checkbox" name = "unique" value= "0" onclick="doOpenCheck2(this);">
</font></div>
<br><br><br>

<font size="4em"><div><b>3. ○○부동산, ○○미용실과 같이 특정업종에만 사용할 수 있습니까?</b><br></font></div>
<div style = "float: right;"><font size="4em">
<b>예</b>.
<input type = "checkbox" name = "harmony" value= "1" onclick="doOpenCheck3(this);">
<b>아니오</B>.
<input type = "checkbox" name = "harmony" value= "0" onclick="doOpenCheck3(this);">
</font></div>

<br><br><br>
<div style = "float: right;"><input style="width:150px;height:35px;font-size:20px;" type="submit" value="완료"></div>

<input type = "hidden" value = "<?php echo $_POST['phoneNum']?>" name = "phoneNum"/><br><br>
<div><font size="3em"><문의> ‘효원작명소’ 팀장 신인철 incheol.shin97@gmail.com / 김승민 mimi9693@gmail.com</div></font>
</form>

</body>

</html>
