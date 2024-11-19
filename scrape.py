import selenium.webdriver as webdriver
from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

AUTH = 'brd-customer-hl_90ad161f-zone-scraping_browser1:o9ovfp5r1axg'
SBR_WEBDRIVER = f'https://{AUTH}@brd.superproxy.io:9515'

def scrape_website(website):
    print("Launching chrome browser...")
    
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        print('Connected! Navigating...')
        driver.get(website)
        print('Navigated! Scraping page content...')
        html = driver.page_source
        return html
    
def extract_body_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, 'html.parser')
    
    for scrip_or_style in soup(["script", "style"]):
        scrip_or_style.extract()
        
    clean_body_content = soup.get_text(separator="\n")
    clean_body_content = "\n".join(line.strip() for line in clean_body_content.splitlines() if line.strip())
    return clean_body_content

def split_dom_content(dom_content, max_length = 6000):
    return [
        dom_content[i: i + max_length] for i in range(0, len(dom_content), max_length)
    ]    