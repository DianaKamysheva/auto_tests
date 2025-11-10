import pytest
import sys
import os
from selenium import webdriver

# Добавляем корневую директорию в PYTHONPATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()