// JS for handling UI for chatbot

var text= $('#chatcontent');
$('#message').keypress(function() {
	if (event.which == 13) {

		var userinput = $('#message').val();
		var res = $('<div class="container" style="margin:15px 0px 19px 27px;background-color: azure;display: block;clear:both;width: 59%;color:steelblue;font-weight:bolder;padding:8px;">');
		res.text('You: ' +userinput);
		res.appendTo(text);
		$('#message').val('');

		//Get the response from views and db
		$.ajax( {

		url: '/chatapp/bot/',
		type : 'POST',
		data: {
			'input': userinput,
		},
		method: 'POST',
		success: function(data) {
			//What to do when getting the data back from views
			var newres = $('<div class="container" style="margin:0px 0px 0px 79px;width: 59%; background-color: antiquewhite;color:indigo;font-weight:bolder;padding:8px;">');
			newres.text('Bot: ' + data['reply']);
			newres.appendTo(text);
		}
		})

	}
})

