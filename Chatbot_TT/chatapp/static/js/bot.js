// JS for handling UI for chatbot

function clickme() {
 alert("jii");

}
var text= $('#chatcontent');
$('#message').keypress(function() {
	if (event.which == 13) {

		var userinput = $('#message').val();
		var res = $('<div style="margin:15px 0 19px 27px;background-color: azure;display: block;clear:both;width: 59%;color:steelblue;font-weight:bolder;padding:8px; position: fixed;">');
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
			var newres = $('<div  style="margin:0 0 0 185px;width: 59%; background-color: antiquewhite;color:indigo;font-weight:bolder;padding:8px; position: fixed;">');
			newres.text('Bot: ' + data['reply']);
			newres.appendTo(text);
		}
		})

	}
})



$('#clickMe').click(function() {
        alert("jelo");

		var userinput = $('#message').val();
		var res = $('<div class="container" style="margin:15px 0 19px 27px;background-color: azure;display: block;clear:both;width: 59%;color:steelblue;font-weight:bolder;padding:8px">');
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
			var newres = $('<div class="container" style="margin:0 0 0 185px;width: 59%; background-color: antiquewhite;color:indigo;font-weight:bolder;padding:8px;">');
			newres.text('Bot: ' + data['reply']);
			newres.appendTo(text);
		}
		})


})
