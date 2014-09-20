$(document).ready(function(){
  var move = function(dire) {
    url="/move";
    $.get(
      url,
      { dire: dire });
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
});
