function talktobot()
{
 msg = $("#botmsgtext").val();
 template=` <li class="chats-right">
 <div class="chats-avatar">
    
     <div class="chats-name">You</div>
 </div>
 <div class="chats-text danger">${msg}</div>
 <div class="chats-hour">08:56 <span class="icon-done_all"></span></div>
</li>`
 $("#botchatslist").append(template)
 $.ajax({
   
  url: 'http://localhost:5000/messagebot/'+msg,
  type: 'GET', 
  dataType:'json'
}).done(function(data){
  $("#botmsgtext").val('');
  console.log(data)
 
  template=`<li class="chats-left">
  <div class="chats-avatar">
     
      <div class="chats-name">bot</div>
  </div>
  <div class="chats-text danger">${data.message}</div>
  <div class="chats-hour">08:56 <span class="icon-done_all"></span></div>
 </li>`
  $("#botchatslist").append(template)
  $("#botmsgtext").val('');
   

});

}



function updateChatbot()
{
  console.log("data sent")
  content = $("#chatbotdatatext").val()
  
  
  $.ajax({
   
    url: 'http://localhost:5000/admin/update_chatbot/'+content,
    type: 'GET', 
    dataType:'json'
  }).done(function(data){
    console.log(data)
    if(data.status=="success")
    {
    swal("Updated ", "chatbot data has been updated sucessfully", "success")
    }
    
   

  });
}