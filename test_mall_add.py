import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestAdvanced:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown_class(self):
        self.driver.quit()

    def test_advanced(self):
        self.driver.get("http://litemall.hogwarts.ceshiren.com/vue/index.html#/login?redirect=user")
        self.driver.find_element(By.CSS_SELECTOR, "input[name='user']").send_keys("Henry")
        self.driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("password")
        self.driver.find_element(By.CSS_SELECTOR, ".van-button").click()
        self.driver.find_element(By.CSS_SELECTOR, ".van-tabbar-item").click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.CSS_SELECTOR, ".van-field__control"))).click()
        self.driver.find_element(By.CSS_SELECTOR, "[placeholder='请输入商品名称']").send_keys("魔兽世界 蛋盾包 双肩包")
        self.driver.find_element(By.CSS_SELECTOR, ".van-field__control").send_keys(Keys.ENTER)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.CSS_SELECTOR, ".van-card__title"))).click()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.CSS_SELECTOR, ".van-goods-action-button--first"))).click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.CSS_SELECTOR, ".van-button--warning"))).click()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.CSS_SELECTOR, ".van-goods-action-icon"))).click()

        res = self.driver.find_elements(By.CSS_SELECTOR, ".van-card__title")
        res_text = [i.text for i in res]
        assert "魔兽世界 蛋盾包 双肩包" in res_text