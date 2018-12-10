$(window).on('load', function() {
    $("#cubierta").fadeOut(200);
});

//stackoverflow does not fire the window onload properly, substituted with fake load

function newW()
{
    $(window).load();
}
setTimeout(newW, 1000);

$(window).on('load', function() {
    $("#cubierta2").fadeOut(200);
});

//stackoverflow does not fire the window onload properly, substituted with fake load

function newW()
{
    $(window).load();
}
setTimeout(newW, 1000);