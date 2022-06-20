import requests, json
#library for api requests; library for parsing/converting json files

url = "https://grandtrain.ru/local/components/oscompany/train.class/ajax.php"
#used url for request; name can be different

payload = {'from': '2004000',
'to': '2078750',
'date': '20.07.2020',
'train': '007А',
'service': 'Купе'}
#current payload includes data for search, which can be provided and formatted from API documantation

response = requests.request("POST", url, data = payload)
# POST request with previous headers and/or payload usage; params can be added as well if needed - 'params = params'

loaded_json = json.loads(response.text)
#set response text value to variable and load it for parse as json

cars = loaded_json['Cars']
#select part of json file relevant to Cars

indexed_cars = cars[0]
#filter first line which indexed as 0

print("Service status code is "+str(response.status_code))
#printing service status code

print("Exists cars type " + indexed_cars['Type'])
#print value from Type field in Cars section

