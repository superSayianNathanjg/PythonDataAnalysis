""" Visualisations

Three main types:
    * Plotting relationships between variables in the data set.
    * Plotting distribution of variables.
    * Seeing how the data varies by category.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

rain = pd.read_csv("https://milliams.com/courses/data_analysis_python/rain.csv")
# rain.plot()
# plt.show()

""" 
Exercise: Read in Office data, draw a line plot of the January temperature over time 
"""
temp = pd.read_csv("https://milliams.com/courses/data_analysis_python/cetml1659on.txt",
                   skiprows=6,
                   delim_whitespace=True,
                   na_values=["-99.9", "99.9"],   # NaN values
)

# year_plot = temp["JAN"].plot(xlabel="Year", ylabel=r"Temperature ($\degree$C)")
# plt.show()


""" *** Seaborn plotting using Tips Data ***
 Pass in dataframe and two dimensions you want compared. Eg. Numerical dimensions not categorical. 
 Data agrument should be Dataframe and x,y should be names of columns. 
"""
tips = pd.read_csv("https://milliams.com/courses/data_analysis_python/tips.csv")
# g = sns.relplot(data=tips, x="total_bill", y="tip")  # Compare total bill to tips.
# g.set_axis_labels("Total Bill ($\degree$C)", "Tip")
# plt.show()

""" Bill per person and percent tip, plot relationship.
Bill per person = Total bill / size of table. 
Percent tip = tip / total bill * 100. 
Set colour to be based on day. 
"""
# tips["bill_per_person"] = tips["total_bill"] / tips["size"]
# tips["percent_tip"] = tips["tip"] / tips["total_bill"] * 100
# sns.relplot(data=tips, x="bill_per_person", y="percent_tip", hue="day")
# plt.show()

""" Displot """
# sns.displot(data=tips, x="total_bill", hue="time", stat="density", common_norm=False)
# plt.show()

""" 
    *** Ex, How time of day affects how much each person spends on average *** 
    Average spend per person = total_bill / party size. 
"""
# tips["avg_spend"] = tips["total_bill"] / tips["size"]
# sns.displot(data=tips, x="avg_spend", hue="time", kind="kde")  # Compare day/night with avg spend.
# plt.show()

""" Categorical Data 
Categories for this data is time and day. To see how total_bill depended on day of the week...
"""
# sns.catplot(data=tips, x="day", y="total_bill", hue="time", order=["Thur", "Fri", "Sat", "Sun"])
sns.catplot(data=tips, x="day", y="total_bill", hue="time", order=["Thur", "Fri", "Sat", "Sun"], kind="violin")
# plt.show()

""" Larger spend on weekends, is this because of:
    large average spend per person?
    or from larger average group sizes?
"""
tips["avg_spend"] = tips["total_bill"] / tips["size"]  # Average spend per person.
# sns.catplot(data=tips, x="day", y="avg_spend", hue="time", order=["Thur", "Fri", "Sat", "Sun"], kind="box")
# Comparing with size.
sns.catplot(data=tips, x="day", y="size", hue="time", order=["Thur", "Fri", "Sat", "Sun"], kind="violin")
plt.show()



