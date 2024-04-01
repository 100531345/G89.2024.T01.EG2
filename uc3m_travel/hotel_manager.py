"""Module: hotel_manager.py"""

import json
from uc3m_travel import HotelManagementException
from uc3m_travel import HotelReservation

VALID_ROOM_TYPES = ["SINGLE", "DOUBLE", "TRIPLE"]


def request_reservation(credit_card_number, id_card, name_surname, phone_number, room_type, arrival,
                        num_days):
    if not isinstance(credit_card_number, int) or len(
            str(abs(credit_card_number))) != 16 or not HotelManager.validate_credit_card(
            credit_card_number):
        raise HotelManagementException("bad credit card number")
    if not isinstance(id_card, str) or len(id_card) != 8:  # still need to add nif alg compliance and check length
        raise HotelManagementException(
            "bad id card")
    if not isinstance(name_surname, str) or len(name_surname) < 10 or len(name_surname) > 50:
        raise HotelManagementException("bad name surname")
    if not isinstance(phone_number, int) or len(str(phone_number)) != 9:
        raise HotelManagementException("bad phone number")
    if not isinstance(room_type, str) or room_type not in VALID_ROOM_TYPES:
        raise HotelManagementException("bad room type")
    if not isinstance(arrival, str) or len(
            arrival) != 10:  # add the rest of the checks about valid dates
        raise HotelManagementException("bad arrival")
    if not isinstance(num_days, int) or num_days < 1 or num_days > 10:
        raise HotelManagementException("bad num days")

    data = {
        'credit_card_number': credit_card_number,
        'id_card': id_card,
        'name_surname': name_surname,
        'phone_number': phone_number,
        'room_type': room_type,
        'num_days': num_days,
    }
    reservation = HotelReservation(data)

    return "function not implemented"


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

    def read_data_from_json(self, fi, encoding="utf-8"):
        """Reads data from JSON with specified encoding."""
        try:
            with open(fi, encoding=encoding) as f:
                data = json.load(f)
        except FileNotFoundError as e:
            raise HotelManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from e

        try:
            c = data["CreditCard"]
            p = data["phoneNumber"]
            res_data = {
                'id_card': '12345678Z',
                'credit_card_number': c,
                'name_and_sur': 'John Doe',
                'phone_num': p,
                'room_type': 'single',
                'num_days': 3
            }
            req = HotelReservation(res_data)
        except KeyError as e:
            raise HotelManagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.validate_credit_card(c):
            raise HotelManagementException("Invalid credit card number")

        # Close the file
        return req