import bs4
import requests
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import os
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def download_image(url, folder_name, num):

    # write image to file
    response = requests.get(url)
    if response.status_code==200:
        with open(os.path.join(folder_name, str(num)+".jpg"),'wb') as file:
            file.write(response.content)

# creating a directory to save images
folder_name = 'brad_pitt' 
if not os.path.isdir(folder_name):
    os.makedirs(folder_name)

chromeDriverPath = 'E:/DataScience/Scraping_Projects/chromedriver-win64/chromedriver-win64/chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service = Service(executable_path=chromeDriverPath)

driver = webdriver.Chrome(options=options,service=service)

# https://www.google.com/search?sca_esv=562253820&rlz=1C1ONGR_enGB1010GB1011&hl=en&sxsrf=AB5stBjSSF0NF6cbbpRB1i7N3sp2gJOQNA:1693703655314&q=chris+hemsworth&tbm=isch&source=lnms&sa=X&ved=2ahUKEwjK9urloY2BAxUmUEEAHe66D-UQ0pQJegQIDRAB&biw=1366&bih=661&dpr=1
# https://www.google.com/search?q=leonardo+dicaprio&tbm=isch&ved=2ahUKEwiq2__moY2BAxUNzKQKHV6sCbwQ2-cCegQIABAA&oq=leo&gs_lcp=CgNpbWcQARgAMgQIIxAnMgoIABCKBRCxAxBDMgcIABCKBRBDMgoIABCKBRCxAxBDMgcIABCKBRBDMg0IABCKBRCxAxCDARBDMgcIABCKBRBDMgcIABCKBRBDMgcIABCKBRBDMgcIABCKBRBDOgUIABCABDoICAAQgAQQsQNQp5MeWI6bHmDwpx5oAnAAeACAAfEHiAHND5IBCzEuMC4xLjIuNy0xmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=6d3zZOrCLY2YkwXe2KbgCw&bih=661&biw=1366&rlz=1C1ONGR_enGB1010GB1011&hl=en
# https://www.google.com/search?q=dwayane+johnson&tbm=isch&ved=2ahUKEwi_uOeKpI2BAxWMmicCHQvSBdoQ2-cCegQIABAA&oq=dwayane&gs_lcp=CgNpbWcQARgAMgUIABCABDIFCAAQgAQyCQgAEBgQgAQQCjIJCAAQGBCABBAKMgkIABAYEIAEEAoyCQgAEBgQgAQQCjIJCAAQGBCABBAKMgkIABAYEIAEEAoyCQgAEBgQgAQQCjIJCAAQGBCABBAKOgQIIxAnOgoIABCKBRCxAxBDOgcIABCKBRBDOggIABCABBCxAzoGCAAQBRAeOgcIABAYEIAEUMHORViP2kVgnOVFaAJwAHgAgAH2A4gBoAmSAQc3LjEuNS0xmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=TeDzZP_dK4y1nsEPi6SX0A0&bih=661&biw=1366&rlz=1C1ONGR_enGB1010GB1011&hl=en
# https://www.google.com/search?q=will+smith&tbm=isch&ved=2ahUKEwjwgNHUrY2BAxVsvicCHQ0cB3oQ2-cCegQIABAA&oq=will+&gs_lcp=CgNpbWcQARgAMgQIIxAnMg0IABCKBRCxAxCDARBDMgcIABCKBRBDMgoIABCKBRCxAxBDMgcIABCKBRBDMgcIABCKBRBDMgoIABCKBRCxAxBDMgcIABCKBRBDMgUIABCABDIICAAQgAQQsQNQugtYtRNgih1oAHAAeACAAZECiAHpB5IBBTMuMC4zmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=WOrzZPD0G-z8nsEPjbic0Ac&bih=661&biw=1366&rlz=1C1ONGR_enGB1010GB1011&hl=en
# https://www.google.com/search?q=brad+pitt&tbm=isch&ved=2ahUKEwjR0dfYw42BAxXgpCcCHd1cAtwQ2-cCegQIABAA&oq=brad+&gs_lcp=CgNpbWcQARgAMgQIIxAnMgcIABCKBRBDMgoIABCKBRCxAxBDMgcIABCKBRBDMgoIABCKBRCxAxBDMgcIABCKBRBDMgcIABCKBRBDMgoIABCKBRCxAxBDMgcIABCKBRBDMgcIABCKBRBDOggIABCABBCxAzoFCAAQgARQwwpYrhBgpxpoAHAAeACAAdIBiAGYBZIBBTQuMS4xmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=cgH0ZNHQIODJnsEP3bmJ4A0&bih=661&biw=1366&rlz=1C1ONGR_enGB1010GB1011&hl=en

search_URL = "https://www.google.com/search?q=brad+pitt&tbm=isch&ved=2ahUKEwjR0dfYw42BAxXgpCcCHd1cAtwQ2-cCegQIABAA&oq=brad+&gs_lcp=CgNpbWcQARgAMgQIIxAnMgcIABCKBRBDMgoIABCKBRCxAxBDMgcIABCKBRBDMgoIABCKBRCxAxBDMgcIABCKBRBDMgcIABCKBRBDMgoIABCKBRCxAxBDMgcIABCKBRBDMgcIABCKBRBDOggIABCABBCxAzoFCAAQgARQwwpYrhBgpxpoAHAAeACAAdIBiAGYBZIBBTQuMS4xmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=cgH0ZNHQIODJnsEP3bmJ4A0&bih=661&biw=1366&rlz=1C1ONGR_enGB1010GB1011&hl=en"
driver.get(search_URL)

a = input("Waiting for user input to start...")

# Scrolling all the way up
driver.execute_script("window.scrollTo(0,0);")

page_html = driver.page_source
pageSoup = bs4.BeautifulSoup(page_html,'html.parser')
containers = pageSoup.findAll('div',{'class':"isv-r PNCib MSM1fd BUooTd"})

len_containers = len(containers)
print('Found %s image containers'%(len_containers))

#//*[@id="islrg"]/div[1]/div[1]
#//*[@id="islrg"]/div[1]/div[2]
#//*[@id="islrg"]/div[1]/div[3]

# //*[@id="islrg"]/div[1]/div[51]/div[25]
# //*[@id="islrg"]/div[1]/div[51]/div[50]
# //*[@id="islrg"]/div[1]/div[51]/div[75]

#driver.find_element("xpath", """//*[@id="islrg"]/div[1]/div[1]""").click()

for i in range(1,len_containers+1):
    if i % 25 == 0:
        continue

   
    xPath = """//*[@id="islrg"]/div[1]/div[%s]"""%(i)

    # Grabbing the URL of small preview images
    try:
        previewImageXPath = """//*[@id="islrg"]/div[1]/div[%s]/a[1]/div[1]/img"""%(i)
        previewImageElement = driver.find_element("xpath",previewImageXPath)
        previewImageURL = previewImageElement.get_attribute("src")
       
    except:
        continue
        

    # Clicking on the image container
    driver.find_element("xpath",xPath).click()

    # Starting a while True loop to wait until we get the URL inside the large image view is different from the preview one
    timeStarted = time.time()
    while True:
            # //*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1] full res image
        imageElement = driver.find_element("xpath",
                                            """//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]""")
        imageURL = imageElement.get_attribute("src")

        print("Waiting for full res image...")
        if imageURL!=previewImageURL:
        # print("Full res URL",imageURL)
            break
        else:
            # making a timeout if the full resolution image can't be loaded
            currentTime = time.time()

            if currentTime - timeStarted>10:
                print("Timeout! Will download a lower resolution image and move onto the next one")
                break

    # Downloading image
    try:
        download_image(imageURL,folder_name, i)
        print("Downloaded element %s out of %s total. URL:%s"%(i,len_containers+1,imageURL))
    except:
        print("Failed to download an image %s, continuing downloading the next one"%(i))

driver.quit()
