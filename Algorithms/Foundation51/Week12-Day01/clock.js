let secondArrow = document.querySelector('.secondArrow')
let minuteArrow = document.querySelector('.minuteArrow')

function clockFunc() {
    d = new Date();
    second = d.getSeconds()
    minute = d.getMinutes()
        // saniyederecesi=360/60
        // degigederecesi=360/3600

    secondRotateAmount = second * 6
    minuteRotateAmount = minute * 0.1;

    secondArrow.style.transform = `rotate(${secondRotateAmount}deg)`

    minuteArrow.style.transform = `rotate(${minuteRotateAmount}deg)`
    secondRotateAmount += 6
    minuteRotateAmount += 0.1;

}

setInterval(clockFunc, 1000)