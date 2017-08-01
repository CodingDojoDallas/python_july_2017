//jQueryBasicAssignment.js
$(document).ready(function(){

  $("#button_click").click(function(){
  alert("Hello");
  });

  $("#button_hide").click(function(){
    $("img").hide();
  });

  $("#button_show").click(function(){
    $("img").show();
  });

  $("#button_toggle").click(function(){
    $("img").toggle();
  });

  $("#button_slidedown").click(function(){
    if ($( "img").is( ":hidden")){
      $("img").slideDown("slow");
    } else {
      $("img").hide();
    }
  });

  $("#button_slideup").click(function(){
    if ($( "img").is( ":hidden")){
      $("img").show("slow");
    } else {
      $("img").slideUp();
    }
  });

  $("#button_slidetoggle").click(function(){
    $("p").slideToggle("slow");
  });

  $("#button_fadein").click(function(){
    $("p").hide();
    $("p").fadeIn(2500);
  });

  $("#button_fadeout").click(function(){
    $("p").show();
    $("p").fadeOut(2500);
  });

  $("#button_addclass").click(function(){
    $("h4").addClass("selected")
  });

  $("#button_before").click(function(){
    $("#before").before($("#after"));
  });

  $("#button_after").click(function(){
    $("#before").after($("#after"));
  });

  $("#button_append").click(function(){
    $("#appendme").append(" World!");
  });

  $("h2").click(function(){
    $(this).html("<p>Now it's changed</p>");
  });

  $( "input" )
    .keyup(function() {
      var value = $( this ).val();
      $( "h4" ).text( value );
    })
    .keyup();
    
});
