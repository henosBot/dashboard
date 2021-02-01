from google.cloud import firestore
import os

os.chdir('C:\\Users\\SPI0003\\OneDrive - boxhillhs.vic.edu.au\\Home\\Coding\\bot\\dashboard\\dashboard\\site')
db = firestore.Client.from_service_account_json("firestore.json")