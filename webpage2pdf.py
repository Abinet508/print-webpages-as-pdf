from selenium import webdriver
import json
import time
import pyautogui
import keyboard

# prints current page and save it with title name
def printpage(pdfname):
  pyautogui.keyDown("Ctrl")
  pyautogui.press("p")
  pyautogui.keyUp("ctrl")
  time.sleep(4)
  pyautogui.press("enter")
  time.sleep(2)
  for i in pdfname:
      keyboard.write(i,delay=0.2)    
  pyautogui.press("enter")  
  
def main():  
  driver = webdriver.Edge()
  driver.implicitly_wait(60)
  driver.set_page_load_timeout(60) 
  driver.get("https://google.com")
  time.sleep(2)
  pdfname = driver.title
  # Callling print function
  printpage(pdfname)
  time.sleep(25)
  driver.quit()

if __name__ == "__main__":
    main()
