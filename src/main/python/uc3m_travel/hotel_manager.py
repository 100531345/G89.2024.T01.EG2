"""Module: hotel_manager.py"""
import json
import os
from stdnum.es import nif
from .hotel_reservation import HotelReservation
from .hotel_management_exception import HotelManagementException
from pathlib import Path

VALID_roomTypeS = ["SINGLE", "DOUBLE", "TRIPLE"]


def roomReservation(creditCardNumber, idCard, nameSurname, phoneNumber, roomType, arrival,
                        numDays):
    """function1 of the assignment"""
    if not isinstance(creditCardNumber, int) or len(
            str(abs(creditCardNumber))) != 16 or not HotelManager.validate_credit_card(
            creditCardNumber):
        raise HotelManagementException("bad credit card number")
    if not isinstance(idCard, str) or len(idCard) != 9 or not nif.is_valid(idCard):  # still need to add nif alg compliance and check length
        raise HotelManagementException("bad id card")
    if not isinstance(nameSurname, str) or len(nameSurname) < 10 or len(nameSurname) > 50:
        raise HotelManagementException("bad name surname")
    names_list = nameSurname.split(" ")
    if not len(names_list) == 2:
        raise HotelManagementException("bad name surname")
    if not isinstance(phoneNumber, int) or len(str(phoneNumber)) != 9:
        raise HotelManagementException("bad phone number")
    if not isinstance(roomType, str) or roomType not in VALID_roomTypeS:
        raise HotelManagementException("bad room type")
    if not isinstance(arrival, str) or len(
            arrival) != 10:  # add the rest of the checks about valid dates
        raise HotelManagementException("bad arrival")
    arrival_list = arrival.split("/")
    if len(arrival_list) != 3 or len(arrival_list[0]) != 2 or len(arrival_list[1]) != 2 or len(arrival_list[2]) != 4:
        raise HotelManagementException("bad arrival")
    for idx, arr in enumerate(arrival_list):
        try:
            arrival_list[idx] = int(arr)
        except Exception as exc:
            raise HotelManagementException("bad arrival") from exc

    if arrival_list[0] < 1 or arrival_list[0] > 31 or arrival_list[1] < 1 or arrival_list[1] > 12:
        raise HotelManagementException("bad arrival")
    if not isinstance(numDays, int) or numDays < 1 or numDays > 10:
        raise HotelManagementException("bad num days")

    data = {
        'credit_card_number': creditCardNumber,
        'id_card': idCard,
        'name_and_sur': nameSurname,
        'phone_num': phoneNumber,
        'room_type': roomType,
        'num_days': numDays,
        'arrival': arrival
    }
    reservation = HotelReservation(data)

    #do some checking in the file to make sure name nameSurname doesn't exist
    #this would mean the client already has a reservation

    __path_data = str(Path.home()) + "/Documents/PycharmProjects/G89.2024.T01.EG2TWO/src/main/python/uc3m_travel/data"
    file_name = 'hotel_reservations.json'
    file_path = os.path.join(__path_data, file_name)

    hotel_data = HotelManager.read_data_from_json(file_path)
    for res in hotel_data:
        if res["name_surname"] == nameSurname:
            raise HotelManagementException("There is already a reservation for this customer")

    # write_file_path = os.path.join(adjacent_dir, 'hotel_reservations.json')
    reservation.write_to_file(file_path)

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

    @staticmethod
    def read_data_from_json(fi, encoding="utf-8"):
        try:
            with open(fi, encoding=encoding, mode='r') as f_base:
                data = json.load(f_base)
        except FileNotFoundError as e:
            raise HotelManagementException("The data file cannot be found.") from e
        except json.JSONDecodeError:  # raise
            data = []
        return data
