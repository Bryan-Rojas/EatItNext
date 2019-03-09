$(function() {
    // this will get the full URL at the address bar
    var url = window.location.href;

    // passes on every "a" tag
    $(".navbar-nav a").each(function() {
        // checks if its the same on the address bar
        if (url == (this.href)) {
            $(this).closest("a").attr('id', 'currentPageInNav');
            //for making parent of submenu active
        }
    });
});   