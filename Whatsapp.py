#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import socket
import pandas

excel_data = pandas.read_excel('E:\\Selinium\\Customer data.xlsx', sheet_name='Customers')
count=0
message_text = excel_data['Message']
no_of_message = 1
#mobile_no_list = excel_data['Contact'].tolist()

def element_presence(by, xpath, time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)

def is_connected():
    try:
        # connect to the host -- tells us if the host is actually reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except BaseException:
        is_connected()


driver = webdriver.Chrome('E:\Selinium\SeleniumBasic-2.0.9.0\chromedriver.exe')
driver.get("http://web.whatsapp.com")
#driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(Contact))


def send_whatsapp_msg(phone_no, text):
    driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))

    try:
        driver.switch_to_alert().accept()

    except Exception as e:
        pass

    try:
        element_presence(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]',30)
        txt_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        global no_of_message
        for x in range(no_of_message):

            txt_box.send_keys(text)
            txt_box.send_keys("\n")

    except Exception as e:
        print("invailid phone no :" + str(phone_no))

        
def main():
    for column in excel_data['Contact'].tolist():
        try:
            send_whatsapp_msg(column, message_text)

        except Exception as e:

            sleep(10)
            is_connected()

if __name__ == '__main__':
    main()

