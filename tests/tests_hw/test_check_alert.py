import time

from pages.alerts import Alerts


def test_alerts(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    assert not alert_page.alert()

    # alert_page.btn_timer_alert.click()
    # time.sleep(5)
    # assert alert_page.alert()
    # alert_page.alert().accept()

    alert_page.btn_timer_alert.click()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        if count == 5:
            assert alert_page.alert()
            alert_page.alert().accept()
            break
        else:
            assert not alert_page.alert()
