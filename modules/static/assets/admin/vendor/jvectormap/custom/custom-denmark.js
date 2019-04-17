// Denmark
$(function(){
	$('#mapDenmark').vectorMap({
		map: 'dk_mill',
		zoomOnScroll: false,
		regionStyle:{
			initial: {
				fill: '#ff94b8',
			},
			hover: {
				"fill-opacity": 0.8
			},
			selected: {
				fill: '#ff4081'
			},
		},
		backgroundColor: '#ffffff',
	});
});