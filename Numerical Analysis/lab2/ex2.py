import csv
import pandas as pd
import matplotlib.pyplot as plt


def linear_interpolation(y0, y1, x0=0, x1=2, xp=1):
    return y0 + ((y1-y0)/(x1-x0)) * (xp - x0)


date = []
visitor = []
with open('dataset_2.csv', 'r') as csv_file:
    file = csv.DictReader(csv_file)
    line_count = 0
    for row in file:
        if line_count == 0:
            line_count += 1
        else:
            date.append(row['Date'])
            if row['Visitors'] == 'Nan':
                visitor.append(0)
            else:
                visitor.append(int(row['Visitors']))


date_time = pd.to_datetime(date)
DF = pd.DataFrame()
DDF = pd.DataFrame()

DF['value'] = visitor

vis = [i for i in visitor]
for i in range(len(vis)):
    if vis[i] == 0:
        vis[i] = int(linear_interpolation(vis[i-1], vis[i+1]))
DDF['value'] = vis

DF = DF.set_index(date_time)
DDF = DDF.set_index(date_time)

plt.plot(DF)
plt.plot(DDF)

plt.gcf().autofmt_xdate()
plt.show()


