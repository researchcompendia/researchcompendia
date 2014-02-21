/* 
 * this toggles the + icons to - icons when a FAQ question is
 * collapsed, and visa versa
 */
$('.panel').on("hidden.bs.collapse", function(e) {
  $icon = $( e.currentTarget ).find( "div#iconstate" )
  $icon.removeClass("icon-plus-sign-alt")
  $icon.addClass("icon-minus-sign-alt")
});
$('.panel').on("shown.bs.collapse", function(e) {
  $icon = $( e.currentTarget ).find( "div#iconstate" )
  $icon.removeClass("icon-minus-sign-alt")
  $icon.addClass("icon-plus-sign-alt")
});

sidebarwidth = $("ul.nav").width()-90; //css('width');
//$('.bs-sidebar').css('width', sidebarwidth);
contentmargin = parseInt(sidebarwidth);
$('.span-fixed-sidebar').css('marginLeft', contentmargin);
