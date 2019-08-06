
# UndetectableWebDriver
### Selenium Chromedriver which PASSES Distil browser automation test


This is a drop-in replacement for selenium.webdriver.Chrome using optimization and older build of Chromium to bypass all current browser-automation-detection systems, with the most important one being Distill Networks.

### Installation
```shell
pip install git+https://ultrafunkamsterdam/stealthchromedriver.git
```

### Usage
```python

from stealthchromedriver import Chrome

driver = Chrome()
driver.get('https://www.distilnetworks.com')
# now try this using regular selenium chromedriver
```


**with options**
```python

from stealthchromedriver import getDriver
driver = getDriver(headless=False,verify_ssl=False, custom_ua="",profile_directory="Default",prefs=None,language="en")
driver.get('https://distillnetworks.com')

# now try this using regular selenium chromedriver
```


**with custom options**
```python

from stealthchromedriver import Chrome, ChromeOptions

options = ChromeOptions()
options.add_argument('--proxy-server=socks5://127.0.0.1:9050')
options.add_argument('--non-secure')

driver = Chrome(options=options)
driver.get('https://distillnetworks.com')

# now try this using regular selenium chromedriver
```



