import random
import string
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def click(driver, method: str, target: str, index_test, index):
    ele = getattr(driver, method)(target)
    actions = ActionChains(driver)
    actions.move_to_element(ele).click().perform()
    time.sleep(1)
    driver.save_screenshot(f"C:/Users/hoang/Desktop/screenshot/test{index_test}/{index}.png")
    return ele


def hover_to(driver, method: str, target: str, index_test, index):
    ele = getattr(driver, method)(target)
    actions = ActionChains(driver)
    actions.move_to_element(ele).perform()
    time.sleep(1)
    driver.save_screenshot(f"C:/Users/hoang/Desktop/screenshot/test{index_test}/{index}.png")
    return ele


def clear(driver, method: str, target: str, index_test, index):
    ele = getattr(driver, method)(target)
    range_ele = ele.get_attribute('value') or ele.text
    ele.send_keys(Keys.CONTROL, 'a')
    ele.send_keys(Keys.BACKSPACE)
    time.sleep(1)
    driver.save_screenshot(f"C:/Users/hoang/Desktop/screenshot/test{index_test}/{index}.png")
    return ele


def send_keys(driver, method: str, target: str, index_test, index, *keys):
    ele = getattr(driver, method)(target)
    for key in keys:
        ele.send_keys(key)
    time.sleep(1)
    driver.save_screenshot(f"C:/Users/hoang/Desktop/screenshot/test{index_test}/{index}.png")
    return ele


def send_keys_enter(driver, method: str, target: str, index_test, index):
    ele = getattr(driver, method)(target)
    ele.send_keys(Keys.ENTER)
    time.sleep(1)
    driver.save_screenshot(f"C:/Users/hoang/Desktop/screenshot/test{index_test}/{index}.png")
    return ele


def get_value(driver, method: str, target: str):
    ele = getattr(driver, method)(target)
    range_ele = ele.get_attribute('value') or ele.text
    return range_ele


def asserts(driver, method: str, target: str, value):
    ele = getattr(driver, method)(target)
    value_asserts = ele.get_attribute('value') or ele.text
    assert value_asserts == value


def main():
    # T??? test1-test12 l?? cho ph???n giao d???ch v???i c??c gi?? tr??? t??m c?? k???t qu??? v?? t??m k c?? k???t qu???

    # T??? test1-test6 l?? cho ph???n giao d???ch v???i c??c gi?? tr??? t??m c?? k???t qu???
    test1()  # test t??m ki???m t??n ng?????i d??ng // pass
    test2()  # test t??m ki???m lo???i ng?????i d??ng // pass
    test3()  # test t??m ki???m d???a ch??? ng?????i d??ng // pass
    test4()  # test t??m ki???m lo???i b???o hi???m// pass
    test5()  # test t??m ki???m gi?? b???o hi???m// pass
    test6()  # test t??m ki???m t???ng ti???n giao d???ch// pass

    # T??? test7-test12 l?? cho ph???n giao d???ch v???i c??c gi?? tr??? t??m kh??ng c?? k???t qu???
    test7()  # test t??m ki???m t??n ng?????i d??ng// pass
    test8()  # test t??m ki???m lo???i ng?????i d??ng// pass
    test9()  # test t??m ki???m d???a ch??? ng?????i d??ng// pass
    test10()  # test t??m ki???m lo???i b???o hi???m// pass
    test11()  # test t??m ki???m gi?? b???o hi???m// pass
    test12()  # test t??m ki???m t???ng ti???n giao d???ch// pass

# T??? test13-test20 l?? cho ph???n ng?????i d??ng v???i c??c gi?? tr??? t??m c?? k???t qu??? v?? t??m kh??ng c?? k???t qu???
    # T??? test13-test16 l?? cho ph???n ng?????i d??ng v???i c??c gi?? tr??? t??m c?? k???t qu???
    test13()  # test t??m ki???m t??n ng?????i d??ng// pass
    test14()  # test t??m ki???m lo???i ng?????i d??ng// pass
    test15()  # test t??m ki???m ?????a ch??? ng?????i d??ng// pass
    test16()  # test t??m ki???m lo???i b???o hi???m// pass
    # T??? test13-test16 l?? cho ph???n ng?????i d??ng v???i c??c gi?? tr??? t??m kh??ng c?? k???t qu???
    test17()  # test t??m ki???m t??n ng?????i d??ng// pass
    test18()  # test t??m ki???m lo???i ng?????i d??ng// pass
    test19()  # test t??m ki???m ?????a ch??? ng?????i d??ng// pass
    test20()  # test t??m ki???m lo???i b???o hi???m// pass
# T??? test21-test24 l?? cho ph???n b???o hi???m v???i c??c gi?? tr??? t??m c?? k???t qu??? v?? t??m kh??ng c?? k???t qu???
    # T??? test21 v?? test22 l?? cho ph???n b???o hi???m v???i c??c gi?? tr??? t??m c?? k???t qu???
    test21()  # test t??m ki???m lo???i b???o hi???m // pass
    test22()  # test t??m ki???m gi?? b???o hi???m // pass
    # T??? test21 v?? test22 l?? cho ph???n b???o hi???m v???i c??c gi?? tr??? t??m kh??ng c?? k???t qu???
    test23()  # test t??m ki???m lo???i b???o hi???m // pass
    test24()  # test t??m ki???m gi?? b???o hi???m // pass
    # test25 v?? test 26 s???a th??nh c??ng gi?? cho b???o hi???m
    test25()  # test s???a t??n b???o hi???m
    test26()  # test s???a gi?? b???o hi???m
    # test27 v?? test 28 s???a nh??ng ???n cancel ????? ki???m tra gi?? tr???  b???o hi???m kh??ng thay ?????i
    test27()  # test s???a t??n b???o hi???m
    test28()  # test gi?? t??n b???o hi???m
# T??? test29-test30 l?? cho ph???n b??o c??o v???i c??c gi?? tr??? t??m c?? k???t qu??? v?? t??m kh??ng c?? k???t qu???
    test29()  # test  l???c theo ng??y th??ng n??m v?? c?? k???t qu???
    test30()  # test  l???c theo ng??y th??ng n??m v?? kh??ng c?? k???t qu???
# check paging ??? page ng?????i d??ng v?? giao d???ch
    test31()  # check paging ??? page  giao d???ch
    test32()  # check paging ??? page ng?????i d??ng
# check paging ??? page ng?????i d??ng v?? giao d???ch khi t??m ki???m
    test33()  # check paging ??? page  giao d???ch khi t??m ki???m lo???i ng?????i d??ng
    test34()  # check paging ??? page  giao d???ch khi t??m ki???m ?????a ch??? ng?????i d??ng
    test35()  # check paging ??? page  giao d???ch khi t??m ki???m lo???i b???o hi???m
    test36()  # check paging ??? page  giao d???ch khi t??m ki???m t???ng ti???n giao d???ch
    test37()  # check paging ??? page  ng?????i d??ng khi t??m ki???m lo???i ng?????i d??ng
    test38()  # check paging ??? page  ng?????i d??ng khi t??m ki???m ?????a ch??? ng?????i d??ng
    test39()  # check paging ??? page  ng?????i d??ng khi t??m ki???m lo???i b???o hi???m


# T??? test29-test30 l?? cho ph???n b??o c??o v???i c??c gi?? tr??? t??m c?? k???t qu??? v?? t??m kh??ng c?? k???t qu???

# c??c test case t??m ki???m gi?? tr??? c?? t???n t???i c???a giao d???ch


def test1():
    URL = 'http://localhost:3000/'
    driver = webdriver.Chrome(r"app\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    try:
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])', 1, 1)
        send_keys(driver, 'find_element_by_xpath', '(//*[@class="ant-input"])', 1, 2, 'a')
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-primary ant-btn-sm"])', 1, 3)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])', 1, 4)
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-sm"])', 1, 5)
    except Exception as error:
        return error.__class__.__name__
    driver.close()
    return True


def test2():
    URL = 'http://localhost:3000/'
    driver = webdriver.Chrome(r"app\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    try:
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[2]', 2, 1)
        send_keys(driver, 'find_element_by_xpath', '(//*[@class="ant-input"])', 2, 2, 'a')
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-primary ant-btn-sm"])', 2, 3)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[2]', 2, 4)
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-sm"])', 2, 5)
    except Exception as error:
        return error.__class__.__name__
    driver.close()
    return True


def test3():
    URL = 'http://localhost:3000/'
    driver = webdriver.Chrome(r"app\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    try:
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[3]', 3, 1)
        send_keys(driver, 'find_element_by_xpath', '(//*[@class="ant-input"])', 3, 2, 'H?? N???i')
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-primary ant-btn-sm"])', 3, 3)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[3]', 3, 4)
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-sm"])', 3, 5)
    except Exception as error:
        return error.__class__.__name__
    driver.close()
    return True


def test4():
    URL = 'http://localhost:3000/'
    driver = webdriver.Chrome(r"app\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    try:
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[4]', 4, 1)
        send_keys(driver, 'find_element_by_xpath', '(//*[@class="ant-input"])', 4, 2, 'bh')
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-primary ant-btn-sm"])', 4, 3)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[4]', 4, 4)
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-sm"])', 4, 5)
    except Exception as error:
        return error.__class__.__name__
    driver.close()
    return True


def test5():
    URL = 'http://localhost:3000/'
    driver = webdriver.Chrome(r"app\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    try:
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[5]', 5, 1)
        send_keys(driver, 'find_element_by_xpath', '(//*[@class="ant-input"])', 5, 2, '123')
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-primary ant-btn-sm"])', 5, 3)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[5]', 5, 4)
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-sm"])', 5, 5)
    except Exception as error:
        return error.__class__.__name__
    driver.close()
    return True


def test6():
    URL = 'http://localhost:3000/'
    driver = webdriver.Chrome(r"app\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    try:
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[6]', 6, 1)
        send_keys(driver, 'find_element_by_xpath', '(//*[@class="ant-input"])', 6, 2, '600000')
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-primary ant-btn-sm"])', 6, 3)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[6]', 6, 4)
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-sm"])', 6, 5)
    except Exception as error:
        return error.__class__.__name__
    driver.close()
    return True

# c??c test case t??m ki???m gi?? tr??? kh??ng t???n t???i c???a giao d???ch


def test7():
    URL = 'http://localhost:3000/'
    driver = webdriver.Chrome(r"app\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    try:
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])', 7, 1)
        send_keys(driver, 'find_element_by_xpath', '(//*[@class="ant-input"])', 7, 2, 'q??eqwe')
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-primary ant-btn-sm"])', 7, 3)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])', 7, 4)
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-sm"])', 7, 5)
    except Exception as error:
        return error.__class__.__name__
    driver.close()
    return True


def test8():
    URL = 'http://localhost:3000/'
    driver = webdriver.Chrome(r"app\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    try:
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[2]', 8, 1)
        send_keys(driver, 'find_element_by_xpath', '(//*[@class="ant-input"])', 8, 2, 'q??eqwe')
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-primary ant-btn-sm"])', 8, 3)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[2]', 8, 4)
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-sm"])', 8, 5)
    except Exception as error:
        return error.__class__.__name__
    driver.close()
    return True


def test9():
    URL = 'http://localhost:3000/'
    driver = webdriver.Chrome(r"app\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    try:
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[3]', 9, 1)
        send_keys(driver, 'find_element_by_xpath', '(//*[@class="ant-input"])', 9, 2, '???bhbjcfvdf')
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-primary ant-btn-sm"])', 9, 3)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[3]', 9, 4)
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-sm"])', 9, 5)
    except Exception as error:
        return error.__class__.__name__
    driver.close()
    return True


def test10():
    URL = 'http://localhost:3000/'
    driver = webdriver.Chrome(r"app\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    try:
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[4]', 10, 1)
        send_keys(driver, 'find_element_by_xpath', '(//*[@class="ant-input"])', 10, 2, '??dhjias')
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-primary ant-btn-sm"])', 10, 3)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[4]', 10, 4)
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-sm"])', 10, 5)
    except Exception as error:
        return error.__class__.__name__
    driver.close()
    return True


def test11():
    URL = 'http://localhost:3000/'
    driver = webdriver.Chrome(r"app\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    try:
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[5]', 11, 1)
        send_keys(driver, 'find_element_by_xpath', '(//*[@class="ant-input"])', 11, 2, '???idb')
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-primary ant-btn-sm"])', 11, 3)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[5]', 11, 4)
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-sm"])', 11, 5)
    except Exception as error:
        return error.__class__.__name__
    driver.close()
    return True


def test12():
    URL = 'http://localhost:3000/'
    driver = webdriver.Chrome(r"app\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    try:
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[6]', 12, 1)
        send_keys(driver, 'find_element_by_xpath', '(//*[@class="ant-input"])', 12, 2, '??bhji')
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-primary ant-btn-sm"])', 12, 3)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[6]', 12, 4)
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-sm"])', 12, 5)
    except Exception as error:
        return error.__class__.__name__
    driver.close()
    return True

# c??c test case t??m ki???m gi?? tr??? c?? t???n t???i c???a ng?????i d??ng


def test13():
    URL = 'http://localhost:3000/'
    driver = webdriver.Chrome(r"app\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    try:
        click(driver, 'find_element_by_id', 'rc-tabs-0-tab-2', 13, 1)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])', 13, 2)
        send_keys(driver, 'find_element_by_xpath', '(//*[@class="ant-input"])', 13, 3, 'Linh')
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-primary ant-btn-sm"])', 13, 4)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])', 13, 5)
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-sm"])', 13, 6)
    except Exception as error:
        return error.__class__.__name__
    driver.close()
    return True


def test14():
    URL = 'http://localhost:3000/'
    driver = webdriver.Chrome(r"app\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    try:
        click(driver, 'find_element_by_id', 'rc-tabs-0-tab-2', 14, 1)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[2]', 14, 2)
        send_keys(driver, 'find_element_by_xpath', '(//*[@class="ant-input"])', 14, 3, 'a')
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-primary ant-btn-sm"])', 14, 4)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[2]', 14, 5)
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-sm"])', 14, 6)
    except Exception as error:
        return error.__class__.__name__
    driver.close()
    return True


def test15():
    URL = 'http://localhost:3000/'
    driver = webdriver.Chrome(r"app\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    try:
        click(driver, 'find_element_by_id', 'rc-tabs-0-tab-2', 15, 1)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[3]', 15, 2)
        send_keys(driver, 'find_element_by_xpath', '(//*[@class="ant-input"])', 15, 3, 'H?? N???i')
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-primary ant-btn-sm"])', 15, 4)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[3]', 15, 5)
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-sm"])', 15, 6)
    except Exception as error:
        driver.close()
        return error.__class__.__name__
    driver.close()
    return True


def test16():
    URL = 'http://localhost:3000/'
    driver = webdriver.Chrome(r"app\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    try:
        click(driver, 'find_element_by_id', 'rc-tabs-0-tab-2', 16, 1)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[4]', 16, 2)
        send_keys(driver, 'find_element_by_xpath', '(//*[@class="ant-input"])', 16, 3, 'bh')
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-primary ant-btn-sm"])', 16, 4)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[4]', 16, 5)
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-sm"])', 16, 6)
    except Exception as error:
        return error.__class__.__name__
    driver.close()
    return True

# c??c test case t??m ki???m gi?? tr??? kh??ng t???n t???i c???a ng?????i d??ng


def test17():
    URL = 'http://localhost:3000/'
    driver = webdriver.Chrome(r"app\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    try:
        click(driver, 'find_element_by_id', 'rc-tabs-0-tab-2', 17, 1)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])', 17, 2)
        send_keys(driver, 'find_element_by_xpath', '(//*[@class="ant-input"])', 17, 3, '123')
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-primary ant-btn-sm"])', 17, 4)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])', 17, 5)
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-sm"])', 17, 6)
    except Exception as error:
        return error.__class__.__name__
    driver.close()
    return True


def test18():
    URL = 'http://localhost:3000/'
    driver = webdriver.Chrome(r"app\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    try:
        click(driver, 'find_element_by_id', 'rc-tabs-0-tab-2', 18, 1)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[2]', 18, 2)
        send_keys(driver, 'find_element_by_xpath', '(//*[@class="ant-input"])', 18, 3, 'uiu890i45')
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-primary ant-btn-sm"])', 18, 4)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[2]', 18, 5)
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-sm"])', 18, 6)
    except Exception as error:
        return error.__class__.__name__
    driver.close()
    return True


def test19():
    URL = 'http://localhost:3000/'
    driver = webdriver.Chrome(r"app\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    try:
        click(driver, 'find_element_by_id', 'rc-tabs-0-tab-2', 19, 1)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[3]', 19, 2)
        send_keys(driver, 'find_element_by_xpath', '(//*[@class="ant-input"])', 19, 3, 'q??eqwe')
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-primary ant-btn-sm"])', 19, 4)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[3]', 19, 5)
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-sm"])', 19, 6)
    except Exception as error:
        return error.__class__.__name__
    driver.close()
    return True


def test20():
    URL = 'http://localhost:3000/'
    driver = webdriver.Chrome(r"app\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    try:
        click(driver, 'find_element_by_id', 'rc-tabs-0-tab-2', 20, 1)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[4]', 20, 2)
        send_keys(driver, 'find_element_by_xpath', '(//*[@class="ant-input"])', 20, 3, 'q??eqwe')
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-primary ant-btn-sm"])', 20, 4)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[4]', 20, 5)
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-sm"])', 20, 6)
    except Exception as error:
        return error.__class__.__name__
    driver.close()
    return True


# c??c test case t??m ki???m c???a b???o hi???m


def test21():
    URL = 'http://localhost:3000/'
    driver = webdriver.Chrome(r"app\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    try:
        click(driver, 'find_element_by_id', 'rc-tabs-0-tab-3', 21, 1)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])', 21, 2)
        send_keys(driver, 'find_element_by_xpath', '(//*[@class="ant-input"])', 21, 3, 'bh')
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-primary ant-btn-sm"])', 21, 4)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])', 21, 5)
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-sm"])', 21, 6)
    except Exception as error:
        return error.__class__.__name__
    driver.close()
    return True


def test22():
    URL = 'http://localhost:3000/'
    driver = webdriver.Chrome(r"app\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    try:
        click(driver, 'find_element_by_id', 'rc-tabs-0-tab-3', 22, 1)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])', 22, 2)
        send_keys(driver, 'find_element_by_xpath', '(//*[@class="ant-input"])', 22, 3, '123')
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-primary ant-btn-sm"])', 22, 4)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])', 22, 5)
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-sm"])', 22, 6)
    except Exception as error:
        return error.__class__.__name__
    driver.close()
    return True
# c??c test case t??m ki???m c???a b???o hi???m


def test23():
    URL = 'http://localhost:3000/'
    driver = webdriver.Chrome(r"app\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    try:
        click(driver, 'find_element_by_id', 'rc-tabs-0-tab-3', 23, 1)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])', 23, 2)
        send_keys(driver, 'find_element_by_xpath', '(//*[@class="ant-input"])', 23, 3, 'yui')
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-primary ant-btn-sm"])', 23, 4)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])', 23, 5)
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-sm"])', 23, 6)
    except Exception as error:
        return error.__class__.__name__
    driver.close()
    return True


def test24():
    URL = 'http://localhost:3000/'
    driver = webdriver.Chrome(r"app\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    try:
        click(driver, 'find_element_by_id', 'rc-tabs-0-tab-3', 24, 1)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[2]', 24, 2)
        send_keys(driver, 'find_element_by_xpath', '(//*[@class="ant-input"])', 24, 3, '109741315448464')
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-primary ant-btn-sm"])', 24, 4)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[2]', 24, 5)
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-sm"])', 24, 6)
    except Exception as error:
        return error.__class__.__name__
    driver.close()
    return True


# test case s???a th??nh c??ng b???o hi???m(s???a t??n)


def test25():
    URL = 'http://localhost:3000/'
    driver = webdriver.Chrome(r"app\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    try:
        click(driver, 'find_element_by_id', 'rc-tabs-0-tab-3', 25, 1)
        hover_to(driver, 'find_element_by_xpath', '(//*[@class="anticon anticon-menu ant-dropdown-trigger"])', 25, 2)
        time.sleep(1)
        click(driver, 'find_element_by_xpath',
              '//li[contains(@class,"ant-dropdown-menu-item ant-dropdown-menu-item-only-child")]', 25, 3)
        time.sleep(1)
        click(driver, 'find_element_by_id', 'nametype', 25, 4)
        time.sleep(1)
        clear(driver, 'find_element_by_id', 'nametype', 25, 4)
        send_keys(driver, 'find_element_by_id', 'nametype', 25, 5, 'B???o hi???m s?? 1')
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-primary"])', 25, 5)
    except Exception as error:
        return error.__class__.__name__
    driver.close()
    return True

# test case s???a gi?? th??nh c??ng b???o hi???m


def test26():
    URL = 'http://localhost:3000/'
    driver = webdriver.Chrome(r"app\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    try:
        click(driver, 'find_element_by_id', 'rc-tabs-0-tab-3', 26, 1)
        hover_to(driver, 'find_element_by_xpath', '(//*[@class="anticon anticon-menu ant-dropdown-trigger"])', 26, 2)
        time.sleep(1)
        click(driver, 'find_element_by_xpath',
              '//li[contains(@class,"ant-dropdown-menu-item ant-dropdown-menu-item-only-child")]', 26, 3)
        time.sleep(1)
        click(driver, 'find_element_by_id', 'price', 26, 4)
        time.sleep(1)
        clear(driver, 'find_element_by_id', 'price', 26, 5)
        send_keys(driver, 'find_element_by_id', 'price', 26, 6, '1000000')
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-primary"])', 26, 7)
    except Exception as error:
        return error.__class__.__name__
    driver.close()
    return True

# test case s???a t??n b???o hi???m nh??ng click n??t quay l???i b???o hi???m


def test27():
    URL = 'http://localhost:3000/'
    driver = webdriver.Chrome(r"app\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    try:
        click(driver, 'find_element_by_id', 'rc-tabs-0-tab-3', 27, 1)
        hover_to(driver, 'find_element_by_xpath', '(//*[@class="anticon anticon-menu ant-dropdown-trigger"])', 27, 2)
        time.sleep(1)
        click(driver, 'find_element_by_xpath',
              '//li[contains(@class,"ant-dropdown-menu-item ant-dropdown-menu-item-only-child")]', 27, 3)
        time.sleep(1)
        click(driver, 'find_element_by_id', 'nametype', 27, 4)
        time.sleep(1)
        clear(driver, 'find_element_by_id', 'nametype', 27, 5)
        send_keys(driver, 'find_element_by_id', 'nametype', 27, 6, 'B???o hi???m s?? 1234556')
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn"])', 27, 7)
    except Exception as error:
        return error.__class__.__name__
    driver.close()
    return True

# test case s???a gi?? b???o hi???m nh??ng click n??t quay l???i b???o hi???m


def test28():
    URL = 'http://localhost:3000/'
    driver = webdriver.Chrome(r"app\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    try:
        click(driver, 'find_element_by_id', 'rc-tabs-0-tab-3', 28, 1)
        hover_to(driver, 'find_element_by_xpath', '(//*[@class="anticon anticon-menu ant-dropdown-trigger"])', 28, 2)
        time.sleep(1)
        click(driver, 'find_element_by_xpath',
              '//li[contains(@class,"ant-dropdown-menu-item ant-dropdown-menu-item-only-child")]', 28, 3)
        time.sleep(1)
        click(driver, 'find_element_by_id', 'price', 28, 4)
        time.sleep(1)
        clear(driver, 'find_element_by_id', 'price', 28, 5)
        send_keys(driver, 'find_element_by_id', 'price', 28, 6, '1000000999')
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn"])', 28, 7)
    except Exception as error:
        return error.__class__.__name__
    driver.close()
    return True

# ch???n ng??y xem b??o c??o


def test29():
    URL = 'http://localhost:3000/'
    driver = webdriver.Chrome(r"app\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    try:
        click(driver, 'find_element_by_id', 'rc-tabs-0-tab-4', 29, 1)
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-picker-input ant-picker-input-active"])', 29, 2)
        time.sleep(1)
        send_keys(driver, 'find_element_by_xpath', '(//input[@placeholder="Start date"])', 29, 3, '2020-05-19')
        click(driver, 'find_element_by_xpath', '(//input[@placeholder="End date"])', 29, 4)
        time.sleep(1)
        send_keys(driver, 'find_element_by_xpath', '(//input[@placeholder="End date"])', 29, 5, '2022-05-29')
        send_keys_enter(driver, 'find_element_by_xpath', '(//input[@placeholder="End date"])', 29, 6)
    except Exception as error:
        return error.__class__.__name__
    driver.close()
    return True


def test30():
    URL = 'http://localhost:3000/'
    driver = webdriver.Chrome(r"app\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    try:
        click(driver, 'find_element_by_id', 'rc-tabs-0-tab-4', 30, 1)
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-picker-input ant-picker-input-active"])', 30, 2)
        time.sleep(1)
        send_keys(driver, 'find_element_by_xpath', '(//input[@placeholder="Start date"])', 30, 3, '2022-05-19')
        click(driver, 'find_element_by_xpath', '(//input[@placeholder="End date"])', 30, 4)
        time.sleep(1)
        send_keys(driver, 'find_element_by_xpath', '(//input[@placeholder="End date"])', 30, 5, '2021-05-29')
        send_keys_enter(driver, 'find_element_by_xpath', '(//input[@placeholder="End date"])', 30, 6)
    except Exception as error:
        return error.__class__.__name__
    driver.close()
    return True


def test31():
    URL = 'http://localhost:3000/'
    driver = webdriver.Chrome(r"app\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    try:
        click(driver, 'find_element_by_id', 'rc-tabs-0-tab-1', 31, 1)
        click(driver, 'find_element_by_xpath', '(//*[@rel="nofollow"])[2]', 31, 2)
    except Exception as error:
        return error.__class__.__name__
    driver.close()
    return True


def test32():
    URL = 'http://localhost:3000/'
    driver = webdriver.Chrome(r"app\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    try:
        click(driver, 'find_element_by_id', 'rc-tabs-0-tab-2', 32, 1)
        click(driver, 'find_element_by_xpath', '(//*[@rel="nofollow"])[2]', 32, 2)
    except Exception as error:
        return error.__class__.__name__
    driver.close()
    return True


def test33():
    URL = 'http://localhost:3000/'
    driver = webdriver.Chrome(r"app\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    try:
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[2]', 33, 1)
        send_keys(driver, 'find_element_by_xpath', '(//*[@class="ant-input"])', 33, 2, 'vip')
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-primary ant-btn-sm"])', 33, 3)
        click(driver, 'find_element_by_xpath', '(//*[@rel="nofollow"])[2]', 33, 4)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[2]', 33, 5)
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-sm"])', 33, 6)
    except Exception as error:
        return error.__class__.__name__
    driver.close()
    return True


def test34():
    URL = 'http://localhost:3000/'
    driver = webdriver.Chrome(r"app\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    try:
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[3]', 34, 1)
        send_keys(driver, 'find_element_by_xpath', '(//*[@class="ant-input"])', 34, 2, 'H?? N???i')
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-primary ant-btn-sm"])', 34, 3)
        click(driver, 'find_element_by_xpath', '(//*[@rel="nofollow"])[2]', 34, 4)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[3]', 34, 5)
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-sm"])', 34, 6)
    except Exception as error:
        return error.__class__.__name__
    driver.close()
    return True


def test35():
    URL = 'http://localhost:3000/'
    driver = webdriver.Chrome(r"app\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    try:
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[4]', 35, 1)
        send_keys(driver, 'find_element_by_xpath', '(//*[@class="ant-input"])', 35, 2, 'bh')
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-primary ant-btn-sm"])', 35, 3)
        click(driver, 'find_element_by_xpath', '(//*[@rel="nofollow"])[2]', 35, 4)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[4]', 35, 5)
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-sm"])', 35, 6)
    except Exception as error:
        return error.__class__.__name__
    driver.close()
    return True


def test36():
    URL = 'http://localhost:3000/'
    driver = webdriver.Chrome(r"app\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    try:
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[4]', 36, 1)
        send_keys(driver, 'find_element_by_xpath', '(//*[@class="ant-input"])', 36, 2, '5415000')
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-primary ant-btn-sm"])', 36, 3)
        click(driver, 'find_element_by_xpath', '(//*[@rel="nofollow"])[2]', 36, 4)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[4]', 36, 5)
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-sm"])', 36, 6)
    except Exception as error:
        return error.__class__.__name__
    driver.close()
    return True


def test37():
    URL = 'http://localhost:3000/'
    driver = webdriver.Chrome(r"app\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    try:
        click(driver, 'find_element_by_id', 'rc-tabs-0-tab-2', 37, 1)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[2]', 37, 2)
        send_keys(driver, 'find_element_by_xpath', '(//*[@class="ant-input"])', 37, 3, 'vip')
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-primary ant-btn-sm"])', 37, 4)
        click(driver, 'find_element_by_xpath', '(//*[@rel="nofollow"])[2]', 37, 5)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[2]', 37, 6)
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-sm"])', 37, 7)
    except Exception as error:
        return error.__class__.__name__
    driver.close()
    return True


def test38():
    URL = 'http://localhost:3000/'
    driver = webdriver.Chrome(r"app\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    try:
        click(driver, 'find_element_by_id', 'rc-tabs-0-tab-2', 38, 1)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[3]', 38, 2)
        send_keys(driver, 'find_element_by_xpath', '(//*[@class="ant-input"])', 38, 3, 'H?? N???i')
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-primary ant-btn-sm"])', 38, 4)
        click(driver, 'find_element_by_xpath', '(//*[@rel="nofollow"])[2]', 38, 5)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[3]', 38, 6)
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-sm"])', 38, 7)
    except Exception as error:
        return error.__class__.__name__
    driver.close()
    return True


def test39():
    URL = 'http://localhost:3000/'
    driver = webdriver.Chrome(r"app\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get(URL)
    try:
        click(driver, 'find_element_by_id', 'rc-tabs-0-tab-2', 39, 1)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[4]', 39, 2)
        send_keys(driver, 'find_element_by_xpath', '(//*[@class="ant-input"])', 39, 3, 'bh')
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-primary ant-btn-sm"])', 39, 4)
        click(driver, 'find_element_by_xpath', '(//*[@rel="nofollow"])[2]', 39, 5)
        click(driver, 'find_element_by_xpath', '(//*[@role="button"])[4]', 39, 6)
        click(driver, 'find_element_by_xpath', '(//*[@class="ant-btn ant-btn-sm"])', 39, 7)
    except Exception as error:
        return error.__class__.__name__
    driver.close()
    return True


main()
