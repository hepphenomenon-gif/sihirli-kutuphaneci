import json
import os

def e_kitap_birlestirici(veri_klasoru="denemelerim", cikti_dosyasi="E-KITAP.md", meta_dosyasi="kitap-meta.json", indeks_dosyasi="indeks.json"):
    icerikler = []
    
    kitap_adi = "Sihirli Kütüphaneci"
    yazar = "Yazar"
    if os.path.exists(meta_dosyasi):
        with open(meta_dosyasi, 'r', encoding='utf-8') as f:
            meta = json.load(f)
            kitap_adi = meta.get("kitap_adi", kitap_adi)
            yazar = meta.get("yazar", yazar)
            
    icerikler.append(f"# {kitap_adi}\n")
    icerikler.append(f"**Yazar:** {yazar}\n\n---\n\n")
    
    if os.path.exists(veri_klasoru):
        dosyalar = sorted([d for d in os.listdir(veri_klasoru) if d.endswith(".txt")])
        for dosya in dosyalar:
            dosya_yolu = os.path.join(veri_klasoru, dosya)
            with open(dosya_yolu, 'r', encoding='utf-8') as f:
                metin = f.read().strip()
                baslik = dosya.split('.')[0].replace('-', ' ').title()
                icerikler.append(f"## {baslik}\n\n")
                icerikler.append(f"{metin}\n\n---\n\n")
                
    with open(cikti_dosyasi, 'w', encoding='utf-8') as f:
        f.writelines(icerikler)
        
    print(f"E-kitap başarıyla birleştirildi: {cikti_dosyasi}")

if __name__ == "__main__":
    e_kitap_birlestirici()
