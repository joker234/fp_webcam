$(document).ready(function(){
  var highlight_btn = function(dire) {
    if (dire == "up") {
      $("#up").focus();
    } else if (dire == "left") {
      $("#left").focus();
    } else if (dire == "right") {
      $("#right").focus();
    } else if (dire == "down") {
      $("#down").focus();
    } else if (dire == "defaultpos") {
      $("#defaultpos").focus();
    }
  }

  var move = function(dire) {
    url="/move";
    $.get(url, { dire: dire });
    highlight_btn(dire);
  }

  // execute move on click
  $("#up").click(function(){
    move("up");
  });
  $("#left").click(function(){
    move("left");
  });
  $("#right").click(function(){
    move("right");
  });
  $("#down").click(function(){
    move("down");
  });
  $("#defaultpos").click(function(){
    move("defaultpos");
  });

  // execute move on swipe
  $("body").on("swipeup",function(){
    move("down");
  });
  $("body").on("swipeleft",function(){
    move("right");
  });
  $("body").on("swiperight",function(){
    move("left");
  });
  $("body").on("swipedown",function(){
    move("up");
  });

  $("body").keydown(function(event){
    if (event.which == 38) {
      move("up");
    } else if (event.which == 37) {
      move("left");
    } else if (event.which == 39) {
      move("right");
    } else if (event.which == 40) {
      move("down");
    }
  });
});
