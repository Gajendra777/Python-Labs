#!/usr/bin/env python3

import json
import locale
import sys
import os
import Report
import emails


src = os.path.abspath("D:\\Python3\\Python-Labs\\Projects\\GenerateAndSendEmail")

def load_data(filename):
    """Loads the contents of filename as a JSON file."""
    with open(os.path.join(src,filename)) as json_file:
        data = json.load(json_file)

    return data


def format_car(car):
    """Given a car dictionary, returns a nicely formatted name."""
    return "{} {} ({})".format(
    car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
    """Analyzes the data, looking for maximums.

    Returns a list of lines that summarize the information.
    """
    locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
    max_revenue = {"revenue": 0}
    max_sales = {"sales": 0,"car":{}}
    car_year = {}

    for item in data:
        # Calculate the revenue generated by this model (price * total_sales)
        # We need to convert the price from "$1234.56" to 1234.56
        item_price = locale.atof(item["price"].strip("$"))
        item_revenue = item["total_sales"] * item_price
        if item_revenue > max_revenue["revenue"]:
            item["revenue"] = item_revenue
            max_revenue = item
    
        # TODO: also handle max sales
        if item["total_sales"] > max_sales["sales"]:
            max_sales["sales"] = item["total_sales"]
            max_sales["car"] = item["car"]


        # TODO: also handle most popular car_year
        year = item["car"]["car_year"]
        if year in car_year.keys():
            car_year[year]= car_year[year] + item["total_sales"]
        else:
            car_year[year] = item["total_sales"]

    
    sorted_list = sorted(car_year.items(), key = lambda kv:(kv[1], kv[0]))
    year, max_sales_in_year = sorted_list[-1]

    summary = [
        "The {} generated the most revenue: ${}".format(
        format_car(max_revenue["car"]), max_revenue["revenue"]),
        "The {} had the most sales: {}".format(format_car(max_sales["car"]),max_sales["sales"]),
        "The most popular year was {} with {} sales.".format(year, max_sales_in_year)
    ]

    return summary

def cars_dict_to_table(car_data):
    """Turns the data in car_data into a list of lists."""
    table_data = [["ID", "Car", "Price", "Total Sales"]]
    for item in car_data:
        table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])

    return table_data

def main(argv):
    """Process the JSON data and generate a full report out of it."""
    data = load_data('car_sales.json')
    summary = process_data(data)
    print(summary)
    
    # TODO: turn this into a PDF report
    table_data= cars_dict_to_table(data)

    #Optional 1
    Sorted_Table_Data = sorted(table_data[1:],key=lambda x: x[3])
    Sorted_Table_Data.insert(0,["ID", "Car", "Price", "Total Sales"])


    summary_paragraph = summary[0] + "<br/>" + summary[1] + "<br/>" + summary[2]
    #/tmp/cars.pdf
    Report.generate("cars.pdf", "Sales summary for last month", summary_paragraph, Sorted_Table_Data)

    # TODO: send the PDF report as an email attachment
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Sales summary for last month"
    body = summary[0] + "\n"  + summary[1] + "\n" + summary[2]
    
    message = emails.generate(sender, receiver, subject, body, "/tmp/cars.pdf")
    emails.send(message)

if __name__ == "__main__":
    main(sys.argv)