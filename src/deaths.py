import pandas as pd

# Dates for filename
# start = "05-01-2021.csv"
# end = "06-30-2021.csv"


def readit(filename):
    # Read CSV while keeping FIPS as a string
    # Base URL for JHU data repo
    base = "https://raw.githubusercontent.com/"
    base += "CSSEGISandData/COVID-19/master/csse_covid_19_data/"
    base += "csse_covid_19_daily_reports/"
    df = pd.read_csv(base + filename, converters={'FIPS': str})
    # df.dropna()  # This doesn't do anything because missing data are not NaN when FIPS is read as a string
    # This eliminates rows without a FIPS (i.e., foreign countries)
    return df[df['FIPS'] != ""]

    """This is a function that returns a dataframe that contain Fips and the death number from start_date to end_date, and create a csv file in data 
    Parameters: 
        start_date:str , write it in form "05-01-2021.csv",
        end_date: str,
    """


def get_death_number_JHU(start, end):
    data = {}

    df_deaths = readit(end)
    for i, row in df_deaths.iterrows():
        fips = row['FIPS']
        data[fips] = row["Deaths"]
    # print(data)
    df_deaths = readit(start)
    for i, row in df_deaths.iterrows():
        fips = row['FIPS']
        data[fips] -= row["Deaths"]

    # Write dictionary to a CSV file
    filename = "data/JHU/deaths-" + \
               start[:2] + '-' + start[3:5] + "-" + start[6:10] + "-to-" + \
               end[:2] + '-' + end[3:5] + "-" + end[6:]

    with open(filename, 'w') as file:
        file.write("FIPS,Deaths\n")  # header
        for key, value in data.items():
            file.write(",".join([key, str(value)]) + "\n")
    df = pd.read_csv(filename)
    return df


# test case 01
# start = "05-01-2021.csv"
# end = "06-30-2021.csv"
# get_JHU_data(start, end)

    """This is a function that returns the confirmed number from start_date to end_date
    Parameters: 
        start_date:str , write it in form "05-01-2021.csv",
        end_date: str,
    """


def get_confirm_number_JHU(start, end):
    data = {}

    df_confirmed = readit(end)
    for i, row in df_confirmed.iterrows():
        fips = row['FIPS']
        if len(fips) == 4:
            fips = "0" + fips
        data[fips] = row["Confirmed"]
    # print(data)
    df_confirmed = readit(start)
    for i, row in df_confirmed.iterrows():
        fips = row['FIPS']
        if len(fips) == 4:
            fips = "0" + fips
        data[fips] -= row["Confirmed"]

    # Write dictionary to a CSV file
    filename = "data/confirmed-" + \
               start[:2] + '-' + start[3:5] + "-" + start[6:10] + "-to-" + \
               end[:2] + '-' + end[3:5] + "-" + end[6:]

    with open(filename, 'w') as file:
        file.write("FIPS,Confirmed\n")  # header
        for key, value in data.items():
            file.write(",".join([key, str(value)]) + "\n")
    df = pd.read_csv(filename)
    print()
    return df


# test case 02
# start = "05-01-2021.csv"
# end = "06-30-2021.csv"
# get_confirm_number_JHU(start, end)

    """This function write death number into 7(month) csv file, each file document death number from 05-01 to the end of this month
    Please create a JHU file in ../data First, Or this function will give error. 
    If you don't want to wast time to input augument to create csv file for every month please run following function
    """


def create_death_number_JHU():
    get_death_number_JHU("05-01-2021.csv", "05-31-2021.csv")
    get_death_number_JHU("05-01-2021.csv", "06-30-2021.csv")
    get_death_number_JHU("05-01-2021.csv", "07-31-2021.csv")
    get_death_number_JHU("05-01-2021.csv", "08-31-2021.csv")
    get_death_number_JHU("05-01-2021.csv", "09-30-2021.csv")
    get_death_number_JHU("05-01-2021.csv", "10-31-2021.csv")
    get_death_number_JHU("05-01-2021.csv", "11-30-2021.csv")


create_death_number_JHU()
