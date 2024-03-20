"""Main."""

from uc3m_travel import HotelManager


def main():
    """Main program."""
    mng = HotelManager()
    res = mng.read_data_from_json("test.json")
    str_res = str(res)
    print(str_res)
    print("CreditCard: " + res.credit_card)
    print(res.localizer)
    print("Past One\n")
    res = mng.read_data_from_json("test2.json")
    str_res = str(res)
    print(str_res)
    print("CreditCard: " + res.credit_card)
    print(res.localizer)
    print("Past Two\n")

if __name__ == "__main__":
    main()
