import statistics
import pandas as pd
import csv
import plotly.figure_factory as ff
import random
import plotly.graph_objects as go

df = pd.read_csv("c111_data.csv")
data = df["Math_score"].tolist()
 

def random_set_of_mean (counter) :
    dataset = []
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean


mean_list=[] 
for i in range(0,1000):
    s= random_set_of_mean(100)
    mean_list.append(s)
Sd= statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
 
print("standar deviation of mean list",Sd)
print("mean of sample meanlist",mean)


sd1_start,sd1_end=mean-Sd,mean + Sd
sd2_start,sd2_end=mean-(2*Sd),mean + (2*Sd)
sd3_start,sd3_end=mean-(3*Sd),mean + (3*Sd)


df = pd.read_csv("i2.csv")
data = df["Math_score"].tolist()

meani=statistics.mean(data)
print("mean of intervention1 is",meani)
fig=ff.create_distplot([mean_list],["result"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[meani,meani],y=[0,0.17],mode="lines",name="mean intervention"))

fig.add_trace(go.Scatter(x=[sd1_end,sd1_end],y=[0,0.17],mode="lines",name=" standard deviation end 1"))
fig.add_trace(go.Scatter(x=[sd2_end,sd2_end],y=[0,0.17],mode="lines",name=" standard deviation end 2"))

fig.show()

z=(mean-meani)/Sd 

print(z)