$(document).ready(function() {		
	$(".selection").click(function() { 
		$('.selection').removeClass('selectionChoice');
		$(this).addClass('selectionChoice');
	});
})