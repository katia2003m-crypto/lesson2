import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

COOKIE_USER_1 = {
    "name": "SESSION",
    "value": "YjRiN2E1YmEtZWU1Zi00ZTFkLWI5M2EtMjIzZTljZTZjNDE5"
}
COOKIE_USER_2 = {
    "name": "SESSION",
    "value": "ZmJlNTgxMzUtNDJlZS00MTg5LTllYzUtYjk0ZjAwOTBiN2M2"
}


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.get("https://gitflic.ru/")

    # Пользователь 1
    driver.add_cookie(COOKIE_USER_1)
    driver.refresh()

    driver.get("https://gitflic.ru/user/name000000000")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    url_user_1 = driver.current_url

    print("Смотрим на профиль 1-го пользователя 5 секунд")
    time.sleep(5)

    driver.delete_all_cookies()

    # Пользователь 2
    driver.add_cookie(COOKIE_USER_2)
    driver.refresh()

    driver.get("https://gitflic.ru/user/name000000001")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    url_user_2 = driver.current_url

    print("Смотрим на профиль 2-го пользователя 5 секунд")
    time.sleep(5)

    assert url_user_1 != url_user_2

    driver.quit()
