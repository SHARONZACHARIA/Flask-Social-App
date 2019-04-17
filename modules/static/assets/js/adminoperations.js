function sendmail(obj){
  swal("Getting Ready", "Please wait .. you can continue your work and will be notified once mail is sent  ", "info");
  title="Immediate Action Required"
  body="You are required to take down or make changes in follwowing post \n \n  post id :" + obj.getAttribute('data-postid') +" \n time:" + obj.getAttribute('data-time')
  user=obj.getAttribute('data-email')
  $.ajax({
    url: 'http://localhost:5000/admin/getmail/'+obj.getAttribute('data-uname'),
    type: 'GET', 
    dataType:'json'
  }).done(function(data){
    for (i=0;i<data.length;i++ )
 $.ajax({
        url: 'http://localhost:5000/admin/sendmail/'+title+'/'+body+'/'+data[i].email,
        type: 'GET', 
        dataType:'json'
      }).done(function(data){
        if(data.status=="success")
        {
          swal("Owner Notified", "E-Mail  has been successfully sent to "+obj.getAttribute('data-uname') +'\n \n ' +'Post Id :' +obj.getAttribute('data-postid') , "success");
        }
      });
    
  });
  
  
 
 
  

   

}

function deletepost(obj){
  
 $.ajax({
        url: 'http://localhost:5000/admin/deletepost/'+obj.getAttribute('data-postid'),
        type: 'GET', 
        dataType:'json'
      }).done(function(data){
        if(data.status=="success")
        {
          swal("Post Deleted ", "post has been deleted sucessfully", "success");
        }
      });


  
}

function block(obj){
  var user = {uname : obj.getAttribute('data-uname')}
  $.ajax({
    url: 'http://localhost:5000/admin/blockuser',
    type: 'POST', 
    dataType:'json',
    contentType:'application/json;charset=UTF-8',
    
    data:JSON.stringify(user)
    

  }).done(function(data){
    if(data.status=="success")
    {
      swal("User Blocked ", "user has been blocked sucessfully", "success");




    }
  });
}

function unblock_user(obj){
  var user = {uname : obj.getAttribute('data-uname')}
  $.ajax({
    url: 'http://localhost:5000/admin/unblock',
    type: 'POST', 
    dataType:'json',
    contentType:'application/json;charset=UTF-8',
    
    data:JSON.stringify(user)
    

  }).done(function(data){
    if(data.status=="success")
    {
      
     
      swal("User Unblocked ", "user has been unblocked sucessfully", "success")
      .then((value)=>{
        window.location.reload()});
    




    }
  });
}


function send_lostpassword_mail()
{
  var user = {mailid : $('#EmailAddress').val()}
  $.ajax({
    url: 'http://localhost:5000/lost_password',
    type: 'POST', 
    dataType:'json',
    contentType:'application/json;charset=UTF-8',
    
    data:JSON.stringify(user)
    

  }).done(function(data){
    if(data.status=="success")
    {
      
      swal("Password sent  ", "password has been sent to mail  sucessfully", "success");
    
      }
      else{
        swal("Failure  ", "Input a valid email id", "error");
      }
    })
}