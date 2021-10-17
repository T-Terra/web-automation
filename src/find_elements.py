from pyautogui import hotkey
from datetime import date
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


hours_ = ["08:00", "12:00", "13:00", "18:00"]
Chrome_options = Options()
Chrome_options.set_headless(headless=False)
driver = Chrome(options=Chrome_options)
driver.set_window_size(1024, 768)
driver.get("https://atecsoft.com.br/modweb/31364769000112/atecsoftweb.dll/m")
weekday = date.today().weekday()


# find the user element
def find_user():
  sleep(3)
  elem = driver.find_element_by_id("ext-element-38")
  sleep(1)
  elem.send_keys("9")
  elem.send_keys(Keys.RETURN)
  

# find the element for the password
def find_password():
  sleep(1)
  elem = driver.find_element_by_id("ext-element-51")
  sleep(1)
  elem.send_keys("123456")
  elem.send_keys(Keys.RETURN)
  

# find the button to log into the system
def button_enter():
  sleep(1)
  elem = driver.find_element_by_id("ext-element-30")
  sleep(1)
  elem.click()

# find the register element
def register_click():
  sleep(1)
  elem = driver.find_element_by_id("ext-element-116")
  sleep(1)
  elem.click()
  
# find the button Map
def click_map():
  sleep(1)
  elem = driver.find_element_by_id("ext-element-177")
  sleep(1)
  elem.click()

# find the button finally operation
def click_register_operation():
  sleep(1)
  elem = driver.find_element_by_id("ext-element-190")
  sleep(1)
  elem.click()

# Find pop-up and finally operation
def button_yes():
  sleep(1)
  elem = driver.find_element_by_xpath(f"//*[@id='ext-element-213']")
  sleep(1)
  elem.click()

# Get hours of web site
def get_hours():
  elem = driver.find_element_by_id("ext-element-187").text
  hours_of_elem = elem.split(":")[0]
  minutes_of_elem = elem.split(":")[1]
  return hours_of_elem + ":" + minutes_of_elem
  
  
def except_days():
  if weekday != 4:
    find_user()
    find_password()
    button_enter()
    register_click()
    click_map()
    if get_hours() in hours_:
      click_register_operation()
      button_yes()
      print(f"\n{hours_}")
      sleep(3)
      driver.close()
      sleep(1)
      hotkey('ctrl', 'c')
    else:
      print("\nHorário não existe na lista!!!")
      sleep(3)
      driver.close()
      sleep(1)
      hotkey('ctrl', 'c')
  else:
    find_user()
    find_password()
    button_enter()
    register_click()
    click_map()
    hours_.pop()
    hours_.append("17:00")
    if get_hours() in hours_:
      click_register_operation()
      button_yes()
      print(f"\n{hours_}")
      sleep(3)
      driver.close()
      sleep(1)
      hotkey('ctrl', 'c')
    else:
      print("\nHorário não existe na lista de sexta-feira!!!")
      sleep(3)
      driver.close()
      sleep(1)
      hotkey('ctrl', 'c')
    

"""
returns:
  0 -> Segunda-feira
  1 -> Terça-feira
  2 -> Quarta-feira
  3 -> Quinta-feira
  4 -> Sexta-feira
  5 -> Sábado
  6 -> Domingo
"""