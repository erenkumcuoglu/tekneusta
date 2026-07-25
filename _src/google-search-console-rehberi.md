# Google Search Console (GSC) — Adım Adım Kurulum ve Optimizasyon Rehberi

> Amaç: tekneusta.com'un tüm sayfalarını Google'a indekslettirmek, performansı ölçmek ve sürekli iyileştirmek.
> Ön koşul: domain (tekneusta.com) alınmış ve Netlify'a bağlanmış olmalı. Domain almadan GSC doğrulaması yapılamaz.

---

## Aşama 0 — Yayına alma (GSC'den önce)
1. Repo'yu GitHub'a push et; Netlify siteyi otomatik yayınlasın.
2. Netlify'da **Domain settings → Add custom domain → tekneusta.com** ekle.
3. Domain sağlayıcında DNS'i Netlify'a yönlendir (Netlify DNS veya A/CNAME kayıtları).
4. Netlify **HTTPS (Let's Encrypt)** sertifikasını otomatik verir — "https" aktif olsun.
5. www ve non-www'den biri **birincil** olsun; diğeri ona yönlensin (Netlify otomatik yapar). Sitedeki canonical `https://www.tekneusta.com` — Netlify birincil domaini de **www** seç ki tutarlı olsun.

## Aşama 1 — Mülk (property) oluşturma ve doğrulama
1. https://search.google.com/search-console adresine Google hesabınla gir.
2. **Add property → Domain** tipini seç (tüm alt alan adlarını ve http/https'i kapsar — önerilen).
3. Verilen **TXT kaydını** domain DNS'ine ekle (Netlify DNS veya sağlayıcı paneli → DNS records → TXT).
4. DNS yayılınca (birkaç dk–saat) **Verify**'a bas.
   - Alternatif: "URL prefix" tipiyle HTML dosyası / meta etiketi ile de doğrulanabilir; ama Domain tipi daha kapsamlıdır.

## Aşama 2 — Sitemap gönderimi
1. GSC → sol menü **Sitemaps**.
2. `sitemap.xml` yaz ve **Submit**. (Tam URL: https://www.tekneusta.com/sitemap.xml)
3. Durum "Success" olmalı; keşfedilen URL sayısı ~80 civarı görünecek (site büyüdükçe artar).
4. Yeni sayfa/makale ekleyip her build sonrası sitemap otomatik güncellenir — tekrar göndermene gerek yok, ama büyük eklemelerde "Resubmit" iyi olur.

## Aşama 3 — İlk indeksleme (öncelikli sayfalar)
İndeksleme sıraya girer; hızlandırmak için önemli sayfaları elle iste:
1. Üst arama çubuğuna URL yapıştır → **URL Inspection**.
2. "URL is not on Google" görürsen **Request Indexing**'e bas.
3. Şu sırayla yap (kota günde sınırlı):
   1. Ana sayfa `/`
   2. 6 hizmet sayfası (`/hizmetler/...`)
   3. İstanbul + en önemli bölge sayfaları
   4. Ticari niyetli makaleler (fiyat/maliyet olanlar önce)
4. Kalan sayfalar sitemap üzerinden zamanla indekslenir.

## Aşama 4 — Kontrol edilecek raporlar (ilk 2–4 hafta)
- **Pages (Indexing):** kaç sayfa indekslendi, hangileri "excluded" ve neden. Sık nedenler:
  - *Discovered – currently not indexed*: normaldir, beklet; iç link ve içerik gücü artınca girer.
  - *Duplicate without user-selected canonical*: canonical etiketini kontrol et (sitede doğru kurulu).
  - *Crawled – not indexed*: içeriği zayıf/ince sayfaları güçlendir.
- **Page Experience / Core Web Vitals:** mobil hız. hero.mp4 büyükse (12 MB) LCP'yi düşürebilir — gerekiyorsa videoyu sıkıştır/kaldır.
- **Mobile Usability** (varsa): tıklama hedefi, yazı boyutu sorunları.

## Aşama 5 — Performans takibi ve optimizasyon (sürekli)
1. **Performance** raporu: Sorgular (queries), sayfalar, ülke, cihaz. Metrikler: gösterim, tıklama, CTR, ortalama pozisyon.
2. **Fırsat avı — pozisyon 5–20 sorgular:** İlk sayfaya yakın ama üstte değil. Bu sorguları hedefleyen sayfayı güçlendir (başlık, içerik derinliği, iç link).
3. **Düşük CTR + yüksek gösterim:** başlık (title) ve açıklamayı (meta description) daha çekici yaz — tıklama artar.
4. **Sayfa başına sorgu:** Bir sayfa hedeflemediğin bir sorguda geliyorsa, o sorgu için ayrı bir makale/başlık düşün (içerik haritasındaki boşluklar).
5. **İç link:** GSC "Links" raporunda az iç link alan önemli sayfalara, ilgili makalelerden link ekle.

## Aşama 6 — Google Business Profile ile bağ (yerel)
- GBP hesabını aç (domain gerektirmez). Web sitesi alanına tekneusta.com'u ekle.
- GBP + bölge sayfaları + tutarlı NAP (isim/adres/telefon) yerel pakette görünürlüğü artırır.
- Not: GBP ayrı bir üründür; GSC organik, GBP harita/yerel sonuçları içindir. İkisi birlikte çalışır.

---

### Hızlı kontrol listesi
- [ ] Domain alındı ve Netlify'a bağlandı (HTTPS aktif)
- [ ] GSC Domain property doğrulandı (TXT)
- [ ] sitemap.xml gönderildi (Success)
- [ ] Ana sayfa + 6 hizmet + İstanbul elle indekslemeye gönderildi
- [ ] Pages raporu haftalık kontrol
- [ ] Performance: pozisyon 5–20 sorgular için içerik güçlendirme döngüsü
- [ ] robots.txt erişilebilir: https://www.tekneusta.com/robots.txt
- [ ] Bing Webmaster Tools'a da aynı sitemap'i ver (ekstra görünürlük, dakikalar sürer)
