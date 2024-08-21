import time
import pyautogui

# Set the Instagram link you want to follow
instagram_link = "https://www.instagram.com/alessandro_greco_aka_aleff/"

# Press Win + R to open the Run dialog
pyautogui.hotkey('win', 'r')
time.sleep(0.5)

# Type the URL into the Run dialog and press Enter
pyautogui.write(instagram_link)
pyautogui.press('enter')
time.sleep(5)  # Wait for the browser to open and load the page

# Navigate to the Follow button and click it
# This might need adjustment depending on the screen resolution and browser
# Ensure the browser is maximized and the follow button is reachable with tab key presses

# Number of tabs to reach the Follow button (this may vary)
tab_count = 12

# Press the Tab key multiple times to navigate to the Follow button
for _ in range(tab_count):
    pyautogui.press('tab')
    time.sleep(0.2)  # Small delay between each Tab press

# Press Enter to click the Follow button
pyautogui.press('enter')

# Wait for a while to ensure the action is completed
time.sleep(1)

# Close the browser (Alt + F4)
pyautogui.hotkey('alt', 'f4')
