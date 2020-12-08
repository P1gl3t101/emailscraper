# The script parses from the mailbox, folders, incoming email addresses into a separate file
# Скрипт парсит из почтового ящика, папки входящие емаил адреса в отдельный файл
#
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from os import system
from time import sleep
from selenium.webdriver.chrome.options import Options
from secrets import username, password



class MailBot():
    def __init__(self):
        #user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'
        
        #opts.add_argument("user-agent=" + user_agent)

        option = webdriver.FirefoxOptions()
        option.set_preference('dom.webdriver.enable', False)
        option.set_preference('dom.webnotifications.enabled', False)
        
        option.set_preference('general.useragent.override','example :)')
       
        # значение True запуск в фоновом режиме
        option.headless = True 
        self.driver = webdriver.Firefox(options=option)
        
       # webdriver браузера chrome 
	   #webdriver chrome
	   #
       #  opts = Options()
       # self.driver = webdriver.Chrome(chrome_options=opts)
       # self.driver.implicitly_wait(10)
       # self.driver.headles = True
       # self.driver = webdriver.Chrome()
       
    
    def login(self):
        self.driver.get('https://mail.ru/')

       # sleep(6)

        login_in = self.driver.find_element_by_xpath('//*[@id="mailbox__login"]')
        login_in.send_keys(username)

        #log_btn = self.driver.find_element_by_xpath('//*[@id="mailbox:submit-button"]/input')
        #log_btn.click()

    def passw(self):

        

        pass_in = self.driver.find_element_by_xpath('//*[@id="mailbox__password"]')
        pass_in.send_keys(password)
        
        sleep(5)
       
        pass_btn = self.driver.find_element_by_xpath('//*[@id="mailbox__auth__button"]')
        pass_btn.click()

        #base_window = self.driver.window_handles[0]
        #self.driver.switch_to_window(self.driver.window_handles[0])
        #sleep(60)

    def brif(self):
        
        sleep(15)
        #brif_btn = self.driver.find_element_by_xpath('/html/body/div[8]').click()
        btn_one = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[6]/div[2]/div[2]/div[4]/div/div[2]/div/div[2]/div[1]/div/a')
        btn_one.click()
        while True: 
            sleep(5)
           
            inform_btn = self.driver.find_element_by_css_selector(".b-letter__head__addrs__from > span:nth-child(1)")
            
            inform_btn.click()
            email = self.driver.find_element_by_class_name("b-contact-informer__email")
                   # lines = add_mail1.text
            print(email.text)
            lines = email.text           
                        #print(add_mail1.text)
            with open("test.txt", "a") as file:
            #    for j in lines:
                  file.write(str(lines)+'\n')
                  file.close()   
                         
            sleep(5)
            next_btn = self.driver.find_element_by_css_selector("#b-toolbar__right > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)")
            
            next_btn.click()
            #sleep(5)
           # self.driver.refresh()
           
bot = MailBot()  
bot.login()  
bot.passw() 
   
bot.brif()

system('pause')