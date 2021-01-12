import csv

"""
LEVEL ONE

General idea:
[1] Find lowest price at all time -> Save all data of this date (lowest_price)
[2] Find highest price at all time -> Save all data of this date (highest_price)
[3] In range of days of lowest_price to highest_price print 📈 or 📉 of price for each day

---- 
Founded dates don't break time rules, 
so there is no need to check if day to buy is after day of sold 
----
"""


def init():
    # Array to put raw data from file
    data_preparation_arr = []
    # Array with data preparation
    final_data = []
    # Read file and put data to array
    with open('data.csv', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            data_preparation_arr.append(row)
    # Delete name of columns
    del data_preparation_arr[0]
    # Prepare data
    for day in data_preparation_arr:
        final_data.append({
            "Date": int(day[1]),
            "Time": int(day[2]),
            "Price": float(day[3]),
        })

    # Constants
    MIN_DEFAULT_PRICE = 100000000
    MAX_DEFAULT_PRICE = -1

    min_price = {
        "Date": None,
        "Time": None,
        "Price": MIN_DEFAULT_PRICE,
    }

    max_price = {
        "Date": None,
        "Time": None,
        "Price": MAX_DEFAULT_PRICE,
    }

    for day in final_data:
        # Find minimum price to buy
        if day["Price"] < min_price["Price"]:
            min_price = day
        # Find maximum price to sold
        if day["Price"] > max_price["Price"]:
            max_price = day

    print(f"Дата покупки: {format_date(min_price['Date'])} || Стоимость акций: {min_price['Price']}")
    print(f"Дата продажи: {format_date(max_price['Date'])} || Стоимость акций: {max_price['Price']}")
    print(f"Стоимость акций увеличилась на {max_price['Price'] - min_price['Price']}$")


def format_date(time):
    time = str(time)
    date = time[6:]
    month = time[4:6]
    year = time[0:4]
    return date + "-" + month + "-" + year


if __name__ == "__main__":
    init()
