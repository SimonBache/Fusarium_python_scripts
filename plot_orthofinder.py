import pandas as pd

data = pd.read_csv("/home/bache/PycharmProjects/pythonProject1/new_assemblies/orthofinder/effecteurs/matrix.csv", index_col=False)

list_value = list(data["count"])


count = pd.Series(list_value, index=[data["UK0001"], data["CAV092"], data["CAV180"], data["CAV807"], data["CAV3049"]])

from upsetplot import plot

plot(count, show_counts=True, sort_by='cardinality')
from matplotlib import pyplot
pyplot.show()
