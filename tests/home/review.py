from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
from selenium.webdriver.common.by import By
from .login import LogIn_as_existing_user

#SPRAWDZANIE WARTOŚCI BRZEGOWYCH PRZY TESTOWANIA DODAWANIA RECENZJI PRODUKTU

email = 'paw.kuznik+99@gmail.com'
password = '123456'

def random_review_200(context):
    review = random.randint(0, 195)
    random_review = 'qwertyy' + '+' + str(review)
    print(random_review)
    return (random_review)

def random_review_10005(context):
    review = random.randint(0, 10005)
    random_review = 'qwertyy' + '+' + str(review)
    print(random_review)
    return (random_review)


driver = webdriver.Chrome()
driver.get("http://34.118.71.117/")


LogIn_as_existing_user()

#Dodawanie recenzji jako zalogowany użytkownik nie zaznaczając żadnej gwiazdki
def Review_as_loged_user_without_marking_stars(context):
    #logowanie
    LogIn_as_existing_user()

    #znajdowanie na głownej stronie pierwszego przedmiotu
    context.driver.find_element(By.XPATH, "//*[contains(@class, 'wp-block-product-new')]//*[contains(@class, 'wc-block-grid__products')]/li/a/div/img").click()

    #znajdowanie Reviews i klikanie
    context.driver.find_element(By.XPATH, "//*[@id='tab-title-reviews']/a").click()

    #wpisywanie losowo wygenerowanego tekstu nie dłuższego niż 200 wyrazów
    context.driver.find_element(By.XPATH, "//*[@id='comment']").send_keys(random_review_200())

    #klikanie w Submit
    context.driver.find_element(By.XPATH, "//*[@id='submit']").click()

#Dodawanie recezji z 5 gwiazdkami jako zalogowany użytkownik zaznaczając 5 gwiazdek i wpisując tekst nie dłuższy niż 200 znaków
def Review_as_loged_user(context):
    #logowanie
    LogIn_as_existing_user()

    #znajdowanie na głownej stronie pierwszego przedmiotu
    context.driver.find_element(By.XPATH, "//*[contains(@class, 'wp-block-product-new')]//*[contains(@class, 'wc-block-grid__products')]/li/a/div/img").click()

    #znajdowanie Reviews i klikanie
    context.driver.find_element(By.XPATH, "//*[@id='tab-title-reviews']/a").click()

    #wpisywanie losowo wygenerowanego tekstu nie dłuższego niż 200 wyrazów
    context.driver.find_element(By.XPATH, "//*[@id='comment']").send_keys(random_review_200())

    #zaznaczenie 5 gwiazdek
    context.driver.find_element(By.XPATH, "//a[text()='5']").click()

    #klikanie w Submit
    context.driver.find_element(By.XPATH, "//*[@id='submit']").click()

#Dodawanie recenzji z 1 gwiazdką jako zalogowany użytkownik wpisując 10005 znaków
def Review_as_loged_user(context):
    #logowanie
    LogIn_as_existing_user()

    # znajdowanie na głownej stronie pierwszego przedmiotu
    context.driver.find_element(By.XPATH,"//*[contains(@class, 'wp-block-product-new')]//*[contains(@class, 'wc-block-grid__products')]/li/a/div/img").click()

    # znajdowanie Reviews i klikanie
    context.driver.find_element(By.XPATH, "//*[@id='tab-title-reviews']/a").click()

    # wpisywanie losowo wygenerowanego tekstu  dłuższego niż 200 wyrazów
    context.driver.find_element(By.XPATH, "//*[@id='comment']").send_keys(random_review_10005())

    # zaznaczenie 1 gwiazdki
    context.driver.find_element(By.XPATH, "//a[text()='1']").click()

    # klikanie w Submit
    context.driver.find_element(By.XPATH, "//*[@id='submit']").click()

#Dodawanie recenzji z 3 gwiazdkami jako zalogowany użytkownik nie wpisując żadnej recenzji
def Review_as_loged_user_without_text(context):
    #logowanie
    LogIn_as_existing_user()

    # znajdowanie na głownej stronie pierwszego przedmiotu
    context.driver.find_element(By.XPATH,"//*[contains(@class, 'wp-block-product-new')]//*[contains(@class, 'wc-block-grid__products')]/li/a/div/img").click()

    # znajdowanie Reviews i klikanie
    context.driver.find_element(By.XPATH, "//*[@id='tab-title-reviews']/a").click()

    # zaznaczenie 3 gwiazdek
    context.driver.find_element(By.XPATH, "//a[text()='3']").click()

    # klikanie w Submit
    context.driver.find_element(By.XPATH, "//*[@id='submit']").click()

#Dodawanie recenzji jako niezalogowany użytkownik wpisując wszystkie informacje: gwiazdkę, recenzje, name, Email
def Review_as_unloged_user(context):
    # znajdowanie na głownej stronie pierwszego przedmiotu
    context.driver.find_element(By.XPATH,"//*[contains(@class, 'wp-block-product-new')]//*[contains(@class, 'wc-block-grid__products')]/li/a/div/img").click()

    # znajdowanie Reviews i klikanie
    context.driver.find_element(By.XPATH, "//*[@id='tab-title-reviews']/a").click()

    # zaznaczenie 2 gwiazdek
    context.driver.find_element(By.XPATH, "//a[text()='2']").click()

    #wpisywanie losowo wygenerowanego tekstu nie dłuższego niż 200 wyrazów
    context.driver.find_element(By.XPATH, "//*[@id='comment']").send_keys(random_review_200())

    #wpisywanie Name
    context.driver.find_element(By.XPATH, "//*[@id='author']").send_keys("JanNowak")

    #wpisywanie Email
    context.driver.find_element(By.XPATH, "//*[@id='email']").sen_keys(email)

    # klikanie w Submit
    context.driver.find_element(By.XPATH, "//*[@id='submit']").click()