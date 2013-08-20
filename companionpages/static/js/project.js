/* this is broken. need help */
$('.panel').on("hidden.bs.collapse", function(e) {
  $icon = $( "div#iconstate" )
  console.log('hidden', $icon)
  $icon.removeClass("icon-plus-sign-alt")
  $icon.addClass("icon-minus-sign-alt")
});
$('.panel').on("shown.bs.collapse", function(e) {
  $icon = $( "div#iconstate" )
  console.log('shown', $icon)
  $icon.removeClass("icon-minus-sign-alt")
  $icon.addClass("icon-plus-sign-alt")
});
