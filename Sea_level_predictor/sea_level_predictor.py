import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level'] 
    plt.scatter(x,y,label='Data')

    # Create first line of best fit
    res = stats.linregress(x,y)
    xe = np.linspace(1880,2050,100)
    plt.plot(xe, res.intercept + res.slope*xe, 'r', label='Best fit line')

    # Create second line of best fit
    df2 = df.loc[(df['Year'] > 1999)]
    x2 = df2['Year']
    y2 = df2['CSIRO Adjusted Sea Level']
    res2 = stats.linregress(x2,y2)
    xe2 = np.linspace(2000,2050,100)
    plt.plot(xe2, res2.intercept + res2.slope*xe2, 'g', label='Best fit line (2000)')
    plt.xlim(1880,2060)
    plt.legend()

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()