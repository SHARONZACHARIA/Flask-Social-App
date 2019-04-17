function deletenotification(obj){
  
    $.ajax({
           url: 'http://localhost:5000/deletenoti/'+obj.getAttribute('data-id'),
           type: 'GET', 
           dataType:'json'
         }).done(function(data){
           if(data.status=="success")
           {
             console.log("notification deleted")
           }
         });
   
   
     
   }