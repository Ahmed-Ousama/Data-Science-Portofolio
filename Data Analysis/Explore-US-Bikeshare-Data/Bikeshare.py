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
    city=''
    while city not in CITY_DATA.keys():
        print("\nTo proceed with data retrieving, Please enter a city name")
        print("\nPlease make sure that is the city included in that list")
        print("\n[chicago, new york city,washington ]")

        city = input().lower()
        if city not in CITY_DATA.keys():
            print("\nThere is a problem with your city's name, it may not exist in our data")
            print("\nI will give you another trial but please make sure that is the city included in that list")
            print("\n[chicago, new york city, washington ]")
    

    # TO DO: get user input for month (all, january, february, ... , june)
    #we have to create a dict contains months that the user will enter as a key and the number of that month in th data
    MONTH_DATA = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month= ''
    while month not in MONTH_DATA.keys():
        print("\n Time to know which time range you need your data in it, please enter a valid month or you can choose all months by inserting 'all'")
        print("\nEnter a month from January to June, or all")
        month = input().lower()
        if month not in MONTH_DATA.keys():
            print("\nThere is a problem with your month's name, it may not exist in our data.")
            print("\nI will give you another trial but please make sure that is the city included from January to June")
            print("\nMake sure that you entered a month in its full name, not an abbreviation")
         
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day= ''
    while day not in DAY_DATA:
        print("\nPlease enter a valid day")
        print("\nEnter a day of week like Sunday or you can choose all of them by inserting 'all'")
        day = input().lower()

        if day not in DAY_DATA:
            print("\nwell, it seems that you entered the wrong day but I will give you another try")
            print("\nPlease enter a valid day")
            print("\nEnter a day of week like Sunday or you can choose all of them by inserting 'all'")

    
    print('-'*40)
    print("\nShowing data of{} at month:{} and day:{}".format(city, month, day))

    return city, month, day


def load_data(city, month, day):
  df = pd.read_csv(CITY_DATA[city])
  df['Start Time'] = pd.to_datetime(df['Start Time'])
  df['month'] = df['Start Time'].dt.month
  df['day'] = df['Start Time'].dt.day_name()
  if month != 'all':
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month = months.index(month) + 1
    df = df[df['month'] == month]
  if day != 'all':
    df = df[df['day'] == day.title()]
   

  return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    Highest_count_month = df['month'].mode()[0]
    print("The Most common moth is {}".format(Highest_count_month))


    # TO DO: display the most common day of week
    Highest_count_day = df['day'].mode()[0]
    print("The Most common day is {}".format(Highest_count_day))


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    Highest_counts_hour = df['hour'].mode()[0]
    print("The Most common hour is {}".format(Highest_counts_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Highly_usedstart_station = df['Start Station'].mode()[0]
    print("The Most common used start station is {}".format(Highly_usedstart_station))



    # TO DO: display most commonly used end station
    Highly_usedend_station = df['End Station'].mode()[0]
    print("The Most common used end station is {}".format(Highly_usedend_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['Start.Station To End.Station'] = df['Start Station'].str.cat(df['End Station'], sep='->')
    combo = df['Start.Station To End.Station'].mode()[0]
    print("The Most frequent combination of start station and end station trip is {}".format(combo))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_travel_time = round(df['Trip Duration'].sum())
    print("The total travel time is {}".format(Total_travel_time))


    # TO DO: display mean travel time
    mean_travel_time = round(df['Trip Duration'].mean())
    print("The mean travel time is {}".format(mean_travel_time))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print("The user types unique values counts is {}".format(user_type))


    # TO DO: Display counts of gender

    try:
        gender = df['Gender'].value_counts()
        print(f"\nWell, There is gender data within that file:\n\n{gender}")
    except:
        print("\nUnfortunately, There is no data about gender in this file.")
    

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = int(df['Birth Year'].min())
        most_recent_year = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode()[0])
        print(f"\nThe earliest_year of birth: {earliest_year}\n\nThe most_recent_year of birth: {most_recent_year}\n\nThe most_common_year year of birth:{most_common_year}")
    except:
        print("There are no birth year details in this file.")
    




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data_displaying(df):

    
  answer_responce_LIST = ['yes', 'no']
  responce = ''
  nrow=0
  while responce not in answer_responce_LIST:
      print("\nWell, Would you like to display the data?")
      print("\nInsert Yes for displaying the data and no to close the program")
      responce = input().lower()
      #the raw data from the df is displayed if user opts for it
      if responce == "yes":
          print(df.head())
      elif responce not in answer_responce_LIST:
          print("\nYou didn't insert the right responce")
          print("\nPlease type 'yes' to display data or 'no' to close the program")

  while responce == 'yes':
      print("Do you want me to retrieve more data?")
      print("\nInsert 'yes' for displaying more data or 'no' if you have the data you need")

      nrow += 5
      responce = input().lower()
      if responce == "yes":
            print(df[nrow:nrow+5])
      elif responce != "yes":
            break

  print('-'*80)    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        raw_data_displaying(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
