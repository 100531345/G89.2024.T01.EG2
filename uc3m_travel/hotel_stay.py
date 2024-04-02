""" Class HotelStay (GE2.2) """
from datetime import datetime
import hashlib
import json
from uc3m_travel import HotelManagementException
from datetime import timedelta

def read_data_from_json(fi, encoding="utf-8"):
    try:
        with open(fi, encoding=encoding, mode='r') as f_base:
            data = json.load(f_base)
    except FileNotFoundError as e:
        raise HotelManagementException("The data file cannot be found.") from e
    except json.JSONDecodeError as e2:  # raise
        raise HotelManagementException("The JSON does not have the expected structure.") from e2
    return data

def guest_arrival(input_file):
    # check file exists
    try:
        with open(input_file, encoding="utf-8", mode='r') as f:
            data = json.load(f)
    except FileNotFoundError as e:
        raise HotelManagementException("The data file cannot be found.") from e
    except json.JSONDecodeError as e2:  # raise
        raise HotelManagementException("The file is not in JSON format.") from e2
    if not isinstance(data, dict):
        raise HotelManagementException("The file is not in JSON format.")

    current = ""
    try:
        localizer = data.get("Localizer")
        id_card = data.get("IdCard")
        if not isinstance(id_card, str) or not isinstance(localizer, str):
            raise HotelManagementException("The JSON does not have the expected structure.")
    except AttributeError:
        raise HotelManagementException("The JSON does not have the expected structure.")

    hotel_data = read_data_from_json(
        "/Users/connorloughlin/Documents/PycharmProjects/G89.2024.T01.EG2TWO/uc3m_travel/data"
        "/hotel_stay_test_data.json")
    # check localizer exists in hotel_data, then that ID matches
    loc_found = False
    id_found = False
    for stay in hotel_data:
        if localizer == stay["Localizer"]:
            loc_found = True
            if id_card == stay["idCard"]:
                id_found = True
                # check if dates are right here
                arrival = stay["arrival"]
                arrival_date = datetime.strptime(arrival, "%d/%m/%Y")
                num_days = stay["num_days"]
                if datetime.now() < arrival_date:
                    raise HotelManagementException("The arrival date does not correspond to the reservation date.")
                current = HotelStay(id_card, localizer, num_days, stay["Type"])
                current_datetime = datetime.now()
                if current_datetime > current.departure:
                    raise HotelManagementException("The arrival date does not correspond to the reservation date.")
    if not id_found or not loc_found:
        raise HotelManagementException("The locator does not correspond to the stored data")

    # Creates a file that includes the data with all the processed stays.
    stay.write_to_file("/Users/connorloughlin/Documents/PycharmProjects/G89.2024.T01.EG2TWO/uc3m_travel/data"
                       "/hotel_stay_output.json")

    # Returns hexadecimal string with the room key (HM-FR-02-O1)
    return current.hex_str


class HotelStay:
    """Custom class for hotel stays."""

    def __init__(self, idcard, localizer, num_days, room_type):
        self.__alg = "SHA-256"
        self.__type = room_type
        self.__idcard = idcard
        self.__localizer = localizer
        justnow = datetime.utcnow()
        self.__arrival = justnow.strftime("%d/%m/%Y")
        # timestamp is represented in seconds.miliseconds
        # to add the number of days we must express numdays in seconds
        num_days = int(num_days)
        self.departure = datetime.now() + timedelta(days=num_days)
        self.hex_str = self.__signature_string()

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

    def to_dict(self):
        """Convert the HotelStay instance to a dictionary."""
        return {
            "Algorithm": self.__alg,
            "Type": self.__type,
            "IdCard": self.__idcard,
            "Localizer": self.__localizer,
            "Arrival": self.__arrival.isoformat(),
            "Departure": self.__departure.isoformat(),
            "Signature": self.hex_str
        }

    def write_to_file(self, filename):
        """Write the HotelStay data to a JSON file."""
        data = self.to_dict()
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)