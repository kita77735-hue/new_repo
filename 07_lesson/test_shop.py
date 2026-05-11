from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_shop_checkout(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(driver)
    inventory.add_to_cart("backpack")
    inventory.add_to_cart("t-shirt")
    inventory.add_to_cart("onesie")
    inventory.go_to_cart()
    cart = CartPage(driver)
    cart.proceed_to_checkout()
    checkout = CheckoutPage(driver)
    checkout.fill_customer_info("Никита", "Пономарев", "123456")
    checkout.continue_checkout()
    total = checkout.get_total_price()
    assert "$58.29" in total
