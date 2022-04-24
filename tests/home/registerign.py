from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
from selenium.webdriver.common.by import By

def generate_unique_email():
    number = random.randint(0, 999999)
    random_email = 'paw.kuznik' + '+' + str(number) + '@gmail.com'
    print(random_email)
    return random_email

email = 'paw.kuznik+99@gmail.com'
password = '123456'

driver = webdriver.Chrome()
driver.get("http://34.118.71.117/")

def registerign_with_random_email(context):
    #Znajdowanie przycisku My account i klikanie w niego
    context.driver.find_element(By.XPATH, "//*[contains(@class, 'focus')]//a[text()='My account']").click()

    #Znajdowanie pola do wpisywanie maila i wprowadzanie logowo wygenerowanego adresu
    context.driver.find_element(By.XPATH, "//*[contains(@class, 'nav-menu')]//a[text()='My account']").send_keys(generate_unique_email())

    #Znajdowanie przycisku register i klikanie w niego
    context.driver.find_element(By.XPATH, "//button[text()='Register']").click()

def registerign_as_allready_registered_user(context):
    #Znajdowanie przycisku My account i klikanie w niego
    context.driver.find_element(By.XPATH, "//*[contains(@class, 'focus')]//a[text()='My account']").click()

    #Znajdowanie pola do wpisywanie maila i wprowadzanie maila który już istnieje w systemie
    context.driver.find_element(By.XPATH, "//*[contains(@class, 'nav-menu')]//a[text()='My account']").send_keys(email())

    #Znajdowanie przycisku register i klikanie w niego
    context.driver.find_element(By.XPATH, "//button[text()='Register']").click()