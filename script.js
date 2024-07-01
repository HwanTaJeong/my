function getValueInText() {
  let userid = document.getElementById("userid").value;
  let userpw = document.getElementById("userpw").value;

  if (userid == "admin" && userpw == "1234") {
    alert("Suceess!");
  }
  else {
    alert("Passward wrong!");
  }
}
