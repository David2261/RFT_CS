import json
from datetime import datetime
import random

import logging
import logging.config

from RFTCS.setup.logging_conf import LOGGING_CONF

logging.config.dictConfig(LOGGING_CONF)
logger = logging.getLogger("dev")
log_info = logging.getLogger("root")

try:
    from numpyencoder import NumpyEncoder
except Exception as ex:
    logger.error(f"Ошибка с импортированием функкций исключений... {ex}")
    print("You may not have connected the numpy library")

try:
    from RFTCS.exceptions.exception import invalid_general
except Exception as ex:
    logger.error(f"Ошибка с импортированием функкций исключений... {ex}")


class JsonLoad:
    """ Return data with json format file """
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def generate_data(self):
        if self.name == 'TotalOil':
            json_data = [
                {
                    "id": ''.join(
                        [
                            random.choice(list('123456789ABCDEF'))
                            for x in range(12)]),
                    "speed": self.data[0],
                    "oil": self.data[1],
                    "date": datetime.now().strftime('%d.%m.%y | %X')
                }
            ]
        elif self.name == 'FlightBallistics':
            json_data = [
                {
                    "id": ''.join(
                        [
                            random.choice(list('123456789ABCDEF'))
                            for x in range(12)]),
                    "flight_range": self.data[0],
                    "flight_time": self.data[1],
                    "date": datetime.now().strftime('%d.%m.%y | %X')
                }
            ]
        elif self.name == 'ModelFlight':
            json_data = [
                {
                    "id": ''.join(
                        [
                            random.choice(list('123456789ABCDEF'))
                            for x in range(12)]),
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
                    "id": ''.join(
                        [
                            random.choice(list('123456789ABCDEF'))
                            for x in range(12)]),
                    "message": "ERROR DATA",
                    "date": datetime.now().strftime('%d.%m.%y | %X')
                }
            ]
        return json_data

    def json_entire(self):
        try:
            with open(
                    'record.json',
                    'r',
                    encoding='utf-8',
                    errors='ignore') as f:
                data_file = json.loads(f.read())
        except Exception as ex:
            logger.error(invalid_general(ex))
        json_data = self.generate_data()
        data_file.append(json_data)
        try:
            with open('record.json', 'w', encoding='utf-8') as file:
                json.dump(
                    data_file,
                    file,
                    indent=2,
                    separators=(', ', ': '),
                    cls=NumpyEncoder)
        except Exception as ex:
            logger.error(invalid_general(ex))

    def json_generate(self):
        json_data = self.generate_data()
        try:
            with open('record.json', 'w', encoding='utf-8') as file:
                json.dump(
                    json_data,
                    file,
                    indent=2,
                    separators=(', ', ': '),
                    cls=NumpyEncoder)
        except Exception as ex:
            logger.error(invalid_general(ex))

    def json_main(self):
        try:
            with open('record.json', 'r', encoding='utf-8'):
                self.json_entire()
        except IOError:
            self.json_generate()


if __name__ == '__main__':
    load = JsonLoad('TotalOil', (450, 230))
    load.json_main()
