let header = document.querySelector("header");
window.addEventListener("scroll", e => {
    if(window.pageYOffset!=0){
        header.style = "box-shadow: 0 8px 6px -6px gray; background-color: white;";
    }
    else
        header.style = "";
})