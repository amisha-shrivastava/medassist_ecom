function addItem() {
    var opt=document.createElement('option')
    opt.text=txt.value
    mobile.add(opt)

}

function removeItem() {
    mobile.remove(mobile.selectedIndex)

}