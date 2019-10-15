#!/usr/bin/python

from string import Template
from csv_manipulation import working_with_csv

(column_chart_data, table_data) = working_with_csv.extract_data(working_with_csv.read_csv('csv_manipulation/TestTimingData.csv'))

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
      
    var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
    chart.draw(data);
  }
</script>
</head>
<body>
    <div id="chart_div" style="width:1000; height:600"></div>
</body>
</html>""")


chart_data_string = ''
for row in column_chart_data[1:]:
    chart_data_string += "%s,\n" %row
print (chart_data_string)
completed_html = html_template.substitute(labels=column_chart_data[0], data=chart_data_string)

with open('ex1_column_chart.html', 'w') as f:
    f.write(completed_html)