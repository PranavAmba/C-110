import pandas as pd
import csv
import random
import statistics as stx
import plotly.figure_factory as ff
import plotly.graph_objects as go

df=pd.read_csv('data.csv')
data=df['temp'].tolist()

#go to find mean and standard deviation of 100 point

dataset=[]
for i in range (0,100):
    random_index=random.randint(0,len(data))
    value=data[random_index]
    dataset.append(value)

mean= stx.mean(dataset)
std_dev=stx.stdev(dataset)

print('mean_of_sample',mean)
print('standard_deviation_of_sample',std_dev)

#go to find the mean of 100 datapoints 1000 times and plot it

def ramdom_set_of_mean(counter):
    dataset=[]
    for i in range (0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)

    mean= stx.mean(dataset)
    return mean

def show_fig(mean_list):
    df=mean_list
    mean=stx.mean(df)
    fig=ff.create_distplot([df],['temp'],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode='lines',name='mean'))
    fig.show()

def setup():
    mean_list=[]
    for i in range (0,1000):
        set_of_mean=ramdom_set_of_mean(100)
        mean_list.append(set_of_mean)

    show_fig(mean_list)
    mean=stx.mean(mean_list)
    print('mean of sampling distribution : ',mean)

setup()

population_mean=stx.mean(data)
print('population_mean:',population_mean)

def standard_deviation():
    mean_list=[]
    for i in range (0,1000):
        set_of_mean=ramdom_set_of_mean(100)
        mean_list.append(set_of_mean)
    standard_dev=stx.stdev(mean_list)
    print ('standard_deviation of sampling distribution:',standard_dev)

standard_deviation()