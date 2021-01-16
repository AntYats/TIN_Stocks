import csv

def init():
    # Array to put raw data from file
    data_preparation_arr = []
    # Array with data preparation
    final_data = []
    # Read file and put data to array
    with open("new.csv", newline='') as file:
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

    # Default values
    max_profit = -10 ** 10
    min_price = {
        "Date": final_data[0]["Date"],
        "Time": final_data[0]["Time"],
        "Price": final_data[0]["Price"]
    }

    # Variables to print transaction info
    day_of_sell = {
        "Date": None,
        "Time": None,
        "Price": None
    }

    day_of_buy = {
        "Date": None,
        "Time": None,
        "Price": None
    }

    for i in range(1, len(final_data)):
        curr_day = final_data[i]

        if curr_day["Price"] - min_price["Price"] > max_profit:
            max_profit = curr_day["Price"] - min_price["Price"]
            day_of_sell = curr_day
            day_of_buy = min_price

        if curr_day["Price"] < min_price["Price"]:
            min_price = curr_day

    print_transaction(day_of_buy, day_of_sell)


def print_transaction(arr_min, arr_max):
    print(f"Дата покупки: {format_date(arr_min['Date'])} || Стоимость акций: {arr_min['Price']}")
    print(f"Дата продажи: {format_date(arr_max['Date'])} || Стоимость акций: {arr_max['Price']}")
    print(f"Стоимость акций увеличилась на {arr_max['Price'] - arr_min['Price']}$")

def format_date(time):
    time = str(time)
    date = time[6:]
    month = time[4:6]
    year = time[0:4]
    return date + "-" + month + "-" + year


if __name__ == "__main__":
    init()
