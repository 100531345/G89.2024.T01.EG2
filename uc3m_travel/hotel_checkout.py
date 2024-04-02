# file for function 3 development
from datetime import datetime
import re
import json
from datetime import datetime, time


# def add_check_out(departure_date, room_key):



class HotelCheckout:

    def get_departure_date_room(room_key):
        # get the departure date
        with open('/Users/matthewibrahim/Desktop/Study_abroad_classes/SoftDev/G89.2024.T01.EG2/uc3m_travel/data/hotel_stay_output.json') as f:
            hotel_stay_output = json.load(f)

        for stay_info in hotel_stay_output:
            if stay_info["Signature"] == room_key:
                return stay_info["Departure"]

    @staticmethod
    def validate_room_key(room_key):
        """
        Validates the provided room key.

        :param room_key: SHA256 hexadecimal string representing the room key.
        :return: True if the room key exists in the output file, False otherwise.
        """

        if not isinstance(room_key, str):

            return False

        with open('/Users/matthewibrahim/Desktop/Study_abroad_classes/SoftDev/G89.2024.T01.EG2/uc3m_travel/data/hotel_stay_output.json') as f:
            hotel_stay_output = json.load(f)

        for stay_info in hotel_stay_output:
            # Check if the key exists in the current object
            if stay_info["Signature"] == room_key:
                return True

        # if room key not found then it is not a valid room key
        return False


    @staticmethod
    def validate_departure_date(room_key):

        """
           Validates the expected dep date of the room key.

           :param departure_date: The departure date to validate.
           :return: True if the departure date received is same as one calculated in func 2, False otherwise.
       """

        if not isinstance(room_key, str):
            return False

        with open('/Users/matthewibrahim/Desktop/Study_abroad_classes/SoftDev/G89.2024.T01.EG2/uc3m_travel/data/hotel_stay_output.json') as f:
            hotel_stay_output = json.load(f)

        current_datetime = datetime.utcnow()
        combined_datetime = current_datetime.replace(hour=0, minute=0, second=0, microsecond=0)
        formatted_datetime = combined_datetime.strftime("%Y-%m-%dT%H:%M:%S")

        for stay_info in hotel_stay_output:
            # Check if the key exists in the current object

            if stay_info["Signature"] == room_key:
                if formatted_datetime == stay_info["Departure"]:
                    # the depature date is valid as it matches the scheduled departure date
                    return True

        # not valid departure date as it does not match the scheduled departure date
        return False


    @staticmethod
    def guest_checkout(room_key):

        filename = "/Users/matthewibrahim/Desktop/Study_abroad_classes/SoftDev/G89.2024.T01.EG2/uc3m_travel/data/check-outs.json"

        timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

        with open(filename, "r+") as f:
            data = json.load(f)
            if HotelCheckout.validate_room_key(room_key) and HotelCheckout.validate_departure_date(room_key):
                data.append({"timestamp": timestamp, "departure_date": HotelCheckout.get_departure_date_room(room_key),
                             "room_key": room_key})
            else:
                return False
            f.seek(0)
            json.dump(data, f)

        return True