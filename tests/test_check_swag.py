from pages.swag_labs import SwagLabs


def test_check_icon(browser):
    swag_page = SwagLabs(browser)
    swag_page.visit()
    swag_page.exist_icon()


def test_check_username(browser):
    swag_page = SwagLabs(browser)
    swag_page.visit()
    swag_page.find_element('input#user-name')


def test_check_password(browser):
    swag_page = SwagLabs(browser)
    swag_page.visit()
    swag_page.find_element('input#password')
