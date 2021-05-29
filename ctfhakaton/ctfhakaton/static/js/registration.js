$("#newUser").click(function(){
    $("h1").text("Регистрация")
    $("#registration-form")[0].style.display = 'block'
    $("#login-form")[0].style.display = 'none'
    $('#newUser')[0].style.display = 'none'
    $('#logIn')[0].style.display = 'block'
  $(".logo").css({
    "width":"120px",
    "height":"120px",
    "top":"10px"
  });
})

$("#logIn").click(function(){
    $("h1").text("Войти")
    $("#login-form")[0].style.display = 'block'
    $("#registration-form")[0].style.display = 'none'
    $('#logIn')[0].style.display = 'none'
    $('#newUser')[0].style.display = 'block'
  $(".logo").css({
    "width":"120px",
    "height":"120px",
    "top":"10px"
  });
})

$("#signup-btn,#login-btn").click(function(){
  $("h1").text("Войти");
  $(".logo").css({
    "width":"150px",
    "height":"150px",
    "top":"30px"
  });

  $("#registration-form,#fpass-form").fadeOut(200);
  $("#login-form").delay(300).fadeIn(500);
  $(".other-options").fadeIn(300);
});

$("#fPass").click(function(){
  $("h1").text("Забыли пароль?");
  $(".logo").css({
    "width":"190px",
    "height":"190px",
    "top":"40px"
  });

  $("#login-form").fadeOut(200);
  $("#fpass-form").delay(300).fadeIn(500);
  //$(".other-options").fadeOut(200);
});