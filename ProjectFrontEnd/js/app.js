let bigImage = document.querySelector('.imgbag img')

function showBigImage(element) {
    let imgSrc = element.querySelector('img').getAttribute('src')
    bigImage.setAttribute('src', imgSrc)
}