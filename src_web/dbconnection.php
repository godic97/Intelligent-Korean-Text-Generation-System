<?
function dbconn(){
$host_name="localhost";
$db_user_id ="root";
$db_name="store_db";
$db_pw="autoset";
$connect=@mysqli_connect($host_name, $db_user_id, $db_pw);
//mysqli_query("set names utf8", $connect);
mysqli_select_db($connect, $db_name);
if(!$connect)die("연결에 실패".mysqli_error());
return $connect;
}

//에러메세지 출력
function Error($msg)
{
  echo"
  <script>
  window.alert('$msg');
  history.back(1);
  </script>
  ";
  exit; //위 에러 메세지만 띄우기
}
?>
