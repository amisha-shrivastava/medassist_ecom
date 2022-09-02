function fillCity() {
    removeItems()
    switch(state.selectedIndex)
    {
        case 1:
            var pb=[['-City-',0],['Amritsar',100000],['Jallandhar',1200000],['Ludhiyana',1700000]]

            fillDD(pb)
            break
        case 2:
            var hr=[['-City-',0],['Sonipat',1000000],['Faridabad',4500000],['Palwal',3000000],['Gurugram',6000000]]

            fillDD(hr)
            break
        case 3:
            var gj=[['-City-',0],['Ahmdabad',9000000],['Surat',3000000],['Vadodra',1400000],['Bhuj',700000]]
            fillDD(gj)
            break

    }

}

function  fillDD(arr) {
            for(i=0;i<arr.length;i++)
            {var opt=document.createElement('option')
             opt.text=arr[i][0]
             opt.value=arr[i][1]
             city.add(opt)
            }

}

function removeItems() {
    for(i=city.options.length-1;i>=0;i--)
    { city.remove(i)}

}

function show() {
    result.innerHTML=city.options[city.selectedIndex].text+","+city.value

}