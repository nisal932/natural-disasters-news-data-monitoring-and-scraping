# natural-disasters-news-data-monitoring-and-scraping
01. main.py
    Introduction
This is the main python file which call each functions both inside and external files (bbc_ajax.py, 
reuters_ajax.py, etc.)
    Functions
1. get_yaml_data()
Load target keyword from the yaml file and return the keywords as an array
2. main()
Main function of the program
Call get_yaml_data function and save keywords as an array
Call two functions (bbc_ajax.main() and reuters_ajax.main()) for scrap all the news from 
both sites.
Pass targeted keyword list and lists of all scaraped news form the each sites to the 
“keywords_validator()” function to find news which contains targeted keywords
3. keywords_validator()
Compare the extracted news and targeted keyword lists and return news which contain 
targeted keywords
02. bbc_ajax.py
Used python “urllib” module to get the HTML of the website
BBC site is powered by AJAX. AJAX is a method to get data from the server without 
refreshing the web browser
I was able to track the required Ajax request links
All the news can scrap with that ajax request links and python “urllib” module
03. reuters_ajax.py
Used python “urllib” module to get the HTML of the website
Reuters site is powered by AJAX. AJAX is a method to get data from the server without 
refreshing the web browser
I was able to track the required Ajax request links
All the news can scrap with that ajax request links and python “urllib” modul