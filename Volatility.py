import matplotlib.pyplot as plt
import pandas as pd
import statistics
import time

# open data file
data = eval(open('C:/Users/bunchies/Desktop/btcdata/btcdata.json', 'r').read())

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
n = 364
m = 29
w = 6
w2 = 4

# plot prep
fig = plt.figure()
ax1 = plt.subplot2grid((10,2), (0,0) , rowspan=4, colspan=2)
ax3 = plt.subplot2grid((10,2), (4,0) , rowspan=3, colspan=1)
ax2 = plt.subplot2grid((10,2), (7,0) , rowspan=3, colspan=1)
ax4 = plt.subplot2grid((10,2), (4,1) , rowspan=3, colspan=1)
ax5 = plt.subplot2grid((10,2), (7,1) , rowspan=3, colspan=1)

# changes class prepares % changes for weekly mean and deviation, monthly mean and deviation and First/Last 
monthly Mean/Deviation XBAR
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

    def monthlyDeviationXBars():
        meanCount = 0
        firstHalf = []
        lastHalf = []
        for data in monthlyDeviations:

            if meanCount <= 24:
                firstHalf.append(data)
            else:
                lastHalf.append(data)
            meanCount += 1
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
    print("day number : ", days, " Date ", time.ctime(dat['x']))

    if days == n:
        # year counter
        print("\nYear Number : ", year)
        n += 365
        year += 1
    allTimes.append(dat['x']), allSamples.append(dat['y'])
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
        print("\nWeekly Precentage change per day : \n", priceChanges.pct_change())
        # reset sample, times and count
        sample = []
        times = []

        # increment for new week
        weeks += 1
        # monthly checks
        monthVars.append(dat['y'])
        if days == m:
            m += 30
            monthlySamples.append(dat['y'])
            monthlyDeviations.append(statistics.stdev(monthVars))
            monthlyMeans.append(statistics.mean(monthVars))
            monthlyTimes.append(dat['x'])
            print("Month number  : ", months)
            print("Monthly Mean : ", monthlyMeans[months])
            print("Monthly Deviation", monthlyDeviations[months])
            months += 1
            monthVars = []
            print("\nBegin New Month number", months)
        print("\nBegin New Week number :", weeks)
    else:
        # continue on same week
        times.append(dat['x']), allTimes.append(dat['x'])
        sample.append(dat['y']), allSamples.append(dat['y'])

        # monthly checks
        monthVars.append(dat['y'])
        if days == m:
            m += 30
            monthlySamples.append(dat['y'])
            monthlyDeviations.append(statistics.stdev(monthVars))
            monthlyMeans.append(statistics.mean(monthVars))
            monthlyTimes.append(dat['x'])
            monthVars = []
            print("Month number : ", months)
            print("Monthly Mean : ", monthlyMeans[months])
            print("Monthly Deviation", monthlyDeviations[months])
            months += 1
            print("\nBegin New Month number :", months)
    days +=1


# gather final weekly change %s
deviationChanges = pd.Series(weeklyDeviations)
meanChanges = pd.Series(weeklyMeans)
mDeviationChanges = pd.Series(monthlyDeviations)
mMeanChanges = pd.Series(monthlyMeans)

# Display processed Data
# output final data
print("\nWeekly Deviation % Changes \n", deviationChanges.pct_change())
print("\nWeekly Mean % Changes \n", meanChanges.pct_change())
print("\n Monthly Deviation % Changes \n", mDeviationChanges.pct_change())
print("\n Monthly Mean % Changes \n", mMeanChanges.pct_change())

print("\n****** These numbers are Total numbers for actual price data   \t ******")
print("****** Public API provides actual price data for every other day  ******")
print("****** There are half as many price points as length of time span ******")
print("\nTotal number of Days", days)
print("Total number of Weeks", weeks)
print("Total number of Months", months)
print("Total number of Years", year)
print("\nFirst Monthly Deviation X Bar : ", changes.monthlyDeviationXBars()[0])
print("Last Monthly Deviation X Bar : ", changes.monthlyDeviationXBars()[1])
print("First Monthly Mean X Bar : ", changes.monthlyMeanXBars()[0])
print("Last Monthly Mean X Bar : ", changes.monthlyMeanXBars()[1])


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
ax5.set_xlabel("[Sept 2010 - Oct 2018]")
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



