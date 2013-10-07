var refreshEveryMs = '700';

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
	    if ($(id).attr('data-intensity') != e.intensity) {
		$(id).attr('data-intensity', e.intensity);
		var id = '#light_x' + e.pos_x + '_y' + e.pos_y;
		var r = Math.ceil(255 * e.intensity / 255);
		var g = Math.ceil(238 * e.intensity / 255);
		var b = Math.ceil(100 * e.intensity / 255);
		var color = 'rgb(' + r + ', ' + g + ', ' + b + ')';
		$(id).animate({backgroundColor: color}, 400);
	    }
	});
    });
}
