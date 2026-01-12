# tests/test_login.py
import pytest
from playwright.sync_api import Page
from Pages.login_page import LoginPage
from Utils.screenshot_helper import take_screenshot


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


# Тесты будут запускаться автоматически в Chromium и Firefox,
# если вы запустите с: pytest --browser chromium --browser firefox
def test_valid_login(login_page: LoginPage):
    """TC-001: Вход с валидными данными"""
    print("\n🎯 TC-001: Вход с валидными данными")

    login_page.goto()
    login_page.login("multicustomer", "secret")
    login_page.enter_otp("0000")

    if login_page.is_logged_in():
        print("✅ Успешный вход под multicustomer")
        take_screenshot(login_page.page, "TC001_valid_login", "PASS")
        assert True
    else:
        take_screenshot(login_page.page, "TC001_valid_login", "FAIL")
        pytest.fail("Не удалось войти с валидными данными")


def test_invalid_login(login_page: LoginPage):
    """TC-002: Вход с невалидными данными"""
    print("\n🎯 TC-002: Вход с невалидными данными")

    login_page.goto()
    login_page.login("invalid_user", "wrong_password")

    if login_page.is_on_login_page() and not login_page.is_logged_in():
        print("✅ Остались на странице входа — вход не удался (ожидаемо)")
        take_screenshot(login_page.page, "TC002_invalid_login", "PASS")
        assert True
    else:
        take_screenshot(login_page.page, "TC002_invalid_login", "FAIL")
        pytest.fail("Попал внутрь системы с невалидными данными!")
        