"""
This module has the unit tests for the HotelCheckout class in the uc3m_travel package.

It tests many scenarios including validating room keys, checking departure dates, and handling
guest checkouts, making sure  all processes follow expected functionalities and error handling.
"""

import json
import os
import unittest
from unittest import TestCase, mock
from freezegun import freeze_time
from uc3m_travel.hotel_checkout import HotelCheckout
from uc3m_travel.hotel_checkout import HotelManagementException


class TestHotelCheckout(TestCase):
    """
        Manages the checkout process for guests in the hotel.

        This class provides functionality to validate room keys, check departure dates,
        and process guest checkouts. It makes sure that all operations follow the hotel's
        checkout requirements.
    """

    # Tests if validate_room_key returns true to valid key
    def test_checkout_tc1(self):
        # Assuming valid_sha256 is defined and represents a valid SHA256 string
        valid_sha256 = "dec56f8cb529f1729316237e89f273407e2c178ac8c565aa7a547e223c4bcc9b"

        # Call the validate_room_key function with the valid_sha256
        result = HotelCheckout.validate_room_key(valid_sha256)

        # Assert that the result is True (indicating the key is valid)
        self.assertEqual(True, result)

    # Tests if validate_room_key returns false to invalid key
    def test_checkout_tc2(self):
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
    def test_checkout_tc3(self):
        valid_sha256 = "dec56f8cb529f1729316237e89f273407e2c178ac8c565aa7a547e223c4bcc9b"

        self.assertEqual(True, HotelCheckout.validate_departure_date(valid_sha256))

    # Tests if invalid scheduled departure date returns False with manfactured freeze time
    @freeze_time("2024-04-01 00:00:00")
    def test_checkout_tc4(self):
        valid_sha256 = "dec56f8cb529f1729316237e89f273407e2c178ac8c565aa7a547e223c4bcc9b"

        with self.assertRaises(HotelManagementException):
            HotelCheckout.validate_departure_date(valid_sha256)

    # Tests that a valid dep date and a valid room key returns True
    @freeze_time("2024-04-03 00:00:00")
    def test_checkout_tc5(self):
        valid_sha256 = "dec56f8cb529f1729316237e89f273407e2c178ac8c565aa7a547e223c4bcc9b"

        self.assertEqual(True, HotelCheckout.guest_checkout(valid_sha256))

    # Tests that a invalid dep date and a valid room key returns False
    @freeze_time("2024-04-08 00:00:00")
    def test_checkout_tc6(self):
        valid_sha256 = "dec56f8cb529f1729316237e89f273407e2c178ac8c565aa7a547e223c4bcc9b"

        with self.assertRaises(HotelManagementException):
            HotelCheckout.validate_departure_date(valid_sha256)

    # Tests that a valid dep date and a invalid room key returns False
    @freeze_time("2024-04-03 00:00:00")
    def test_checkout_tc7(self):
        valid_sha256 = "dec56f8cb529f1729316237e89l273407e2c178ac8c565aa7a547e223c4bcc9b"

        with self.assertRaises(HotelManagementException):
            HotelCheckout.guest_checkout(valid_sha256)

    # Tests that a invalid dep date and a invalid room key returns False
    @freeze_time("2024-04-02 00:00:00")
    def test_checkout_tc8(self):
        valid_sha256 = "dec56f8cb529f1729316237e89f273407e2c178ac8c565aa7a547e223c4bcc9b"

        with self.assertRaises(HotelManagementException):
            HotelCheckout.guest_checkout(valid_sha256)

    @freeze_time("2024-04-03 00:00:00")
    def test_checkout_tc9(self):
        """
            Test case to verify the functionality of the guest_checkout method.

            This test case simulates a checkout process for a guest with a valid room key. It then
            calls the guest_checkout method to verify it has correct functionality.
            :return: None
        """
        room_key = "dec56f8cb529f1729316237e89f273407e2c178ac8c565aa7a547e223c4bcc9b"

        # Call the guest_checkout function
        result = HotelCheckout.guest_checkout(room_key)

        # Assert that the function returns True, indicating successful checkout
        self.assertTrue(result)

        cwd = os.getcwd()
        parent_dir = os.path.dirname(cwd)
        parent_dir = os.path.dirname(parent_dir)
        parent_dir = os.path.dirname(parent_dir)

        filename = os.path.join(parent_dir, "src", "main", "python","uc3m_travel","data","check"
                                                                                         "-outs"
                                                                                         ".json")


        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.assertTrue(any(entry["room_key"] == room_key for entry in data))

    # Test case for handling file not found error during room key validation
    def test_checkout_tc10(self):
        with mock.patch("builtins.open", side_effect=FileNotFoundError):
            with self.assertRaises(HotelManagementException) as context:
                HotelCheckout.validate_room_key("valid_sha256")

            self.assertEqual("Hotel stay data file not found.", str(context.exception))

        # Test case for handling file not found error during departure date validation

    def test_checkout_tc11(self):
        with mock.patch("builtins.open", side_effect=FileNotFoundError):
            with self.assertRaises(HotelManagementException) as context:
                HotelCheckout.validate_departure_date("valid_sha256")

            self.assertEqual("Hotel stay data file not found.", str(context.exception))

    def test_checkout_tc12(self):
        with mock.patch("builtins.open", side_effect=FileNotFoundError):
            with self.assertRaises(HotelManagementException) as context:
                HotelCheckout.guest_checkout("valid_sha256")

            self.assertEqual("Checkout data file not found.", str(context.exception))


if __name__ == '__main__':
    unittest.main()
