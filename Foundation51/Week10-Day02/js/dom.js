// Javascript vasite ile
// 1. Men html element nece yarada bilerem. html daxilinde elnen yazmadan
// 2. HTML daxilinde var olan elementi nece silebilerem
// 3. html daxilinde olan elementin atributlarini nece idare edebilerem
// 4. html daxilindeki elementi css stillerini nece deyisebilerem
// 5. html elementinin daxilindeki contenti nece idare edebilerem

let heading = document.createElement('h1')
heading.innerHTML = 'Bu bir basligdir'
document.body.appendChild(heading)

// method void yoxsa return oldugunu oyrenmek
// eyer return metoddursa istehsal etdiyi deyerin tipi ve valuesunu oyrenmek
// methodun hansi parametrleri gebul etdiyini oyrenmek

function Foo(a, b = 67) {
    console.log(a + b)
}

Foo(4)