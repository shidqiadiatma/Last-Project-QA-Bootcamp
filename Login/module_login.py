from lib2to3.pgen2 import driver 
import unittest 
import time 
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.support.ui import Select 
 
class Test(unittest.TestCase): 
    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install()) 
 
    def test_success_login(self): 
        driver=self.driver 
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") 
        time.sleep(2) 
        driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin") #mencari elemet email 
        time.sleep(2) 
        driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123") 
        time.sleep(2) 
        driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click() 
        time.sleep(5) 
        
    def tearDown(self):
        self.driver.close()
        
        
        # test case : login with wrong password
    def test_failed_login(self): 
        driver=self.driver 
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") 
        time.sleep(2) 
        driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin") #mencari elemet email 
        time.sleep(2) 
        driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("123admin") 
        time.sleep(2) 
        driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click() 
        time.sleep(5) 
        response_data = driver.find_element(By.ID,"spanMessage").text
        self.assertEqual(response_data, 'Invalid credentials')
        self.driver.close() 
 
if __name__ == "__main__": 
    unittest.main()