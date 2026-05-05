import json
import os
import math
from datetime import datetime

class MagicLibrarian:
    def __init__(self):
        self.data_dir = "denemelerim"
        self.output_file = "SIHIRLI_KITAP.html"
        self.meta_file = "kitap-meta.json"
        self.index_file = "indeks.json"
        self.chapters = []

    def calculate_read_time(self, text):
        words = len(text.split())
        minutes = math.ceil(words / 200) # Dakikada 200 kelime hızıyla
        return minutes, words

    def get_meta(self):
        if os.path.exists(self.meta_file):
            with open(self.meta_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {"kitap_adi": "Sihirli Kitap", "yazar": "Anonim"}

    def run(self):
        print("📜 Kütüphaneci antik rafları tarıyor...")
        meta = self.get_meta()
        
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

        # Dosyaları oku ve analiz et
        files = sorted([f for f in os.listdir(self.data_dir) if f.endswith(".txt")])
        full_index = {}

        book_content = f"""
        <html>
        <head>
            <style>
                body {{ background-color: #f4f1ea; font-family: 'Georgia', serif; color: #3d2b1f; padding: 50px; line-height: 1.6; }}
                .cover {{ text-align: center; border: 10px double #d4af37; padding: 100px 20px; margin-bottom: 50px; }}
                h1 {{ font-size: 60px; text-transform: uppercase; margin-bottom: 10px; }}
                .author {{ font-size: 24px; font-style: italic; }}
                .toc {{ background: #eee8d5; padding: 20px; border-radius: 5px; margin: 40px 0; }}
                .chapter {{ margin-bottom: 60px; border-bottom: 1px solid #ccc; padding-bottom: 30px; }}
                .stats {{ font-size: 14px; color: #777; }}
                .dropcap {{ float: left; font-size: 75px; line-height: 60px; padding-top: 4px; padding-right: 8px; font-family: 'Times New Roman'; color: #d4af37; }}
            </style>
        </head>
        <body>
            <div class="cover">
                <h1>{meta['kitap_adi']}</h1>
                <div class="author">Yazan: {meta['yazar']}</div>
                <p>Oluşturulma Tarihi: {datetime.now().strftime('%d.%m.%Y')}</p>
            </div>
            <div class="toc"><h2>İçindekiler</h2><ul>
        """

        chapter_bodies = ""
        for f_name in files:
            path = os.path.join(self.data_dir, f_name)
            with open(path, 'r', encoding='utf-8') as f:
                text = f.read().strip()
                if not text: continue
                
                m, w = self.calculate_read_time(text)
                title = f_name.replace(".txt", "").replace("-", " ").title()
                anchor = f_name.replace(".txt", "")
                
                # İndeksle
                full_index[title] = {"dosya": f_name, "kelime": w, "sure": m}
                
                # İçindekilere ekle
                book_content += f'<li><a href="#{anchor}">{title}</a> ({m} dk okuma)</li>'
                
                # Bölüm içeriğini hazırla
                first_letter = text[0]
                rest_of_text = text[1:]
                chapter_bodies += f"""
                <div class="chapter" id="{anchor}">
                    <h2>{title}</h2>
                    <div class="stats">{w} kelime | Yaklaşık {m} dakika okuma süresi</div>
                    <p><span class="dropcap">{first_letter}</span>{rest_of_text}</p>
                </div>
                """

        book_content += "</ul></div>" + chapter_bodies + "</body></html>"

        # Dosyaları kaydet
        with open(self.output_file, 'w', encoding='utf-8') as f:
            f.write(book_content)
        
        with open(self.index_file, 'w', encoding='utf-8') as f:
            json.dump(full_index, f, ensure_ascii=False, indent=4)

        print(f"✅ Üretim Tamamlandı! {self.output_file} hazır.")

if __name__ == "__main__":
    Librarian = MagicLibrarian()
    Librarian.run()
