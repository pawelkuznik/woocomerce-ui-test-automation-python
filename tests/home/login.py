from selenium import webdriver
from selenium.webdriver.common.by import By
from .registerign import generate_unique_email
import random
email = 'paw.kuznik+99@gmail.com'
password = '123456'

driver = webdriver.Chrome()
driver.get("http://34.118.71.117/")

def generate_unique_password():
        number = random.randint(0, 999999)
        random_password = 'Qwerty1234' + '+' + str(number)
        print(random_password)
        return random_password


def LogIn_as_existing_user(context):
    #Znajdowanie przycisku My account i klikanie w niego
    context.driver.find_element(By.XPATH, "//*[contains(@class, 'focus')]//a[text()='My account']").click()

    #Znajdowanie pola do wprowadzania emaila i wpisywanie emaila stworzonego już użytkownika
    context.driver.find_element(By.XPATH, "//*[@id='username']").send_keys(email)

    #Znajdowanie pola do wprowadzania hasła i wprowadzania hasła do już istniejącego konta
    context.driver.find_element(By.XPATH, "//*[@id='password']").send_keys(password)

    #klikanie w przycisk Log in
    context.driver.find_element(By.XPATH, "//button[text()='Log in']").click()

def LogIn_with_invalid_data(context):
    #Znajdowanie przycisku My account i klikanie w niego
    context.driver.find_element(By.XPATH, "//*[contains(@class, 'focus')]//a[text()='My account']").click()

    #Znajdowanie pola do wprowadzania emaila i wprowadzanie maila do nieistniejącego użytkownika
    context.driver.find_element(By.XPATH, "//*[@id='username']").send_keys(generate_unique_email())

    # Znajdowanie pola do wprowadzania hasła i wprowadzania hasła do już istniejącego konta
    context.driver.find_element(By.XPATH, "//*[@id='password']").send_keys(generate_unique_password())

