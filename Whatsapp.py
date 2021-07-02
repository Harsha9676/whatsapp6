from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import socket
from selenium import webdriver
from time import sleep, time
from selenium import webdriver
import os
from webdriver_manager.chrome import ChromeDriverManager
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
driver = webdriver.Chrome(ChromeDriverManager().install())
message_text = 'Hi this text is sent through python programm test case please ignore.'

no_of_message = 1

moblie_no_list = [919000503460, 917893989484]


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


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://web.whatsapp.com")
sleep(10)


def send_whatsapp_msg(phone_no, text):
    driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))
    try:
        driver.switch_to_alert().accept()

    except Exception as e:
        pass

    try:
        element_presence(By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]', 30)
        txt_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        global no_of_message
        for x in range(no_of_message):
            txt_box.send_keys(text)
            txt_box.send_keys("\n")

    except Exception as e:
        print("invailid phone no :" + str(phone_no))


def main():
    for moblie_no in moblie_no_list:
        try:
            send_whatsapp_msg(moblie_no, message_text)

        except Exception as e:

            sleep(10)
            is_connected()


if __name__ == '__main__':
    main()
