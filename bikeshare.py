import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#the type of CITY_DATA is dict
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while #loop to handle invalid inputs
    city_list = ["chicago", "new york city", "washington"]
    month_list = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    day_list = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    i = 0
    j = 0
    k = 0
    city = city_list[i]
    month = month_list [j]
    day = day_list[k]


    question = input('\nWhich city do you want to looking for?\n')
    while question.lower() == city_list[i]:
        print('City: {}'.format(city_list[i]))
        i += 1



    # TO DO: get user input for month (all, january, february, ... , june)

    question = input('\nWhich month do you want to looking for?\n')
    while question.lower() == month_list[j]:
        print('Month: {}'.format(month_list[j]))
        j += 1


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    question = input('\nWhich day of week do you want to looking for?\n')
    while question.lower() == day_list[k]:
        print('Day of Week: {}'.format(day_list[k]))
        k += 1

#    print('-'*40)
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
    df = pd.read_csv(CITY_DATA[city])

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
    common_month = df['month'].mode()[0]
    print('Most Common Month: {}'.format(common_month))


    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most Common Day: {}'.format(common_day))


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print('Most Common Start Hour: {}'.format(common_start_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    count_start_station = df.groupby(['Start Station']).size()
    most_common_start_station = max(count_start_station.index)
    print('Most Common Start Station: ', most_common_start_station)


    # TO DO: display most commonly used end station
    count_end_station = df.groupby(['End Station']).size()
    most_common_end_station = max(count_end_station.index)
    print('Most Common End Station: ', most_common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    count_combination = df.groupby(['Start Station', 'End Station']).size()
    most_frequent_trip_route = max(count_combination.index)
    print('Most Frequent Combination of Start and End Station is {}'.format(most_frequent_trip_route))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    start_travel_time = pd.to_datetime(df['Start Time'])
    end_time = pd.to_datetime(df['End Time'])
    total_duration = end_time - start_travel_time
    print('Total travel time is: {}'.format(total_duration))


    # TO DO: display mean travel time
    mean_travel_time = total_duration.mean()
    print('Mean Travel Time is: {}'.format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_type = df['User Type'].value_counts()
    print('The number of User Type: {}'.format(count_user_type))


    # TO DO: Display counts of gender
    count_gender = df['Gender'].value_counts()
    print('Gender Counts: {}'.format(count_gender))



    # TO DO: Display earliest, most recent, and most common year of birth
    most_earliest = df['Birth Year'].min()
    print('The Most Earliest Year of Birth: ', most_earliest)
    most_recent = df['Birth Year'].max(0)
    print('The Most Recent Year of Birth: ', most_recent)
    most_common = df['Birth Year'].mode()[0]
    print('The Most Common Year of Birth: ', most_common)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

     view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while view_data.lower() != 'no':
        print(df.iloc[0:5])
        start_loc += 5
        view_display = input('Do you wish to continue?: ').lower()
        break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
#As long as you click 'yes', the process is continously repeated

if __name__ == "__main__":
	main()
