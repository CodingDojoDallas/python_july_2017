//Ninja.js

$( document ).ready(function() {

    $('img').click(function(){
      $(this).fadeOut();
    });

    $('#restore_button').click(function(){
      $('img').show();
    });
});
