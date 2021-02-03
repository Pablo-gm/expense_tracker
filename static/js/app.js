
var currencyFormat = new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
});

let category_display_names = {
    'INC': 'Income',
    'TRA': 'Transportation',
    'HOU': 'Housing',
    'FOO': 'Food & Groceries',
    'UTL': 'Utilities',
    'MED': 'Medical & Insurance',
    'SAV': 'Savings',
    'PER': 'Personal',
    'ENT': 'Entertainment',
    'EDU': 'Education',
    'GIF': 'Gifts & Donations'
}

let category_colors = {
    'INC': '#21cc76',
    'TRA': '#ffcd43',
    'HOU': '#09d7e6',
    'FOO': '#5f5cff',
    'UTL': '#2f3132',
    'MED': '#e02d3f',
    'SAV': '#fd7e14',
    'PER': '#d92b71',
    'ENT': '#0d69fd',
    'EDU': '#2ce6af',
    'GIF': '#d92b71'
}

let category_label_colors = {
    'INC': '#000000',
    'TRA': '#000000',
    'HOU': '#000000',
    'FOO': '#ffffff',
    'UTL': '#ffffff',
    'MED': '#ffffff',
    'SAV': '#000000',
    'PER': '#ffffff',
    'ENT': '#ffffff',
    'EDU': '#000000',
    'GIF': '#ffffff'
}

// Sort json object if neccesary
//const chart_info = Object.entries(chart_info2).sort(([,a],[,b]) => b-a).reduce((r, [k, v]) => ({ ...r, [k]: v }), {});

function drawDoughnut(chart_info, balance, chart_selector){
    let chart_labels = Object.keys(chart_info).map(str => category_display_names[str])
    let chart_values = Object.values(chart_info).map(num => Number(num));
    let chart_fill_colors = Object.keys(chart_info).map(str => category_colors[str])
    let chart_labels_colors = Object.keys(chart_info).map(str => category_label_colors[str])
    
    let budget_balance = balance;
    
    var options = {
        series: chart_values,
        chart: {
            type: 'donut',
        },
        colors: chart_fill_colors,
        responsive: [{
            breakpoint: 480,
            options: {
                chart: {
                    height: 400
                },
                legend: {
                    position: 'bottom'
                }
            }
        }],
        legend: {
            show: true,
            position: 'bottom'
        },
        labels:
            chart_labels,
        dataLabels: {
            enabled: true,
            style: {
                fontSize: '12px',
                fontFamily: 'Inter, Helvetica, Arial, sans-serif',
                fontWeight: 'bold',
                colors: chart_labels_colors
            },
            dropShadow: {
                enabled: false,
                blur: 3,
                opacity: 0.8
            }
        },
        plotOptions: {
            pie: {
                donut: {
                    size: '66%',
                    labels: {
                        show: true,
                        showAlways: true,
                        value: {
                            fontWeight: 600,
                            color: '#2f3132',
                            fontFamily: 'Inter, Helvetica, Arial, sans-serif',
                            formatter: (v) => currencyFormat.format(v)
                        },
                        total: {
                            show: true,
                            label: 'TOTAL:',
                            color: '#777b7d',
                            fontSize: '18px',
                            fontFamily: 'Inter, Helvetica, Arial, sans-serif',
                            fontWeight: 500,
                            formatter: () => currencyFormat.format(budget_balance)
                        }
                    }
                }
            }
        },
        tooltip: {
            y: {
                formatter: (v) => currencyFormat.format(v)
            },
        }
    };
    
    var chart = new ApexCharts(document.querySelector(chart_selector), options);
    chart.render();
    
}

function drawBars(chart_info, chart_selector){

    let chart_labels = Object.keys(chart_info).map(str => category_display_names[str])
    let chart_values = Object.values(chart_info).map(num => Number(num));
    let chart_fill_colors = Object.keys(chart_info).map(str => category_colors[str])

    var bar_values = [];
    for(let i = 0; i < chart_values.length; i++){
        bar_values.push({name: chart_labels[i], data:chart_values[i]})
    }


    var options = {
        series: [{
            name: 'Total expenses',
            data: chart_values
        }],
        colors:  chart_fill_colors,
        chart: {
            type: 'bar',
            toolbar: { show: false},
            height: chart_values.length * 40 + 48
        },
        plotOptions: {
            bar: {
                horizontal: true,
                distributed: true,
                barHeight: '100%',
                dataLabels: {
                    position: 'bottom'
                }
            }
        },
        legend: {
                show: false,
                position: 'bottom'
            },
            
        dataLabels: {
            enabled: false
        },
        xaxis: {
            categories: chart_labels,
            //max: chart_values[chart_values.length - 1],
            tickAmount: 5,
            axisBorder: {
                color: '#d5dde0'
            },
            axisTick: {
                color: '#d5dde0'
            }
        },
        yaxis: {
            categories: Object.keys(chart_info),
            labels: {
                show: true,
                color: '#2f3132',
                fontSize: '14px'
            }
        },
        tooltip: {
            fillSeriesColor: false,
            style: {
                fontSize: '12px',
                fontFamily: 'Inter, Helvetica, Arial, sans-serif'
            },
            y: {
                formatter: (v) => currencyFormat.format(v)
            },
        }
    };


    var chart = new ApexCharts(document.querySelector(chart_selector), options);
    chart.render();
}
