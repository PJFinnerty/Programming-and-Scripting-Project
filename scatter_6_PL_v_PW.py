# Peter Finnerty - Project - Scattergrams.

# Output a scattergram of each variable to png files.
#  This program will create a scattergram of (a)Iris setosa, (b)Iris virginica 
# and (c)Iris versicolor.

# Petal Length versus Petal Width

# 6. 
#------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")

sL = df["petal_length"]
sW = df["petal_width"]

plt.scatter(df['petal_length'], df['petal_width'] )
# or plt.scatter(sL, sW)
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.title("Petal Length Versus Petal Width (ALL SPECIES)")
#plt.legend()
plt.show()

#plt.savefig("scatter6-PLvPW.png")
#plt.clf