$(document).ready( () => {

    $("#collection a").click(function(evt) {
        if($(this).next().attr("class") != "hide"){
            $(this).next().hide().toggleClass("hide").animate({opacity: 0.1})
        }else{
            $(this).next().show().toggleClass("hide").animate({opacity:1});
        };
        evt.preventDefault();        
    });

    setTimeout(function(){
    $("#centerImage").fadeOut(500).fadeIn(500).fadeOut(500).fadeIn(500).fadeOut(500).fadeIn(500).fadeOut(500).fadeIn(500)
    })
});