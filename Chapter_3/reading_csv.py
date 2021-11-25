import pandas as pd
from pandas import plotting
import matplotlib.pyplot as plt

rain = pd.read_csv("https://milliams.com/courses/data_analysis_python/rain.csv")

""" Find the mean """
# print(rain.mean())

""" How many years was rain above 100mm for each city """
# print(rain[rain > 100].count())

""" Extract single column """
# cardiff = rain["Cardiff"]
# print(cardiff)

""" Plot data using pandas """
# rain.plot(xlabel="Date", ylabel="Average monthly rainfall (mm) ")
# plt.show()

# example = "https://milliams.com/courses/data_analysis_python/city_pop.csv"
# # print(example)
# """ To skip rows """
# example = pd.read_csv(example, skiprows=5, sep=";", na_values="-1", index_col="year")  # Skip certain rows. Controlled by sep => separator value.
# print(example)

""" Querying Data """
tips = pd.read_csv("https://milliams.com/courses/data_analysis_python/tips.csv")
# print(tips[["total_bill", "tip"]].count())
# print(tips.loc[2])  # Returns second row.
# print(tips["size"].mean())
# print(tips["size"].sum())
# print(tips["size"].max())  # Returns max VALUE.
# print(tips["size"].idxmax())  # Returns row index which contains max value.
# index_of_max_bill = tips["total_bill"].idxmax()
# print(tips.loc[index_of_max_bill])  # Biggest bill and related information.
# index_of_smallest_bill = tips["total_bill"].idxmin()
# print(tips.loc[index_of_smallest_bill])  # Smallest bill and related information.
# print(tips["tip"] / tips["total_bill"] * 100)  # Ratio between tip amount and total bill value. *100 to get percentage
# tips["Total Spent (PP)"] = tips["total_bill"] / tips["size"]
# print(tips)

""" Perform operation on subset of data. Create a filter, apply filter. """
# Tips on certain days might affect data so just grab data for Saturdays etc.
# Grab day column which refers to Sat.
sat = tips[tips["day"] == "Sat"]
thur = tips[tips["day"] == "Thur"]
# print(thur)
# print(thur["tip"].mean())
# print(sat["tip"].mean())
# print(thur.mean())
#
# print(tips[tips["size"] >= 5])  # Print info where party size >= 5.
""" Apply 2 filters """'' \
    # Prints data only from Saturday where bill is <= to 10.
# print(tips[(tips["day"] == "Sat") & (tips["total_bill"] <= 10)])

# Filtering data so only parties of >= 4 people which were there at lunch time is presented.
# print(tips[(tips["size"] >= 4) & (tips["time"] == "Lunch")])
