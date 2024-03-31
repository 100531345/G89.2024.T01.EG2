"""Module: hotel_reservation.py"""

import hashlib
from datetime import datetime
from math import abs
import hotel_manager.py
import hotel_management_exception

VALID_ROOM_TYPES = ["SINGLE", "DOUBLE", "TRIPLE"]

#this is the method I am making for function 1, we should consider moving this to inside a class

def request_reservation(credit_card_number, id_card, name_surname, phone_number, room_type, arrival, num_days):
    if not is_instance(int, credit_card_number) or len(str(abs(credit_card_number))) != 16 or not HotelManager.validate_credit_card(credit_card_number):
        raise HotelManagementException("Something is wrong with the credit card number")
    if not is_instance(str, id_card) or len(id_card) != 8: #still need to add nif alg compliance and check length
        raise HotelManagementException("Something is wrong with the id card number still need to add nif alg check")
    if not is_instance(str, name_surname) or len(name_surname) < 10 or len(name_surname) > 50:
        raise HotelManagementException("Something is wrong with name surname")
    if not is_instance(int, phone_number) or len(phone_number) != 9:
        raise HotelManagementException("Something is wrong with the phone number")
    if not is_instance(str, room_type) or room_type not in VALID_ROOM_TYPES:
        raise HotelManagementException("Something is wrong with the room type")
    if not is_instance(str, arrival) or len(arrival) != 10: #add the rest of the checks about valid dates
        raise HotelManagementException("Something is wrong with the arrival date")
    if not is_instance(int, num_days) or num_days < 1 or num_days > 10:
        raise HotelManagementException("Something is wrong with num days")


    return "function not implemented"

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
