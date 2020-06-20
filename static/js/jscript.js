$(document).ready(function () {
    $('.modal').modal();
    $('.dropdown-trigger').dropdown();
    $('.sidenav').sidenav();
    $('.tabs').tabs();
    $('.chips').chips();
    $('select').formSelect();
    $('.collapsible').collapsible();
    $("select[required]").css({ display: "inline", height: 0, padding: 0, width: 0 });
    Materialize.updateTextFields();
});
