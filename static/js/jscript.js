$(document).ready(function () {
    $('.modal').modal();
    $('.dropdown-trigger').dropdown();
    $('.sidenav').sidenav();
    $('.tabs').tabs();
    $('.chips').chips();
    $('select').formSelect();
    $('.collapsible').collapsible();
    $("select[required]").css({ display: "inline", height: 0, padding: 0, width: 0 });
   // $('textarea#ingredients').html($('textarea#ingredients').html().trim());
    //$('textarea#prep_steps').html($('textarea#prep_steps').html().trim());
    //$('textarea#further_info').html($('textarea#further_info').html().trim());
   // $('textarea#tool_further_info').html($('textarea#_tool_further_info').html().trim());
    Materialize.updateTextFields();
});
