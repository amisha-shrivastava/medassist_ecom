$(document).ready(function(){
var state=['-Select-','Madhya Pradesh','Haryana','Punjab','Uttar Pradesh']
   state.map((item)=>{
      $('#states').append($('<option>').text(item))
   })

   $('#states').change(function(){
      $('#cities').empty()
      if($('#states').val()==="Madhya Pradesh")
      {
       var mp=['-Select-','Indore','Bhopal','Gwalior']
       mp.map((item)=>{
          $('#cities').append($('<option>').text(item))

       })
      }

   })

})