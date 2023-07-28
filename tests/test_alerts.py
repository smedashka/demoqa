import time

from pages.alerts import Alerts


def test_alerts(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    assert not alert_page.alert()

    alert_page.btn_alert.click()
    time.sleep(2)
    assert alert_page.alert()
    alert_page.alert().accept()


def test_alert_text(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    alert_page.btn_alert.click()
    time.sleep(2)
    assert alert_page.alert().text == 'You clicked a button'
    alert_page.alert().accept()
    assert not alert_page.alert()


def test_confirm(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    alert_page.btn_confirm.click()
    time.sleep(2)
    alert_page.alert().dismiss()
    assert alert_page.confirm_res_text.get_text() == 'You selected Cancel'


def test_promt(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    alert_page.btn_promt.click()
    time.sleep(2)

    name = 'Test'

    alert_page.alert().send_keys(name)
    alert_page.alert().accept()
    assert alert_page.promt_res_text.get_text() == 'You entered ' + name




