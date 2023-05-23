import json
import time
from datetime import datetime

def simular_domicilio(log_file):
    with open(log_file, 'r') as file:
        data = json.load(file)

    data.sort(key=lambda x: datetime.strptime(x['datetime'], "%Y-%m-%dT%H:%M:%S"))

    current_time = datetime.strptime(data[0]['datetime'], "%Y-%m-%dT%H:%M:%S")

    for entry in data:
        event_time = datetime.strptime(entry['datetime'], "%Y-%m-%dT%H:%M:%S")
        time_diff = (event_time - current_time).total_seconds()

        if time_diff > 0:
            time.sleep(time_diff)

        print(f"Sensor: {entry['sensor'].ljust(15)} Valor: {entry['valor'].ljust(50)} Fecha y hora: {entry['datetime']}")

        current_time = event_time
