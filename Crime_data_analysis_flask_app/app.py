# Flask Setup
import os
from flask import Flask
app = Flask(__name__)

# Google Sheets API Setup
import gspread
from oauth2client.service_account import ServiceAccountCredentials

print("test")

credential = ServiceAccountCredentials.from_json_keyfile_name("Crime_data_analysis\CrimeAnalysis-a804da08d954.json",["https://spreadsheets.google.com/feeds",                             "https://www.googleapis.com/auth/spreadsheets",                                                        "https://www.googleapis.com/auth/drive.file",                                                        "https://www.googleapis.com/auth/drive"])
client = gspread.authorize(credential)
gsheet = client.open("crime").sheet1

from routes import *

if __name__ == "__main__":
    #app.run(host='0.0.0.0', debug=False, port=os.environ.get('PORT', 80))
    app.run(debug=True)
print("done")