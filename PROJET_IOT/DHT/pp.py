import random

tmp = random.random() * 100
hum = random.random() * 100
temperature = {
    "payload": tmp
}

humidity = {
    "payload": hum
}

output = [temperature, humidity]
print(output[0]["payload"])
print(output[1]["payload"])