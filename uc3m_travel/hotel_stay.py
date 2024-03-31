""" Class HotelStay (GE2.2) """
from datetime import datetime
import hashlib
import json
from uc3m_travel import HotelManagementException


def guest_arrival(input_file):
    arrival_data = read_data_from_json(input_file)
    localizer = arrival_data["Localizer"]
    id_value = arrival_data["idCard"]
    hotel_data = read_data_from_json("uc3m_travel/data/hotel_stay_test_data.json")
    # check localizer exists in hotel_data, then that ID matches
    # if valid, generate an instance of the HotelStay class

    # Returns hexadecimal string with the room key (HM-FR-02-O1)
    # Returns a file that includes the data with all the processed stays.
    return


def read_data_from_json(fi, encoding="utf-8"):
    try:
        with open(fi, encoding=encoding, mode='r') as f:
            data = json.load(f)
    except FileNotFoundError as e:
        raise HotelManagementException("Wrong file or file path") from e
    except json.JSONDecodeError as e2: # raise
        raise HotelManagementException("Wrong file or file path") from e2
        # EDIT THIS ONE
    return data


class HotelStay:
    """Custom class for hotel stays."""

    def __init__(self, idcard, localizer, num_days, room_type):
        self.__alg = "SHA-256"
        self.__type = room_type
        self.__idcard = idcard
        self.__localizer = localizer
        justnow = datetime.utcnow()
        self.__arrival = justnow
        # timestamp is represented in seconds.miliseconds
        # to add the number of days we must express numdays in seconds
        self.__departure = self.__arrival + (num_days * 24 * 60 * 60)

    def __signature_string(self):
        """Composes the string to be used for generating the key for the room"""
        return "{alg:" + self.__alg + ",typ:" + self.__type + ",localizer:" + \
            self.__localizer + ",arrival:" + self.__arrival + \
            ",departure:" + self.__departure + "}"

    @property
    def id_card(self):
        """Property that represents the product_id of the patient"""
        return self.__idcard

    @id_card.setter
    def id_card(self, value):
        self.__idcard = value

    @property
    def localizer(self):
        """Property that represents the order_id"""
        return self.__localizer

    @localizer.setter
    def localizer(self, value):
        self.__localizer = value

    @property
    def arrival(self):
        """Property that represents the phone number of the client"""
        return self.__arrival

    @property
    def room_key(self):
        """Returns the sha256 signature of the date"""
        return hashlib.sha256(self.__signature_string().encode()).hexdigest()

    @property
    def departure(self):
        """Returns the issued at value"""
        return self.__departure

    @departure.setter
    def departure(self, value):
        self.__departure = value
