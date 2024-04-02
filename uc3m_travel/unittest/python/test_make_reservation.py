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
    def setUp(self):
        print("fjkdslapjfkle;ajfkld;sajkfldsa;j")
        empty_data = []
        current_dir = os.getcwd()
        parent_dir = os.path.dirname(current_dir)
        parent_dir = os.path.dirname(parent_dir)
        adjacent_dir = os.path.join(parent_dir, 'data')
        file_name = 'hotel_reservations.json'
        file_path = os.path.join(adjacent_dir, file_name)
        with open(file_path, 'w') as f:
            json.dump(empty_data, f, indent=4)
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

    def test_request_TC35(self):
        self.assertRaisesRegexp(HotelManagementException, "bad name surname",
                                room_reservation, 5555555555554444, "12345678Z", "JOSELOPEZ", 911234567, "SINGLE",
                                "01/07/2024", 2)
