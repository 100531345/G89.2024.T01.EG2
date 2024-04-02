"""Module: hotel_manager.py"""

import json
from uc3m_travel import HotelManagementException
from uc3m_travel import HotelReservation
from stdnum.es import nif
import os

VALID_ROOM_TYPES = ["SINGLE", "DOUBLE", "TRIPLE"]

# def request_checkout(deproom_key):
#     if not isinstance()

def room_reservation(credit_card_number, id_card, name_surname, phone_number, room_type, arrival,
                        num_days):
    if not isinstance(credit_card_number, int) or len(
            str(abs(credit_card_number))) != 16 or not HotelManager.validate_credit_card(
            credit_card_number):
        raise HotelManagementException("bad credit card number")
    if not isinstance(id_card, str) or len(id_card) != 9 or not nif.is_valid(id_card):  # still need to add nif alg compliance and check length
        raise HotelManagementException("bad id card")
    if not isinstance(name_surname, str) or len(name_surname) < 10 or len(name_surname) > 50:
        raise HotelManagementException("bad name surname")
    if not isinstance(phone_number, int) or len(str(phone_number)) != 9:
        raise HotelManagementException("bad phone number")
    if not isinstance(room_type, str) or room_type not in VALID_ROOM_TYPES:
        raise HotelManagementException("bad room type")
    if not isinstance(arrival, str) or len(
            arrival) != 10:  # add the rest of the checks about valid dates
        raise HotelManagementException("bad arrival")
    arrival = arrival.split("/")
    if len(arrival) != 3 or len(arrival[0]) != 2 or len(arrival[1]) != 2 or len(arrival[2]) != 4:
        raise HotelManagementException("bad arrival")
    for i in range(len(arrival)):
        try:
            arrival[i] = int(arrival[i])
        except:
            raise HotelManagementException("bad arrival")
    if arrival[0] < 1 or arrival[0] > 31 or arrival [1] < 1 or arrival[1] > 12:
        raise HotelManagementException("bad arrival")
    if not isinstance(num_days, int) or num_days < 1 or num_days > 10:
        raise HotelManagementException("bad num days")

    data = {
        'credit_card_number': credit_card_number,
        'id_card': id_card,
        'name_and_sur': name_surname,
        'phone_num': phone_number,
        'room_type': room_type,
        'num_days': num_days,
    }
    reservation = HotelReservation(data)
    localizer = reservation.localizer

    #do some checking in the file to make sure name name_surname doesn't exist
    #this would mean the client already has a reservation

    current_dir = os.getcwd()
    parent_dir = os.path.dirname(current_dir)
    parent_dir = os.path.dirname(parent_dir)
    adjacent_dir = os.path.join(parent_dir, 'data')
    file_name = 'hotel_reservations.json'
    file_path = os.path.join(adjacent_dir, file_name)

    hotel_data = HotelManager.read_data_from_json(file_path)
    for res in hotel_data:
        if res["name_surname"] == name_surname:
            raise HotelManagementException("There is already a reservation for this customer")

    write_file_path = os.path.join(adjacent_dir, 'hotel_reservations.json')
    reservation.write_to_file(write_file_path)

    return reservation.localizer


class HotelManager:
    """Custom class for hotel management."""

    def __init__(self):
        pass

    @staticmethod
    def validate_credit_card(x):
        """Validates a credit card."""
        # turn the int value into a string
        x = str(x)
        # Remove any non-digit characters from the input string
        x = ''.join(filter(lambda char: char.isdigit(), x))

        # Reverse the string
        x = x[::-1]

        total = 0
        for index, digit_char in enumerate(x):
            digit = int(digit_char)

            # Double every second digit
            if index % 2 == 1:
                digit *= 2

                # If the doubled digit is greater than 9, subtract 9
                if digit > 9:
                    digit -= 9

            total += digit

        # The number is valid if the total is a multiple of 10
        return total % 10 == 0

    # def read_data_from_json(self, fi, encoding="utf-8"):
    #     """Reads data from JSON with specified encoding."""
    #     try:
    #         with open(fi, encoding=encoding) as f:
    #             data = json.load(f)
    #     except FileNotFoundError as e:
    #         raise HotelManagementException("Wrong file or file path") from e
    #     except json.JSONDecodeError as e:
    #         raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from e
    #
    #     try:
    #         c = data["CreditCard"]
    #         p = data["phoneNumber"]
    #         res_data = {
    #             'id_card': '12345678Z',
    #             'credit_card_number': c,
    #             'name_and_sur': 'John Doe',
    #             'phone_num': p,
    #             'room_type': 'single',
    #             'num_days': 3
    #         }
    #         req = HotelReservation(res_data)
    #     except KeyError as e:
    #         raise HotelManagementException("JSON Decode Error - Invalid JSON Key") from e
    #     if not self.validate_credit_card(c):
    #         raise HotelManagementException("Invalid credit card number")
    #
    #     # Close the file
    #     return req

    @staticmethod
    def read_data_from_json(fi, encoding="utf-8"):
        try:
            with open(fi, encoding=encoding, mode='r') as f_base:
                data = json.load(f_base)
        except FileNotFoundError as e:
            raise HotelManagementException("The data file cannot be found.") from e
        except json.JSONDecodeError as e2:  # raise
            data = []
        return data
