"""Module: hotel_management_exception.py"""


class HotelManagementException(Exception):
    """Custom exception class for hotel management errors."""
    def __init__(self, message):
        """Initialize with the given error message."""
        self.__message = message
        super().__init__(self.message)

    @property
    def message(self):
        """Get the error message."""
        return self.__message

    @message.setter
    def message(self, value):
        """Set the error message."""
        self.__message = value
