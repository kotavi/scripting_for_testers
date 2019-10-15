# !/usr/bin/python

from string import Template
import csv


data_from_file = []
with open('TestAnalysisData.csv') as csv_data:
    file_reader = csv.reader(csv_data)
    for row in file_reader:
        data_from_file.append(row)

data_from_file_int = []
for row in data_from_file[1:]:
    temp_list = [row[0]]
    for item in row[1:]:
        temp_list.append(int(item))
    data_from_file_int.append(temp_list)
print(data_from_file_int)

chart_data_str = ''
for row in data_from_file_int:
    chart_data_str += "%s,\n" % row
print(chart_data_str)
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

    var options = {
        title: "Example of the colored graph",
        legend: { position: 'top'}
    };

    var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
    chart.draw(data, options);
  }
</script>
</head>
<body>
    <div id="chart_div" style="width:1000; height:800"></div>
</body>
</html>
""")

completed_html = html_template.substitute(labels=["Test Name", "Number of Asserts", "Number of Failed Asserts"], data=chart_data_str)

with open('ex3_column_chart.html', 'w') as f:
    f.write(completed_html)