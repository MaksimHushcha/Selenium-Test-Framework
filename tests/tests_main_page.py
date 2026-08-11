from pages.main_page import MainBasePage

def test_dynamic_id_link(driver):
    main_page = MainBasePage(driver)
    main_page.load()
    main_page.click_dynamic_id()