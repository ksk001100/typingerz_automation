from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def click_wait_xpath(driver, wait_xpath, click_xpath):
    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, wait_xpath)))
    driver.find_element_by_xpath(click_xpath).click()


def hoge(driver):
    wait = WebDriverWait(driver, 30)
    wait_visibility_xpath = lambda xpath: wait.until(
        EC.visibility_of_element_located((By.XPATH, xpath)))
    body_send_keys = lambda keys: driver.find_element_by_tag_name(
        'body').send_keys(keys)

    wait_visibility_xpath('/html/body/div[2]/div/div/div[2]/div[2]/a').click()
    wait_visibility_xpath(
        '/html/body/div[4]/div/div/div/main/div/div[1]/a').click()
    wait_visibility_xpath(
        '/html/body/div[4]/div/div/div[8]/main/div/div[1]/div[2]/div/a').click(
        )
    wait_visibility_xpath(
        '/html/body/div[5]/div/div[14]/div/div[4]/div/main/div/canvas')

    while not driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[3]/div[5]').is_displayed():
        body_send_keys(Keys.SPACE)

    driver.find_element_by_xpath('/html/body/div[5]/div/div[3]/div[5]').click()

    while not driver.find_element_by_xpath(
            '//*[@id="startfield"]').is_displayed():
        body_send_keys(Keys.SPACE)

    body_send_keys('s')

    while True:
        while not driver.find_element_by_xpath(
                '//*[@id="youwin"]').is_displayed():
            wait_visibility_xpath('//*[@id="mondaifield"]/font')
            send_strings = driver.find_element_by_xpath(
                '//*[@id="mondaifield"]/font').text
            driver.find_element_by_tag_name('body').send_keys(send_strings)

        body_send_keys('n')

        while not driver.find_element_by_xpath(
                '//*[@id="startfield"]').is_displayed():
            body_send_keys(Keys.SPACE)

        wait_visibility_xpath('//*[@id="startfield"]')
        time.sleep(2)
        body_send_keys('s')


def online_battle(driver):
    wait = WebDriverWait(driver, 30)
    wait_visibility_xpath = lambda xpath: wait.until(
        EC.visibility_of_element_located((By.XPATH, xpath)))
    body_send_keys = lambda keys: driver.find_element_by_tag_name(
        'body').send_keys(keys)

    wait_visibility_xpath('/html/body/div[2]/div/div/div[2]/div[1]/a')
    driver.find_element_by_xpath('//*[@id="menu"]/li[4]/a').click()

    wait_visibility_xpath(
        '/html/body/div[4]/div/div[2]/div[8]/main/div/div[1]/div[1]/a').click(
        )

    wait_visibility_xpath('/html/body/div[5]/div/div[2]/div[5]').click()

    wait_visibility_xpath('//*[@id="battleNickname"]')
    nickname_input = driver.find_element_by_xpath(
        '//*[@id="battleNickname"]').send_keys('ksk001100')
    driver.execute_script('nameTouroku()')

    wait_visibility_xpath('//*[@id="handi1"]/fieldset/p')
    body_send_keys(Keys.ENTER)

    wait_visibility_xpath('//*[@id="startfield"]/span')
    body_send_keys(Keys.ENTER)

    wait_visibility_xpath('//*[@id="startfield"]')
    body_send_keys('s')

    while True:
        try:
            wait_visibility_xpath('//*[@id="mondaifield"]/font')
            send_strings = driver.find_element_by_xpath(
                '//*[@id="mondaifield"]/font').text
            driver.find_element_by_tag_name('body').send_keys(send_strings)
        except:
            break


def main():
    driver_path = './chromedriver'
    driver = webdriver.Chrome(driver_path)
    driver.get('https://typingerz.com/')
    #online_battle(driver)
    hoge(driver)
    input()
    #driver.close()
    #driver.quit()


if __name__ == '__main__':
    main()
