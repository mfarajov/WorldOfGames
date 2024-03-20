from selenium import webdriver
from selenium.webdriver.common.by import By
import sys


def test_scores_service(url):
    driver = webdriver.Chrome()
    try:
        driver.get(url)

        score_element = driver.find_element(By.ID, 'score')
        score = int(score_element.text)

        return 1 <= score <= 1000
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        driver.quit()


def main_function():
    test_url = 'http://127.0.0.1:8777'

    if test_scores_service(test_url):
        print('Test passed!')
        return 0

    else:
        print('Test failed!')
        return -1


if __name__ == "__main__":
    exit_code = main_function()
    sys.exit(exit_code)
