window.addEventListener("DOMContentLoaded", domLoaded);

function domLoaded() {
   let convert = document.querySelector("#calc")
   convert.addEventListener("click",callConvert)
}

function callConvert(){
    console.log('click')
    let score_display = document.querySelector("#score")
    let q = qInput.value - 60
    let d = dInput.value - 60
    let v = vInput.value - 60
    let tot = 205
    tot += (Math.floor((q+d+v)*2/3))*10
    if ((q+d+v)%3==1){
        tot +=10
    }
    if ( q < 0 || q > 30 || v < 0 || v > 30 || d < 0 || d > 30){
        score_display.textContent = "All scores should be between 60 and 90"
    }
    else{
    score_display.textContent = "Score: " + tot
    }
}

