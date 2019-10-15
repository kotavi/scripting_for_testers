
## To download data from Jira
# import requests
#
# url = "http://jira.<company-name>/rest/api/latest/search?jql=reporter=dwestervel"
# response = requests.get(url)

# But as there is no <company-name> I'll use pre downloaded data JiraJsonData.json

import json
json_data = open('JiraJsonData.json').read()

data = json.loads(json_data)

status_counts = {}
for project in (data['projects']):
    for issue in project['issues']:
        if issue['status'] not in status_counts.keys():
            status_counts[issue['status']] = 1
        else:
            status_counts[issue['status']] += 1
print (status_counts)

from string import Template

html_template = Template("""<html>
<head>
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script type="text/javascript">
  google.charts.load('current', {packages: ['corechart']});
  google.charts.setOnLoadCallback(drawChart);
  function drawChart () {
      var data = google.visualization.arrayToDataTable([
          $label,
          $data
        ]);

        var options = {
          title: 'Analyze test data'
        };
        var chart = new google.visualization.PieChart(document.getElementById('piechart'));
        chart.draw(data, options);
  };
</script>
</head>
<body>
    <div id="piechart" style="width: 900px; height: 500px;"></div>
</body>
</html>""")

# Convert status_counts dictionary to a format that is acceptable by the template
list_data = ''
for key in status_counts.keys():
    list_data += "['%s', %s],\n" % (key, status_counts[key])
print (list_data)

html_page = html_template.substitute(label=['Issue Type', 'Number of issues'], data=list_data)

with open('ex4_pie_chart.html', 'w') as f:
    f.write(html_page)