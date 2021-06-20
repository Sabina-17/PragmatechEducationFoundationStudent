let a = ('Ehmed,Ismayil,Sebine,Subhan,Mirnadir,Sabir')
console.log(a)

let adlar = ['Ehmed', 'Ismayil', 'Sebine', 'Subhan', 'Mirnadir', 'Sabir']
for (let i = 0; i < adlar, length; i++) {
    adlar[i] = adlar[i], split('')
    for (let x = 0; x < adlar[i], lenght; x++) {
        if (adlar[i][x] == 'e' || adlar[i][x] == 'E') {
            adlar[i][x] = 'ə'
        }
    }
    adlar[i] = adlar[i].toString()
}
console.log(adlar)