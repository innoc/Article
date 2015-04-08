(function($) {
  $.fn.invisible = function() {
      return this.each(function() {
          $(this).css("visibility", "hidden");
      });
  };
  $.fn.visible = function() {
      return this.each(function() {
          $(this).css("visibility", "visible");
      });
  };
}(jQuery));

$(document).ready(function(){  
  $(".sidebar--bottom__responsive").click(function(){
    var visible = $('.sidebar--bottom__nav').css("visibility") == "visible"; 
    if(visible)
    {
      $(".sidebar").css({height: "200px"});
      $(".sidebar--bottom__nav").invisible();
    }
    else {       
      $(".sidebar--bottom__nav").visible();
      $(".sidebar").css({height: "630px"});
    }
  });

  $(window).resize(function() {
    if($(window).width() > 757)
    {
      $(".sidebar--bottom__nav").visible();
      $(".sidebar").css({height: "630px"});
    }
    else{ 
     $(".sidebar").css({height: "200px"});
      $(".sidebar--bottom__nav").invisible(); 
    }
  });
})