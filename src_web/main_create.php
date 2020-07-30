<script>
function execute(){
  var target = document.getElementById('result');
  var keyword = document.getElementById('keyword').value;
  target.innerHTML = "<font size = '4em'>"+keyword+"</font>";
}

function doOpenCheck(chk){
  var obj = document.getElementsByName("adding");
  for(var i=0; i<obj.length; i++){
      if(obj[i] != chk){
        obj[i].checked = false;
      }
  }
}
</script>
<html>
<meta charset="utf-8">
<title>상호명 생성기</title>
</html>
<body>
  <table width=100% cellpadding="5" cellspacing="0" border="1" bordercolor = "#0D347A" align="center">
    <tr>
      <td bgcolor="#155993">
      <font color = "white" size = "2em">졸업 과제 [효원작명소]</font>
      </td>
      <td width = 10% align="center" bgcolor="#155993">
      <button style="width:80px;height:25px;font-size:15px;" type="button">도움말</button>
      </td>
    </tr>
  </table>
  <table width=100% cellpadding="5" cellspacing="0" border="1" bordercolor = "#0D347A" align="center">
    <tr>
      <td align="center" bgcolor="#318DDB">
      <b><font size = "5em">상호명 생성기</font></b>
      </td>
    </tr>
  </table>
  <table  width=100% cellpadding="10" cellspacing="0" border="1" bordercolor = "#0D347A" align="center" vertical-align = "middle" >
    <form>
    <tr>
      <td align="center" bgcolor="#8EDFFF">
        업종
      </td>
      <td align="left" bgcolor="#D9F8FF">
        <select name = 'big'>
          <option value = "">대분류</option>
          <option value = "음식점">음식점</option>
        </select>
        <select name = 'middle'>
          <option value = "">중분류</option>
          <option value = "음식점">음식점</option>
          </select>
        <select name = 'small'>
          <option value = "">소분류</option>
          <option value = "음식점">음식점</option>
        </select>
      </td>
    </tr>
    <tr>
      <td align="center" bgcolor="#8EDFFF">
        넣고 싶은 단어
      </td>
      <td align="left" bgcolor="#D9F8FF">
        <input type="text" name = 'keyword' id = "keyword" style="width:100px;height:20px;font-size:15px;"  class="box"/>
      </td>
    </tr>
    <tr>
      <td align="center" bgcolor="#8EDFFF">
        후보 수
      </td>
      <td align="left" bgcolor="#D9F8FF">
        <select name = 'candinate'>
          <option value = "">수량</option>
          <option value = "10">10</option>
          <option value = "20">20</option>
          <option value = "30">30</option>
          <option value = "40">40</option>
          <option value = "50">50</option>
        </select>
      </td>
    </tr>
    <tr>
      <td align="center" bgcolor="#8EDFFF">
        업종명을
      </td>
      <td align="left" bgcolor="#D9F8FF">
        붙인다<input type = "checkbox" name = "adding" value= "1" onclick="doOpenCheck(this);">
        안 붙인다<input type = "checkbox" name = "adding" value= "0" onclick="doOpenCheck(this);">
        선택 없음<input type = "checkbox" name = "adding" value= "2" onclick="doOpenCheck(this);">
      </td>
    </tr>
    <tr>
      <td align="center" bgcolor="#8EDFFF">
        차별도
      </td>
      <td align="left" bgcolor="#D9F8FF">
        <input type="range" id="a" name="different" min="10" max="100" value='50' step="10" oninput="document.getElementById('different').innerHTML=this.value;">
        <span id="different"></span>
      </td>
    </tr>
    </form>
  </table>
  <table width=100% cellpadding="5" cellspacing="0" border="1" bordercolor = "#0D347A" align="center">
    <tr>
      <td align="center" bgcolor="#8EDFFF">
        <button style="width:80px;height:25px;font-size:15px;" type="button" onclick="execute();">적  용 </button>
      </td>
    </tr>
  </talbe>
  <table width=100% cellpadding="5" cellspacing="0" border="1" bordercolor = "#0D347A" align="center">
    <tr>
      <td align="left" bgcolor="#D9F8FF" >
        <h1 id = "result"><br></h1>
      </td>
    </tr>
  </talbe>
  <table width=100% cellpadding="5" cellspacing="0" border="1" bordercolor = "#0D347A" align="center">
    <tr>
      <td align="right" bgcolor="#8EDFFF">
        <button style="width:80px;height:25px;font-size:15px;" type="button" onclick="execute();">저  장 </button>
      </td>
    </tr>
  </talbe>
</body>
