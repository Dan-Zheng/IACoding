$(document).ready(function(){
	$('.thumbnail').each(function(){
		if( $(this).css('background-image') == 'none')
			{
				var x = $(this).attr('id');
				if(x != null){
					$(this).css('background-image','url("staff-pics/'+x+'.jpg")');
				}else{
					$(this).css('background-image','url("staff-pics/logo.jpg")');
				}
			}
	});
});