function fillMobile() {
    removeItems()
    switch(company.selectedIndex)
    {
        case 1:
            var sm=[['-Mobile-',0],['Samsung A8',180000],['Samsung M31',240000],['Samsung S22',120000]]

            fillDD(sm)
            break
        case 2:
            var ip=[['-Mobile-',0],['IPhone 11',45000],['Iphone 12',55000],['Iphone 13',67000]]

            fillDD(ip)
            break

    }

}

function  fillDD(arr) {
            for(i=0;i<arr.length;i++)
            {var opt=document.createElement('option')
             opt.text=arr[i][0]
             opt.value=arr[i][1]
             mobile.add(opt)
            }

}

function removeItems() {
    for(i=mobile.options.length-1;i>=0;i--)
    { mobile.remove(i)}

}

function show() {
    var mn=mobile.options[mobile.selectedIndex].text
    var price=mobile.value
    var offer=price*10/100
    var netprice=price-offer
    var htm="<table border='1' cellspacing='0' width='30%'><caption><h3>Mobile Shoppe</h3></caption>"
htm+="<tr><th><font size='5' color='#ff1493'><b>"+mn+"</b></font></th></tr>"
htm+="<tr><th><img src='"+mn+".jpg' width='80'></th>"
htm+="<tr><th><font size='4' color='red'><b>&#8377;<s>"+price+"</s></b></font></th>"
htm+="<tr><th><font size='4' color='green'><b>&#8377;"+netprice+"</b></font></th>"
htm+="<tr><th><font size='4' color='teal'><b>You save:&#8377;"+offer+"</b></font></th>"
htm+="</table>"

result.innerHTML=htm

}

function showDetails() {
    var mn=mobile.options[mobile.selectedIndex].text
    var price=mobile.value
    var offer=price*10/100
    var netprice=price-offer
    var htm="<table border='1' cellspacing='0' width='30%'><caption><h3>Mobile Shoppe</h3></caption>"
htm+=`<tr><th><font size='5' color='#ff1493'><b>${mn}</b></font></th></tr>`
htm+=`<tr><th><img src='${mn}.jpg' width='80'></th>`
htm+=`<tr><th><font size='4' color='red'><b>&#8377;<s>${price}</s></b></font></th>`
htm+=`<tr><th><font size='4' color='green'><b>&#8377;${netprice}</b></font></th>`
htm+=`<tr><th><font size='4' color='teal'><b>You save:&#8377;${offer}</b></font></th>`
htm+="</table>"

result.innerHTML=htm

}