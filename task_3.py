# Применив selenium, напишите unit-test для авторизации на Яндексе по
# url: https://passport.yandex.ru/auth/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://passport.yandex.ru/auth")

#  Заполнение поля логин
login = driver.find_element_by_name("login")
login.send_keys("логин")
login.send_keys(Keys.RETURN)

#  Нажатие кнопки Войти
butt = driver.find_element_by_css_selector("button.Button2").click()

#  Ввод пароля
elem = driver.find_element_by_name("passwd")
elem.send_keys("пароль")
elem.send_keys(Keys.RETURN)

#  Нажатие кнопки Войти еще раз
butt_2 = driver.find_element_by_css_selector("button.Button2").click()

driver.close()
driver.quit()
