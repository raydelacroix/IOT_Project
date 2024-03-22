import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
import random

###log: rayon | projet_iot c'est le nom du l'organisation|   mdp : Davidoetjm2007@  | token API: N1Z1mxpqv85Lk6vr5UGtZODflDPdOZtG2m5lq9IBNDmwQ5PcqSnoYbR8gGi_axlaQTc_LMAjNrT1rlTzzetB1w==

# tmp = random.random() * 100
# hum = random.random() * 100
# temperature = {
#     "payload": tmp
# }

# humidity = {
#     "payload": hum
# }
# output = [temperature, humidity]

bucket ="storage"
org="projet_iot"
token= "QUG3mGi382mSlyqVhh8Y7R9hhk0_S6kdK7S-27NT_kHZ9mE2Z1WdAT2TPjNZfKIe1F5p16pHRZY-SyBmZH2Mhg=="
url ="http://localhost:8086"
client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org
)
write_api = client.write_api(write_options=SYNCHRONOUS)
data= influxdb_client.Point("measurement").tag("building","Trade center").field("temperature",90)
write_api.write(bucket=bucket, org=org, record=data)
