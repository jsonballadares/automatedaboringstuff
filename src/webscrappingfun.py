import bs4
import requests


def get_udemy_course_title(url):
    response = requests.get(url=url)
    response.raise_for_status()
    beautiful_soup = bs4.BeautifulSoup(
        response.text, 'html.parser')
    elements = beautiful_soup.select(
        '#udemy > div.main-content-wrapper > div.main-content > div.paid-course-landing-page__container > div.top-container.dark-background > div > div > div:nth-child(4) > div > div.udlite-text-sm.clp-lead > div.clp-component-render > h1')
    title = elements[0].text.strip()
    return title


#url = "https://www.udemy.com/course/python-for-machine-learning-data-science-masterclass/"
url = "https://www.udemy.com/course/automate/"
print(get_udemy_course_title(url))
