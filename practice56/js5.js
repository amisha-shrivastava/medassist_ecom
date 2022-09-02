function call() {
    foodname.innerHTML=foods.value
    if(foods.value=="Chola Bhatura")
    {
        foodprice.innerHTML=160
    }
    else if(foods.value=="Pav Bhaji")
    {
        foodprice.innerHTML=120
    }
    else if(foods.value=="Veg Momo's")
    {
        foodprice.innerHTML=60
    }
   else if(foods.value=="Pizza")
    {
        foodprice.innerHTML=600
    }

   foodimage.src=foods.value+".jpg"


}