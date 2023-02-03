import csv
import sys
from datetime import datetime
from collections import defaultdict

def spend_points(amount, transactions):
    # added assert to be safe
    assert amount >= 0

    payers = defaultdict(int)
    sorted_transactions = sorted(transactions, key=lambda x: x[2])
    transact = True
    for payer, points, timestamp in sorted_transactions:

        # add points to the payer
        payers[payer] += points


        if transact:
            if payers[payer] >= amount:
                # if the payer has enough points, we can spend them
                payers[payer] -= amount
                amount = 0
            elif payers[payer] >= 0:
                # if the payer has positive points less than amount, we can spend them
                amount = max(amount - payers[payer], 0)
                payers[payer] = 0
            else:
                # if the payer has negative points, we can't spend any more points
                amount -= points
                payers[payer] = 0

        # if we have spent all the points, we can stop
        if amount == 0 and all_positive(payers):
            transact = False

    return dict(payers)

def all_positive(payers):
    for payer in payers:
        if payers[payer] < 0:
            return False
    return True

if __name__ == "__main__":
    # verify that the user provided an amount
    if len(sys.argv) != 2:
        print("Usage: python main.py [amount]")
        exit(1)

    # verify the user provided a valid/positive amount
    try:
        amount = int(sys.argv[1])
        if amount < 0:
            raise ValueError
    except ValueError:
        print("Invalid amount")
        exit(1)

    amount = int(sys.argv[1])
    transactions = []
    # process the csv file
    with open("transactions.csv", "r") as file:
        reader = csv.reader(file)
        next(reader) # skip the header row
        for row in reader:
            payer, points, timestamp = row
            transactions.append((payer, int(points), datetime.fromisoformat(timestamp)))

    result = spend_points(amount, transactions)
    print(result)
