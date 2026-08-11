
def test_button_with_dynamic_id(dynamic_id_page):
    dynamic_id_page.load()
    dynamic_id_page.click_button_with_dynamic_id()
    dynamic_id_page.check_current_url_is("http://www.uitestingplayground.com/dynamicid/")