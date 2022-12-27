import pandas # Use pandas to save data to a csv
import datetime # Module for get the date and time now

def save_to_csv(bbc, reuters): # BBC news contain keywords, Reuters news contain keywords
    now = (str(datetime.datetime.now()))[:-7] # Get time now for genarate proper file names for the csv files
    now = now.replace(':', '.') # Edit the format of the time
    df1 = pandas.DataFrame.from_dict(bbc, orient='index') # Genarate pandas data frame from the BBC news dictionary(Don't include index/ID)
    df1 = df1.transpose() # Transpose the data fram(Rows -> Columns and Columns -> Rows)

    df2 = pandas.DataFrame.from_dict(reuters, orient='index') # Genarate pandas data frame from the Reuters news dictionary(Don't include index/ID)
    df2 = df2.transpose()  # Transpose the data fram(Rows -> Columns and Columns -> Rows)


    file_name1 = 'BBC_' + now + '.csv' # Prepare file name string for BBC
    file_name2 = 'REUTERS_' + now + '.csv' # Prepare file name string for REUTERS

    df1.to_csv(file_name1, index=False) # Save data in a new csv for BBC 
    df2.to_csv(file_name2, index=False) # Save data in a new csv for REUTERS

