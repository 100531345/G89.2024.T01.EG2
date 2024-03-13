#THIS MAIN PROGRAM IS ONLY VALID FOR THE FIRST THREE WEEKS OF CLASS
#IN GUIDED EXERCISE 2.2, TESTING MUST BE PERFORMED USING UNITTESTS.

from UC3MTravel import HotelManager


def main():
    mng = HotelManager()
    res = mng.ReaddatafromJSOn("test.json")
    strRes = res.__str__()
    print(strRes)
    print("CreditCard: " + res.CREDITCARD)
    print(res.LOCALIZER)
    print("Past One\n")
    res = mng.ReaddatafromJSOn("test2.json")
    strRes = res.__str__()
    print(strRes)
    print("CreditCard: " + res.CREDITCARD)
    print(res.LOCALIZER)
    print("Past Two\n")

if __name__ == "__main__":
    main()
