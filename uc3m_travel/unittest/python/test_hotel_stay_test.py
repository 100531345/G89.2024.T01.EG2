from uc3m_travel import request_reservation, HotelManagementException
from unittest import TestCase

class TestRequestReservation(TestCase):

    def test_request_TC1(self):
        self.assertEqual(True, request_reservation(5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                                   "6/14/24", 2))

    def test_request_TC2(self):
        self.assertRaises(HotelManagementException,
                          request_reservation,5555555555554442, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                              "6/14/24", 2)

    def test_request_TC3(self):
        self.assertRaises(HotelManagementException,
                          request_reservation, "555555555555444a", "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                              "6/14/24", 2)

    def test_request_TC4(self):
        self.assertRaises(HotelManagementException,
                          request_reservation, 55555555555544440, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                              "6/14/24", 2)

    def test_request_TC5(self):
        self.assertRaises(HotelManagementException,
                          request_reservation, 555555555555444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                              "6/14/24", 2)

    def test_request_TC6(self):
        self.assertEqual(True, request_reservation(5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                                   "6/14/24", 2))

    def test_request_TC7(self):
        self.assertRaises(HotelManagementException,
                          request_reservation, 5555555555554444, "12341234H", "JOSE LOPEZ", 911234567, "SINGLE",
                                              "6/14/24", 2)

    def test_request_TC8(self):
        self.assertRaises(HotelManagementException,
                          request_reservation, 5555555555554444, "123412345Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                              "6/14/24", 2)

    def test_request_TC9(self):
        self.assertRaises(HotelManagementException,
                          request_reservation, 5555555555554444, 0, "JOSE LOPEZ", 911234567, "SINGLE", "6/14/24", 2)

    def test_request_TC10(self):
        self.assertEquals(True, request_reservation(5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                                    "6/14/24", 2))

    def test_request_TC11(self):
        self.assertRaises(HotelManagementException,
                          request_reservation, 5555555555554444, "12345678Z", 12, 911234567, "SINGLE", "6/14/24", 2)

    def test_request_TC12(self):
        self.assertRaises(HotelManagementException, request_reservation, 5555555555554444, "12345678Z",
                                                                          "ABCDEFGHIJKLMNOPQRSTUVWXY ABCDEFGHIJKLMNOPQRSTUVWXY",
                                                                          911234567, "SINGLE", "6/14/24", 2)

    def test_request_TC13(self):
        self.assertRaises(HotelManagementException,
                          request_reservation, 5555555555554444, "12345678Z", "JAY SMITH", 911234567, "SINGLE",
                                              "6/14/24", 2)

    def test_request_TC14(self):
        self.assertEquals(HotelManagementException,
                          request_reservation(5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                              "6/14/24", 2))

    def test_request_TC15(self):
        self.assertRaises(HotelManagementException,
                          request_reservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", "ABC", "SINGLE", "6/14/24",
                                              2)

    def test_request_TC16(self):
        self.assertRaises(HotelManagementException,
                          request_reservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 1234567890, "SINGLE",
                                              "6/14/24", 2)

    def test_request_TC17(self):
        self.assertRaises(HotelManagementException,
                          request_reservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 12345678, "SINGLE",
                                              "6/14/24", 2)

    def test_request_TC18(self):
        self.assertEquals(True, request_reservation(5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                                    "6/14/24", 2))

    def test_request_TC19(self):
        self.assertEquals(True, request_reservation(5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "DOUBLE",
                                                    "6/14/24", 2))

    def test_request_TC20(self):
        self.assertEquals(True, request_reservation(5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "TRIPLE",
                                                    "6/14/24", 2))

    def test_request_TC21(self):
        self.assertRaises(HotelManagementException,
                          request_reservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "AGBAGB",
                                              "6/14/24", 2)

    def test_request_TC22(self):
        self.assertRaises(HotelManagementException,
                          request_reservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, 123, "6/14/24",
                                              2)

    def test_request_TC23(self):
        self.assertEquals(True, request_reservation(5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                                    "6/14/24", 2))

    def test_request_TC24(self):
        self.assertRaises(HotelManagementException,
                          request_reservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                              "120624", 2)

    def test_request_TC25(self):
        self.assertRaises(HotelManagementException,
                          request_reservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE", 61424,
                                              2)

    def test_request_TC26(self):
        self.assertRaises(HotelManagementException,
                          request_reservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                              "00/14/2000", 2)

    def test_request_TC27(self):
        self.assertRaises(HotelManagementException,
                          request_reservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                              "01/13/2000", 2)

    def test_request_TC28(self):
        self.assertRaises(HotelManagementException,
                          request_reservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                              "001/01/2000", 2)

    def test_request_TC29(self):
        self.assertRaises(HotelManagementException,
                          request_reservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                              "01/001/2000", 2)

    def test_request_TC30(self):
        self.assertRaises(HotelManagementException,
                          request_reservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                              "01/01/20000", 2)

    def test_request_TC31(self):
        self.assertEquals(True, request_reservation(5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                                    "6/14/24", 5))

    def test_request_TC32(self):
        self.assertRaises(HotelManagementException,
                          request_reservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                              "6/14/24", "f")

    def test_request_TC33(self):
        self.assertRaises(HotelManagementException,
                          request_reservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                              "6/14/24", 0)

    def test_request_TC34(self):
        self.assertRaises(HotelManagementException,
                          request_reservation, 5555555555554444, "12345678Z", "JOSE LOPEZ", 911234567, "SINGLE",
                                              "6/14/24", 11)


class TestStayHotel(TestCase):

    def test_stay_1(self):
        return
