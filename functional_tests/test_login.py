from .base import FunctionalTest

class NewVisitorTest(FunctionalTest):
    def test_can_register_as_a_new_user(self):
        # 听说有个好用的在线gtd网站
        # 点开首页
        self.browser.get(self.server_url)
        # 注意到网页的标题和头部都有"MyGTD"的字样
        self.assertIn('MyGTD', self.browser.title)
        

class UserVisitorTest(FunctionalTest):
    def test_can_login(self):
        pass
