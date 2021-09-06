let zoom = 1;
const ZOOM_SPEED = 0.1;
var lastscroll = 0;

window.onload = function() {
    arrow = document.getElementById("arrow");
    nav = document.querySelector(".nav");
    main = document.getElementsByClassName("square");
    modal = document.getElementsByClassName("modal");
    quote = document.getElementsByClassName("quote");
    ellipsis = document.getElementsByClassName("ellipsis");
    more();
};

window.onscroll = function() {
    hide();
};

function more() {
    for (let i = 0; i < quote.length; i++) {
        if (isOverflown(quote[i])) {
            ellipsis[i].style.display = "block";
        } else {
            ellipsis[i].style.display = "none";
        }
    }
}

function isOverflown(element) {
    return element.scrollHeight > element.clientHeight || element.scrollWidth > element.clientWidth;
}

function hide() {
    if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
        arrow.style.display = "none";
        nav.style.opacity = 1 - document.documentElement.scrollTop / 250;
        for (let i = 0; i < main.length; i++) {
            main[i].style.opacity = document.documentElement.scrollTop / 800;
        }
        if (document.body.scrollTop > 600 && document.body.scrollTop < 1300 || document.documentElement.scrollTop > 600 && document.documentElement.scrollTop < 1300) {
            document.getElementsByClassName('sidebar')[0].style.display = 'block';
        } else {document.getElementsByClassName('sidebar')[0].style.display = 'none';}
    } else {
        arrow.style.display = "block";
        nav.style.opacity = 1 + document.documentElement.scrollTop / 250;
        for (let i = 0; i < main.length; i++) {
            main[i].style.opacity = 1 - document.documentElement.scrollTop / 800;
        }
    }
};

function enlarge(x) {
    document.getElementById(x).style.display = "block";
}

window.onclick = function(event) {
    for (let i = 0; i < modal.length; i++) {
        if (event.target == modal[i]) {
            modal[i].style.display = "none";
          }
    }
} 
