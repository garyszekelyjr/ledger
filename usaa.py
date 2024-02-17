import csv

from datetime import datetime
from decimal import Decimal

transactions = []

with open("data/bk_download.csv") as file:
    for transaction in csv.DictReader(file):
        if transaction['Status'] == 'Posted':
            transactions.append({
                'date': datetime.strptime(transaction['Date'], '%Y-%m-%d'),
                'category': transaction['Category'],
                'description': transaction['Description'],
                'amount': Decimal(transaction['Amount'])
            })

transactions = sorted(transactions, key=lambda e: (e['date'], e['category'], e['description'], e['amount']))