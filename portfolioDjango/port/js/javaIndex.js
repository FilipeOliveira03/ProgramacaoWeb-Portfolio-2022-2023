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
    
    if(num == 1){
        document.getElementById('butaoDarkMode').innerHTML = "Light Mode"
        num = 2;
    }else{
        document.getElementById('butaoDarkMode').innerHTML = "Dark Mode"
        num = 1;
    }
}

const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        console.log(entry)
        if(entry.isIntersecting){
            entry.target.classList.add('show');
        }else{
            entry.target.classList.remove('show');
        }
    })
})

const hiddenElements = document.querySelectorAll('.hidden');
hiddenElements.forEach((el) => observer.observe(el));
