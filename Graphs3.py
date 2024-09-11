import numpy as np
import matplotlib.pyplot as plt
from matplotlib import interactive
import matplotlib.pyplot as plt
import sys
import sqlite3

def viewg(g1):
    

    for row in g1.values():
        pass

    height=[]
    bars = ()
    bars= tuple(g1.keys())



    print(type(g1.values()))
    height= list(g1.values())
    print(bars, height)
    f=plt.figure(1)
    plt.ion()
    y_pos = np.arange(len(bars))
    plt.bar(bars,height, color=['blue', 'cyan', 'orange'])
    plt.xlabel('Sentiment Analysis')
    plt.ylabel('No.of Tweets')
    plt.title('Features')
    plt.show()
    plt.pause(0.0001)  
    labels =  g1.keys()
    sizes =  g1.values()
    explode = (0.1, 0.1,0.1)  
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    fig1.canvas.manager.window.move(1000,100)
    

if __name__ == "__main__":
    d={'jan':2,'feb':0,'mar':0}
    viewg(d)



