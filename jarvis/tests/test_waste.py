import webbrowser
import pyautogui
import time
# chrome = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'

# webbrowser.get(chrome).open("youtube.com", new= 2)
# print("SUCESS")


webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
# webbrowser.get('chrome').open('youtube.com')

youtube_search = input("NNN")
webbrowser.get('chrome').open('youtube.com')
time.sleep(10)
# pyautogui.click()
pyautogui.press('/')
time.sleep(1)
pyautogui.write(youtube_search)
time.sleep(1)
pyautogui.press('enter')


