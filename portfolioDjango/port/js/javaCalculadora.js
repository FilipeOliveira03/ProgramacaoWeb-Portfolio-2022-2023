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

const display = document.querySelector("#display");
const buttons = document.querySelectorAll("button");

buttons.forEach((item) => {
    item.onclick = () => {
        if (item.id != "butaoDarkMode") {
            if (item.id == "clear") {
                display.innerText = "";
            } else if (item.id == "backspace") {
                let string = display.innerText.toString();
                display.innerText = string.substr(0, string.length - 1);
            } else if (display.innerText != "" && item.id == "equal") {
                display.innerText = eval(display.innerText);
            } else if (display.innerText == "" && item.id == "equal") {
                display.innerText = "Empty!";
                setTimeout(() => (display.innerText = ""), 2000);
            } else {
                display.innerText += item.id;
            }
        }else{
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


    };
});


