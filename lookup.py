from tkinter import *
import requests #connects to API so we can get information
import json
#######################
def red_green(amount):
    if amount >= 0:
        return "green"
    else:
        return "red"
######################

root = Tk()
root.title("Crypto-Currency Portfolio")

# label function in tkinter is text
name = Label(root, text="Ethan Haga", bg="white", fg="blue")
# the whole screen is a grid so put the name(label) into the top left


# these below are dictionary header keys from the API
#######################################################
#######################################################

header_name = Label(root, text="Name", bg="silver", font="Arial 12 bold")
header_name.grid(row=0, column=0, sticky=N+S+E+W)

header_rank = Label(root, text="Rank", bg="white", font="Arial 12 bold")
header_rank.grid(row=0, column=1, sticky=N+S+E+W)

header_current_price = Label(root, text="Current Price", bg="silver", font="Arial 12 bold")
header_current_price.grid(row=0, column=2, sticky=N+S+E+W)

header_price_paid = Label(root, text="Price Paid", bg="white", font="Arial 12 bold")
header_price_paid.grid(row=0, column=3, sticky=N+S+E+W)

header_1_hour_change = Label(root, text="1-hour change", bg="silver", font="Arial 12 bold")
header_1_hour_change.grid(row=0, column=4, sticky=N+S+E+W)

header_24_hour_change = Label(root, text="24-Hour Change", bg="white", font="Arial 12 bold")
header_24_hour_change.grid(row=0, column=5, sticky=N+S+E+W)

header_7_day_change = Label(root, text="7-Day Change", bg="silver", font="Arial 12 bold")
header_7_day_change.grid(row=0, column=6, sticky=N+S+E+W)

header_current_value = Label(root, text="Current Value", bg="white", font="Arial 12 bold")
header_current_value.grid(row=0, column=7, sticky=N+S+E+W)

header_profit_loss_total = Label(root, text="Profit Loss Total", bg="silver", font="Arial 12 bold")
header_profit_loss_total.grid(row=0, column=8, sticky=N+S+E+W)


#######################################################
#######################################################



def lookup():

    api_request = requests.get("https://api.coinmarketcap.com/v1/ticker/") # get this api data
    api = json.loads(api_request.content) # we are parsing the api information with json

    # this is my portfolio, a dictionary in a list
    my_portfolio = [
        {
            "sym":"BTC",
            "amt_owned": 150,
            "price_paid_per_coin": 1.4
        },
        {
            "sym":"ETH",
            "amt_owned": 379,
            "price_paid_per_coin": 3.2
        },
        {
            "sym":"XRP",
            "amt_owned": 190,
            "price_paid_per_coin": 0.6
        }
    ]
    portfolio_profit = 0
    row_count = 1
    for x in api:
        for coin in my_portfolio:
            if coin["sym"] == x["symbol"]:

                # math operations
                total_paid = float(coin["amt_owned"]) * float(coin["price_paid_per_coin"])
                current_port_value = float(coin["amt_owned"]) * float(x["price_usd"])
                profit_gained = current_port_value - total_paid
                portfolio_profit += profit_gained

                profit_gain_per_coin = float(x["price_usd"]) - float(coin["price_paid_per_coin"])

                print(x["name"])
                print("Gain per coin: ${0:.2f}".format(float(profit_gain_per_coin)))
                print("USD Price: ${0:.2f}".format(float(x["price_usd"])))
                print("Rank: {0:.1f}".format(float(x["rank"])))
                print("Total Paid: ${0:.2f}".format(float(total_paid)))
                print("Portfolio Value: ${0:.2f}".format(float(current_port_value)))
                print("Profit Gained/Loss: ${0:.2f}".format(float(profit_gained)))
                print("---------------------------------------")

                name = Label(root, text=x["name"], bg="silver")
                name.grid(row=row_count, column=0, sticky=N+S+E+W)

                rank = Label(root, text=x["rank"], bg="white")
                rank.grid(row=row_count, column=1, sticky=N+S+E+W)

                profit_loss_per = Label(root, text="${0:.2f}".format(float(profit_gained)), bg="silver", fg=red_green(float(profit_gained)))
                profit_loss_per.grid(row=row_count, column=2, sticky=N+S+E+W)

                profit_loss_total = Label(root, text="${0:.2f}".format(float(profit_gain_per_coin)), bg="white", fg=red_green(float(profit_gain_per_coin)))
                profit_loss_total.grid(row=row_count, column=3, sticky=N+S+E+W)

                current_price = Label(root, text="${0:.2f}".format(float(x["price_usd"])), bg="silver", fg=red_green(float(x["price_usd"])))
                current_price.grid(row=row_count, column=4, sticky=N+S+E+W)

                price_paid = Label(root, text="${0:.2f}".format(float(coin["price_paid_per_coin"])), bg="white", fg=red_green(float(coin["price_paid_per_coin"])))
                price_paid.grid(row=row_count, column=5, sticky=N+S+E+W)

                one_hour_change = Label(root, text="%{0:.2f}".format(float(x["percent_change_1h"])), bg="silver", fg=red_green(float(x["percent_change_1h"])))
                one_hour_change.grid(row=row_count, column=6, sticky=N+S+E+W)

                twentyfour_hour_change = Label(root, text="%{0:.2f}".format(float(x["percent_change_24h"])), bg="white", fg=red_green(float(x["percent_change_24h"])))
                twentyfour_hour_change.grid(row=row_count, column=7, sticky=N+S+E+W)

                seven_day_change = Label(root, text="%{0:.2f}".format(float(x["percent_change_7d"])), bg="silver", fg=red_green(float(x["percent_change_7d"])))
                seven_day_change.grid(row=row_count, column=8, sticky=N+S+E+W)

                row_count += 1

    portfolio_profit = Label(root, text="$")

lookup()
root.mainloop()
