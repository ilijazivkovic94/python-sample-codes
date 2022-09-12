import pyautogui, time

time.sleep(5)
print('Press Ctrl-C to quit.')

# pos = pyautogui.locateOnScreen('vm.png')
# center_pos = pyautogui.center(pos)
# print(center_pos)
# pyautogui.click(center_pos)

distance = 200
while distance > 0:
  pyautogui.dragRel(distance, 0, duration=0.2)   # move right
  distance = distance - 5
  pyautogui.dragRel(0, distance, duration=0.2)   # move down
  pyautogui.dragRel(-distance, 0, duration=0.2)  # move left
  distance = distance - 5
  pyautogui.dragRel(0, -distance, duration=0.2)  # move up

# for i in range(2):
#   pyautogui.moveRel(100, 0, duration=0.25)
#   pyautogui.moveRel(0, 100, duration=0.25)
#   pyautogui.moveRel(-100, 0, duration=0.25)
#   pyautogui.moveRel(0, -100, duration=0.25)

# pyautogui.click(10, 5)