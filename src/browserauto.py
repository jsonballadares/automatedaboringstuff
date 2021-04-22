from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://automatetheboringstuff.com')
element = browser.find_element_by_css_selector(
    'body > div.top_header > a:nth-child(2)')
element.click()
browser.close()
