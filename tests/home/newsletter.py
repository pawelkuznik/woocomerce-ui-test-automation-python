from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
from selenium.webdriver.common.by import By
from .login import LogIn_as_existing_user
from .registerign import generate_unique_email

#SPRAWDZANIE MOŻLIWOŚCI ZAPISYWANIA DO NEWSLETTERA TESTUJĄC WARTOŚCI BRZEGOWE

driver = webdriver.Chrome()
driver.get("http://34.118.71.117/")

#zapisywanie sie do newsletera uzupełanijąc wszystkie wymagane informacje
def newsletter_subscribe(context):
    #klikanie w newsletter
    context.driver.find_element(By.XPATH, "//*[contains(@class, 'focus')]//a[text()='Newsletter']").click()
    #wprowadzanie imienia
    context.driver.find_element(By.XPATH, "//*[@id='tnp-1']").send_keys("JanNowak")
    #wprowadzanie maila
    context.driver.find_element(By.XPATH, "//*[@id='tnp-2']").send_keys("generate_unique_email")
    #akteptowanie privaCy policy
    context.driver.find_element(By.XPATH, "//*[@name='ny']").clicl()
    #klikanie w Subscribe
    context.driver.find_element(By.XPATH, "//*[contains(@class, 'tnp-field-button')]//*[contains(@class, 'tnp-submit')]").clicl()

#zapisywanie się do newslettera nie zaznaczająć polityki prywatności
def newsletter_subscribe_no_privacy(context):
    #klikanie w newsletter
    context.driver.find_element(By.XPATH, "//*[contains(@class, 'focus')]//a[text()='Newsletter']").click()
    #wprowadzanie imienia
    context.driver.find_element(By.XPATH, "//*[@id='tnp-1']").send_keys("JanNowak")
    #wprowadzanie maila
    context.driver.find_element(By.XPATH, "//*[@id='tnp-2']").send_keys("generate_unique_email")
    #klikanie w Subscribe
    context.driver.find_element(By.XPATH, "//*[contains(@class, 'tnp-field-button')]//*[contains(@class, 'tnp-submit')]").clicl()


# zapisywanie sie do newsletera nie wpisując imienia
def newsletter_subscribe_no_name(context):
    # klikanie w newsletter
    context.driver.find_element(By.XPATH, "//*[contains(@class, 'focus')]//a[text()='Newsletter']").click()
    # wprowadzanie maila
    context.driver.find_element(By.XPATH, "//*[@id='tnp-2']").send_keys("generate_unique_email")
    # akteptowanie privaCy policy
    context.driver.find_element(By.XPATH, "//*[@name='ny']").clicl()
    # klikanie w Subscribe


# zapisywanie sie do newsletera bez maila
def newsletter_subscribe_no_mail(context):
    # klikanie w newsletter
    context.driver.find_element(By.XPATH, "//*[contains(@class, 'focus')]//a[text()='Newsletter']").click()
    # wprowadzanie imienia
    context.driver.find_element(By.XPATH, "//*[@id='tnp-1']").send_keys("JanNowak")
    # akteptowanie privaCy policy
    context.driver.find_element(By.XPATH, "//*[@name='ny']").clicl()
    # klikanie w Subscribe
