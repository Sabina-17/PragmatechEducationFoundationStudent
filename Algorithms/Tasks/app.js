_slider = document.querySelector('.slider')
item = document.querySelector('.slider-item')
items = document.querySelectorAll('.slider-item')
let sliderFrame = document.querySelector('.slider-frame')

let sliderPos = 0;

for (let i = 0; i < items.length; i++) {
    items[i].style.width = _slider.clientWidth / 4 + 'px';
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