let imageIndex = 0;
let postion = 0;

const IMAGE_WIDTH = 600;  
const btnPrevious = document.querySelector(".previous")
const btnNext = document.querySelector(".next")
const images = document.querySelector(".images")
 
function previous(){
  if(imageIndex > 0){
    btnNext.removeAttribute("disabled")
    postion += IMAGE_WIDTH;
    images.style.transform = `translateX(${postion}px)`;
    imageIndex = imageIndex - 1;
  }
  if(imageIndex == 0){
    btnPrevious.setAttribute('disabled', 'true')
  }
}
function next(){

  if(imageIndex < 3){
    btnPrevious.removeAttribute("disabled")
    postion -= IMAGE_WIDTH;
    images.style.transform = `translateX(${postion}px)`;
    imageIndex = imageIndex + 1;
    
  }
  if(imageIndex == 3){
    btnNext.setAttribute('disabled', 'true')
  }
}

function init(){
  btnPrevious.setAttribute('disabled', 'true')
  btnPrevious.addEventListener("click", previous)
  btnNext.addEventListener("click", next)

}

init();