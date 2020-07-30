<script>
function doOpenCheck1(chk){
          var obj = document.getElementsByName("mood");
          for(var i=0; i<obj.length; i++){
              if(obj[i] != chk){
                obj[i].checked = false;
          }
      }
}
</script>

<html>
<head>
<meta charset="utf-8">
<title>상호명 생성기</title>
<style type="text/css">
.my-box { border:1px solid; padding:10px; }
</style>
</head>



<div style = "float: right;"><button style="width:80px;height:25px;font-size:15px;" type="button">도움말</button></div>
<br><br>

<table width="400" cellpadding="0" cellspacing="0" border="0" align="center">
  <tr align="center">
   <td><b><font size = "5em">상호명 생성기</font></b></td>
  </tr>
<tr height="15">
  <td colspan="7"><!-- 여백 --></td>
</tr>
<table width="400" cellpadding="0" cellspacing="0" border="0" align="center">
<tr>
   <td width="200" valign="top" bgcolor="#8080FF">
    <table width="180" cellpadding="5" cellspacing="0" border="0" align="center">
    <tr align = "center">
     <td>업종</td>
    </tr>
    <tr align = "center">
     <td>넣고 싶은 단어</td>
    </tr>
    <tr align = "center">
     <td>후보 수</td>
    </tr>
    <tr align = "center">
     <td>업종명을</td>
    </tr>
    <tr align = "center">
     <td>차별도</td>
    </tr>
    </table>
   </td>
   <td width="300" valign="top">
    <table width="280" cellpadding="5" cellspacing="0" border="1" align="center">
    <tr>
      <td>
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
      <td>
        <input type="text" name = 'keyword' id = "keyword" style="width:100px;height:20px;font-size:15px;"  class="box"/>
     </td>
    </tr>
    <tr>
      <td>
        <select name = 'candinate'>
          <option value = "">수량</option>
          <option value = "5">5</option>
          <option value = "10">10</option>
          <option value = "20">20</option>
          <option value = "30">30</option>
          <option value = "40">40</option>
          <option value = "50">50</option>
        </select>
      </td>
    </tr>
    <tr>
      <td>
        <form>
          붙인다<input type = "checkbox" name = "adding" value= "1">
          안 붙인다<input type = "checkbox" name = "adding" value= "0">
          선택 없음<input type = "checkbox" name = "adding" value= "2">
        </form>
      </td>
    </tr>
    <tr>
      <td>
         <form>
         <input type="range" id="a" name="ages" min="10" max="60" step="10">
         </form>
      </td>
    </tr>
    </table>
   </td>
</tr>
</table>

</html>
