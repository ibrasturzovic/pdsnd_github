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
        city = input("Would you like to see data for Chicago, New York City, or Washington?").lower()
        if city not in CITY_DATA:
            print("The city name you entered is invalid. Please choose a correct city name.")
        else:
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please choose a month between January and June for which you would like to see the data. If you want to see all months just type 'all'.").lower()
        months = ["january", "february", "march", "april", "may", "june"]
        if month != "all" and month not in months:
            print("Invalid month value. Please choose a correct month value.")
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please choose a day of week for which you would like to see the data. If you want to see all days just type 'all'.").lower()
        days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        if day != "all" and day not in days:
            print("You entered an invalid day value. Please choose a correct day value.")
        else:
            break


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
    # INPUT FROM PRACTICE QUESTION #3
    # Load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # This converts the "Start Time" column to datetime
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    # Extract month and day from "Start Time" to create new columns
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.day_name()

    # This is supposed to filter by month (if applicable)
    if month != "all":

        # Use the index of the months list to get the corresponding int
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1

        # Filter by month to create the new dataframe
        df = df[df["month"] == month]

    #Filter by day of week if applicable
    if day != "all":
        # Filter by day of week to create the new dataframe
        df = df[df["day_of_week"] == day.title()]

    return df


def show_raw_data(df):
    """
    Supposed to show subsequent rows of data according to the answer of the user.

    Args:
        Pandas DataFrame which includes city data filtered by month and day being returned from the previous load_data() function.
    """
    i = 0
    user_answer = input("Would you like to see the first 5 rows of data? Please enter 'yes' or 'no': ").lower()
    pd.set_option("display.max_columns", None)

    while True:
        if user_answer == "no":
            break
        print(df[i:i+5])
        user_answer = input("Would you like to see the next 5 rows of data? Please enter 'yes' or 'no': ").lower()
        i+=5


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df["month"].mode()[0]
    print("Most common month: ", common_month)

    # TO DO: display the most common day of week
    common_day = df["day_of_week"].mode()[0]
    print("Most common day: ", common_day)

    # TO DO: display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    common_hour = df["hour"].mode()[0]
    print("Most common hour: ", common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df["Start Station"].mode()[0]
    print("Most commonly used start station: ", common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df["End Station"].mode()[0]
    print("Most commonly used end station: ", common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    common_start_end_station = (df["Start Station"] + "-" + df["End Station"]).mode()[0]
    print("Most frequent combination of start station and end station trip: ", common_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("Total travel time: ", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("Mean travel time: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df["User Type"].value_counts()
    print("Counts of user types: ", user_type)

    # TO DO: Display counts of gender
    if "Gender" in df:
        print("Counts of gender: ", df["Gender"].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        earliest_birth_year = int(df["Birth Year"].min())
        print("Earliest year of birth: ", earliest_birth_year)

        most_recent_birth_year = int(df["Birth Year"].max())
        print("Most recent year of birth: ", most_recent_birth_year)

        most_common_birth_year = int(df["Birth Year"].mode()[0])
        print("Most common year of birth: ", most_common_birth_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        show_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
