// JS for handling UI for chatbot
var text= $('#chatcontent');
$('#message').keypress(function() {
	if (event.which == 13) {

		var userinput = $('#message').val();
		var res = $('<div class="form-group" style="margin:0 0 0 50px;color:steelblue;font-weight:bolder;">');
		res.text('You: ' + userinput);
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
			var newres = $('<div style="margin:0 0 0 250px;color:fuchsia;font-weight:bolder;">');
			newres.text('Bot: ' + data['reply']);
			newres.appendTo(text);
		}
		})

	}
})
