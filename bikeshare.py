import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

        
    while True:
        try:
            city= input('Enter a city name from the list chicago, new york city, or washington: ').lower()
            if city == 'washington'or city== 'chicago' or city=='new york city':             
                break
        finally:
            print('\nAttempted Input\n')
   # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month= input('Enter a month from the following list - January, February, March, April, May, June, or All:').lower()
            if month== 'january' or month=='february'or month == 'march'or month=='april'or month == 'may'or month=='june'or month=='all':
                break        
        finally:
                print('\nAttempted Input\n')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        try:
            day= input('Enter a day of the week from the following list - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or All:').lower()
            if day== 'monday' or day=='tuesday'or day == 'wednesday'or day=='thursday'or day == 'friday'or day=='saturday'or day == 'sunday'or day == 'all':
                break        
        finally:
                print('\nAttempted Input\n')
        
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
         
    # TO DO: display the most common month 

    common_month=df['month'].value_counts().nlargest(1)
    print("\nThe most common month is",common_month)


    # TO DO: display the most common day of week

    common_day=df['day_of_week'].value_counts().nlargest(1)
    print("\nThe most common day of the week is",common_day)

    # TO DO: display the most common start hour
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('\nMost Popular Start Hour is:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station=df['Start Station'].value_counts().nlargest(1)
    print("\nThe most commonly used start station is",start_station)

    # TO DO: display most commonly used end station
    end_station=df['End Station'].value_counts().nlargest(1)
    print("\nThe most commonly used end station is",end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Combine'] = df['Start Station'].astype(str)+"-"+df['End Station']
    combine_station=df['Combine'].value_counts().nlargest(1)
    print("\nThe most frequent comination of start station and end station is:",combine_station)

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print("\nTotal travel time is:{} seconds".format(total_travel_time))
    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print("\nMean travel time is:{} seconds".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_type=df['User Type'].value_counts(dropna=True)
    print("\nThe counts of user types are:", count_user_type)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender=df['Gender'].value_counts(dropna=True)
        print("\nThe counts for gender are:", gender)
   

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year=df['Birth Year'].min()
        print("\nThe earliest birth year is", earliest_year)
    if 'Birth Year' in df.columns:
        most_recent_year=df['Birth Year'].max()
        print("\nThe most recent birth year is", most_recent_year)
    if 'Birth Year' in df.columns:
        common_year=df['Birth Year'].value_counts(dropna=True).nlargest(1)
        print("\nThe most common birth year is", common_year)
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def see_data(df):
    
    start=0
    end=5
    total= len(df.index)
    while start<total:
        raw_data= input('Would you like to see 5 lines of raw data? Yes/No: ').lower()
        if raw_data=='yes':
            print(df.iloc[start:end])
            start+=5
            end+=5
        else:
            break
        

def main():
    
    while True:
        city, month ,day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        see_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
        main()

print('Goodbye')
