import time
# import pytest
# from selenium import webdriver
from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.select import Select

from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_search(self):   #test for search field

        log = self.getLogger()
        self.driver.find_element_by_xpath('//i[@class="pe-7s-search"]').click()
        log.info("placing search query into the search field")
        self.driver.find_element_by_id('search').send_keys('Introducing the Everlasting Bicycle Frame')
        time.sleep(2)
        log.info("Search sample is displayed")
        search_result = self.driver.find_elements_by_css_selector("li[class='item post post-item'] a")
        print(len(search_result))
        for result in search_result:
            if result.text == 'Introducing the Everlasting Bicycle Frame':
                result.click()
                break
        pageTitle = self.driver.find_element_by_xpath("//h1[@class='page-header']").text
        log.info("text received from page is " + pageTitle)
        assert ("Introducing the Everlasting Bicycle Frame" in pageTitle)


    def test_bikes_portfolio(self):        # test for redirect to the page with bikes categories

        log = self.getLogger()
        self.driver.find_element_by_xpath("//span[contains(text(),'Bikes')]").click()
        bikesCategories = self.driver.find_element_by_xpath("//ul[@id='tabs_categories_porfolio']").text
        log.info("Text received from this page is " + bikesCategories)
        assert (("All Works") or ("E-Bikes") or ("City Bikes") or ("Cargo Bike") in bikesCategories)

    def test_accessories_page(self):       # test for redirect to the page with accessories categories

        log = self.getLogger()
        self.driver.find_element_by_xpath("//span[@data-hover='Accessories']").click()
        accessoriesCatogories = self.driver.find_element_by_class_name('landing-categories').text
        log.info("system displays a list of accessories present on this page: " + accessoriesCatogories)
        assert (("OKO") or ("OKO LS") or ("AMS") or ("PEK") in accessoriesCatogories)


    def test_static_dropdown_home_page_the_story(self):  # test for The Story page redirect
        log = self.getLogger()
        action = ActionChains(self.driver)
        log.info("system goes to the dropdown")
        drop_down_menu = self.driver.find_element_by_xpath \
        ("//a[@class='level0 dropdown-toggle']//span[contains(text(),'Biomega')]")
        action.move_to_element(drop_down_menu).perform()
        log.info("system displays dropdown options and selects THE STORY")
        element_to_select = self.driver.find_element_by_xpath("//a[contains(text(),'The Story')]")
        element_to_select.click()
        the_story_Header = self.driver.find_element_by_xpath("//h1[@class='page-header']").text
        assert (("The Story") in the_story_Header)

    def test_static_dropdown_home_page_the_community(self):   # test for The Community page redirect
        log = self.getLogger()
        action = ActionChains(self.driver)
        drop_down_menu = self.driver.find_element_by_xpath \
        ("//a[@class='level0 dropdown-toggle']//span[contains(text(),'Biomega')]")
        action.move_to_element(drop_down_menu).perform()

        element_to_select = self.driver.find_element_by_xpath("//a[contains(text(),'The Community')]")
        element_to_select.click()
        the_community_Header = self.driver.find_element_by_xpath("//h1[@class='page-header']").text
        assert (("The Community") in the_community_Header)

    def test_static_dropdown_home_page_our_designers(self):
        log = self.getLogger()
        action = ActionChains(self.driver)
        drop_down_menu = self.driver.find_element_by_xpath \
        ("//a[@class='level0 dropdown-toggle']//span[contains(text(),'Biomega')]")
        action.move_to_element(drop_down_menu).perform()

        element_to_select = self.driver.find_element_by_xpath("//a[contains(text(),'Our Designers')]")
        element_to_select.click()
        our_designers_page = self.driver.find_element_by_xpath("//span[contains(text(),'OUR PHILOSOPHY')]").text
        assert (("OUR PHILOSOPHY") in our_designers_page)

    def test_static_dropdown_home_page_who_we_are(self):   # test for Who We Are page redirect
        log = self.getLogger()
        action = ActionChains(self.driver)
        drop_down_menu = self.driver.find_element_by_xpath \
        ("//a[@class='level0 dropdown-toggle']//span[contains(text(),'Biomega')]")
        action.move_to_element(drop_down_menu).perform()

        element_to_select = self.driver.find_element_by_xpath("//a[contains(text(),'Who are we?')]")
        element_to_select.click()
        who_are_we_page = self.driver.find_element_by_xpath("//h1[@class='page-header']").text
        assert(("Our design philosophy") in who_are_we_page)

    #def test_currency_selection_dkk(self):  # test for DKK currency selection
        #log = self.getLogger()
        #self.driver.find_element_by_xpath("//a[contains(text(),'DKK')]").click()
        #self.driver.find_element_by_xpath("//span[contains(text(),'DKK')]")
        #assert(())

    #def test_currency_selection_usd(self):  # test for USD currency selection
        #log = self.getLogger()
        #self.driver.find_element_by_xpath("//a[contains(text(),'USD')]").click()
        #time.sleep(2)
        #self.driver.find_element_by_xpath("//span[contains(text(),'Bikes')]").click()
        #time.sleep(3)

    def test_book_a_test_ride(self):    # test for booking a test ride page redirect
        log = self.getLogger()
        self.driver.find_element_by_class_name('cto-btn-primary').click()
        book_ride = self.driver.find_element_by_xpath("//h1[@class='page-header']").text
        assert (("Biomega retailers") in book_ride)

    def test_find_retailer_page(self):  # test for find retailer page redirect
        log = self.getLogger()
        self.driver.find_element_by_class_name('cto-btn-default').click()
        retailers = self.driver.find_element_by_xpath("//h1[@class='page-header']").text
        assert(("Store Locator") in retailers)

    def test_footer_customer_care_terms_and_conditions(self):
        log = self.getLogger()
        self.driver.find_element_by_xpath("//a[contains(text(),'Terms and conditions')]").click()
        terms_conditions = self.driver.find_element_by_xpath("//h1[@class='page-header']").text
        assert (("Terms and conditions") in terms_conditions)

    def test_footer_customer_care_cookie_policy(self):
        log = self.getLogger()
        self.driver.find_element_by_xpath("//a[contains(text(),'Cookie policy')]").click()
        cookie_policy = self.driver.find_element_by_xpath("//h1[@class='page-header']").text
        assert(("Privatlivs and cookiepolitik") in cookie_policy)

    def test_footer_customer_care_returns(self):
        log = self.getLogger()
        self.driver.find_element_by_xpath("//a[contains(text(),'Returns')]").click()
        returns = self.driver.find_element_by_xpath("//h1[@class='page-header']").text
        assert(("Terms and conditions") in returns)

    def test_footer_customer_contact_successful(self):
        log = self.getLogger()
        self.driver.find_element_by_xpath("//a[@tabindex='0'][contains(text(),'Contact')]").click()
        self.driver.find_element_by_xpath("//input[@id='name']").send_keys('name')
        self.driver.find_element_by_xpath("//input[@id='email']").send_keys('tetiana.nishtuk@gmail.com')
        self.driver.find_element_by_xpath("//textarea[@id='comment']").send_keys('test text')
        self.driver.find_element_by_xpath("//span[contains(text(),'Send')]").click()
        time.sleep(2)
        contact_form_success = self.driver.find_element_by_xpath("//div[@class='message-success success message']").text
        assert(("Thanks for contacting us with your comments and questions. We'll respond to you very soon.") in contact_form_success)

    def test_footer_customer_contact_failed(self):
        log = self.getLogger()
        self.driver.find_element_by_xpath("//a[@tabindex='0'][contains(text(),'Contact')]").click()
        self.driver.find_element_by_xpath("//input[@id='name']").send_keys('')
        self.driver.find_element_by_xpath("//input[@id='email']").send_keys('')
        self.driver.find_element_by_xpath("//textarea[@id='comment']").send_keys('')
        self.driver.find_element_by_xpath("//span[contains(text(),'Send')]").click()
        time.sleep(2)
        contact_form_fail = self.driver.find_element_by_xpath("//div[@id='comment-error']").text
        assert(("This is a required field.") in contact_form_fail)

    def test_footer_general_about_biomega(self):
        log = self.getLogger()
        self.driver.find_element_by_xpath("//a[contains(text(),'About Biomega')]").click()
        about_biomega = self.driver.find_element_by_xpath("//h1[@class='page-header']").text
        assert(("About Biomega") in about_biomega)

    def test_footer_general_our_story(self):
        log = self.getLogger()
        self.driver.find_element_by_xpath("//a[contains(text(),'Our Story')]").click()
        assert self.driver.find_element_by_xpath("//main[@id='maincontent']")

    def test_footer_general_retailers(self):
        log = self.getLogger()
        self.driver.find_element_by_xpath("//a[contains(text(),'Retailers')]").click()
        assert self.driver.find_element_by_xpath("//main[@id='maincontent']")

    def test_basket_add_bike_remove_from_basket(self):
        log = self.getLogger()
        self.driver.find_element_by_xpath("//span[contains(text(),'Bikes')]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//a[contains(text(),'AMS')]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//div[@id='option-label-color-93-item-5441']").click()
        self.driver.find_element_by_xpath("//div[@id='option-label-size-205-item-5467']").click()
        self.driver.find_element_by_xpath("//div[@id='option-label-speed-206-item-5457']").click()
        self.driver.find_element_by_xpath("//button[@id='product-addtocart-button']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//span[contains(text(),'Go To Cart')]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//span[@class='fa fa-trash']").click()
        time.sleep(3)
        no_items_in_basket_message = self.driver.find_element_by_xpath("//section[@id='maincontent']//div[@class='row']").text
        assert (("You have no items in your shopping cart") in no_items_in_basket_message)

    def test_basket_add_bike_change_quantity(self):
        log = self.getLogger()
        self.driver.find_element_by_xpath("//span[contains(text(),'Bikes')]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//a[contains(text(),'PEK')]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//div[@id='option-label-color-93-item-5441']").click()
        self.driver.find_element_by_xpath("//div[@id='option-label-size-205-item-5468']").click()
        self.driver.find_element_by_xpath("//div[@id='option-label-speed-206-item-5462']").click()
        self.driver.find_element_by_xpath("//span[@class='edit-qty plus disable-select-text']").click()
        self.driver.find_element_by_xpath("//button[@id='product-addtocart-button']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//span[contains(text(),'Go To Cart')]").click()
        time.sleep(2)
        shopping_cart = self.driver.find_element_by_xpath("//h1[@class='page-header']").text
        assert (("Shopping Cart") in shopping_cart)



    def test_find_bike_by_sku(self):
        log = self.getLogger()
        self.driver.find_element_by_xpath('//i[@class="pe-7s-search"]').click()
        self.driver.find_element_by_id('search').send_keys('57000')
        time.sleep(2)
        self.driver.find_element_by_xpath("//i[@class='pe-7s-play arrow']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[contains(@class,'product-top')]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@id='option-label-color-93-item-5441']").click()
        self.driver.find_element_by_xpath("//div[@id='option-label-size-205-item-5468']").click()
        self.driver.find_element_by_xpath("//div[@id='option-label-speed-206-item-5462']").click()
        self.driver.find_element_by_xpath("//button[@id='product-addtocart-button']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//span[contains(text(),'Go To Cart')]").click()
        time.sleep(2)
        shopping_cart = self.driver.find_element_by_xpath("//h1[@class='page-header']").text
        assert (("Shopping Cart") in shopping_cart)

    def test_find_accessory_by_sku(self):
        log = self.getLogger()
        self.driver.find_element_by_xpath('//i[@class="pe-7s-search"]').click()
        self.driver.find_element_by_id('search').send_keys('10030')
        time.sleep(2)
        self.driver.find_element_by_xpath("//i[@class='pe-7s-play arrow']").click()
        self.driver.find_element_by_xpath("//div[@class='product-top']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[@id='product-addtocart-button']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//span[contains(text(),'Go To Cart')]").click()
        time.sleep(2)
        shopping_cart = self.driver.find_element_by_xpath("//h1[@class='page-header']").text
        assert (("Shopping Cart") in shopping_cart)

    def test_find_accessory_by_sku_checkout_proceed(self):
        log = self.getLogger()
        self.driver.find_element_by_xpath('//i[@class="pe-7s-search"]').click()
        self.driver.find_element_by_id('search').send_keys('10030')
        time.sleep(2)
        self.driver.find_element_by_xpath("//i[@class='pe-7s-play arrow']").click()
        self.driver.find_element_by_xpath("//div[@class='product-top']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[@id='product-addtocart-button']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[@id='top-cart-btn-checkout']").click()
        time.sleep(3)
        shipping_address = self.driver.find_element_by_xpath("//div[contains(text(),'Shipping Address')]").text
        assert (("Shipping Address") in shipping_address)

    def test_find_by_OKO_request(self):
        log = self.getLogger()
        self.driver.find_element_by_xpath('//i[@class="pe-7s-search"]').click()
        self.driver.find_element_by_id('search').send_keys('oko')
        time.sleep(2)
        self.driver.find_element_by_xpath("//i[@class='pe-7s-play arrow']").click()
        search_result = self.driver.find_element_by_xpath("//h1[@class='page-header']").text
        assert("Search results for: 'oko'" in search_result)
