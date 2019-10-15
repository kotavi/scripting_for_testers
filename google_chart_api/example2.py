#!/usr/bin/python

from string import Template

html_template = Template("""
<html>
<head>
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script type="text/javascript">
  google.charts.load('current', {packages: ['corechart']});
  google.charts.setOnLoadCallback(drawChart);
  function drawChart () {
    var data = google.visualization.arrayToDataTable([
       $labels,
       $data
      ],
      false); // 'false' means that the first row contains labels, not data.
      
    var ranges = [
        [0, 10, '#e53935'],  // red
        [10, 20, '#fdd835'], // yellow
        [20, 30, '#43a047'], // green
        [30, 40, '#1e88e5'], // blue
        [40, 50, '#1ef8e5']  // blue
    ];

    var view = new google.visualization.DataView(data);
    view.setColumns([0, 1, {
        calc: function (dt, row) {
            var rowValue = dt.getValue(row, 1);
            var color;
            ranges.forEach(function (range, index) {
                if ((rowValue >= range[0]) && ((rowValue < range[1]) || (range[1] === null))) {
                color = range[2];
                }
            });
        return color;
        },
        role: 'style',
        type: 'string'
    }]);
  
    var options = {
        title: "Example of the colored graph",
        legend: { position: 'top'}
    };

    var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
    chart.draw(view, options);
  }
</script>
</head>
<body>
    <div id="chart_div" style="width:1000; height:800"></div>
</body>
</html>
""")

data_str = ''
with open('random_set.txt') as f:
    numbers = f.read().split(',')
    for i in range(len(numbers)):
        temp_list = [['Data%s' % i, int(numbers[i])]]
        data_str += "%s,\n" % temp_list[0]
print (data_str)

completed_html = html_template.substitute(labels=['Name', 'Value'], data=data_str)

with open('ex2_column_chart.html', 'w') as f:
    f.write(completed_html)