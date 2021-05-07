# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from time import sleep
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium import webdriver
# import secrets
# import string
# alphabet = string.ascii_letters + string.digits
# password = ''.join(secrets.choice(alphabet) for i in range(20))


# class EmailGen:
    
#     ''' Open google chrome '''
#     def __init__(self):
#         self.driver = webdriver.Chrome()
#         self.wait = WebDriverWait(self.driver, 6)

#     ''' Open tutanota.com '''
#     def open_browser(self, url):
#         self.driver.get(url)

#     def skip_select(self):                        
#         skip_select =self.driver.find_element_by_xpath("//*[@id='upgrade-account-dialog']/div[2]/div[1]/div[1]/div[4]")
#         skip_select.click()      

#     def accept_rules1(self):                        
#         accept_rules1 =self.driver.find_element_by_xpath("//*[@id='modal']/div[2]/div/div/div/div[2]/div[1]")
#         accept_rules1.click()  

#     def accept_rules2(self):                        
#         accept_rules2 =self.driver.find_element_by_xpath("//*[@id='modal']/div[2]/div/div/div/div[2]/div[2]/div/div")
#         accept_rules2.click()
          

#     def accept_rules(self):                        
#         accept_rules =self.driver.find_element_by_xpath("//*[@id='modal']/div[2]/div/div/div/div[3]/button[2]/div/div")
#         accept_rules.click() 



#     def accpet_2(self):                        
#         accept_rules =self.driver.find_element_by_xpath("//*[@id='signup-account-dialog']/div/div[4]/div/div")
#         accept_rules.click()
    
#     def acc_ge():
#         while True:
#             alphabet=string.ascii_letters.lower()
#             email1="".join(secrets.choice(alphabet)for i in range(14))+"".join(secrets.choice(string.digits)for i in range(3))
#             print('email: ',email1)

#             alphabet=string.ascii_letters +')(*&^%$#@!~=+' +string.digits
#             password1="".join(secrets.choice(alphabet)for i in range(20))
#             print('password: ',password1)
#             print('----------------------')


# if __name__ == '__main__':
#     emails = EmailGen()
#     emails.open_browser('https://mail.tutanota.com/signup#theme=blue')
#     sleep(4)
#     emails.skip_select()
#     emails.accept_rules1()
#     emails.accept_rules2()
#     emails.accept_rules()
#     sleep(3)
#     emails.accept_2()






# def captcha():
#     captcha_list= [
#     "01:05","01:10","01:15","01:20","01:25","01:30","01:35","01:40","01:45","01:50","01:55","01:00",
#     "02:05","02:10","02:15","02:20","02:25","02:30","02:35","02:40","02:45","02:50","02:55","02:00",
#     "03:05","03:10","03:15","03:20","03:25","03:30","03:35","03:40","03:45","03:50","03:55","03:00",
#     "04:05","04:10","04:15","04:20","04:25","04:30","04:35","04:40","04:45","04:50","04:55","04:00",
#     "05:05","05:10","05:15","05:20","05:25","05:30","05:35","05:40","05:45","05:50","05:55","05:00",
#     "06:05","06:10","06:15","06:20","06:25","06:30","06:35","06:40","06:45","06:50","06:55","06:00",
#     "07:05","07:10","07:15","07:20","07:25","07:30","07:35","07:40","07:45","07:50","07:55","07:00",
#     "08:05","08:10","08:15","08:20","08:25","08:30","08:35","08:40","08:45","08:50","08:55","08:00",
#     "09:05","09:10","09:15","09:20","09:25","09:30","09:35","09:40","09:45","09:50","09:55","09:00",
#     "10:05","10:10","10:15","10:20","10:25","10:30","10:35","10:40","10:45","10:50","10:55","10:00",
#     "11:05","11:10","11:15","11:20","11:25","11:30","11:35","11:40","11:45","11:50","11:55","11:00",
#     "12:05","12:10","12:15","12:20","12:25","12:30","12:35","12:40","12:45","12:50","12:55","12:00",]
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import secrets
import string
import json
alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(20))


a={"email":"kaskos1211" , "password":'AvGF$#'}
json_object = json.dumps(a, indent = 4)

# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)


class EmailGen:
    
    ''' Open google chrome '''
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 6)

    ''' Open tutanota.com '''
    def open_browser(self, url):
        self.driver.get(url)

    def skip_select(self):                        
        skip_select =self.driver.find_element_by_xpath("//*[@id='upgrade-account-dialog']/div[2]/div[1]/div[1]/div[4]")
        skip_select.click()      

    def accept_rules1(self):                        
        accept_rules1 =self.driver.find_element_by_xpath("//*[@id='modal']/div[2]/div/div/div/div[2]/div[1]")
        accept_rules1.click()  

    def accept_rules2(self):                        
        accept_rules2 =self.driver.find_element_by_xpath("//*[@id='modal']/div[2]/div/div/div/div[2]/div[2]/div/div")
        accept_rules2.click()
          

    def accept_rules(self):                        
        accept_rules =self.driver.find_element_by_xpath("//*[@id='modal']/div[2]/div/div/div/div[3]/button[2]/div/div")
        accept_rules.click() 

    def accept_1(self):                        
        accept_1 =self.driver.find_element_by_xpath("//*[@id='signup-account-dialog']/div/div[3]/div/input")
        accept_1.click() 

    def accept_2(self):                        
        accept_2 =self.driver.find_element_by_xpath("//*[@id='signup-account-dialog']/div/div[4]/div/div")
        accept_2.click() 

    def fill_email(self):   
        fill_email =self.driver.find_element_by_xpath("//*[@id='signup-account-dialog']/div/div[1]/div/div/div/div[1]/input")
        fill_email.send_keys("safahisidiotbruh")

    
    def fill_pass(self):   
        fill_pass = self.driver.find_element_by_xpath("//*[@id='signup-account-dialog']/div/div[2]/div[1]/div[1]/div/div/div[1]/input[4]")
        rep_pass = self.driver.find_element_by_xpath("//*[@id='signup-account-dialog']/div/div[2]/div[3]/div[1]/div/div/div/input")
        fill_pass.send_keys("test!@$Jfd$234")
        sleep(1)
        rep_pass.send_keys("test!@$Jfd$234")


    def next_click(self):                        
        next_click =self.driver.find_element_by_xpath("//*[@id='signup-account-dialog']/div/div[5]/button/div/div")
        next_click.click() 

        
    def fill_cap(self):
        fill_cap = self.driver.find_element_by_xpath("//*[@id='modal']/div[3]/div/div/div/div[2]/div/div[1]/div/div/div/input")
        cap_ok = self.driver.find_element_by_xpath("//*[@id='modal']/div[3]/div/div/div/div[1]/div/div[3]/button/div/div")
        cap_try_again =self.driver.find_element_by_xpath("//*[@id='modal']/div[3]/div/div/div/div[2]/button/div/div")
        captcha_list= [
                        "01:05","01:10","01:15","01:20","01:25","01:30","01:35","01:40","01:45","01:50","01:55","01:00",
                        "02:05","02:10","02:15","02:20","02:25","02:30","02:35","02:40","02:45","02:50","02:55","02:00",
                        "03:05","03:10","03:15","03:20","03:25","03:30","03:35","03:40","03:45","03:50","03:55","03:00",
                        "04:05","04:10","04:15","04:20","04:25","04:30","04:35","04:40","04:45","04:50","04:55","04:00",
                        "05:05","05:10","05:15","05:20","05:25","05:30","05:35","05:40","05:45","05:50","05:55","05:00",
                        "06:05","06:10","06:15","06:20","06:25","06:30","06:35","06:40","06:45","06:50","06:55","06:00",
                        "07:05","07:10","07:15","07:20","07:25","07:30","07:35","07:40","07:45","07:50","07:55","07:00",
                        "08:05","08:10","08:15","08:20","08:25","08:30","08:35","08:40","08:45","08:50","08:55","08:00",
                        "09:05","09:10","09:15","09:20","09:25","09:30","09:35","09:40","09:45","09:50","09:55","09:00",
                        "10:05","10:10","10:15","10:20","10:25","10:30","10:35","10:40","10:45","10:50","10:55","10:00",
                        "11:05","11:10","11:15","11:20","11:25","11:30","11:35","11:40","11:45","11:50","11:55","11:00",
                        "12:05","12:10","12:15","12:20","12:25","12:30","12:35","12:40","12:45","12:50","12:55","12:00"]

        for i in captcha_list: 
            sleep(1)
            if fill_cap:
                fill_cap.send_keys(i)  
                sleep(1)
                cap_ok.click() 
                sleep(1)
                cap_try_again.click() 
                sleep(1)
            else:
                break

         


if __name__ == '__main__':
    emails = EmailGen()
    emails.open_browser('https://mail.tutanota.com/signup#theme=blue')
    sleep(4)
    emails.skip_select()
    emails.accept_rules1()
    emails.accept_rules2()
    emails.accept_rules()
    sleep(1)
    emails.accept_1()
    emails.accept_2()
    emails.fill_email() 
    sleep(8)
    emails.fill_pass() 
    sleep(1)
    emails.next_click()
    sleep(25)
    emails.fill_cap()
