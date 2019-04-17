
function fetchfriendsearch()
{ 
  name= $("#textbox").val()
  
$.ajax({
   
    url: 'http://localhost:5000/searchFriends/'+name,
    type: 'GET', 
    dataType:'json'
  }).done(function(data){
    uname = $("#sessionvalue").val()
    $("#wrappers").empty();
    
      for(i=0;i<data.length;i++)
      {
         if(data[i].uname ==uname)
         {
           continue
         }
        
         
         
        console.log(data[i].uname)
        src = "./static/assets/uploads/profile/"+data[i].filename
       message_template=  `
       <div id="results" class="results" style="box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
       transition: 0.8s;
       width: 150px;
       margin: 8px ;
       padding-left:4px;
       border-radius: 5px;
        border-radius: 8px;
         width: 150px;
         height:220px;
        font-size: 80%;">
        <center>
        <img id="${data[i].uname}" src="./static/assets/uploads/profile/${data[i].filename}" alt="${data[i].filename}"  width="120px" height="120px">
        <h4><b>${data[i].uname} </b></h4> 
        <a href ="http://localhost:5000/sendrequest/${uname}/${data[i].uname}">ADD FRIEND</a>
      <i>${data[i].email} </i> <br>
      </center>
      </div>
     `
     src_image='http://localhost:5000/static/assets/uploads/profile/'+data[i].filename
     
     
 
     $('#wrappers').append(message_template);
      }
    
     
    
  });
}