import json
from .HotelManagementException import HotelManagementException
from .HotelReservation import HotelReservation

class HotelManager:
    def __init__(self):
        pass

    def validatecreditcard( self, x ):
        # Remove any non-digit characters from the input string
        x = ''.join(filter(str.isdigit, x))

        # Reverse the string
        x = x[::-1]

        total = 0
        for i in range(len(x)):
            digit = int(x[i])

            # Double every second digit
            if i % 2 == 1:
                digit *= 2

                # If the doubled digit is greater than 9, subtract 9
                if digit > 9:
                    digit -= 9

            total += digit

        # The number is valid if the total is a multiple of 10
        return total % 10 == 0

    def ReaddatafromJSOn( self, fi):

        try:
            with open(fi) as f:
                DATA = json.load(f)
        except FileNotFoundError as e:
            raise HotelManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from e


        try:
            c = DATA["CreditCard"]
            p = DATA["phoneNumber"]
            req = HotelReservation(IDCARD="12345678Z",creditcardNumb=c,nAMeAndSURNAME="John Doe",phonenumber=p,room_type="single",numdays=3)
        except KeyError as e:
            raise HotelManagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.validatecreditcard(c):
            raise HotelManagementException("Invalid credit card number")

        # Close the file
        return req