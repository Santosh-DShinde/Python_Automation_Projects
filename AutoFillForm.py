import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


def FillForm():

    Data = pd.read_excel('TestFile.xlsx', keep_default_na=True)

    s = Service(r"C:\\Users\\ASUS\\Downloads\\chromedriver_win32\\chromedriver.exe")
    web = webdriver.Chrome(service=s)
    web.get(
        "https://docs.google.com/forms/d/e/1FAIpQLSe7ijO8cqPe8Vq38rWAQcEHtstzsHnYuHbJQ6dxx8rEvX16YQ/viewform?vc=0&c=0"
        "&w=1&flr=0")
    time.sleep(2)

    for i in range(len(Data)):

        web.find_element(By.XPATH,
                         value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'). \
            send_keys(
            Data.First_Name[i])

        web.find_element(By.XPATH,
                         value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'). \
            send_keys(
            Data.Middle_Name[i])

        web.find_element(By.XPATH,
                         value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'). \
            send_keys(
            Data.Last_Name[i])

        web.find_element(By.XPATH,
                         value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea'). \
            send_keys(
            Data.MailID[i])

        web.find_element(By.XPATH,
                         value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input'). \
            send_keys(
            str(Data.Number[i]))

        web.find_element(By.XPATH,
                         value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input'). \
            send_keys(
            Data.City[i])

        web.find_element(By.XPATH,
                         value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/div[2]/div['
                               '1]/div/div[1]/input'). \
            send_keys(
            str(Data.DateOfBirth[i]))

        submit = web.find_element(By.XPATH,
                                  value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
        submit.click()

        time.sleep(2)

        SubAnotherForm = web.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')

        SubAnotherForm.click()
        time.sleep(1)

    web.close()


def main():
    FillForm()


if __name__ == '__main__':
    main()
