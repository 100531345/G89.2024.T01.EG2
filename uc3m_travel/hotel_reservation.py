"""Module: hotel_reservation.py"""

import hashlib
from datetime import datetime

#this is the method I am making for function 1, we should consider moving this to inside a class


class HotelReservation:
    """Custom class for hotel reservations."""
    def __init__(self, data):
        self.__idcard = data.get('id_card')
        justnow = datetime.utcnow()
        self.__arrival = datetime.timestamp(justnow)
        self.__name_surname = data.get('name_and_sur')
        self.__phone_number = data.get('phone_num')
        self.__room_type = data.get('room_type')
        self.__num_days = data.get('num_days')
        self.__credit_card_number = data.get('credit_card_number')

    def __str__(self):
        """return a json string with the elements required to calculate the localizer"""
        #VERY IMPORTANT: JSON KEYS CANNOT BE RENAMED
        json_info = {"id_card": self.__idcard,
                     "name_surname": self.__name_surname,
                     "credit_card": self.__credit_card_number,
                     "phone_number:": self.__phone_number,
                     "arrival_date": self.__arrival,
                     "num_days": self.__num_days,
                     "room_type": self.__room_type,
                     }
        return "HotelReservation:" + json_info.__str__()

    @property
    def credit_card(self):
        """Creates credit card log."""
        return self.__credit_card_number

    @credit_card.setter
    def credit_card(self, value):
        """Setter for credit_card."""
        self.__credit_card_number = value

    @property
    def idcard(self):
        """Creates new idcard instance."""
        return self.__idcard

    @idcard.setter
    def idcard(self, value):
        self.__idcard = value

    @property
    def localizer(self):
        """Returns the md5 signature"""
        return hashlib.md5(str(self).encode()).hexdigest()
