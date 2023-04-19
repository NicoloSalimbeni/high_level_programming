"""exercise 5 week 4"""
# Load the file "user_data.json", filter the data by the
# "CreditCardType" field equals to "American Express".
# Than save the data a to CSV."

import csv
import json

data = json.load(open("user_data.json"))

fields = [
    'ID', 'JobTitle', 'EmailAddress', 'FirstNameLastName', 'CreditCard',
    "CreditCardType"
]
file_name = "credic_card_users_filtered.csv"

# open a csv to write
with open(file_name, 'w') as csv_out:
    csv_writer = csv.writer(csv_out)
    csv_writer.writerow(fields)
    for user in data:  # loop over users
        if user["CreditCardType"] == "American Express":
            row = [
                str(user["ID"]),
                str(user["JobTitle"]),
                str(user["EmailAddress"]),
                str(user["FirstNameLastName"]),
                str(user["CreditCard"]),
                str(user["CreditCardType"])
            ]
            csv_writer.writerow(row)
