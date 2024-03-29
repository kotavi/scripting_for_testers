import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name("client_secret2.json", scope)

client = gspread.authorize(credentials)

sheet  = client.open('ServiceAccountTest').sheet1

result = sheet.update_cell(1, 1, "test")
print (result)

result = sheet.row_values(1)
print (result)

result = sheet.get_all_values()
print (result)

my_data = [[1,2,3], [4,5,6], [7,8,9]]

for row_index, row in enumerate(my_data):
    for col_index, value in enumerate(row):
        sheet.update_cell(row_index + 1, col_index + 1, value)



