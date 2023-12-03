"""
Please write your name
@author:

"""

# Reminder: You are only allowed to import the csv module (done it for you).
# OTHER MODULES ARE NOT ALLOWED (NO OTHER IMPORT!!!).

import csv


class Diabetes:
    def __init__(self, filepath) -> None:
        # delete pass and this line to write your code
        pass

    def get_dimension(self) -> list:
        # delete pass and this line to write your code
        pass

    def web_summary(self, filepath: str) -> None:
        # delete pass and this line to write your code
        pass

    def count_instances(self, criteria) -> int:
        # delete pass and this line to write your code
        # you can change the parameter criteria or the number of parameters
        # as you want, provided they are explained in doctring for this
        # method
        pass


if __name__ == "__main__":
    # You can comment the following when you are testing your code
    # You can add more tests as you want

    # test diabetes_data.csv
    d1 = Diabetes("diabetes_data.csv")
    print(d1.get_dimension())
    d1.web_summary('stat01.html')
    # d1.count_instances() # change according to your criteria
    print()

    # test diabetes2_data.csv
    d2 = Diabetes("diabetes2_data.csv")
    print(d2.get_dimension())
    d2.web_summary('stat02.html')
    # d2.count_instances()  # change according to your criteria
