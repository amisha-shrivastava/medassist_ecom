function call() {
    var cn=cars.options[cars.selectedIndex].text
    carname.innerHTML=cn
    carprice.innerHTML=cars.value
    var rtotax=cars.value*28/100
    var insamt=cars.value*12/100
    var orp=parseInt(cars.value)+rtotax+insamt
    rto.innerHTML=rtotax
    insu.innerHTML=insamt
    onroadprice.innerHTML=orp
    carimage.src=cn+".jpg"
}