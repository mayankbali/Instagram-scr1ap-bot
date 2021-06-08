
#### The functions being used do the following:

- recent_post_links: scrapes the most recent Instagram posts and grabs their urls (can set any number)
- insta_link_details: takes a post url and returns a dictionary with post details, including:
  - link - original url link
  - type - whether it is a photo or video
  - likes/views - count of likes or views for photo or video
  - age - when posted
  - comment - initial comment from poster
  - hashtags - hashtags extracted from comment, via regular expression
  - mentions - mentions extracted from comment, via regular expression

### Quick Start
This works to make a csv file with all of the from insta_scrape.py. 
Installation: Clone this repo and cd into it. Make sure geckodriver the Firefox Selenium Driver is executable in project path.
Edit the make.py file with your desired username. 
Then run `python3 make.py` to compile your CSV. 
