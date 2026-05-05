import json
import os

def sihirli_kutuphaneci(veri_klasoru="denemelerim", indeks_dosyasi="indeks.json"):
    indeks = {}
    
    if not os.path.exists(veri_klasoru):
        os.makedirs(veri_klasoru)
        print(f"'{veri_klasoru}' isimli yeni bir oda hazırlandı.")
        return
    
    for dosya_adi in os.listdir(veri_klasoru):
        if dosya_adi.endswith(".txt"):
            dosya_yolu = os.path.join(veri_klasoru, dosya_adi)
            
            with open(dosya_yolu, 'r', encoding='utf-8') as f:
                icerik = f.read().strip()
                if icerik.split():
                    anahtar_kelime = icerik.split()[0].lower()
                    indeks[anahtar_kelime] = dosya_adi
                    
    with open(indeks_dosyasi, 'w', encoding='utf-8') as f:
        json.dump(indeks, f, ensure_ascii=False, indent=4)
        
    print(f"Kütüphaneci işini bitirdi! İndeks '{indeks_dosyasi}' dosyasına kaydedildi.")

if __name__ == "__main__":
    if not os.path.exists("denemelerim"):
        os.makedirs("denemelerim", exist_ok=True)
        with open("denemelerim/girizgah.txt", "w", encoding="utf-8") as f:
            f.write("İlk denememizde harika bir başlangıç yapıyoruz.")
        
    sihirli_kutuphaneci()
