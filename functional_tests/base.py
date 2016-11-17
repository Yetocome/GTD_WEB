from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import sys

class FunctionalTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):    # 用于设定下整个类的测试背景，该方法只会执行一次，而不会在每个测试方法运行前都执行。
                            # LiveServerTestCase和StaticLiveServerTestCase一般都在这个方法中启动测试服务器。
        for arg in sys.argv:
            if 'liveserver' in arg:     # 在命令行中查找参数liveserver
                cls.server_url = 'http://' + arg.split('=')[1]
                # 如果找到，把过渡服务器的URL赋值给server_url变了
                cls.live_server_url = cls.server_url
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()

    def setUp(self):
        self.browser = webdriver.Chrome('/Users/xmh/Desktop/python/chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        self.assertIn(row_text, [row.text for row in rows])

    def get_item_input_box(self):
        return self.browser.find_element_by_id('id_text')
