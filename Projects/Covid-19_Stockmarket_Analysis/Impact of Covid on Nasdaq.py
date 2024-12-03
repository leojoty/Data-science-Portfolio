############################### Instructions #################################
#1. Find the path variable.
#2. Change the path variable to your own file path.
#3. Place file1, file2, file3, file4 in the chosen file path.
#4. Press the green arrow to run the file.
#5. Prepare... to be amazed (or mildly disappointed).

#6. Note: File outputs include PrimaryCorrelation, SecondaryCorrelation,
# PrimaryOutputGroup10, and SecondaryOutputGroup10. The correlation files to 
# review which include the meaningful correlations labeled are CorrelationPrimary
# and CorrelationSecondary.

##############################################################################
#                             Group 10                                       #
##############################################################################

# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

###############################################################################
#           Efficient File Navigation Variables (Flexible directory)          #
###############################################################################
path = 'C:\\Users\\JDK\\School\\Texas Tech\\Classes\\ISQS 6339\\FinalProject\\Group10FinalSubmission\\'
file1 = 'Provisional_COVID-19_Death_Counts_by_Week_Ending_Date_and_State.csv'
file2 = 'stock_data.csv'
file3 = 'United_States_COVID-19_Cases_and_Deaths_by_State_over_Time.csv'
file4 = 'nasdaq_stock_file.csv'
corrfile1 ='PrimaryCorrelation.csv'
corrfile2 = 'SecondaryCorrelation.csv'
outfile = 'PrimaryOutputGroup10.csv'
alternateoutfile = 'SecondaryOutputGroup10.csv'

# Set the display options to show all the columns
pd.set_option('display.max_columns', None)

### Output files for testing purposes
testoutfile1 = 'Test_Covid_States.csv'
testoutfile2 = 'Test_Covid_United_Sates.csv'
testoutfile3 = 'Test_Funeral_Stocks.csv'
testoutfile4 = 'Test_Case_File.csv'
testoutfile5 = 'Test_Nasdaq_File.csv'
testoutfile6 = 'Test_Projectout.csv'
testoutfile7 = 'Test_project1.csv'

#Create State dictionary for translation
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'United States': 'US',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}


###############################################################################
#                Clean & Load Data (Munging)- COVID-19 Data                   #
###############################################################################
dfcovid = pd.read_csv(path+file1, index_col = None)
dfcovid.head()
dfcovid.tail()
dfcovid.info()
dfcovid.describe()
dfcovid.dtypes

#Rename State to State Name
dfcovid = dfcovid.rename(columns={'State':'State Name'})

#Create a new State column and convert State Name to the State abbreviation
dfcovid['State'] = dfcovid['State Name'].map(us_state_abbrev)

### Copy the dataset and slice to remove columns not being used
### Copy allows to maintain original data if needed
dfcovidDrops = dfcovid.drop(columns=['Data as of', 'Start week', 'Group', 'Indicator'])

### Subset limiting to United States data
dfcovidUSonly = dfcovidDrops[dfcovid['State Name'] == 'United States']
dfcovidUSonly.head()
dfcovidUSonly.count()

### Subset removing United States data and limiting to only state data
dfcovidSTonly = dfcovidDrops[dfcovid['State Name'] != 'United States']
dfcovidSTonly.count()
dfcovidSTonly.head()

#Convert New York City to NY so it's counted within NY state
for index, row in dfcovidSTonly.iterrows():
        dfcovidSTonly['State'][(dfcovidSTonly['State Name'] == 'New York City')] = 'NY'

#Drop State Name
dfcovidSTonly = dfcovidSTonly.drop(columns=['State Name'])
   
#Create a Date column then drop End Week
dfcovidSTonly['Date'] = dfcovidSTonly['End Week']
dfcovidUSonly['Date'] = dfcovidUSonly['End Week']
dfcovidSTonly=dfcovidSTonly.drop(columns=['End Week'])
dfcovidUSonly=dfcovidUSonly.drop(columns=['End Week'])

### Convert the 'End Week' object to datetime to create 'Month' column
dfcovidSTonly['Date'] = pd.to_datetime(dfcovidSTonly['Date'])
dfcovidUSonly['Date'] = pd.to_datetime(dfcovidUSonly['Date'])

#Create a Week Number column to act as the primary key to merge
dfcovidSTonly['Week Number'] = dfcovidSTonly['Date'].dt.week 
dfcovidUSonly['Week Number'] = dfcovidUSonly['Date'].dt.week
                                       
### Create column for 'Month' from the datetime 'End Week' value (returns month integer)
dfcovidSTonly['Month'] = pd.DatetimeIndex(dfcovidSTonly['Date']).month
dfcovidUSonly['Month'] = pd.DatetimeIndex(dfcovidUSonly['Date']).month

### Creat column and use the Month Name value from 'Date'
dfcovidSTonly['Month Name'] = pd.DatetimeIndex(dfcovidSTonly['Date']).month_name()
dfcovidUSonly['Month Name'] = pd.DatetimeIndex(dfcovidUSonly['Date']).month_name()

## subset to remove prior to March 2020
dfcovidSTonly = dfcovidSTonly[dfcovidSTonly.Month != 2]
dfcovidSTonly.count()

dfcovidUSonly = dfcovidUSonly[dfcovidUSonly.Month != 2]
dfcovidUSonly.count()
'''
US data has 29 rows and no missing data
Now we have max rows 1537 for States, Date, Week Number, Month, and Month Name
Columns with missing values
    COVID-19 Deaths                             1234
    Total Deaths                                1531
    Pneumonia Deaths                            1375
    Pneumonia and COVID-19 Deaths               1095
    Influenza Deaths                            1090
    Pneumonia, Influenza, or COVID-19 Deaths    1418
    
There are NO missing values for States, Date, Week Number, Month, 
or Month Name, only numerical stats.
 
These must be cleaned. Determined to use ZERO for all NULLS
Example: Alabama has two missing values for Covid deaths
    Average Covid deaths for Alabama is 97.2
    Using the Alabama average for missing adds 194 deaths for Alabama and they
    only show total 3012 so that adds 7% increase.
Example: Alaska only shows one entry for 10 Influenza deaths, and 4 zero values.
    Filling with their average Influenza deaths of 2 per week, the 29 nulls would
    add 58 more deaths.
'''
### Fill the missing values with 0
### Can use fillna applied to the dataframe knowing that only required numerical
### fields contain NULLs and knowing desired outcome is to fill all with ZERO 
dfcovidSTonly.fillna(0,inplace=True)
dfcovidSTonly.count()
'''
Now there are no missing rows

End Week                                    1537
State                                       1537
COVID-19 Deaths                             1537
Total Deaths                                1537
Percent of Expected Deaths                  1537
Pneumonia Deaths                            1537
Pneumonia and COVID-19 Deaths               1537
Influenza Deaths                            1537
Pneumonia, Influenza, or COVID-19 Deaths    1537
Month                                       1537
'''
### Export the cleaned dataset for inspection
### Note: this is not a final project output, this is simply for our own data inspection

### First, sort by State and then End Week
dfcovidSTonly.sort_values(['State','Week Number'], axis=0, ascending=True, inplace=True)
#dfcovidSTonly.to_csv(path+testoutfile1, sep=',', index=False)

dfcovidUSonly.sort_values(['Week Number'], axis=0, ascending=True, inplace=True)
#dfcovidUSonly.to_csv(path+testoutfile2, sep=',', index=False)
### Confirmed correct data, no missing values, correctly filled using '0', 
### correctly sorted
##############################################################################
#                              COVID Data Analysis                           #
##############################################################################
dfcovid.mean()
dfcovid.median()
dfcovid.std()
dfcovid.var()
dfcovid.corr()
#dfcovid.hist()
#pd.plotting.scatter_matrix(dfcovid)

dfcovidSTonly.mean()
dfcovidSTonly.median()
dfcovidSTonly.std()
dfcovidSTonly.var()
dfcovidSTonly.corr()
#dfcovidSTonly.hist()
#pd.plotting.scatter_matrix(dfcovidSTonly)

dfcovidUSonly.mean()
dfcovidUSonly.median()
dfcovidUSonly.std()
dfcovidUSonly.var()
dfcovidUSonly.corr()
#dfcovidUSonly.hist()
#pd.plotting.scatter_matrix(dfcovidUSonly)
###############################################################################
#                   Clean Data (Munging)-Funeral Home Stocks                  #
###############################################################################
dfstocks = pd.read_csv(path+file2, index_col=None)
dfstocks.head()
dfstocks.tail()
dfstocks.info()
dfstocks.describe()
dfstocks.dtypes

# Convert datatype to datetime
dfstocks['Date'] = pd.to_datetime(dfstocks['Date'])

# Create the Month column
dfstocks['Month'] = pd.DatetimeIndex(dfstocks['Date']).month
dfstocks['Month'] = dfstocks['Month'].astype(int)

#Drop first two months pre-COVID
dfstocks = dfstocks[dfstocks.Month > 2]

#Convert to weekly data. This accounts for no trading over the weekends and holidays.
dfstocks = dfstocks.resample('w-sat', label='right', closed = 'right', on='Date').mean().reset_index().sort_values(by='Date')

#Create a Week Number column to act as the primary key to merge
dfstocks['Week Number'] = dfstocks['Date'].dt.week 

# Creating a new categorical column for the Close Column
dfstocks['Closing_Cat'] = 'Bottom 25%'
dfstocks['Closing_Cat'][dfstocks['Close'] > 16] = 'Mid 50%'
dfstocks['Closing_Cat'][dfstocks['Close'] > 21] = 'Top 25%'
dfstocks['Closing_Cat'] = dfstocks['Closing_Cat'].astype('category')

#Generate file output to confirm data
#dfstocks.to_csv(path+testoutfile3, sep=',', index=False)
##############################################################################
#                              Stock Data Analysis                           #
##############################################################################
dfstocks.mean()
dfstocks.median()
dfstocks.std()
dfstocks.var()
dfstocks.corr()
#dfstocks.hist()
#pd.plotting.scatter_matrix(dfstocks)

###############################################################################
#                   Clean Data (Munging)- COVID-19 Case File                  #
###############################################################################
dfcase = pd.read_csv(path+file3, index_col=None)
dfcase.head()
dfcase.tail()
dfcase.info()
dfcase.describe()
dfcase.dtypes

# Rename columns to be used for consistency
dfcase = dfcase.rename(columns={'submission_date':'Date', 'state':'State', 'tot_cases':'Total COVID Cases'})

# Define DF to only be the columns wanted using index
dfcase = dfcase.iloc[:, [0,1,2]]

# Introduce 'Month' column
dfcase['Month'] = pd.DatetimeIndex(dfcase['Date']).month

#Drop first two months pre-COVID
dfcase = dfcase[dfcase.Month > 2]

# Convert datatype to datetime
dfcase['Date'] = pd.to_datetime(dfcase['Date'])

#Create a Week Number column to act as the primary key to merge
dfcase['Week Number'] = dfcase['Date'].dt.week 

#Drop non-state values
dfcase = dfcase.drop(dfcase[dfcase.State.isin(['PW', 'RMI', 'FSM', 'GU','MP'])].index)

dfcase.reset_index(drop=True, inplace=True)

#Convert to weekly data, group, and sort
dfcase = dfcase.groupby(['State','Week Number'])['Total COVID Cases'].sum().reset_index().sort_values(by='Week Number')

#Sort values by date
dfcase.sort_values(['Week Number'], axis=0, ascending=True, inplace=True)

# Output file for testing purposes
#dfcase.to_csv(path+testoutfile4, sep=',', index=False)

##############################################################################
#                              Case Data Analysis                            #
##############################################################################
dfcase.mean()
dfcase.median()
dfcase.std()
dfcase.var()
dfcase.corr()
#dfcase.hist()
#pd.plotting.scatter_matrix(dfcase)

###############################################################################
#                   Clean Data (Munging)- NASDAQ Stock File                   #
###############################################################################
dfnasdaq = pd.read_csv(path+file4, index_col=None)
dfnasdaq.head()
dfnasdaq.tail()
dfnasdaq.info()
dfnasdaq.describe()
dfnasdaq.dtypes

# Convert datatype to datetime
dfnasdaq['Date'] = pd.to_datetime(dfnasdaq['Date'])

#Convert to weekly data, group, and sort
dfnasdaq = dfnasdaq.resample('w-sat', label='right', closed = 'right', on='Date').mean().reset_index().sort_values(by='Date')

#Create a Week Number column to act as the primary key to merge
dfnasdaq['Week Number'] = dfnasdaq['Date'].dt.week 

# Introduce 'Month' column to act as a primary ID to JOIN datasets
dfnasdaq['Month'] = pd.DatetimeIndex(dfnasdaq['Date']).month
dfnasdaq['Month'] = dfnasdaq['Month'].astype(int)

#Drop first two months pre-COVID
dfnasdaq = dfnasdaq[dfnasdaq.Month > 2]

# Creating a new categorical column for the Close Column.
# Used quantile() to determine the 25% quartiles.
dfnasdaq['Closing_Cat'] = 'Bottom 25%'
dfnasdaq['Closing_Cat'][dfnasdaq['Close'] > 2867.3] = 'Mid 50%'
dfnasdaq['Closing_Cat'][dfnasdaq['Close'] > 3247.2] = 'Top 25%'
dfnasdaq['Closing_Cat'] = dfnasdaq['Closing_Cat'].astype('category')

# Output file for testing purposes
#dfnasdaq.to_csv(path+testoutfile5, sep=',', index=False)
##############################################################################
#                             NASDAQ Data Analysis                           #
##############################################################################
dfnasdaq.mean()
dfnasdaq.median()
dfnasdaq.std()
dfnasdaq.var()
dfnasdaq.corr()
#dfnasdaq.hist()
#pd.plotting.scatter_matrix(dfnasdaq)

###############################################################################
#                   Merge Files into New Data Frames & Munge                  #
###############################################################################
dfproject = dfcovidSTonly.merge(dfcase, how='left', on=['State', 'Week Number'])

#Munge data in dfproject
dfproject.info()
dfproject.head()
dfproject.tail()
dfproject.count()
dfproject.describe()
dfproject.dtypes

# Output file for testing purposes
#dfproject.to_csv(path+testoutfile6, sep=',', index=False)

#Merge into second data set
dfproject1 = dfproject.merge(dfstocks, how='left', on='Week Number')

#Munge necessary data
dfproject1.info()
dfproject1.head()
dfproject1.tail()
dfproject1.info()
dfproject1.describe()
dfproject1.dtypes

# Output file for testing purposes
#dfproject.to_csv(path+testoutfile7, sep=',', index=False)

#Merge into final data set
dfprojectfinal = dfproject1.merge(dfnasdaq, how='left', on='Week Number')
dfprojectfinal = dfprojectfinal.drop(columns=['Date_x','Date_y','Month_x','Month_y'])

dfprojectfinal.info()
dfprojectfinal.head()
dfprojectfinal.tail()
dfprojectfinal.info()
dfprojectfinal.describe()
dfprojectfinal.dtypes

#Generate final file output
dfprojectfinal.to_csv(path + outfile, sep=',', index=False)

### Merge files for secondary output not otherwise available through main merge
StockX = dfstocks.merge(dfnasdaq, how='left', on='Week Number')
dfprojectX = dfcovidUSonly.merge(StockX, how='left', on='Week Number')
dfprojectX = dfprojectX.drop(columns=['Date_x','Date_y','Month_x','Month_y'])
### Munge data in dfproject
dfprojectX.info()
dfprojectX.head()
dfprojectX.tail()
dfprojectX.info()
dfprojectX.describe()
dfprojectX.dtypes
### Output file for Alternative Analysis
dfprojectX.to_csv(path+alternateoutfile, sep=',', index=False)

###############################################################################
#              Correlation & Graphical Analysis of Primary DF                 #
###############################################################################
correlation1 = dfprojectfinal.corr()
correlation1.to_csv(path + corrfile1)

sns.heatmap(correlation1, xticklabels=correlation1.columns, yticklabels=correlation1.columns, annot=False)

###############################################################################
#            Correlation & Graphical Analysis of Sceondary DF                 #
###############################################################################
correlation2 = dfprojectX.corr()
correlation2.to_csv(path + corrfile2)

##############################################################################
#Demonstration of the inverse relationship of CSV Stock prices and COVID Deaths.
# Subplot for Plotting Figure
fig, ax1 = plt.subplots()  

# Similar to fig=plt.figure(figsize=(12,6))
fig.set_figwidth(12)
fig.set_figheight(6)

# set x label which is common
ax1.set_xlabel('Date')

# bottom= false disables ticks and labelbottom disables x-axis labels
# True will enable ticks and labels.
ax1.tick_params(axis = 'x',
                    bottom=True,
                    labelbottom=True) 

# set left y-axis label
ax1.set_ylabel('COVID-19 Deaths', 
                    color='red',
                    size='x-large')

# set labelcolor and labelsize to the left Y-axis
ax1.tick_params(axis='y', 
                     labelcolor='red', 
                     labelsize='large')

# plot on Y-axis to the left 
ax1.plot(dfprojectX['Date'], 
              dfprojectX['COVID-19 Deaths'], 
              color='red')

# twinx sets the same x-axis for both plots 
ax2 = ax1.twinx()

#set Right y-axis label
ax2.set_ylabel('CSV Stock Highs', 
                     color='blue', 
                     size='x-large') 

# set labelcolor and labelsize to the Right Y-axis
ax2.tick_params(axis='y', 
                      labelcolor='blue',
                      labelsize='large')

# plot on Y-axis to the Right 
ax2.plot(dfprojectX['Date'], 
         dfprojectX['High_x'], 
         color='blue')

plt.show()
##############################################################################
#This demonstrates how NASDAQ also continued to increase.
# Subplot for Plotting Figure
fig, ax1 = plt.subplots()  

# Similar to fig=plt.figure(figsize=(12,6))
fig.set_figwidth(12)
fig.set_figheight(6)

# set x label which is common
ax1.set_xlabel('Date')

# bottom= false disables ticks and labelbottom disables x-axis labels
# True will enable ticks and labels.
ax1.tick_params(axis = 'x',
                    bottom=True,
                    labelbottom=True) 

# set left y-axis label
ax1.set_ylabel('COVID-19 Deaths', 
                    color='red',
                    size='x-large')

# set labelcolor and labelsize to the left Y-axis
ax1.tick_params(axis='y', 
                     labelcolor='red', 
                     labelsize='large')

# plot on Y-axis to the left 
ax1.plot(dfprojectX['Date'], 
              dfprojectX['COVID-19 Deaths'], 
              color='red')

#ax1.legend(0)

# twinx sets the same x-axis for both plots 
ax2 = ax1.twinx()

#set Right y-axis label
ax2.set_ylabel('NASDAQ Highs', 
                     color='blue', 
                     size='x-large') 

# set labelcolor and labelsize to the Right Y-axis
ax2.tick_params(axis='y', 
                      labelcolor='blue',
                      labelsize='large')

# plot on Y-axis to the Right 
ax2.plot(dfprojectX['Date'], 
         dfprojectX['High_y'], 
         color='blue')

plt.show()
##############################################################################

