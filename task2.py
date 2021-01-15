import csv

"""
LEVEL TWO

General idea:
[1] Find lowest price at all time -> Save all data of this date (lowest_price)
[2] Find highest price at all time -> Save all data of this date (highest_price)
[3] In range of days of lowest_price to highest_price print 📈 or 📉 of price for each day
[4] Do steps [1] -> [2] -> [3] but begin searching from day of the sell
---- 

----
"""


def init():
    # Array to put raw data from file
    data_preparation_arr = []
    # Array with data preparation
    final_data = []
    # Read file and put data to array
    with open('new.csv', newline='') as file:
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

    print_transaction(min_price, max_price)


    idx_of_sold_day = final_data.index(max_price)

    min_price_2 = {
        "Date": None,
        "Time": None,
        "Price": MIN_DEFAULT_PRICE,
    }

    max_price_2 = {
        "Date": None,
        "Time": None,
        "Price": MAX_DEFAULT_PRICE,
    }
    
    # Find min and max price from previous sold day
    for day in range(idx_of_sold_day, len(final_data)):
        if final_data[day]["Price"] < min_price_2["Price"]:
            min_price_2 = final_data[day]

    idx_of_min = final_data.index(min_price_2)

    for day in range(idx_of_min, len(final_data)):
        if final_data[day]["Price"] > max_price_2["Price"]:
            max_price_2 = final_data[day]

    print_transaction(min_price_2, max_price_2)


def format_date(time):
    time = str(time)
    date = time[6:]
    month = time[4:6]
    year = time[0:4]
    return date + "-" + month + "-" + year


def print_transaction(arr_min, arr_max):
    print(f"Дата покупки: {format_date(arr_min['Date'])} || Стоимость акций: {arr_min['Price']}")
    print(f"Дата продажи: {format_date(arr_max['Date'])} || Стоимость акций: {arr_max['Price']}")
    print(f"Стоимость акций увеличилась на {arr_max['Price'] - arr_min['Price']}$")


if __name__ == "__main__":
    init()
