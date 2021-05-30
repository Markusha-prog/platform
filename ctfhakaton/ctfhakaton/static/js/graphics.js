function aver(vals) {
    let averVals = [0];
    for (let i = 0; i < vals.length; i++) {
        let summ = 0;
        for (let j = 0; j<=i; j++){
            summ += vals[j]
        }
        averVals.push((summ/(i+1)).toFixed(2))
    }
return averVals;
}


document.addEventListener("DOMContentLoaded", function(){
	// Create liteChart.js Object
    let vals1 = [4, 3, 1, 5];
    let vals2 = [3, 5, 5, 4, 3,]
    let labels = []
    let size = 0;
    let values = [aver(vals1), aver(vals2)]
    if (vals1.length>vals2.length) size = vals1.length
    else size = vals2.length
    for (let i = 0; i < size+1; i++){
        labels.push(i);
    }
	// Chart Values

// Initiate Chart 1
Chartist.Line("#chart1", {
	labels: labels,
	series: values
}, {
	width: 350,
    height: 200,
    high: 7,
    low: 0,
	chartPadding: {
	},
	axisY: {
		onlyInteger: true
	}
}).on("draw", function(data) {
	if (data.type === "point") {
		data.element._node.setAttribute("title", "Value: " + data.value.y);
		data.element._node.setAttribute("data-chart-tooltip", "chart1");
	}
}).on("created", function() {
	// Initiate Tooltip
	$("#chart1").tooltip({
		selector: '[data-chart-tooltip="chart1"]',
		container: "#chart1",
		html: true
	});
});
});