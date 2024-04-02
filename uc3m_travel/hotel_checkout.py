"""
This module handles process of checking out of the hotel.

It includes functionalities for loading hotel stay data from JSON files, validating room keys,
validating departure dates, and managing guest checkouts. This makes sure that the  checkout process
is executed correctly.
"""
import json
import os
from datetime import datetime
from uc3m_travel import HotelManagementException


class HotelCheckout:
    """
        HotelCheckout manages the checkout process for a hotel management system.

        It includes functionalities to validate departure dates, retrieve departure dates
        for specific room keys, and handle guest checkouts. This class ensures that the
        checkout process is executed correctly, verifying that room keys are valid and that
        departures occur as scheduled.
        """

    @staticmethod
    def get_departure_date_room(roomKey):
        """
        Retrieves the departure date for a given room key from the hotel stay output data.

        :param roomKey: The room key to search the departure date for.
        :type roomKey: str
        :return: The departure date for the given room key.
        :rtype: str
        :raises HotelManagementException: If the hotel stay data file is not found or the room key does not exist.
        """
        script_dir = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(script_dir, "data", "hotel_stay_output.json")

        try:
            with open(filename, encoding='utf-8') as f:
                hotel_stay_output = json.load(f)

            for stay_info in hotel_stay_output:
                if stay_info["Signature"] == roomKey:
                    return stay_info["Departure"]
        except FileNotFoundError as exc:
            raise HotelManagementException("Hotel stay data file not found.") from exc

        raise HotelManagementException("Room key does not exist.")

    @staticmethod
    def validate_room_key(roomKey):
        """
        Validate if the provided room key exists in the hotel stay data.

        :param roomKey: The room key to be validated.
        :type roomKey: str
        :return: True if the room key is found, False otherwise.
        :rtype: bool
        :raises HotelManagementException: If the hotel stay data file is not found or the room key is not registered.
        """
        script_dir = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(script_dir, "data", "hotel_stay_output.json")

        try:
            with open(filename, encoding='utf-8') as f:
                hotel_stay_output = json.load(f)

            for stay_info in hotel_stay_output:
                if stay_info["Signature"] == roomKey:
                    return True

            # If the loop completes without finding a matching room key, raise an exception
            raise HotelManagementException("The room key is not registered")
        except FileNotFoundError as exc:
            # Re-raise the FileNotFoundError with a more informative message
            raise HotelManagementException(f"Hotel stay data file not found.{exc}") from exc

    @staticmethod
    def validate_departure_date(roomKey):
        """
        Validate the departure date for a given room key.

        :param roomKey: The room key for which to validate the departure date.
        :type roomKey: str
        :return: True if the departure date is valid for the given room key, False otherwise.
        :rtype: bool
        :raises HotelManagementException: If the hotel stay data file is not found or the departure date is not registered/valid.
        """
        script_dir = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(script_dir, "data", "hotel_stay_output.json")

        try:
            with open(filename, encoding='utf-8') as f:
                hotel_stay_output = json.load(f)

            current_datetime = datetime.utcnow()
            formatted_datetime = current_datetime.strftime("%Y-%m-%dT%H:%M:%S")

            for stay_info in hotel_stay_output:
                if stay_info["Signature"] == roomKey:
                    if formatted_datetime == stay_info["Departure"]:
                        return True

            # If the loop completes without finding a matching room key, raise an exception
            raise HotelManagementException("The departure date is not registered/valid.")
        except FileNotFoundError as exc:

            raise HotelManagementException(f"Hotel stay data file not found.{exc}") from exc

    @staticmethod
    def guest_checkout(roomKey):
        """
            Perform guest checkout and update the checkout data file.

            :param roomKey: The room key for the guest.
            :type roomKey: str
            :return: True if checkout is successful, False otherwise.
            :rtype: bool
            :raises HotelManagementException: If the checkout data file is not found.
            """
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            filename = os.path.join(script_dir, "data", "check-outs.json")
            timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

            with open(filename, "r+", encoding="utf-8") as f:
                data = json.load(f)
                if (HotelCheckout.validate_room_key(roomKey)
                        and HotelCheckout.validate_departure_date(roomKey)):
                    data.append({"timestamp": timestamp,
                                 "departure_date": HotelCheckout.get_departure_date_room(roomKey),
                                 "room_key": roomKey})
                else:
                    return False
                f.seek(0)
                json.dump(data, f)
            return True
        except FileNotFoundError as exc:
            raise HotelManagementException(f"Checkout data file not found.{exc}") from exc
