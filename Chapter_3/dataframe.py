"""

Dataframe
Table of data. 2D list. => Series is a column. Dataframe contains a bunch of series' in a collection.

Dataframe selects by column first.
A Series selects by row.

Dataframe takes more work to find rows and is slower than taking out/finding columns.
"""
from pandas import DataFrame

data = {
    "city": ["Paris", "Paris", "Paris", "Paris",
             "London", "London", "London", "London",
             "Rome", "Rome", "Rome", "Rome"],
    "year": [2001, 2008, 2009, 2010,
             2001, 2006, 2011, 2015,
             2001, 2006, 2009, 2012],
    "pop": [2.148, 2.211, 2.234, 2.244,
            7.322, 7.657, 8.174, 8.615,
            2.547, 2.627, 2.734, 2.627]
}

df = DataFrame(data)
# print(df)
# print(df.head())
# print(df.info())

# Check if Paris matches with entire dataframe
# - df["city"] == "Paris"

""" To return only values that match with Paris 
 - df[df["city"] == "Paris"]  """
# print(df[df["city"] == "Paris"])

# print(df.loc[3])  # Extract particular row.

""" 
Adds a new column continental, from existing columns which != London.
To delete a column, # del df["Continental"]  
"""
# df["Continental"] = df["city"] != "London"
# print(df)

""" Ex) To find citys with population  < 2.6 million """
# print(df["pop"] < 2.6)  # Returns list showing all cities and whether true or false to < 2.6 mill pop.
# print(df[df["pop"] < 2.6])  # Return only cities with < 2.6 million pop.
# print(df[df["year"] == 2001]
pop = (df[df["year"] == 2001]["pop"])
# print(pop.min())  # Print minimum value.
# print(pop.idxmin())  # Returns the row which has the minimum in it.

print(df["city"][pop.idxmin()])
