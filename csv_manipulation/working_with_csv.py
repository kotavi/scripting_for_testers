import csv


def read_csv(file_name='TestTimingData.csv'):
    timing_data = []
    with open(file_name) as csv_file:
        file_reader = csv.reader(csv_file)
        for row in file_reader:
            timing_data.append(row)
    return timing_data


def extract_data(input_data):
    column_chart_data = [['Test Name', 'Diff From Avg']]
    table_data = [['Test Name', 'Run Time (s)']]

    for row in input_data[1:]:
        test_name = row[0]
        if not row[1] or not row[2]:
            continue
        current_run_time = float(row[1])
        avg_run_time = float(row[2])
        diff_from_avg = avg_run_time - current_run_time
        column_chart_data.append([test_name, diff_from_avg])
        table_data.append([test_name, current_run_time])
    print(column_chart_data)
    print(table_data)
    return column_chart_data, table_data


if __name__ == "__main__":
    data = read_csv()
    (columnChartData, tableData) = extract_data(data)
    print(columnChartData)
    print(tableData)

