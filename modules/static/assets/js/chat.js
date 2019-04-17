$(document).ready(function() {

	$('#form').submit( function(event) {
		
         
		$.ajax({
			
			data : {
				name : 'username',
				message: $('#text').val()
			},
			type : 'POST',
			url : '/receive_msg'
			
		
			
		})
		.done(function(data,event) {
             
			if (data.result=='sucess') {
				 console.log("data received"+ data.message )
				var bully = data.bully_status
				if(bully =='[1]')
				{
				}
				$('<li class="sent"><img src="http://emilcarlsson.se/assets/mikeross.png" alt="" /><p>' + data.message +data.bully_status+ '</p></li>').appendTo($('.messages ul'));
				$('.message-input input').val(null);
				$('.contact.active .preview').html('<span>You: </span>' + data.message);
				$(".messages").animate({ scrollTop: $(document).height() }, "fast");
			}
			else{
				console.log("something went wrong ")
			}
		});

		event.preventDefault();

	});


	

});


var s = 0 
  function re_page()
	{
	

		if(s==0)
		{
			s+=1
		console.log('onloaded')
		  $.ajax({
			  data : {
				  chatid : 'sample_id2',
				  
			  },
			  type : 'POST',
			  url : '/fetch_msg'
					});
					
				} 
				else{
					console.log('onloaded2')
		  $.ajax({
			  data : {
				  chatid : 'sample_id2',
				  
				},
				dataType:'json',
			  type : 'POST',
			  url : '/fetch_msg'
					}).done(function(data,event) {

						jQuery.each(data, function(index,item)
						{ console.log("dataskajk")
							$('<li class="sent"><img src="http://emilcarlsson.se/assets/mikeross.png" alt="" /><p>' + item.message+ '</p></li>').appendTo($('.messages ul'));
				$('.message-input input').val(null);
				$('.contact.active .preview').html('<span>You: </span>' + data.message);
				$(".messages").animate({ scrollTop: $(document).height() }, "fast");

						});
						
						
						

					});
				}
	  }
	
 
		setInterval(re_page,5000)


