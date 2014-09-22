$(document).ready(function(){
  var move = function(dire) {
    url="/move";
    $.get(url, { dire: dire });
    $("#direction").text(dire);
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
