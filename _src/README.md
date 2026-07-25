# Tekne Usta — site kaynağı

Site artık **veri-güdümlü statik bir jeneratörle** üretiliyor. Tek tek HTML dosyası
düzenlemiyorsun; içeriği `_src/content.py` içinde düzenliyor, `build.py` ile tüm sayfaları
(TR + EN) yeniden üretiyorsun.

## Yapı
```
_src/
  content.py     ← TÜM metinler burada (hizmetler, bölgeler, blog, ana sayfa) TR+EN
  build.py       ← jeneratör (çalıştır: python3 _src/build.py)
  templates/     ← Jinja2 şablonları (tasarım/yerleşim)
assets/          ← css, js, görseller, video
index.html, hizmetler/, bolgeler/, blog/, en/  ← ÜRETİLEN dosyalar (elle düzenleme)
sitemap.xml, robots.txt, netlify.toml, 404.html
```

## Nasıl derlenir
```bash
pip install jinja2 --break-system-packages   # ilk seferde
python3 _src/build.py                          # tüm sayfaları üretir
```

## Yeni hizmet / bölge / blog eklemek
`_src/content.py` içindeki `SERVICES`, `REGIONS` veya `POSTS` listesine yeni bir kayıt
ekle (TR+EN alanlarıyla), sonra `build.py` çalıştır. Sitemap, menü, iç linkler ve schema
otomatik güncellenir.

## Deploy (Netlify)
Bu klasör doğrudan GitHub repo'suna push edilebilir; Netlify kök dizini yayınlar.
Domain bağlanınca (tekneusta.com) canonical/hreflang zaten doğru host'u işaret ediyor.

## İşin bittiği yer / dikkat
- `content.py` içindeki `SITE` bloğunda e-posta, Instagram, YouTube linklerini gerçek
  hesaplarla güncelle.
- LocalBusiness schema'daki adres/koordinat şu an İstanbul geneli; gerçek atölye/marina
  adresini ve Google Business Profile bilgisini ekleyince netleşecek.
- `aggregateRating` (4.9 / 87) örnek değerdir; gerçek yorum sayısıyla güncellenmeli.
