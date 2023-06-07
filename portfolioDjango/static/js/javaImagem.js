window.onscroll = function () {
    var barra = document.getElementById("barra");
    var menu = document.getElementById("menu");

    if (window.pageXOffset >= menu.offsetTop) {
        barra.classList.add("sticky");
    } else {
        barra.classList.remove("sticky");
    }
}

var num = 1;

function clicaDarkMode() {
    var element = document.getElementById('index');
    element.classList.toggle("darkMode");

    if (num == 1) {
        document.getElementById('butaoDarkMode').innerHTML = "Light Mode"
        num = 2;
    } else {
        document.getElementById('butaoDarkMode').innerHTML = "Dark Mode"
        num = 1;
    }
}

function bigImg(x) {
    x.style.left = "10%";
    x.style.top = "30%";
    x.style.height = "50%";
    x.style.width = "50%";
    x.style.scale = "90%";
}

function normalImg(x) {
    x.style.left = "10%";
    x.style.top = "30%";
    x.style.height = "50%";
    x.style.width = "50%";
    x.style.scale = "60%";
}

function exibirTexto() {
    var texto = document.getElementById("texto").value;
    if(texto != ""){
        document.getElementById("textoDigitado").innerHTML = texto;
    }
}