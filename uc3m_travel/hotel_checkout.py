import json
from datetime import datetime
from uc3m_travel import HotelManagementException

class HotelCheckout:

    @staticmethod
    def get_departure_date_room(room_key):
        try:
            with open('/Users/matthewibrahim/Desktop/Study_abroad_classes/SoftDev/G89.2024.T01.EG2/uc3m_travel/data/hotel_stay_output.json') as f:
                hotel_stay_output = json.load(f)

            for stay_info in hotel_stay_output:
                if stay_info["Signature"] == room_key:
                    return stay_info["Departure"]
        except FileNotFoundError:
            raise HotelManagementException("Hotel stay data file not found.")

    @staticmethod
    def validate_room_key(room_key):
        try:
            with open('/Users/matthewibrahim/Desktop/Study_abroad_classes/SoftDev/G89.2024.T01.EG2/uc3m_travel/data/hotel_stay_output.json') as f:
                hotel_stay_output = json.load(f)

            for stay_info in hotel_stay_output:
                if stay_info["Signature"] == room_key:
                    return True
        except FileNotFoundError:
            raise HotelManagementException("Hotel stay data file not found.")

        raise HotelManagementException("The room key is not registered")

    @staticmethod
    def validate_departure_date(room_key):
        try:
            with open('/Users/matthewibrahim/Desktop/Study_abroad_classes/SoftDev/G89.2024.T01.EG2/uc3m_travel/data/hotel_stay_output.json') as f:
                hotel_stay_output = json.load(f)

            current_datetime = datetime.utcnow()
            formatted_datetime = current_datetime.strftime("%Y-%m-%dT%H:%M:%S")

            for stay_info in hotel_stay_output:
                if stay_info["Signature"] == room_key:
                    if formatted_datetime == stay_info["Departure"]:
                        return True
        except FileNotFoundError:
            raise HotelManagementException("Hotel stay data file not found.")

        raise HotelManagementException("The dep date is not registered/valid.")

    @staticmethod
    def guest_checkout(room_key):
        try:
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
        except FileNotFoundError:
            raise HotelManagementException("Checkout data file not found.")
