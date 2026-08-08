# Brevo ile info@tekneusta.com'dan E-posta Gönderme (Ücretsiz)

> Amaç: Cloudflare zaten `info@`'ya geleni Gmail'ine düşürüyor (alım ✓). Bu rehber, **Gmail'den `info@tekneusta.com` adresiyle GÖNDERME** içindir. Brevo ücretsiz SMTP (~300 mail/gün) + Gmail "Send mail as" ile, $0.

## 1) Brevo hesabı
- https://www.brevo.com → ücretsiz kaydol.

## 2) Alan adı doğrulama (spam'e düşmemek için önemli)
- Brevo → **Senders, Domains & Dedicated IPs → Domains → Add a domain** → `tekneusta.com`.
- Brevo sana **DKIM + SPF/DMARC** için DNS kayıtları verir.
- Bunları **Cloudflare → DNS → Add record** ile ekle (verilen tip/isim/değerle, **DNS only / gri bulut**).
- Brevo'da **Authenticate / Verify**'a bas (yayılması birkaç dk–saat).

## 3) Gönderen adresi ekle
- Brevo → **Senders → Add a sender** → `info@tekneusta.com`.
- Brevo `info@`'ya doğrulama maili atar → Cloudflare Gmail'ine yönlendirir → linke tıkla, onayla.

## 4) SMTP bilgilerini al
- Brevo → sağ üst → **SMTP & API → SMTP** sekmesi:
  - **Server:** `smtp-relay.brevo.com`
  - **Port:** `587`
  - **Login:** Brevo hesap e-postan
  - **Password:** "Generate a new SMTP key" ile üret (bu SMTP anahtarı; Brevo giriş şifren değil)

## 5) Gmail'e "Send mail as" ekle
- Gmail → **⚙ Ayarlar → Tüm ayarları gör → Hesaplar ve İçe Aktarma**.
- **"Diğer adreslerinizle e-posta gönderin" → Başka bir e-posta adresi ekle**:
  - Ad: `Tekne Usta` · E-posta: `info@tekneusta.com` (takma ad olarak işaretle) → İleri
  - SMTP Sunucusu: `smtp-relay.brevo.com` · Port: `587`
  - Kullanıcı adı: Brevo login · Şifre: SMTP key · **TLS** → Ekle
- Gmail `info@`'ya bir doğrulama kodu gönderir → Cloudflare Gmail'ine düşer → kodu gir / linke tıkla.

## 6) Kullanım
- Gmail'de yeni e-postada "Kimden" olarak **info@tekneusta.com**'u seç.
- İstersen varsayılan gönderen yap: Ayarlar → Hesaplar → "varsayılan yap".

## Notlar
- Brevo ücretsiz kademe küçük işletme için yeter; limit dolarsa yükseltirsin.
- Domain doğrulaması (DKIM/SPF) yapılmadan gönderirsen mailler spam'e düşebilir — 2. adımı atlama.
- Site zaten `info@tekneusta.com`'u gösteriyor; bu kurulumla adres hem alır hem gönderir hale gelir.
