// Helper function to calculate average of objects passed in an array
const calculateMonthlyAvg = function (array) {
    let avg_price = 0;
    let total_price = 0;
    array.forEach(obj => { 
        // Convert price from string to a number.
        obj.price = +obj.price;
        total_price += obj.price;
    })

    avg_price = total_price / array.length;
    return avg_price.toFixed(3);
};


// Use d3 to update data table with week and gas price
d3.json("http://localhost:5000/home").then(function (data) {
    // console.log(data.history);


    //Set up parser for company name

    
    var groupedData = d3.nest()
        .key(function (dt) { return formatYear(parseTime(dt.date)); }) //placeholder
        .key(function (dt) { return formatMonth(parseTime(dt.date)); }) //placeholder
        //.key(function (dt) { return dt.price; })
        .entries(data.history);

    // console.log(groupedData);
    
    // Should old monthly price totals
    let monthlyPrices = {}; //placeholder

    //placeholder
    groupedData.forEach(yearlyData => {
        let year = yearlyData.key;
        
        // Initialize year object
        monthlyPrices[year] = {};

        yearlyData.values.forEach(monthlyData => {
            const month =  monthlyData.key;
            const monthly_price = calculateMonthlyAvg(monthlyData.values);
            monthlyPrices[year][month] = monthly_price;
        });
    });


});