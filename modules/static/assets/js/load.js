
function fetchsearch()
{ 
    console.log("fetching data....")
    name = $("#sessionvalue");
    console.log(name)
    $.ajax({
   
        url: 'http://localhost:5000/getuserdata',
        type: 'GET', 
        dataType:'json'
      }).done(function(data){
        
        $("#username_master").html(data.fname+" "+data.lname)
        $("#ph_master").html(data.phone)
        $("#email_master").html(data.email)
       src = "./static/assets/uploads/profile/"+data.filename
       console.log(data.filename)
        $("#propic_master").attr("src",src)
       
      });


      $.ajax({
   
        url: 'http://localhost:5000/getnoticount',
        type: 'GET', 
        dataType:'json'
      }).done(function(data){
        console.log("getting count ....")
        $('#noticount').html(data.count +' Notification(s)')
        
      });





}

function sendmsg()
{
 msg = $("#msgtext").val();

 $.ajax({
   
  url: 'http://localhost:5000/save_chat/sharon/jimmy/sharon/'+msg,
  type: 'GET', 
  dataType:'json'
}).done(function(data){

 
  template=` <ul type="">
  <li> ${data.msg} </li>
 
 </ul>`
  $("#message_list").append(template)
  
 

});

}


