"""Tests for making reservations."""
import json
import os
from unittest import TestCase
from uc3m_travel.hotel_manager import roomReservation
from uc3m_travel.hotel_management_exception import HotelManagementException


class TestRequestReservation(TestCase):
    """test class for func 1"""

    def setUp(self):
        empty_data = []
        current_dir = os.getcwd()
        parent_dir = os.path.dirname(current_dir)
        parent_dir = os.path.dirname(parent_dir)
        adjacent_dir = os.path.join(parent_dir, 'data')
        file_name = 'hotel_reservations.json'
        file_path = os.path.join(adjacent_dir, file_name)
        with open(file_path, 'w', encoding="utf-8") as f:
            json.dump(empty_data, f, indent=4)

    def test_request_tc1(self):
        self.assertEqual('23418945094a3b622ac43085569f2b33',
                         roomReservation(5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                         "01/07/2024", 2))

    def test_request_tc2(self):
        self.assertRaisesRegex(HotelManagementException, "bad credit card number",
                               roomReservation, 5555555555554442, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                               "01/07/2024", 2)

    def test_request_tc3(self):
        self.assertRaisesRegex(HotelManagementException, "bad credit card number",
                               roomReservation, "555555555555444a", "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                               "01/07/2024", 2)

    def test_request_tc4(self):
        self.assertRaisesRegex(HotelManagementException, "bad credit card number",
                               roomReservation, 55555555555544440, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                               "01/07/2024", 2)

    def test_request_tc5(self):
        self.assertRaisesRegex(HotelManagementException, "bad credit card number",
                               roomReservation, 555555555555444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                               "01/07/2024", 2)

    def test_request_tc6(self):
        self.assertEqual('23418945094a3b622ac43085569f2b33',
                         roomReservation(5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                         "01/07/2024", 2))

    def test_request_tc7(self):
        self.assertRaisesRegex(HotelManagementException, "bad id card",
                               roomReservation, 5555555555554444, "12341234H", "JOSE LOPEZ", 911234567, "SINGLE",
                               "01/07/2024", 2)

    def test_request_tc8(self):
        self.assertRaisesRegex(HotelManagementException, "bad id card",
                               roomReservation, 5555555555554444, "123412345Z", "JOSE LOPEZ", 911234567, "SINGLE",
                               "01/07/2024", 2)

    def test_request_tc9(self):
        self.assertRaisesRegex(HotelManagementException, "bad id card",
                               roomReservation, 5555555555554444, 0, "JOSE LOPEZ", 911234567, "SINGLE", "01/07/2024",
                               2)

    def test_request_tc10(self):
        self.assertEqual('23418945094a3b622ac43085569f2b33',
                         roomReservation(5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                         "01/07/2024", 2))

    def test_request_tc11(self):
        self.assertRaisesRegex(HotelManagementException, "bad name surname",
                               roomReservation, 5555555555554444, "12345678Z", 12, 911234567, "SINGLE", "01/07/2024",
                               2)

    def test_request_tc12(self):
        self.assertRaisesRegex(HotelManagementException, "bad name surname", roomReservation, 5555555555554444,
                               "12345678Z",
                               "ABCDEFGHIJKLMNOPQRSTUVWXY ABCDEFGHIJKLMNOPQRSTUVWXY",
                               911234567, "SINGLE", "01/07/2024", 2)

    def test_request_tc13(self):
        self.assertRaisesRegex(HotelManagementException, "bad name surname",
                               roomReservation, 5555555555554444, "12345678Z", "JAY SMITH", 911234567, "SINGLE",
                               "01/07/2024", 2)

    def test_request_tc14(self):
        self.assertEqual('23418945094a3b622ac43085569f2b33',
                         roomReservation(5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                         "01/07/2024", 2))

    def test_request_tc15(self):
        self.assertRaisesRegex(HotelManagementException, "bad phone number",
                               roomReservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", "ABC", "SINGLE",
                               "01/07/2024",
                               2)

    def test_request_tc16(self):
        self.assertRaisesRegex(HotelManagementException, "bad phone number",
                               roomReservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 1234567890, "SINGLE",
                               "01/07/2024", 2)

    def test_request_tc17(self):
        self.assertRaisesRegex(HotelManagementException, "bad phone number",
                               roomReservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 12345678, "SINGLE",
                               "01/07/2024", 2)

    def test_request_tc18(self):
        self.assertEqual('23418945094a3b622ac43085569f2b33',
                         roomReservation(5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                         "01/07/2024", 2))

    def test_request_tc19(self):
        self.assertEqual('1398049719a529627c18ef6c85b07dd4',
                         roomReservation(5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "DOUBLE",
                                         "01/07/2024", 2))

    def test_request_tc20(self):
        self.assertEqual('bae9ccdc1b158115f1246b8fe3332cd7',
                         roomReservation(5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "TRIPLE",
                                         "01/07/2024", 2))

    def test_request_tc21(self):
        self.assertRaisesRegex(HotelManagementException, "bad room type",
                               roomReservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "AGBAGB",
                               "01/07/2024", 2)

    def test_request_tc22(self):
        self.assertRaisesRegex(HotelManagementException, "bad room type",
                               roomReservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, 123,
                               "01/07/2024",
                               2)

    def test_request_tc23(self):
        self.assertEqual('23418945094a3b622ac43085569f2b33',
                         roomReservation(5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                         "01/07/2024", 2))

    def test_request_tc24(self):
        self.assertRaisesRegex(HotelManagementException, "bad arrival",
                               roomReservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                               "120624", 2)

    def test_request_tc25(self):
        self.assertRaisesRegex(HotelManagementException, "bad arrival",
                               roomReservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                               61424,
                               2)

    def test_request_tc26(self):
        self.assertRaisesRegex(HotelManagementException, "bad arrival",
                               roomReservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                               "00/14/2000", 2)

    def test_request_tc27(self):
        self.assertRaisesRegex(HotelManagementException, "bad arrival",
                               roomReservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                               "01/13/2000", 2)

    def test_request_tc28(self):
        self.assertRaisesRegex(HotelManagementException, "bad arrival",
                               roomReservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                               "001/01/2000", 2)

    def test_request_tc29(self):
        self.assertRaisesRegex(HotelManagementException, "bad arrival",
                               roomReservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                               "01/001/2000", 2)

    def test_request_tc30(self):
        self.assertRaisesRegex(HotelManagementException, "bad arrival",
                               roomReservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                               "01/01/20000", 2)

    def test_request_tc31(self):
        self.assertEqual('8c1ca44f6d7f6a21e142a86def72da31',
                         roomReservation(5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                         "01/07/2024", 5))

    def test_request_tc32(self):
        self.assertRaisesRegex(HotelManagementException, "bad num days",
                               roomReservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                               "01/07/2024", "f")

    def test_request_tc33(self):
        self.assertRaisesRegex(HotelManagementException, "bad num days",
                               roomReservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                               "01/07/2024", 0)

    def test_request_tc34(self):
        self.assertRaisesRegex(HotelManagementException, "bad num days",
                               roomReservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                               "01/07/2024", 11)

    def test_request_tc35(self):
        self.assertRaisesRegex(HotelManagementException, "bad name surname",
                               roomReservation, 5555555555554444, "12345678Z", "JOSELOPEZ", 911234567, "SINGLE",
                               "01/07/2024", 2)

    def test_request_tc36(self):  # cant double book test
        roomReservation(5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                        "01/07/2024", 2)
        self.assertRaisesRegex(HotelManagementException, "There is already a reservation for this customer",
                               roomReservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                               "01/07/2024", 2)
