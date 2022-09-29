# CREATE A FUNCTION WHICH WILL BE ASK ENDPOINT WITH WEBSITE CONTAINING EXCHANGE RATES

# ADD EXCEPTIONS TRY: & EXCEPT

# ADD SECOND FUNCTIONS WHICH WILL BE MEASURING TIME OF DURATION AND TIME + DATE WHEN THE REQUEST HAPPEND

# RETURN THIS REQUEST IN PRINT

# WHOLE PROGRAMM SHOULD BE DONE IN A LOOP IN INTERVAL OF 15 MINUTES

# IN ADDITION GENERETE THE CSV REPORT API: Zprxvd3LMsHWToQBzoPWvXmnglmqfaCT

import requests
import time
import pandas as pd
import json

file = json.loads(doc)
json = pd.DataFrame({'data': file})

url = "https://api.apilayer.com/exchangerates_data/latest?symbols=PLN,EUR,GBP&base=USD"
url2 = "https://api.apilayer.com/exchangerates_data/latest?symbols=USD,EUR,GBP&base=PLN"


payload = {}
headers= {
  "apikey": "Zprxvd3LMsHWToQBzoPWvXmnglmqfaCT"
}

response = requests.request("GET", url, headers=headers, data = payload)
response2 = requests.request("GET", url2, headers=headers, data = payload)

#Status code for url 1 & 2
status_code = response.status_code
status_code2 = response2.status_code

#Text Result for url endpoint 1 & 2
result = response.text
result2 = response2.text

while True:
    try:
        print(result)
        result.to_csv("response.csv")
        
    except:
        print('We could not download the Exchange rates. Please upgrade API Plan')
    time.sleep(120)
        
        










