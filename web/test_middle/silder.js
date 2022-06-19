const menu = document.getElementById("jsme");
            function slideDown(){
                menu.style.left = "-300px";
            }
            function slideUp(){
              menu.style.left = "0";
            }
            function handleMouseMove(event){
                let clientX = event.clientX;
  
                if(clientX >= 0 && clientX <= 10){
                  slideUp();
                }else if(clientX > 310){
                  slideDown();
                }
            }
            function init(){
                document.addEventListener("mousemove",handleMouseMove);
            }
            init()
            let win = null;

            function load(url){
                win = window.open(url,"_self");
                
            }
