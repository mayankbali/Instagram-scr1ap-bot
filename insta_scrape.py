import time
import re
import urllib
from selenium.webdriver.chrome.options import Options

from selenium import webdriver
from selenium.webdriver import Chrome


#driver= webdriver.Chrome(executable_path = 'C:\Users\mayan\Desktop\Mayank\MBA Folder\trimester 3\web_scraping_corgis-master\chromedriver.exe')

def recent_post_links(username, post_count=10):
    
    url = "https://www.instagram.com/" + username + "/"
    browser = Chrome()
    browser.get(url)
    post = 'https://www.instagram.com/p/'
    post_links = []
    while len(post_links) < post_count:
        links = [a.get_attribute('href')
                 for a in browser.find_elements_by_tag_name('a')]
        for link in links:
            if post in link and link not in post_links:
                post_links.append(link)
        scroll_down = "window.scrollTo(0, document.body.scrollHeight);"
        browser.execute_script(scroll_down)
        time.sleep(10)
    else:
        browser.stop_client()
        return post_links[:post_count]




def find_mentions_or_hashtags(comment, pattern):
    mentions = re.findall(pattern, comment)
    if (len(mentions) > 1) & (len(mentions) != 1):
        return mentions
    elif len(mentions) == 1:
        return mentions[0]
    else:
        return ""


def insta_link_details(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    browser = Chrome(options=chrome_options)
    browser.get(url)
    try:
        # This captures the standard like count.
        likes = browser.find_element_by_xpath(
            """/html/body/div[5]/div[2]/div/article/div[3]/section[2]/div/div/a""").text.split()[0]
        post_type = 'photo'
    except:
        # This captures the like count for videos which is stored
        likes = browser.find_element_by_xpath(
            """/html/body/div[5]/div[2]/div/article/div[3]/section[2]/div/div/a""").text.split()[0]
        '''post_type = 'video'
    age = browser.find_element_by_css_selector('a time').text
    comment = browser.find_element_by_xpath(
        """/html/body/div[5]/div[2]/div/article/div[3]/div[1]""").text'''

    hashtags = find_mentions_or_hashtags(comment, '#[A-Za-z]+')
    mentions = find_mentions_or_hashtags(comment, '@[A-Za-z]+')
    post_details = {'link': url, 'type': post_type, 'likes/views': likes,
                    'age': age, 'comment': comment, 'hashtags': hashtags,
                    'mentions': mentions}
    time.sleep(10)
    return post_details



'''def insta_url_to_img(url, filename="insta.jpg"):
    """
    Getting the actual photo file from an Instagram url

    Args:
    url: Instagram direct post url
    filename: file name for image at url

    Returns:
    image file, saved locally
    """
    firefox_options = Options()
    firefox_options.add_argument("--headless")
    browser = Firefox(firefox_options=firefox_options)
    browser.get(url)
    try: 
        image = browser.find_element_by_xpath(
            """/html/body/span/section/main/div/div/article/
                div[1]/div/div/div[1]/div[1]/img""").get_attribute('src').split(' ')[0]
        urllib.request.urlretrieve(image, filename)
    # If image is not a photo, print notice
    except:
        print("No image")'''