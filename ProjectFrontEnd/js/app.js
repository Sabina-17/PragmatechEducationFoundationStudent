//index.html slider
let img = document.querySelector('.slider img');
let imgSources = [
    "img/main-banner-1-1903x670.jpg",
    "img/main-banner-2-1903x670.jpg"
]

let count = 0;

function goPrev() {
    if (count < 1) {
        img.setAttribute('src', imgSources[1])
        count = 1
    } else {
        img.setAttribute('src', imgSources[count])
        count--
    }
    console.log('countun deyeri: ', count)
}

function goNext() {
    if (count > 1) {
        img.setAttribute('src', imgSources[0])
        count = 0
    } else {
        img.setAttribute('src', imgSources[count])
        count++
    }
    console.log('countun deyeri: ', count)
}


//page1.html  gallery-image
let bigImage = document.querySelector('.imgbag img')

function showBigImage(element) {
    let imgSrc = element.querySelector('img').getAttribute('src')
    bigImage.setAttribute('src', imgSrc)
}


//page1.html tabs
function openTab(evt, TabName) {
    let i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(TabName).style.display = "block";
    evt.currentTarget.className += " active";
}
document.getElementById("defaultOpen").click();


//page1.html content-slider
_slider = document.querySelector('.slider')
item = document.querySelector('.slider-item')
items = document.querySelectorAll('.slider-item')
let sliderFrame = document.querySelector('.slider-frame')

let sliderPos = 0;

for (let i = 0; i < items.length; i++) {
    items[i].style.width = _slider.clientWidth / 3 + 'px';
}

sliderFrame.style.width = items.length * item.clientWidth + 'px';


// prevBtn


let prevBtn = document.querySelector('.prevBtn')

prevBtn.onclick = function() {
    sliderPos += 300;
    sliderFrame.style.left = sliderPos + 'px'
}


// nextBtn
let nextBtn = document.querySelector('.nextBtn')

nextBtn.onclick = function() {
    sliderPos -= 300;
    sliderFrame.style.left = sliderPos + 'px'
}