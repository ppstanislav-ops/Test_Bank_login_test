# pages/login_page.py
from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("[name='password']")
        self.login_button = page.locator("#login-button")
        self.otp_input = page.locator("#otp-code")
        self.otp_button = page.locator("#login-otp-button")
        self.logout_button = page.locator("#logout-button")

    def goto(self):
        """Открыть страницу входа"""
        self.page.goto(
            "https://idemo.bspb.ru/auth?response_type=code&client_id=1"
            "&redirect_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fsuccess"
            "&prefetch_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fprefetch"
            "&force_new_session=true"
        )

    def login(self, username: str, password: str):
        """Ввести логин и пароль, нажать Войти"""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def enter_otp(self, code: str):
        """Ввести OTP-код"""
        self.otp_input.wait_for(timeout=10000)
        self.otp_input.fill(code)
        self.otp_button.click()

    def is_logged_in(self) -> bool:
        """Проверить, вошли ли мы в систему"""
        try:
            self.logout_button.wait_for(state="visible", timeout=10000)
            return True
        except:
            return False

    def is_on_login_page(self) -> bool:
        """Проверить, что мы всё ещё на странице входа"""
        try:
            self.login_button.wait_for(state="visible", timeout=5000)
            return True
        except:
            return False