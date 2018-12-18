import matplotlib.pyplot as plt
import pandas as pd
import statistics
import time
import requests
import json
from scipy.stats import norm
import numpy as np


# to get new data
#url = "https://blockchain.info/charts/market-price?timespan=2961days&format=json"

#req = requests.get(url)

#print(req.json())

#f = open('C:/Users/bunchies/Desktop/btcdata/btcdataNew.json', 'w')
#f.write(str(req.json()))


# open data file
data = eval(open('C:/Users/bunchies/Desktop/btcdata/btcdataNew.json', 'r').read())

# init
allSamples = []
allTimes = []
sample = []
times = []
weeklyDeviations = []
weeklyMeans = []
weeklyTimes = []
weeklySamples = []
monthVars = []
monthlyMeans = []
monthlySamples = []
monthlyDeviations = []
monthlyTimes = []
count = 0
weeks = 0
month = 0
months = 0
days = 0
year = 0
i = []
y = 364
m = 29
w = 6

# plot prep
fig = plt.figure()
ax1 = plt.subplot2grid((10,2), (0,0) , rowspan=4, colspan=2)
ax3 = plt.subplot2grid((10,2), (4,0) , rowspan=3, colspan=1)
ax2 = plt.subplot2grid((10,2), (7,0) , rowspan=3, colspan=1)
ax4 = plt.subplot2grid((10,2), (4,1) , rowspan=3, colspan=1)
ax5 = plt.subplot2grid((10,2), (7,1) , rowspan=3, colspan=1)

# changes class prepares % changes for weekly mean and deviation, monthly mean and deviation and First/Last monthly Mean/Deviation XBAR
class changes:
    def meanChanges():
        i = []
        for j in meanChanges.pct_change():
            i.append(j)
        return i
    def deviationChanges():
        i = []
        for j in deviationChanges.pct_change():
            i.append(j)
        return i
    def mDeviationChanges():
        i = []
        for j in mDeviationChanges.pct_change():
            i.append(j)
        return i

    def mMeanChanges():
        i = []
        for j in mMeanChanges.pct_change():
            i.append(j)
        return i
    def weeklyXbar():
        wCount = 0
        firstHalf = []
        lastHalf = []
        weeklyChanges = changes.deviationChanges()

        for j in weeklyChanges:
            if wCount > 0 and wCount < 105:
                firstHalf.append(j)
                print("first half : ", wCount)

            elif wCount == 105:
                print("COUNT IS 105 - SKIPPING WEEK")
            elif wCount > 105:
                lastHalf.append(j)
                print("last half : ", wCount)


            wCount += 1

        print("COUNT WEEKLY XBAR = ", wCount)
        firstHalfMean = statistics.mean(firstHalf)
        firstHalfDeviation = statistics.stdev(firstHalf)
        lastHalfMean = statistics.mean(lastHalf)
        lastHalfDeviation = statistics.stdev(lastHalf)
        return firstHalfMean, lastHalfMean, firstHalfDeviation, lastHalfDeviation

    def monthlyDeviationXBars():
        devCount = 0
        firstHalf = []
        lastHalf = []
        for data in monthlyDeviations:

            if devCount <= 24:
                firstHalf.append(data)
            else:
                lastHalf.append(data)
            devCount += 1
        firstXBar = statistics.mean(firstHalf)

        lastXBar = statistics.mean(lastHalf)

        return firstXBar, lastXBar

    def monthlyMeanXBars():
        meanCount = 0
        firstHalf = []
        lastHalf = []
        for data in monthlyMeans:

            if meanCount <= 24:
                firstHalf.append(data)
            else:
                lastHalf.append(data)
            meanCount += 1
        firstXBar = statistics.mean(firstHalf)
        lastXBar = statistics.mean(lastHalf)
        return firstXBar, lastXBar

# single for loop to process all data
for dat in data['values']:
    #begin day
    times.append(dat['x']), allTimes.append(dat['x'])
    sample.append(dat['y']), allSamples.append(dat['y'])
    monthVars.append(dat['y'])
    print("day number : ", days, " Date ", time.ctime(dat['x']))

    if days == y:
        # year counter
        print("\nYear Number : ", year)
        y += 365
        year += 1
    # weekly checks
    if days == w:
        w += 7
        print("\nWeek # ", weeks, " of", time.ctime(dat['x']))
        weeklySamples.append(dat['y'])
        # final day of week
        #gather all main data points
        # get stats from current weeks data
        deviation = statistics.stdev(sample)
        mean = statistics.mean(sample)
        # get percentage changes from daily price action
        priceChanges = pd.Series(sample)
        #add deviations for the week to list
        weeklyDeviations.append(deviation)
        # add current weeks means for the weekly plots
        weeklyMeans.append(mean)
        #add current days epoch for weekly plots
        weeklyTimes.append(dat['x'])
        #display weekly data
        print("\n7 day mean", mean)
        print("7 day stddev", deviation)
        print("\nWeekly Percentage change per day : \n", priceChanges.pct_change())
        # monthly checks
        if days == m:
            m += 30
            monthlySamples.append(dat['y']), monthlyTimes.append(dat['x'])
            monthlyDeviations.append(statistics.stdev(monthVars))
            monthlyMeans.append(statistics.mean(monthVars))
            print("Month number  : ", months)
            print("Monthly Mean : ", monthlyMeans[months])
            print("Monthly Deviation", monthlyDeviations[months])
            # increment new month
            months += 1
            monthVars = []
            print("\nBegin New Month number", months)

        # increment for new week
        weeks += 1
        # reset sample, times AND START NEW WEEK
        sample = []
        times = []
        print("\nBegin New Week number :", weeks)
    else:
        # continue on same week
        # monthly checks
        if days == m:
            m += 30
            monthlySamples.append(dat['y']), monthlyTimes.append(dat['x'])
            monthlyDeviations.append(statistics.stdev(monthVars))
            monthlyMeans.append(statistics.mean(monthVars))
            print("Month number : ", months)
            print("Monthly Mean : ", monthlyMeans[months])
            print("Monthly Deviation", monthlyDeviations[months])
            months += 1
            monthVars = []
            print("\nBegin New Month number :", months)
    days +=1

# gather final change %s
deviationChanges = pd.Series(weeklyDeviations)
meanChanges = pd.Series(weeklyMeans)
mDeviationChanges = pd.Series(monthlyDeviations)
mMeanChanges = pd.Series(monthlyMeans)

#final output for project comparison
weeklyXBar = changes.weeklyXbar()

# Display processed Data
# output final data
print("\nWeekly Deviation % Changes \n", deviationChanges.pct_change())
print("\nWeekly Mean % Changes \n", meanChanges.pct_change())
print("\n Monthly Deviation % Changes \n", mDeviationChanges.pct_change())
print("\n Monthly Mean % Changes \n", mMeanChanges.pct_change(), "\n")

print("****** These numbers are Total numbers for actual price data   \t  ******")
print("****** Public API provides actual price data for every other day  ******")
print("****** There are half as many price points as length of time span ******\n")

print("Total number of Days", days)
print("Total number of Weeks", weeks)
print("Total number of Months", months)
print("Total number of Years", year)

print("\nFirst Monthly Deviation X Bar : ", changes.monthlyDeviationXBars()[0])
print("Last Monthly Deviation X Bar : ", changes.monthlyDeviationXBars()[1])

print("\n*** XBAR FROM WEEKLY DEVIATION PERCENTAGE CHANGES!!! ***\n")

print("First Half : ", weeklyXBar[0], "\nLast Half : ", weeklyXBar[1])
print("First Half Deviation : ", weeklyXBar[2], "\nLast Half Deviation : ", weeklyXBar[3])
#plot charts, color, legend names, grid, clear xaxis

ax1.grid(),ax2.grid(),ax3.grid(), ax4.grid(), ax5.grid()
ax1.plot(allTimes, allSamples, color='green', label='Price')
ax2.plot(weeklyTimes, changes.meanChanges(), color='blue', label='Weekly Mean')
ax3.plot(weeklyTimes, changes.deviationChanges(), color='red', label='Weekly Deviation')
ax4.plot(monthlyTimes, changes.mDeviationChanges(), color='orange', label='Monthly Deviation')
ax5.plot(monthlyTimes, changes.mMeanChanges(), color='grey', label='Monthly Mean')
ax1.xaxis.set_major_formatter(plt.NullFormatter())
ax3.xaxis.set_major_formatter(plt.NullFormatter())
ax4.xaxis.set_major_formatter(plt.NullFormatter())

#chart labels
ax1.set_ylabel("Price in $USD")
ax2.set_xlabel("Epoch Time (UTC)")
ax5.set_xlabel("[Sept 2010 - Nov 2018]")
ax2.set_ylabel("% Change")
ax3.set_ylabel("% Change")
ax4.set_ylabel("% Change")
ax5.set_ylabel("% Change")

#legend positions, frame
ax1.legend(loc='upper left', frameon=True)
ax2.legend(loc='upper right', frameon=True)
ax3.legend(loc='upper right', frameon=True)
ax4.legend(loc='upper right', frameon=True)
ax5.legend(loc='upper right', frameon=True)

#display charts
plt.show()

# Plot between -10 and 10 with .1 steps.
x_axis = np.arange(-10, 10, 0.1)
# Mean = weeklyXBar[0,1], SD = weeklyXBar[2,3]
plt.draw()
plt.plot(x_axis, norm.pdf(x_axis,weeklyXBar[0],weeklyXBar[2]), color='blue', label='First Half')
plt.plot(x_axis, norm.pdf(x_axis,weeklyXBar[1],weeklyXBar[3]), color='red', label='Last Half')
plt.legend(loc='upper left')
plt.show()







