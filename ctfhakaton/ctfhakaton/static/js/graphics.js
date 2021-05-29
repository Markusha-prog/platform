function aver(vals) {
    let averVals = [0];
    for (let i = 0; i < vals.length; i++) {
        let summ = 0;
        for (let j = 0; j<=i; j++){
            summ += vals[j]
        }
        averVals.push(summ/(i+1))
    }
return averVals;
}

document.addEventListener("DOMContentLoaded", function(){
	// Create liteChart.js Object
	let d = new liteChart("chart");
	let vals = [];
	// Set labels
	//d.setLabels(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]);

	// Set legends and values
	d.addLegend({"name": "Общая", "stroke": "#CDDC39", "fill": "#fff", "values": aver(vals)});
	d.addLegend({"name": "Текущий хакатон", "stroke": "#3b95f7", "fill": "#fff", "values": aver(vals)});

	// Inject chart into DOM object
	let div = document.getElementById("stats");
	d.inject(div);

	// Draw
	d.draw();
});