import pandas as pd
import urllib.request
from collections import Counter
from insta_scrape import recent_post_links, insta_link_details 
outlook_urls = recent_post_links('indiancricketteam', post_count=10)
print(outlook_urls)
outlook_details = [insta_link_details(url) for url in outlook_urls]
outlook = pd.DataFrame(outlook_details)
outlook.head()
outlook.to_csv('csv/outlook_insta.csv')
