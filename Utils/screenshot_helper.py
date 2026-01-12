# utils/screenshot_helper.py
import time
from pathlib import Path


def take_screenshot(page, test_name: str, status: str, folder: str = "screenshots"):
    """
    Сохраняет скриншот с понятным именем.
    """
    Path(folder).mkdir(exist_ok=True)
    filename = f"{folder}/screenshot_{test_name}_{status}_{int(time.time())}.png"
    page.screenshot(path=filename)
    print(f"📸 Скриншот сохранён: {filename}")
    return filename