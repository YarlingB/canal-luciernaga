$(function(){
	
});

function showmore(idvid){
	$('#video_name_'+ idvid).addClass('hidden');
	$('#expand-icon_'+ idvid).removeClass('hidden');
	$('#activeVideo').removeClass('hidden');
	console.log( "ready showmore!" );
}