<script>
function agreeProvidingIdentity(){
  var chk=false;
  var objChk = document.getElementsByName("identity");
  var phoneNum = document.getElementById("custom_phone").value;

  for(var i=0; i<objChk.length; i++){
    if (objChk[i].checked){
      chk=true;
      if(phoneNum != ''){
        return true;
      }
      else {
        alert('전화번호를 입력해주세요.');
        return false;
      }
    }
  }
  if(phoneNum != ''){
    for(var i=0; i<objChk.length; i++){
      if(objChk[i].checked){
        chk = true;
        return true;
      }
      else {
        alert('동의합니다를 체크해주세요.');
        return false;
      }
    }
  }
  return true;
}

function nextPage(frm){
  frm.action = './main.php';
  frm.submit();
  return true;
}

</script>
<html>
<head>
<style type="text/css">
.my-box { border:1px solid; padding:10px; }
</style>
</head>
<body>
  <?
  session_start();
  //if(!empty($_SESSION['phoneNum'] )&& $_SESSION['phoneNum']  == 'default'){
    //echo "같다!";
  //}
  if (!empty($_SESSION['phoneNum'])){

      //session_destroy();
      //unset( $_SESSION['phoneNum'] );
      echo "<script>location.href='./main.php'</script>";
  }
  ?>
  <form action='./main.php' id = "privideIdentity" method='post' onsubmit="return agreeProvidingIdentity();">
<br>
<br>
<CENTER><font size = "6em"><b>[상호명 설문조사]</b></font></div><br></CENTER><br>
<div><font size="4em">
안녕하십니까.<br>
 저희는 부산대학교 전기컴퓨터공학부 정보컴퓨터공학전공 <졸업과제를 진행 중인 ‘효원작명소’ 팀 입니다.<br>
현재 상호명에서 느껴지는 분위기와 특성을 조사하기 위하여 온라인 설문조사를 진행하고 있습니다.<br>
<br>
* 연락처를 남기시면 추첨을 통하여 기프티콘을 드립니다.<br>
* 반복적으로 참여가 가능하며, 참여횟수가 많을수록 당첨 확률이 올라갑니다.<br><br>
<div class="my-box">
◎ 개인정보 취급방침<br>
작성하신 실명과 전화번호는 개인정보보호법 제 15조 및 제 22조에 의거, 경품 추첨 및 발송용도로만 사용되며 이벤트가 진행되는 기간 동안만 보관하게 됩니다. <br>
수집된 개인 정보는 휴대전화 번호이며 경품발송의 목적으로만 사용됩니다. <br>
<br>
- 개인정보의 수집, 이용 목적: 경품 추첨 및 발송<br>
- 수집하려는 개인정보의 항목: 휴대폰 번호<br>
- 개인정보의 보유 및 이용기간: 경품발송 7일 후 파기<br>
</div>
</div>
</font>
<br>
<form action="" method="post">
<div style = "float: right;"><input type = "checkbox" name = "identity" value= "profession1"><font size = "4em"><b>동의합니다.</b></font></div>
<br><br>
<CENTER><label>전화 번호 : </label><input type="text" name = 'phoneNum' id = "custom_phone" minlength="11" maxlength="11" style="width:200px;height:30px;font-size:20px;"  class="box"/></br></CENTER>
<br>
<center><div><input type="submit" style="width:150px;height:35px;font-size:20px;" value="제출하기"/></center><br>
<div style = "float: right;"><input type="submit" style="width:100px;height:30px;font-size:15px;" value="넘어가기" onclick='return nextPage(this.form);'/></div>
<div><font size="3em"><문의> ‘효원작명소’ 팀장 신인철 incheol.shin97@gmail.com / 김승민 mimi9693@gmail.com</div></font>
<input type = "hidden" id = "input_phone" name = "input_phone">

</form>
</body>

</html>
