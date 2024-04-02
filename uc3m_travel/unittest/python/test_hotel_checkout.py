import json
import unittest
from unittest import TestCase, mock
from freezegun import freeze_time

from uc3m_travel import HotelManagementException
from uc3m_travel.hotel_checkout import HotelCheckout

# test all new functionality
# add hotelmanagement exception
# check new file creation works

class TestHotelCheckout(TestCase):

    # Tests if validate_room_key returns true to valid key
    def test_checkout_TC1(self):
        # Assuming valid_sha256 is defined and represents a valid SHA256 string
        valid_sha256 = "dec56f8cb529f1729316237e89f273407e2c178ac8c565aa7a547e223c4bcc9b"

        # Call the validate_room_key function with the valid_sha256
        result = HotelCheckout.validate_room_key(valid_sha256)

        # Assert that the result is True (indicating the key is valid)
        self.assertEqual(True, result)


    # Tests if validate_room_key returns false to invalid key
    def test_checkout_TC2(self):
        # Assuming valid_sha256 is defined and represents a valid SHA256 string
        valid_sha256 = "dec56f8cb529f17n9316237e89f273407e2c178ac8c565aa7a547e223c4bcc9b"

        # Call the validate_room_key function with the valid_sha256
        # result =

        with self.assertRaises(HotelManagementException):
            HotelCheckout.validate_room_key(valid_sha256)

        # Assert that the result is True (indicating the key is valid)
        # self.assertEqual(False, result)


    # Tests if valid scheduled departure date returns True with manfactured freeze time to match
    @freeze_time("2024-04-03 00:00:00")
    def test_checkout_TC3(self):

        valid_sha256 = "dec56f8cb529f1729316237e89f273407e2c178ac8c565aa7a547e223c4bcc9b"

        self.assertEqual(True, HotelCheckout.validate_departure_date(valid_sha256))

    # Tests if invalid scheduled departure date returns False with manfactured freeze time
    @freeze_time("2024-04-01 00:00:00")
    def test_checkout_TC4(self):

        valid_sha256 = "dec56f8cb529f1729316237e89f273407e2c178ac8c565aa7a547e223c4bcc9b"


        with self.assertRaises(HotelManagementException):
            HotelCheckout.validate_departure_date(valid_sha256)


    # Tests that a valid dep date and a valid room key returns True
    @freeze_time("2024-04-03 00:00:00")
    def test_checkout_TC5(self):

        valid_sha256 = "dec56f8cb529f1729316237e89f273407e2c178ac8c565aa7a547e223c4bcc9b"

        self.assertEqual(True, HotelCheckout.guest_checkout(valid_sha256))




    # Tests that a invalid dep date and a valid room key returns False
    @freeze_time("2024-04-08 00:00:00")
    def test_checkout_TC6(self):

        valid_sha256 = "dec56f8cb529f1729316237e89f273407e2c178ac8c565aa7a547e223c4bcc9b"


        with self.assertRaises(HotelManagementException):
            HotelCheckout.validate_departure_date(valid_sha256)



    # Tests that a valid dep date and a invalid room key returns False
    @freeze_time("2024-04-03 00:00:00")
    def test_checkout_TC7(self):

        valid_sha256 = "dec56f8cb529f1729316237e89l273407e2c178ac8c565aa7a547e223c4bcc9b"

        with self.assertRaises(HotelManagementException):
            HotelCheckout.guest_checkout(valid_sha256)


    # Tests that a invalid dep date and a invalid room key returns False
    @freeze_time("2024-04-02 00:00:00")
    def test_checkout_TC8(self):

        valid_sha256 = "dec56f8cb529f1729316237e89f273407e2c178ac8c565aa7a547e223c4bcc9b"

        with self.assertRaises(HotelManagementException):
            HotelCheckout.guest_checkout(valid_sha256)

    @freeze_time("2024-04-03 00:00:00")
    def test_checkout_TC9(self):
        # Define a room key for testing
        room_key = "dec56f8cb529f1729316237e89f273407e2c178ac8c565aa7a547e223c4bcc9b"

        # Call the guest_checkout function
        result = HotelCheckout.guest_checkout(room_key)

        # Assert that the function returns True, indicating successful checkout
        self.assertTrue(result)

        # Now you can add assertions to check if the data was added to the file
        # For example, you can open the file and check if the added data exists
        with open(
                "/Users/matthewibrahim/Desktop/Study_abroad_classes/SoftDev/G89.2024.T01.EG2/uc3m_travel/data/check-outs.json",
                "r") as f:
            data = json.load(f)
            # Add assertions to check if the added data is present in the file
            self.assertTrue(any(entry["room_key"] == room_key for entry in data))

    # Test case for handling file not found error during room key validation
    def test_checkout_TC10(self):
        with mock.patch("builtins.open", side_effect=FileNotFoundError):
            with self.assertRaises(HotelManagementException) as context:
                HotelCheckout.validate_room_key("valid_sha256")

            self.assertEqual("Hotel stay data file not found.", str(context.exception))

        # Test case for handling file not found error during departure date validation
    def test_checkout_TC11(self):
        with mock.patch("builtins.open", side_effect=FileNotFoundError):
            with self.assertRaises(HotelManagementException) as context:
                HotelCheckout.validate_departure_date("valid_sha256")

            self.assertEqual("Hotel stay data file not found.", str(context.exception))

    def test_checkout_TC12(self):
        with mock.patch("builtins.open", side_effect=FileNotFoundError):
            with self.assertRaises(HotelManagementException) as context:
                HotelCheckout.guest_checkout("valid_sha256")

            self.assertEqual("Checkout data file not found.", str(context.exception))

if __name__ == '__main__':
    unittest.main()
