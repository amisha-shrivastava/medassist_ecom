function  call() {
    var v=''
    if(Sony.checked)
    v+=Sony.value+","

    if(Lg.checked)
    v+=Lg.value+","

    if(Samsung.checked)
    v+=Samsung.value+","
    result.innerHTML=v



}