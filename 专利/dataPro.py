import pandas as pd
import matplotlib.pyplot as plt


fig = plt.figure()



data = pd.read_csv('positive_ZL2.csv')
positive = data[data['label']==1]
nagetive = data[data['label']==0]


axes = fig.add_subplot(111)

axes.scatter(positive['inner'],positive['sum'],color='red')
axes.scatter(nagetive['inner'],nagetive['sum'],color='blue')


plt.show()
