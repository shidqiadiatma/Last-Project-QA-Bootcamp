import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class MaintenanceTest(unittest.TestCase):  # TEST SCENARIO

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())  
    
    def test_a_access_maintenance_wrong_pass(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        browser.maximize_window()
        time.sleep(5)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a/span").click() # maintenance
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/form/div[3]/div/div[2]/input").send_keys('admin124') # input pass
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/form/div[4]/button[2]").click() # tombol confirm
        time.sleep(2)
    
        #validasihtml
        adaText = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/form/div[2]/div[1]/p").text
        self.assertIn('Invalid', adaText)


    def test_b_access_maintenance_success(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        browser.maximize_window()
        time.sleep(5)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a/span").click() # maintenance
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/form/div[3]/div/div[2]/input").send_keys('admin123') # input pass
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/form/div[4]/button[2]").click() # tombol confirm
        time.sleep(2)
        #validasihtml
        adaText = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/h6").text
        
        self.assertIn('Purge', adaText)


    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()            