window.onscroll = function () { scrollFunction() };

function scrollFunction() {
    if (document.body.scrollTop > 290 || document.documentElement.scrollTop > 290) {
        $(".navbar").addClass("fixed-top")
        $(".header .navbar").removeAttr("style");
        $(".header .navbar").attr("style", "background-color:#9f9f9f !important");
        $(".search-bar").removeClass("navbarSupportedContent")
    } else {
        $(".navbar").removeClass("fixed-top")
        $(".header .navbar").removeAttr("style");
        $(".header .navbar").attr("style", "background-color:transparent !important");
        $(".search-bar").addClass("navbarSupportedContent")
    }
}