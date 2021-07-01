//check for browser or tab close and deletes all the users files to save server memory 

$(document).ready(function(){
	$(window).on("beforeunload",function(e){
		$.ajax({
			url:delete_user_data,
			method: 'POST',
		)}
	});
});
