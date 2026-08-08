# Tekne Usta — SEO & GEO Büyüme Playbook'u

> Amaç: jenerik aramalarda ("tekne tamiri", "osmoz tedavisi", "tekne boyama fiyatları" vb.) üst sıralara çıkmak, orada kalmak ve AI asistanlarınca (ChatGPT, Gemini, Perplexity) önerilmek → sürekli lead.
> Site tarafı (teknik SEO + 73 makale + schema + sitemap + llms.txt) hazır. Bu belge, **siteyi besleyen ve sıralamayı sürdüren dış + sürekli işleri** kapsar.

---

## NAP Kartı (her yerde BİREBİR aynı kullan)
Tutarlı NAP (Name-Address-Phone), yerel SEO'nun temelidir. Her dizin/profilde aynen:
- **İsim:** Tekne Usta
- **Telefon:** +90 532 173 89 78
- **Web:** https://www.tekneusta.com
- **E-posta:** info@tekneusta.com
- **Bölge:** İstanbul (Beşiktaş) + Ege kıyıları
- **Kategori:** Tekne tamir servisi / Boat repair shop

---

## A) Aktivasyon (kritik, ilk hafta)
1. **Google Search Console** — doğrula (DNS TXT), `sitemap.xml` gönder, ana sayfa + 7 hizmet + İstanbul/Tuzla/Bodrum + amiral makaleleri elle indekslet. (Rehber: `google-search-console-rehberi.md`)
2. **Google Business Profile** — kur, doğrula (video), optimize, yorum topla. (Rehber: `google-business-profile-rehberi.md`)
3. **Bing Webmaster Tools** — aynı sitemap. (ChatGPT/Copilot aramaları Bing'i kullanır → GEO'ya doğrudan dokunur.)
4. **Bing Places** — GBP'nin Bing karşılığı; yerel görünürlük + GEO.

## B) Yerel Atıflar / Dizinler (citations) — tutarlı NAP ile
Her biri hem yerel sinyal hem de AI'ların okuduğu bir kaynak. NAP kartını aynen gir:
- Apple Business Connect (Apple Haritalar)
- Yandex Business (Türkiye'de yaygın)
- Foursquare
- Armut.com — profil (aynı zamanda lead kanalı)
- Sahibinden "Hizmet" ilanı/profil
- Denizcilik/marina dizinleri ve marina web sitelerinin "servis sağlayıcılar" listeleri
- Sektörel forum/rehberler (teknecilik toplulukları)

## C) Backlink (düşük bütçe, yüksek etki)
Backlink hâlâ en güçlü sıralama faktörlerinden. Ücretsiz/ucuz taktikler:
- **Marina & iş ortaklıkları:** Hizmet verdiğin marina/çekek sitelerinin bağlantı/liste sayfalarına girmek.
- **Denizcilik blog/forumları:** Değerli katkı + profil/imza linki; uygun yerlerde misafir yazı.
- **Yerel basın:** "İstanbul/Ege'de aracısız tekne servisi" açılış haberi → bölge haber siteleri.
- **Tedarikçi/marka çapraz tanıtımı:** Kullandığın boya/teak markalarının bayi/uygulayıcı listelerine girmek.
- **Sosyal profiller:** Instagram (ve varsa YouTube) bio'sunda site linki.
- Not: Kalite > adet. Spam dizinlerden kaçın.

## D) İçerik Motoru (sürekli — tazelik + kapsam)
- **Tempo:** Ayda 2-4 yeni makale. Kaynak: `genisletilmis-icerik-plani.md`'deki kalan konular + GSC'de **pozisyon 5-20** çıkan sorgular (ilk sayfaya yakın; onlara özel içerik/güçlendirme).
- **Güncelleme:** "Fiyat/maliyet" ve mevsimlik makaleleri yılda bir güncelle (Google tazeliği ödüllendirir).
- **Sezonluk zamanlama:** Sonbahar → kışlatma içerikleri öne çıkar; ilkbahar → bahar bakımı/antifouling. Yayın + kampanya eşzamanlı.
- **Sözlük hub'ı** (opsiyonel güçlü hamle): tüm terimleri tek sayfada toplayıp 70+ makaleye iç link → topikal otorite + GEO.

## E) Yorum Stratejisi (local ranking + dönüşüm + GEO)
- Her memnun müşteriden **GBP yorumu** iste (panelden kısa link al, WhatsApp'tan gönder).
- Hedef: ilk 2-3 ayda düzenli, gerçek akış. Sahte yorum yok (ban riski).
- Her yoruma yanıt ver.
- Gerçek yorumlar biriktikçe → sitedeki görüşleri gerçeğiyle değiştir + gerçek `aggregateRating` schema'yı geri ekle.

## F) GEO (AI'da önerilmek) — üstündekilerin doğal çıktısı
LLM'ler webdeki bilgiyi sentezler; şunlar seni "önerilir" yapar:
- **Yapısal veri** (LocalBusiness/Service/FAQ/Article) ✓ hazır
- **llms.txt** ✓ hazır
- **Statik, JS'siz içerik** ✓ (AI tarayıcıları tam görür)
- **Web genelinde tutarlı marka + atıf** (B ve C maddeleri) → LLM'ler seni birden çok kaynakta görür
- **Gerçek yorumlar + forum/dizin varlığı** → güven sinyali
- **Net, alıntılanabilir gerçekler** ("nedir/nasıl/X vs Y", fiyatı belirleyen faktörler) ✓ hazır

## G) Ölçüm & Ritim
- **Analytics (GA4):** dönüşümleri gör (WhatsApp tık, form gönderimi). Ölçmeden iyileştirilemez. → *Kurulacak (Measurement ID gerekli).*
- **Haftalık:** GSC → Pages (indeksleme) + Performance (pozisyon 5-20 sorgular).
- **Aylık:** yeni içerik yayını, yorum durumu, yeni backlink/atıf, GBP insights.

---

### Öncelik Sırası (özet)
1. Netlify deploy'u tamamla (bekleyen değişiklikler canlıya).
2. GSC + GBP + Bing (aktivasyon).
3. Atıflar (citations) + ilk backlink'ler.
4. Yorum toplamaya başla.
5. İçerik temposu + sezonluk kampanyalar.
6. GA4 ile ölç, pozisyon 5-20 sorgulara abanarak sürekli iyileştir.
