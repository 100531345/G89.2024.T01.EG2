"""
Module Test: test_hotel_stay.py
"""
from unittest import TestCase
import json
import tempfile
import os
from freezegun import freeze_time
from src.main.python.uc3m_travel.hotel_manager import roomReservation
from src.main.python.uc3m_travel.hotel_stay import guestArrival
from src.main.python.uc3m_travel.hotel_management_exception import HotelManagementException

from src.main.python.uc3m_travel.hotel_checkout import HotelCheckout


class TestStayHotel(TestCase):
    """Class for hotel_stay tests"""

    def setUp(self):
        full_data = [{
        "id_card": "12345678Z",
        "name_surname": "JOSE LOPEZ",
        "credit_card": 5555555555554444,
        "phone_number:": 911234567,
        "arrival_date": "01/04/2024",
        "num_days": 2,
        "room_type": "SINGLE",
        "Localizer": "e3778b02fa0ada33f9202203acb054d5"
    }]
        current_dir = os.getcwd()
        parent_dir = os.path.dirname(current_dir)
        parent_dir = os.path.dirname(parent_dir)
        adjacent_dir = os.path.join(parent_dir, 'main', 'python', 'uc3m_travel', 'data')
        file_name = 'hotel_reservations.json'
        file_path = os.path.join(adjacent_dir, file_name)
        with open(file_path, 'w', encoding="utf-8") as f:
            json.dump(full_data, f, indent=4)

    @freeze_time("2024-4-01")
    def test_stay_1(self):
        "Test for hotel_stay file"
        valid_json = '{"Localizer": "e3778b02fa0ada33f9202203acb054d5", "IdCard": "12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(valid_json)

        result = guestArrival(temp_file.name)
        self.assertEqual(
            "dec56f8cb529f1729316237e89f273407e2c178ac8c565aa7a547e223c4bcc9b",
            result)
        os.unlink(temp_file.name)

    def test_stay_2(self):
        "Test for hotel_stay file"
        invalid_json = '"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException) as message:
            guestArrival(temp_file.name)

        expected_error_message = "The file is not in JSON format."
        self.assertEqual(str(message.exception), expected_error_message)

        os.unlink(temp_file.name)

    def test_stay_3(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer": "AHDE3EDDGDS", "IdCard": "12345678Z"'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_4(self):
        "Test for hotel_stay file"
        invalid_json = '["Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_5(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_6(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_7(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"]'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_8(self):
        "Test for hotel_stay file"
        invalid_json = '{}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException) as message:
            guestArrival(temp_file.name)

        expected_error_message = "The JSON data does not have valid values."
        self.assertEqual(str(message.exception), expected_error_message)

        os.unlink(temp_file.name)

    def test_stay_9(self):
        "Test for hotel_stay file"
        invalid_json = ('{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z" '
                        '"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}')

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_10(self):
        "Test for hotel_stay file"
        invalid_json = '{,"IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_11(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3" "Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_12(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3""IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_13(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3",,"IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_14(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3"."IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_15(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3",}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_16(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z" "IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_17(self):
        "Test for hotel_stay file"
        invalid_json = '{:"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_18(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3" "Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_19(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer""5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_20(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer"::"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_21(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer";"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_22(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":,"IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_23(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3""5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_24(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3""IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_25(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3",,"IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_26(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3"."IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_27(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3",:"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_28(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard""IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_29(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard""12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_30(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard"::"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_31(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard";"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_32(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_33(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z""12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_34(self):
        "Test for hotel_stay file"
        invalid_json = '{Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_35(self):
        "Test for hotel_stay file"
        invalid_json = '{""Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_36(self):
        "Test for hotel_stay file"
        invalid_json = '{:Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_37(self):
        "Test for hotel_stay file"
        invalid_json = '{"":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_38(self):
        "Test for hotel_stay file"
        invalid_json = '{"LocalizerLocalizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_39(self):
        "Test for hotel_stay file"
        invalid_json = '{"Farizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_40(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer:"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_41(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer"":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_42(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer::"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_43(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_44(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":""5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_45(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer"::5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_46(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_47(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc35eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_48(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"TEST","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException) as message:
            guestArrival(temp_file.name)

        expected_error_message = "The locator does not correspond to the stored data"
        self.assertEqual(expected_error_message, str(message.exception))

        os.unlink(temp_file.name)

    def test_stay_49(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3,"IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_50(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3"","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_51(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3:,"IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_52(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3",IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_53(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3",""IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_54(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3",:IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_55(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_56(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCardIdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_57(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","HotelRoom":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_58(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard:"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_59(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard"":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_60(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard::"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_61(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_62(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":""12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_63(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard"::12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_64(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":""}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_65(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_66(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"14"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)
        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_67(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_68(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z""}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_69(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z:}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_70(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"4eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_71(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc33","IdCard":12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_72(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc","IdCard":""12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_73(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard"::12341234H"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_74(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"123412345H"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_75(self):
        "Test for hotel_stay file"
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"0"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guestArrival(temp_file.name)

        os.unlink(temp_file.name)

    @freeze_time("2023-4-01")
    def test_stay_76(self):
        "Test for hotel_stay file"
        valid_json = '{"Localizer":"e3778b02fa0ada33f9202203acb054d5","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(valid_json)

        with self.assertRaises(HotelManagementException) as message:
            guestArrival(temp_file.name)

        expected_error_message = "The arrival date does not correspond to the reservation date."
        self.assertEqual(expected_error_message, str(message.exception))
        os.unlink(temp_file.name)

    @freeze_time("2025-4-01")
    def test_stay_77(self):
        "Test for hotel_stay file"
        valid_json = '{"Localizer":"e3778b02fa0ada33f9202203acb054d5","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(valid_json)

        with self.assertRaises(HotelManagementException) as message:
            guestArrival(temp_file.name)

        expected_error_message = "The arrival date does not correspond to the reservation date."
        self.assertEqual(expected_error_message, str(message.exception))
        os.unlink(temp_file.name)


class TestCombinations(TestCase):
    "Testing functions combined in one Test"

    def setUp(self):
        empty_data = []
        current_dir = os.getcwd()
        parent_dir = os.path.dirname(current_dir)
        parent_dir = os.path.dirname(parent_dir)
        adjacent_dir = os.path.join(parent_dir, 'main', 'python', 'uc3m_travel', 'data')
        file_name = 'hotel_reservations.json'
        file_path = os.path.join(adjacent_dir, file_name)
        with open(file_path, 'w', encoding="utf-8") as f:
            json.dump(empty_data, f, indent=4)

    @freeze_time("2024-4-01")
    def test_func_one_and_two_three(self):

        "Test for hotel_stay file"
        localizer = roomReservation(5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                         "01/04/2024", 2)

        valid_json = json.dumps({"Localizer": localizer, "IdCard": "12345678Z"})

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(valid_json)


        result = guestArrival(temp_file.name)

        self.assertEqual(
            "dec56f8cb529f1729316237e89f273407e2c178ac8c565aa7a547e223c4bcc9b",
            result)
        os.unlink(temp_file.name)

        with freeze_time("2024-04-03"):
            func3_res = HotelCheckout.guest_checkout(
                "dec56f8cb529f1729316237e89f273407e2c178ac8c565aa7a547e223c4bcc9b")

            self.assertEqual(True, func3_res)
