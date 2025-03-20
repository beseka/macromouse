import pyautogui
import time

# Tıklanacak koordinatlar
click_points = [
    (-1355, 1000),  # Örnek: İlk tıklama noktası
    (-467, 184),    # Örnek: İkinci tıklama noktası
    (-1217, 459),   # Örnek: Üçüncü tıklama noktası
    (-1220, 761),   # Örnek: Dördüncü tıklama noktası
]

# Her tıklama arasındaki gecikme (saniye)
delay = 15 # 1 saniye
extra_delay = 5 # 4 tıklamadan sonra ek gecikme

def controlled_sleep(seconds):
    """Kesintiye uğrayabilen bir bekleme fonksiyonu."""
    start = time.time()
    while time.time() - start < seconds:
        time.sleep(0.1)  # Küçük aralıklarla bekleme, Ctrl + C'yi yakalayabilir

def main():
    print("Program başlıyor. Çıkmak için 'Ctrl + C' tuşlarına basın.")
    controlled_sleep(5)  # Kullanıcıya başlangıç için 5 saniye bekleme
    
    click_count = 0

    while True:
        for point in click_points:
            x, y = point
            pyautogui.moveTo(x, y, duration=0.5)  # Fareyi belirli bir noktaya taşır
            pyautogui.click()  # Belirtilen noktaya tıklar
            print(f"Tıklandı: {x}, {y}")
            click_count += 1  # Tıklama sayısını artır
            
            # 4 tıklama sonrası ekstra bekleme
            if click_count % 4 == 0:
                print(f"{click_count} tıklamadan sonra {extra_delay} saniye bekleniyor...")
                controlled_sleep(extra_delay)
            else:
                controlled_sleep(delay)  # Normal gecikme

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram durduruldu.")
