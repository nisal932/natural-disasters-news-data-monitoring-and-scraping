import urllib.request, json

out = {}
def main():
    page = 0 # page 1 at the begining
    try:
        while page <51:
            # Open the link using urllib request
            with urllib.request.urlopen("https://push.api.bbci.co.uk/batch?t=%2Fdata%2Fbbc-morph-lx-commentary-data-paged%2Fabout%2Fe6369e45-f838-49cc-b5ac-857ed182e549%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F"+str(page)+"%2Fversion%2F1.5.6?timeout=5") as url:
                data = json.load(url) # In this website AJAX data passing as JSON file format. We can load data in JSON format
                results = (data['payload'][0]['body']['results']) # Location for the news list in the JSON file

                for i in results: # Go through all the news for extract the news texts for each news

                    try:
                        title = i['title'] # News title
                    except: title = '' # If title not found
                    try:
                        description = i["summary"] # News description
                    except: description = '' # If news description not found

                    try:
                        link = 'https://www.bbc.com' + i["url"] # Genarate direct URL from the AJAX request URL
                    except: link = ''
                    out[link] = title + ' ' + description # Combine both description and title and save them into the "out" dictionary


            page+=1 # This number should increasing by the 1 accourding to the format of ajax request url

    except: return out # If got error at the end of the oldest news page. Then over the loop and return all the news
    return out # If reach end of the oldest news page without an error
