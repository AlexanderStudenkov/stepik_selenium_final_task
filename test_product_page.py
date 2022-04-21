from .pages.product_page import ProductPage
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

# найденный номер промо с ошибкой
fn = 7
# range(10) первоначально для поиска промо с ошибкой
links = ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'+str(i) for i in range(1)]


@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.guest_can_add_product_to_basket()