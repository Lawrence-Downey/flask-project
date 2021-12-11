$(document).ready( () => {

    $("#collection a").click(function(evt) {
        if($(this).next().attr("class") != "hide"){
            $(this).next().fadeOut(1500).toggleClass("hide");
        }else{
            $(this).next().fadeIn(1000).toggleClass("hide");
        };
        evt.preventDefault();        
    });

    setTimeout(function(){
    $("#centerImage").fadeOut(500).fadeIn(500).fadeOut(500).fadeIn(500)
                     .fadeOut(500).fadeIn(500).fadeOut(500).fadeIn(500)
    }, 2000);

    $("errorMessage").fadeOut(500).fadeIn(500).fadeOut(500).fadeIn(500)
                     .fadeOut(500).fadeIn(500).fadeOut(500).fadeIn(500)
});