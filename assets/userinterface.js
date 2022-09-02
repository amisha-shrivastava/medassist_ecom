$(document).ready(function(){
 $("#user-menu-button").click(function () {
     $('#dropdown').toggle()
 })
 $.getJSON('http://localhost:8000/fetch_all_user_category',function(data){
   var htm=''
   data.data.map((item)=>{
       htm+=`<li><a href="#">${item.categoryname}</a></li>`
   })

  $('.mainmenu').html(htm)

 })

$.getJSON('http://localhost:8000/fetch_all_products',function(data){
   htm=''
    data.data.map(item=>{
        var price
        var offerprice
        var save
        if(item.offerprice>0)
        { price="<s style='color: red;'>"+item.price+"</s>"
          offerprice=item.offerprice
          save=item.price-item.offerprice
        }
        else
        {
             offerprice=item.price
             price="<div></div>"
            save="<div></div>"
        }


        htm+=`<div style=" border-radius:10px; margin:10px;display: flex; flex-direction: column;align-items: center; width:250px;height:300px;padding: 5px;border:1px solid #bdc3c7;box-shadow: 2px 2px #ecf0f1;elevation: below;">
          <div>
          <img src="http://localhost:8000/static/${item.productimage}" style='width:150px; height: 150px;' >
          </div>
          <div style="padding:5px;">
          <div style="width:200px;font-weight: bolder;text-align: left;">
${item.productname} ${item.scname}
</div>
<div style="width:200px; font-size:10px;text-align: left;">
<i>Mkt:${item.bname}</i>
</div>

<div style="width:200px;font-weight: bolder;text-align: left;">
MRP:&#8377 ${price}
</div>
<div style="width:200px;font-weight: bolder;text-align: left;">
Offer:&#8377 ${offerprice}
</div>
<div style="width:200px;font-weight:bold;text-align: left; color:green">
You save &#8377 ${save}
</div>



</div>
         </div>`
})

  $('#productlist').html(htm)

 })





})