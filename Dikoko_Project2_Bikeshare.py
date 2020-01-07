import time
import pandas as pd
import numpy as np

# Opening the csv files with raw data from Motivate
CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


# Loading the data for analysis
def load_data(city):
    df = pd.read_csv(CITY_DATA[city])

    # Data Cleaning
    ## Replacing NAN Values
    df.fillna(method='backfill', axis=0, inplace=True)
    df.fillna(method='ffill', axis=0, inplace=True)

    ##Converting the data into datetime so that we can manipulate the dates
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.weekday_name
    df['Hour of Day'] = df['Start Time'].dt.hour

    filter = input(
        'Would you like to filter data by month, day or both? Default gives the summary statitics of the city you have chosen.').lower()
    if filter == 'month' or filter == 'both':
        month = input('Which month- January, February, March, April, May or June?').lower()
        if month != '':
            # use the index of the months list to get the corresponding int
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            month = months.index(month) + 1
            # filter by month to create the new dataframe
            df = df[df['Month'] == month]

    if filter == 'day' or filter == 'both':
        # filter by day
        day = input('Which day- Monday, Tuesday, Wednesday, Thursday, Friday,Saturday or Sunday?').title()
        if day != '':
            # filter by day of week to create the new dataframe
            df = df[df['Day of Week'] == day.title()]
        else:
            print('Please try again since you have chosen to stop filtering by days of the week')

    # Popular Times of Travel
    ##Popular Hour
    popular_hour = df['Hour of Day'].mode()[0]
    print('The most popular Start Hour:', popular_hour)

    ##Popular Weekday

    popular_day = df['Day of Week'].mode()[0]
    print('The most popular Day:', popular_day)

    ##Popular Month
    popular_month = df['Month'].mode()[0]
    print('The most popular Month:', popular_month)

    # Popular Stations and Trips
    ##Start Station
    start_station = df['Start Station'].mode()[0]
    print('The most common Start Station is:', start_station)

    ##End Station
    end_station = df['End Station'].mode()[0]
    print('The most common End Station is:', end_station)

    ##Combination of Start and End Station
    station_combo = df['Start Station'] + ' , ' + df['End Station']
    station_trip = station_combo.mode()[0]
    print('The most common trip from start to end (by station) is:', station_trip)

    # Trip Duration
    ##Total Travel Time
    tot_travel_time = df['Trip Duration'].sum()
    print('The total travel time is:', tot_travel_time)

    ##Average Travel Time
    avg_trave_time = df['Trip Duration'].mean()
    print('The average travel time is:', avg_trave_time)

    ##Counts of each user type
    userstype_count = df['User Type'].value_counts()
    print('The user types are:', userstype_count)

    if city != 'washington':
        # Counts of each gender
        gender_count = df['Gender'].value_counts()
        print('The gender split is:', gender_count)

        # Most common birth year
        common_birthyear = df['Birth Year'].mode()[0]
        print('The most common Year of Birth:', common_birthyear)

        # Earliest Birth Year
        earliest_birthyear = df['Birth Year'].min()
        print('The earliest Birth Year is:', earliest_birthyear)

        # Recent Birth Year
        recent_birthyear = df['Birth Year'].max()
        print('The most recent Birth Year is:', recent_birthyear)

    # Does user want to view raw data? Created a loop that prompts them if they want to see raw data which breaks if they say no.
    while True:
        raw_data = input('Would you like to see rows of raw data (Yes or No)?').lower()
        if raw_data == 'yes':
            no_of_rows = input('How many rows?')
            print(df.head(int(no_of_rows)))
            raw_data
        else:
            break


while True:
    city = input('Would you like to see data for Chicago, New York City, or Washington? ').lower()
    if city in (CITY_DATA.keys()):
        print('You have chosen: ', city)
        load_data(city)
        try_again = input('Would you like to try another city, month or day (Yes or No)?').lower()
        if try_again == "yes":
            pass
        else:
            print("You have chosen to discontinue viewing our data. Thank you for stopping-by! ")
            break
    else:
        print('Oops! That\'s not a valid city name. Try again.')
