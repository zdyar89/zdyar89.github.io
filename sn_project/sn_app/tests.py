from django.test import TestCase, Client, LiveServerTestCase
from selenium import webdriver
from django.test import SimpleTestCase
from selenium.webdriver.common.keys import Keys
from django.urls import reverse, resolve
from sn_app.views import home, uploadfile, test, stt
import sn_app.urls
import json
# Create your tests here.

##@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
# Create your tests here.


class TestUrls(SimpleTestCase):

    def test_homepage_is_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, sn_app.views.home)

    def test_stt_is_resolved(self):
        url = reverse('stt')
        print(resolve(url))
        self.assertEquals(resolve(url).func, sn_app.views.stt)

class TestViews(TestCase):

    def test_home_request(self):
        client = Client()
        response = client.get(reverse('home'))
        print('TestView_1')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')