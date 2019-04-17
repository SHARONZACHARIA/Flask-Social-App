var chart12 = c3.generate({
	bindto: '#pieChart1',
	data: {
		// iris data from R
		columns: [
			['Mon', 219],
			['Tue', 167],
			['Wed', 115],
			['Thu', 87],
			['Fri', 60],
			['Sat', 30],
		],
		type : 'pie',
		colors: {
			Mon: '#5c36b1',
			Tue: '#6b45c3',
			Wed: '#8059dc',
			Thu: '#a17ff1',
			Fri: '#a886f9',
			Sat: '#bda6f3',
		},
		onclick: function (d, i) { console.log("onclick", d, i); },
		onmouseover: function (d, i) { console.log("onmouseover", d, i); },
		onmouseout: function (d, i) { console.log("onmouseout", d, i); }
	},
});