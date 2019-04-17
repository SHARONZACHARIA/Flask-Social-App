to_user = null

function sendmsg()
{
 msg = $("#msgtext").val();

 $.ajax({
   
  url: 'http://localhost:5000/save_chat/'+to_user+'/'+msg,
  type: 'GET', 
  dataType:'json'
}).done(function(data){
  $("#msgtext").val('')
  template=''
  var offensive=''
           if(data.bully=='[1]')
           {
             offensive = 'offensive word(s) found'
           }
  if(data.fuser==to_user)
  {
  
  template=`<li class="chats-left">
  <div class="chats-avatar">
     
      <div class="chats-name">${data.fuser}</div>
  </div>
  <div class="chats-text danger">${data.msg}</div>
  <div class="chats-hour">${data.times} | ${offensive} <span class="icon-done_all"></span></div>
 </li>`
 
  }
  else
  {
    template=`<li class="chats-right">
    <div class="chats-avatar">
       
        <div class="chats-name">you</div>
    </div>
    <div class="chats-text danger">${data.msg}</div>
    <div class="chats-hour">${data.times} | ${offensive} <span class="icon-done_all"></span></div>
   </li>`
   
    
  }
   
  $("#message_list").append(template)
  window.scrollTo(0,document.querySelector(".message_list").scrollHeight)

});

}

 function fetch_recent()
{  
    $.ajax({
   
        url: 'http://localhost:5000/recent_chat/'+to_user,
        type: 'GET', 
        dataType:'json'
      }).done(function(data){
       
        template=``
         for(i=0;i<data.length;i++)
        {  var offensive=''
           if(data[i].bully=='[1]')
           {
             offensive = 'offensive word(s) found'
           }

          if(data[i].fuser==to_user)
          {
          
          template=`<li class="chats-left">
          <div class="chats-avatar">
             
              <div class="chats-name">${data[i].fuser}</div>
          </div>
          <div class="chats-text danger">${data[i].msg}</div>
          <div class="chats-hour">${data[i].times} | ${offensive}<span class="icon-done_all"></span></div>
         </li>`
         
          }
          else
          {
            template=`<li class="chats-right">
            <div class="chats-avatar">
               
                <div class="chats-name">you</div>
            </div>
            <div class="chats-text danger">${data[i].msg}</div>
            <div class="chats-hour">${data[i].times} |  ${offensive} <span class="icon-done_all"></span></div>
           </li>`
          }
           
          $("#message_list").append(template)
          }
      });

      $.ajax({
   
        url: 'http://localhost:5000/seen/'+to_user,
        type: 'GET', 
        dataType:'json'
      }).done(function(data){

      
    });
       
}
 setInterval(fetch_recent,5000)



function chatwith(id)
{ $("#sendbtn").attr("disabled",false)
  to_user = id
  to = id
  $("#to_user_name").html(id)

  $.ajax({
   
    url: 'http://localhost:5000/chat/'+to,
    type: 'GET', 
    dataType:'json'
  }).done(function(data){
    template=``
    $("#message_list").empty();
     for(i=0;i<data.length;i++)
    {
      var offensive=''
           if(data[i].bully=='[1]')
           {
             offensive = 'offensive word(s) found'
           }
      if(data[i].fuser==to_user)
          {
          
          template=`<li class="chats-left" style="width:300px">
          <div class="chats-avatar">
             
              <div class="chats-name">${data[i].fuser}</div>
          </div>
          <div class="chats-text danger" style="width:300px">${data[i].msg}</div>
          <div class="chats-hour">${data[i].times} | ${offensive} <span class="icon-done_all"></span></div>
         </li>`
         
          }
          else
          {
            template=`<li class="chats-right">
            <div class="chats-avatar">
               
                <div class="chats-name">you</div>
            </div>
            <div class="chats-text danger">${data[i].msg}</div>
            <div class="chats-hour">${data[i].times} | ${offensive}<span class="icon-done_all"></span></div>
           </li>`
           
          }
           
          $("#message_list").append(template)
          }
   

  });


  $.ajax({
   
    url: 'http://localhost:5000/seen/'+to_user,
    type: 'GET', 
    dataType:'json'
  }).done(function(data){

  
});
   
}