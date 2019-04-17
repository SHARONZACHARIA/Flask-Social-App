$(function() {
 

  $('#chat_btn').on('click', function() {
    console.log("working")
    let message = $('#chat_text').val();
    let username = $('#uname').val();
    $.post('/message', {'username' : username, 'message' : message ,'status':0}, function() {
      $('#chat_text').val('');
    });
  });
      // Enable pusher logging - don't include this in production
  Pusher.logToConsole = true;
  var pusher = new Pusher('352252f257aba2bb3745', {
    cluster: 'ap2',
    encrypted: true
  });
  var channel = pusher.subscribe('chat-channel');
  channel.bind('new-message', function(data) {
    console.log("data received in client side")
      let name = data.username;
      let message = data.message;
      let status = data.status;
      if(status =="[0]")
      {
      let message_template = `<article class="media">
                              <div class="media-content">
                                <div class="content">
                                  <p>
                                    <strong>${name}</strong>
                                    <br> ${message}
                                  </p>
                                </div>
                              </div>
                            </article>`;
                            $('#content').append(message_template);
                            
     
      }
      if(status=="[1]")
      {
        let message_template = `<article class="media">
                              <div class="media-content">
                                <div class="content">
                                  <p>
                                    <strong>${name}</strong>
                                    <br> <P style="color:red"> ${message}</P>
                                  </p>
                                </div>
                              </div>
                            </article>`;
                            $('#content').append(message_template);
      }
      
    });
  
  
});

function box()
{
  $("#box").on('click' ,function()
  {
   alert(this.$('#uname').val());

  });

}




