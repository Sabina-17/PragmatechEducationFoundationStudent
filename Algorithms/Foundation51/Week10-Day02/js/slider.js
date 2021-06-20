let img = document.querySelector('.sliderFrame img');
let imgSources = [
    'img/11.jpg',
    'img/22.jpg',
    'img/33.jpg',
    'img/44.jpg',
    'img/55.jpg'
]

let count = 0;

function goPrev() {
    if (count < 1) {
        img.setAttribute('src', imgSources[4])
        count = 4
    } else {
        img.setAttribute('src', imgSources[count])
        count--
    }
    console.log('countun deyeri: ', count)
}

function goNext() {
    if (count > 4) {
        img.setAttribute('src', imgSources[0])
        count = 0
    } else {
        img.setAttribute('src', imgSources[count])
        count++
    }
    console.log('countun deyeri: ', count)
}