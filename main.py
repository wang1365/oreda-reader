import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def run():
    options = webdriver.ChromeOptions()
    options.add_argument('--proxy-server=http://127.0.0.1:10809')

    driver = webdriver.Chrome(options)
    print('start chrome')
    driver.get("https://webapp.oreda.com/")
    driver.implicitly_wait(5)

    with open('./out/oreda_login.html', 'w', encoding='utf8') as f:
        f.write(driver.page_source)

    # 输入用户名
    username = driver.find_element(By.ID, "username")
    username.send_keys("xxx@xxx.com")
    driver.implicitly_wait(5)

    # 点击继续，显示密码输入框
    continue_btn = driver.find_element(By.ID, "continue")
    continue_btn.click()
    driver.implicitly_wait(5)

    # 输入密码
    password = driver.find_element(By.ID, "password")
    password.send_keys("*****")
    driver.implicitly_wait(2)

    # 点击登录
    login = driver.find_element(By.ID, "next")
    login.click()
    driver.implicitly_wait(5)

    # 找到并点击Population节点，使其展开
    population = driver.find_element(By.XPATH, '//vaadin-horizontal-layout/span[text()="Population"]')
    population.click()
    driver.implicitly_wait(2)

    # 找到并点击Equipment class节点，使其展开
    population = driver.find_element(By.XPATH, '//vaadin-horizontal-layout/span[text()="Equipment class"]')
    population.click()
    driver.implicitly_wait(10)

    equipment_class = set()
    equipment_class_subs = driver.find_elements(By.XPATH, '//vaadin-grid-tree-toggle[@style="---level: 2;"]/*/*/vaadin-checkbox')
    equipment_class_spans = driver.find_elements(By.XPATH, '//vaadin-grid-tree-toggle[@style="---level: 2;"]/*/*/span')
    for i, span in enumerate(equipment_class_spans):
        print(f"=> {i} {span.text}")
        equipment_class.add(span.text)

    design_class = driver.find_element(By.XPATH, '//vaadin-horizontal-layout/span[text()="Design class"]')
    ActionChains(driver).move_to_element(design_class).perform()
    ActionChains(driver).scroll_by_amount(0, 800)
    driver.implicitly_wait(5)
    equipment_class_spans = driver.find_elements(By.XPATH, '//vaadin-grid-tree-toggle[@style="---level: 2;"]/*/*/span')
    for i, span in enumerate(equipment_class_spans):
        print(f"=> {i} {span.text}")
        equipment_class.add(span.text)
    print(equipment_class)
    driver.implicitly_wait(2)

    while 1:
        time.sleep(6000)


if __name__ == '__main__':
    run()
