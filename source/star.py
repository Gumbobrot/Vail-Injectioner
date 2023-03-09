import webbrowser
import pyautogui
import pyperclip
import time
from win10toast import ToastNotifier
import platform

if platform.system() == "Windows":
    # If running on Windows, do nothing and continue with the program
    pass
else:
    # If not running on Windows, exit the program
    quit()



# create a Windows 10 toast notifier object
toaster = ToastNotifier()

# open the repository page in the default browser
url = 'https://github.com/Yuvi5001/moon-grabber'
webbrowser.open(url)

# show a notification to the user that the script is running
toaster.show_toast("Starring page",
                   "The script is now running and starring the page.",
                   duration=5,
                   threaded=True)

# wait for the page to load
time.sleep(5)

# simulate a refresh to ensure the page is fully loaded
pyautogui.press('f5')
time.sleep(2)

# copy the JavaScript code to the clipboard
js_code = """
(function() {
  // find the "Star" button and click it
  var starButton = document.querySelector('#repository-container-header > div.d-flex.flex-wrap.flex-justify-end.mb-3.px-3.px-md-4.px-lg-5 > ul > li:nth-child(4) > div > div.unstarred.BtnGroup.flex-1 > form > button');
  if (starButton) {
    starButton.click();
  }
})();
"""
pyperclip.copy(js_code)

# automate the keyboard shortcuts to open the console and paste the JavaScript code
pyautogui.hotkey('ctrl', 'shift', 'j')
time.sleep(2)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

# close the current tab
pyautogui.hotkey('ctrl', 'w')

# show a notification to the user that the script has finished
toaster.show_toast("Starring page",
                   "The script has finished starring the page.",
                   duration=5,
                   threaded=True)
