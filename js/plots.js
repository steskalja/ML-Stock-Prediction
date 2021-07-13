fortunedata_url = 'http://localhost:5000/home';

d3.json(fortunedata_url).then(fortunedata => {
    let dates = [];
    let prices = [];

    // Place holder
    
    fortunedata.history.forEach(r => {
        
    });

    // Adding graph selector options button to limit to
    // 1mo, ymo, year-to-date, 1y, and all
    const selectorOptions = {
        buttons: [{
            step: 'company',
            stepmode: 'backward',
            count: 1,
            label: 'Fortune 1'
        }, {
            step: 'company',
            stepmode: 'backward',
            count: 1,
            label: 'Fortune 2'
        }, {
            step: 'company',
            stepmode: 'backward',
            count: 1,
            label: 'Fortune 3'
        }, {
            step: 'company',
            stepmode: 'backward',
            count: 1,
            label: 'Fortune 4'
        }, {
            step: 'company',
            stepmode: 'backward',
            count: 1,
            label: 'Fortune 5'
        },{
            step: 'company',
            stepmode: 'backward',
            count: 1,
            label: 'Fortune 6'
        }, {
            step: 'company',
            stepmode: 'backward',
            count: 1,
            label: 'Fortune 7'
        }, {
            step: 'company',
            stepmode: 'backward',
            count: 1,
            label: 'Fortune 8'
        }, {
            step: 'company',
            stepmode: 'backward',
            count: 1,
            label: 'Fortune 9'
        }, {
            step: 'company',
            stepmode: 'backward',
            count: 1,
            label: 'Fortune 10'
        }],
    };

    const trace = {
        type: 'scatter',
        mode: 'lines',
        name: 'fortune10',
        x: dates,
        y: prices,
        line: { color: "#17BECF" }
    };

    const trace_events = {
        type: 'scatter',
        mode: 'markers',
        name: 'Events',
        x: [],
        y: [],
        text: [],
        marker: {size: 15}

    };

    const data = [trace, trace_events];

    const layout = {
        title: 'Fortune 10 Stock Predictions',
        xaxis: {
            rangeselector: selectorOptions,
            rangeslider: {},
            showticklabels: true,
            tickangle: 'auto',
        },
        yaxis: {
            title: {
                text: "In USD"
            },
            fixedrange: true,
        }
    };

    Plotly.newPlot('plot', data, layout);

}).catch(error => console.log(error));
