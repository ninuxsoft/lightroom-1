var refreshEveryMs = '200';

$(document).ready(function() {
    loadToggles();
    refreshLights();
});

function toggleLight() {
    var x = $(this).attr('data-x');
    var y = $(this).attr('data-y');

    $.ajax({
	url: '/toggle/' + x + '/' + y + '/'
    });
}

function loadToggles () {
    $('.cell').each(function() {
	$(this).click(toggleLight);
    });
}

function refreshLights () {
    window.setTimeout(refreshLights, refreshEveryMs);

    $.ajax({
	url: '/get_multi'
    }).done(function(data) {
	$.each($.parseJSON(data), function (i, e) {
	    var id = '#light_x' + e.pos_x + '_y' + e.pos_y;
	    $(id).css(
		 'background',
		'rgb(' + e.intensity + ', ' + e.intensity + ', ' + e.intensity + ')');
	    $(id).html(e.intensity);
	});
    });
}
