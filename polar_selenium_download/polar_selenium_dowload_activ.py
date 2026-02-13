'Get tcx file from polar.'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from subprocess import getoutput

# set dowload dir
download_dir = "/home/rafatieppo/Downloads/"
# driver = webdriver.Firefox() #driver = webdriver.Chrome()

# firefox snap
options = Options()
options.binary_location = getoutput("find /snap/firefox -name firefox").split("\n")[-1]
driver = webdriver.Firefox(service=Service(
    executable_path=getoutput("find /snap/firefox -name geckodriver").split("\n")[-1]),
                           options=options)

# Login Polar
url = 'https://flow.polar.com/'
driver.get(url)

# Click on the checkbox
u = driver.find_element(By.XPATH, '//*[@id="loginButtonNav"]')
u.click()
u = driver.find_element(By.XPATH, '//*[@id="login"]')
u.click()

# fill login
name = driver.find_element(By.XPATH, '//*[@id="username"]')
name.send_keys('rafaeltieppo@yahoo.com.br')
pw = driver.find_element(By.XPATH, '//*[@id="password"]')
pw.send_keys('your_password')
u = driver.find_element(By.XPATH, '/html/body/div/div/div/form/button[1]')
u.click()

# page with month calendar CHANGE HERE the month
url = "https://flow.polar.com/diary/2025/month/6"
driver.get(url)
# class_name = "event event-month exercise"
# get all elements with activitie in calendar
activ = None
activ = driver.find_elements(
    By.XPATH,
    '//div[@class="event event-month exercise"]')
# activ = driver.find_elements(By.XPATH, '/html/body/div[4]/div[2]/div/div/div/table/tbody/tr[1]/td[1]/div/div/div[1]/div')
print(len(activ))

# create lists with code activities and download link
code_activ_list = []
link_activ_list = []
for idx in range(len(activ)):
    x = activ[idx]
    y = x.find_elements(By.TAG_NAME, 'a')
    link = y[0].get_attribute('href')
    link_activ_list.append(link)
    code_activ = link.split('/')[-1]
    code_activ_list.append(code_activ)

print(code_activ_list)
print(len(code_activ_list))

# set the waiting time load page
driver.set_page_load_timeout(15)

# ------------------------------------------------------------
# dowload ......
# ------------------------------------------------------------

for idx in range(len(code_activ_list)):
    cod = code_activ_list[idx]
    urlpage = 'https://flow.polar.com/training/analysis2/' + cod
    print(idx, urlpage)
    driver.get(url=urlpage)
    # u = driver.find_element(
        # By.XPATH, '/html/body/div/div/div/main/div[2]/div[1]/div/div[1]/div[2]/div[2]')
    # u.click()
    url_download = 'https://flow.polar.com/api/export/training/tcx/' +\
        code_activ_list[idx] + '?compress=false'
    # print(idx, url_download)
    try:
        # driver.timeouts.getPageLoadTimeout(15)
        driver.get(url=url_download)
    except:
        print('pass')


# it is necessary to close the driver to get another month
driver.close()

# ------------------------------------------------------------
# TESTES
# ------------------------------------------------------------
# local geckodriver
# cService = webdriver.ChromeService(executable_path=’C:/Users/MyUsername/Downloads/chromedriver-win64/chromedriver.exe’)
# driver = webdriver.Chrome(service=cService)
# driver = webdriver.Firefox()

# https://flow.polar.com/api/export/training/tcx/8045861429?compress=false
# it did not worked
profile = FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", download_dir)
# add the mime types of the files you want to download without prompt.
profile.set_preference("browser.helperApps.neverAsk.saveToDisk",
                       "application/octet-stream, application/pdf, text/csv, text/plain")
# ensure safebrowsing is enabled.
profile.set_preference("browser.safebrowsing.enabled", True)

options = Options()
options.profile = profile
