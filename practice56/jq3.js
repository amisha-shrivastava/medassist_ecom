$(document).ready(function(){
$('#btn').click(function(){
   var c=parseInt($('#txt1').val())+parseInt($('#txt2').val())
   $('#result').html(`<h1>Sum:${c}</h1>`)

})


})