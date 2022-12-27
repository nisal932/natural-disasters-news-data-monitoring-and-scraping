import time

import reuters_ajax
import bbc_ajax
import yaml
import save


"""Function for read data from the yaml"""
def get_yaml_data():
    file = open('config.yaml') # Open the yaml file
    config = yaml.safe_load(file)
    keywords = config['Keywords'] # Save keywords to a list
    return keywords

"""Function for compare news texts and targeted keywords"""
def keywords_validator(keyword_list, news_list): # Targeted keyword list , Scraped news list
    news_contain_target_keywords = {} # Dic for save the news wich contain targeted keywords
    for i in keyword_list:
        news_contain_target_keywords[i] = []
        for j in news_list:
            news_text = news_list[j]
            if i.lower() in news_text.lower(): # 1. Convert all news and targted keywords to simple letters to avoid case sensitivity. 2. check the availability of targeted keywords
                (news_contain_target_keywords[i]).append(j)
    return news_contain_target_keywords # return news wich contains targeted keywords


def main():
    keyword_list = get_yaml_data() # Save yaml keywords to a list
    print('> Program starting...')
    time.sleep(0.5) # Just for clear arangment of the terminal outputs
    print("> Scraping data from BBC")
    bbc_data = bbc_ajax.main() # Call the function for scrap all the news from bbc
    print("BBC Scraping completed!!!")
    print("> Scraping data from REUTERS")
    reuter_data = reuters_ajax.main() # Call the function for scrap all the news from reuters
    print("REUTERS Scraping completed!!!")
    print("> Saving the Data...")
    time.sleep(0.5) # Just for clear arangment of the terminal outputs
    bbc_news = keywords_validator(keyword_list, bbc_data) # Call the function for find the bbc news contains targeted keywords
    reuter_news = keywords_validator(keyword_list,reuter_data) # Call the function for find the reuters news contains targeted keywords
    save.save_to_csv(bbc_news, reuter_news) # Save data using save_to_cv function in the save.py file
    print("Program Completed!!!")



if __name__ == '__main__':
    main()
