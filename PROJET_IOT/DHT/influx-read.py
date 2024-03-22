import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

bucket = "storage"
org="projet_iot"
token= "QUG3mGi382mSlyqVhh8Y7R9hhk0_S6kdK7S-27NT_kHZ9mE2Z1WdAT2TPjNZfKIe1F5p16pHRZY-SyBmZH2Mhg=="
url = "http://localhost:8086"

client = influxdb_client.InfluxDBClient(
    url = url,
    token = token,
    org = org
)

query_api = client.query_api()
query = 'from(bucket:"storage")\
|> range(start: -10m)\
|> filter(fn:(r) => r._measurement == "measurement")\
|> filter(fn:(r) => r.building == "Trade Center")\
|> filter(fn:(r) => r._field == "temperature")'

result = query_api.query(org=org, query=query)

results = []

for table in result:
    for record in table.records:
        results.append((record.get_field(), record.get_value()))
#j'ai un souci j'arrive a récupéré les data de influxdb a mon terminal
#voci le tuto que j'ai suivie : https://www.youtube.com/watch?v=8BfYE4qC3NI
print(results)