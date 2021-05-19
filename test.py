from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def main():
    open()
    browse()
    close()

def open():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    global driver
    driver = webdriver.Chrome(chrome_options=chrome_options)
    URL = 'http://www.facebook.com/'
    driver.get(URL)


def browse():
    print(driver.title)
    return driver.title


def close():
    driver.close()

if __name__ == '__main__':
    main()
