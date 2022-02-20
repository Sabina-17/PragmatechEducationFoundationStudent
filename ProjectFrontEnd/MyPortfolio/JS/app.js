// Navbar
// function myFunction(x) {
//     x.classList.toggle("change");
//   }

function deyis(){
  document.querySelector(".navbar-nav").style.visibility="visible"
  document.querySelector(".navbar-nav").style.opacity="1"
  document.querySelector(".navbar-nav").style.transition="all 1s"
  document.querySelector("#close").style.visibility="visible"
  document.querySelector("#close").style.opacity="1"
  document.querySelector("#open").style.visibility="hidden"
  document.querySelector("#open").style.opacity="0"
  


}
function bagla(){

  document.querySelector(".navbar-nav").style.visibility="hidden"
  document.querySelector(".navbar-nav").style.opacity="0"

  document.querySelector("#close").style.visibility="hidden"
  document.querySelector("#close").style.opacity="0"
  document.querySelector("#open").style.visibility="visible"
  document.querySelector("#open").style.opacity="1"
 
  
 }
 function _border(){
  document.querySelector(".navbar-nav span").style.borderColor="red"
 }

