"""Module: hotel_manager.py"""

import json
from uc3m_travel import HotelManagementException
from uc3m_travel import HotelReservation


class HotelManager:
    """Custom class for hotel management."""

    def __init__(self):
        pass

    def validate_credit_card(self, x):
        """Validates a credit card."""
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
