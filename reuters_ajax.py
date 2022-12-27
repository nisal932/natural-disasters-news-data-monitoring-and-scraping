import urllib.request, json

out = {}
def main():
    page = 0 # page 1 at the begining
    while True:
        try:
            # AJAX link
            current_page = 'https://www.reuters.com/pf/api/v3/content/fetch/articles-by-section-alias-or-id-v1?query={"arc-site":"reuters","called_from_a_component":true,"fetch_type":"collection","offset":'+str(page)+',"section_id":"/business/environment/","size":20,"sophi_page":"*","sophi_widget":"topic","website":"reuters"}&d=123&_website=reuters'
            with urllib.request.urlopen(current_page) as url: # Open the link using urllib request
                data = json.load(url) # In this website AJAX data passing as JSON file format. We can load data in JSON format 
                results = (data['result']['articles']) # Location for the news list in the JSON file
                for i in results: # Go through all the news for extract the news texts for each news
                    try:
                        title = i['title'] # News title
                    except: title = '' # If title not found

                    try:
                        description = i['description'] # News description
                    except: description = '' # If news description not found

                    try:
                        link = 'https://www.reuters.com' + i['canonical_url'] # Genarate direct URL from the AJAX request URL
                    except: link = ''

                    out[link] = title + ' ' + description # Combine both description and title and save them into the "out" dictionary
            page += 21 # This number should increasing by the 21 accourding to the format of ajax request url
        except:
            return out # There should be an error at the end of the oldest news page. Then over the loop and return all the news


