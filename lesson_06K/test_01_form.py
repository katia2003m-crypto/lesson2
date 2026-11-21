import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture
def driver():
    service = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form_submission(driver):
    wait = WebDriverWait(driver, 10)
    url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    driver.get(url)

    form_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "zip-code": "",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for field_name, value in form_data.items():
        locator = (By.NAME, field_name)
        input_field = wait.until(
            EC.presence_of_element_located(locator)
        )
        input_field.clear()
        if value:
            input_field.send_keys(value)

    submit_btn = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[type='submit']")
        )
    )
    submit_btn.click()

    zip_code_field = wait.until(
        EC.presence_of_element_located((By.ID, "zip-code"))
    )
    zip_class = zip_code_field.get_attribute("class")
    assert "alert-danger" in zip_class, (
        "Поле Zip code не подсвечено красным!"
    )

    success_fields = driver.find_elements(
        By.CSS_SELECTOR, ".alert-success"
    )
    assert len(success_fields) == 9, (
        f"Ожидалось 9 зеленых полей, найдено {len(success_fields)}"
    )
