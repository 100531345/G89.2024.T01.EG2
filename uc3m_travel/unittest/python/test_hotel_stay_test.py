from uc3m_travel import room_reservation
from freezegun import freeze_time
from uc3m_travel import guest_arrival
from uc3m_travel import HotelManagementException
from unittest import TestCase
import re
import json
import tempfile
import os


class TestRequestReservation(TestCase):
    def test_request_TC1(self):
        self.assertEqual(True, room_reservation(5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                                "01/07/2024", 2))

    def test_request_TC2(self):
        self.assertRaisesRegexp(HotelManagementException, "bad credit card number",
                                room_reservation, 5555555555554442, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                "01/07/2024", 2)

    def test_request_TC3(self):
        self.assertRaisesRegexp(HotelManagementException, "bad credit card number",
                                room_reservation, "555555555555444a", "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                "01/07/2024", 2)

    def test_request_TC4(self):
        self.assertRaisesRegexp(HotelManagementException, "bad credit card number",
                                room_reservation, 55555555555544440, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                "01/07/2024", 2)

    def test_request_TC5(self):
        self.assertRaisesRegexp(HotelManagementException, "bad credit card number",
                                room_reservation, 555555555555444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                "01/07/2024", 2)

    def test_request_TC6(self):
        self.assertEqual(True, room_reservation(5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                                "01/07/2024", 2))

    def test_request_TC7(self):
        self.assertRaisesRegexp(HotelManagementException, "bad id card",
                                room_reservation, 5555555555554444, "12341234H", "JOSE LOPEZ", 911234567, "SINGLE",
                                "01/07/2024", 2)

    def test_request_TC8(self):
        self.assertRaisesRegexp(HotelManagementException, "bad id card",
                                room_reservation, 5555555555554444, "123412345Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                "01/07/2024", 2)

    def test_request_TC9(self):
        self.assertRaisesRegexp(HotelManagementException, "bad id card",
                                room_reservation, 5555555555554444, 0, "JOSE LOPEZ", 911234567, "SINGLE", "01/07/2024",
                                2)

    def test_request_TC10(self):
        self.assertEqual(True, room_reservation(5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                                "6/14/24", 2))

    def test_request_TC11(self):
        self.assertRaisesRegexp(HotelManagementException, "bad name surname",
                                room_reservation, 5555555555554444, "12345678Z", 12, 911234567, "SINGLE", "01/07/2024",
                                2)

    def test_request_TC12(self):
        self.assertRaisesRegexp(HotelManagementException, "bad name surname", room_reservation, 5555555555554444,
                                "12345678Z",
                                "ABCDEFGHIJKLMNOPQRSTUVWXY ABCDEFGHIJKLMNOPQRSTUVWXY",
                                911234567, "SINGLE", "01/07/2024", 2)

    def test_request_TC13(self):
        self.assertRaisesRegexp(HotelManagementException, "bad name surname",
                                room_reservation, 5555555555554444, "12345678Z", "JAY SMITH", 911234567, "SINGLE",
                                "01/07/2024", 2)

    def test_request_TC14(self):
        self.assertEqual(HotelManagementException,
                         room_reservation(5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                          "6/14/24", 2))

    def test_request_TC15(self):
        self.assertRaisesRegexp(HotelManagementException, "bad phone number",
                                room_reservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", "ABC", "SINGLE",
                                "01/07/2024",
                                2)

    def test_request_TC16(self):
        self.assertRaisesRegexp(HotelManagementException, "bad phone number",
                                room_reservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 1234567890, "SINGLE",
                                "01/07/2024", 2)

    def test_request_TC17(self):
        self.assertRaisesRegexp(HotelManagementException, "bad phone number",
                                room_reservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 12345678, "SINGLE",
                                "01/07/2024", 2)

    def test_request_TC18(self):
        self.assertEqual(True, room_reservation(5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                                "6/14/24", 2))

    def test_request_TC19(self):
        self.assertEqual(True, room_reservation(5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "DOUBLE",
                                                "6/14/24", 2))

    def test_request_TC20(self):
        self.assertEqual(True, room_reservation(5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "TRIPLE",
                                                "6/14/24", 2))

    def test_request_TC21(self):
        self.assertRaisesRegexp(HotelManagementException, "bad room type",
                                room_reservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "AGBAGB",
                                "01/07/2024", 2)

    def test_request_TC22(self):
        self.assertRaisesRegexp(HotelManagementException, "bad room type",
                                room_reservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, 123,
                                "01/07/2024",
                                2)

    def test_request_TC23(self):
        self.assertEqual(True, room_reservation(5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                                "6/14/24", 2))

    def test_request_TC24(self):
        self.assertRaisesRegexp(HotelManagementException, "bad arrival",
                                room_reservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                "120624", 2)

    def test_request_TC25(self):
        self.assertRaisesRegexp(HotelManagementException, "bad arrival",
                                room_reservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                61424,
                                2)

    def test_request_TC26(self):
        self.assertRaisesRegexp(HotelManagementException, "bad arrival",
                                room_reservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                "00/14/2000", 2)

    def test_request_TC27(self):
        self.assertRaisesRegexp(HotelManagementException, "bad arrival",
                                room_reservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                "01/13/2000", 2)

    def test_request_TC28(self):
        self.assertRaisesRegexp(HotelManagementException, "bad arrival",
                                room_reservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                "001/01/2000", 2)

    def test_request_TC29(self):
        self.assertRaisesRegexp(HotelManagementException, "bad arrival",
                                room_reservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                "01/001/2000", 2)

    def test_request_TC30(self):
        self.assertRaisesRegexp(HotelManagementException, "bad arrival",
                                room_reservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                "01/01/20000", 2)

    def test_request_TC31(self):
        self.assertEqual(True, room_reservation(5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                                "6/14/24", 5))

    def test_request_TC32(self):
        self.assertRaisesRegexp(HotelManagementException, "bad num days",
                                room_reservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                "01/07/2024", "f")

    def test_request_TC33(self):
        self.assertRaisesRegexp(HotelManagementException, "bad num days",
                                room_reservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                "01/07/2024", 0)

    def test_request_TC34(self):
        self.assertRaisesRegexp(HotelManagementException, "bad num days",
                                room_reservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                "01/07/2024", 11)


class TestStayHotel(TestCase):

    @freeze_time("2024-4-01")
    def test_stay_1(self):
        valid_json = '{"Localizer": "5eb63bbbe01eeed093cb22bb8f5acdc3", "IdCard": "12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(valid_json)

        result = guest_arrival(temp_file.name)
        self.assertEqual(
            "0da54330cafe260e91643305780e4a60483a93263bb18ec5262119ed152f86ce",
            result)
        os.unlink(temp_file.name)

    def test_stay_2(self):
        invalid_json = '"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException) as message:
            guest_arrival(temp_file.name)

        expected_error_message = "The file is not in JSON format."
        self.assertEqual(str(message.exception), expected_error_message)

        os.unlink(temp_file.name)

    def test_stay_3(self):
        invalid_json = '{"Localizer": "AHDE3EDDGDS", "IdCard": "12345678Z"'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_4(self):
        invalid_json = '["Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_5(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_6(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_7(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"]'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_8(self):
        invalid_json = '{}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException) as message:
            guest_arrival(temp_file.name)

        expected_error_message = "The JSON data does not have valid values."
        self.assertEqual(str(message.exception), expected_error_message)

        os.unlink(temp_file.name)

    def test_stay_9(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z" "Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_10(self):
        invalid_json = '{,"IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_11(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3" "Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_12(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3""IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_13(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3",,"IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_14(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3"."IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_15(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3",}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_16(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z" "IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_17(self):
        invalid_json = '{:"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_18(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3" "Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_19(self):
        invalid_json = '{"Localizer""5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_20(self):
        invalid_json = '{"Localizer"::"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_21(self):
        invalid_json = '{"Localizer";"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_22(self):
        invalid_json = '{"Localizer":,"IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_23(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3""5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_24(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3""IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_25(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3",,"IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_26(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3"."IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_27(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3",:"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_28(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard""IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_29(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard""12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_30(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard"::"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_31(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard";"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_32(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_33(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z""12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_34(self):
        invalid_json = '{Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_35(self):
        invalid_json = '{""Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_36(self):
        invalid_json = '{:Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_37(self):
        invalid_json = '{"":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_38(self):
        invalid_json = '{"LocalizerLocalizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_39(self):
        invalid_json = '{"Farizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_40(self):
        invalid_json = '{"Localizer:"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_41(self):
        invalid_json = '{"Localizer"":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_42(self):
        invalid_json = '{"Localizer::"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_43(self):
        invalid_json = '{"Localizer":5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_44(self):
        invalid_json = '{"Localizer":""5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_45(self):
        invalid_json = '{"Localizer"::5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_46(self):
        invalid_json = '{"Localizer":"","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_47(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc35eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_48(self):
        invalid_json = '{"Localizer":"TEST","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException) as message:
            guest_arrival(temp_file.name)

        expected_error_message = "The locator does not correspond to the stored data"
        self.assertEqual(expected_error_message, str(message.exception))

        os.unlink(temp_file.name)

    def test_stay_49(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3,"IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_50(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3"","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_51(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3:,"IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_52(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3",IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_53(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3",""IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_54(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3",:IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_55(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_56(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCardIdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_57(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","HotelRoom":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_58(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard:"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_59(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard"":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_60(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard::"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_61(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_62(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":""12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_63(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard"::12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_64(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":""}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_65(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_66(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"14"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_67(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_68(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z""}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_69(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z:}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_70(self):
        invalid_json = '{"Localizer":"4eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_71(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc33","IdCard":12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_72(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc","IdCard":""12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_73(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard"::12341234H"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_74(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"123412345H"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    def test_stay_75(self):
        invalid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"0"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(invalid_json)

        # Test if the function raises the expected exception
        with self.assertRaises(HotelManagementException):
            guest_arrival(temp_file.name)

        os.unlink(temp_file.name)

    @freeze_time("2023-4-01")
    def test_stay_76(self):
        valid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(valid_json)

        with self.assertRaises(HotelManagementException) as message:
            guest_arrival(temp_file.name)

        expected_error_message = "The arrival date does not correspond to the reservation date."
        self.assertEqual(expected_error_message, str(message.exception))
        os.unlink(temp_file.name)

    @freeze_time("2025-4-01")
    def test_stay_77(self):
        valid_json = '{"Localizer":"5eb63bbbe01eeed093cb22bb8f5acdc3","IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(valid_json)

        with self.assertRaises(HotelManagementException) as message:
            guest_arrival(temp_file.name)

        expected_error_message = "The arrival date does not correspond to the reservation date."
        self.assertEqual(expected_error_message, str(message.exception))
        os.unlink(temp_file.name)


class TestRequestReservation(TestCase):
    def test_func_one_and_two(self):
        localizer = room_reservation(5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                         "01/07/2024", 2)

        valid_json = '{"Localizer": ' + localizer + ',"IdCard":"12345678Z"}'

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(valid_json)

        result = guest_arrival(temp_file.name)
        self.assertEqual(
            "0da54330cafe260e91643305780e4a60483a93263bb18ec5262119ed152f86ce",
            result)
        os.unlink(temp_file.name)
