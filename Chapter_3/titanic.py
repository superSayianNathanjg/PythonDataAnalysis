""" Answer the following questions regarding the Titanic Dataset """

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import dataset.
tit_data = pd.read_csv("https://milliams.com/courses/data_analysis_python/titanic.csv")

"""
 *** Summarising Questions *** 
"""

"""  Average age of all people on board """
# print(tit_data.info())
# print(tit_data.describe())  # Average age can be shown.
# print(tit_data["age"].describe())  # Average age can be shown.
# print(tit_data["age"].mean())  # Better way to do it.

""" Filter to select only males """
# print(tit_data[tit_data["gender"] == "male"])
only_males = tit_data[tit_data["gender"] == "male"]
# print(only_males)

""" Find average age of the males on board """
# print(tit_data[tit_data["gender"] == "male"].describe())
# print(only_males["age"].mean())  # Better way to do it.

""" *** Filter Questions ***  """
""" Select only people in 3rd class """
# print(tit_data[tit_data["class"] == "3rd"])

""" Create dataframe with only passengers on board """
passengers = tit_data[tit_data["class"].isin(["1st", "2nd", "3rd"])]
# print(passengers)

""" Plotting """
""" Plot and compare distribution of ages for males and females """
# sns.displot(data=passengers,
#             x="age",
#             hue="gender",
#             kind="kde",
#             cut=0
#             )
#
# """ Split by classes. Just add col="class", and col_order=["c1, etc]. """
# sns.displot(data=passengers,
#             x="age",
#             hue="gender",
#             kind="kde",
#             cut=0,
#             col="class",
#             col_order=["1st", "2nd", "3rd"]
#             )
#
# plt.show()

""" Combine 
Calculate percentage that survived within each class. 

Create a function called survived_percentage, which takes in a dataframe. 
Takes DF then returns total amount that survived (yes) divided by length of dataframe. 
Split three classes into dataframes and then pass to function. 
"""


def survived_percentage(df):
    yes = df[df["survived"] == "yes"]  # How many survived.
    return len(yes) / len(df)  # Total survived / total amount of people in this class.


first_class = survived_percentage(passengers[passengers["class"] == "1st"])  # 1st class ratio.
second_class = survived_percentage(passengers[passengers["class"] == "2nd"])  # 2nd class ratio.
third_class = survived_percentage(passengers[passengers["class"] == "3rd"])  # 3rd class ratio.

print("Ratio for 1st class = " + str(first_class) + "\nRatio for 2nd class = " + str(second_class) +
      "\nRatio for 3rd class = " + str(third_class))
