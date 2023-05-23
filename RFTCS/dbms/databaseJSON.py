import json
from datetime import datetime
import random
import numpy as np
from numpyencoder import NumpyEncoder


class JsonLoad:
    """ Return data with json format file """
    def __init__(self, name, data):
        self.name = name
        self.data = data
    
    def generate_data(self):
        if self.name == 'TotalOil':
            json_data = [
                {
                    "id": np.random.randint(low=0, high=10, size=(10,)).astype(int),
                    "speed": self.data[0],
                    "oil": self.data[1],
                    "date": datetime.now().strftime('%d.%m.%y | %X')
                }
            ]
        elif self.name == 'FlightBallistics':
            json_data = [
                {
                    "id": np.random.randint(low=0, high=10, size=(10,)).astype(int),
                    "flight_range": self.data[0],
                    "flight_time": self.data[1],
                    "date": datetime.now().strftime('%d.%m.%y | %X')
                }
            ]
        elif self.name == 'ModelFlight':
            json_data = [
                {
                    "id": np.random.randint(low=0, high=10, size=(10,)).astype(int),
                    "flow": self.data[0],
                    "mass": self.data[1],
                    "speed_0": self.data[2],
                    "date": datetime.now().strftime('%d.%m.%y | %X')
                }
            ]
        else:
            print("error")
            json_data = [
                {
                    "id": np.random.randint(low=0, high=10, size=(10,)).astype(int),
                    "message": "ERROR DATA",
                    "date": datetime.now().strftime('%d.%m.%y | %X')
                }
            ]
        return json_data
    
    def json_entire(self):
        data_file = json.load(open('record.json'))
        json_data = self.generate_data()
        data_file.append(json_data)
        with open('record.json', 'w', encoding='utf-8') as file:
            json.dump(data_file, file, indent=2, separators=(', ', ': '), cls=NumpyEncoder)

    def json_generate(self):
        json_data = self.generate_data()
        with open('record.json', 'w', encoding='utf-8') as file:
            json.dump(json_data, file, indent=2, separators=(', ', ': '), cls=NumpyEncoder)

    def json_main(self):
        try:
            with open('record.json', 'r', encoding='utf-8') as file:
                self.json_entire()
        except IOError:
            self.json_generate()

if __name__ == '__main__':
    load = JsonLoad('TotalOil', (450, 230))
    load.json_main()