import unittest
import requests
from datetime import datetime, timedelta


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # API URL
        url = "https://showcase.api.linx.twenty57.net/UnixTime/fromunixtimestamp?unixtimestamp=1549892280"
        # get response from URL
        response = requests.get(url)

        print(response.text)

        # error message if test case got failed
        message = "URL response and calculated value are not equal !"
        baseValue = datetime(1970, 1, 1, 0, 0, 0)  # Base value to calculate epoch time i.e. 01/Jan/1970 00:00:00
        CalValue = baseValue + timedelta(seconds=1549892280)  # Add elapsed second in base value, as mentioned in URL
        finalValue = '{"Datetime":"' + str(CalValue) + '"}'
        # print(baseValue)
        # print(CalValue)

        # assertEqual() to check equality of url response & calculated value value
        self.assertEqual(response.text, finalValue, message)




if __name__ == '__main__':
    unittest.main()
