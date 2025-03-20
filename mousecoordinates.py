import pyautogui
import time

print("Farenizi istediğiniz noktaya götürün. Koordinatlar 5 saniye içinde alınacak...")
time.sleep(5)  # Kullanıcıya fareyi hareket ettirmesi için süre tanır

# Fare pozisyonunu al
x, y = pyautogui.position()
print(f"Fare pozisyonu: ({x}, {y})")