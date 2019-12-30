# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import time
import pandas as pd
import numpy as np

data = {'chicago': 'chicago.csv',
        'new york city': 'new_york_city.csv',
        'washington': 'washington.csv'}

cities = ['chicago', 'new york city', 'washington']
months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']


def get_filters():
    
    """Ask user to specify city, month, day
    Returns these specific values"""
    
    print("Hello! Let's explore some US Bikeshare Data!")
    
    print("Would you like to see data for Chicago, New York, or Washington?")
    def city_name():
        city = str(input('Type city name: '))
        city = city.lower()
        if city not in cities:
            print("Please select the correct city among Chicago, New York City or Washington")
            city = city_name()
        return city
    city = city_name()
    
    print("Select a month or all?")
    def month_name():
        month = str(input('Type month name jan, feb, mar, apr, may, jun or all: '))
        month = month.lower()
        if month not in months:
            print("Please select the correct month?")
            month = month_name()
        return month
    month = month_name()
    
    print("Select a day of the week or all?")
    def day_name():
        day = str(input('Type a day name: '))
        day = day.lower()
        if day not in days:
            print("Select a valid day name?")
            day = day_name()
        return day
    day = day_name()
    
    print("#"*30)
    return city, month, day


def load_data(city, month, day):
    
    """Loads data for the specified city and filters 
    by month and day"""
    
    df = pd.read_csv(data[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.weekday_name
    
    #filter by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        df = df[df['Month'] == month]
        
    #filter by day of week
    if day != 'all':
        df = df[df['Day of Week'] == day.title()]
        
    return df


def time_stats(orignal_df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    orignal_df['month'] = pd.DatetimeIndex(orignal_df['Start Time']).month

    months_count = orignal_df['month'].value_counts()

    maxV = months_count.idxmax()
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    print('Most common month is {} and count is {}.'.format((months[maxV-1]).title(),months_count.max()))

    # display the most common day of week
    orignal_df['Week Day'] = pd.DatetimeIndex(orignal_df['Start Time']).weekday_name
    days_count = orignal_df['Week Day'].value_counts()

    maxDay = days_count.idxmax()

    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    print('Most common day of week is {} and count is {}.'.format(maxDay.title(),days_count.max()))



    # display the most common start hour

    orignal_df['Hours'] = pd.DatetimeIndex(orignal_df['Start Time']).hour
    hours_count = orignal_df['Hours'].value_counts()

    print('Most common hour is {} and count : {}'.format(hours_count.idxmax(),hours_count.max()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('#'*30)
          
          
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    Start_Station_counts = df['Start Station'].value_counts()
    print('Most commonly used start station is "{}" and count : {}'.format(Start_Station_counts.idxmax(),Start_Station_counts.max()))
    # display most commonly used end station
    End_Station_counts = df['End Station'].value_counts()
    print('Most commonly used end station is "{}" and count : {}'.format(Start_Station_counts.idxmax(),End_Station_counts.max()))
    # display most frequent combination of start station and end station trip
    df['Start End stations'] = df['Start Station'] + df['End Station']
    Start_End_Station = df['Start End stations'].value_counts()

    print('Most commonly used start station and end station is "{}" and counts :"{}".'.format(Start_End_Station.idxmax(),Start_End_Station.max()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('#'*30)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time_sum = df['Trip Duration'].sum()
    print('Total travel time is {}.'.format(total_time_sum))
    # display mean travel time
    total_time_mean = df['Trip Duration'].mean()
    print('Total traveling mean time is {}.'.format(total_time_mean))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('#'*30)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user = df['User Type'].value_counts()
    print('Total Counts of user type are {}.'.format(count_user))
    # Display counts of gender
    df['Gender'].fillna('Not given',inplace=True)
    count_user_gender = df['Gender'].value_counts()
    print('Total Counts of user Gender type are {}.'.format(count_user_gender))


    # Display earliest, most recent, and most common year of birth
    birth_year = df['Birth Year'].value_counts()
    if city == 'new york city' or city== 'washington':
        print('Birth Year is not present for this city {}.'.format(city))

    if city == 'chicago':

        print('Earliest, most recent, and most common year of births are "{}", "{}" and "{}" of {}.'.format(birth_year.idxmin(),df['Birth Year'].iloc[0], birth_year.idxmax(),city))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('#'*30)
          
          

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        #orignal_df = pd.read_csv(data[city])
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
