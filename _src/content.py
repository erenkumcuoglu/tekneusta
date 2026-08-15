# -*- coding: utf-8 -*-
"""Tekne Usta — site content (TR + EN). Edited by humans; rendered by build.py."""

SITE = {
    "domain": "https://www.tekneusta.com",
    "brand": "Tekne Usta",
    "phone_display": "+90 532 173 89 78",
    "phone_e164": "+905321738978",
    "wa": "905321738978",
    "email": "info@tekneusta.com",
    "instagram": "https://www.instagram.com/tekneusta",
    "youtube": "https://www.youtube.com/@tekneusta",
    "rating": "4.9",
    "review_count": "87",
    "founded": "2009",
    "ga4_id": "G-EXT5LH2ZHR",  # GA4 Measurement ID — analytics aktif
}

# ------------------------------------------------------------------ UI strings
I18N = {
    "tr": {
        "nav": {"home": "Ana Sayfa", "services": "Hizmetler", "regions": "Bölgeler",
                "about": "Hakkımızda", "blog": "Blog", "tool": "Maliyet Aracı", "cta": "Teklif Al"},
        "footer": {
            "tag": "Tekne tamiri, renovasyon ve bakımında güvenilir usta eli. Her tekneye, her hasara özel çözüm.",
            "contact": "İletişim", "wa": "WhatsApp'tan Yaz", "rights": "Tüm hakları saklıdır.", "privacy": "Gizlilik & KVKK",
        },
        "aside": {
            "title": "Ücretsiz keşif alın",
            "text": "Teknenizi yerinde inceleyelim, 48 saat içinde kalem kalem yazılı teklif sunalım. Hiçbir yükümlülük yok.",
            "cta": "WhatsApp'tan Teklif Al", "other": "Diğer Hizmetler",
        },
        "process": {
            "label": "Nasıl Çalışıyoruz?", "title": "Tekliften Teslime",
            "sub": "Şeffaf süreç, net fiyatlar, sürpriz yok. Keşiften teslime kadar her aşamada yanınızdayız.",
            "steps": [
                {"title": "Başvuru ve Randevu", "desc": "Formu doldurun veya WhatsApp'tan yazın. 24 saat içinde dönerek uygun randevuyu ayarlıyoruz."},
                {"title": "Ücretsiz Keşif", "desc": "Ustamız teknenizi yerinde inceleyerek kapsamlı bir durum değerlendirmesi yapar."},
                {"title": "Yazılı Teklif", "desc": "48 saat içinde kalemlerin ayrı ayrı belirtildiği, sürprizsiz yazılı fiyat teklifini sunuyoruz."},
                {"title": "Teslim", "desc": "Belirlenen takvimde çalışmalar başlar; sizi adım adım bilgilendirerek teknenizi teslim ederiz."},
            ],
        },
        "faq": {"label": "Sık Sorulan Sorular", "title": "Aklınızdaki Sorular",
                "aside_title": "Tekneniz için ücretsiz değerlendirme alın",
                "aside_text": "Ustalarımız teknenizi yerinde inceleyerek ihtiyacınızı doğru analiz eder. Hiçbir yükümlülük olmadan.",
                "aside_cta": "Teklif Talebini Gönderin"},
        "region": {"other": "Diğer Bölgeler"},
        "boattype": {"label": "Tekne Tipleri", "other": "Diğer Tekne Tipleri"},
        "blog": {"title": "Tekne Bakım Rehberi", "sub": "Osmozdan antifoulinge, teak bakımından kışlatmaya — tekne sahipleri için pratik, uzman içerik."},
        "form": {
            "label": "Ücretsiz Teklif", "title": "Tekneniz İçin Teklif Alın",
            "pitch": "Formu doldurun, WhatsApp'tan hemen görüşmeye başlayalım.",
            "promises": ["24 saat içinde geri arama garantisi", "Yerinde ücretsiz keşif (İstanbul içi)",
                         "Kalem kalem şeffaf fiyat teklifi", "Kesin başlangıç ve teslim tarihi", "İşçilik garantisi"],
            "name": "Adınız", "phone": "Telefon", "boat": "Tekne Tipi", "service": "İstenen Hizmet",
            "select": "Seçin...", "note": "Kısaca Bilgi Verin", "note_ph": "Teknenizin markası, modeli ve durumu...",
            "boat_types": ["Motor Tekne", "Yelkenli", "Yat / Motoryat", "RIB / Bot", "Klasik Ahşap", "Diğer"],
            "other": "Genel Değerlendirme", "submit": "WhatsApp'tan Teklif Al",
            "email": "E-posta (opsiyonel)", "email_ph": "ornek@eposta.com",
            "consent": "Bakım ve kampanya bilgilendirmelerini e-posta ile almak istiyorum. (İstediğiniz an çıkabilirsiniz.)",
            "privacy": "Bilgileriniz yalnızca sizinle iletişim amacıyla kullanılır.",
            "success_title": "Talebiniz Alındı", "success_text": "24 saat içinde ustamız sizi arayacak. Teşekkür ederiz.",
            "lead": "Merhaba, tekneusta.com üzerinden teklif talebi:",
        },
    },
    "en": {
        "nav": {"home": "Home", "services": "Services", "regions": "Regions",
                "about": "About", "blog": "Blog", "tool": "Cost Tool", "cta": "Get a Quote"},
        "footer": {
            "tag": "The trusted craftsman for boat repair, refit and maintenance. A tailored solution for every boat and every job.",
            "contact": "Contact", "wa": "Message on WhatsApp", "rights": "All rights reserved.", "privacy": "Privacy",
        },
        "aside": {
            "title": "Get a free survey",
            "text": "We inspect your boat on site and send an itemised written quote within 48 hours. No obligation.",
            "cta": "Get a Quote on WhatsApp", "other": "Other Services",
        },
        "process": {
            "label": "How We Work", "title": "From Quote to Delivery",
            "sub": "A transparent process, clear pricing, no surprises. We are with you at every stage, from survey to delivery.",
            "steps": [
                {"title": "Enquiry & Appointment", "desc": "Fill in the form or message us on WhatsApp. We reply within 24 hours to arrange a convenient time."},
                {"title": "Free Survey", "desc": "Our craftsman inspects your boat on site and makes a thorough condition assessment."},
                {"title": "Written Quote", "desc": "Within 48 hours we send a clear, itemised written quote with no hidden costs."},
                {"title": "Delivery", "desc": "Work starts on the agreed schedule; we keep you informed at every step and hand your boat back ready."},
            ],
        },
        "faq": {"label": "Frequently Asked Questions", "title": "Your Questions Answered",
                "aside_title": "Get a free assessment for your boat",
                "aside_text": "Our craftsmen inspect your boat on site and assess exactly what it needs. With no obligation.",
                "aside_cta": "Send a Quote Request"},
        "region": {"other": "Other Regions"},
        "boattype": {"label": "Boat Types", "other": "Other Boat Types"},
        "blog": {"title": "Boat Care Guide", "sub": "From osmosis to antifouling, teak care to winterising — practical, expert content for boat owners."},
        "form": {
            "label": "Free Quote", "title": "Get a Quote for Your Boat",
            "pitch": "Fill in the form and let's start the conversation on WhatsApp.",
            "promises": ["Callback guaranteed within 24 hours", "Free on-site survey (within Istanbul)",
                         "Fully itemised, transparent quote", "Firm start and delivery dates", "Workmanship guarantee"],
            "name": "Your Name", "phone": "Phone", "boat": "Boat Type", "service": "Service Needed",
            "select": "Select...", "note": "Tell Us Briefly", "note_ph": "Make, model and condition of your boat...",
            "boat_types": ["Motorboat", "Sailboat", "Yacht / Motoryacht", "RIB / Tender", "Classic Wooden", "Other"],
            "other": "General Assessment", "submit": "Get a Quote on WhatsApp",
            "email": "Email (optional)", "email_ph": "you@email.com",
            "consent": "I'd like to receive maintenance and campaign updates by email. (You can opt out anytime.)",
            "privacy": "Your details are used only to contact you.",
            "success_title": "Request Received", "success_text": "Our craftsman will call you within 24 hours. Thank you.",
            "lead": "Hello, quote request via tekneusta.com:",
        },
    },
}

# ------------------------------------------------------------------ Home copy
HOME = {
    "tr": {
        "badge": "Tekne Tamiri · Renovasyon · Bakım",
        "h1": "Tekneniz <em>Usta Eline</em> Emanet",
        "sub": "Fiberglas onarımından ahşap renovasyonuna, profesyonel boyadan kışlatmaya — teknenizi yeniden suya layık hale getiriyoruz.",
        "cta1": "Ücretsiz Teklif Al", "cta2": "Hizmetleri Keşfet", "scroll": "Kaydır", "detail": "Detay →",
        "stats": [
            {"num": "15+", "label": "Yıl Deneyim"}, {"num": "300+", "label": "Tamamlanan Proje"},
            {"num": "19", "label": "Hizmet Bölgesi"}, {"num": "%100", "label": "İşçilik Garantisi"},
            {"num": "48s", "label": "Teklif Süresi"},
        ],
        "svc_label": "Hizmetlerimiz", "svc_title": "Her Tekneye Özel Uzmanlık",
        "svc_sub": "Fiberglas, ahşap veya alüminyum — hangi malzeme olursa olsun, teknenizin ihtiyacına göre doğru çözümü üretiyoruz.",
        "quotes": ["İşimizi sözümüzle değil, sonuçlarımızla anlatıyoruz.",
                   "Her teknenin bir hikâyesi vardır; biz onu korur ve geleceğe taşırız.",
                   "Şeffaf fiyat, net takvim, arkasında durulan işçilik."],
        "about_label": "Biz Kimiz", "about_title": "15 Yıllık Deneyim, Her Tekneye Saygı",
        "about_img_alt": "Tersanede tekne üzerinde çalışan usta",
        "about_paras": [
            "2009'dan bu yana yüzlerce tekne sahibinin güvenini kazandık. Referanslarla büyüdük — çünkü işimizi sözümüzle değil, sonuçlarımızla anlatıyoruz.",
            "Her proje için ayrı bir değerlendirme yapıyor, teknenizin tarihini ve özelliklerini anlayarak çalışıyoruz. Fiberglas, ahşap veya karma malzeme fark etmez — her sistemde uzman ekibimiz var.",
        ],
        "vals": [
            {"label": "Şeffaflık", "text": "Sürpriz fatura yok. Her kalem önceden yazılı olarak belirtilir."},
            {"label": "Takvim", "text": "Söylediğimiz tarihte teslim ederiz — sezon planınızı bozmayız."},
            {"label": "Garanti", "text": "İşçiliğimizin arkındayız. Sorun olursa ücretsiz döneriz."},
            {"label": "İletişim", "text": "Proje boyunca sizi adım adım bilgilendiriyoruz."},
        ],
        "reg_label": "Hizmet Bölgeleri", "reg_title": "İstanbul ve Ege'de Yanınızdayız",
        "reg_sub": "İstanbul marinaları ve Ege kıyılarında yerinde keşif ve servis. Bölgenizi seçin, size en yakın çözümü sunalım.",
        "type_label": "Tekne Tipleri", "type_title": "Her Tekne Tipine Özel Uzmanlık",
        "type_sub": "Yat, yelkenli, motoryat, gulet, RIB veya klasik ahşap — teknenizin tipine göre doğru bakım ve onarım yaklaşımı.",
        "test_label": "Müşteri Görüşleri", "test_title": "Tekne Sahipleri Ne Diyor?",
    },
    "en": {
        "badge": "Boat Repair · Refit · Maintenance",
        "h1": "Your Boat, in <em>Master Hands</em>",
        "sub": "From fibreglass repair to wooden refit, professional painting to winterising — we make your boat seaworthy again.",
        "cta1": "Get a Free Quote", "cta2": "Explore Services", "scroll": "Scroll", "detail": "Details →",
        "stats": [
            {"num": "15+", "label": "Years Experience"}, {"num": "300+", "label": "Projects Completed"},
            {"num": "19", "label": "Service Regions"}, {"num": "100%", "label": "Workmanship Warranty"},
            {"num": "48h", "label": "Quote Turnaround"},
        ],
        "svc_label": "Our Services", "svc_title": "Expertise Tailored to Every Boat",
        "svc_sub": "Fibreglass, wood or aluminium — whatever the material, we find the right solution for what your boat needs.",
        "quotes": ["We let our results speak, not our promises.",
                   "Every boat has a story; we protect it and carry it forward.",
                   "Transparent pricing, a clear schedule, workmanship we stand behind."],
        "about_label": "Who We Are", "about_title": "15 Years of Experience, Respect for Every Boat",
        "about_img_alt": "Craftsman working on a boat in the yard",
        "about_paras": [
            "Since 2009 we have earned the trust of hundreds of boat owners. We have grown through referrals — because we let our results, not our words, speak for us.",
            "We assess every project individually, working with an understanding of your boat's history and character. Fibreglass, wood or mixed construction — we have an expert for every system.",
        ],
        "vals": [
            {"label": "Transparency", "text": "No surprise invoices. Every item is stated in writing in advance."},
            {"label": "Schedule", "text": "We deliver on the date we promise — we won't disrupt your season plans."},
            {"label": "Warranty", "text": "We stand behind our workmanship. If something's wrong, we put it right at no cost."},
            {"label": "Communication", "text": "We keep you informed at every step throughout the project."},
        ],
        "reg_label": "Service Regions", "reg_title": "At Your Side in Istanbul & the Aegean",
        "reg_sub": "On-site survey and service across Istanbul's marinas and the Aegean coast. Choose your region and we'll bring the nearest solution.",
        "type_label": "Boat Types", "type_title": "Expertise Tailored to Every Boat Type",
        "type_sub": "Yacht, sailboat, motoryacht, gulet, RIB or classic wooden — the right care and repair approach for your boat's type.",
        "test_label": "Client Reviews", "test_title": "What Boat Owners Say",
    },
}

TESTIMONIALS = [
    {"initials": "MA", "name": "Murat A.", "boat": "Bayliner 245",
     "tr": "2003 model fiberglas teknem ciddi osmoz hasarı almıştı. Ekip tedaviyi mükemmel yaptı, teknem şu an sıfır gibi. Fiyat-kalite dengesi için kesinlikle tavsiye ederim.",
     "en": "My 2003 fibreglass boat had serious osmosis damage. The team treated it perfectly — it now looks brand new. I'd absolutely recommend them for value and quality."},
    {"initials": "SY", "name": "Serap Y.", "boat": "Klasik Ahşap Yelkenli",
     "tr": "1970 yapımı ahşap teknemin restorasyonunu güvenle verebileceğim bir yer arıyordum. İşin bitişinde ağzım açık kaldı — tarihi dokuyu tamamen korudular.",
     "en": "I was looking for somewhere I could trust with the restoration of my 1970 wooden boat. The result left me speechless — they preserved every bit of the original character."},
    {"initials": "KD", "name": "Kerem D.", "boat": "Jeanneau Sun Odyssey 36",
     "tr": "Her sene kışlatma ve bakımı burada yaptırıyorum. İletişimleri kusursuz, söz verdikleri tarihe yüzde yüz sadık kalıyorlar.",
     "en": "I have my winterising and maintenance done here every year. Their communication is flawless and they stick to the promised date without fail."},
]

# ------------------------------------------------------------------ Services
SERVICES = [
{
 "slug": "fiberglas-onarim", "slug_en": "fibreglass-repair",
 "image": "/assets/images/services/fiberglas.jpg",
 "deep": {
   "tr": """
<h2>Hangi hasar, hangi yöntem?</h2>
<p>Fiber teknelerde her hasar farklı bir yaklaşım ister. Aşağıdaki tablo, en sık karşılaştığımız durumları ve tipik çözümleri özetliyor — kesin yöntem elbette keşifteki değerlendirmeye göre netleşir.</p>
<table>
<thead><tr><th>Durum</th><th>Uygulanan yöntem</th><th>Tipik süre</th></tr></thead>
<tbody>
<tr><td>Yüzeysel çizik / mat gelcoat</td><td>Zımpara, parlatma (cut &amp; polish)</td><td>1–2 gün</td></tr>
<tr><td>Çatlak / kırık (kozmetik)</td><td>Açma, dolgu, gelcoat bitişi</td><td>2–4 gün</td></tr>
<tr><td>Yapısal kırık / delik</td><td>Laminasyon (cam elyafı + reçine)</td><td>4–8 gün</td></tr>
<tr><td>Osmoz (yaygın)</td><td>Jelkot sıyırma, kurutma, epoksi bariyer</td><td>2–4 hafta*</td></tr>
</tbody>
</table>
<p><em>*Kurutma süresi iklime ve laminat nemine bağlıdır; net takvim nem ölçümüyle verilir.</em></p>
<h2>Osmoz tedavisinde neden acele etmiyoruz?</h2>
<p>Osmozda başarının sırrı sabırdır. Laminat tam kurumadan bariyer kat atmak, nemi içeride hapseder ve sorun 1–2 sezon içinde geri döner. Biz nem ölçer değeri kabul edilebilir eşiğe düşene kadar bir sonraki adıma geçmeyiz. Bu, işi "iki kez yaptırmanın" önüne geçer — en pahalı osmoz tedavisi, yarım yapılandır.</p>
<h2>Fiber, GRP, polyester — hepsi aynı mı?</h2>
<p>Tekne dünyasında "fiber", "fiberglas", "GRP" (cam takviyeli plastik) çoğunlukla aynı malzemeyi anlatır. Onarımda kritik olan, reçine uyumudur: orijinal laminatla uyumlu bir sistem seçmek (bkz. <a href="/blog/polyester-vs-epoksi-recine/">polyester vs epoksi</a>). Yanlış reçine, kısa sürede kabaran bir onarım demektir.</p>
""",
   "en": """
<h2>Which damage, which method?</h2>
<p>Every kind of damage on a fibreglass boat needs a different approach. The table below sums up the situations we see most and their typical solutions — the exact method is confirmed by the survey.</p>
<table>
<thead><tr><th>Condition</th><th>Method applied</th><th>Typical time</th></tr></thead>
<tbody>
<tr><td>Surface scratch / dull gelcoat</td><td>Sanding, cut &amp; polish</td><td>1–2 days</td></tr>
<tr><td>Crack / break (cosmetic)</td><td>Open out, fill, gelcoat finish</td><td>2–4 days</td></tr>
<tr><td>Structural break / hole</td><td>Lamination (glass + resin)</td><td>4–8 days</td></tr>
<tr><td>Osmosis (widespread)</td><td>Gelcoat peel, drying, epoxy barrier</td><td>2–4 weeks*</td></tr>
</tbody>
</table>
<p><em>*Drying time depends on climate and laminate moisture; a firm schedule follows a moisture reading.</em></p>
<h2>Why we don't rush osmosis treatment</h2>
<p>The secret to success in osmosis is patience. Applying a barrier coat before the laminate is fully dry traps moisture inside, and the problem returns within a season or two. We don't move to the next step until the moisture reading drops below an acceptable threshold. This avoids doing the job twice — the most expensive osmosis treatment is a half-done one.</p>
<h2>Fibreglass, GRP, polyester — are they the same?</h2>
<p>In the boating world, "fibreglass" and "GRP" (glass-reinforced plastic) usually mean the same material. In repair, what matters is resin compatibility: choosing a system compatible with the original laminate (see <a href="/en/blog/polyester-vs-epoxy-resin/">polyester vs epoxy</a>). The wrong resin means a repair that soon blisters.</p>
""",
 },
 "tr": {
   "name": "Fiberglas Onarım & Osmoz",
   "short": "Çarpma, çatlak ve kırıklardan osmoz tedavisine kadar tüm fiberglas onarımları.",
   "bullets": ["Çatlak ve delik onarımı", "Osmoz kabarcığı tedavisi", "Gelcoat yenileme ve parlatma", "Su altı yapı onarımı"],
   "hero_title": "Fiberglas Tekne Onarımı ve Osmoz Tedavisi",
   "hero_sub": "Çatlak, kırık ve çarpma hasarlarından osmoz ve gelcoat sorunlarına — fiber teknenizi yapısal olarak sağlam ve pürüzsüz bir yüzeyle suya döndürüyoruz.",
   "meta_title": "Fiberglas Tekne Onarımı ve Osmoz Tedavisi | Tekne Usta",
   "meta_desc": "Fiber tekne tamiri, fiberglas çatlak ve kırık onarımı, osmoz tedavisi, gelcoat yenileme. İstanbul ve Ege'de ücretsiz keşif, 48 saat yazılı teklif, işçilik garantisi.",
   "body": """
<h2>Fiber teknenizde ne varsa çözüyoruz</h2>
<p>Fiberglas (fiber) tekneler dayanıklıdır ama darbe, yaşlanan gelcoat ve deniz suyunun etkisiyle zamanla çatlak, kabarma ve osmoz gibi sorunlar yaşar. <strong>Tekne Usta</strong> olarak yüzeysel bir kozmetik onarımla yetinmeyiz; hasarın kaynağına inip yapısal bütünlüğü geri kazandırır, ardından yüzeyi orijinalinden ayırt edilemeyecek şekilde bitiririz.</p>
<p>İster küçük bir çizik, ister su altında ilerleyen bir osmoz olsun, önce ücretsiz keşifle durumu net biçimde ortaya koyar, ne yapılacağını ve neden yapılacağını size yazılı olarak anlatırız.</p>
<h2>Yaptığımız fiberglas işleri</h2>
<ul>
<li><strong>Çatlak, kırık ve delik onarımı</strong> — çarpma ve yapısal hasarların laminasyonla güçlendirilmesi</li>
<li><strong>Osmoz tedavisi</strong> — kabarcıkların açılması, kurutma, epoksi bariyer kat ve yeniden kaplama</li>
<li><strong>Gelcoat yenileme</strong> — solmuş, çatlamış gelcoat'un onarımı, renk eşleştirme ve parlatma</li>
<li><strong>Su altı yapısal onarım</strong> — omurga, karina ve bordo hasarlarının onarımı</li>
</ul>
<h2>Osmoz nedir, neden ciddiye alınmalı?</h2>
<p>Osmoz, jelkotun altına sızan suyun laminatta asidik kabarcıklar oluşturmasıdır. Erken müdahale edilmezse yapısal zayıflamaya yol açar. Tedavide acele etmeyiz: kabarcıkları açar, laminatı <strong>tam kuruyana kadar</strong> bekletir, ancak nem seviyesi uygun olduğunda bariyer kat ve antifouling uygularız. Detaylı bilgi için <a href="/blog/osmoz-nedir-tedavisi/">osmoz rehberimize</a> göz atabilirsiniz.</p>
<h2>Fiyat ve süre</h2>
<p>Fiberglas onarım fiyatı; hasarın büyüklüğüne, tekne boyuna ve işlemin türüne göre değişir. Küçük gelcoat onarımları 2–5 iş günü, kapsamlı osmoz tedavisi kurutma süresiyle birlikte 2–4 hafta sürebilir. Keşif sonrası <strong>kalem kalem</strong> yazılı teklif veririz; sürpriz fatura çıkarmayız.</p>
""",
   "tiles": [
     {"h": "Yapısal sağlamlık", "p": "Kozmetik değil; laminatı güçlendirerek kalıcı onarım yaparız."},
     {"h": "Doğru kurutma", "p": "Osmozda nem seviyesi uygun olmadan kaplama yapmayız."},
     {"h": "Renk eşleştirme", "p": "Gelcoat onarımında tekneyle uyumlu renk ve parlaklık."},
   ],
   "faqs": [
     {"q": "Fiber tekne tamiri ne kadar sürer?", "a": "Küçük çatlak ve kırık onarımları 2–5 iş günü; osmoz tedavisi ve kapsamlı yüzey yenileme, kurutma süresi dahil 2–4 hafta sürebilir. Keşif sonrası kesin takvim verilir."},
     {"q": "Osmoz tedavisi garantili mi?", "a": "Evet. Doğru kurutma ve bariyer kat uygulaması sonrası işçiliğimize garanti veriyoruz. Kapsam ve süre teklifte yazılı olarak belirtilir."},
     {"q": "Gelcoat rengini tutturabiliyor musunuz?", "a": "Teknenizin mevcut rengine göre eşleştirme yaparız. Yaşlanmış jelkotlarda birebir eşleşme için bazen bölgesel değil komple yüzey uygulaması öneririz."},
   ],
 },
 "en": {
   "name": "Fibreglass Repair & Osmosis",
   "short": "Every fibreglass repair — from impact cracks and holes to full osmosis treatment.",
   "bullets": ["Crack & hole repair", "Osmosis blister treatment", "Gelcoat renewal & polishing", "Below-waterline structural repair"],
   "hero_title": "Fibreglass Boat Repair & Osmosis Treatment",
   "hero_sub": "From cracks, breaks and impact damage to osmosis and gelcoat problems — we return your fibreglass boat to the water structurally sound with a flawless finish.",
   "meta_title": "Fibreglass Boat Repair & Osmosis Treatment | Tekne Usta",
   "meta_desc": "Fibreglass boat repair, crack and hole repair, osmosis treatment and gelcoat renewal in Istanbul and the Aegean. Free survey, written quote in 48 hours, workmanship warranty.",
   "body": """
<h2>Whatever your fibreglass boat needs</h2>
<p>Fibreglass boats are tough, but impact, ageing gelcoat and seawater eventually cause cracks, blistering and osmosis. At <strong>Tekne Usta</strong> we never settle for a cosmetic fix; we get to the root of the damage, restore structural integrity and then finish the surface so it's indistinguishable from original.</p>
<p>Whether it's a small scratch or advancing osmosis below the waterline, we start with a free survey, then explain in writing exactly what we'll do and why.</p>
<h2>Fibreglass work we do</h2>
<ul>
<li><strong>Crack, break and hole repair</strong> — reinforcing impact and structural damage with laminate</li>
<li><strong>Osmosis treatment</strong> — opening blisters, drying, epoxy barrier coat and recoating</li>
<li><strong>Gelcoat renewal</strong> — repairing faded, cracked gelcoat, colour matching and polishing</li>
<li><strong>Below-waterline structural repair</strong> — keel, hull and topside damage</li>
</ul>
<h2>What is osmosis and why take it seriously?</h2>
<p>Osmosis is water seeping under the gelcoat and forming acidic blisters in the laminate. Left untreated it weakens the structure. We never rush the cure: we open the blisters and let the laminate dry <strong>completely</strong>, applying the barrier coat and antifouling only when the moisture level is right. See our <a href="/en/blog/what-is-osmosis-treatment/">osmosis guide</a> for detail.</p>
<h2>Price and timing</h2>
<p>Fibreglass repair cost depends on the extent of damage, boat length and the type of work. Small gelcoat repairs take 2–5 working days; full osmosis treatment, including drying, can take 2–4 weeks. After the survey we give an <strong>itemised</strong> written quote — no surprise invoices.</p>
""",
   "tiles": [
     {"h": "Structural strength", "p": "Not cosmetic — we reinforce the laminate for a lasting repair."},
     {"h": "Proper drying", "p": "In osmosis we never recoat until the moisture level is right."},
     {"h": "Colour matching", "p": "Gelcoat repairs matched to your boat's colour and gloss."},
   ],
   "faqs": [
     {"q": "How long does fibreglass repair take?", "a": "Small crack and break repairs take 2–5 working days; osmosis treatment and full surface renewal, including drying, can take 2–4 weeks. We give a firm schedule after the survey."},
     {"q": "Is osmosis treatment guaranteed?", "a": "Yes. We warranty our workmanship after correct drying and barrier-coat application. Scope and duration are stated in writing in the quote."},
     {"q": "Can you match the gelcoat colour?", "a": "We colour-match to your boat's existing finish. On aged gelcoat, we sometimes recommend a full surface rather than a spot repair for a seamless match."},
   ],
 },
},
{
 "slug": "ahsap-tekne-renovasyonu", "slug_en": "wooden-boat-refit",
 "image": "/assets/images/services/ahsap.jpg",
 "deep": {
   "tr": """
<h2>Ahşap tekne işleri: hangi durumda ne yapılır?</h2>
<p>Ahşap teknede doğru müdahale, sorunun türüne bağlıdır. Aşağıdaki tablo en sık karşılaşılan durumları özetliyor.</p>
<table>
<thead><tr><th>Durum</th><th>Uygulanan yöntem</th><th>Not</th></tr></thead>
<tbody>
<tr><td>Su alan derzler</td><td><a href="/blog/kalafat-nedir/">Kalafat</a> yenileme (üstüpü + macun/dolgu)</td><td>Ahşap hareketine uygun esneklik şart</td></tr>
<tr><td>Çürük bölge</td><td>Temizleme + ahşap ekleme / <a href="/blog/epoksi-ile-ahsap-guclendirme/">epoksi</a></td><td>Sağlam ahşaba kadar açılır</td></tr>
<tr><td>Solmuş / çatlak vernik</td><td>Zımpara + çok katlı <a href="/blog/ahsap-tekne-vernik-bakimi/">vernik</a></td><td>Doğal doku korunur</td></tr>
<tr><td>Yapısal zayıflık (posta/omurga)</td><td>Eleman yenileme / güçlendirme</td><td>Özgün yönteme sadık kalınır</td></tr>
</tbody>
</table>
<h2>Restorasyon süreci nasıl işler?</h2>
<p>Kapsamlı bir restorasyon aceleye gelmez. Önce teknenin durumu haritalanır (hangi bölge yapısal, hangisi kozmetik), sonra aşamalı bir plan çıkarılır. Böylece hem bütçeyi kontrol eder hem işi doğru sırayla yaparız: yapısal onarım → su sızdırmazlık → yüzey bitişi. Bir örnek için <a href="/blog/ahsap-tekne-restorasyon-vaka/">vaka çalışmamıza</a> bakın.</p>
<h2>Gelenek mi, modern mi?</h2>
<p>En iyi sonuç, ikisinin doğru karışımıdır: geleneksel kalafat ve marangozluk, modern epoksi ve laminasyonla desteklenir. Amaç tekneyi "yeni" göstermek değil; karakterini koruyarak <strong>bir sonraki nesle sağlam aktarmaktır</strong>. Klasik tekne tipleri hakkında <a href="/blog/klasik-tekne-turleri/">bu yazıya</a> göz atabilirsiniz.</p>
""",
   "en": """
<h2>Wooden boat work: what's done in which case?</h2>
<p>The right intervention on a wooden boat depends on the type of problem. The table below sums up the most common situations.</p>
<table>
<thead><tr><th>Condition</th><th>Method applied</th><th>Note</th></tr></thead>
<tbody>
<tr><td>Leaking seams</td><td><a href="/en/blog/caulking-explained/">Caulking</a> renewal (oakum + stopping)</td><td>Flexibility for wood movement is essential</td></tr>
<tr><td>Rotten area</td><td>Clean out + wood graft / <a href="/en/blog/epoxy-wood-reinforcement/">epoxy</a></td><td>Opened back to sound wood</td></tr>
<tr><td>Faded / cracked varnish</td><td>Sanding + multi-coat <a href="/en/blog/wooden-boat-varnish-care/">varnish</a></td><td>Natural grain preserved</td></tr>
<tr><td>Structural weakness (frame/keel)</td><td>Member renewal / reinforcement</td><td>Faithful to the original method</td></tr>
</tbody>
</table>
<h2>How does the restoration process work?</h2>
<p>A thorough restoration can't be rushed. First the boat's condition is mapped (which areas are structural, which cosmetic), then a staged plan is drawn up. This controls the budget and does the work in the right order: structural repair → watertightness → surface finish. For an example, see our <a href="/en/blog/wooden-restoration-case-study/">case study</a>.</p>
<h2>Tradition or modern?</h2>
<p>The best result is the right blend of both: traditional caulking and joinery supported by modern epoxy and lamination. The aim isn't to make the boat look "new" but to preserve its character and <strong>hand it soundly to the next generation</strong>. See <a href="/en/blog/classic-boat-types/">this article</a> on classic boat types.</p>
""",
 },
 "tr": {
   "name": "Ahşap Tekne Renovasyonu",
   "short": "Klasik ahşap teknelerde özgün dokuyu koruyarak kapsamlı restorasyon ve yenileme.",
   "bullets": ["Kalafat ve kaplama yenileme", "Epoksi güçlendirme", "Vernik ve boya uygulaması", "Yapısal onarım"],
   "hero_title": "Ahşap Tekne Restorasyonu ve Renovasyonu",
   "hero_sub": "Klasik ahşap teknelerin ruhunu koruyarak; kalafat, kaplama, vernik ve yapısal onarımla teknenizi yeniden hayata döndürüyoruz.",
   "meta_title": "Ahşap Tekne Restorasyonu ve Renovasyonu | Tekne Usta",
   "meta_desc": "Ahşap tekne tamiri, restorasyonu ve renovasyonu: kalafat, kaplama yenileme, epoksi güçlendirme, vernik ve boya. İstanbul ve Ege'de özgün dokuya saygılı işçilik.",
   "body": """
<h2>Ahşabın hakkını veren usta işçiliği</h2>
<p>Ahşap tekneler sabır ve ustalık ister. Modern epoksi ve laminasyon teknikleriyle geleneksel kalafat ve marangozluğu bir arada kullanır, teknenizin <strong>özgün dokusunu bozmadan</strong> sağlamlaştırırız. Klasik bir yelkenli, tirhandil ya da gulet fark etmez — her ahşap tekne kendi hikâyesiyle ele alınır.</p>
<h2>Yaptığımız ahşap işleri</h2>
<ul>
<li><strong>Kalafat ve kaplama yenileme</strong> — su alan derzlerin ve yıpranmış kaplamaların onarımı</li>
<li><strong>Epoksi güçlendirme</strong> — çürük bölgelerin temizlenip epoksi ile yapısal onarımı</li>
<li><strong>Vernik ve boya</strong> — çok katlı vernik, ahşap boyama ve koruyucu uygulamalar</li>
<li><strong>Yapısal onarım</strong> — posta, döşek ve omurga elemanlarının yenilenmesi</li>
</ul>
<h2>Özgünlüğe saygı</h2>
<p>Tarihi teknelerde özgün malzeme ve yöntem kullanımına özen gösteririz. Amacımız tekneyi "yeni" göstermek değil, karakterini koruyarak <strong>bir sonraki nesle sağlam biçimde aktarmaktır</strong>.</p>
<h2>Fiyat ve süre</h2>
<p>Ahşap renovasyon; teknenin durumu, boyu ve işin kapsamına göre belirlenir. Bölgesel onarımlar birkaç hafta, kapsamlı restorasyonlar birkaç ay sürebilir. Keşif sonrası aşamalı bir plan ve kalem kalem teklif sunarız.</p>
""",
   "tiles": [
     {"h": "Gelenek + epoksi", "p": "Geleneksel kalafat ile modern epoksiyi birlikte kullanırız."},
     {"h": "Özgün doku", "p": "Tekneyi 'yeni' değil, karakterini koruyarak sağlam yaparız."},
     {"h": "Aşamalı plan", "p": "Kapsamlı restorasyonları bütçeye göre aşamalandırabiliriz."},
   ],
   "faqs": [
     {"q": "Ahşap teknemin çürükleri onarılabilir mi?", "a": "Çoğu durumda evet. Çürük bölge temizlenir, kurutulur ve epoksi/ahşap ekleme ile yapısal olarak yenilenir. Kapsam keşifte netleşir."},
     {"q": "Vernik mi boya mı önerirsiniz?", "a": "Ahşabın durumuna ve istediğiniz görünüme göre değişir. Doğal dokuyu göstermek isterseniz çok katlı vernik, daha korunaklı bir yüzey için boya öneririz."},
     {"q": "Klasik teknelerde orijinal malzeme kullanıyor musunuz?", "a": "Mümkün olduğunca özgün ahşap türü ve yöntemi kullanırız. Bulunamadığında dayanıklılığı ve görünümü en yakın alternatifi öneririz."},
   ],
 },
 "en": {
   "name": "Wooden Boat Refit",
   "short": "Comprehensive restoration of classic wooden boats that preserves their original character.",
   "bullets": ["Caulking & planking renewal", "Epoxy reinforcement", "Varnish & paint", "Structural repair"],
   "hero_title": "Wooden Boat Restoration & Refit",
   "hero_sub": "Preserving the soul of classic wooden boats — with caulking, planking, varnish and structural repair we bring your boat back to life.",
   "meta_title": "Wooden Boat Restoration & Refit | Tekne Usta",
   "meta_desc": "Wooden boat repair, restoration and refit: caulking, planking renewal, epoxy reinforcement, varnish and paint in Istanbul and the Aegean. Craftsmanship that respects original character.",
   "body": """
<h2>Craftsmanship that does wood justice</h2>
<p>Wooden boats demand patience and skill. We combine traditional caulking and joinery with modern epoxy and lamination to strengthen your boat <strong>without spoiling its original character</strong>. A classic sailboat, a tirhandil or a gulet — every wooden boat is treated on its own terms.</p>
<h2>Wooden boat work we do</h2>
<ul>
<li><strong>Caulking & planking renewal</strong> — repairing leaking seams and worn planking</li>
<li><strong>Epoxy reinforcement</strong> — cleaning out rot and rebuilding structurally with epoxy</li>
<li><strong>Varnish & paint</strong> — multi-coat varnish, wood painting and protective treatments</li>
<li><strong>Structural repair</strong> — renewing frames, floors and keel members</li>
</ul>
<h2>Respect for originality</h2>
<p>On historic boats we take care to use original materials and methods. Our aim isn't to make the boat look "new" but to preserve its character and <strong>hand it safely to the next generation</strong>.</p>
<h2>Price and timing</h2>
<p>A wooden refit depends on the boat's condition, length and scope of work. Local repairs take a few weeks; full restorations can take several months. After the survey we present a staged plan and an itemised quote.</p>
""",
   "tiles": [
     {"h": "Tradition + epoxy", "p": "We combine traditional caulking with modern epoxy."},
     {"h": "Original character", "p": "We make the boat sound while keeping its character, not faking 'new'."},
     {"h": "Staged plan", "p": "Large restorations can be staged to suit your budget."},
   ],
   "faqs": [
     {"q": "Can the rot in my wooden boat be repaired?", "a": "In most cases, yes. The rotten area is cut out, dried and rebuilt structurally with epoxy or a wood graft. Scope is confirmed at the survey."},
     {"q": "Do you recommend varnish or paint?", "a": "It depends on the wood's condition and the look you want. For a natural grain we recommend multi-coat varnish; for a more protected surface, paint."},
     {"q": "Do you use original materials on classic boats?", "a": "We use the original timber species and methods wherever possible. When unavailable, we recommend the closest match for durability and appearance."},
   ],
 },
},
{
 "slug": "tekne-boyama-antifouling", "slug_en": "boat-painting-antifouling",
 "image": "/assets/images/services/boya.jpg",
 "deep": {
   "tr": """
<h2>Antifouling türleri: hangisi hangi tekneye?</h2>
<p>Doğru zehirli boya, teknenin kullanımına göre değişir. Aşağıdaki tablo ana tipleri özetliyor (detay için <a href="/blog/antifouling-secimi/">antifouling seçim rehberi</a>).</p>
<table>
<thead><tr><th>Tip</th><th>Uygun tekne</th><th>Özellik</th></tr></thead>
<tbody>
<tr><td>Sert matris (hard)</td><td>Hızlı / sık çekilen / yarış</td><td>Aşınmaz, ara zımpara ister</td></tr>
<tr><td>Aşınan (self-polishing)</td><td>Gezi / orta hız</td><td>Kontrollü aşınır, katman birikmez</td></tr>
<tr><td>Ablatif</td><td>Az kullanılan</td><td>Yumuşak, ekonomik</td></tr>
<tr><td>Bakırsız (alüminyum)</td><td>Alüminyum gövde</td><td>Korozyonu önler</td></tr>
</tbody>
</table>
<h2>Kalıcı boyanın sırrı: yüzey hazırlığı</h2>
<p>Maliyetin ve kalitenin çoğu boyada değil, hazırlıktadır. Doğru zımpara, yağdan arındırma, dolgu ve astar olmadan en pahalı boya bile kısa sürede kabarır. Biz teklifi <strong>kalem kalem</strong> veririz; hazırlık, astar, kat sayısı ve işçilik ayrı görünür — böylece ucuz görünüp yarım kalan işlerden kaçınırsınız (bkz. <a href="/blog/tekne-boyama-maliyeti/">boyama maliyeti</a>).</p>
<h2>Dış cephe: gelcoat mı, boya mı?</h2>
<p>Solmuş bir yüzeyi yenilerken jelkot ve boya farklı amaçlara hizmet eder. Yüzey sağlamsa jelkot yenileme ekonomiktir; renk değişimi veya süperyat parlaklığı için <a href="/blog/2k-poliuretan-boya/">2K poliüretan</a> boya tercih edilir. Karar için <a href="/blog/jelkot-vs-boya/">jelkot mu boya mı</a> yazımıza bakın.</p>
""",
   "en": """
<h2>Antifouling types: which for which boat?</h2>
<p>The right antifouling depends on how the boat is used. The table below sums up the main types (for detail, see the <a href="/en/blog/choosing-antifouling/">antifouling selection guide</a>).</p>
<table>
<thead><tr><th>Type</th><th>Suited to</th><th>Trait</th></tr></thead>
<tbody>
<tr><td>Hard matrix</td><td>Fast / often hauled / racing</td><td>Non-eroding, needs occasional sanding</td></tr>
<tr><td>Self-polishing</td><td>Cruising / mid speed</td><td>Erodes in a controlled way, no build-up</td></tr>
<tr><td>Ablative</td><td>Lightly used</td><td>Soft, economical</td></tr>
<tr><td>Copper-free (aluminium)</td><td>Aluminium hulls</td><td>Prevents corrosion</td></tr>
</tbody>
</table>
<h2>The secret to lasting paint: surface prep</h2>
<p>Most of the cost and quality is in the prep, not the paint. Without correct sanding, degreasing, filling and priming, even the most expensive paint soon blisters. We quote <strong>itemised</strong> — prep, primer, coat count and labour shown separately — so you avoid cheap-looking jobs that end up half-done (see <a href="/en/blog/boat-painting-cost/">painting cost</a>).</p>
<h2>Topside: gelcoat or paint?</h2>
<p>When renewing a faded surface, gelcoat and paint serve different aims. If the surface is sound, gelcoat renewal is economical; for a colour change or superyacht gloss, <a href="/en/blog/2k-polyurethane-paint/">2K polyurethane</a> paint is preferred. To decide, see our <a href="/en/blog/gelcoat-vs-paint/">gelcoat or paint</a> article.</p>
""",
 },
 "tr": {
   "name": "Boya & Antifouling",
   "short": "Antifouling, dış cephe boyası ve özel renk uygulamalarıyla teknenize yeni bir kimlik.",
   "bullets": ["Antifouling (zehirli boya)", "Tam dış cephe boyama", "Kılavuz şerit ve grafik", "Epoksi astar sistemleri"],
   "hero_title": "Tekne Boyama ve Antifouling (Zehirli Boya)",
   "hero_sub": "Su altı antifouling'den süperyat kalitesinde dış cephe boyasına — doğru astar sistemi, temiz maskeleme ve kusursuz bir bitişle.",
   "meta_title": "Tekne Boyama ve Antifouling (Zehirli Boya) | Tekne Usta",
   "meta_desc": "Tekne boyama, antifouling (zehirli boya) uygulaması, dış cephe boyama, gelcoat ve epoksi astar sistemleri. İstanbul ve Ege'de temiz işçilik, doğru boya seçimi.",
   "body": """
<h2>Boya, teknenin hem kalkanı hem kimliğidir</h2>
<p>İyi bir boya işi sadece güzel görünmez; tekneyi UV, tuz ve deniz canlılarından korur. <strong>Tekne Usta</strong> olarak yüzey hazırlığına en az boya kadar önem veririz — çünkü kalıcı bir bitiş, doğru zımpara, astar ve maskeleme ile başlar.</p>
<h2>Boya hizmetlerimiz</h2>
<ul>
<li><strong>Antifouling (zehirli boya)</strong> — su altı için doğru zehirli boya seçimi ve uygulaması</li>
<li><strong>Tam dış cephe boyama</strong> — bordo ve üst yapı için çok katlı boya sistemleri</li>
<li><strong>Gelcoat ve epoksi astar</strong> — yüzeyin sağlam bir zemine oturtulması</li>
<li><strong>Kılavuz şerit, isim ve grafik</strong> — temiz maskeleme ile net çizgiler</li>
</ul>
<h2>Doğru antifouling seçimi</h2>
<p>Her tekneye aynı zehirli boya uymaz. Teknenizin malzemesine, hızına ve bağlandığı suyun karakterine göre <strong>sert matris mi, aşınan (self-polishing) tip mi</strong> gerektiğini birlikte belirleriz. Ayrıntılar için <a href="/blog/antifouling-secimi/">antifouling seçim rehberimize</a> bakın.</p>
<h2>Fiyat ve süre</h2>
<p>Boya fiyatı; tekne boyuna, kat sayısına ve yüzey hazırlığının kapsamına göre değişir. Sadece antifouling yenilemesi birkaç gün, komple dış cephe boyaması 1–3 hafta sürebilir. Keşifte yüzeyi görüp net teklif veririz.</p>
""",
   "tiles": [
     {"h": "Yüzey hazırlığı", "p": "Kalıcı bitiş, boyadan önce doğru zımpara ve astarla başlar."},
     {"h": "Doğru boya", "p": "Malzeme ve kullanıma göre antifouling ve boya sistemi seçeriz."},
     {"h": "Temiz çizgiler", "p": "Kılavuz şerit ve grafiklerde titiz maskeleme."},
   ],
   "faqs": [
     {"q": "Antifouling ne sıklıkla yenilenmeli?", "a": "Çoğu teknede yılda bir, sezon başında yenilenir. Kullanım yoğunluğu ve suyun karakteri sıklığı etkiler; keşifte size özel öneri veririz."},
     {"q": "Eski boyayı sökmek gerekiyor mu?", "a": "Katlar kalınlaşıp yapışması zayıfladıysa evet. Aksi halde yüzey hazırlığıyla üzerine uygulanabilir. Durumu keşifte değerlendiririz."},
     {"q": "Renk değişimi yapabilir misiniz?", "a": "Evet, dış cephe rengini tamamen değiştirebiliriz. Doğru astar sistemiyle kalıcı ve düzgün bir sonuç elde edilir."},
   ],
 },
 "en": {
   "name": "Painting & Antifouling",
   "short": "Antifouling, topside painting and custom colour that give your boat a new identity.",
   "bullets": ["Antifouling", "Full topside painting", "Boot stripe & graphics", "Epoxy primer systems"],
   "hero_title": "Boat Painting & Antifouling",
   "hero_sub": "From below-waterline antifouling to superyacht-grade topside paint — with the right primer system, clean masking and a flawless finish.",
   "meta_title": "Boat Painting & Antifouling | Tekne Usta",
   "meta_desc": "Boat painting, antifouling application, topside painting, gelcoat and epoxy primer systems in Istanbul and the Aegean. Clean workmanship and the right paint choice.",
   "body": """
<h2>Paint is both the boat's shield and its identity</h2>
<p>A good paint job doesn't just look good; it protects the boat from UV, salt and marine growth. At <strong>Tekne Usta</strong> we treat surface preparation as seriously as the paint itself — because a lasting finish starts with correct sanding, priming and masking.</p>
<h2>Our painting services</h2>
<ul>
<li><strong>Antifouling</strong> — choosing and applying the right antifouling below the waterline</li>
<li><strong>Full topside painting</strong> — multi-coat systems for hull and superstructure</li>
<li><strong>Gelcoat & epoxy primer</strong> — building the surface on a sound base</li>
<li><strong>Boot stripe, name and graphics</strong> — crisp lines with clean masking</li>
</ul>
<h2>Choosing the right antifouling</h2>
<p>Not every antifouling suits every boat. Together we decide whether you need a <strong>hard matrix or a self-polishing type</strong> based on your boat's material, speed and the water it sits in. See our <a href="/en/blog/choosing-antifouling/">antifouling guide</a> for detail.</p>
<h2>Price and timing</h2>
<p>Painting cost depends on boat length, number of coats and the extent of surface prep. An antifouling refresh takes a few days; a full topside repaint 1–3 weeks. We give a firm quote after inspecting the surface.</p>
""",
   "tiles": [
     {"h": "Surface prep", "p": "A lasting finish starts with correct sanding and priming."},
     {"h": "Right paint", "p": "We select the antifouling and paint system for the material and use."},
     {"h": "Crisp lines", "p": "Meticulous masking on boot stripes and graphics."},
   ],
   "faqs": [
     {"q": "How often should antifouling be renewed?", "a": "On most boats once a year, at the start of the season. Usage and water conditions affect frequency; we give tailored advice at the survey."},
     {"q": "Does the old paint need stripping?", "a": "If the coats have built up and adhesion is failing, yes. Otherwise it can be overcoated after prep. We assess this at the survey."},
     {"q": "Can you change the colour?", "a": "Yes, we can fully change the topside colour. With the right primer system the result is durable and even."},
   ],
 },
},
{
 "slug": "teak-guverte-doseme", "slug_en": "teak-deck",
 "image": "/assets/images/services/ic-mekan.jpg",
 "deep": {
   "tr": """
<h2>Teak seçenekleri karşılaştırması</h2>
<p>Güverte döşemede doğal ve sentetik seçeneklerin her birinin yeri var. Aşağıdaki tablo karar vermeyi kolaylaştırır (detay: <a href="/blog/teak-vs-sentetik-teak/">teak vs sentetik</a>).</p>
<table>
<thead><tr><th>Seçenek</th><th>Bakım</th><th>Öne çıkan</th></tr></thead>
<tbody>
<tr><td>Doğal teak (tik)</td><td>Düzenli bakım ister</td><td>Eşsiz doku, klasik prestij</td></tr>
<tr><td>PVC teak (Flexiteek tarzı)</td><td>Bakımsız</td><td>Dikişsiz, su geçirmez</td></tr>
<tr><td>EVA köpük</td><td>Bakımsız</td><td>Ekonomik, yumuşak, kaymaz</td></tr>
</tbody>
</table>
<p>Sentetik alternatiflerin ayrıntısı için <a href="/blog/sentetik-teak-alternatifleri/">bu yazıya</a> bakın.</p>
<h2>Sadece derz mi, komple döşeme mi?</h2>
<p>Karar teak kalınlığına bağlıdır. Teak hâlâ yeterince kalınsa <a href="/blog/teak-derz-yenileme/">derz yenileme</a> çok daha ekonomiktir; su sızdırmazlığı geri kazandırır. Teak inceldiyse komple döşeme gerekir. Keşifte kalınlığı ölçüp sizi doğru yönlendiririz — gereksiz büyük iş önermeyiz.</p>
<h2>İşçilik farkı</h2>
<p>Teakta sonucu belirleyen düz çizgiler, temiz köşe geçişleri ve su geçirmez derzlerdir. Fiyatı etkileyen kalemleri <a href="/blog/teak-guverte-fiyatlari/">teak güverte fiyatları</a> yazımızda açıkladık.</p>
""",
   "en": """
<h2>Teak options compared</h2>
<p>In decking, natural and synthetic options each have their place. The table below makes deciding easier (detail: <a href="/en/blog/teak-vs-synthetic-teak/">teak vs synthetic</a>).</p>
<table>
<thead><tr><th>Option</th><th>Maintenance</th><th>Stands out for</th></tr></thead>
<tbody>
<tr><td>Natural teak</td><td>Needs regular care</td><td>Unique grain, classic prestige</td></tr>
<tr><td>PVC teak (Flexiteek-style)</td><td>Maintenance-free</td><td>Seamless, waterproof</td></tr>
<tr><td>EVA foam</td><td>Maintenance-free</td><td>Economical, soft, non-slip</td></tr>
</tbody>
</table>
<p>For detail on synthetic alternatives, see <a href="/en/blog/synthetic-teak-alternatives/">this article</a>.</p>
<h2>Seams only, or a full deck?</h2>
<p>The decision depends on teak thickness. If the teak is still thick enough, <a href="/en/blog/teak-seam-renewal/">seam renewal</a> is far more economical and restores watertightness. If thinned, a full deck is needed. We measure the thickness at the survey and advise you correctly — we don't recommend needless big work.</p>
<h2>The workmanship difference</h2>
<p>In teak, straight lines, clean corner transitions and watertight seams decide the result. We explain the items that affect price in our <a href="/en/blog/teak-deck-cost/">teak deck cost</a> article.</p>
""",
 },
 "tr": {
   "name": "Teak Güverte Döşeme",
   "short": "Yeni teak güverte döşeme, eski teak yenileme ve profesyonel teak bakımı.",
   "bullets": ["Yeni teak döşeme", "Eski teak yenileme", "Derz (kalafat) yenileme", "Teak bakım ve zımpara"],
   "hero_title": "Teak Güverte Döşeme ve Yenileme",
   "hero_sub": "Klasik teak görünümünden modern sentetik teak alternatiflerine — güvertenizi hem şık hem güvenli bir yürüyüş yüzeyine dönüştürüyoruz.",
   "meta_title": "Teak Güverte Döşeme ve Yenileme | Tekne Usta",
   "meta_desc": "Teak güverte döşeme, eski teak yenileme, derz (kalafat) yenileme ve teak bakımı. İstanbul ve Ege'de titiz işçilikle doğal veya sentetik teak uygulaması.",
   "body": """
<h2>Güverte, teknenin ilk izlenimidir</h2>
<p>Teak güverte hem estetiği hem güvenliğiyle teknenin en çok göze çarpan yüzeyidir. Yıllar içinde teak incelir, derzler açılır ve su altına sızmaya başlar. <strong>Tekne Usta</strong> olarak yeni teak döşeme, eskisini yenileme ve derz onarımını titiz bir işçilikle yapıyoruz.</p>
<h2>Teak hizmetlerimiz</h2>
<ul>
<li><strong>Yeni teak güverte döşeme</strong> — doğal teak veya bakım gerektirmeyen sentetik teak seçenekleri</li>
<li><strong>Eski teak yenileme</strong> — zımpara, derz yenileme ve yüzey restorasyonu</li>
<li><strong>Derz (kalafat) yenileme</strong> — su sızdıran siyah derzlerin sökülüp yeniden yapılması</li>
<li><strong>Periyodik teak bakımı</strong> — teakın gri değil sıcak tonunu koruması için bakım</li>
</ul>
<h2>Doğal mı, sentetik teak mi?</h2>
<p>Doğal teakın dokusu eşsizdir ama düzenli bakım ister. Sentetik teak ise <strong>bakım gerektirmez, sıcakta yumuşamaz</strong> ve renk seçenekleri geniştir. Kullanımınıza ve bütçenize göre ikisini de öneririz.</p>
<h2>Fiyat ve süre</h2>
<p>Teak döşeme fiyatı; güverte alanına, seçilen malzemeye ve derz durumuna göre değişir. Bölgesel yenilemeler birkaç gün, komple güverte döşeme 1–3 hafta sürebilir.</p>
""",
   "tiles": [
     {"h": "Doğal veya sentetik", "p": "Kullanımınıza göre doğal teak veya bakımsız sentetik teak."},
     {"h": "Su geçirmez derz", "p": "Derz yenilemede su sızdırmazlığı önceliğimizdir."},
     {"h": "Titiz işçilik", "p": "Düz çizgiler ve temiz köşe geçişleri."},
   ],
   "faqs": [
     {"q": "Sentetik teak doğala göre nasıl?", "a": "Görünüm olarak çok yakındır; avantajı bakım gerektirmemesi, kaymaması ve sıcakta yumuşamamasıdır. Doğal teakın dokusunu isteyenler için doğal seçenek de sunuyoruz."},
     {"q": "Sadece derzler yenilenebilir mi?", "a": "Teak kalınlığı yeterliyse evet — eski derzleri söküp yenileyerek su sızdırmazlığı geri kazandırırız. Teak inceldiyse komple döşeme öneririz."},
     {"q": "Teak neden griye döner?", "a": "UV ve tuz etkisiyle yüzey oksitlenir. Düzenli bakımla sıcak tonu korunur; ihmal edilirse zımpara ile yenilenir."},
   ],
 },
 "en": {
   "name": "Teak Decking",
   "short": "New teak decking, renewal of old teak and professional teak maintenance.",
   "bullets": ["New teak decking", "Old teak renewal", "Seam (caulking) renewal", "Teak care & sanding"],
   "hero_title": "Teak Deck Laying & Renewal",
   "hero_sub": "From classic teak looks to modern synthetic teak alternatives — we turn your deck into a walking surface that's both elegant and safe.",
   "meta_title": "Teak Deck Laying & Renewal | Tekne Usta",
   "meta_desc": "Teak decking, old teak renewal, seam (caulking) renewal and teak maintenance in Istanbul and the Aegean. Natural or synthetic teak laid with meticulous craftsmanship.",
   "body": """
<h2>The deck is a boat's first impression</h2>
<p>A teak deck is the most eye-catching surface on a boat, for both looks and safety. Over the years teak thins, seams open and water starts to seep below. At <strong>Tekne Usta</strong> we lay new teak, renew old decks and repair seams with meticulous craftsmanship.</p>
<h2>Our teak services</h2>
<ul>
<li><strong>New teak decking</strong> — natural teak or maintenance-free synthetic teak options</li>
<li><strong>Old teak renewal</strong> — sanding, seam renewal and surface restoration</li>
<li><strong>Seam (caulking) renewal</strong> — removing and remaking leaking black seams</li>
<li><strong>Regular teak care</strong> — keeping teak warm-toned rather than grey</li>
</ul>
<h2>Natural or synthetic teak?</h2>
<p>Natural teak has an unmatched grain but needs regular care. Synthetic teak <strong>needs no maintenance, won't soften in heat</strong> and offers a wide colour range. We recommend both depending on your use and budget.</p>
<h2>Price and timing</h2>
<p>Teak decking cost depends on deck area, chosen material and seam condition. Local renewals take a few days; a full deck 1–3 weeks.</p>
""",
   "tiles": [
     {"h": "Natural or synthetic", "p": "Natural teak, or maintenance-free synthetic, to suit your use."},
     {"h": "Watertight seams", "p": "Watertightness is our priority in seam renewal."},
     {"h": "Meticulous work", "p": "Straight lines and clean corner transitions."},
   ],
   "faqs": [
     {"q": "How does synthetic teak compare to natural?", "a": "It looks very close; the advantage is no maintenance, non-slip and no softening in heat. For those who want the real grain, we also offer natural teak."},
     {"q": "Can just the seams be renewed?", "a": "If the teak is still thick enough, yes — we remove and remake the old seams to restore watertightness. If the teak has thinned, we recommend a full deck."},
     {"q": "Why does teak turn grey?", "a": "UV and salt oxidise the surface. Regular care keeps the warm tone; if neglected, it's renewed by sanding."},
   ],
 },
},
{
 "slug": "ic-mekan-yenileme", "slug_en": "interior-refit",
 "image": "/assets/images/services/bakim.jpg",
 "deep": {
   "tr": """
<h2>Neyi yenileyebiliriz?</h2>
<p>İç mekan yenileme, küçük bir dokunuştan komple dönüşüme kadar esnektir. Aşağıdaki tablo başlıca kalemleri ve faydalarını özetliyor.</p>
<table>
<thead><tr><th>Öğe</th><th>Malzeme / çözüm</th><th>Fayda</th></tr></thead>
<tbody>
<tr><td>Minder &amp; döşeme</td><td><a href="/blog/tekne-doseme-kumas-secimi/">Deniz sınıfı kumaş</a> + hızlı kuruyan sünger</td><td>Konfor, küf direnci</td></tr>
<tr><td>Perde &amp; stor</td><td>Blackout / güneşlik</td><td><a href="/blog/tekne-perde-stor/">Mahremiyet, ısı kontrolü</a></td></tr>
<tr><td>Aydınlatma</td><td><a href="/blog/kabin-led-aydinlatma/">LED katmanlı</a></td><td>Verimli, ferah his</td></tr>
<tr><td>Dolap &amp; galley</td><td>Ölçüye özel marangozluk</td><td>Depolama, düzen</td></tr>
</tbody>
</table>
<h2>Küçük alanı büyük göstermek</h2>
<p>Açık renkler, katmanlı aydınlatma ve akıllı depolama; sınırlı kabini çok daha ferah hissettirir. Fikirler için <a href="/blog/ic-mekan-yenileme-fikirleri/">iç mekan yenileme fikirleri</a> yazımıza bakın.</p>
<h2>Nem ve küfü baştan çözmek</h2>
<p>Yenilemeyi kalıcı kılmak için nemi kaynağında ele alırız: doğru havalandırma ve <a href="/blog/teknede-kuf-nem-onleme/">küf önleme</a> önlemleriyle döşemeniz uzun ömürlü olur. Aksi halde en güzel yenileme bile kısa sürede lekelenir.</p>
""",
   "en": """
<h2>What can we renew?</h2>
<p>An interior refit is flexible, from a small touch to a full transformation. The table below sums up the main items and their benefits.</p>
<table>
<thead><tr><th>Item</th><th>Material / solution</th><th>Benefit</th></tr></thead>
<tbody>
<tr><td>Cushions &amp; upholstery</td><td><a href="/en/blog/marine-upholstery-fabric/">Marine-grade fabric</a> + quick-dry foam</td><td>Comfort, mould resistance</td></tr>
<tr><td>Curtains &amp; blinds</td><td>Blackout / shade</td><td><a href="/en/blog/boat-curtains-blinds/">Privacy, heat control</a></td></tr>
<tr><td>Lighting</td><td><a href="/en/blog/cabin-led-lighting/">Layered LED</a></td><td>Efficient, spacious feel</td></tr>
<tr><td>Cabinetry &amp; galley</td><td>Made-to-measure joinery</td><td>Storage, order</td></tr>
</tbody>
</table>
<h2>Making a small space feel bigger</h2>
<p>Light colours, layered lighting and smart storage make a limited cabin feel far more spacious. For ideas, see our <a href="/en/blog/interior-refit-ideas/">interior refit ideas</a> article.</p>
<h2>Solving damp and mould from the start</h2>
<p>To make the refit last, we address damp at its source: with proper ventilation and <a href="/en/blog/preventing-mould-damp/">mould prevention</a>, your upholstery lasts. Otherwise even the finest refit soon stains.</p>
""",
 },
 "tr": {
   "name": "İç Mekan Yenileme",
   "short": "Teknenizin iç mekânını konfor ve estetik açısından baştan tasarlıyoruz.",
   "bullets": ["Kumaş ve sünger değişimi", "Dolap ve mutfak yenileme", "Kabin aydınlatma", "İç ahşap ve kaplama"],
   "hero_title": "Tekne İç Mekan Döşeme ve Yenileme",
   "hero_sub": "Kumaş ve süngerden dolap ve aydınlatmaya — kabininizi daha konforlu, daha aydınlık ve size ait bir alana dönüştürüyoruz.",
   "meta_title": "Tekne İç Mekan Döşeme ve Yenileme | Tekne Usta",
   "meta_desc": "Tekne iç döşeme, kumaş ve sünger değişimi, dolap ve mutfak yenileme, kabin aydınlatma ve iç ahşap kaplama. İstanbul ve Ege'de konfor odaklı iç mekan yenileme.",
   "body": """
<h2>Konfor, teknede vakit geçirmenin anahtarıdır</h2>
<p>İç mekân yıprandığında tekneyle geçirilen zaman keyifsizleşir. Solmuş kumaşlar, çökmüş süngerler, eskiyen dolaplar… <strong>Tekne Usta</strong> olarak kabini baştan ele alır, hem estetiği hem işlevi yenileriz.</p>
<h2>İç mekan hizmetlerimiz</h2>
<ul>
<li><strong>Kumaş ve sünger değişimi</strong> — minder, döşeme ve perdelerin yenilenmesi</li>
<li><strong>Dolap, mutfak ve marangozluk</strong> — depolama ve mutfak çözümlerinin yenilenmesi</li>
<li><strong>Kabin aydınlatma</strong> — LED ve enerji verimli aydınlatma</li>
<li><strong>İç ahşap ve kaplama</strong> — yüzeylerin cilalanması ve yenilenmesi</li>
</ul>
<h2>Nemle ve deniz koşullarıyla uyumlu malzeme</h2>
<p>Teknede kullanılan kumaş ve süngerler evdekinden farklıdır; <strong>neme, küfe ve UV'ye dayanıklı</strong> deniz sınıfı malzemeler seçeriz. Böylece yenileme uzun ömürlü olur.</p>
<h2>Fiyat ve süre</h2>
<p>İç mekan yenileme; kapsamına göre birkaç günden birkaç haftaya kadar değişir. Sadece döşeme yenileme mi, komple iç mekan mı istediğinizi keşifte netleştirir, kalem kalem teklif veririz.</p>
""",
   "tiles": [
     {"h": "Deniz sınıfı malzeme", "p": "Neme, küfe ve UV'ye dayanıklı kumaş ve sünger."},
     {"h": "Konfor + estetik", "p": "Hem görünümü hem kullanımı birlikte yeniliyoruz."},
     {"h": "Ölçüye özel", "p": "Minder ve dolaplar teknenize özel üretilir."},
   ],
   "faqs": [
     {"q": "Sadece minderleri yeniletebilir miyim?", "a": "Elbette. Kumaş ve sünger değişimini bağımsız yapıyoruz; komple iç mekan yenileme şart değil."},
     {"q": "Hangi kumaşları öneriyorsunuz?", "a": "Deniz koşullarına dayanıklı, leke ve UV direnci yüksek deniz sınıfı kumaşlar öneriyoruz. Renk ve doku seçimini birlikte yapıyoruz."},
     {"q": "İş sırasında teknemi kullanabilir miyim?", "a": "Kapsamlı işlerde tekne kısa süre servistedir. Planı sezon programınıza göre ayarlarız."},
   ],
 },
 "en": {
   "name": "Interior Refit",
   "short": "We redesign your boat's interior for comfort and style, from the ground up.",
   "bullets": ["Upholstery & foam renewal", "Cabinetry & galley renewal", "Cabin lighting", "Interior woodwork"],
   "hero_title": "Boat Interior Refit & Upholstery",
   "hero_sub": "From upholstery and foam to cabinetry and lighting — we turn your cabin into a more comfortable, brighter space that feels like yours.",
   "meta_title": "Boat Interior Refit & Upholstery | Tekne Usta",
   "meta_desc": "Boat interior refit, upholstery and foam renewal, cabinetry and galley renewal, cabin lighting and interior woodwork in Istanbul and the Aegean.",
   "body": """
<h2>Comfort is the key to time aboard</h2>
<p>When the interior wears out, time aboard loses its charm. Faded fabrics, collapsed foam, tired cabinetry… At <strong>Tekne Usta</strong> we take the cabin in hand and renew both looks and function.</p>
<h2>Our interior services</h2>
<ul>
<li><strong>Upholstery & foam renewal</strong> — cushions, upholstery and curtains</li>
<li><strong>Cabinetry, galley & joinery</strong> — renewing storage and galley solutions</li>
<li><strong>Cabin lighting</strong> — LED and energy-efficient lighting</li>
<li><strong>Interior woodwork & veneer</strong> — refinishing and renewing surfaces</li>
</ul>
<h2>Materials made for damp, marine conditions</h2>
<p>The fabrics and foams used aboard differ from those at home; we choose <strong>marine-grade materials resistant to damp, mould and UV</strong>, so the refit lasts.</p>
<h2>Price and timing</h2>
<p>An interior refit ranges from a few days to a few weeks depending on scope. We confirm at the survey whether you want just upholstery or a full interior, and quote itemised.</p>
""",
   "tiles": [
     {"h": "Marine-grade materials", "p": "Fabric and foam resistant to damp, mould and UV."},
     {"h": "Comfort + style", "p": "We renew both the look and the way it's used."},
     {"h": "Made to measure", "p": "Cushions and cabinetry built specifically for your boat."},
   ],
   "faqs": [
     {"q": "Can I just have the cushions redone?", "a": "Of course. We renew upholstery and foam independently; a full interior refit isn't required."},
     {"q": "Which fabrics do you recommend?", "a": "Marine-grade fabrics with high stain and UV resistance. We choose colour and texture together with you."},
     {"q": "Can I use my boat during the work?", "a": "For larger jobs the boat is in the workshop briefly. We schedule around your season plan."},
   ],
 },
},
{
 "slug": "tekne-kislatma", "slug_en": "winterising-storage",
 "image": "/assets/images/services/motor.jpg",
 "deep": {
   "tr": """
<h2>Depolama seçenekleri karşılaştırması</h2>
<p>Tekneyi kışın nerede sakladığınız, hem korumayı hem maliyeti belirler. Aşağıdaki tablo seçenekleri özetliyor (detay: <a href="/blog/kisin-tekne-nerede-saklanir/">kışın tekne nerede saklanır</a>).</p>
<table>
<thead><tr><th>Seçenek</th><th>Artı</th><th>Dikkat</th></tr></thead>
<tbody>
<tr><td>Karada (hardstand)</td><td>Karina kurur, bakım kolay, osmoz riski azalır</td><td>Doğru payanda + havalandırmalı örtü</td></tr>
<tr><td>Suda (marina)</td><td>Çekme maliyeti yok, hızlı erişim</td><td>Kirlenme, osmoz, buzlanma riski</td></tr>
<tr><td>Kapalı depo</td><td>Tam koruma, jelkot/ahşap için ideal</td><td>Maliyet ve yer sınırlı</td></tr>
</tbody>
</table>
<h2>Kışlatma bir kontrol listesi işidir</h2>
<p>İyi bir kışlatma rastgele değil, adım adım yapılır: karaya çekme, basınçlı yıkama, karina ve <a href="/blog/anot-zinc-bakimi/">anot</a> kontrolü, iç mekan havalandırması ve <a href="/blog/tekne-ortusu-secimi/">doğru örtü</a>. Tüm adımları <a href="/blog/tekne-kislatma-kontrol-listesi/">kışlatma kontrol listemizde</a> topladık.</p>
<h2>Kapsamımız (ve dışında kalanlar)</h2>
<p>Karaya çekme, karina, örtü ve gözetimli depolama tarafında tam hizmet veriyoruz. <strong>Motor ve mekanik kışlatma</strong> uzmanlık alanımız dışında; bu iş için güvendiğimiz servislere yönlendiriyoruz. Bahar açılışında karina ve boya durumunu birlikte değerlendirip <a href="/blog/bahar-tekne-bakimi/">bahar bakımını</a> önceden planlıyoruz.</p>
""",
   "en": """
<h2>Storage options compared</h2>
<p>Where you store the boat in winter determines both protection and cost. The table below sums up the options (detail: <a href="/en/blog/winter-boat-storage/">where to store a boat in winter</a>).</p>
<table>
<thead><tr><th>Option</th><th>Pro</th><th>Watch for</th></tr></thead>
<tbody>
<tr><td>Ashore (hardstand)</td><td>Hull dries, easy maintenance, lower osmosis risk</td><td>Correct props + ventilated cover</td></tr>
<tr><td>Afloat (marina)</td><td>No lift cost, quick access</td><td>Growth, osmosis, ice risk</td></tr>
<tr><td>Indoor storage</td><td>Full protection, ideal for gelcoat/wood</td><td>Cost and limited space</td></tr>
</tbody>
</table>
<h2>Winterising is a checklist job</h2>
<p>Good winterising isn't random but step by step: haul-out, pressure wash, hull and <a href="/en/blog/anode-zinc-care/">anode</a> checks, interior ventilation and the <a href="/en/blog/boat-cover-selection/">right cover</a>. We've gathered all the steps in our <a href="/en/blog/boat-winterising-checklist/">winterising checklist</a>.</p>
<h2>Our scope (and what's outside it)</h2>
<p>We provide full service for haul-out, hull, covering and supervised storage. <strong>Engine and mechanical winterising</strong> is outside our expertise; we refer you to services we trust for that. At spring launch we assess hull and paint together and plan <a href="/en/blog/spring-boat-maintenance/">spring maintenance</a> ahead.</p>
""",
 },
 "tr": {
   "name": "Tekne Kışlatma",
   "short": "Sezonu güvenle kapatmak için karaya çekme, tekne yıkama ve kış muhafazası.",
   "bullets": ["Karaya çekme ve yıkama", "Karina temizliği", "Kış muhafaza örtüsü", "Güvenli depolama"],
   "hero_title": "Tekne Kışlatma ve Kış Muhafazası",
   "hero_sub": "Karaya çekmeden karina temizliğine, örtüden güvenli depolamaya — teknenizi kışa hazırlayıp bir sonraki sezona sağlam çıkarıyoruz.",
   "meta_title": "Tekne Kışlatma ve Kış Muhafazası | Tekne Usta",
   "meta_desc": "Tekne kışlatma, karaya çekme, karina temizliği, kış muhafaza örtüsü ve güvenli depolama. İstanbul ve Ege'de sezon sonu tekne bakımı ve kışlatma paketleri.",
   "body": """
<h2>İyi bir kışlatma, sezonu erken açar</h2>
<p>Tekneyi kışa doğru hazırlamak, ilkbaharda hem zaman hem para kazandırır. Karaya çekilmeden bekleyen, doğru örtülmeyen tekneler nem, küf ve karina sorunlarıyla sezona başlar. <strong>Tekne Usta</strong> olarak kışlatmayı bir kontrol listesi disipliniyle yaparız.</p>
<h2>Kışlatma paketimiz</h2>
<ul>
<li><strong>Karaya çekme ve basınçlı yıkama</strong> — sezon boyunca biriken deniz kirinin temizlenmesi</li>
<li><strong>Karina temizliği ve kontrol</strong> — antifouling ve su altı yüzeyin durum tespiti</li>
<li><strong>Kış muhafaza örtüsü</strong> — nem ve UV'ye karşı doğru havalandırmalı örtü</li>
<li><strong>Güvenli depolama</strong> — teknenizin gözetim altında bekletilmesi</li>
</ul>
<p><em>Not: Motor ve mekanik kışlatma işlemleri kapsamımız dışındadır; bu alanda güvendiğimiz servislere yönlendirme yapabiliriz.</em></p>
<h2>İlkbaharda hazır tekne</h2>
<p>Kış boyunca teknenizi takip eder, sezon açılışında karina ve boya durumunu birlikte değerlendiririz. Bahar bakımını önceden planlarsanız, suya ilk teknelerden biriyle inersiniz.</p>
<h2>Fiyat ve süre</h2>
<p>Kışlatma fiyatı; tekne boyuna, çekme yöntemine ve örtü tipine göre belirlenir. Sezon sonu erken rezervasyon önerilir çünkü çekek alanları hızla dolar.</p>
""",
   "tiles": [
     {"h": "Kontrol listesi", "p": "Kışlatmayı adım adım, atlama yapmadan uygularız."},
     {"h": "Doğru örtü", "p": "Nem ve küfü önleyen havalandırmalı muhafaza."},
     {"h": "Erken sezon", "p": "Bahar bakımını önceden planlayıp erken suya iniş."},
   ],
   "faqs": [
     {"q": "Kışlatma ne zaman yaptırılmalı?", "a": "Genellikle sonbaharda, sezonun kapanmasıyla. Çekek alanları dolduğu için erken rezervasyon avantajlıdır."},
     {"q": "Motor kışlatması yapıyor musunuz?", "a": "Motor ve mekanik kışlatma kapsamımız dışında. Karaya çekme, karina, örtü ve depolama tarafında tam hizmet veriyoruz; motor için güvendiğimiz servislere yönlendirebiliriz."},
     {"q": "Kış boyunca teknem kontrol edilir mi?", "a": "Evet, depolama süresince teknenizi gözetim altında tutar, gerektiğinde sizi bilgilendiririz."},
   ],
 },
 "en": {
   "name": "Winterising & Storage",
   "short": "Close the season safely — haul-out, wash-down and winter storage.",
   "bullets": ["Haul-out & wash-down", "Hull cleaning", "Winter cover", "Secure storage"],
   "hero_title": "Boat Winterising & Winter Storage",
   "hero_sub": "From haul-out and hull cleaning to covering and secure storage — we prepare your boat for winter and bring it through ready for the next season.",
   "meta_title": "Boat Winterising & Winter Storage | Tekne Usta",
   "meta_desc": "Boat winterising, haul-out, hull cleaning, winter covers and secure storage in Istanbul and the Aegean. End-of-season boat care and winterising packages.",
   "body": """
<h2>Good winterising opens the season early</h2>
<p>Preparing a boat for winter saves both time and money in spring. Boats left afloat and poorly covered start the season with damp, mould and hull problems. At <strong>Tekne Usta</strong> we winterise with the discipline of a checklist.</p>
<h2>Our winterising package</h2>
<ul>
<li><strong>Haul-out & pressure wash</strong> — removing a season's marine growth</li>
<li><strong>Hull cleaning & inspection</strong> — assessing antifouling and the underwater surface</li>
<li><strong>Winter cover</strong> — a properly ventilated cover against damp and UV</li>
<li><strong>Secure storage</strong> — keeping your boat under supervision</li>
</ul>
<p><em>Note: engine and mechanical winterising is outside our scope; we can refer you to services we trust for that.</em></p>
<h2>A boat that's ready in spring</h2>
<p>We keep an eye on your boat through winter and assess the hull and paint together at the start of the season. Plan spring maintenance ahead and you'll be among the first back in the water.</p>
<h2>Price and timing</h2>
<p>Winterising cost depends on boat length, haul-out method and cover type. Early end-of-season booking is recommended as hardstanding fills up fast.</p>
""",
   "tiles": [
     {"h": "Checklist", "p": "We winterise step by step, skipping nothing."},
     {"h": "Right cover", "p": "A ventilated cover that prevents damp and mould."},
     {"h": "Early season", "p": "Plan spring maintenance ahead for an early launch."},
   ],
   "faqs": [
     {"q": "When should I winterise?", "a": "Usually in autumn, as the season closes. Early booking is an advantage because hardstanding fills up."},
     {"q": "Do you winterise engines?", "a": "Engine and mechanical winterising is outside our scope. We provide full service for haul-out, hull, covering and storage, and can refer you to trusted engine services."},
     {"q": "Is my boat checked over winter?", "a": "Yes, we keep your boat under supervision during storage and inform you if anything needs attention."},
   ],
 },
},
{
 "slug": "tekne-detailing", "slug_en": "boat-detailing",
 "image": "/assets/images/parallax-2.jpg",
 "deep": {
   "tr": """
<h2>Detailing paketleri</h2>
<p>İhtiyacınıza göre tek seferlik bir tazeleme mi, yoksa sezonluk bir bakım mı? Aşağıdaki tablo tipik paketleri özetliyor.</p>
<table>
<thead><tr><th>Paket</th><th>Kapsam</th><th>Ne zaman</th></tr></thead>
<tbody>
<tr><td>Sezon öncesi</td><td>Yıkama, pasta-polisaj, wax, iç temizlik</td><td>İlkbahar, suya inmeden</td></tr>
<tr><td>Sezon içi</td><td>Dış yıkama, hızlı iç temizlik</td><td>Periyodik</td></tr>
<tr><td>Sezon sonu</td><td>Derin temizlik, koruma, <a href="/blog/teknede-kuf-nem-onleme/">nem/küf</a> önlemi</td><td>Kışlatma ile</td></tr>
</tbody>
</table>
<h2>Neden düzenli detailing?</h2>
<p>Tuz ve UV, ihmal edildiğinde jelkotu ve döşemeyi kalıcı olarak yıpratır. Düzenli detailing, <a href="/blog/gelcoat-yenileme/">komple gelcoat yenilemeyi</a> veya döşeme değişimini yıllarca erteler — yani en ucuz koruma yöntemidir. Detaylar için <a href="/blog/tekne-temizligi-detailing/">detailing yazımıza</a> bakın.</p>
""",
   "en": """
<h2>Detailing packages</h2>
<p>A one-off refresh, or seasonal care? The table below sums up typical packages.</p>
<table>
<thead><tr><th>Package</th><th>Scope</th><th>When</th></tr></thead>
<tbody>
<tr><td>Pre-season</td><td>Wash, compound-polish, wax, interior clean</td><td>Spring, before launch</td></tr>
<tr><td>In-season</td><td>Exterior wash, quick interior clean</td><td>Periodic</td></tr>
<tr><td>End-of-season</td><td>Deep clean, protection, <a href="/en/blog/preventing-mould-damp/">damp/mould</a> measures</td><td>With winterising</td></tr>
</tbody>
</table>
<h2>Why regular detailing?</h2>
<p>Salt and UV, if neglected, permanently wear the gelcoat and upholstery. Regular detailing postpones a full <a href="/en/blog/gelcoat-renewal/">gelcoat renewal</a> or re-upholstery for years — the cheapest form of protection. For detail, see our <a href="/en/blog/boat-cleaning-detailing/">detailing article</a>.</p>
""",
 },
 "tr": {
   "name": "Temizlik & Detailing",
   "short": "İç-dış temizlik, pasta-polisaj ve jelkot koruma ile teknenizi ilk günkü hâline yaklaştırın.",
   "bullets": ["Dış yüzey yıkama & pasta-polisaj", "Jelkot koruma / wax", "İç mekan & döşeme temizliği", "Paslanmaz, cam ve detay bakımı"],
   "hero_title": "Tekne Temizliği ve Detailing",
   "hero_sub": "Tuz ve UV yıpratmadan önce; profesyonel iç-dış temizlik, pasta-polisaj ve koruyucu bakımla teknenizin görünümünü ve değerini koruyoruz.",
   "meta_title": "Tekne Temizliği ve Detailing Hizmeti | Tekne Usta",
   "meta_desc": "Tekne temizliği ve detailing: dış yüzey yıkama, pasta polisaj, jelkot koruma, iç mekan ve döşeme temizliği. İstanbul ve Ege'de sezon öncesi/sonrası detailing paketleri.",
   "body": """
<h2>Temizlik, korumanın ilk adımıdır</h2>
<p>Detailing yalnızca estetik değildir; teknenin yüzeyini, değerini ve ömrünü koruyan en ucuz bakımdır. <strong>Tekne Usta</strong> olarak temizliği bütünsel bakım anlayışının bir parçası olarak ele alıyoruz — yüzeyi sadece parlatmıyor, koruyoruz.</p>
<h2>Neler yapıyoruz?</h2>
<ul>
<li><strong>Dış yüzey:</strong> Tuz, kir ve leke temizliği; <a href="/blog/gelcoat-cizik-sararma-giderme/">pasta-polisaj</a> ile parlaklığın geri kazanılması.</li>
<li><strong>Jelkot koruma:</strong> Temizlik sonrası koruyucu wax/cila ile UV ve oksidasyona karşı kalkan.</li>
<li><strong>İç mekan:</strong> Kabin, döşeme ve yüzey temizliği; <a href="/blog/teknede-kuf-nem-onleme/">küf ve nem</a> önlemi.</li>
<li><strong>Detay:</strong> Paslanmaz, cam ve fikstür bakımı.</li>
</ul>
<h2>Yüzey işini bilen ellerde</h2>
<p>Pasta-polisaj ve koruma, jelkotu koruyacak doğru teknik ve ürünle yapılmalıdır; agresif bir polisaj jelkotu inceltir. Biz yüzeyi <a href="/hizmetler/fiberglas-onarim/">fiberglas onarım</a> deneyimimizle, zarar vermeden ele alırız.</p>
""",
   "tiles": [
     {"h": "Koruma odaklı", "p": "Sadece parlatmıyor; wax ile UV'ye karşı koruyoruz."},
     {"h": "Doğru teknik", "p": "Pasta-polisajı jelkotu inceltmeden yaparız."},
     {"h": "Paket esnekliği", "p": "Sezon öncesi, içi ve sonrası için farklı paketler."},
   ],
   "faqs": [
     {"q": "Pasta-polisaj jelkota zarar verir mi?", "a": "Yanlış yapılırsa evet — agresif polisaj jelkotu inceltir. Biz uygun aşındırıcı ve teknikle, yüzeyi koruyarak yapıyoruz."},
     {"q": "Detailing ne sıklıkla yapılmalı?", "a": "Çoğu tekede sezon öncesi ve sonrası birer detailing idealdir; yoğun kullanımda sezon içi ara temizlikler eklenir."},
     {"q": "İç mekan temizliği de dahil mi?", "a": "Evet. Kabin, döşeme ve yüzey temizliğinin yanı sıra küf/nem önlemlerini de kapsayan paketlerimiz var."},
   ],
 },
 "en": {
   "name": "Cleaning & Detailing",
   "short": "Bring your boat close to day-one with interior-exterior cleaning, compound-polish and gelcoat protection.",
   "bullets": ["Exterior wash & compound-polish", "Gelcoat protection / wax", "Interior & upholstery cleaning", "Stainless, glass & detail care"],
   "hero_title": "Boat Cleaning and Detailing",
   "hero_sub": "Before salt and UV take their toll — professional interior-exterior cleaning, compound-polish and protective care keep your boat's look and value.",
   "meta_title": "Boat Cleaning and Detailing Service | Tekne Usta",
   "meta_desc": "Boat cleaning and detailing: exterior wash, compound-polish, gelcoat protection, interior and upholstery cleaning. Pre/post-season detailing packages in Istanbul and the Aegean.",
   "body": """
<h2>Cleaning is the first step in protection</h2>
<p>Detailing isn't just cosmetic; it's the cheapest care that protects a boat's surface, value and life. At <strong>Tekne Usta</strong> we treat cleaning as part of holistic care — we don't just polish the surface, we protect it.</p>
<h2>What we do</h2>
<ul>
<li><strong>Exterior:</strong> removing salt, dirt and stains; restoring gloss with <a href="/en/blog/gelcoat-scratch-yellowing/">compound-polish</a>.</li>
<li><strong>Gelcoat protection:</strong> a protective wax after cleaning shields against UV and oxidation.</li>
<li><strong>Interior:</strong> cleaning the cabin, upholstery and surfaces; <a href="/en/blog/preventing-mould-damp/">mould and damp</a> measures.</li>
<li><strong>Detail:</strong> stainless, glass and fixture care.</li>
</ul>
<h2>In hands that know surfaces</h2>
<p>Compound-polish and protection must be done with the right technique and products to protect the gelcoat; an aggressive polish thins it. We handle the surface with our <a href="/en/services/fibreglass-repair/">fibreglass repair</a> experience, without harm.</p>
""",
   "tiles": [
     {"h": "Protection-focused", "p": "Not just polishing; we protect against UV with wax."},
     {"h": "The right technique", "p": "We compound-polish without thinning the gelcoat."},
     {"h": "Flexible packages", "p": "Different packages for pre-, in- and post-season."},
   ],
   "faqs": [
     {"q": "Does compound-polish harm the gelcoat?", "a": "Done wrong, yes — an aggressive polish thins the gelcoat. We use the right abrasive and technique, protecting the surface."},
     {"q": "How often should detailing be done?", "a": "For most boats one detailing before and after the season is ideal; heavy use adds mid-season cleans."},
     {"q": "Is interior cleaning included?", "a": "Yes. We have packages covering cabin, upholstery and surface cleaning as well as mould/damp measures."},
   ],
 },
},
{
 "slug": "tente-branda", "slug_en": "marine-canvas",
 "image": "/assets/images/parallax-3.jpg",
 "deep": {
   "tr": """
<h2>Ne üretiyoruz?</h2>
<p>Marine dikişhane işleri, teknenin dış tekstillerini ve döşemesini kapsar. Aşağıdaki tablo başlıca ürünleri özetliyor.</p>
<table>
<thead><tr><th>Ürün</th><th>İşlev</th><th>Not</th></tr></thead>
<tbody>
<tr><td>Bimini</td><td>Kokpit üzeri güneşlik</td><td>Seyir konforunun temeli</td></tr>
<tr><td>Sprayhood</td><td>Yağmur/serpinti koruması</td><td>Kokpit girişini korur</td></tr>
<tr><td>Kaplama brandası</td><td>Kullanılmadığında koruma</td><td>UV ve kirden korur</td></tr>
<tr><td>Kışlama brandası</td><td>Kışın nem/UV koruması</td><td>Havalandırmalı (bkz. <a href="/blog/tekne-ortusu-secimi/">örtü seçimi</a>)</td></tr>
<tr><td>Minder & döşeme</td><td>Kokpit/iç mekan dikişi</td><td>Deniz sınıfı kumaş</td></tr>
</tbody>
</table>
<h2>Kumaş ve dikiş kalitesi</h2>
<p>Deniz koşullarına uygun, UV'ye dayanıklı ve su itici kumaş; <strong>UV dayanımlı iplik</strong> ve paslanmaz fikstürler şarttır. En iyi kumaş bile zayıf dikişle kısa ömürlü olur — dikiş kalitesi belirleyicidir. Detaylar için <a href="/blog/tente-branda-bimini/">tente/branda rehberimize</a> bakın.</p>
""",
   "en": """
<h2>What we make</h2>
<p>Marine canvas work covers a boat's exterior textiles and upholstery. The table below sums up the main products.</p>
<table>
<thead><tr><th>Product</th><th>Function</th><th>Note</th></tr></thead>
<tbody>
<tr><td>Bimini</td><td>Cockpit sunshade</td><td>The basis of cruising comfort</td></tr>
<tr><td>Sprayhood</td><td>Rain/spray protection</td><td>Shields the cockpit entry</td></tr>
<tr><td>Storage cover</td><td>Protection when not in use</td><td>Guards against UV and dirt</td></tr>
<tr><td>Winter cover</td><td>Damp/UV protection in winter</td><td>Ventilated (see <a href="/en/blog/boat-cover-selection/">cover selection</a>)</td></tr>
<tr><td>Cushions & upholstery</td><td>Cockpit/interior sewing</td><td>Marine-grade fabric</td></tr>
</tbody>
</table>
<h2>Fabric and stitch quality</h2>
<p>Fabric suited to marine conditions — UV-resistant and water-repellent — plus <strong>UV-resistant thread</strong> and stainless fixtures are essential. Even the best fabric is short-lived with weak stitching. For detail, see our <a href="/en/blog/marine-canvas-covers/">canvas guide</a>.</p>
""",
 },
 "tr": {
   "name": "Tente & Branda",
   "short": "Bimini, sprayhood, kaplama ve kışlama brandaları; marine dikişhane ve döşeme işleri.",
   "bullets": ["Bimini & sprayhood", "Kaplama & kışlama brandası", "Minder & döşeme dikişi", "Onarım & yenileme"],
   "hero_title": "Tente, Branda ve Marine Dikişhane",
   "hero_sub": "Güneş, yağmur ve UV'ye karşı; teknenize özel ölçü bimini, sprayhood, kaplama ve kışlama brandaları ile döşeme dikişi.",
   "meta_title": "Tekne Tente, Branda ve Bimini | Marine Dikişhane — Tekne Usta",
   "meta_desc": "Tekne tente, branda ve bimini: özel ölçü bimini, sprayhood, kaplama ve kışlama brandası, minder-döşeme dikişi ve onarım. Deniz sınıfı kumaş, UV dayanımlı dikiş. İstanbul ve Ege.",
   "body": """
<h2>Teknenizin dış tekstili, hem koruma hem konfor</h2>
<p>Tente ve brandalar; tekneyi güneş, yağmur ve UV'den korur, aynı zamanda seyir konforunu belirler. İyi seçilmiş ve <strong>teknenize özel ölçü</strong> dikilmiş bir sistem, hem sizi hem teknenizi yıllarca korur. Marine dikişhane işlerini deniz sınıfı malzeme ve titiz işçilikle yapıyoruz.</p>
<h2>Neler yapıyoruz?</h2>
<ul>
<li><strong>Bimini & sprayhood</strong> — kokpit güneşliği ve yağmur koruması</li>
<li><strong>Kaplama & kışlama brandaları</strong> — kullanım dışı ve kış koruması</li>
<li><strong>Minder & döşeme dikişi</strong> — kokpit ve iç mekan (bkz. <a href="/hizmetler/ic-mekan-yenileme/">iç mekan yenileme</a>)</li>
<li><strong>Onarım & yenileme</strong> — yıpranmış tente/branda tamiri, fermuar ve dikiş yenileme</li>
</ul>
<h2>Neden özel ölçü?</h2>
<p>Hazır ölçü tente/branda nadiren tam oturur; yanlış gerginlik hem görünümü bozar hem üzerinde su biriktirir. Teknenin hattına özel kalıp, doğru gerginlik ve su akışı; sonucun hem estetiğini hem ömrünü belirler.</p>
""",
   "tiles": [
     {"h": "Deniz sınıfı kumaş", "p": "UV, tuz ve suya dayanıklı, solmayan kumaş."},
     {"h": "UV dayanımlı dikiş", "p": "İplik ve fikstürler dikişin ömrünü belirler."},
     {"h": "Özel ölçü", "p": "Teknenizin hattına birebir kalıp ve gerginlik."},
   ],
   "faqs": [
     {"q": "Mevcut tentemi onarır mısınız yoksa yeni mi gerekir?", "a": "Kumaş sağlamsa dikiş, fermuar ve bağlantı onarımı yapılabilir. Kumaş UV'den yıprandıysa yenileme daha mantıklıdır; keşifte birlikte karar veririz."},
     {"q": "Kışlama brandası ile normal branda farkı ne?", "a": "Kışlama brandası nem hapsetmeyen, havalandırmalı olmalı; aksi halde küf yapar. Kullanım brandası daha çok UV/kir korumasına odaklanır."},
     {"q": "Hangi kumaşı kullanıyorsunuz?", "a": "Deniz koşullarına uygun, UV ve su dirençli akrilik/deniz sınıfı kumaşlar ve UV dayanımlı iplik kullanıyoruz."},
   ],
 },
 "en": {
   "name": "Canvas & Covers",
   "short": "Biminis, sprayhoods, storage and winter covers; marine canvas and upholstery work.",
   "bullets": ["Bimini & sprayhood", "Storage & winter covers", "Cushion & upholstery sewing", "Repair & renewal"],
   "hero_title": "Canvas, Covers and Marine Upholstery",
   "hero_sub": "Against sun, rain and UV — made-to-measure biminis, sprayhoods, storage and winter covers plus upholstery sewing for your boat.",
   "meta_title": "Boat Canvas, Covers and Bimini | Marine Upholstery — Tekne Usta",
   "meta_desc": "Boat canvas, covers and bimini: made-to-measure bimini, sprayhood, storage and winter cover, cushion-upholstery sewing and repair. Marine-grade fabric, UV-resistant stitching.",
   "body": """
<h2>Your boat's exterior textiles — protection and comfort</h2>
<p>Canvas and covers protect the boat from sun, rain and UV, and also shape cruising comfort. A well-chosen, <strong>made-to-measure</strong> system protects both you and your boat for years. We do marine canvas work in marine-grade materials with meticulous craftsmanship.</p>
<h2>What we make</h2>
<ul>
<li><strong>Bimini & sprayhood</strong> — cockpit sunshade and rain protection</li>
<li><strong>Storage & winter covers</strong> — off-season and winter protection</li>
<li><strong>Cushion & upholstery sewing</strong> — cockpit and interior (see <a href="/en/services/interior-refit/">interior refit</a>)</li>
<li><strong>Repair & renewal</strong> — worn canvas repair, zip and stitch renewal</li>
</ul>
<h2>Why made-to-measure?</h2>
<p>Off-the-shelf canvas rarely fits exactly; wrong tension spoils the look and pools water. A pattern made to the boat's lines, correct tension and water run-off determine both the look and the life.</p>
""",
   "tiles": [
     {"h": "Marine-grade fabric", "p": "UV-, salt- and water-resistant, non-fading fabric."},
     {"h": "UV-resistant stitching", "p": "Thread and fixtures determine the seam's life."},
     {"h": "Made to measure", "p": "An exact pattern and tension for your boat's lines."},
   ],
   "faqs": [
     {"q": "Do you repair my existing cover or is a new one needed?", "a": "If the fabric is sound, stitching, zips and fittings can be repaired. If the fabric is UV-worn, renewal makes more sense; we decide together at the survey."},
     {"q": "What's the difference between a winter cover and a normal cover?", "a": "A winter cover must be ventilated and not trap damp; otherwise it breeds mould. A use cover focuses more on UV/dirt protection."},
     {"q": "Which fabric do you use?", "a": "Marine-grade acrylic/fabrics resistant to UV and water, plus UV-resistant thread, suited to marine conditions."},
   ],
 },
},
]

# ------------------------------------------------------------------ Regions
REGIONS = [
{
 "slug": "istanbul", "image": "/assets/images/parallax-1.jpg",
 "tr": {
   "name": "İstanbul",
   "short": "Tuzla, Pendik, Ataköy ve Kalamış marinalarında yerinde keşif ve servis.",
   "hero_title": "İstanbul'da Tekne Tamiri, Bakımı ve Renovasyonu",
   "hero_sub": "Tuzla'dan Ataköy'e, Kalamış'tan Pendik'e — İstanbul'un tüm marinalarında fiberglas onarımı, boya, ahşap renovasyon ve kışlatma hizmeti.",
   "meta_title": "İstanbul Tekne Tamiri, Bakımı ve Renovasyonu | Tekne Usta",
   "meta_desc": "İstanbul'da tekne tamiri, fiberglas onarımı, osmoz tedavisi, tekne boyama (antifouling), ahşap renovasyon ve kışlatma. Tuzla, Pendik, Ataköy, Kalamış marinalarında ücretsiz keşif.",
   "body": """
<h2>İstanbul'un her marinasında yanınızdayız</h2>
<p>İstanbul, Türkiye'nin en yoğun tekne trafiğine sahip şehri. <strong>Tekne Usta</strong> olarak <strong>Tuzla, Pendik Marina, Viaport Marina, Ataköy Marina, Kalamış ve West Istanbul Marina</strong> başta olmak üzere şehrin iki yakasındaki marinalarda yerinde keşif ve servis sunuyoruz. Teknenizi bulunduğu yerde inceler, gerekirse çekek alanına alarak çalışırız.</p>
<h2>İstanbul'da verdiğimiz hizmetler</h2>
<ul>
<li><a href="/hizmetler/fiberglas-onarim/">Fiberglas onarım ve osmoz tedavisi</a></li>
<li><a href="/hizmetler/tekne-boyama-antifouling/">Tekne boyama ve antifouling</a></li>
<li><a href="/hizmetler/ahsap-tekne-renovasyonu/">Ahşap tekne renovasyonu</a></li>
<li><a href="/hizmetler/teak-guverte-doseme/">Teak güverte döşeme</a></li>
<li><a href="/hizmetler/tekne-kislatma/">Tekne kışlatma ve kış muhafazası</a></li>
</ul>
<h2>Neden İstanbul'da Tekne Usta?</h2>
<p>Marina içi lojistik, çekek randevusu ve sezon yoğunluğu İstanbul'da işi zorlaştırır. Biz süreci sizin adınıza yönetir, <strong>ücretsiz keşif ve 48 saatte yazılı teklif</strong> ile net bir plan sunarız. Aracı komisyonları olmadan, doğrudan ustayla çalışırsınız.</p>
""",
 },
 "en": {
   "name": "Istanbul",
   "short": "On-site survey and service at Tuzla, Pendik, Ataköy and Kalamış marinas.",
   "hero_title": "Boat Repair, Maintenance & Refit in Istanbul",
   "hero_sub": "From Tuzla to Ataköy, Kalamış to Pendik — fibreglass repair, painting, wooden refit and winterising across all of Istanbul's marinas.",
   "meta_title": "Istanbul Boat Repair, Maintenance & Refit | Tekne Usta",
   "meta_desc": "Boat repair, fibreglass repair, osmosis treatment, boat painting (antifouling), wooden refit and winterising in Istanbul. Free survey at Tuzla, Pendik, Ataköy and Kalamış marinas.",
   "body": """
<h2>At your side in every Istanbul marina</h2>
<p>Istanbul has Turkey's busiest boating traffic. <strong>Tekne Usta</strong> offers on-site survey and service at marinas on both sides of the city, including <strong>Tuzla, Pendik Marina, Viaport Marina, Ataköy Marina, Kalamış and West Istanbul Marina</strong>. We inspect your boat where it lies and, if needed, work on the hardstanding.</p>
<h2>Services we provide in Istanbul</h2>
<ul>
<li><a href="/en/services/fibreglass-repair/">Fibreglass repair & osmosis treatment</a></li>
<li><a href="/en/services/boat-painting-antifouling/">Boat painting & antifouling</a></li>
<li><a href="/en/services/wooden-boat-refit/">Wooden boat refit</a></li>
<li><a href="/en/services/teak-deck/">Teak decking</a></li>
<li><a href="/en/services/winterising-storage/">Winterising & winter storage</a></li>
</ul>
<h2>Why Tekne Usta in Istanbul?</h2>
<p>Marina logistics, haul-out slots and peak-season demand make work in Istanbul harder. We manage the process for you and give a clear plan with a <strong>free survey and a written quote in 48 hours</strong>. You work directly with the craftsman — no broker commissions.</p>
""",
 },
},
{
 "slug": "bodrum", "image": "/assets/images/parallax-2.jpg",
 "tr": {
   "name": "Bodrum",
   "short": "Yalıkavak, Turgutreis ve Milta Bodrum Marina çevresinde tekne servisi.",
   "hero_title": "Bodrum'da Tekne Tamiri, Bakımı ve Renovasyonu",
   "hero_sub": "Yalıkavak Marina'dan Turgutreis'e — Bodrum yarımadasında fiberglas onarımı, boya, ahşap renovasyon ve teak döşeme.",
   "meta_title": "Bodrum Tekne Tamiri, Bakımı ve Renovasyonu | Tekne Usta",
   "meta_desc": "Bodrum'da tekne tamiri, fiberglas onarımı, osmoz tedavisi, tekne boyama ve ahşap renovasyon. Yalıkavak, Turgutreis ve Milta Bodrum Marina çevresinde hizmet.",
   "body": """
<h2>Bodrum yarımadasında usta eli</h2>
<p>Bodrum, Ege'nin en canlı yat merkezlerinden biri. <strong>Yalıkavak Marina, Milta Bodrum Marina ve Turgutreis</strong> çevresindeki tekneler için fiberglas onarımı, boya, ahşap renovasyon ve teak hizmetleri sunuyoruz. Yoğun sezon öncesi bakımlarınızı zamanında planlıyoruz.</p>
<h2>Bodrum'da verdiğimiz hizmetler</h2>
<ul>
<li><a href="/hizmetler/fiberglas-onarim/">Fiberglas onarım ve osmoz tedavisi</a></li>
<li><a href="/hizmetler/tekne-boyama-antifouling/">Tekne boyama ve antifouling</a></li>
<li><a href="/hizmetler/ahsap-tekne-renovasyonu/">Ahşap tekne renovasyonu</a></li>
<li><a href="/hizmetler/teak-guverte-doseme/">Teak güverte döşeme</a></li>
</ul>
<p>Bölgede güvenilir, şeffaf fiyatlı bir usta arıyorsanız <strong>ücretsiz keşif</strong> için bize yazın.</p>
""",
 },
 "en": {
   "name": "Bodrum",
   "short": "Boat service around Yalıkavak, Turgutreis and Milta Bodrum Marina.",
   "hero_title": "Boat Repair, Maintenance & Refit in Bodrum",
   "hero_sub": "From Yalıkavak Marina to Turgutreis — fibreglass repair, painting, wooden refit and teak decking across the Bodrum peninsula.",
   "meta_title": "Bodrum Boat Repair, Maintenance & Refit | Tekne Usta",
   "meta_desc": "Boat repair, fibreglass repair, osmosis treatment, painting and wooden refit in Bodrum. Service around Yalıkavak, Turgutreis and Milta Bodrum Marina.",
   "body": """
<h2>A craftsman's hand on the Bodrum peninsula</h2>
<p>Bodrum is one of the Aegean's liveliest yachting hubs. We serve boats around <strong>Yalıkavak Marina, Milta Bodrum Marina and Turgutreis</strong> with fibreglass repair, painting, wooden refit and teak work. We plan your pre-season maintenance in good time.</p>
<h2>Services we provide in Bodrum</h2>
<ul>
<li><a href="/en/services/fibreglass-repair/">Fibreglass repair & osmosis treatment</a></li>
<li><a href="/en/services/boat-painting-antifouling/">Boat painting & antifouling</a></li>
<li><a href="/en/services/wooden-boat-refit/">Wooden boat refit</a></li>
<li><a href="/en/services/teak-deck/">Teak decking</a></li>
</ul>
<p>If you're looking for a trusted, transparently priced craftsman in the area, message us for a <strong>free survey</strong>.</p>
""",
 },
},
{
 "slug": "gocek", "image": "/assets/images/parallax-3.jpg",
 "tr": {
   "name": "Göcek",
   "short": "D-Marin, Club Marina ve Marinturk çevresinde yat bakım ve refit.",
   "hero_title": "Göcek'te Tekne Tamiri, Bakımı ve Renovasyonu",
   "hero_sub": "Göcek'in korunaklı koylarındaki yatlar için fiberglas onarımı, boya, ahşap renovasyon ve teak döşeme hizmeti.",
   "meta_title": "Göcek Tekne Tamiri, Bakımı ve Renovasyonu | Tekne Usta",
   "meta_desc": "Göcek'te tekne tamiri, fiberglas onarımı, osmoz tedavisi, tekne boyama ve ahşap renovasyon. D-Marin Göcek, Club Marina ve Marinturk çevresinde hizmet.",
   "body": """
<h2>Göcek'in yat cennetinde güvenilir servis</h2>
<p>Göcek, Türkiye'nin en yoğun yat üssülerinden biri; <strong>D-Marin Göcek, Club Marina ve Marinturk</strong> çevresinde çok sayıda yat kışlar ve bakım görür. Bu tekneler için fiberglas onarım, boya, ahşap renovasyon ve teak hizmetlerimizle yanınızdayız.</p>
<h2>Göcek'te verdiğimiz hizmetler</h2>
<ul>
<li><a href="/hizmetler/fiberglas-onarim/">Fiberglas onarım ve osmoz tedavisi</a></li>
<li><a href="/hizmetler/tekne-boyama-antifouling/">Tekne boyama ve antifouling</a></li>
<li><a href="/hizmetler/ahsap-tekne-renovasyonu/">Ahşap tekne renovasyonu</a></li>
<li><a href="/hizmetler/teak-guverte-doseme/">Teak güverte döşeme</a></li>
</ul>
""",
 },
 "en": {
   "name": "Göcek",
   "short": "Yacht maintenance and refit around D-Marin, Club Marina and Marinturk.",
   "hero_title": "Boat Repair, Maintenance & Refit in Göcek",
   "hero_sub": "For yachts in Göcek's sheltered bays — fibreglass repair, painting, wooden refit and teak decking.",
   "meta_title": "Göcek Boat Repair, Maintenance & Refit | Tekne Usta",
   "meta_desc": "Boat repair, fibreglass repair, osmosis treatment, painting and wooden refit in Göcek. Service around D-Marin Göcek, Club Marina and Marinturk.",
   "body": """
<h2>Trusted service in Göcek's yachting haven</h2>
<p>Göcek is one of Turkey's busiest yachting bases; many yachts winter and are maintained around <strong>D-Marin Göcek, Club Marina and Marinturk</strong>. We support these boats with fibreglass repair, painting, wooden refit and teak work.</p>
<h2>Services we provide in Göcek</h2>
<ul>
<li><a href="/en/services/fibreglass-repair/">Fibreglass repair & osmosis treatment</a></li>
<li><a href="/en/services/boat-painting-antifouling/">Boat painting & antifouling</a></li>
<li><a href="/en/services/wooden-boat-refit/">Wooden boat refit</a></li>
<li><a href="/en/services/teak-deck/">Teak decking</a></li>
</ul>
""",
 },
},
{
 "slug": "marmaris", "image": "/assets/images/parallax-1.jpg",
 "tr": {
   "name": "Marmaris",
   "short": "Netsel Marina ve Yat Marin çevresinde tekne tamiri ve bakımı.",
   "hero_title": "Marmaris'te Tekne Tamiri, Bakımı ve Renovasyonu",
   "hero_sub": "Netsel Marina ve Yat Marin çevresindeki tekneler için fiberglas onarımı, boya, ahşap renovasyon ve kışlatma.",
   "meta_title": "Marmaris Tekne Tamiri, Bakımı ve Renovasyonu | Tekne Usta",
   "meta_desc": "Marmaris'te tekne tamiri, fiberglas onarımı, osmoz tedavisi, boya ve ahşap renovasyon. Netsel Marina ve Yat Marin çevresinde ücretsiz keşif ve şeffaf teklif.",
   "body": """
<h2>Marmaris'te usta işçiliği</h2>
<p>Marmaris, hem yerli hem yabancı tekne sahipleri için önemli bir üs. <strong>Netsel Marmaris Marina ve Yat Marin</strong> çevresindeki tekneler için fiberglas onarım, boya, ahşap renovasyon ve kışlatma hizmeti veriyoruz.</p>
<h2>Marmaris'te verdiğimiz hizmetler</h2>
<ul>
<li><a href="/hizmetler/fiberglas-onarim/">Fiberglas onarım ve osmoz tedavisi</a></li>
<li><a href="/hizmetler/tekne-boyama-antifouling/">Tekne boyama ve antifouling</a></li>
<li><a href="/hizmetler/ahsap-tekne-renovasyonu/">Ahşap tekne renovasyonu</a></li>
<li><a href="/hizmetler/tekne-kislatma/">Tekne kışlatma</a></li>
</ul>
""",
 },
 "en": {
   "name": "Marmaris",
   "short": "Boat repair and maintenance around Netsel Marina and Yat Marin.",
   "hero_title": "Boat Repair, Maintenance & Refit in Marmaris",
   "hero_sub": "For boats around Netsel Marina and Yat Marin — fibreglass repair, painting, wooden refit and winterising.",
   "meta_title": "Marmaris Boat Repair, Maintenance & Refit | Tekne Usta",
   "meta_desc": "Boat repair, fibreglass repair, osmosis treatment, painting and wooden refit in Marmaris. Free survey and transparent quote around Netsel Marina and Yat Marin.",
   "body": """
<h2>Craftsmanship in Marmaris</h2>
<p>Marmaris is an important base for both local and foreign boat owners. We serve boats around <strong>Netsel Marmaris Marina and Yat Marin</strong> with fibreglass repair, painting, wooden refit and winterising.</p>
<h2>Services we provide in Marmaris</h2>
<ul>
<li><a href="/en/services/fibreglass-repair/">Fibreglass repair & osmosis treatment</a></li>
<li><a href="/en/services/boat-painting-antifouling/">Boat painting & antifouling</a></li>
<li><a href="/en/services/wooden-boat-refit/">Wooden boat refit</a></li>
<li><a href="/en/services/winterising-storage/">Winterising & storage</a></li>
</ul>
""",
 },
},
{
 "slug": "fethiye", "image": "/assets/images/parallax-2.jpg",
 "tr": {
   "name": "Fethiye",
   "short": "Ece Marina ve Fethiye körfezinde tekne servisi ve refit.",
   "hero_title": "Fethiye'de Tekne Tamiri, Bakımı ve Renovasyonu",
   "hero_sub": "Ece Saray Marina ve Fethiye körfezindeki tekneler için fiberglas onarımı, boya, ahşap renovasyon ve teak döşeme.",
   "meta_title": "Fethiye Tekne Tamiri, Bakımı ve Renovasyonu | Tekne Usta",
   "meta_desc": "Fethiye'de tekne tamiri, fiberglas onarımı, osmoz tedavisi, boya ve ahşap renovasyon. Ece Marina ve Fethiye körfezi çevresinde ücretsiz keşif.",
   "body": """
<h2>Fethiye körfezinde güvenilir usta</h2>
<p>Fethiye, Göcek'e komşuluğu ve korunaklı körfeziyle önemli bir tekne bölgesi. <strong>Ece Saray Marina</strong> ve çevresindeki tekneler için fiberglas onarım, boya, ahşap renovasyon ve teak hizmetleri sunuyoruz.</p>
<h2>Fethiye'de verdiğimiz hizmetler</h2>
<ul>
<li><a href="/hizmetler/fiberglas-onarim/">Fiberglas onarım ve osmoz tedavisi</a></li>
<li><a href="/hizmetler/tekne-boyama-antifouling/">Tekne boyama ve antifouling</a></li>
<li><a href="/hizmetler/ahsap-tekne-renovasyonu/">Ahşap tekne renovasyonu</a></li>
<li><a href="/hizmetler/teak-guverte-doseme/">Teak güverte döşeme</a></li>
</ul>
""",
 },
 "en": {
   "name": "Fethiye",
   "short": "Boat service and refit around Ece Marina and Fethiye bay.",
   "hero_title": "Boat Repair, Maintenance & Refit in Fethiye",
   "hero_sub": "For boats around Ece Saray Marina and Fethiye bay — fibreglass repair, painting, wooden refit and teak decking.",
   "meta_title": "Fethiye Boat Repair, Maintenance & Refit | Tekne Usta",
   "meta_desc": "Boat repair, fibreglass repair, osmosis treatment, painting and wooden refit in Fethiye. Free survey around Ece Marina and Fethiye bay.",
   "body": """
<h2>A trusted craftsman in Fethiye bay</h2>
<p>Fethiye, neighbouring Göcek with its sheltered bay, is an important boating area. We serve boats around <strong>Ece Saray Marina</strong> with fibreglass repair, painting, wooden refit and teak work.</p>
<h2>Services we provide in Fethiye</h2>
<ul>
<li><a href="/en/services/fibreglass-repair/">Fibreglass repair & osmosis treatment</a></li>
<li><a href="/en/services/boat-painting-antifouling/">Boat painting & antifouling</a></li>
<li><a href="/en/services/wooden-boat-refit/">Wooden boat refit</a></li>
<li><a href="/en/services/teak-deck/">Teak decking</a></li>
</ul>
""",
 },
},
{
 "slug": "tuzla", "image": "/assets/images/parallax-3.jpg",
 "tr": {
   "name": "Tuzla",
   "short": "Tuzla tersaneler bölgesi ve marina çevresinde çekek, boya ve onarım.",
   "hero_title": "Tuzla'da Tekne Tamiri, Boya ve Çekek Hizmetleri",
   "hero_sub": "Türkiye'nin en yoğun tersaneler bölgesinde; fiberglas onarım, antifouling, boya ve ahşap işleri için usta eli.",
   "meta_title": "Tuzla Tekne Tamiri, Boya ve Çekek | Tekne Usta",
   "meta_desc": "Tuzla'da tekne tamiri, fiberglas onarımı, osmoz tedavisi, antifouling ve boya. Tuzla tersaneler bölgesi ve Viaport Marina çevresinde çekek imkânıyla hizmet.",
   "body": """
<h2>Tuzla: işin kalbinde çalışıyoruz</h2>
<p>Tuzla, İstanbul'un — ve Türkiye'nin — en yoğun tekne ve tersane bölgesidir. Çekek alanları, halat ve vinç imkânı bu bölgede işi kolaylaştırır; kapsamlı karina, boya ve fiberglas işleri için ideal bir konumdur. <strong>Tekne Usta</strong> olarak Tuzla ve <strong>Viaport Marina</strong> çevresindeki tekneler için karaya çekme gerektiren işlerde de yanınızdayız.</p>
<h2>Tuzla'da öne çıkan işler</h2>
<ul>
<li><a href="/hizmetler/fiberglas-onarim/">Fiberglas onarım ve osmoz tedavisi</a> — kurutma gerektiren kapsamlı işler için uygun çekek</li>
<li><a href="/hizmetler/tekne-boyama-antifouling/">Antifouling ve dış cephe boyama</a></li>
<li><a href="/hizmetler/ahsap-tekne-renovasyonu/">Ahşap tekne renovasyonu</a></li>
<li><a href="/hizmetler/tekne-kislatma/">Kışlatma ve kış muhafazası</a></li>
</ul>
<p>Tuzla'da şeffaf fiyatlı, doğrudan ustayla çalışmak isterseniz ücretsiz keşif için bize yazın.</p>
""",
 },
 "en": {
   "name": "Tuzla",
   "short": "Haul-out, painting and repair around the Tuzla shipyard zone and marina.",
   "hero_title": "Boat Repair, Painting & Haul-out in Tuzla",
   "hero_sub": "In Turkey's busiest shipyard district — a craftsman's hand for fibreglass repair, antifouling, painting and woodwork.",
   "meta_title": "Tuzla Boat Repair, Painting & Haul-out | Tekne Usta",
   "meta_desc": "Boat repair, fibreglass repair, osmosis treatment, antifouling and painting in Tuzla. Service with haul-out around the Tuzla shipyard zone and Viaport Marina.",
   "body": """
<h2>Tuzla: working at the heart of the industry</h2>
<p>Tuzla is Istanbul's — and Turkey's — busiest boat and shipyard district. Hardstanding, slings and cranes make work here easier; it's an ideal location for extensive hull, paint and fibreglass jobs. <strong>Tekne Usta</strong> supports boats around Tuzla and <strong>Viaport Marina</strong>, including work that requires hauling out.</p>
<h2>Notable work in Tuzla</h2>
<ul>
<li><a href="/en/services/fibreglass-repair/">Fibreglass repair & osmosis treatment</a> — hardstanding suited to jobs that need drying</li>
<li><a href="/en/services/boat-painting-antifouling/">Antifouling & topside painting</a></li>
<li><a href="/en/services/wooden-boat-refit/">Wooden boat refit</a></li>
<li><a href="/en/services/winterising-storage/">Winterising & storage</a></li>
</ul>
<p>To work directly with the craftsman at transparent prices in Tuzla, message us for a free survey.</p>
""",
 },
},
{
 "slug": "cesme", "image": "/assets/images/parallax-1.jpg",
 "tr": {
   "name": "Çeşme",
   "short": "Çeşme Marina ve Alaçatı çevresinde tekne bakım ve onarımı.",
   "hero_title": "Çeşme'de Tekne Tamiri, Bakımı ve Renovasyonu",
   "hero_sub": "Çeşme Marina, Ilıca ve Alaçatı çevresindeki tekneler için fiberglas onarım, boya, ahşap renovasyon ve teak.",
   "meta_title": "Çeşme Tekne Tamiri, Bakımı ve Renovasyonu | Tekne Usta",
   "meta_desc": "Çeşme'de tekne tamiri, fiberglas onarımı, osmoz tedavisi, antifouling ve ahşap renovasyon. Çeşme Marina ve Alaçatı çevresinde ücretsiz keşif ve şeffaf teklif.",
   "body": """
<h2>Çeşme'nin rüzgârıyla yıpranan teknelere</h2>
<p>Çeşme ve Alaçatı, güçlü rüzgârı ve yoğun yaz sezonuyla teknelere hızlı bir yük bindirir; boya, karina ve donanım daha çabuk yıpranır. <strong>Çeşme Marina</strong> ve çevresindeki tekneler için fiberglas onarım, boya/antifouling, ahşap renovasyon ve teak hizmetleriyle sezonu güçlü açmanıza yardımcı oluyoruz.</p>
<h2>Çeşme'de verdiğimiz hizmetler</h2>
<ul>
<li><a href="/hizmetler/fiberglas-onarim/">Fiberglas onarım ve osmoz tedavisi</a></li>
<li><a href="/hizmetler/tekne-boyama-antifouling/">Tekne boyama ve antifouling</a></li>
<li><a href="/hizmetler/ahsap-tekne-renovasyonu/">Ahşap tekne renovasyonu</a></li>
<li><a href="/hizmetler/teak-guverte-doseme/">Teak güverte döşeme</a></li>
</ul>
""",
 },
 "en": {
   "name": "Çeşme",
   "short": "Boat maintenance and repair around Çeşme Marina and Alaçatı.",
   "hero_title": "Boat Repair, Maintenance & Refit in Çeşme",
   "hero_sub": "For boats around Çeşme Marina, Ilıca and Alaçatı — fibreglass repair, painting, wooden refit and teak.",
   "meta_title": "Çeşme Boat Repair, Maintenance & Refit | Tekne Usta",
   "meta_desc": "Boat repair, fibreglass repair, osmosis treatment, antifouling and wooden refit in Çeşme. Free survey and transparent quote around Çeşme Marina and Alaçatı.",
   "body": """
<h2>For boats worn by the Çeşme wind</h2>
<p>Çeşme and Alaçatı, with their strong wind and busy summer season, put boats under quick strain; paint, hull and rigging wear faster. For boats around <strong>Çeşme Marina</strong> we help you open the season strong with fibreglass repair, painting/antifouling, wooden refit and teak work.</p>
<h2>Services we provide in Çeşme</h2>
<ul>
<li><a href="/en/services/fibreglass-repair/">Fibreglass repair & osmosis treatment</a></li>
<li><a href="/en/services/boat-painting-antifouling/">Boat painting & antifouling</a></li>
<li><a href="/en/services/wooden-boat-refit/">Wooden boat refit</a></li>
<li><a href="/en/services/teak-deck/">Teak decking</a></li>
</ul>
""",
 },
},
{
 "slug": "yalikavak", "image": "/assets/images/parallax-2.jpg",
 "tr": {
   "name": "Yalıkavak",
   "short": "Yalıkavak Marina çevresinde yat bakım, refit ve teak işleri.",
   "hero_title": "Yalıkavak'ta Yat Bakımı, Refit ve Teak Hizmetleri",
   "hero_sub": "Bodrum'un premium yat üssünde; fiberglas, boya, teak ve iç mekan işlerinde detaya önem veren usta işçiliği.",
   "meta_title": "Yalıkavak Yat Bakımı, Refit ve Teak | Tekne Usta",
   "meta_desc": "Yalıkavak'ta yat bakımı, fiberglas onarımı, boya, teak güverte döşeme ve iç mekan yenileme. Yalıkavak Marina çevresinde titiz, premium işçilik.",
   "body": """
<h2>Yalıkavak'ın standardına uygun işçilik</h2>
<p>Yalıkavak, Bodrum'un en prestijli yat üslerinden biri; <strong>Yalıkavak Marina</strong> çevresinde bakım gören tekneler genelde yüksek beklentili yat sahiplerine aittir. Bu bölgede detay ve bitiş kalitesi öne çıkar — teak geçişleri, boya parlaklığı ve iç mekan işçiliği fark yaratır. Biz de bu standarda göre çalışırız.</p>
<h2>Yalıkavak'ta öne çıkan işler</h2>
<ul>
<li><a href="/hizmetler/teak-guverte-doseme/">Teak güverte döşeme ve yenileme</a></li>
<li><a href="/hizmetler/tekne-boyama-antifouling/">Boya ve antifouling</a></li>
<li><a href="/hizmetler/fiberglas-onarim/">Fiberglas onarım ve gelcoat</a></li>
<li><a href="/hizmetler/ic-mekan-yenileme/">İç mekan yenileme</a></li>
</ul>
""",
 },
 "en": {
   "name": "Yalıkavak",
   "short": "Yacht maintenance, refit and teak work around Yalıkavak Marina.",
   "hero_title": "Yacht Maintenance, Refit & Teak in Yalıkavak",
   "hero_sub": "At Bodrum's premium yacht base — detail-focused craftsmanship in fibreglass, paint, teak and interior work.",
   "meta_title": "Yalıkavak Yacht Maintenance, Refit & Teak | Tekne Usta",
   "meta_desc": "Yacht maintenance, fibreglass repair, painting, teak decking and interior refit in Yalıkavak. Meticulous, premium workmanship around Yalıkavak Marina.",
   "body": """
<h2>Workmanship to match Yalıkavak's standard</h2>
<p>Yalıkavak is one of Bodrum's most prestigious yacht bases; boats maintained around <strong>Yalıkavak Marina</strong> usually belong to owners with high expectations. Here, detail and finish quality stand out — teak transitions, paint gloss and interior work make the difference. We work to that standard.</p>
<h2>Notable work in Yalıkavak</h2>
<ul>
<li><a href="/en/services/teak-deck/">Teak decking and renewal</a></li>
<li><a href="/en/services/boat-painting-antifouling/">Painting & antifouling</a></li>
<li><a href="/en/services/fibreglass-repair/">Fibreglass repair & gelcoat</a></li>
<li><a href="/en/services/interior-refit/">Interior refit</a></li>
</ul>
""",
 },
},
{
 "slug": "pendik", "image": "/assets/images/parallax-3.jpg",
 "tr": {
   "name": "Pendik",
   "short": "Pendik Marina ve çevresinde tekne tamiri, boya ve bakım.",
   "hero_title": "Pendik'te Tekne Tamiri, Bakımı ve Renovasyonu",
   "hero_sub": "Pendik Marina çevresindeki tekneler için fiberglas onarımı, antifouling, ahşap renovasyon ve kışlatma.",
   "meta_title": "Pendik Tekne Tamiri, Bakımı ve Renovasyonu | Tekne Usta",
   "meta_desc": "Pendik'te tekne tamiri, fiberglas onarımı, osmoz tedavisi, antifouling ve ahşap renovasyon. Pendik Marina çevresinde ücretsiz keşif ve şeffaf teklif.",
   "body": """
<h2>Pendik ve çevresinde usta eli</h2>
<p>İstanbul'un Anadolu yakasında, <strong>Pendik Marina</strong> çevresindeki tekneler için fiberglas onarım, boya, ahşap renovasyon ve kışlatma hizmeti veriyoruz. Tuzla'ya yakınlığıyla çekek gerektiren işlerde de esneğiz.</p>
<h2>Pendik'te verdiğimiz hizmetler</h2>
<ul>
<li><a href="/hizmetler/fiberglas-onarim/">Fiberglas onarım ve osmoz tedavisi</a></li>
<li><a href="/hizmetler/tekne-boyama-antifouling/">Tekne boyama ve antifouling</a></li>
<li><a href="/hizmetler/ahsap-tekne-renovasyonu/">Ahşap tekne renovasyonu</a></li>
<li><a href="/hizmetler/tekne-kislatma/">Tekne kışlatma</a></li>
</ul>
""",
 },
 "en": {
   "name": "Pendik",
   "short": "Boat repair, painting and maintenance around Pendik Marina.",
   "hero_title": "Boat Repair, Maintenance & Refit in Pendik",
   "hero_sub": "For boats around Pendik Marina — fibreglass repair, antifouling, wooden refit and winterising.",
   "meta_title": "Pendik Boat Repair, Maintenance & Refit | Tekne Usta",
   "meta_desc": "Boat repair, fibreglass repair, osmosis treatment, antifouling and wooden refit in Pendik. Free survey and transparent quote around Pendik Marina.",
   "body": """
<h2>A craftsman's hand in and around Pendik</h2>
<p>On Istanbul's Anatolian side, we serve boats around <strong>Pendik Marina</strong> with fibreglass repair, painting, wooden refit and winterising. Close to Tuzla, we're flexible for jobs that need hauling out.</p>
<h2>Services we provide in Pendik</h2>
<ul>
<li><a href="/en/services/fibreglass-repair/">Fibreglass repair & osmosis treatment</a></li>
<li><a href="/en/services/boat-painting-antifouling/">Boat painting & antifouling</a></li>
<li><a href="/en/services/wooden-boat-refit/">Wooden boat refit</a></li>
<li><a href="/en/services/winterising-storage/">Winterising & storage</a></li>
</ul>
""",
 },
},
{
 "slug": "atakoy", "image": "/assets/images/parallax-1.jpg",
 "tr": {
   "name": "Ataköy",
   "short": "Ataköy Marina çevresinde tekne bakım, boya ve onarım.",
   "hero_title": "Ataköy'de Tekne Tamiri, Bakımı ve Renovasyonu",
   "hero_sub": "İstanbul'un Avrupa yakasında, Ataköy Marina çevresindeki tekneler için fiberglas, boya, ahşap ve kışlatma.",
   "meta_title": "Ataköy Tekne Tamiri, Bakımı ve Renovasyonu | Tekne Usta",
   "meta_desc": "Ataköy'de tekne tamiri, fiberglas onarımı, osmoz tedavisi, antifouling ve ahşap renovasyon. Ataköy Marina çevresinde ücretsiz keşif.",
   "body": """
<h2>Avrupa yakasında güvenilir servis</h2>
<p><strong>Ataköy Marina</strong>, İstanbul'un Avrupa yakasındaki en büyük yat limanlarından biri. Buradaki tekneler için fiberglas onarım, boya, ahşap renovasyon ve kışlatma hizmetleriyle yanınızdayız.</p>
<h2>Ataköy'de verdiğimiz hizmetler</h2>
<ul>
<li><a href="/hizmetler/fiberglas-onarim/">Fiberglas onarım ve osmoz tedavisi</a></li>
<li><a href="/hizmetler/tekne-boyama-antifouling/">Tekne boyama ve antifouling</a></li>
<li><a href="/hizmetler/ahsap-tekne-renovasyonu/">Ahşap tekne renovasyonu</a></li>
<li><a href="/hizmetler/teak-guverte-doseme/">Teak güverte döşeme</a></li>
</ul>
""",
 },
 "en": {
   "name": "Ataköy",
   "short": "Boat maintenance, painting and repair around Ataköy Marina.",
   "hero_title": "Boat Repair, Maintenance & Refit in Ataköy",
   "hero_sub": "On Istanbul's European side, for boats around Ataköy Marina — fibreglass, painting, wood and winterising.",
   "meta_title": "Ataköy Boat Repair, Maintenance & Refit | Tekne Usta",
   "meta_desc": "Boat repair, fibreglass repair, osmosis treatment, antifouling and wooden refit in Ataköy. Free survey around Ataköy Marina.",
   "body": """
<h2>Trusted service on the European side</h2>
<p><strong>Ataköy Marina</strong> is one of the largest marinas on Istanbul's European side. We support boats here with fibreglass repair, painting, wooden refit and winterising.</p>
<h2>Services we provide in Ataköy</h2>
<ul>
<li><a href="/en/services/fibreglass-repair/">Fibreglass repair & osmosis treatment</a></li>
<li><a href="/en/services/boat-painting-antifouling/">Boat painting & antifouling</a></li>
<li><a href="/en/services/wooden-boat-refit/">Wooden boat refit</a></li>
<li><a href="/en/services/teak-deck/">Teak decking</a></li>
</ul>
""",
 },
},
{
 "slug": "kalamis", "image": "/assets/images/parallax-2.jpg",
 "tr": {
   "name": "Kalamış",
   "short": "Kalamış ve Fenerbahçe Marina çevresinde tekne servisi.",
   "hero_title": "Kalamış'ta Tekne Tamiri, Bakımı ve Renovasyonu",
   "hero_sub": "Kalamış ve Fenerbahçe Marina çevresindeki tekneler için fiberglas, boya, ahşap ve teak hizmetleri.",
   "meta_title": "Kalamış Tekne Tamiri, Bakımı ve Renovasyonu | Tekne Usta",
   "meta_desc": "Kalamış'ta tekne tamiri, fiberglas onarımı, osmoz tedavisi, antifouling ve ahşap renovasyon. Kalamış ve Fenerbahçe Marina çevresinde ücretsiz keşif.",
   "body": """
<h2>Kalamış'ın köklü denizcilik kültürüne</h2>
<p>Kalamış ve Fenerbahçe, İstanbul'un en köklü yelken ve tekne merkezlerinden biri. <strong>Kalamış Marina ve Fenerbahçe Marina</strong> çevresindeki tekneler için fiberglas onarım, boya, ahşap renovasyon ve teak hizmetleri sunuyoruz.</p>
<h2>Kalamış'ta verdiğimiz hizmetler</h2>
<ul>
<li><a href="/hizmetler/fiberglas-onarim/">Fiberglas onarım ve osmoz tedavisi</a></li>
<li><a href="/hizmetler/tekne-boyama-antifouling/">Tekne boyama ve antifouling</a></li>
<li><a href="/hizmetler/ahsap-tekne-renovasyonu/">Ahşap tekne renovasyonu</a></li>
<li><a href="/hizmetler/teak-guverte-doseme/">Teak güverte döşeme</a></li>
</ul>
""",
 },
 "en": {
   "name": "Kalamış",
   "short": "Boat service around Kalamış and Fenerbahçe Marina.",
   "hero_title": "Boat Repair, Maintenance & Refit in Kalamış",
   "hero_sub": "For boats around Kalamış and Fenerbahçe Marina — fibreglass, painting, wood and teak services.",
   "meta_title": "Kalamış Boat Repair, Maintenance & Refit | Tekne Usta",
   "meta_desc": "Boat repair, fibreglass repair, osmosis treatment, antifouling and wooden refit in Kalamış. Free survey around Kalamış and Fenerbahçe Marina.",
   "body": """
<h2>For Kalamış's deep sailing culture</h2>
<p>Kalamış and Fenerbahçe form one of Istanbul's most established sailing and boating centres. We serve boats around <strong>Kalamış Marina and Fenerbahçe Marina</strong> with fibreglass repair, painting, wooden refit and teak work.</p>
<h2>Services we provide in Kalamış</h2>
<ul>
<li><a href="/en/services/fibreglass-repair/">Fibreglass repair & osmosis treatment</a></li>
<li><a href="/en/services/boat-painting-antifouling/">Boat painting & antifouling</a></li>
<li><a href="/en/services/wooden-boat-refit/">Wooden boat refit</a></li>
<li><a href="/en/services/teak-deck/">Teak decking</a></li>
</ul>
""",
 },
},
{
 "slug": "urla", "image": "/assets/images/parallax-3.jpg",
 "tr": {
   "name": "Urla / İzmir",
   "short": "Urla, Sığacık ve İzmir körfezinde tekne bakım ve onarımı.",
   "hero_title": "Urla ve İzmir'de Tekne Tamiri, Bakımı ve Renovasyonu",
   "hero_sub": "Urla, Sığacık ve İzmir körfezindeki tekneler için fiberglas, boya, ahşap renovasyon ve teak.",
   "meta_title": "Urla / İzmir Tekne Tamiri ve Bakımı | Tekne Usta",
   "meta_desc": "Urla ve İzmir'de tekne tamiri, fiberglas onarımı, osmoz tedavisi, antifouling ve ahşap renovasyon. Urla, Sığacık ve İzmir körfezinde ücretsiz keşif.",
   "body": """
<h2>İzmir körfezinin canlı denizciliğine</h2>
<p>Urla ve Sığacık, İzmir'in en gözde tekne bölgeleri. <strong>Levent Marina Urla ve Teos Marina Sığacık</strong> çevresindeki tekneler için fiberglas onarım, boya, ahşap renovasyon ve teak hizmetleri sunuyoruz.</p>
<h2>Urla / İzmir'de verdiğimiz hizmetler</h2>
<ul>
<li><a href="/hizmetler/fiberglas-onarim/">Fiberglas onarım ve osmoz tedavisi</a></li>
<li><a href="/hizmetler/tekne-boyama-antifouling/">Tekne boyama ve antifouling</a></li>
<li><a href="/hizmetler/ahsap-tekne-renovasyonu/">Ahşap tekne renovasyonu</a></li>
<li><a href="/hizmetler/teak-guverte-doseme/">Teak güverte döşeme</a></li>
</ul>
""",
 },
 "en": {
   "name": "Urla / İzmir",
   "short": "Boat maintenance and repair around Urla, Sığacık and the Gulf of İzmir.",
   "hero_title": "Boat Repair, Maintenance & Refit in Urla & İzmir",
   "hero_sub": "For boats around Urla, Sığacık and the Gulf of İzmir — fibreglass, painting, wooden refit and teak.",
   "meta_title": "Urla / İzmir Boat Repair & Maintenance | Tekne Usta",
   "meta_desc": "Boat repair, fibreglass repair, osmosis treatment, antifouling and wooden refit in Urla and İzmir. Free survey around Urla, Sığacık and the Gulf of İzmir.",
   "body": """
<h2>For the lively boating of the Gulf of İzmir</h2>
<p>Urla and Sığacık are among İzmir's most popular boating areas. We serve boats around <strong>Levent Marina Urla and Teos Marina Sığacık</strong> with fibreglass repair, painting, wooden refit and teak work.</p>
<h2>Services we provide in Urla / İzmir</h2>
<ul>
<li><a href="/en/services/fibreglass-repair/">Fibreglass repair & osmosis treatment</a></li>
<li><a href="/en/services/boat-painting-antifouling/">Boat painting & antifouling</a></li>
<li><a href="/en/services/wooden-boat-refit/">Wooden boat refit</a></li>
<li><a href="/en/services/teak-deck/">Teak decking</a></li>
</ul>
""",
 },
},
{
 "slug": "didim", "image": "/assets/images/parallax-1.jpg",
 "tr": {
   "name": "Didim",
   "short": "D-Marin Didim çevresinde tekne bakım, boya ve onarımı.",
   "hero_title": "Didim'de Tekne Tamiri, Bakımı ve Renovasyonu",
   "hero_sub": "D-Marin Didim çevresindeki tekneler için fiberglas, boya, ahşap renovasyon ve kışlatma.",
   "meta_title": "Didim Tekne Tamiri, Bakımı ve Renovasyonu | Tekne Usta",
   "meta_desc": "Didim'de tekne tamiri, fiberglas onarımı, osmoz tedavisi, antifouling ve ahşap renovasyon. D-Marin Didim çevresinde ücretsiz keşif ve şeffaf teklif.",
   "body": """
<h2>Didim'in büyük marina trafiğine</h2>
<p>Ege'nin büyük yat üslerinden <strong>D-Marin Didim</strong> çevresinde çok sayıda tekne kışlar ve bakım görür. Bu tekneler için fiberglas onarım, boya, ahşap renovasyon ve kışlatma hizmetleriyle yanınızdayız.</p>
<h2>Didim'de verdiğimiz hizmetler</h2>
<ul>
<li><a href="/hizmetler/fiberglas-onarim/">Fiberglas onarım ve osmoz tedavisi</a></li>
<li><a href="/hizmetler/tekne-boyama-antifouling/">Tekne boyama ve antifouling</a></li>
<li><a href="/hizmetler/ahsap-tekne-renovasyonu/">Ahşap tekne renovasyonu</a></li>
<li><a href="/hizmetler/tekne-kislatma/">Tekne kışlatma</a></li>
</ul>
""",
 },
 "en": {
   "name": "Didim",
   "short": "Boat maintenance, painting and repair around D-Marin Didim.",
   "hero_title": "Boat Repair, Maintenance & Refit in Didim",
   "hero_sub": "For boats around D-Marin Didim — fibreglass, painting, wooden refit and winterising.",
   "meta_title": "Didim Boat Repair, Maintenance & Refit | Tekne Usta",
   "meta_desc": "Boat repair, fibreglass repair, osmosis treatment, antifouling and wooden refit in Didim. Free survey and transparent quote around D-Marin Didim.",
   "body": """
<h2>For Didim's busy marina traffic</h2>
<p>Around <strong>D-Marin Didim</strong>, one of the Aegean's large yacht bases, many boats winter and are maintained. We support these boats with fibreglass repair, painting, wooden refit and winterising.</p>
<h2>Services we provide in Didim</h2>
<ul>
<li><a href="/en/services/fibreglass-repair/">Fibreglass repair & osmosis treatment</a></li>
<li><a href="/en/services/boat-painting-antifouling/">Boat painting & antifouling</a></li>
<li><a href="/en/services/wooden-boat-refit/">Wooden boat refit</a></li>
<li><a href="/en/services/winterising-storage/">Winterising & storage</a></li>
</ul>
""",
 },
},
{
 "slug": "ayvalik", "image": "/assets/images/parallax-2.jpg",
 "tr": {
   "name": "Ayvalık",
   "short": "Ayvalık ve Setur Ayvalık Marina çevresinde tekne servisi.",
   "hero_title": "Ayvalık'ta Tekne Tamiri, Bakımı ve Renovasyonu",
   "hero_sub": "Ayvalık ve Setur Ayvalık Marina çevresindeki tekneler için fiberglas, boya, ahşap ve kışlatma.",
   "meta_title": "Ayvalık Tekne Tamiri, Bakımı ve Renovasyonu | Tekne Usta",
   "meta_desc": "Ayvalık'ta tekne tamiri, fiberglas onarımı, osmoz tedavisi, antifouling ve ahşap renovasyon. Setur Ayvalık Marina çevresinde ücretsiz keşif.",
   "body": """
<h2>Kuzey Ege'nin sakin koylarına</h2>
<p>Ayvalık, adaları ve korunaklı koylarıyla kuzey Ege'nin sevilen tekne bölgelerinden. <strong>Setur Ayvalık Marina</strong> çevresindeki tekneler için fiberglas onarım, boya, ahşap renovasyon ve kışlatma sunuyoruz.</p>
<h2>Ayvalık'ta verdiğimiz hizmetler</h2>
<ul>
<li><a href="/hizmetler/fiberglas-onarim/">Fiberglas onarım ve osmoz tedavisi</a></li>
<li><a href="/hizmetler/tekne-boyama-antifouling/">Tekne boyama ve antifouling</a></li>
<li><a href="/hizmetler/ahsap-tekne-renovasyonu/">Ahşap tekne renovasyonu</a></li>
<li><a href="/hizmetler/tekne-kislatma/">Tekne kışlatma</a></li>
</ul>
""",
 },
 "en": {
   "name": "Ayvalık",
   "short": "Boat service around Ayvalık and Setur Ayvalık Marina.",
   "hero_title": "Boat Repair, Maintenance & Refit in Ayvalık",
   "hero_sub": "For boats around Ayvalık and Setur Ayvalık Marina — fibreglass, painting, wood and winterising.",
   "meta_title": "Ayvalık Boat Repair, Maintenance & Refit | Tekne Usta",
   "meta_desc": "Boat repair, fibreglass repair, osmosis treatment, antifouling and wooden refit in Ayvalık. Free survey around Setur Ayvalık Marina.",
   "body": """
<h2>For the calm bays of the northern Aegean</h2>
<p>Ayvalık, with its islands and sheltered bays, is a favourite boating area of the northern Aegean. We offer fibreglass repair, painting, wooden refit and winterising for boats around <strong>Setur Ayvalık Marina</strong>.</p>
<h2>Services we provide in Ayvalık</h2>
<ul>
<li><a href="/en/services/fibreglass-repair/">Fibreglass repair & osmosis treatment</a></li>
<li><a href="/en/services/boat-painting-antifouling/">Boat painting & antifouling</a></li>
<li><a href="/en/services/wooden-boat-refit/">Wooden boat refit</a></li>
<li><a href="/en/services/winterising-storage/">Winterising & storage</a></li>
</ul>
""",
 },
},
{
 "slug": "datca", "image": "/assets/images/parallax-3.jpg",
 "tr": {
   "name": "Datça",
   "short": "Datça ve çevresindeki koylarda tekne bakım ve onarımı.",
   "hero_title": "Datça'da Tekne Tamiri, Bakımı ve Renovasyonu",
   "hero_sub": "Datça ve çevresindeki tekneler için fiberglas, boya, ahşap renovasyon ve teak hizmetleri.",
   "meta_title": "Datça Tekne Tamiri, Bakımı ve Renovasyonu | Tekne Usta",
   "meta_desc": "Datça'da tekne tamiri, fiberglas onarımı, osmoz tedavisi, antifouling ve ahşap renovasyon. Datça ve çevresinde ücretsiz keşif ve şeffaf teklif.",
   "body": """
<h2>Datça'nın el değmemiş koylarına</h2>
<p>Datça yarımadası, temiz denizi ve sakin koylarıyla tekne sahiplerinin gözdesi. Bölgedeki tekneler için fiberglas onarım, boya, ahşap renovasyon ve teak hizmetleri sunuyoruz; Marmaris ve Bodrum'a yakınlığıyla lojistik olarak esneğiz.</p>
<h2>Datça'da verdiğimiz hizmetler</h2>
<ul>
<li><a href="/hizmetler/fiberglas-onarim/">Fiberglas onarım ve osmoz tedavisi</a></li>
<li><a href="/hizmetler/tekne-boyama-antifouling/">Tekne boyama ve antifouling</a></li>
<li><a href="/hizmetler/ahsap-tekne-renovasyonu/">Ahşap tekne renovasyonu</a></li>
<li><a href="/hizmetler/teak-guverte-doseme/">Teak güverte döşeme</a></li>
</ul>
""",
 },
 "en": {
   "name": "Datça",
   "short": "Boat maintenance and repair in Datça and its surrounding bays.",
   "hero_title": "Boat Repair, Maintenance & Refit in Datça",
   "hero_sub": "For boats around Datça — fibreglass, painting, wooden refit and teak services.",
   "meta_title": "Datça Boat Repair, Maintenance & Refit | Tekne Usta",
   "meta_desc": "Boat repair, fibreglass repair, osmosis treatment, antifouling and wooden refit in Datça. Free survey and transparent quote around Datça.",
   "body": """
<h2>For Datça's unspoilt bays</h2>
<p>The Datça peninsula, with its clean sea and quiet bays, is a favourite of boat owners. We offer fibreglass repair, painting, wooden refit and teak work for boats in the area; close to Marmaris and Bodrum, we're logistically flexible.</p>
<h2>Services we provide in Datça</h2>
<ul>
<li><a href="/en/services/fibreglass-repair/">Fibreglass repair & osmosis treatment</a></li>
<li><a href="/en/services/boat-painting-antifouling/">Boat painting & antifouling</a></li>
<li><a href="/en/services/wooden-boat-refit/">Wooden boat refit</a></li>
<li><a href="/en/services/teak-deck/">Teak decking</a></li>
</ul>
""",
 },
},
{
 "slug": "antalya", "image": "/assets/images/parallax-1.jpg",
 "tr": {
   "name": "Antalya",
   "short": "Antalya marinaları çevresinde tekne bakım, boya ve onarımı.",
   "hero_title": "Antalya'da Tekne Tamiri, Bakımı ve Renovasyonu",
   "hero_sub": "Setur Antalya ve Çelebi Marina çevresindeki tekneler için fiberglas, boya, ahşap ve teak hizmetleri.",
   "meta_title": "Antalya Tekne Tamiri, Bakımı ve Renovasyonu | Tekne Usta",
   "meta_desc": "Antalya'da tekne tamiri, fiberglas onarımı, osmoz tedavisi, antifouling ve ahşap renovasyon. Setur Antalya ve Çelebi Marina çevresinde ücretsiz keşif.",
   "body": """
<h2>Akdeniz'in yat merkezine</h2>
<p>Antalya, uzun sezonu ve büyük marina kapasitesiyle Akdeniz'in önemli yat merkezlerinden. <strong>Setur Antalya Marina, Çelebi Marina ve Kaleiçi Yat Limanı</strong> çevresindeki tekneler için fiberglas onarım, boya, ahşap renovasyon ve teak hizmetleri sunuyoruz.</p>
<h2>Antalya'da verdiğimiz hizmetler</h2>
<ul>
<li><a href="/hizmetler/fiberglas-onarim/">Fiberglas onarım ve osmoz tedavisi</a></li>
<li><a href="/hizmetler/tekne-boyama-antifouling/">Tekne boyama ve antifouling</a></li>
<li><a href="/hizmetler/ahsap-tekne-renovasyonu/">Ahşap tekne renovasyonu</a></li>
<li><a href="/hizmetler/teak-guverte-doseme/">Teak güverte döşeme</a></li>
</ul>
""",
 },
 "en": {
   "name": "Antalya",
   "short": "Boat maintenance, painting and repair around Antalya's marinas.",
   "hero_title": "Boat Repair, Maintenance & Refit in Antalya",
   "hero_sub": "For boats around Setur Antalya and Çelebi Marina — fibreglass, painting, wood and teak services.",
   "meta_title": "Antalya Boat Repair, Maintenance & Refit | Tekne Usta",
   "meta_desc": "Boat repair, fibreglass repair, osmosis treatment, antifouling and wooden refit in Antalya. Free survey around Setur Antalya and Çelebi Marina.",
   "body": """
<h2>For the Mediterranean's yachting hub</h2>
<p>Antalya, with its long season and large marina capacity, is an important Mediterranean yachting hub. We serve boats around <strong>Setur Antalya Marina, Çelebi Marina and the Kaleiçi Marina</strong> with fibreglass repair, painting, wooden refit and teak work.</p>
<h2>Services we provide in Antalya</h2>
<ul>
<li><a href="/en/services/fibreglass-repair/">Fibreglass repair & osmosis treatment</a></li>
<li><a href="/en/services/boat-painting-antifouling/">Boat painting & antifouling</a></li>
<li><a href="/en/services/wooden-boat-refit/">Wooden boat refit</a></li>
<li><a href="/en/services/teak-deck/">Teak decking</a></li>
</ul>
""",
 },
},
{
 "slug": "kas", "image": "/assets/images/parallax-2.jpg",
 "tr": {
   "name": "Kaş",
   "short": "Kaş ve çevresindeki koylarda tekne bakım ve onarımı.",
   "hero_title": "Kaş'ta Tekne Tamiri, Bakımı ve Renovasyonu",
   "hero_sub": "Kaş Marina ve çevresindeki tekneler için fiberglas, boya, ahşap renovasyon ve teak hizmetleri.",
   "meta_title": "Kaş Tekne Tamiri, Bakımı ve Renovasyonu | Tekne Usta",
   "meta_desc": "Kaş'ta tekne tamiri, fiberglas onarımı, osmoz tedavisi, antifouling ve ahşap renovasyon. Kaş Marina çevresinde ücretsiz keşif ve şeffaf teklif.",
   "body": """
<h2>Kaş'ın berrak sularındaki teknelere</h2>
<p>Kaş, temiz denizi ve dalış turizmiyle Akdeniz'in özel köşelerinden. <strong>Kaş Marina</strong> ve çevresindeki tekneler için fiberglas onarım, boya, ahşap renovasyon ve teak hizmetleri sunuyoruz.</p>
<h2>Kaş'ta verdiğimiz hizmetler</h2>
<ul>
<li><a href="/hizmetler/fiberglas-onarim/">Fiberglas onarım ve osmoz tedavisi</a></li>
<li><a href="/hizmetler/tekne-boyama-antifouling/">Tekne boyama ve antifouling</a></li>
<li><a href="/hizmetler/ahsap-tekne-renovasyonu/">Ahşap tekne renovasyonu</a></li>
<li><a href="/hizmetler/teak-guverte-doseme/">Teak güverte döşeme</a></li>
</ul>
""",
 },
 "en": {
   "name": "Kaş",
   "short": "Boat maintenance and repair in Kaş and its surrounding bays.",
   "hero_title": "Boat Repair, Maintenance & Refit in Kaş",
   "hero_sub": "For boats around Kaş Marina — fibreglass, painting, wooden refit and teak services.",
   "meta_title": "Kaş Boat Repair, Maintenance & Refit | Tekne Usta",
   "meta_desc": "Boat repair, fibreglass repair, osmosis treatment, antifouling and wooden refit in Kaş. Free survey and transparent quote around Kaş Marina.",
   "body": """
<h2>For boats in Kaş's clear waters</h2>
<p>Kaş, with its clean sea and diving tourism, is a special corner of the Mediterranean. We serve boats around <strong>Kaş Marina</strong> with fibreglass repair, painting, wooden refit and teak work.</p>
<h2>Services we provide in Kaş</h2>
<ul>
<li><a href="/en/services/fibreglass-repair/">Fibreglass repair & osmosis treatment</a></li>
<li><a href="/en/services/boat-painting-antifouling/">Boat painting & antifouling</a></li>
<li><a href="/en/services/wooden-boat-refit/">Wooden boat refit</a></li>
<li><a href="/en/services/teak-deck/">Teak decking</a></li>
</ul>
""",
 },
},
{
 "slug": "kusadasi", "image": "/assets/images/parallax-3.jpg",
 "tr": {
   "name": "Kuşadası",
   "short": "Kuşadası Setur Marina çevresinde tekne bakım ve onarımı.",
   "hero_title": "Kuşadası'nda Tekne Tamiri, Bakımı ve Renovasyonu",
   "hero_sub": "Kuşadası Setur Marina çevresindeki tekneler için fiberglas, boya, ahşap renovasyon ve kışlatma.",
   "meta_title": "Kuşadası Tekne Tamiri, Bakımı ve Renovasyonu | Tekne Usta",
   "meta_desc": "Kuşadası'nda tekne tamiri, fiberglas onarımı, osmoz tedavisi, antifouling ve ahşap renovasyon. Kuşadası Setur Marina çevresinde ücretsiz keşif.",
   "body": """
<h2>Kuşadası'nın yoğun marina trafiğine</h2>
<p>Kuşadası, Ege'nin en işlek yat limanlarından birine ev sahipliği yapıyor. <strong>Kuşadası Setur Marina</strong> çevresindeki tekneler için fiberglas onarım, boya, ahşap renovasyon ve kışlatma hizmetleri sunuyoruz.</p>
<h2>Kuşadası'nda verdiğimiz hizmetler</h2>
<ul>
<li><a href="/hizmetler/fiberglas-onarim/">Fiberglas onarım ve osmoz tedavisi</a></li>
<li><a href="/hizmetler/tekne-boyama-antifouling/">Tekne boyama ve antifouling</a></li>
<li><a href="/hizmetler/ahsap-tekne-renovasyonu/">Ahşap tekne renovasyonu</a></li>
<li><a href="/hizmetler/tekne-kislatma/">Tekne kışlatma</a></li>
</ul>
""",
 },
 "en": {
   "name": "Kuşadası",
   "short": "Boat maintenance and repair around Kuşadası Setur Marina.",
   "hero_title": "Boat Repair, Maintenance & Refit in Kuşadası",
   "hero_sub": "For boats around Kuşadası Setur Marina — fibreglass, painting, wooden refit and winterising.",
   "meta_title": "Kuşadası Boat Repair, Maintenance & Refit | Tekne Usta",
   "meta_desc": "Boat repair, fibreglass repair, osmosis treatment, antifouling and wooden refit in Kuşadası. Free survey around Kuşadası Setur Marina.",
   "body": """
<h2>For Kuşadası's busy marina traffic</h2>
<p>Kuşadası hosts one of the Aegean's busiest marinas. We serve boats around <strong>Kuşadası Setur Marina</strong> with fibreglass repair, painting, wooden refit and winterising.</p>
<h2>Services we provide in Kuşadası</h2>
<ul>
<li><a href="/en/services/fibreglass-repair/">Fibreglass repair & osmosis treatment</a></li>
<li><a href="/en/services/boat-painting-antifouling/">Boat painting & antifouling</a></li>
<li><a href="/en/services/wooden-boat-refit/">Wooden boat refit</a></li>
<li><a href="/en/services/winterising-storage/">Winterising & storage</a></li>
</ul>
""",
 },
},
{
 "slug": "mudanya", "image": "/assets/images/parallax-1.jpg",
 "tr": {
   "name": "Mudanya",
   "short": "Mudanya ve Marmara kıyısında tekne bakım ve onarımı.",
   "hero_title": "Mudanya'da Tekne Tamiri, Bakımı ve Renovasyonu",
   "hero_sub": "Mudanya ve Bursa kıyısındaki tekneler için fiberglas, boya, ahşap renovasyon ve kışlatma.",
   "meta_title": "Mudanya Tekne Tamiri, Bakımı ve Renovasyonu | Tekne Usta",
   "meta_desc": "Mudanya'da tekne tamiri, fiberglas onarımı, osmoz tedavisi, antifouling ve ahşap renovasyon. Mudanya ve Marmara kıyısında ücretsiz keşif.",
   "body": """
<h2>Marmara kıyısının tekne sahiplerine</h2>
<p>Mudanya, Bursa'nın deniz kapısı ve Marmara'nın sevilen bir tekne bölgesi. <strong>Mudanya</strong> ve çevresindeki tekneler için fiberglas onarım, boya, ahşap renovasyon ve kışlatma hizmetleri sunuyoruz; İstanbul'a yakınlığıyla lojistik olarak esneğiz.</p>
<h2>Mudanya'da verdiğimiz hizmetler</h2>
<ul>
<li><a href="/hizmetler/fiberglas-onarim/">Fiberglas onarım ve osmoz tedavisi</a></li>
<li><a href="/hizmetler/tekne-boyama-antifouling/">Tekne boyama ve antifouling</a></li>
<li><a href="/hizmetler/ahsap-tekne-renovasyonu/">Ahşap tekne renovasyonu</a></li>
<li><a href="/hizmetler/tekne-kislatma/">Tekne kışlatma</a></li>
</ul>
""",
 },
 "en": {
   "name": "Mudanya",
   "short": "Boat maintenance and repair in Mudanya and the Marmara coast.",
   "hero_title": "Boat Repair, Maintenance & Refit in Mudanya",
   "hero_sub": "For boats on the Mudanya and Bursa coast — fibreglass, painting, wooden refit and winterising.",
   "meta_title": "Mudanya Boat Repair, Maintenance & Refit | Tekne Usta",
   "meta_desc": "Boat repair, fibreglass repair, osmosis treatment, antifouling and wooden refit in Mudanya. Free survey on the Mudanya and Marmara coast.",
   "body": """
<h2>For boat owners on the Marmara coast</h2>
<p>Mudanya, Bursa's gateway to the sea, is a favourite Marmara boating area. We serve boats around <strong>Mudanya</strong> with fibreglass repair, painting, wooden refit and winterising; close to Istanbul, we're logistically flexible.</p>
<h2>Services we provide in Mudanya</h2>
<ul>
<li><a href="/en/services/fibreglass-repair/">Fibreglass repair & osmosis treatment</a></li>
<li><a href="/en/services/boat-painting-antifouling/">Boat painting & antifouling</a></li>
<li><a href="/en/services/wooden-boat-refit/">Wooden boat refit</a></li>
<li><a href="/en/services/winterising-storage/">Winterising & storage</a></li>
</ul>
""",
 },
},
]

# ------------------------------------------------------------------ Blog posts
POSTS = [
{
 "slug": "osmoz-nedir-tedavisi", "slug_en": "what-is-osmosis-treatment",
 "image": "/assets/images/services/fiberglas.jpg", "date": "2026-02-10",
 "tr": {
   "category": "Fiberglas",
   "title": "Osmoz Nedir, Fiber Teknelerde Nasıl Tedavi Edilir?",
   "excerpt": "Fiber teknelerde osmoz kabarcıkları neden oluşur, nasıl anlaşılır ve doğru tedavi nasıl yapılır? Tekne sahipleri için sade bir rehber.",
   "meta_title": "Osmoz Nedir? Fiber Teknede Osmoz Tedavisi Rehberi | Tekne Usta",
   "meta_desc": "Fiber teknelerde osmoz nedir, kabarcıklar neden oluşur ve osmoz tedavisi nasıl yapılır? Belirtiler, kurutma süreci ve maliyeti etkileyen faktörler.",
   "body": """
<p>Osmoz, fiberglas tekne sahiplerinin en çok korktuğu kelimelerden biridir — ama doğru anlaşıldığında yönetilebilir bir sorundur. Bu yazıda osmozun ne olduğunu, nasıl fark edileceğini ve profesyonel bir tedavinin nasıl işlediğini sade biçimde anlatıyoruz.</p>
<h2>Osmoz nedir?</h2>
<p>Fiberglas tekneler, dış yüzeydeki jelkot (gelcoat) katmanının altında cam elyafı ve reçineden oluşan bir laminata sahiptir. Zamanla su, jelkotun mikro gözeneklerinden içeri sızar ve laminattaki çözünür bileşenlerle tepkimeye girer. Bu tepkime asidik bir sıvı ve gaz üretir; basınç arttıkça jelkotun altında <strong>kabarcıklar</strong> oluşur. İşte bu sürece osmoz denir.</p>
<h2>Osmoz belirtileri nelerdir?</h2>
<ul>
<li>Su altı yüzeyde, özellikle tekne karadayken beliren <strong>kabarcıklar</strong></li>
<li>Kabarcık delindiğinde çıkan <strong>ekşi/sirke benzeri kokulu sıvı</strong></li>
<li>Jelkotta yer yer matlaşma ve nem izleri</li>
</ul>
<p>Birkaç küçük kabarcık her zaman acil bir felaket değildir; ancak yaygınlaşırsa laminatın yapısal bütünlüğünü tehdit eder. Bu yüzden erken tespit önemlidir.</p>
<h2>Osmoz tedavisi nasıl yapılır?</h2>
<p>Doğru bir osmoz tedavisi sabır ister ve şu aşamalardan geçer:</p>
<ul>
<li><strong>Jelkot sıyırma:</strong> Etkilenen jelkot katmanı özel bir planya ile kaldırılır.</li>
<li><strong>Yıkama ve kurutma:</strong> Laminat basınçlı suyla yıkanır ve <strong>nem seviyesi kabul edilebilir bir eşiğe düşene kadar</strong> — bazen haftalarca — kurumaya bırakılır. Bu adım atlanırsa tedavi başarısız olur.</li>
<li><strong>Onarım ve dolgu:</strong> Açılan kabarcıklar epoksi dolgu ile onarılır.</li>
<li><strong>Epoksi bariyer kat:</strong> Suyun bir daha girmemesi için çok katlı epoksi bariyer uygulanır.</li>
<li><strong>Antifouling:</strong> Son olarak su altı boya (antifouling) uygulanır.</li>
</ul>
<p>En kritik nokta <strong>kurutmadır</strong>. Nem ölçümü yapmadan bariyer kat uygulayan bir servis, sorunu içeri hapsetmiş olur. Biz nem seviyesi uygun olmadan bir sonraki adıma geçmeyiz.</p>
<h2>Maliyeti ve süreyi ne belirler?</h2>
<p>Osmoz tedavisinin maliyeti; tekne boyuna, hasarın yaygınlığına ve gereken kurutma süresine göre değişir. Kurutma iklime ve laminatın durumuna bağlı olduğu için süre baştan net verilemez; keşifte nem ölçümüyle gerçekçi bir takvim çıkarırız.</p>
<h2>Osmozdan nasıl korunulur?</h2>
<p>Yeni teknelerde kaliteli bir epoksi bariyer kat, koruyucu bir yatırımdır. Mevcut teknelerde ise düzenli karina kontrolü ve antifouling bakımı erken uyarı sağlar.</p>
<p>Teknenizde kabarcık fark ettiyseniz, <a href="/hizmetler/fiberglas-onarim/">fiberglas onarım ve osmoz tedavisi</a> hizmetimiz kapsamında ücretsiz keşif için bize yazın. Nem ölçümüyle durumu net ortaya koyar, kalem kalem teklif veririz.</p>
""",
 },
 "en": {
   "category": "Fibreglass",
   "title": "What Is Osmosis and How Is It Treated on Fibreglass Boats?",
   "excerpt": "Why do osmosis blisters form on fibreglass boats, how do you spot them, and how is proper treatment done? A plain guide for boat owners.",
   "meta_title": "What Is Osmosis? Fibreglass Osmosis Treatment Guide | Tekne Usta",
   "meta_desc": "What is osmosis on fibreglass boats, why do blisters form and how is osmosis treatment done? Symptoms, the drying process and what affects the cost.",
   "body": """
<p>Osmosis is one of the words fibreglass boat owners dread most — but understood correctly, it's a manageable problem. This article explains, in plain terms, what osmosis is, how to spot it and how a professional treatment works.</p>
<h2>What is osmosis?</h2>
<p>Fibreglass boats have a laminate of glass fibre and resin beneath the outer gelcoat layer. Over time water seeps through the gelcoat's micro-pores and reacts with soluble components in the laminate. This reaction produces an acidic liquid and gas; as pressure builds, <strong>blisters</strong> form under the gelcoat. That process is osmosis.</p>
<h2>What are the symptoms?</h2>
<ul>
<li><strong>Blisters</strong> on the underwater surface, most visible when the boat is ashore</li>
<li>A <strong>sour, vinegar-like fluid</strong> when a blister is pierced</li>
<li>Patchy dullness and moisture marks in the gelcoat</li>
</ul>
<p>A few small blisters aren't always an emergency; but once widespread, they threaten the laminate's structural integrity. That's why early detection matters.</p>
<h2>How is osmosis treated?</h2>
<p>Correct osmosis treatment takes patience and follows these stages:</p>
<ul>
<li><strong>Gelcoat peeling:</strong> the affected gelcoat layer is removed with a special peeler.</li>
<li><strong>Washing and drying:</strong> the laminate is pressure-washed and left to dry <strong>until the moisture level drops below an acceptable threshold</strong> — sometimes for weeks. Skip this and the treatment fails.</li>
<li><strong>Repair and fill:</strong> opened blisters are repaired with epoxy filler.</li>
<li><strong>Epoxy barrier coat:</strong> a multi-coat epoxy barrier keeps water from getting back in.</li>
<li><strong>Antifouling:</strong> finally, underwater paint is applied.</li>
</ul>
<p>The critical point is <strong>drying</strong>. A yard that applies a barrier coat without measuring moisture simply traps the problem inside. We never move to the next step until the moisture level is right.</p>
<h2>What determines cost and time?</h2>
<p>The cost of osmosis treatment depends on boat length, how widespread the damage is and the drying time required. Because drying depends on climate and laminate condition, the timing can't be fixed in advance; we produce a realistic schedule from a moisture reading at the survey.</p>
<h2>How do you prevent osmosis?</h2>
<p>On new boats a quality epoxy barrier coat is a protective investment. On existing boats, regular hull checks and antifouling maintenance give early warning.</p>
<p>If you've noticed blisters, message us for a free survey under our <a href="/en/services/fibreglass-repair/">fibreglass repair and osmosis treatment</a> service. We'll assess the situation with a moisture reading and give an itemised quote.</p>
""",
 },
},
{
 "slug": "antifouling-secimi", "slug_en": "choosing-antifouling",
 "image": "/assets/images/services/boya.jpg", "date": "2026-03-05",
 "tr": {
   "category": "Boya",
   "title": "Antifouling (Zehirli Boya) Seçimi: Teknenize Doğru Boya Nasıl Seçilir?",
   "excerpt": "Sert matris mi, aşınan (self-polishing) tip mi? Antifouling seçerken teknenizin malzemesi, hızı ve suyu neden önemli?",
   "meta_title": "Antifouling (Zehirli Boya) Seçim Rehberi | Tekne Usta",
   "meta_desc": "Antifouling zehirli boya nasıl seçilir? Sert matris ve self-polishing farkı, tekne malzemesi ve kullanıma göre doğru antifouling seçimi ve uygulama ipuçları.",
   "body": """
<p>Antifouling — halk arasında "zehirli boya" — tekneyi su altındaki deniz canlılarının (yosun, midye, kaya midyesi) yapışmasından koruyan boyadır. Yanlış seçim, hem performans kaybına hem gereksiz masrafa yol açar. Peki teknenize doğru antifouling nasıl seçilir?</p>
<h2>Antifouling neden önemli?</h2>
<p>Su altına yapışan canlılar tekneyi ağırlaştırır, yakıt tüketimini artırır ve zamanla yüzeye zarar verir. İyi bir antifouling, sezon boyunca karinayı temiz tutar.</p>
<h2>İki ana tip: sert matris ve self-polishing</h2>
<ul>
<li><strong>Sert matris (hard) antifouling:</strong> Yüzeyde sert bir film bırakır, aşınmaz. Yüksek hızlı tekneler, sık karaya çekilen tekneler ve yarış tekneleri için uygundur. Zamanla katman biriktiği için ara ara zımpara gerekir.</li>
<li><strong>Aşınan (self-polishing) antifouling:</strong> Tekne su içinde hareket ettikçe kontrollü biçimde aşınır ve sürekli taze bir yüzey açığa çıkarır. Gezi tekneleri ve düşük-orta hızlı tekneler için idealdir; katman birikimi daha azdır.</li>
</ul>
<h2>Seçimi etkileyen faktörler</h2>
<ul>
<li><strong>Tekne malzemesi:</strong> Alüminyum teknelerde bakır içeren bazı boyalar korozyon yapar; bu teknelerde bakırsız formüller gerekir.</li>
<li><strong>Kullanım ve hız:</strong> Hızlı ve az kullanılan tekne mi, sürekli seyir hâlinde bir gezi teknesi mi?</li>
<li><strong>Suyun karakteri:</strong> Sıcak ve besin açısından zengin sular daha agresif canlı yapışması demektir; daha güçlü koruma gerekir.</li>
<li><strong>Önceki boya:</strong> Yeni boya, eski boya tipiyle uyumlu olmalı; değilse ara kat (tie-coat) veya sıyırma gerekebilir.</li>
</ul>
<h2>Uygulamada dikkat edilmesi gerekenler</h2>
<p>En iyi boya bile kötü uygulamayla işe yaramaz. Yüzeyin temiz, kuru ve doğru zımparalanmış olması; kat sayısına ve üreticinin kuruma sürelerine uyulması şarttır. Su hattı ve hareketli yüzeylerde ekstra kat önerilir.</p>
<h2>Ne sıklıkla yenilenmeli?</h2>
<p>Çoğu tekne için yılda bir, sezon başında yenileme idealdir. Yoğun kullanılan ve sıcak sularda kalan tekneler daha sık bakım isteyebilir.</p>
<p>Teknenize hangi antifouling'in uygun olduğundan emin değilseniz, <a href="/hizmetler/tekne-boyama-antifouling/">tekne boyama ve antifouling</a> hizmetimiz kapsamında karinanızı yerinde değerlendirir, malzeme ve kullanımınıza en uygun sistemi öneririz.</p>
""",
 },
 "en": {
   "category": "Painting",
   "title": "Choosing Antifouling: How to Pick the Right Paint for Your Boat",
   "excerpt": "Hard matrix or self-polishing? Why your boat's material, speed and water matter when choosing antifouling.",
   "meta_title": "Antifouling Selection Guide | Tekne Usta",
   "meta_desc": "How to choose antifouling paint? The difference between hard matrix and self-polishing, picking the right antifouling for your boat's material and use, plus application tips.",
   "body": """
<p>Antifouling is the paint that protects a boat's underwater surface from marine growth (weed, mussels, barnacles). The wrong choice costs you both performance and money. So how do you pick the right antifouling for your boat?</p>
<h2>Why antifouling matters</h2>
<p>Growth on the hull adds weight, raises fuel consumption and eventually damages the surface. A good antifouling keeps the hull clean through the season.</p>
<h2>Two main types: hard matrix and self-polishing</h2>
<ul>
<li><strong>Hard matrix antifouling:</strong> leaves a hard film that doesn't erode. Suited to high-speed boats, frequently hauled boats and racers. Because build-up accumulates, occasional sanding is needed.</li>
<li><strong>Self-polishing antifouling:</strong> erodes in a controlled way as the boat moves, constantly exposing a fresh surface. Ideal for cruising and low-to-mid-speed boats; less build-up.</li>
</ul>
<h2>Factors that affect the choice</h2>
<ul>
<li><strong>Hull material:</strong> on aluminium boats some copper-based paints cause corrosion; these need copper-free formulas.</li>
<li><strong>Use and speed:</strong> a fast, lightly used boat, or a cruiser constantly under way?</li>
<li><strong>Water character:</strong> warm, nutrient-rich water means more aggressive growth and stronger protection needed.</li>
<li><strong>Previous paint:</strong> new paint must be compatible with the old type; if not, a tie-coat or stripping may be needed.</li>
</ul>
<h2>What to watch in application</h2>
<p>Even the best paint fails with poor application. The surface must be clean, dry and correctly sanded, and the number of coats and the maker's drying times must be respected. Extra coats are recommended at the waterline and on moving surfaces.</p>
<h2>How often to renew?</h2>
<p>For most boats, once a year at the start of the season is ideal. Heavily used boats in warm water may need more frequent care.</p>
<p>If you're unsure which antifouling suits your boat, we'll assess your hull on site under our <a href="/en/services/boat-painting-antifouling/">boat painting and antifouling</a> service and recommend the best system for your material and use.</p>
""",
 },
},
{
 "slug": "gelcoat-yenileme", "slug_en": "gelcoat-renewal",
 "image": "/assets/images/services/fiberglas.jpg", "date": "2026-03-20",
 "tr": {
   "category": "Fiberglas",
   "title": "Gelcoat Yenileme: Solmuş Jelkot Nasıl Parlatılır ve Onarılır?",
   "excerpt": "Jelkot neden solar, çatlar ve matlaşır? Gelcoat parlatma ile yenileme arasındaki fark ve ne zaman hangisinin gerektiği.",
   "meta_title": "Gelcoat Yenileme ve Jelkot Onarımı Rehberi | Tekne Usta",
   "meta_desc": "Gelcoat yenileme, jelkot parlatma ve onarımı: solmuş, çatlamış veya matlaşmış jelkot nasıl geri kazandırılır? Parlatma ile komple yenileme arasındaki fark.",
   "body": """
<p>Jelkot (gelcoat), fiberglas teknenin dış yüzeyindeki renkli ve parlak koruyucu katmandır. Zamanla güneş, tuz ve oksidasyon bu katmanı soldurur, matlaştırır ve çatlatır. İyi haber: çoğu durumda tekneyi baştan boyamaya gerek kalmadan jelkot geri kazandırılabilir.</p>
<h2>Jelkot neden bozulur?</h2>
<ul>
<li><strong>Oksidasyon:</strong> UV ışınları yüzeyi kalksileştirir; parlaklık gider, renk grileşir.</li>
<li><strong>Çizik ve mikro çatlaklar:</strong> Darbe ve gerilim jelkotta örümcek ağı denen ince çatlaklar oluşturur.</li>
<li><strong>Leke ve sararma:</strong> Su hattı lekeleri ve kimyasal temas rengi bozar.</li>
</ul>
<h2>Parlatma mı, yenileme mi?</h2>
<p>Jelkot hâlâ yeterince kalınsa <strong>parlatma (cut &amp; polish)</strong> çoğu zaman yeterlidir: aşındırıcı pasta ve makineyle oksitlenmiş ince tabaka kaldırılır, altındaki sağlam parlak yüzey açığa çıkar. Jelkot fazla incelmiş, derin çatlaklı veya yer yer dökülmüşse <strong>gelcoat yenileme</strong> gerekir: bölgesel dolgu, zımpara ve yeni jelkot/örtücü uygulaması yapılır.</p>
<h2>Renk eşleştirme</h2>
<p>Yaşlanmış beyaz jelkotlar hafif krem tonuna kayar; bu yüzden bölgesel onarımda birebir renk tutturmak zor olabilir. Görünür yüzeylerde, gerektiğinde bölgesel değil komple panel uygulaması öneririz — böylece geçişler belli olmaz.</p>
<h2>Ne zaman boya gerekir?</h2>
<p>Jelkot onarılamayacak kadar yıprandıysa veya renk değiştirmek istiyorsanız, <a href="/hizmetler/tekne-boyama-antifouling/">tekne boyama</a> daha mantıklıdır. Karar için önce ücretsiz keşifte yüzeyin kalınlığını ve durumunu değerlendiririz.</p>
<p>Teknenizin jelkotu soldu, çizildi ya da matlaştıysa <a href="/hizmetler/fiberglas-onarim/">fiberglas onarım</a> hizmetimiz kapsamında yerinde bakalım; parlatma mı yoksa yenileme mi gerektiğini net söyleyelim.</p>
""",
 },
 "en": {
   "category": "Fibreglass",
   "title": "Gelcoat Renewal: How to Polish and Repair Faded Gelcoat",
   "excerpt": "Why does gelcoat fade, crack and go dull? The difference between polishing and renewal, and when each is needed.",
   "meta_title": "Gelcoat Renewal & Repair Guide | Tekne Usta",
   "meta_desc": "Gelcoat renewal, polishing and repair: how to restore faded, cracked or dull gelcoat, and the difference between a cut & polish and a full renewal.",
   "body": """
<p>Gelcoat is the coloured, glossy protective layer on the outside of a fibreglass boat. Over time sun, salt and oxidation fade it, dull it and crack it. The good news: in most cases gelcoat can be restored without repainting the whole boat.</p>
<h2>Why does gelcoat degrade?</h2>
<ul>
<li><strong>Oxidation:</strong> UV chalks the surface; gloss goes and the colour greys.</li>
<li><strong>Scratches and micro-cracks:</strong> impact and stress cause fine "spider" cracks.</li>
<li><strong>Stains and yellowing:</strong> waterline stains and chemical contact spoil the colour.</li>
</ul>
<h2>Polish or renew?</h2>
<p>If the gelcoat is still thick enough, a <strong>cut &amp; polish</strong> is usually enough: an abrasive compound and machine remove the thin oxidised layer, exposing the sound gloss beneath. If the gelcoat has thinned too far, has deep cracks or is flaking, a <strong>gelcoat renewal</strong> is needed: local filling, sanding and fresh gelcoat/topcoat.</p>
<h2>Colour matching</h2>
<p>Aged white gelcoat drifts to a cream tone, so an exact match on a spot repair can be hard. On visible surfaces we recommend a full panel rather than a spot when needed, so transitions don't show.</p>
<h2>When is paint required?</h2>
<p>If the gelcoat is too far gone to repair, or you want to change colour, <a href="/en/services/boat-painting-antifouling/">boat painting</a> makes more sense. We assess thickness and condition at a free survey before deciding.</p>
<p>If your gelcoat has faded, scratched or dulled, let's take a look on site under our <a href="/en/services/fibreglass-repair/">fibreglass repair</a> service and tell you clearly whether polishing or renewal is needed.</p>
""",
 },
},
{
 "slug": "teak-guverte-bakimi", "slug_en": "teak-deck-maintenance",
 "image": "/assets/images/services/ic-mekan.jpg", "date": "2026-04-08",
 "tr": {
   "category": "Teak",
   "title": "Teak Güverte Bakımı: Griye Dönmeden Sıcak Tonu Korumak",
   "excerpt": "Teak neden griye döner, nasıl temizlenir ve yağlanmalı mı? Teak güverteyi yıllarca güzel tutmanın pratik yolları.",
   "meta_title": "Teak Güverte Bakımı ve Temizliği Rehberi | Tekne Usta",
   "meta_desc": "Teak güverte bakımı: teak temizliği, griye dönmeyi önleme, yağlama tartışması ve derz kontrolü. Teakı yıllarca sağlam ve güzel tutmanın yolları.",
   "body": """
<p>Teak güverte, teknenin en güzel ama en çok ilgi isteyen yüzeyidir. Doğru bakımla on yıllar dayanır; ihmal edilirse incelir, derzleri açılır ve su almaya başlar. İşte teakı sağlıklı tutmanın temel ilkeleri.</p>
<h2>Teak neden griye döner?</h2>
<p>Gri renk aslında zarar değil, yüzeydeki doğal yağların UV ile oksitlenmesidir. Estetik olarak istenmese de teakın kendisi sağlamsa griyi hafif bir temizlikle sıcak tona döndürmek mümkündür.</p>
<h2>Nasıl temizlenmeli?</h2>
<ul>
<li><strong>Yumuşak fırçayla, damarın enine değil boyuna</strong> fırçalayın — sert fırça yumuşak yaz damarını aşındırır.</li>
<li>Agresif asitli teak temizleyicilerini abartmayın; teakı hızla inceltirler.</li>
<li>Bol suyla durulayın, derzlerdeki kiri biriktirmeyin.</li>
</ul>
<h2>Teak yağı sürülmeli mi?</h2>
<p>Tartışmalı bir konu: yağ, teaka geçici olarak güzel bir ton verir ama sıcakta yapışkanlaşır, küf tutabilir ve düzenli yenileme ister. Birçok profesyonel, denizde <strong>yağsız bakımı</strong> (düzenli nazik temizlik) tercih eder. Kararı kullanımınıza göre birlikte veririz.</p>
<h2>Derzleri (kalafat) ihmal etmeyin</h2>
<p>Siyah derzler su geçirmezliğin anahtarıdır. Çatlayan, kabaran veya teak seviyesinin altına düşen derzler su sızdırır ve altındaki yapıyı tehdit eder. Derz sorunları büyümeden yenilenmeli.</p>
<p>Teakınız gri, derzleri açılmış veya inceldiyse <a href="/hizmetler/teak-guverte-doseme/">teak güverte döşeme ve yenileme</a> hizmetimiz kapsamında durumu yerinde değerlendirir, bakım mı yoksa yenileme mi gerektiğini söyleriz.</p>
""",
 },
 "en": {
   "category": "Teak",
   "title": "Teak Deck Maintenance: Keeping the Warm Tone Instead of Grey",
   "excerpt": "Why does teak turn grey, how should it be cleaned, and should it be oiled? Practical ways to keep a teak deck beautiful for years.",
   "meta_title": "Teak Deck Maintenance & Cleaning Guide | Tekne Usta",
   "meta_desc": "Teak deck maintenance: cleaning teak, preventing greying, the oiling debate and seam checks. How to keep teak sound and good-looking for years.",
   "body": """
<p>A teak deck is a boat's most beautiful but most demanding surface. With the right care it lasts decades; neglected, it thins, its seams open and it starts to leak. Here are the essentials of keeping teak healthy.</p>
<h2>Why does teak turn grey?</h2>
<p>Grey isn't damage but the natural oils on the surface oxidising under UV. Even if it's not the look you want, as long as the teak itself is sound the grey can be brought back to a warm tone with gentle cleaning.</p>
<h2>How should it be cleaned?</h2>
<ul>
<li>Brush with a soft brush <strong>along the grain, not across it</strong> — a stiff brush erodes the soft summer grain.</li>
<li>Don't overdo aggressive acid teak cleaners; they thin teak fast.</li>
<li>Rinse well and don't let dirt build up in the seams.</li>
</ul>
<h2>Should teak be oiled?</h2>
<p>A debated topic: oil gives teak a lovely tone temporarily, but goes tacky in heat, can hold mould and needs regular renewal. Many professionals prefer <strong>oil-free care</strong> (regular gentle cleaning) at sea. We decide together based on your use.</p>
<h2>Don't neglect the seams</h2>
<p>The black seams are the key to watertightness. Seams that crack, lift or drop below the teak level leak and threaten the structure beneath. They should be renewed before the problem grows.</p>
<p>If your teak is grey, its seams have opened or it has thinned, we'll assess it on site under our <a href="/en/services/teak-deck/">teak decking and renewal</a> service and tell you whether care or renewal is needed.</p>
""",
 },
},
{
 "slug": "tekne-kislatma-kontrol-listesi", "slug_en": "boat-winterising-checklist",
 "image": "/assets/images/services/bakim.jpg", "date": "2026-04-22",
 "tr": {
   "category": "Bakım",
   "title": "Tekne Kışlatma Kontrol Listesi: Sezonu Doğru Kapatmak",
   "excerpt": "Karaya çekmeden örtüye, karina temizliğinden depolamaya — teknenizi kışa hazırlarken atlanmaması gereken adımlar.",
   "meta_title": "Tekne Kışlatma Kontrol Listesi | Tekne Usta",
   "meta_desc": "Tekne kışlatma kontrol listesi: karaya çekme, karina temizliği, örtü, nem ve güvenli depolama. Sezonu doğru kapatıp bahara sağlam çıkmanın adımları.",
   "body": """
<p>İyi bir kışlatma bahar bakımını kısaltır, sürprizleri önler ve teknenin ömrünü uzatır. Aşağıdaki kontrol listesi, sezonu kapatırken atlanmaması gereken temel adımları özetliyor. (Not: motor ve mekanik işlemler uzmanlık alanımız dışında; onlar için güvendiğimiz servislere yönlendiriyoruz.)</p>
<h2>Su altı ve gövde</h2>
<ul>
<li><strong>Karaya çekme ve basınçlı yıkama:</strong> sezon boyunca biriken yosun ve deniz kirini hemen temizleyin — kuruyunca çok daha zor çıkar.</li>
<li><strong>Karina kontrolü:</strong> antifouling durumu, olası osmoz kabarcıkları ve çizikler not edilir; bahar planı buna göre yapılır.</li>
<li><strong>Zinc/anot kontrolü:</strong> tükenmiş anotlar işaretlenir.</li>
</ul>
<h2>Güverte, iç mekan ve nem</h2>
<ul>
<li>İç mekanı boşaltıp <strong>havalandırma</strong> sağlayın; minderleri dik veya evde saklayın.</li>
<li>Nem tutucu ve iyi hava sirkülasyonu küfü önler.</li>
<li>Su tanklarını ve devreleri suyla bırakmayın (donma riski).</li>
</ul>
<h2>Örtü ve depolama</h2>
<ul>
<li><strong>Doğru örtü:</strong> nem hapsetmeyen, havalandırmalı kış muhafaza örtüsü kullanın; sıkı naylon küf yapar.</li>
<li><strong>Güvenli zemin:</strong> tekne düzgün payandalanmalı, yük dengeli dağıtılmalı.</li>
<li><strong>Erken rezervasyon:</strong> çekek alanları hızla dolar; sezon sonunu beklemeyin.</li>
</ul>
<h2>Bahara hazırlık</h2>
<p>Kış boyunca teknenizi takip eder, sezon açılışında karina ve boya durumunu birlikte değerlendiririz. Bahar bakımını önceden planlarsanız suya ilk inenlerden olursunuz.</p>
<p>Kışlatma paketimizin kapsamı için <a href="/hizmetler/tekne-kislatma/">tekne kışlatma</a> sayfamıza bakın; erken rezervasyon için bize yazın.</p>
""",
 },
 "en": {
   "category": "Maintenance",
   "title": "Boat Winterising Checklist: Closing the Season Right",
   "excerpt": "From haul-out to cover, hull cleaning to storage — the steps not to skip when preparing your boat for winter.",
   "meta_title": "Boat Winterising Checklist | Tekne Usta",
   "meta_desc": "Boat winterising checklist: haul-out, hull cleaning, cover, damp control and secure storage. The steps to close the season right and come through spring sound.",
   "body": """
<p>Good winterising shortens spring maintenance, prevents surprises and extends the boat's life. The checklist below sums up the essentials not to skip when closing the season. (Note: engine and mechanical work is outside our expertise; we refer you to trusted services for that.)</p>
<h2>Underwater and hull</h2>
<ul>
<li><strong>Haul-out and pressure wash:</strong> clean off a season's weed and growth straight away — it's far harder once dry.</li>
<li><strong>Hull check:</strong> note antifouling condition, any osmosis blisters and scratches; plan spring accordingly.</li>
<li><strong>Anode check:</strong> flag spent anodes.</li>
</ul>
<h2>Deck, interior and damp</h2>
<ul>
<li>Empty the interior and ensure <strong>ventilation</strong>; stand cushions up or store them at home.</li>
<li>Desiccant and good air circulation prevent mould.</li>
<li>Don't leave water in tanks and circuits (freeze risk).</li>
</ul>
<h2>Cover and storage</h2>
<ul>
<li><strong>The right cover:</strong> use a ventilated winter cover that doesn't trap damp; tight plastic breeds mould.</li>
<li><strong>Secure standing:</strong> the boat must be properly propped with weight evenly distributed.</li>
<li><strong>Book early:</strong> hardstanding fills fast; don't wait for season's end.</li>
</ul>
<h2>Ready for spring</h2>
<p>We keep an eye on your boat through winter and assess hull and paint together at the start of the season. Plan spring maintenance ahead and you'll be among the first afloat.</p>
<p>For what our package covers see our <a href="/en/services/winterising-storage/">boat winterising</a> page; message us to book early.</p>
""",
 },
},
{
 "slug": "tekne-boyama-maliyeti", "slug_en": "boat-painting-cost",
 "image": "/assets/images/services/boya.jpg", "date": "2026-05-06",
 "tr": {
   "category": "Boya",
   "title": "Tekne Boyama Maliyetini Ne Belirler? Şeffaf Bir Rehber",
   "excerpt": "Tekne boyama fiyatı neye göre değişir? Yüzey hazırlığı, kat sayısı, boya sistemi ve tekne boyunun maliyete etkisi.",
   "meta_title": "Tekne Boyama Fiyatını Ne Belirler? Maliyet Rehberi | Tekne Usta",
   "meta_desc": "Tekne boyama maliyetini belirleyen faktörler: yüzey hazırlığı, kat sayısı, boya sistemi, tekne boyu ve antifouling. Şeffaf fiyatlandırma nasıl olmalı?",
   "body": """
<p>"Tekne boyama ne kadar?" sorusunun tek bir cevabı yoktur — ama fiyatı neyin belirlediğini anlarsanız, aldığınız teklifi doğru değerlendirir ve ucuz görünüp sonradan kabaran işlerden kaçınırsınız.</p>
<h2>Maliyeti belirleyen ana faktörler</h2>
<ul>
<li><strong>Tekne boyu ve yüzey alanı:</strong> Boya ve işçilik doğrudan alanla ölçeklenir.</li>
<li><strong>Yüzey hazırlığının kapsamı:</strong> Maliyetin çoğu boyada değil hazırlıktadır — zımpara, dolgu, astar. Eski boyanın sökülmesi gerekiyorsa iş büyür.</li>
<li><strong>Boya sistemi:</strong> Tek katlı bir yenileme ile çok katlı iki-bileşenli (2K) poliüretan sistemi çok farklı fiyatlardadır. 2K sistemler pahalıdır ama uzun ömürlü ve parlaktır.</li>
<li><strong>Antifouling mi, dış cephe mi?</strong> Sadece su altı <a href="/hizmetler/tekne-boyama-antifouling/">antifouling</a> yenilemesi, komple dış cephe boyamasından çok daha kısa ve ucuzdur.</li>
<li><strong>Renk ve grafik:</strong> Renk değişimi, kılavuz şerit ve grafikler ek maskeleme ve işçilik demektir.</li>
</ul>
<h2>Ucuz teklif neden pahalıya patlar?</h2>
<p>Yüzey hazırlığından kısan bir iş kısa sürede kabarır, dökülür ve baştan yapılması gerekir. Kalıcı bir boya işinin sırrı görünmeyen adımlardadır: doğru zımpara, doğru astar, üreticinin kuruma sürelerine uyum. Bu yüzden teklifleri sadece rakama göre değil, <strong>kapsamına göre</strong> karşılaştırın.</p>
<h2>Şeffaf fiyat nasıl olmalı?</h2>
<p>İyi bir teklif kalem kalemdir: hazırlık, astar, boya sistemi, kat sayısı ve işçilik ayrı ayrı görünür. Biz keşif sonrası bu formatta yazılı teklif veririz; sürpriz fatura çıkarmayız.</p>
<p>Tekneniz için net bir fiyat mı istiyorsunuz? <a href="/hizmetler/tekne-boyama-antifouling/">Tekne boyama ve antifouling</a> hizmetimiz kapsamında ücretsiz keşifle yüzeyi görüp kalem kalem teklif sunalım.</p>
""",
 },
 "en": {
   "category": "Painting",
   "title": "What Determines Boat Painting Cost? A Transparent Guide",
   "excerpt": "What makes boat painting cost vary? How surface prep, coat count, paint system and boat length affect the price.",
   "meta_title": "What Determines Boat Painting Cost? A Guide | Tekne Usta",
   "meta_desc": "Factors that determine boat painting cost: surface prep, number of coats, paint system, boat length and antifouling. What transparent pricing should look like.",
   "body": """
<p>"How much is boat painting?" has no single answer — but if you understand what drives the price, you can judge a quote properly and avoid cheap-looking jobs that blister later.</p>
<h2>The main cost factors</h2>
<ul>
<li><strong>Boat length and surface area:</strong> paint and labour scale directly with area.</li>
<li><strong>Extent of surface prep:</strong> most of the cost is in prep, not paint — sanding, filling, priming. If the old paint must be stripped, the job grows.</li>
<li><strong>Paint system:</strong> a single-coat refresh and a multi-coat two-part (2K) polyurethane system are very different prices. 2K systems cost more but last longer and shine.</li>
<li><strong>Antifouling or topside?</strong> A below-waterline <a href="/en/services/boat-painting-antifouling/">antifouling</a> refresh is much shorter and cheaper than a full topside repaint.</li>
<li><strong>Colour and graphics:</strong> a colour change, boot stripe and graphics mean extra masking and labour.</li>
</ul>
<h2>Why a cheap quote costs more</h2>
<p>A job that skimps on prep soon blisters, flakes and has to be redone. The secret to a lasting paint job is in the invisible steps: correct sanding, the right primer, respecting drying times. So compare quotes by <strong>scope, not just the number</strong>.</p>
<h2>What transparent pricing looks like</h2>
<p>A good quote is itemised: prep, primer, paint system, coat count and labour shown separately. We give a written quote in this format after the survey — no surprise invoices.</p>
<p>Want a clear price for your boat? Under our <a href="/en/services/boat-painting-antifouling/">boat painting and antifouling</a> service we'll inspect the surface at a free survey and give an itemised quote.</p>
""",
 },
},
{
 "slug": "osmoz-belirtileri", "slug_en": "osmosis-symptoms",
 "image": "/assets/images/services/fiberglas.jpg", "date": "2026-05-20",
 "tr": {
   "category": "Fiberglas",
   "title": "Teknemde Osmoz Var mı? 5 Belirti ve Basit Kontrol",
   "excerpt": "Osmozu erken yakalamak masrafı düşürür. Fiber teknenizde osmoz olup olmadığını gösteren belirtiler ve kendi yapabileceğiniz kontrol.",
   "meta_title": "Osmoz Belirtileri: Teknemde Osmoz Var mı? | Tekne Usta",
   "meta_desc": "Fiber teknede osmoz belirtileri: kabarcık, koku, nem ve matlaşma. Osmozu erken yakalamak için basit kontrol adımları ve ne zaman uzmana danışmalı.",
   "body": """
<p>Osmoz sinsi ilerler; erken yakalanırsa küçük bir müdahaleyle çözülür, gecikince karina baştan elden geçer. İşte teknenizde osmoz olup olmadığını anlamanıza yardımcı belirtiler.</p>
<h2>1. Su altında kabarcıklar</h2>
<p>En klasik belirti, tekne karadayken su altı yüzeyde beliren küçük kabarcıklardır. Parmakla bastırıldığında yumuşak veya içi dolu hissedilebilir.</p>
<h2>2. Ekşi koku</h2>
<p>Bir kabarcık delindiğinde çıkan sıvı sirke/ekşi kokuluysa bu osmozun güçlü işaretidir. Bu, laminatta gerçekleşen kimyasal tepkimenin ürünüdür.</p>
<h2>3. Nem ve matlaşma</h2>
<p>Jelkotta yer yer nem izleri, matlaşma ve renk farkı görünüyorsa yüzeyin altında su hareketi olabilir.</p>
<h2>4. Yüzey düzgünsüzlüğü</h2>
<p>Elinizi su altı yüzeyde gezdirdiğinizde hissedilen tümsekler, henüz gözle görünmeyen kabarcıkların habercisi olabilir.</p>
<h2>5. Nem ölçer değeri</h2>
<p>Kesin sonuç için profesyoneller nem ölçer (moisture meter) kullanır. Yüksek nem, gözle görünür kabarcık olmasa bile risk demektir.</p>
<h2>Ne yapmalı?</h2>
<p>Bir-iki küçük kabarcık panik sebebi değildir ama takip edilmelidir. Yaygınlaşan kabarcık ve yüksek nem varsa tedavi zamanı gelmiştir. Osmozun nasıl tedavi edildiğini <a href="/blog/osmoz-nedir-tedavisi/">osmoz tedavisi rehberimizde</a> anlattık. Emin olmak için <a href="/hizmetler/fiberglas-onarim/">fiberglas onarım</a> hizmetimiz kapsamında ücretsiz keşif ve nem ölçümü yapıyoruz.</p>
""",
 },
 "en": {
   "category": "Fibreglass",
   "title": "Does My Boat Have Osmosis? 5 Signs and a Simple Check",
   "excerpt": "Catching osmosis early lowers the cost. The signs that tell you whether your fibreglass boat has osmosis, and a check you can do yourself.",
   "meta_title": "Osmosis Symptoms: Does My Boat Have Osmosis? | Tekne Usta",
   "meta_desc": "Osmosis symptoms on a fibreglass boat: blisters, smell, moisture and dullness. Simple checks to catch osmosis early and when to consult a professional.",
   "body": """
<p>Osmosis advances quietly; caught early it's a small job, left late the whole hull needs work. Here are the signs that help you tell whether your boat has osmosis.</p>
<h2>1. Blisters below the waterline</h2>
<p>The classic sign is small blisters on the underwater surface when the boat is ashore. Pressed with a finger they may feel soft or fluid-filled.</p>
<h2>2. A sour smell</h2>
<p>If the fluid from a pierced blister smells of vinegar, that's a strong sign of osmosis — the product of the chemical reaction in the laminate.</p>
<h2>3. Moisture and dullness</h2>
<p>Patchy moisture marks, dullness and colour variation in the gelcoat can mean water is moving beneath the surface.</p>
<h2>4. Surface unevenness</h2>
<p>Bumps you feel running a hand over the underwater surface can herald blisters not yet visible to the eye.</p>
<h2>5. Moisture-meter reading</h2>
<p>For a definitive answer professionals use a moisture meter. High moisture means risk even without visible blisters.</p>
<h2>What to do</h2>
<p>One or two small blisters aren't cause for panic but should be monitored. Widespread blistering and high moisture mean it's time to treat. We explain how osmosis is treated in our <a href="/en/blog/what-is-osmosis-treatment/">osmosis treatment guide</a>. To be sure, we offer a free survey and moisture reading under our <a href="/en/services/fibreglass-repair/">fibreglass repair</a> service.</p>
""",
 },
},
{
 "slug": "fiber-mi-ahsap-tekne", "slug_en": "fibreglass-vs-wooden-boat",
 "image": "/assets/images/parallax-2.jpg", "date": "2026-06-03",
 "tr": {
   "category": "Rehber",
   "title": "Fiber mi Ahşap Tekne mi? Bakım Açısından Karşılaştırma",
   "excerpt": "Fiber ve ahşap teknelerin bakım yükü, maliyeti ve dayanıklılığı nasıl farklılaşır? Tekne alırken veya sahipken bilmeniz gerekenler.",
   "meta_title": "Fiber mi Ahşap Tekne mi? Bakım Karşılaştırması | Tekne Usta",
   "meta_desc": "Fiber ve ahşap tekne karşılaştırması: bakım yükü, maliyet, dayanıklılık ve karakter. Tekne alırken veya sahipken hangi malzemenin size uygun olduğu.",
   "body": """
<p>"Fiber mi alsam, ahşap mı?" — tekne dünyasının klasik sorusu. Her ikisinin de yeri var; doğru seçim beklentinize ve bakıma ayırabileceğiniz zamana bağlı. İşte bakım gözünden dürüst bir karşılaştırma.</p>
<h2>Fiberglas tekneler</h2>
<p><strong>Artıları:</strong> Daha düşük rutin bakım, suya dayanıklı, geniş ikinci el pazarı. <strong>Dikkat:</strong> Zamanla <a href="/blog/osmoz-nedir-tedavisi/">osmoz</a>, gelcoat solması ve çatlaklar görülebilir; ama bunlar yönetilebilir işlerdir.</p>
<h2>Ahşap tekneler</h2>
<p><strong>Artıları:</strong> Eşsiz karakter, onarılabilirlik, klasik değer. <strong>Dikkat:</strong> Düzenli <a href="/blog/ahsap-tekne-vernik-bakimi/">vernik ve kalafat bakımı</a> ister; ihmal edildiğinde çürük ve su alma riski artar. Doğru bakılırsa nesiller boyu yaşar.</p>
<h2>Maliyet ve zaman</h2>
<p>Fiber tekne genelde daha az yıllık bakım saati ister; ahşap tekne ise düzenli ilgi bekler ama malzeme onarımı çoğu zaman mümkündür. Yani ahşap "daha masraflı" değil, "daha ilgi isteyen"dir.</p>
<h2>Hangisi size uygun?</h2>
<p>Az vakitle çok denize çıkmak istiyorsanız fiber; teknenizle ilgilenmekten keyif alıyor ve karakter arıyorsanız ahşap mantıklı. Her iki malzemede de <a href="/hizmetler/fiberglas-onarim/">fiberglas</a> ve <a href="/hizmetler/ahsap-tekne-renovasyonu/">ahşap renovasyon</a> hizmetlerimizle yanınızdayız.</p>
""",
 },
 "en": {
   "category": "Guide",
   "title": "Fibreglass or Wooden Boat? A Maintenance Comparison",
   "excerpt": "How do the maintenance burden, cost and durability of fibreglass and wooden boats differ? What to know when buying or owning.",
   "meta_title": "Fibreglass or Wooden Boat? Maintenance Comparison | Tekne Usta",
   "meta_desc": "Fibreglass vs wooden boat comparison: maintenance burden, cost, durability and character. Which material suits you when buying or owning a boat.",
   "body": """
<p>"Fibreglass or wood?" — a classic question in the boating world. Both have their place; the right choice depends on your expectations and the time you can give to care. Here's an honest comparison from a maintenance viewpoint.</p>
<h2>Fibreglass boats</h2>
<p><strong>Pros:</strong> lower routine maintenance, water-resistant, a wide used market. <strong>Watch for:</strong> over time <a href="/en/blog/what-is-osmosis-treatment/">osmosis</a>, gelcoat fading and cracks can appear; but these are manageable jobs.</p>
<h2>Wooden boats</h2>
<p><strong>Pros:</strong> unique character, repairability, classic value. <strong>Watch for:</strong> regular <a href="/en/blog/wooden-boat-varnish-care/">varnish and caulking care</a>; neglected, the risk of rot and leaks grows. Cared for properly, they last generations.</p>
<h2>Cost and time</h2>
<p>A fibreglass boat generally needs fewer annual maintenance hours; a wooden boat expects regular attention but material repair is usually possible. So wood isn't "more expensive," it's "more attention-hungry."</p>
<h2>Which suits you?</h2>
<p>If you want maximum time on the water with minimal fuss, fibreglass; if you enjoy caring for your boat and want character, wood makes sense. We support both with our <a href="/en/services/fibreglass-repair/">fibreglass</a> and <a href="/en/services/wooden-boat-refit/">wooden refit</a> services.</p>
""",
 },
},
{
 "slug": "ahsap-tekne-vernik-bakimi", "slug_en": "wooden-boat-varnish-care",
 "image": "/assets/images/services/ahsap.jpg", "date": "2026-06-17",
 "tr": {
   "category": "Ahşap",
   "title": "Ahşap Tekne Vernik Bakımı: Parlaklığı Yıllarca Korumak",
   "excerpt": "Vernik neden çatlar ve sararır? Kaç kat gerekir, ne sıklıkla yenilenir ve arada bakım nasıl yapılır?",
   "meta_title": "Ahşap Tekne Vernik Bakımı Rehberi | Tekne Usta",
   "meta_desc": "Ahşap tekne vernik bakımı: kat sayısı, yenileme sıklığı, ara bakım ve doğru zemin hazırlığı. Verniğin parlaklığını yıllarca korumanın yolları.",
   "body": """
<p>Vernikli ahşap, bir teknenin en etkileyici detayıdır — ama en çok emek isteyen yüzeydir. Doğru uygulama ve düzenli bakımla o derinlikli parlaklık yıllarca korunur.</p>
<h2>Vernik neden bozulur?</h2>
<p>Güneşin UV ışınları verniği zamanla çatlatır, matlaştırır ve sarartır. Çatlaklardan giren su ahşabı karartır. Bu yüzden vernik, dökülene kadar beklemeden, ince aşınma aşamasında yenilenmelidir.</p>
<h2>Kaç kat gerekir?</h2>
<p>Denizde kalıcı bir sonuç için genellikle çok sayıda ince kat (çoğu profesyonel 6–10 kat) tercih edilir. Her kat hafif zımparalanır; zemin ne kadar iyi hazırlanırsa parlaklık o kadar derin ve dayanıklı olur.</p>
<h2>Ara bakım</h2>
<p>Vernik henüz sağlamken yılda bir-iki kez atılan bir <strong>koruma katı</strong>, komple soymayı yıllarca erteler. İhmal edilirse tek çare baştan zımpara ve yeniden verniklemedir.</p>
<h2>Ne zaman komple yenileme?</h2>
<p>Vernik geniş alanda çatladıysa, karardıysa veya soyulmaya başladıysa bölgesel dokunuş yetmez; yüzey ahşaba kadar açılıp yeniden kurulur. Bu işi <a href="/hizmetler/ahsap-tekne-renovasyonu/">ahşap tekne renovasyonu</a> hizmetimiz kapsamında yapıyoruz.</p>
<p>Ahşabın bakımı hakkında daha fazlası için <a href="/blog/fiber-mi-ahsap-tekne/">fiber mi ahşap mı</a> yazımıza da bakabilirsiniz.</p>
""",
 },
 "en": {
   "category": "Wood",
   "title": "Wooden Boat Varnish Care: Keeping the Shine for Years",
   "excerpt": "Why does varnish crack and yellow? How many coats are needed, how often to renew, and how to maintain between refits?",
   "meta_title": "Wooden Boat Varnish Care Guide | Tekne Usta",
   "meta_desc": "Wooden boat varnish care: coat count, renewal frequency, maintenance coats and proper surface prep. How to keep varnish glossy for years.",
   "body": """
<p>Varnished wood is a boat's most striking detail — and its most labour-intensive surface. With correct application and regular care, that deep shine lasts for years.</p>
<h2>Why does varnish break down?</h2>
<p>The sun's UV cracks, dulls and yellows varnish over time. Water entering the cracks darkens the wood. So varnish should be renewed at the thin-wear stage, not left until it flakes.</p>
<h2>How many coats?</h2>
<p>For a lasting result at sea, many thin coats are preferred (most professionals use 6–10). Each coat is lightly sanded; the better the base is prepared, the deeper and more durable the shine.</p>
<h2>Maintenance coats</h2>
<p>A <strong>maintenance coat</strong> once or twice a year while the varnish is still sound postpones a full strip for years. Neglected, the only remedy is sanding back and re-varnishing.</p>
<h2>When is a full renewal needed?</h2>
<p>If the varnish has cracked widely, darkened or begun to peel, a spot touch-up won't do; the surface is taken back to bare wood and rebuilt. We do this under our <a href="/en/services/wooden-boat-refit/">wooden boat refit</a> service.</p>
<p>For more on wood care, see our <a href="/en/blog/fibreglass-vs-wooden-boat/">fibreglass or wood</a> article.</p>
""",
 },
},
{
 "slug": "antifouling-uygulama-hatalari", "slug_en": "antifouling-mistakes",
 "image": "/assets/images/services/boya.jpg", "date": "2026-07-01",
 "tr": {
   "category": "Boya",
   "title": "Antifouling Uygulamasında En Sık Yapılan 6 Hata",
   "excerpt": "Yanlış ürün, kötü hazırlık, hatalı zamanlama... Antifouling'in erken bitmesine yol açan ve önlenebilir hatalar.",
   "meta_title": "Antifouling Uygulama Hataları: Kaçınılması Gerekenler | Tekne Usta",
   "meta_desc": "Antifouling uygulamasında sık yapılan hatalar: uyumsuz ürün, kötü yüzey hazırlığı, yetersiz kat ve yanlış zamanlama. Zehirli boyanın ömrünü uzatmanın yolları.",
   "body": """
<p>İyi bir antifouling bir sezon boyu karinayı temiz tutar; kötü uygulanmış bir antifouling ise birkaç ayda dökülür. İşte en sık görülen ve tamamen önlenebilir hatalar.</p>
<h2>1. Uyumsuz ürün seçmek</h2>
<p>Eski boyayla kimyasal olarak uyumsuz yeni boya, kısa sürede kabarır ve soyulur. Doğru ürün için önce mevcut sistemi bilmek gerekir.</p>
<h2>2. Yüzey hazırlığını atlamak</h2>
<p>Kirli, yağlı veya iyi zımparalanmamış yüzeye atılan boya tutmaz. İşin kalitesi görünmeyen bu adımda belli olur.</p>
<h2>3. Yanlış kat sayısı</h2>
<p>Yetersiz kat, özellikle su hattı ve baş bodoslamada erken aşınır. Üreticinin önerdiği kat sayısına uymak şarttır.</p>
<h2>4. Yanlış zamanlama</h2>
<p>Nemli havada veya suya inmeden hemen önce atılan boya doğru kürlenmez. Kuruma ve suya iniş aralığı üreticinin talimatına göre olmalıdır.</p>
<h2>5. Anotları boyamak</h2>
<p>Zinc anotların üzerine boya gelirse görevini yapamaz ve galvanik korozyon başlar.</p>
<h2>6. Malzemeyi göz ardı etmek</h2>
<p>Alüminyum teknelerde bakırlı boya korozyona yol açar; bu teknelerde bakırsız formül gerekir.</p>
<p>Bu hatalardan kaçınmak için doğru sistem seçimi ve titiz uygulama şart. <a href="/hizmetler/tekne-boyama-antifouling/">Tekne boyama ve antifouling</a> hizmetimiz kapsamında karinanızı değerlendirir, doğru ürünü öneririz. Hangi tip antifouling için <a href="/blog/antifouling-secimi/">seçim rehberimize</a> bakın.</p>
""",
 },
 "en": {
   "category": "Painting",
   "title": "The 6 Most Common Antifouling Application Mistakes",
   "excerpt": "Wrong product, poor prep, bad timing... The preventable mistakes that make antifouling fail early.",
   "meta_title": "Antifouling Application Mistakes to Avoid | Tekne Usta",
   "meta_desc": "Common antifouling mistakes: incompatible product, poor surface prep, too few coats and bad timing. How to make antifouling last a full season.",
   "body": """
<p>Good antifouling keeps the hull clean for a season; poorly applied, it flakes within months. Here are the most common — and entirely preventable — mistakes.</p>
<h2>1. Choosing an incompatible product</h2>
<p>New paint that's chemically incompatible with the old blisters and peels quickly. Choosing the right product means knowing the existing system first.</p>
<h2>2. Skipping surface prep</h2>
<p>Paint won't hold on a dirty, greasy or poorly sanded surface. Quality shows in this invisible step.</p>
<h2>3. The wrong number of coats</h2>
<p>Too few coats wear early, especially at the waterline and stem. Following the maker's coat count is essential.</p>
<h2>4. Bad timing</h2>
<p>Paint applied in damp weather or just before launch doesn't cure properly. The dry-and-launch window must follow the maker's instructions.</p>
<h2>5. Painting the anodes</h2>
<p>Paint over zinc anodes stops them working and galvanic corrosion begins.</p>
<h2>6. Ignoring the material</h2>
<p>Copper-based paint on aluminium boats causes corrosion; these need a copper-free formula.</p>
<p>Avoiding these mistakes takes the right system and careful application. Under our <a href="/en/services/boat-painting-antifouling/">boat painting and antifouling</a> service we assess your hull and recommend the right product. For which type to choose, see our <a href="/en/blog/choosing-antifouling/">selection guide</a>.</p>
""",
 },
},
{
 "slug": "yillik-tekne-bakim-takvimi", "slug_en": "annual-boat-maintenance-calendar",
 "image": "/assets/images/services/bakim.jpg", "date": "2026-07-15",
 "tr": {
   "category": "Bakım",
   "title": "Yıllık Tekne Bakım Takvimi: Mevsim Mevsim Ne Yapılmalı?",
   "excerpt": "İlkbahardan kışa, teknenizin sezon boyunca ihtiyaç duyduğu bakımların basit bir takvimi.",
   "meta_title": "Yıllık Tekne Bakım Takvimi | Tekne Usta",
   "meta_desc": "Yıllık tekne bakım takvimi: ilkbahar hazırlığı, yaz kontrolleri, sonbahar kışlatma ve kış depolama. Mevsim mevsim tekne bakımı kontrol listesi.",
   "body": """
<p>Düzenli bakım, büyük onarımların en iyi ilacıdır. İşte teknenizi yıl boyu sağlıklı tutacak mevsimlik bir yol haritası. (Not: motor/mekanik bakımlar uzmanlık alanımız dışında; onlar için servis yönlendirmesi yapabiliriz.)</p>
<h2>İlkbahar — sezona hazırlık</h2>
<ul>
<li>Karina kontrolü ve gerekiyorsa <a href="/hizmetler/tekne-boyama-antifouling/">antifouling</a> yenileme</li>
<li>Gelcoat/boya kontrolü, çizik ve <a href="/blog/osmoz-belirtileri/">osmoz belirtisi</a> taraması</li>
<li>Suya iniş öncesi genel gözden geçirme</li>
</ul>
<h2>Yaz — sezon içi kontrol</h2>
<ul>
<li>Su hattı ve karinada erken kirlenme kontrolü</li>
<li>Teak ve dış ahşapta güneş yıpranması takibi</li>
<li>Küçük hasarların büyümeden onarımı</li>
</ul>
<h2>Sonbahar — kışlatma</h2>
<ul>
<li>Karaya çekme, basınçlı yıkama ve karina değerlendirmesi</li>
<li><a href="/blog/tekne-kislatma-kontrol-listesi/">Kışlatma kontrol listesi</a>nin uygulanması</li>
<li>Nem ve küfü önleyen havalandırmalı örtü</li>
</ul>
<h2>Kış — planlama ve büyük işler</h2>
<ul>
<li>Kapsamlı <a href="/hizmetler/fiberglas-onarim/">fiberglas</a> veya <a href="/hizmetler/ahsap-tekne-renovasyonu/">ahşap renovasyon</a> için en uygun dönem</li>
<li>Bahar bakımını önceden planlayıp erken suya iniş</li>
</ul>
<p>Teknenize özel bir bakım planı için <a href="/hizmetler/tekne-kislatma/">kışlatma ve bakım</a> hizmetimiz kapsamında ücretsiz keşif yapalım.</p>
""",
 },
 "en": {
   "category": "Maintenance",
   "title": "Annual Boat Maintenance Calendar: What to Do, Season by Season",
   "excerpt": "From spring to winter, a simple calendar of the care your boat needs through the season.",
   "meta_title": "Annual Boat Maintenance Calendar | Tekne Usta",
   "meta_desc": "Annual boat maintenance calendar: spring prep, summer checks, autumn winterising and winter storage. A season-by-season boat maintenance checklist.",
   "body": """
<p>Regular maintenance is the best cure for big repairs. Here's a seasonal roadmap to keep your boat healthy year-round. (Note: engine/mechanical care is outside our scope; we can refer you to a service for that.)</p>
<h2>Spring — season prep</h2>
<ul>
<li>Hull check and, if needed, <a href="/en/services/boat-painting-antifouling/">antifouling</a> renewal</li>
<li>Gelcoat/paint check, scanning for scratches and <a href="/en/blog/osmosis-symptoms/">osmosis signs</a></li>
<li>General review before launch</li>
</ul>
<h2>Summer — in-season checks</h2>
<ul>
<li>Watch for early growth at the waterline and hull</li>
<li>Monitor sun wear on teak and exterior wood</li>
<li>Repair small damage before it grows</li>
</ul>
<h2>Autumn — winterising</h2>
<ul>
<li>Haul-out, pressure wash and hull assessment</li>
<li>Working through the <a href="/en/blog/boat-winterising-checklist/">winterising checklist</a></li>
<li>A ventilated cover that prevents damp and mould</li>
</ul>
<h2>Winter — planning and big jobs</h2>
<ul>
<li>The best time for extensive <a href="/en/services/fibreglass-repair/">fibreglass</a> or <a href="/en/services/wooden-boat-refit/">wooden refit</a></li>
<li>Plan spring maintenance ahead for an early launch</li>
</ul>
<p>For a maintenance plan tailored to your boat, let's do a free survey under our <a href="/en/services/winterising-storage/">winterising and maintenance</a> service.</p>
""",
 },
},
{
 "slug": "satin-alma-oncesi-tekne-ekspertizi", "slug_en": "pre-purchase-boat-survey",
 "image": "/assets/images/hakkimizda.jpg", "date": "2026-07-22",
 "tr": {
   "category": "Rehber",
   "title": "İkinci El Tekne Alırken: Satın Alma Öncesi Nelere Bakılmalı?",
   "excerpt": "İkinci el tekne alırken gözden kaçan pahalı sorunlar. Fiberglas, ahşap, karina ve güvertede kontrol edilecekler.",
   "meta_title": "Satın Alma Öncesi Tekne Kontrolü Rehberi | Tekne Usta",
   "meta_desc": "İkinci el tekne alırken satın alma öncesi kontrol: fiberglas ve osmoz, ahşap çürük, karina, güverte ve teak. Pahalı sürprizlerden kaçınmanın yolları.",
   "body": """
<p>İkinci el tekne, doğru seçilirse harika bir yatırımdır; ama görünmeyen sorunlar sonradan cebi ciddi yorabilir. Satın almadan önce şu noktaları kontrol edin (veya bir uzmana kontrol ettirin).</p>
<h2>Fiberglas gövde</h2>
<p>Su altı yüzeyde <a href="/blog/osmoz-belirtileri/">osmoz belirtileri</a>, gelcoat çatlakları ve önceki onarım izlerine bakın. Nem ölçer değeri yüksekse pazarlıkta bunu göz önünde bulundurun.</p>
<h2>Ahşap gövde</h2>
<p>Güverte ve gövde birleşimlerinde yumuşama, kararma ve çürük belirtileri kritik. Kalafat ve verniğin durumu bakım yükünü gösterir.</p>
<h2>Karina ve su hattı</h2>
<p>Kaç kat antifouling birikmiş, karina düzgün mü, çarpma/onarım izi var mı? Kalın boya katmanları ve gizlenmiş onarımlar dikkat ister.</p>
<h2>Güverte ve teak</h2>
<p>Teakın kalınlığı, derzlerin durumu ve güvertede yumuşak (su almış) bölgeler önemli. Islak güverte pahalı bir onarım demektir.</p>
<h2>Neden uzman kontrolü?</h2>
<p>Deneyimli bir göz, gözden kaçan sorunları fiyata yansımadan önce görür ve pazarlıkta elinizi güçlendirir. <a href="/hizmetler/fiberglas-onarim/">Fiberglas</a> ve <a href="/hizmetler/ahsap-tekne-renovasyonu/">ahşap</a> tarafında durum değerlendirmesi yapıyoruz — almayı düşündüğünüz tekne için bize yazın, birlikte bakalım.</p>
""",
 },
 "en": {
   "category": "Guide",
   "title": "Buying a Used Boat: What to Check Before You Buy",
   "excerpt": "The costly problems overlooked when buying a used boat. What to check in fibreglass, wood, hull and deck.",
   "meta_title": "Pre-Purchase Boat Check Guide | Tekne Usta",
   "meta_desc": "Pre-purchase checks when buying a used boat: fibreglass and osmosis, wood rot, hull, deck and teak. How to avoid expensive surprises.",
   "body": """
<p>A used boat, chosen well, is a great investment; but hidden problems can hit the wallet hard later. Before you buy, check these points (or have an expert check them).</p>
<h2>Fibreglass hull</h2>
<p>Look for <a href="/en/blog/osmosis-symptoms/">osmosis signs</a>, gelcoat cracks and traces of previous repairs on the underwater surface. If the moisture reading is high, factor it into the negotiation.</p>
<h2>Wooden hull</h2>
<p>Softness, darkening and rot at deck and hull joints are critical. The state of caulking and varnish shows the maintenance burden.</p>
<h2>Hull and waterline</h2>
<p>How many antifouling layers have built up, is the hull fair, are there impact or repair marks? Thick paint layers and hidden repairs deserve attention.</p>
<h2>Deck and teak</h2>
<p>Teak thickness, seam condition and soft (water-ingressed) areas on deck matter. A wet deck means an expensive repair.</p>
<h2>Why an expert check?</h2>
<p>An experienced eye spots overlooked problems before they hit your wallet and strengthens your hand in negotiation. We assess condition on the <a href="/en/services/fibreglass-repair/">fibreglass</a> and <a href="/en/services/wooden-boat-refit/">wood</a> side — message us about the boat you're considering and let's look together.</p>
""",
 },
},
{
 "slug": "osmoz-tedavisi-fiyatlari", "slug_en": "osmosis-treatment-cost",
 "image": "/assets/images/services/fiberglas.jpg", "date": "2026-08-05",
 "tr": {
   "category": "Fiberglas",
   "title": "Osmoz Tedavisi Fiyatını Ne Belirler? Maliyet Rehberi",
   "excerpt": "Osmoz tedavisi neden sabit fiyatlı değildir? Tekne boyu, hasarın yaygınlığı ve kurutma süresinin maliyete etkisi.",
   "meta_title": "Osmoz Tedavisi Fiyatını Ne Belirler? | Tekne Usta",
   "meta_desc": "Osmoz tedavisi fiyatını belirleyen faktörler: tekne boyu, hasarın yaygınlığı, kurutma süresi ve bariyer kat sistemi. Şeffaf fiyatlandırma nasıl olmalı?",
   "body": """
<p>"Osmoz tedavisi ne kadar?" sorusuna dürüst cevap: değişir. Ama neyin değiştirdiğini bilirsen, aldığın teklifi doğru değerlendirir ve ucuz görünüp yarım kalan işlerden kaçınırsın.</p>
<h2>Maliyeti belirleyen faktörler</h2>
<ul>
<li><strong>Tekne boyu ve yüzey alanı:</strong> İşlem su altı alanla ölçeklenir.</li>
<li><strong>Hasarın yaygınlığı:</strong> Birkaç bölgesel kabarcık ile komple etkilenmiş bir karina çok farklıdır.</li>
<li><strong>Kurutma süresi:</strong> En değişken kalem. Laminat tam kuruyana kadar beklemek gerekir; bu iklime ve nem seviyesine bağlıdır.</li>
<li><strong>Bariyer kat sistemi:</strong> Kaç kat epoksi ve hangi ürün kullanıldığı fiyatı etkiler.</li>
</ul>
<h2>Neden sabit fiyat verilemez?</h2>
<p>Osmozda işin çoğu kurutmadır ve kurutma süresi baştan kesin bilinemez. Nem ölçmeden "şu kadar" diyen bir teklif ya işi eksik yapacaktır ya da riski fiyata şişirmiştir. Doğru yaklaşım, keşifte nem ölçümü yapıp gerçekçi bir aralık vermektir.</p>
<h2>Ucuz teklifin gizli maliyeti</h2>
<p>Kurutmayı beklemeden bariyer kat atan bir iş, nemi içeri hapseder ve 1-2 sezon içinde osmoz geri döner. Yani en pahalı osmoz tedavisi, iki kez yapılandır.</p>
<p>Teknenizin durumunu net görmek için <a href="/hizmetler/fiberglas-onarim/">fiberglas onarım</a> hizmetimiz kapsamında ücretsiz keşif ve nem ölçümü yapıp kalem kalem teklif veriyoruz. Osmozun ne olduğunu <a href="/blog/osmoz-nedir-tedavisi/">osmoz rehberimizde</a>, belirtilerini ise <a href="/blog/osmoz-belirtileri/">bu yazıda</a> anlattık.</p>
""",
 },
 "en": {
   "category": "Fibreglass",
   "title": "What Determines Osmosis Treatment Cost? A Guide",
   "excerpt": "Why isn't osmosis treatment a fixed price? How boat length, extent of damage and drying time affect the cost.",
   "meta_title": "What Determines Osmosis Treatment Cost? | Tekne Usta",
   "meta_desc": "Factors that determine osmosis treatment cost: boat length, extent of damage, drying time and barrier-coat system. What transparent pricing should look like.",
   "body": """
<p>The honest answer to "how much is osmosis treatment?" is: it depends. But if you know what changes it, you can judge a quote properly and avoid cheap-looking jobs that end up half-done.</p>
<h2>Factors that set the cost</h2>
<ul>
<li><strong>Boat length and surface area:</strong> the job scales with the underwater area.</li>
<li><strong>Extent of damage:</strong> a few local blisters and a fully affected hull are very different.</li>
<li><strong>Drying time:</strong> the most variable item. The laminate must dry completely; this depends on climate and moisture level.</li>
<li><strong>Barrier-coat system:</strong> how many epoxy coats and which product affect the price.</li>
</ul>
<h2>Why no fixed price?</h2>
<p>Most of the osmosis job is drying, and drying time can't be known exactly upfront. A quote that says "this much" without measuring moisture will either under-do the work or pad the risk into the price. The right approach is a moisture reading at the survey and a realistic range.</p>
<h2>The hidden cost of a cheap quote</h2>
<p>A job that applies a barrier coat before drying traps the moisture inside, and osmosis returns within a season or two. So the most expensive osmosis treatment is the one done twice.</p>
<p>To see your boat's condition clearly, we do a free survey and moisture reading and give an itemised quote under our <a href="/en/services/fibreglass-repair/">fibreglass repair</a> service. We explain what osmosis is in our <a href="/en/blog/what-is-osmosis-treatment/">osmosis guide</a> and its signs in <a href="/en/blog/osmosis-symptoms/">this article</a>.</p>
""",
 },
},
{
 "slug": "tekne-cekek-karaya-cekme", "slug_en": "boat-haul-out-guide",
 "image": "/assets/images/services/bakim.jpg", "date": "2026-08-19",
 "tr": {
   "category": "Bakım",
   "title": "Tekne Çekek ve Karaya Çekme Rehberi: Ne Zaman, Neden, Nasıl?",
   "excerpt": "Tekne neden karaya çekilir, hangi işler çekek gerektirir ve süreç nasıl işler? Karaya çekme hakkında bilmeniz gerekenler.",
   "meta_title": "Tekne Çekek ve Karaya Çekme Rehberi | Tekne Usta",
   "meta_desc": "Tekne çekek ve karaya çekme rehberi: hangi işler çekek gerektirir, travel-lift süreci, karina kontrolü ve depolama. Karaya çekme hakkında pratik bilgiler.",
   "body": """
<p>Bazı işler suda yapılamaz; karina, antifouling ve kapsamlı fiberglas onarımları teknenin karaya çekilmesini gerektirir. İşte çekek süreci hakkında pratik bir rehber.</p>
<h2>Hangi işler çekek gerektirir?</h2>
<ul>
<li><a href="/hizmetler/tekne-boyama-antifouling/">Antifouling</a> yenileme ve su altı boya</li>
<li><a href="/hizmetler/fiberglas-onarim/">Osmoz tedavisi</a> ve su altı yapısal onarımlar</li>
<li>Karina temizliği, şaft/dümen kontrolü ve genel değerlendirme</li>
</ul>
<h2>Süreç nasıl işler?</h2>
<p>Tekne travel-lift (gezer vinç) veya kızak ile sudan alınır, payandalarla sabitlenir. Hemen ardından basınçlı yıkama yapılır — çünkü deniz kiri kuruyunca çok daha zor çıkar. Sonra planlanan işler başlar.</p>
<h2>Ne zaman çekilmeli?</h2>
<p>Sezon sonu (kışlatma ile birlikte) en yaygın dönemdir; hem çekek maliyeti bakımla birleşir hem de kış boyunca büyük işlere zaman kalır. Çekek alanları sezon sonunda hızla dolduğu için erken rezervasyon önemlidir.</p>
<h2>Karadayken fırsat</h2>
<p>Tekne karadayken karinayı, boyayı ve su altı donanımı yakından görmek mümkündür; küçük sorunlar büyümeden çözülür. <a href="/blog/tekne-kislatma-kontrol-listesi/">Kışlatma kontrol listemiz</a> bu fırsatı değerlendirmenize yardımcı olur.</p>
<p>Karaya çekme gerektiren işler için <a href="/hizmetler/tekne-kislatma/">kışlatma ve bakım</a> hizmetimiz kapsamında planlama yapıyoruz.</p>
""",
 },
 "en": {
   "category": "Maintenance",
   "title": "Boat Haul-Out Guide: When, Why and How?",
   "excerpt": "Why are boats hauled out, which jobs need it, and how does the process work? What to know about hauling out.",
   "meta_title": "Boat Haul-Out Guide | Tekne Usta",
   "meta_desc": "Boat haul-out guide: which jobs need hauling out, the travel-lift process, hull inspection and storage. Practical information about hauling out.",
   "body": """
<p>Some jobs can't be done afloat; hull work, antifouling and extensive fibreglass repairs need the boat out of the water. Here's a practical guide to the haul-out process.</p>
<h2>Which jobs need a haul-out?</h2>
<ul>
<li><a href="/en/services/boat-painting-antifouling/">Antifouling</a> renewal and underwater paint</li>
<li><a href="/en/services/fibreglass-repair/">Osmosis treatment</a> and below-waterline structural repairs</li>
<li>Hull cleaning, shaft/rudder checks and general assessment</li>
</ul>
<h2>How does it work?</h2>
<p>The boat is lifted out by travel-lift (or slipway) and secured on props. A pressure wash follows immediately — marine growth is far harder to remove once dry. Then the planned work begins.</p>
<h2>When to haul out?</h2>
<p>End of season (together with winterising) is the most common time; the lift cost combines with maintenance and there's time over winter for big jobs. Book early, as hardstanding fills fast at season's end.</p>
<h2>An opportunity ashore</h2>
<p>With the boat ashore you can inspect the hull, paint and underwater gear closely; small problems get fixed before they grow. Our <a href="/en/blog/boat-winterising-checklist/">winterising checklist</a> helps you make the most of it.</p>
<p>For jobs that need a haul-out, we plan the work under our <a href="/en/services/winterising-storage/">winterising and maintenance</a> service.</p>
""",
 },
},
{
 "slug": "jelkot-vs-boya", "slug_en": "gelcoat-vs-paint",
 "image": "/assets/images/services/boya.jpg", "date": "2026-09-02",
 "tr": {
   "category": "Boya",
   "title": "Jelkot mu Boya mı? Fiber Teknenin Dış Yüzeyini Yenilemek",
   "excerpt": "Solmuş fiber teknenin dış yüzeyi jelkotla mı yoksa boyayla mı yenilenmeli? Avantajlar, dezavantajlar ve karar kriterleri.",
   "meta_title": "Jelkot mu Boya mı? Fiber Tekne Yüzey Yenileme | Tekne Usta",
   "meta_desc": "Jelkot ve boya karşılaştırması: fiber teknenin dış yüzeyini yenilerken jelkot mu boya mı? Dayanıklılık, maliyet, onarılabilirlik ve görünüm farkları.",
   "body": """
<p>Fiber teknenin dış yüzeyi yıprandığında iki yol vardır: mevcut jelkotu yenilemek ya da üzerine profesyonel boya sistemi uygulamak. İkisinin de yeri var; karar teknenizin durumuna ve beklentinize bağlı.</p>
<h2>Jelkot</h2>
<p>Jelkot, teknenin orijinal yüzeyidir. <strong>Artıları:</strong> kalın, aşınmaya dayanıklı, kolay onarılabilir (bölgesel dokunuş mümkün). <strong>Sınırı:</strong> yaşlandıkça matlaşır ve renk seçenekleri boyaya göre daha kısıtlıdır. Yüzey hâlâ sağlamsa <a href="/blog/gelcoat-yenileme/">gelcoat yenileme/parlatma</a> çoğu zaman en ekonomik yoldur.</p>
<h2>Boya (2K poliüretan)</h2>
<p>Modern iki bileşenli boya sistemleri derin bir parlaklık ve geniş renk yelpazesi sunar. <strong>Artıları:</strong> pürüzsüz, yüksek parlaklık, renk değişimi imkânı. <strong>Sınırı:</strong> doğru astar ve yüzey hazırlığı şarttır; onarımı jelkota göre daha uzmanlık ister.</p>
<h2>Nasıl karar verilir?</h2>
<p>Jelkot inceldi ama sağlamsa ve renk değişimi istemiyorsanız jelkot yenileme; komple bir görünüm tazelemesi, renk değişimi veya süperyat kalitesinde bir bitiş istiyorsanız boya mantıklıdır. Kararı keşifte yüzeyin kalınlığına bakarak birlikte veririz.</p>
<p>Her iki seçenekte de <a href="/hizmetler/tekne-boyama-antifouling/">boya</a> ve <a href="/hizmetler/fiberglas-onarim/">fiberglas onarım</a> hizmetlerimizle yardımcı oluyoruz.</p>
""",
 },
 "en": {
   "category": "Painting",
   "title": "Gelcoat or Paint? Renewing a Fibreglass Boat's Exterior",
   "excerpt": "Should a faded fibreglass exterior be renewed with gelcoat or paint? The pros, cons and criteria for deciding.",
   "meta_title": "Gelcoat or Paint? Fibreglass Surface Renewal | Tekne Usta",
   "meta_desc": "Gelcoat vs paint comparison: gelcoat or paint when renewing a fibreglass exterior? Differences in durability, cost, repairability and appearance.",
   "body": """
<p>When a fibreglass exterior wears out there are two routes: renew the existing gelcoat, or apply a professional paint system over it. Both have their place; the choice depends on your boat's condition and your expectations.</p>
<h2>Gelcoat</h2>
<p>Gelcoat is the boat's original surface. <strong>Pros:</strong> thick, wear-resistant, easy to repair (spot touch-ups possible). <strong>Limit:</strong> it dulls with age and colour options are narrower than paint. If the surface is still sound, a <a href="/en/blog/gelcoat-renewal/">gelcoat renewal/polish</a> is often the most economical route.</p>
<h2>Paint (2K polyurethane)</h2>
<p>Modern two-part paint systems offer deep gloss and a wide colour range. <strong>Pros:</strong> smooth, high gloss, colour change possible. <strong>Limit:</strong> correct primer and surface prep are essential; repair takes more expertise than gelcoat.</p>
<h2>How to decide?</h2>
<p>If the gelcoat has thinned but is sound and you don't want a colour change, renew the gelcoat; if you want a full refresh, a colour change or a superyacht-grade finish, paint makes sense. We decide together at the survey by checking surface thickness.</p>
<p>We help with both through our <a href="/en/services/boat-painting-antifouling/">painting</a> and <a href="/en/services/fibreglass-repair/">fibreglass repair</a> services.</p>
""",
 },
},
{
 "slug": "teak-vs-sentetik-teak", "slug_en": "teak-vs-synthetic-teak",
 "image": "/assets/images/services/ic-mekan.jpg", "date": "2026-09-16",
 "tr": {
   "category": "Teak",
   "title": "Doğal Teak mı Sentetik Teak mi? Güverte İçin Karşılaştırma",
   "excerpt": "Doğal teak ile sentetik teak arasındaki fark: görünüm, bakım, ısı, kaymazlık ve maliyet. Güverteniz için hangisi?",
   "meta_title": "Doğal Teak mı Sentetik Teak mi? Karşılaştırma | Tekne Usta",
   "meta_desc": "Doğal teak ve sentetik teak karşılaştırması: görünüm, bakım yükü, ısı, kaymazlık ve maliyet. Güverte döşeme için hangisinin size uygun olduğu.",
   "body": """
<p>Yeni bir güverte döşerken en sık sorulan soru: doğal teak mı, sentetik teak mı? İkisi de güzel görünür ama bakım, konfor ve maliyet açısından ayrışırlar.</p>
<h2>Doğal teak</h2>
<p><strong>Artıları:</strong> eşsiz doğal doku, sıcak his, klasik prestij. <strong>Dikkat:</strong> düzenli <a href="/blog/teak-guverte-bakimi/">bakım ister</a>, zamanla incelir, güneşte griye döner ve fiyatı yüksektir.</p>
<h2>Sentetik teak</h2>
<p><strong>Artıları:</strong> neredeyse sıfır bakım, güneşte yumuşamaz, kaymaz, geniş renk/desen seçeneği, lekeye dayanıklı. <strong>Dikkat:</strong> doğal ahşabın canlı dokusunu birebir vermez; kalite markaya göre değişir.</p>
<h2>Isı ve kaymazlık</h2>
<p>Kaliteli sentetik teak, koyu renklerde bile güneşte doğal teaktan çok ısınmayacak şekilde üretilebilir ve ıslakken kaymazlığı yüksektir — çocuklu ve yoğun kullanılan tekneler için avantaj.</p>
<h2>Hangisi size uygun?</h2>
<p>Klasik görünüm ve prestij önceliğinizse ve bakıma vakit ayırabiliyorsanız doğal teak; bakımla uğraşmadan şık ve güvenli bir güverte istiyorsanız sentetik teak mantıklı. İkisini de <a href="/hizmetler/teak-guverte-doseme/">teak güverte döşeme</a> hizmetimiz kapsamında uyguluyoruz.</p>
""",
 },
 "en": {
   "category": "Teak",
   "title": "Natural or Synthetic Teak? A Comparison for Your Deck",
   "excerpt": "The difference between natural and synthetic teak: looks, maintenance, heat, non-slip and cost. Which is right for your deck?",
   "meta_title": "Natural or Synthetic Teak? A Comparison | Tekne Usta",
   "meta_desc": "Natural vs synthetic teak comparison: appearance, maintenance burden, heat, non-slip and cost. Which teak decking suits you.",
   "body": """
<p>The most common question when laying a new deck: natural teak or synthetic? Both look good, but they differ in maintenance, comfort and cost.</p>
<h2>Natural teak</h2>
<p><strong>Pros:</strong> unmatched natural grain, warm feel, classic prestige. <strong>Watch for:</strong> it needs regular <a href="/en/blog/teak-deck-maintenance/">care</a>, thins over time, greys in the sun and is expensive.</p>
<h2>Synthetic teak</h2>
<p><strong>Pros:</strong> near-zero maintenance, doesn't soften in the sun, non-slip, a wide colour/pattern range, stain-resistant. <strong>Watch for:</strong> it doesn't perfectly reproduce natural wood's living grain; quality varies by brand.</p>
<h2>Heat and non-slip</h2>
<p>Quality synthetic teak can be made so that, even in dark colours, it doesn't heat up like natural teak in the sun, and it's highly non-slip when wet — an advantage for boats with children and heavy use.</p>
<h2>Which suits you?</h2>
<p>If classic looks and prestige are your priority and you can give it time, natural teak; if you want an elegant, safe deck without the upkeep, synthetic teak makes sense. We lay both under our <a href="/en/services/teak-deck/">teak decking</a> service.</p>
""",
 },
},
{
 "slug": "fiberglas-catlak-onarimi", "slug_en": "fibreglass-crack-repair",
 "image": "/assets/images/services/fiberglas.jpg", "date": "2026-09-30",
 "tr": {
   "category": "Fiberglas",
   "title": "Fiberglas Çatlak ve Kırık Onarımı Nasıl Yapılır?",
   "excerpt": "Örümcek çatlağı mı, yapısal kırık mı? Fiber teknede çatlak türleri ve doğru onarımın adımları.",
   "meta_title": "Fiberglas Çatlak ve Kırık Onarımı Rehberi | Tekne Usta",
   "meta_desc": "Fiberglas çatlak ve kırık onarımı: örümcek çatlakları, yapısal kırıklar ve delikler nasıl onarılır? Laminasyon, dolgu ve yüzey bitişinin adımları.",
   "body": """
<p>Fiber teknelerde çatlaklar kozmetikten yapısala kadar geniş bir aralıkta olur. Doğru onarım, çatlağın türünü doğru okumakla başlar.</p>
<h2>Çatlak türleri</h2>
<ul>
<li><strong>Örümcek (spider) çatlakları:</strong> Jelkotta yüzeysel, ince ağ şeklinde çatlaklar. Genelde kozmetiktir ama gizli bir darbeye işaret edebilir.</li>
<li><strong>Gerilim çatlakları:</strong> Yük binen bölgelerde (güverte donanımı çevresi) tekrarlayan stresle oluşur.</li>
<li><strong>Yapısal kırık ve delik:</strong> Çarpma sonucu laminatın hasar görmesi; su alma riski taşır.</li>
</ul>
<h2>Onarım adımları</h2>
<ul>
<li><strong>Değerlendirme:</strong> Çatlağın yüzeysel mi yoksa laminata kadar mı indiği belirlenir.</li>
<li><strong>Açma ve temizleme:</strong> Çatlak, sağlam malzemeye ulaşana kadar açılır (V veya U kanal).</li>
<li><strong>Laminasyon:</strong> Yapısal hasarda cam elyafı ve reçineyle kat kat güçlendirme yapılır.</li>
<li><strong>Dolgu ve zımpara:</strong> Yüzey epoksi dolgu ile düzeltilir.</li>
<li><strong>Yüzey bitişi:</strong> <a href="/blog/gelcoat-yenileme/">Gelcoat</a> veya boya ile orijinaline yakın bir bitiş sağlanır.</li>
</ul>
<h2>Kozmetik onarım yeterli mi?</h2>
<p>Sadece jelkotu doldurup geçmek, altında yapısal bir sorun varsa çözüm değildir; çatlak geri gelir. Bu yüzden önce kaynağı anlamak gerekir.</p>
<p>Teknenizdeki çatlağın türünü ve doğru çözümü belirlemek için <a href="/hizmetler/fiberglas-onarim/">fiberglas onarım</a> hizmetimiz kapsamında ücretsiz keşif yapıyoruz.</p>
""",
 },
 "en": {
   "category": "Fibreglass",
   "title": "How Are Fibreglass Cracks and Breaks Repaired?",
   "excerpt": "Spider crack or structural break? The types of cracks in a fibreglass boat and the steps to a proper repair.",
   "meta_title": "Fibreglass Crack and Break Repair Guide | Tekne Usta",
   "meta_desc": "Fibreglass crack and break repair: how spider cracks, structural breaks and holes are repaired. The steps of lamination, filling and surface finishing.",
   "body": """
<p>Cracks in fibreglass boats range from cosmetic to structural. A proper repair starts with reading the type of crack correctly.</p>
<h2>Types of crack</h2>
<ul>
<li><strong>Spider cracks:</strong> fine, web-like surface cracks in the gelcoat. Usually cosmetic but can hint at a hidden impact.</li>
<li><strong>Stress cracks:</strong> form under repeated stress at loaded areas (around deck hardware).</li>
<li><strong>Structural breaks and holes:</strong> laminate damage from impact; carry a risk of water ingress.</li>
</ul>
<h2>Repair steps</h2>
<ul>
<li><strong>Assessment:</strong> determine whether the crack is superficial or reaches the laminate.</li>
<li><strong>Opening and cleaning:</strong> the crack is opened back to sound material (a V or U groove).</li>
<li><strong>Lamination:</strong> for structural damage, glass fibre and resin build up layer by layer.</li>
<li><strong>Filling and sanding:</strong> the surface is faired with epoxy filler.</li>
<li><strong>Surface finish:</strong> <a href="/en/blog/gelcoat-renewal/">gelcoat</a> or paint restores a near-original finish.</li>
</ul>
<h2>Is a cosmetic repair enough?</h2>
<p>Simply filling the gelcoat isn't a solution if there's a structural problem beneath; the crack returns. So the cause must be understood first.</p>
<p>To identify the type of crack and the right solution, we do a free survey under our <a href="/en/services/fibreglass-repair/">fibreglass repair</a> service.</p>
""",
 },
},
{
 "slug": "bahar-tekne-bakimi", "slug_en": "spring-boat-maintenance",
 "image": "/assets/images/parallax-1.jpg", "date": "2026-10-14",
 "tr": {
   "category": "Bakım",
   "title": "Bahar Tekne Bakımı: Sezona Sağlam Başlamak İçin Kontrol Listesi",
   "excerpt": "Kıştan çıkan teknenizi suya indirmeden önce yapılması gerekenler. Bahar bakımı adım adım.",
   "meta_title": "Bahar Tekne Bakımı Kontrol Listesi | Tekne Usta",
   "meta_desc": "Bahar tekne bakımı: karina ve antifouling kontrolü, gelcoat/boya, teak ve iç mekan. Sezona sağlam başlamak için suya iniş öncesi kontrol listesi.",
   "body": """
<p>Kış boyunca bekleyen tekne, suya inmeden önce dikkatli bir bahar bakımı ister. İyi bir başlangıç, sezonun keyfini ikiye katlar. İşte suya iniş öncesi kontrol listesi.</p>
<h2>Karina ve su altı</h2>
<ul>
<li><a href="/hizmetler/tekne-boyama-antifouling/">Antifouling</a> durumunu kontrol edin; gerekiyorsa yenileyin.</li>
<li>Karinada çizik, çatlak ve <a href="/blog/osmoz-belirtileri/">osmoz belirtisi</a> taraması yapın.</li>
<li>Anotları kontrol edip tükenmişleri değiştirin.</li>
</ul>
<h2>Gövde ve güverte</h2>
<ul>
<li>Gelcoat/boya parlaklığı; gerekiyorsa <a href="/blog/gelcoat-yenileme/">parlatma</a>.</li>
<li>Teak ve dış ahşapta kış yıpranması; derz kontrolü.</li>
<li>Su alan güverte bölgelerini (yumuşaklık) kontrol edin.</li>
</ul>
<h2>İç mekan</h2>
<ul>
<li>Nem ve küf kontrolü; iyi havalandırma.</li>
<li>Kumaş ve minderlerde nem/küf izleri.</li>
</ul>
<h2>Erken planlamanın avantajı</h2>
<p>Bahar bakımını sezon açılmadan planlarsanız çekek ve servis yoğunluğuna takılmadan suya ilk inenlerden olursunuz. <a href="/blog/yillik-tekne-bakim-takvimi/">Yıllık bakım takvimimiz</a> tüm sezonu planlamanıza yardımcı olur.</p>
<p>Bahar bakımı için <a href="/hizmetler/tekne-kislatma/">bakım</a> hizmetimiz kapsamında ücretsiz keşif yapalım.</p>
""",
 },
 "en": {
   "category": "Maintenance",
   "title": "Spring Boat Maintenance: A Checklist to Start the Season Right",
   "excerpt": "What to do before launching your boat after winter. Spring maintenance, step by step.",
   "meta_title": "Spring Boat Maintenance Checklist | Tekne Usta",
   "meta_desc": "Spring boat maintenance: hull and antifouling checks, gelcoat/paint, teak and interior. A pre-launch checklist to start the season sound.",
   "body": """
<p>A boat that's sat all winter needs a careful spring check before launch. A good start doubles the season's enjoyment. Here's the pre-launch checklist.</p>
<h2>Hull and underwater</h2>
<ul>
<li>Check the <a href="/en/services/boat-painting-antifouling/">antifouling</a> and renew if needed.</li>
<li>Scan the hull for scratches, cracks and <a href="/en/blog/osmosis-symptoms/">osmosis signs</a>.</li>
<li>Check anodes and replace spent ones.</li>
</ul>
<h2>Hull and deck</h2>
<ul>
<li>Gelcoat/paint gloss; <a href="/en/blog/gelcoat-renewal/">polish</a> if needed.</li>
<li>Winter wear on teak and exterior wood; seam check.</li>
<li>Check deck areas for softness (water ingress).</li>
</ul>
<h2>Interior</h2>
<ul>
<li>Check for damp and mould; ventilate well.</li>
<li>Look for damp/mould marks on fabric and cushions.</li>
</ul>
<h2>The advantage of early planning</h2>
<p>Plan spring maintenance before the season opens and you'll be among the first afloat, ahead of the haul-out and service rush. Our <a href="/en/blog/annual-boat-maintenance-calendar/">annual maintenance calendar</a> helps you plan the whole season.</p>
<p>For spring maintenance, let's do a free survey under our <a href="/en/services/winterising-storage/">maintenance</a> service.</p>
""",
 },
},
{
 "slug": "tekne-ismi-grafik-uygulamasi", "slug_en": "boat-name-graphics",
 "image": "/assets/images/services/boya.jpg", "date": "2026-10-28",
 "tr": {
   "category": "Boya",
   "title": "Tekne İsmi ve Grafik Uygulaması: Temiz Bir Sonuç İçin",
   "excerpt": "Tekne ismi, kılavuz şerit ve grafikler nasıl uygulanır? Folyo mu boya mı, dayanıklılık ve temiz çizgi için ipuçları.",
   "meta_title": "Tekne İsmi ve Grafik Uygulaması Rehberi | Tekne Usta",
   "meta_desc": "Tekne ismi, kılavuz şerit (boot stripe) ve grafik uygulaması: folyo mu boya mı, malzeme seçimi, dayanıklılık ve temiz maskeleme için ipuçları.",
   "body": """
<p>Teknenizin ismi ve şeritleri, karakterini tamamlayan detaylardır. İyi uygulanmış bir grafik yıllarca keskin durur; kötü uygulananı ise kısa sürede kalkar ve kenarlarından su alır.</p>
<h2>Folyo mu, boya mı?</h2>
<p><strong>Folyo (vinil):</strong> Hızlı, ekonomik, renk ve tasarım esnekliği yüksek. Deniz sınıfı döküm vinil doğru uygulandığında uzun ömürlüdür. <strong>Boya:</strong> Kalıcılığı en yüksek seçenek; özellikle kılavuz şerit ve büyük yüzeylerde tercih edilir ama işçilik ve maskeleme ustalık ister.</p>
<h2>Temiz çizginin sırrı: maskeleme</h2>
<p>İster folyo ister boya olsun, sonucu belirleyen yüzey hazırlığı ve maskelemedir. Temiz, yağdan arınmış yüzey; keskin ve düz maskeleme çizgileri; doğru kuruma süresi — hepsi kenarların kalkmaması için şarttır.</p>
<h2>Yerleşim ve okunabilirlik</h2>
<p>İsmin konumu, yazı tipi ve boyutu hem estetik hem yasal görünürlük açısından önemlidir. Tekne hattına uyumlu, uzaktan okunabilir bir yerleşim öneririz.</p>
<p>Grafik ve isim uygulamasını <a href="/hizmetler/tekne-boyama-antifouling/">tekne boyama</a> hizmetimiz kapsamında yapıyoruz; renk değişimi veya komple dış cephe ile birlikte planlanabilir. Boya maliyetini etkileyen faktörler için <a href="/blog/tekne-boyama-maliyeti/">bu yazıya</a> bakın.</p>
""",
 },
 "en": {
   "category": "Painting",
   "title": "Boat Name and Graphics: For a Clean Result",
   "excerpt": "How are boat names, boot stripes and graphics applied? Vinyl or paint, durability and tips for crisp lines.",
   "meta_title": "Boat Name and Graphics Application Guide | Tekne Usta",
   "meta_desc": "Boat name, boot stripe and graphics application: vinyl or paint, material choice, durability and tips for clean masking.",
   "body": """
<p>Your boat's name and stripes are the details that complete its character. Well applied, graphics stay crisp for years; poorly applied, they soon lift and let water under the edges.</p>
<h2>Vinyl or paint?</h2>
<p><strong>Vinyl:</strong> fast, economical, flexible in colour and design. Marine-grade cast vinyl, correctly applied, is long-lasting. <strong>Paint:</strong> the most durable option, preferred especially for boot stripes and large surfaces, but the labour and masking take skill.</p>
<h2>The secret to crisp lines: masking</h2>
<p>Whether vinyl or paint, prep and masking decide the result. A clean, grease-free surface; sharp, straight masking lines; correct drying time — all essential to keep edges from lifting.</p>
<h2>Placement and legibility</h2>
<p>The name's position, font and size matter for both looks and legal visibility. We suggest a layout that suits the boat's lines and reads from a distance.</p>
<p>We apply graphics and names under our <a href="/en/services/boat-painting-antifouling/">boat painting</a> service; they can be planned alongside a colour change or full topside. For what affects painting cost, see <a href="/en/blog/boat-painting-cost/">this article</a>.</p>
""",
 },
},
{
 "slug": "kalafat-nedir", "slug_en": "caulking-explained",
 "image": "/assets/images/services/ahsap.jpg", "date": "2026-11-11",
 "tr": {
   "category": "Ahşap",
   "title": "Kalafat Nedir? Ahşap Teknede Su Sızdırmazlığın Temeli",
   "excerpt": "Kalafat neden gerekli, ne zaman yenilenmeli ve modern yöntemler nelerdir? Ahşap tekne sahipleri için temel bilgiler.",
   "meta_title": "Kalafat Nedir? Ahşap Tekne Kalafat Rehberi | Tekne Usta",
   "meta_desc": "Kalafat nedir, ahşap teknede neden gereklidir ve ne zaman yenilenmeli? Geleneksel ve modern kalafat yöntemleri, su sızdırmazlık ve bakım.",
   "body": """
<p>Kalafat, ahşap teknelerde kaplama tahtaları arasındaki derzlerin su geçirmez hâle getirilmesidir. Yüzyıllardır teknenin su üstünde kalmasını sağlayan bu işçilik, doğru yapıldığında ahşap teknenin en kritik güvencesidir.</p>
<h2>Kalafat neden gerekli?</h2>
<p>Ahşap, nemle şişer ve kururken büzülür. Bu hareket derzlerin açılıp kapanmasına yol açar. Kalafat malzemesi bu hareketi karşılayacak esneklikte olmalı; hem su tutmalı hem çatlamamalıdır.</p>
<h2>Geleneksel ve modern yöntemler</h2>
<p>Geleneksel yöntemde derzlere üstüpü (pamuk/keten) çakılır ve üzeri macunla kapatılır. Modern uygulamalarda esnek poliüretan/polisülfit dolgular kullanılır. Doğru yöntem, teknenin yapısına ve yaşına göre seçilir.</p>
<h2>Ne zaman yenilenmeli?</h2>
<p>Su alan, derzleri kabaran veya kuruyup çatlayan bir teknede kalafat zamanı gelmiştir. Küçük sızıntıları ertelemek, altındaki ahşabın çürümesine yol açabilir.</p>
<p>Kalafat ve kaplama işlerini <a href="/hizmetler/ahsap-tekne-renovasyonu/">ahşap tekne renovasyonu</a> hizmetimiz kapsamında yapıyoruz. Ahşap bakımı hakkında daha fazlası için <a href="/blog/ahsap-tekne-vernik-bakimi/">vernik bakımı</a> yazımıza da bakın.</p>
""",
 },
 "en": {
   "category": "Wood",
   "title": "What Is Caulking? The Basis of Watertightness in Wooden Boats",
   "excerpt": "Why is caulking needed, when should it be renewed, and what are the modern methods? Essentials for wooden boat owners.",
   "meta_title": "What Is Caulking? Wooden Boat Caulking Guide | Tekne Usta",
   "meta_desc": "What is caulking, why is it needed on a wooden boat and when should it be renewed? Traditional and modern caulking methods, watertightness and care.",
   "body": """
<p>Caulking is making the seams between planking on a wooden boat watertight. This craft, which has kept boats afloat for centuries, is the wooden boat's most critical safeguard when done right.</p>
<h2>Why is caulking needed?</h2>
<p>Wood swells with moisture and shrinks as it dries. This movement opens and closes the seams. The caulking material must be flexible enough to accommodate it — holding water out without cracking.</p>
<h2>Traditional and modern methods</h2>
<p>The traditional method drives oakum (cotton/flax) into the seams and covers it with a stopping compound. Modern applications use flexible polyurethane/polysulphide sealants. The right method is chosen for the boat's construction and age.</p>
<h2>When should it be renewed?</h2>
<p>A boat that leaks, has lifting seams or dried, cracked stopping is due for caulking. Postponing small leaks can rot the wood beneath.</p>
<p>We do caulking and planking under our <a href="/en/services/wooden-boat-refit/">wooden boat refit</a> service. For more on wood care, see our <a href="/en/blog/wooden-boat-varnish-care/">varnish care</a> article.</p>
""",
 },
},
{
 "slug": "kisin-tekne-nerede-saklanir", "slug_en": "winter-boat-storage",
 "image": "/assets/images/services/bakim.jpg", "date": "2026-11-25",
 "tr": {
   "category": "Bakım",
   "title": "Kışın Tekne Nerede Saklanır? Karada, Suda ve Kapalı Depolama",
   "excerpt": "Tekneyi kışın karada mı, suda mı, kapalı alanda mı saklamalı? Her seçeneğin artıları, riskleri ve maliyeti.",
   "meta_title": "Kışın Tekne Nerede Saklanır? Depolama Rehberi | Tekne Usta",
   "meta_desc": "Kışın tekne depolama seçenekleri: karada (hardstand), suda (marina) ve kapalı depolama. Her birinin avantajları, riskleri, maliyeti ve hangisi size uygun.",
   "body": """
<p>Kış geldiğinde tekne sahiplerinin ilk sorusu: "Tekneyi nerede saklayayım?" Üç ana seçenek var; doğru tercih teknenize, bütçenize ve bölgenize bağlı.</p>
<h2>Karada depolama (hardstand)</h2>
<p>En yaygın seçenek. Tekne karaya çekilir, payandalanır ve örtülür. <strong>Artıları:</strong> karina kurur, su altı işleri kolayca yapılır, osmoz riski azalır. <strong>Dikkat:</strong> doğru payandalama ve havalandırmalı örtü şart.</p>
<h2>Suda depolama (marina)</h2>
<p>Tekne suda kalır. <strong>Artıları:</strong> çekme maliyeti yok, hızlı erişim. <strong>Dikkat:</strong> karina sürekli suyla temasta olduğu için kirlenme ve osmoz riski, fırtına ve buzlanma riski artar.</p>
<h2>Kapalı depolama</h2>
<p>En korunaklı ama en pahalı seçenek. <strong>Artıları:</strong> hava koşullarından tam koruma, jelkot ve ahşap için ideal. <strong>Dikkat:</strong> maliyet ve yer sınırlı; erken rezervasyon gerekir.</p>
<h2>Hangisi doğru?</h2>
<p>Çoğu tekne için karada depolama en dengeli seçenektir — hem bakım fırsatı hem koruma sağlar. Kışlatma sürecini <a href="/blog/tekne-kislatma-kontrol-listesi/">kontrol listemizde</a> anlattık. <a href="/hizmetler/tekne-kislatma/">Kışlatma ve depolama</a> hizmetimiz kapsamında karaya çekme, örtü ve gözetimli depolama sunuyoruz.</p>
""",
 },
 "en": {
   "category": "Maintenance",
   "title": "Where to Store a Boat in Winter? Ashore, Afloat and Indoors",
   "excerpt": "Should you store a boat ashore, afloat or indoors in winter? The pros, risks and cost of each option.",
   "meta_title": "Where to Store a Boat in Winter? Storage Guide | Tekne Usta",
   "meta_desc": "Winter boat storage options: ashore (hardstand), afloat (marina) and indoor storage. The advantages, risks, cost of each and which suits you.",
   "body": """
<p>When winter comes, boat owners' first question is: "Where do I store the boat?" There are three main options; the right one depends on your boat, budget and region.</p>
<h2>Ashore (hardstand)</h2>
<p>The most common option. The boat is hauled out, propped and covered. <strong>Pros:</strong> the hull dries, underwater work is easy, osmosis risk drops. <strong>Watch for:</strong> correct propping and a ventilated cover are essential.</p>
<h2>Afloat (marina)</h2>
<p>The boat stays in the water. <strong>Pros:</strong> no lift cost, quick access. <strong>Watch for:</strong> the hull is in constant contact with water, raising growth and osmosis risk, plus storm and ice risk.</p>
<h2>Indoor storage</h2>
<p>The most protected but most expensive option. <strong>Pros:</strong> full protection from the weather, ideal for gelcoat and wood. <strong>Watch for:</strong> cost and limited space; book early.</p>
<h2>Which is right?</h2>
<p>For most boats, ashore is the most balanced option — both a maintenance opportunity and protection. We cover the process in our <a href="/en/blog/boat-winterising-checklist/">winterising checklist</a>. Under our <a href="/en/services/winterising-storage/">winterising and storage</a> service we offer haul-out, covering and supervised storage.</p>
""",
 },
},
{
 "slug": "tekne-doseme-kumas-secimi", "slug_en": "marine-upholstery-fabric",
 "image": "/assets/images/services/ic-mekan.jpg", "date": "2026-12-09",
 "tr": {
   "category": "İç Mekan",
   "title": "Tekne Döşeme Kumaşı Seçimi: Denize Dayanıklı ve Şık",
   "excerpt": "Teknede hangi kumaş kullanılmalı? UV, tuz, nem ve küfe dayanıklı deniz sınıfı kumaş ve sünger seçimi.",
   "meta_title": "Tekne Döşeme Kumaşı Seçimi Rehberi | Tekne Usta",
   "meta_desc": "Tekne döşeme kumaşı seçimi: UV, tuz, nem ve küfe dayanıklı deniz sınıfı kumaşlar, hızlı kuruyan sünger ve dış mekan döşeme için ipuçları.",
   "body": """
<p>Teknede döşeme, evdekinden çok daha zorlu koşullarla karşılaşır: güneş, tuz, nem ve sürekli kullanım. Bu yüzden kumaş ve sünger seçimi, döşemenin ne kadar dayanacağını doğrudan belirler.</p>
<h2>Deniz sınıfı kumaşlar</h2>
<p>Denize uygun kumaşlar UV'ye karşı solmaya dirençli, su itici, lekeye ve küfe dayanıklıdır. Dış mekân (kokpit) döşemelerinde çözgü boyalı akrilik kumaşlar; iç mekânda ise deniz sınıfı vinil ve kumaşlar tercih edilir.</p>
<h2>Doğru sünger</h2>
<p>Teknede standart sünger su tutar ve küflenir. <strong>Hızlı kuruyan (drenajlı) sünger</strong>, özellikle dış mekân minderlerinde nemi geçirir ve küfü önler. İç mekânda konfor ve yoğunluk dengesi önemlidir.</p>
<h2>Dikiş ve detaylar</h2>
<p>Dikişte UV'ye dayanıklı iplik kullanılmalı; aksi halde kumaş sağlamken dikişler çözülür. Fermuar ve çıtçıtların paslanmaz olması da uzun ömür için önemlidir.</p>
<p>Kumaş, sünger ve komple döşeme yenilemeyi <a href="/hizmetler/ic-mekan-yenileme/">iç mekan yenileme</a> hizmetimiz kapsamında yapıyoruz; renk ve dokuyu birlikte seçiyoruz.</p>
""",
 },
 "en": {
   "category": "Interior",
   "title": "Choosing Marine Upholstery Fabric: Durable and Elegant",
   "excerpt": "Which fabric should you use aboard? Choosing marine-grade fabric and foam resistant to UV, salt, damp and mould.",
   "meta_title": "Choosing Marine Upholstery Fabric Guide | Tekne Usta",
   "meta_desc": "Choosing marine upholstery fabric: UV-, salt-, damp- and mould-resistant marine-grade fabrics, quick-dry foam and tips for exterior upholstery.",
   "body": """
<p>Upholstery aboard faces far tougher conditions than at home: sun, salt, damp and constant use. So the choice of fabric and foam directly determines how long the upholstery lasts.</p>
<h2>Marine-grade fabrics</h2>
<p>Suitable fabrics resist UV fading, repel water and resist stains and mould. For exterior (cockpit) upholstery, solution-dyed acrylics; for interiors, marine-grade vinyl and fabrics are preferred.</p>
<h2>The right foam</h2>
<p>Standard foam holds water and grows mould aboard. <strong>Quick-dry (draining) foam</strong>, especially for exterior cushions, lets moisture through and prevents mould. Indoors, the balance of comfort and density matters.</p>
<h2>Stitching and details</h2>
<p>Stitching should use UV-resistant thread; otherwise the seams fail while the fabric is still sound. Stainless zips and snaps also matter for longevity.</p>
<p>We renew fabric, foam and full interiors under our <a href="/en/services/interior-refit/">interior refit</a> service, choosing colour and texture together with you.</p>
""",
 },
},
{
 "slug": "ikinci-el-tekne-alim-rehberi", "slug_en": "used-boat-buying-guide",
 "image": "/assets/images/hakkimizda.jpg", "date": "2026-12-23",
 "tr": {
   "category": "Rehber",
   "title": "İkinci El Tekne Alım Rehberi: Doğru Tekneyi Seçmek",
   "excerpt": "İkinci el tekne alırken bütçe, tip, kullanım ve durum değerlendirmesi. Doğru kararı vermek için kapsamlı rehber.",
   "meta_title": "İkinci El Tekne Alım Rehberi | Tekne Usta",
   "meta_desc": "İkinci el tekne alım rehberi: bütçe planlama, tekne tipi seçimi, kullanım amacı, durum değerlendirmesi ve gizli maliyetler. Doğru tekneyi seçmenin yolları.",
   "body": """
<p>İkinci el tekne, yeni tekneye göre çok daha erişilebilir bir giriş kapısıdır — ama doğru seçim bilgi ister. Bu rehber, karar sürecini adım adım özetliyor.</p>
<h2>Önce kullanım amacı</h2>
<p>Günübirlik gezinti mi, konaklamalı seyir mi, balık mı, yelken mi? Kullanımınız tekne tipini belirler: motor tekne, yelkenli, RIB veya klasik ahşap. Yanlış tip, sonradan pişmanlığın en yaygın sebebidir.</p>
<h2>Gerçek bütçe: satın alma + işletme</h2>
<p>Teknenin fiyatı buzdağının görünen kısmıdır. Bağlama, kışlatma, sigorta, bakım ve olası onarımlar yıllık işletme maliyetini oluşturur. Bütçeyi bu kalemlerle birlikte planlayın.</p>
<h2>Durum değerlendirmesi</h2>
<p>Fiber teknede <a href="/blog/osmoz-belirtileri/">osmoz</a> ve gelcoat; ahşap teknede çürük ve <a href="/blog/kalafat-nedir/">kalafat</a>; her tekede karina, güverte ve donanım kontrol edilmeli. Deneyimli bir gözle yapılan <a href="/blog/satin-alma-oncesi-tekne-ekspertizi/">satın alma öncesi kontrol</a>, gizli maliyetleri ortaya çıkarır ve pazarlıkta elinizi güçlendirir.</p>
<h2>Karar</h2>
<p>Duygusal değil, kontrol listesiyle karar verin. Almayı düşündüğünüz tekneyi <a href="/hizmetler/fiberglas-onarim/">fiberglas</a> veya <a href="/hizmetler/ahsap-tekne-renovasyonu/">ahşap</a> tarafında birlikte değerlendirebiliriz — bize yazın.</p>
""",
 },
 "en": {
   "category": "Guide",
   "title": "Used Boat Buying Guide: Choosing the Right Boat",
   "excerpt": "Budget, type, use and condition assessment when buying a used boat. A comprehensive guide to making the right decision.",
   "meta_title": "Used Boat Buying Guide | Tekne Usta",
   "meta_desc": "Used boat buying guide: budget planning, choosing a boat type, intended use, condition assessment and hidden costs. How to choose the right boat.",
   "body": """
<p>A used boat is a far more accessible way in than a new one — but the right choice takes knowledge. This guide sums up the decision process step by step.</p>
<h2>Start with intended use</h2>
<p>Day trips, overnight cruising, fishing, sailing? Your use determines the type: motorboat, sailboat, RIB or classic wooden. The wrong type is the most common cause of later regret.</p>
<h2>The real budget: purchase + running costs</h2>
<p>The purchase price is the tip of the iceberg. Berthing, winterising, insurance, maintenance and possible repairs make up the annual running cost. Plan the budget with these items included.</p>
<h2>Condition assessment</h2>
<p>On fibreglass, check <a href="/en/blog/osmosis-symptoms/">osmosis</a> and gelcoat; on wood, rot and <a href="/en/blog/caulking-explained/">caulking</a>; on any boat, the hull, deck and gear. A <a href="/en/blog/pre-purchase-boat-survey/">pre-purchase check</a> by an experienced eye reveals hidden costs and strengthens your hand in negotiation.</p>
<h2>The decision</h2>
<p>Decide with a checklist, not emotion. We can assess the boat you're considering on the <a href="/en/services/fibreglass-repair/">fibreglass</a> or <a href="/en/services/wooden-boat-refit/">wood</a> side together — message us.</p>
""",
 },
},
{
 "slug": "ahsap-tekne-restorasyon-vaka", "slug_en": "wooden-restoration-case-study",
 "image": "/assets/images/services/ahsap.jpg", "date": "2027-01-06",
 "tr": {
   "category": "Vaka Çalışması",
   "title": "Vaka Çalışması: 1970 Model Klasik Ahşap Yelkenlinin Restorasyonu",
   "excerpt": "Elli yıllık bir ahşap yelkenlinin özgün dokusu korunarak nasıl restore edildiği — süreç, kararlar ve sonuç.",
   "meta_title": "Ahşap Tekne Restorasyonu Vaka Çalışması | Tekne Usta",
   "meta_desc": "Klasik ahşap yelkenli restorasyonu vaka çalışması: durum değerlendirmesi, çürük onarımı, kalafat, vernik ve özgün dokunun korunması. Adım adım süreç.",
   "body": """
<p>Bazen bir tekne sadece bir araç değil, bir hikâyedir. Bu vaka çalışmasında, 1970 yapımı klasik bir ahşap yelkenlinin özgün karakteri korunarak nasıl yeniden hayata döndürüldüğünü paylaşıyoruz.</p>
<h2>Başlangıç: durum değerlendirmesi</h2>
<p>Tekne bize su alan derzler, yer yer çürümüş kaplama ve solmuş vernikle geldi. İlk adım, hasarın haritasını çıkarmak oldu: hangi bölgeler yapısal, hangileri kozmetikti? Aceleye getirilmeyen bir keşif, doğru planın temelidir.</p>
<h2>Yapısal onarım</h2>
<p>Çürüyen bölgeler sağlam ahşaba kadar temizlendi; mümkün olan yerde özgün ahşap türüyle ekleme, gereken yerde epoksi güçlendirme yapıldı. Amaç tekneyi "yeni" göstermek değil, karakterini koruyarak sağlamlaştırmaktı.</p>
<h2>Kalafat ve su sızdırmazlık</h2>
<p>Açılan derzler <a href="/blog/kalafat-nedir/">kalafatla</a> yeniden yapıldı; teknenin ahşap hareketini karşılayacak esneklikte bir sistem seçildi.</p>
<h2>Vernik ve bitiş</h2>
<p>Yüzey ahşaba kadar açıldı ve çok katlı <a href="/blog/ahsap-tekne-vernik-bakimi/">vernik</a> uygulandı. Sonuçta, elli yıllık ruhunu koruyan ama yeniden suya layık bir tekne ortaya çıktı.</p>
<h2>Sonuç</h2>
<p>Sahibinin ifadesiyle "tarihi doku tamamen korundu." Klasik ahşap teknenizin restorasyonu için <a href="/hizmetler/ahsap-tekne-renovasyonu/">ahşap tekne renovasyonu</a> hizmetimiz kapsamında ücretsiz keşifle başlayalım.</p>
""",
 },
 "en": {
   "category": "Case Study",
   "title": "Case Study: Restoring a 1970 Classic Wooden Sailboat",
   "excerpt": "How a fifty-year-old wooden sailboat was restored while preserving its original character — the process, decisions and result.",
   "meta_title": "Wooden Boat Restoration Case Study | Tekne Usta",
   "meta_desc": "Classic wooden sailboat restoration case study: condition assessment, rot repair, caulking, varnish and preserving original character. A step-by-step process.",
   "body": """
<p>Sometimes a boat isn't just a vessel but a story. In this case study we share how a 1970 classic wooden sailboat was brought back to life while preserving its original character.</p>
<h2>The start: condition assessment</h2>
<p>The boat came to us with leaking seams, patches of rotten planking and faded varnish. The first step was to map the damage: which areas were structural and which cosmetic? An unhurried survey is the basis of the right plan.</p>
<h2>Structural repair</h2>
<p>Rotten areas were cut back to sound wood; where possible we grafted in the original timber species, and reinforced with epoxy where needed. The aim wasn't to make the boat look "new" but to strengthen it while keeping its character.</p>
<h2>Caulking and watertightness</h2>
<p>The opened seams were remade with <a href="/en/blog/caulking-explained/">caulking</a>, choosing a system flexible enough to accommodate the wood's movement.</p>
<h2>Varnish and finish</h2>
<p>The surface was taken back to bare wood and multi-coat <a href="/en/blog/wooden-boat-varnish-care/">varnish</a> applied. The result: a boat that keeps its fifty-year-old soul but is seaworthy again.</p>
<h2>The result</h2>
<p>In the owner's words, "the historic character was completely preserved." To restore your classic wooden boat, let's start with a free survey under our <a href="/en/services/wooden-boat-refit/">wooden boat refit</a> service.</p>
""",
 },
},
{
 "slug": "fiberglas-tekne-bakimi", "slug_en": "fibreglass-boat-care",
 "image": "/assets/images/services/fiberglas.jpg", "date": "2027-01-20",
 "tr": {
   "category": "Fiberglas",
   "title": "Fiberglas Tekne Bakımı: Yıllarca Sağlam Kalması İçin",
   "excerpt": "Fiber tekneyi neler yıpratır ve düzenli bakımda nelere dikkat edilir? Jelkottan karinaya temel bakım rehberi.",
   "meta_title": "Fiberglas Tekne Bakımı Rehberi | Tekne Usta",
   "meta_desc": "Fiberglas tekne bakımı: jelkot koruma, karina ve antifouling, osmoz önleme ve düzenli temizlik. Fiber teknenizi yıllarca sağlam tutmanın yolları.",
   "body": """
<p>Fiberglas tekneler dayanıklıdır ama "bakım istemez" değildir. Düzenli, basit bakım; büyük ve pahalı onarımların önündeki en iyi settir.</p>
<h2>Jelkotu koruyun</h2>
<p>Güneş ve tuz jelkotu zamanla matlaştırır. Düzenli yıkama, ara ara cila/koruyucu ve yılda bir parlatma; rengi ve parlaklığı korur. Solmayı çok ilerletmeden müdahale, <a href="/blog/gelcoat-yenileme/">komple gelcoat yenilemeyi</a> yıllarca erteler.</p>
<h2>Karina ve su altı</h2>
<p>Sezon başında <a href="/hizmetler/tekne-boyama-antifouling/">antifouling</a> kontrolü, sezon boyunca kirlenme takibi ve karadayken <a href="/blog/osmoz-belirtileri/">osmoz belirtisi</a> taraması şart. Küçük çizik ve çatlaklar büyümeden onarılmalı.</p>
<h2>Rutin kontroller</h2>
<p>Güverte donanımı çevresindeki gerilim çatlakları, sintine nemi ve conta/sızdırmazlıklar düzenli kontrol edilmeli. Erken fark edilen sorun, ucuz sorundur.</p>
<p>Teknenizin genel durumunu değerlendirmek için <a href="/hizmetler/fiberglas-onarim/">fiberglas onarım</a> hizmetimiz kapsamında ücretsiz keşif yapıyor, bakım planı çıkarıyoruz.</p>
""",
 },
 "en": {
   "category": "Fibreglass",
   "title": "Fibreglass Boat Care: Keeping It Sound for Years",
   "excerpt": "What wears a fibreglass boat and what to watch in regular care? A basic care guide from gelcoat to hull.",
   "meta_title": "Fibreglass Boat Care Guide | Tekne Usta",
   "meta_desc": "Fibreglass boat care: protecting gelcoat, hull and antifouling, preventing osmosis and regular cleaning. How to keep your fibreglass boat sound for years.",
   "body": """
<p>Fibreglass boats are durable, but not "maintenance-free". Regular, simple care is the best defence against big, expensive repairs.</p>
<h2>Protect the gelcoat</h2>
<p>Sun and salt dull the gelcoat over time. Regular washing, occasional wax/protectant and a yearly polish keep the colour and gloss. Acting before fading advances postpones a full <a href="/en/blog/gelcoat-renewal/">gelcoat renewal</a> for years.</p>
<h2>Hull and underwater</h2>
<p>Check <a href="/en/services/boat-painting-antifouling/">antifouling</a> at season start, monitor growth through the season and scan for <a href="/en/blog/osmosis-symptoms/">osmosis signs</a> when ashore. Repair small scratches and cracks before they grow.</p>
<h2>Routine checks</h2>
<p>Regularly check stress cracks around deck hardware, bilge moisture and seals. A problem caught early is a cheap problem.</p>
<p>To assess your boat's overall condition, we do a free survey and produce a care plan under our <a href="/en/services/fibreglass-repair/">fibreglass repair</a> service.</p>
""",
 },
},
{
 "slug": "polyester-vs-epoksi-recine", "slug_en": "polyester-vs-epoxy-resin",
 "image": "/assets/images/services/fiberglas.jpg", "date": "2027-02-03",
 "tr": {
   "category": "Fiberglas",
   "title": "Polyester mi Epoksi Reçine mi? Onarımda Doğru Seçim",
   "excerpt": "Fiberglas onarımda polyester ve epoksi reçine arasındaki fark: yapışma, dayanıklılık, su geçirmezlik ve maliyet.",
   "meta_title": "Polyester vs Epoksi Reçine: Onarım Rehberi | Tekne Usta",
   "meta_desc": "Fiberglas onarımda polyester ve epoksi reçine karşılaştırması: yapışma gücü, su geçirmezlik, dayanıklılık ve maliyet. Hangi reçine ne zaman kullanılır?",
   "body": """
<p>Fiberglas onarımın kalitesi büyük ölçüde doğru reçine seçimine bağlıdır. İki ana seçenek vardır: polyester ve epoksi. İkisinin de yeri farklıdır.</p>
<h2>Polyester reçine</h2>
<p>Teknelerin çoğu polyesterle üretilir; onarımda uyumlu ve ekonomiktir. <strong>Artıları:</strong> düşük maliyet, kolay uygulama, orijinal laminatla uyum. <strong>Sınırı:</strong> yapışma ve su geçirmezliği epoksiye göre daha düşüktür.</p>
<h2>Epoksi reçine</h2>
<p><strong>Artıları:</strong> üstün yapışma, yüksek mukavemet ve mükemmel su geçirmezlik. <a href="/blog/osmoz-nedir-tedavisi/">Osmoz</a> bariyer katında ve yapısal onarımlarda tercih edilir. <strong>Sınırı:</strong> daha pahalıdır ve uygulama koşullarına daha duyarlıdır.</p>
<h2>Hangisi ne zaman?</h2>
<p>Genel kozmetik ve orijinal laminatla uyumlu onarımlarda polyester; su altı, yapısal ve osmoz işlerinde epoksi mantıklıdır. Doğru seçimi teknenin yapısına ve işin türüne göre yaparız.</p>
<p>Onarımınız için doğru reçine sistemini <a href="/hizmetler/fiberglas-onarim/">fiberglas onarım</a> hizmetimiz kapsamında belirliyoruz.</p>
""",
 },
 "en": {
   "category": "Fibreglass",
   "title": "Polyester or Epoxy Resin? The Right Choice for Repair",
   "excerpt": "The difference between polyester and epoxy resin in fibreglass repair: adhesion, durability, waterproofing and cost.",
   "meta_title": "Polyester vs Epoxy Resin: A Repair Guide | Tekne Usta",
   "meta_desc": "Polyester vs epoxy resin in fibreglass repair: adhesion strength, waterproofing, durability and cost. Which resin to use and when.",
   "body": """
<p>The quality of a fibreglass repair largely depends on choosing the right resin. There are two main options: polyester and epoxy. Each has its place.</p>
<h2>Polyester resin</h2>
<p>Most boats are built with polyester; it's compatible and economical in repair. <strong>Pros:</strong> low cost, easy to apply, compatible with the original laminate. <strong>Limit:</strong> lower adhesion and waterproofing than epoxy.</p>
<h2>Epoxy resin</h2>
<p><strong>Pros:</strong> superior adhesion, high strength and excellent waterproofing. Preferred for the <a href="/en/blog/what-is-osmosis-treatment/">osmosis</a> barrier coat and structural repairs. <strong>Limit:</strong> more expensive and more sensitive to application conditions.</p>
<h2>Which and when?</h2>
<p>For general cosmetic repairs compatible with the original laminate, polyester; for underwater, structural and osmosis work, epoxy. We make the right choice for the construction and the job.</p>
<p>We determine the right resin system for your repair under our <a href="/en/services/fibreglass-repair/">fibreglass repair</a> service.</p>
""",
 },
},
{
 "slug": "su-alti-yapisal-onarim", "slug_en": "underwater-structural-repair",
 "image": "/assets/images/services/fiberglas.jpg", "date": "2027-02-17",
 "tr": {
   "category": "Fiberglas",
   "title": "Su Altı Yapısal Onarım: Karina, Omurga ve Bodoslama",
   "excerpt": "Karaya oturma, çarpma veya yapısal hasarda su altı onarım nasıl yapılır? Güvenlik açısından kritik bir konu.",
   "meta_title": "Su Altı Yapısal Onarım Rehberi | Tekne Usta",
   "meta_desc": "Su altı yapısal onarım: karina, omurga ve bodoslama hasarları nasıl onarılır? Karaya oturma ve çarpma sonrası yapısal güçlendirme ve güvenlik.",
   "body": """
<p>Teknenin su altı bölümü, tüm yükü taşıyan bölgedir. Karaya oturma, kayaya çarpma veya yıllar içindeki yorulma; karina, omurga ve bodoslamada yapısal hasar bırakabilir. Bu işler kozmetik değil, güvenlik işidir.</p>
<h2>Yapısal hasar neden ciddidir?</h2>
<p>Su altı yapıdaki bir çatlak veya delaminasyon, su almaya ve zamanla yapının zayıflamasına yol açar. Görünürde küçük bir iz, altında ciddi bir katman ayrışması gizleyebilir.</p>
<h2>Onarım yaklaşımı</h2>
<p>Hasar önce doğru okunur: yüzeysel mi, laminata mı iniyor? Sağlam malzemeye kadar açılır, uygun reçine ve cam elyafıyla <strong>kat kat laminasyon</strong> yapılır. Yük taşıyan bölgelerde <a href="/blog/polyester-vs-epoksi-recine/">epoksi</a> tercih edilir.</p>
<h2>Sonra ne olur?</h2>
<p>Yapısal onarımın ardından yüzey <a href="/blog/fiberglas-catlak-onarimi/">bitiş</a> ve <a href="/hizmetler/tekne-boyama-antifouling/">antifouling</a> ile tamamlanır. Karaya oturma sonrası teknenizi mutlaka kontrol ettirin.</p>
<p>Su altı yapısal onarımlar için <a href="/hizmetler/fiberglas-onarim/">fiberglas onarım</a> hizmetimiz kapsamında değerlendirme yapıyoruz.</p>
""",
 },
 "en": {
   "category": "Fibreglass",
   "title": "Underwater Structural Repair: Hull, Keel and Stem",
   "excerpt": "How is underwater repair done after grounding, impact or structural damage? A matter critical to safety.",
   "meta_title": "Underwater Structural Repair Guide | Tekne Usta",
   "meta_desc": "Underwater structural repair: how hull, keel and stem damage is repaired. Structural reinforcement and safety after grounding and impact.",
   "body": """
<p>A boat's underwater section carries all the load. Grounding, striking a rock or years of fatigue can leave structural damage in the hull, keel and stem. This is not cosmetic work but safety work.</p>
<h2>Why is structural damage serious?</h2>
<p>A crack or delamination in the underwater structure leads to water ingress and, over time, a weakened structure. A small visible mark can hide serious layer separation beneath.</p>
<h2>The repair approach</h2>
<p>The damage is read correctly first: superficial, or into the laminate? It's opened back to sound material and rebuilt with <strong>layer-by-layer lamination</strong> in the right resin and glass. In load-bearing areas, <a href="/en/blog/polyester-vs-epoxy-resin/">epoxy</a> is preferred.</p>
<h2>What comes next?</h2>
<p>After structural repair the surface is completed with <a href="/en/blog/fibreglass-crack-repair/">finishing</a> and <a href="/en/services/boat-painting-antifouling/">antifouling</a>. Always have your boat checked after a grounding.</p>
<p>For underwater structural repairs, we assess under our <a href="/en/services/fibreglass-repair/">fibreglass repair</a> service.</p>
""",
 },
},
{
 "slug": "ahsap-curuk-onarimi", "slug_en": "wood-rot-repair",
 "image": "/assets/images/services/ahsap.jpg", "date": "2027-03-03",
 "tr": {
   "category": "Ahşap",
   "title": "Ahşap Tekne Çürük Onarımı: Nasıl Yapılır, Önlenir mi?",
   "excerpt": "Ahşap teknede çürük neden oluşur, nasıl fark edilir ve onarılır? Çürüğü büyümeden durdurmanın yolları.",
   "meta_title": "Ahşap Tekne Çürük Onarımı Rehberi | Tekne Usta",
   "meta_desc": "Ahşap tekne çürük onarımı: çürük nedenleri, belirtileri, temizlik ve epoksi/ahşap ekleme ile onarım. Çürüğü önleme ve durdurma yolları.",
   "body": """
<p>Çürük, ahşap teknenin en sinsi düşmanıdır. Nemin sıkıştığı, havalanmayan bölgelerde başlar ve fark edilmezse yapısal elemanlara yayılır. İyi haber: erken müdahaleyle durdurulabilir ve onarılabilir.</p>
<h2>Çürük neden oluşur?</h2>
<p>Sürekli nem + havasızlık = mantar faaliyeti. Genelde güverte-gövde birleşimleri, sintine, direk dibi ve su biriken köşelerde başlar. Kararma, yumuşama ve kolay dağılan lif çürüğün işaretidir.</p>
<h2>Onarım adımları</h2>
<p>Çürük bölge <strong>sağlam ahşaba kadar</strong> temizlenir (yarım bırakmak çürüğü geri getirir). Ardından mümkünse özgün ahşap türüyle ekleme, gereken yerde <a href="/blog/epoksi-ile-ahsap-guclendirme/">epoksi ile güçlendirme</a> yapılır. Kaplamaysa <a href="/blog/kalafat-nedir/">kalafat</a> ile su sızdırmazlık tamamlanır.</p>
<h2>Önleme</h2>
<p>İyi havalandırma, sağlam vernik/boya ve su biriken noktaların kontrolü çürüğü büyük ölçüde önler.</p>
<p>Çürük onarımını <a href="/hizmetler/ahsap-tekne-renovasyonu/">ahşap tekne renovasyonu</a> hizmetimiz kapsamında yapıyoruz; kapsam keşifte netleşir.</p>
""",
 },
 "en": {
   "category": "Wood",
   "title": "Wooden Boat Rot Repair: How It's Done and Prevented",
   "excerpt": "Why does rot form in a wooden boat, how do you spot it and repair it? How to stop rot before it spreads.",
   "meta_title": "Wooden Boat Rot Repair Guide | Tekne Usta",
   "meta_desc": "Wooden boat rot repair: causes, symptoms, cleaning out and repair with epoxy/wood grafts. How to prevent and stop rot.",
   "body": """
<p>Rot is the wooden boat's most insidious enemy. It starts where moisture is trapped and unventilated, and spreads to structural members if missed. The good news: caught early, it can be stopped and repaired.</p>
<h2>Why does rot form?</h2>
<p>Constant moisture + no airflow = fungal activity. It usually starts at deck-hull joints, the bilge, mast step and corners where water pools. Darkening, softness and easily crumbling fibres are signs of rot.</p>
<h2>Repair steps</h2>
<p>The rotten area is cleaned out <strong>back to sound wood</strong> (leaving any brings rot back). Then a graft in the original species where possible, and <a href="/en/blog/epoxy-wood-reinforcement/">epoxy reinforcement</a> where needed. On planking, watertightness is completed with <a href="/en/blog/caulking-explained/">caulking</a>.</p>
<h2>Prevention</h2>
<p>Good ventilation, sound varnish/paint and checking points where water pools largely prevent rot.</p>
<p>We do rot repair under our <a href="/en/services/wooden-boat-refit/">wooden boat refit</a> service; scope is confirmed at the survey.</p>
""",
 },
},
{
 "slug": "epoksi-ile-ahsap-guclendirme", "slug_en": "epoxy-wood-reinforcement",
 "image": "/assets/images/services/ahsap.jpg", "date": "2027-03-17",
 "tr": {
   "category": "Ahşap",
   "title": "Epoksi ile Ahşap Güçlendirme: Gelenek ve Modern Bir Arada",
   "excerpt": "Epoksi, ahşap teknede nasıl kullanılır? Emdirme, dolgu ve laminasyonla güçlendirmenin avantajları ve sınırları.",
   "meta_title": "Epoksi ile Ahşap Tekne Güçlendirme | Tekne Usta",
   "meta_desc": "Epoksi ile ahşap güçlendirme: emdirme, dolgu ve laminasyon teknikleri. Ahşap teknede epoksinin avantajları, sınırları ve doğru kullanımı.",
   "body": """
<p>Modern epoksi, ahşap tekneciliğe yeni bir güç kattı. Doğru kullanıldığında geleneksel ahşap işçiliğini bozmadan tekneyi güçlendirir ve su geçirmezliği artırır.</p>
<h2>Epoksi ne işe yarar?</h2>
<p><strong>Emdirme:</strong> zayıflamış ama sağlam ahşabı içten güçlendirir. <strong>Dolgu:</strong> boşluk ve çatlakları yapısal olarak kapatır. <strong>Laminasyon:</strong> cam elyafıyla birlikte kritik bölgelere ek mukavemet verir.</p>
<h2>Avantajları</h2>
<p>Yüksek yapışma, mükemmel su geçirmezlik ve dayanıklılık. <a href="/blog/ahsap-curuk-onarimi/">Çürük onarımında</a> temizlenen bölgenin yeniden kurulmasında çok etkilidir.</p>
<h2>Sınırları ve doğru kullanım</h2>
<p>Epoksi her yere uygun değildir; ahşabın nefes almasını ve doğal hareketini kısıtlayabilir. Bu yüzden nerede epoksi, nerede geleneksel yöntem kullanılacağı deneyim ister. Yanlış yerde epoksi, altta nem hapsedip çürüğü gizleyebilir.</p>
<p>Ahşabınızda epoksi güçlendirmenin doğru olup olmadığını <a href="/hizmetler/ahsap-tekne-renovasyonu/">ahşap tekne renovasyonu</a> hizmetimiz kapsamında değerlendiriyoruz.</p>
""",
 },
 "en": {
   "category": "Wood",
   "title": "Epoxy Wood Reinforcement: Tradition and Modern Combined",
   "excerpt": "How is epoxy used in a wooden boat? The advantages and limits of reinforcement by saturation, filling and lamination.",
   "meta_title": "Epoxy Wooden Boat Reinforcement | Tekne Usta",
   "meta_desc": "Epoxy wood reinforcement: saturation, filling and lamination techniques. The advantages, limits and correct use of epoxy in a wooden boat.",
   "body": """
<p>Modern epoxy has added new strength to wooden boatbuilding. Used correctly, it strengthens the boat and improves waterproofing without spoiling traditional woodwork.</p>
<h2>What does epoxy do?</h2>
<p><strong>Saturation:</strong> strengthens weakened but sound wood from within. <strong>Filling:</strong> structurally closes voids and cracks. <strong>Lamination:</strong> with glass fibre, adds strength to critical areas.</p>
<h2>Advantages</h2>
<p>High adhesion, excellent waterproofing and durability. It's very effective for rebuilding a cleaned area in <a href="/en/blog/wood-rot-repair/">rot repair</a>.</p>
<h2>Limits and correct use</h2>
<p>Epoxy isn't right everywhere; it can restrict the wood's ability to breathe and move naturally. So where to use epoxy and where traditional methods takes experience. Epoxy in the wrong place can trap moisture beneath and hide rot.</p>
<p>We assess whether epoxy reinforcement is right for your wood under our <a href="/en/services/wooden-boat-refit/">wooden boat refit</a> service.</p>
""",
 },
},
{
 "slug": "ahsap-tekne-boyama", "slug_en": "wooden-boat-painting",
 "image": "/assets/images/services/ahsap.jpg", "date": "2027-03-31",
 "tr": {
   "category": "Ahşap",
   "title": "Ahşap Tekne Boyama: Vernik mi, Boya mı, Ne Zaman?",
   "excerpt": "Ahşap teknede boya ile vernik arasındaki fark, doğru zemin hazırlığı ve uzun ömürlü bir bitiş için ipuçları.",
   "meta_title": "Ahşap Tekne Boyama Rehberi | Tekne Usta",
   "meta_desc": "Ahşap tekne boyama: boya ile vernik farkı, zemin hazırlığı, astar ve kat sayısı. Ahşap teknede uzun ömürlü ve korunaklı bir bitiş için ipuçları.",
   "body": """
<p>Ahşap teknede yüzey bitişi hem estetik hem koruma işidir. Boya ve vernik farklı amaçlara hizmet eder; doğru tercih ahşabın durumuna ve istediğiniz görünüme bağlıdır.</p>
<h2>Boya mı, vernik mi?</h2>
<p><strong>Vernik:</strong> ahşabın doğal dokusunu gösterir, klasik ve sıcak bir görünüm verir; ama daha çok bakım ister. <strong>Boya:</strong> daha korunaklı ve dayanıklı bir yüzeydir, ahşabı UV'den daha iyi korur; doku görünmez. Gövdenin çok yıpranmış bölgelerinde boya sık tercih edilir.</p>
<h2>Zemin hazırlığı belirleyicidir</h2>
<p>Kalıcı bir bitişin sırrı boyada değil hazırlıktadır: eski katmanların doğru sökülmesi, ahşabın kuru ve sağlam olması, uygun astar. Nemli veya çürük ahşaba atılan boya kısa sürede kabarır.</p>
<h2>Kat sayısı ve bakım</h2>
<p>Çok katlı, ince uygulamalar en dayanıklı sonucu verir. Her iki yöntemde de düzenli <a href="/blog/ahsap-tekne-vernik-bakimi/">ara bakım</a> ömrü uzatır.</p>
<p>Ahşap teknenizin boyama/vernik işini <a href="/hizmetler/ahsap-tekne-renovasyonu/">ahşap tekne renovasyonu</a> hizmetimiz kapsamında yapıyoruz.</p>
""",
 },
 "en": {
   "category": "Wood",
   "title": "Wooden Boat Painting: Varnish or Paint, and When?",
   "excerpt": "The difference between paint and varnish on a wooden boat, correct surface prep and tips for a long-lasting finish.",
   "meta_title": "Wooden Boat Painting Guide | Tekne Usta",
   "meta_desc": "Wooden boat painting: paint vs varnish, surface prep, primer and coat count. Tips for a long-lasting, protective finish on a wooden boat.",
   "body": """
<p>Surface finishing on a wooden boat is both aesthetic and protective. Paint and varnish serve different aims; the right choice depends on the wood's condition and the look you want.</p>
<h2>Paint or varnish?</h2>
<p><strong>Varnish:</strong> shows the wood's natural grain, gives a classic, warm look, but needs more care. <strong>Paint:</strong> a more protective, durable surface that shields the wood from UV better; the grain doesn't show. On heavily worn hull areas, paint is often preferred.</p>
<h2>Surface prep is decisive</h2>
<p>The secret to a lasting finish is in the prep, not the paint: correctly stripping old layers, dry and sound wood, the right primer. Paint over damp or rotten wood soon blisters.</p>
<h2>Coat count and care</h2>
<p>Many thin coats give the most durable result. In both methods, regular <a href="/en/blog/wooden-boat-varnish-care/">maintenance coats</a> extend the life.</p>
<p>We do your wooden boat's painting/varnish under our <a href="/en/services/wooden-boat-refit/">wooden boat refit</a> service.</p>
""",
 },
},
{
 "slug": "klasik-tekne-turleri", "slug_en": "classic-boat-types",
 "image": "/assets/images/services/ahsap.jpg", "date": "2027-04-14",
 "tr": {
   "category": "Ahşap",
   "title": "Klasik Ahşap Tekne Türleri: Tirhandil, Gulet, Aynakıç",
   "excerpt": "Türk denizciliğinin klasik ahşap tekne tipleri ve her birinin karakteri, kullanımı ve bakım özellikleri.",
   "meta_title": "Klasik Ahşap Tekne Türleri Rehberi | Tekne Usta",
   "meta_desc": "Klasik ahşap tekne türleri: tirhandil, gulet, aynakıç ve tknelerin karakteri, kullanımı ve bakım özellikleri. Türk denizciliğinin ahşap mirası.",
   "body": """
<p>Türk denizciliğinin ahşap mirası zengindir. Her tekne tipi, yörenin denizine ve kullanımına göre şekillenmiştir. İşte en bilinen klasik ahşap tekne türleri ve karakterleri.</p>
<h2>Tirhandil</h2>
<p>İki ucu sivri (aynasız), zarif hatlı, denize dayanıklı klasik bir tekne tipidir. Yelken ve gezi için sevilir; estetiği ve deniz tutuşuyla klasik tekne meraklılarının favorisidir.</p>
<h2>Gulet</h2>
<p>Geniş, konforlu, aynakıçlı klasik gezi teknesi. Mavi yolculukların simgesidir; büyük iç hacmi ve güvertesiyle konaklamalı seyir için idealdir.</p>
<h2>Aynakıç ve diğerleri</h2>
<p>Aynakıç (düz kıç aynası olan) tekneler, ile bölgesel çeşitler (piyade, çektirme vb.) farklı kullanım ve estetik sunar. Her tip, kendi yapısına uygun bakım ister.</p>
<h2>Bakım ortak paydası</h2>
<p>Tipi ne olursa olsun, klasik ahşap tekneler düzenli <a href="/blog/ahsap-tekne-vernik-bakimi/">vernik</a>, <a href="/blog/kalafat-nedir/">kalafat</a> ve çürük kontrolü ister. Bu tekneleri özgün dokusunu koruyarak <a href="/hizmetler/ahsap-tekne-renovasyonu/">restore ediyoruz</a>.</p>
""",
 },
 "en": {
   "category": "Wood",
   "title": "Classic Wooden Boat Types: Tirhandil, Gulet, Transom",
   "excerpt": "The classic wooden boat types of Turkish seafaring and each one's character, use and maintenance traits.",
   "meta_title": "Classic Wooden Boat Types Guide | Tekne Usta",
   "meta_desc": "Classic wooden boat types: tirhandil, gulet, transom-stern boats and their character, use and maintenance traits. Turkish seafaring's wooden heritage.",
   "body": """
<p>Turkish seafaring's wooden heritage is rich. Each boat type is shaped by its region's sea and use. Here are the best-known classic wooden boat types and their characters.</p>
<h2>Tirhandil</h2>
<p>A double-ended (no transom), elegantly lined, sea-kindly classic type. Loved for sailing and cruising; a favourite of classic-boat enthusiasts for its aesthetics and sea-keeping.</p>
<h2>Gulet</h2>
<p>A broad, comfortable, transom-sterned classic cruiser. The symbol of "blue voyage" cruising; its large interior volume and deck make it ideal for overnight cruising.</p>
<h2>Transom-stern and others</h2>
<p>Transom-sterned boats and regional variants offer different uses and aesthetics. Each type needs care suited to its construction.</p>
<h2>The common thread: care</h2>
<p>Whatever the type, classic wooden boats need regular <a href="/en/blog/wooden-boat-varnish-care/">varnish</a>, <a href="/en/blog/caulking-explained/">caulking</a> and rot checks. We <a href="/en/services/wooden-boat-refit/">restore</a> these boats while preserving their original character.</p>
""",
 },
},
{
 "slug": "2k-poliuretan-boya", "slug_en": "2k-polyurethane-paint",
 "image": "/assets/images/services/boya.jpg", "date": "2027-04-28",
 "tr": {
   "category": "Boya",
   "title": "2K Poliüretan Boya Nedir? Neden Süperyat Kalitesi?",
   "excerpt": "İki bileşenli (2K) poliüretan boya nedir, tek bileşenliye göre farkı ne ve neden dayanıklı bir bitiş sağlar?",
   "meta_title": "2K Poliüretan Boya Nedir? Rehber | Tekne Usta",
   "meta_desc": "2K poliüretan boya nedir, tek bileşenli boyaya göre farkı ne? İki bileşenli boyanın dayanıklılığı, parlaklığı, uygulama koşulları ve avantajları.",
   "body": """
<p>Süperyatların derin, cam gibi parlaklığının sırrı çoğu zaman iki bileşenli (2K) poliüretan boyadır. Peki bu boya nedir ve neden bu kadar iyi bir sonuç verir?</p>
<h2>2K ne demek?</h2>
<p>2K, boyanın bir ana bileşen ve bir sertleştiriciden oluşması demektir. Karıştırıldığında kimyasal olarak kürlenir ve çok sert, dayanıklı bir film oluşturur. Tek bileşenli (1K) boyalar ise havayla kurur ve daha yumuşak kalır.</p>
<h2>Avantajları</h2>
<p>Yüksek ve kalıcı parlaklık, mükemmel UV ve kimyasal direnç, uzun ömür. Doğru uygulandığında yıllarca ilk günkü gibi durur.</p>
<h2>Uygulama koşulları</h2>
<p>2K sistemler ustalık ister: doğru karışım oranı, sıcaklık/nem koşulları, tozsuz ortam ve uygun ekipman. Bu yüzden kaliteli bir 2K uygulaması yüzey hazırlığı ve işçilikle bir bütündür — <a href="/blog/tekne-boyama-maliyeti/">maliyeti</a> de bu yüzden 1K'ya göre yüksektir.</p>
<p>Teknenize 2K poliüretan uygulamasını <a href="/hizmetler/tekne-boyama-antifouling/">tekne boyama</a> hizmetimiz kapsamında yapıyoruz.</p>
""",
 },
 "en": {
   "category": "Painting",
   "title": "What Is 2K Polyurethane Paint? Why Superyacht Quality?",
   "excerpt": "What is two-part (2K) polyurethane paint, how does it differ from single-part, and why does it give a durable finish?",
   "meta_title": "What Is 2K Polyurethane Paint? A Guide | Tekne Usta",
   "meta_desc": "What is 2K polyurethane paint and how does it differ from single-part paint? The durability, gloss, application conditions and advantages of two-part paint.",
   "body": """
<p>The secret to superyachts' deep, glass-like gloss is often two-part (2K) polyurethane paint. So what is it and why does it give such a good result?</p>
<h2>What does 2K mean?</h2>
<p>2K means the paint consists of a base and a hardener. Mixed, it cures chemically and forms a very hard, durable film. Single-part (1K) paints dry with air and stay softer.</p>
<h2>Advantages</h2>
<p>High, lasting gloss, excellent UV and chemical resistance, long life. Applied correctly, it stays like new for years.</p>
<h2>Application conditions</h2>
<p>2K systems take skill: the right mix ratio, temperature/humidity conditions, a dust-free environment and proper equipment. So a quality 2K job is a whole with surface prep and workmanship — which is why its <a href="/en/blog/boat-painting-cost/">cost</a> is higher than 1K.</p>
<p>We apply 2K polyurethane to your boat under our <a href="/en/services/boat-painting-antifouling/">boat painting</a> service.</p>
""",
 },
},
{
 "slug": "tekne-renk-degisimi", "slug_en": "boat-colour-change",
 "image": "/assets/images/services/boya.jpg", "date": "2027-05-12",
 "tr": {
   "category": "Boya",
   "title": "Tekne Renk Değişimi: Yeni Bir Kimlik İçin Bilmeniz Gerekenler",
   "excerpt": "Teknenizin dış cephe rengini değiştirmek: süreç, dikkat edilmesi gerekenler ve kalıcı bir sonuç için ipuçları.",
   "meta_title": "Tekne Renk Değişimi Rehberi | Tekne Usta",
   "meta_desc": "Tekne renk değişimi: dış cephe boyama süreci, koyu renklerde ısı, astar sistemi ve kalıcı bir sonuç için dikkat edilmesi gerekenler.",
   "body": """
<p>Bir renk değişimi, tekneye tümüyle yeni bir kimlik kazandırır. Ama iyi bir sonuç, sadece rengi seçmekten ibaret değildir; doğru sistem ve işçilik gerekir.</p>
<h2>Süreç</h2>
<p>Mevcut yüzey değerlendirilir, hazırlanır ve uygun <strong>astar sistemi</strong> uygulanır. Renk değişiminde astar kritiktir çünkü yeni rengin örtücülüğünü ve tutuşunu belirler. Ardından çok katlı boya uygulanır.</p>
<h2>Koyu renklere dikkat</h2>
<p>Koyu renkler şık durur ama güneşte daha çok ısınır ve her kusuru daha belirgin gösterir. Koyu renk seçerken yüzey hazırlığı daha da önemlidir; ayrıca ısı, altındaki malzemeyi etkileyebilir.</p>
<h2>Kalıcı sonuç</h2>
<p>Renk değişimi çoğu zaman <a href="/blog/2k-poliuretan-boya/">2K poliüretan</a> ile yapılır. İsim ve grafiklerin de yeni renge göre <a href="/blog/tekne-ismi-grafik-uygulamasi/">yeniden planlanması</a> gerekir.</p>
<p>Teknenizin renk değişimini <a href="/hizmetler/tekne-boyama-antifouling/">tekne boyama</a> hizmetimiz kapsamında yapıyor, keşifte net teklif veriyoruz.</p>
""",
 },
 "en": {
   "category": "Painting",
   "title": "Boat Colour Change: What to Know for a New Identity",
   "excerpt": "Changing your boat's topside colour: the process, what to watch and tips for a lasting result.",
   "meta_title": "Boat Colour Change Guide | Tekne Usta",
   "meta_desc": "Boat colour change: the topside painting process, heat in dark colours, primer system and what to watch for a lasting result.",
   "body": """
<p>A colour change gives a boat an entirely new identity. But a good result is more than choosing the colour; it takes the right system and workmanship.</p>
<h2>The process</h2>
<p>The existing surface is assessed, prepared and the right <strong>primer system</strong> applied. Primer is critical in a colour change because it determines the new colour's coverage and adhesion. Then multi-coat paint is applied.</p>
<h2>Beware dark colours</h2>
<p>Dark colours look elegant but heat up more in the sun and show every flaw. When choosing dark, surface prep matters even more; heat can also affect the material beneath.</p>
<h2>A lasting result</h2>
<p>A colour change is usually done in <a href="/en/blog/2k-polyurethane-paint/">2K polyurethane</a>. Names and graphics also need <a href="/en/blog/boat-name-graphics/">replanning</a> for the new colour.</p>
<p>We do your boat's colour change under our <a href="/en/services/boat-painting-antifouling/">boat painting</a> service and give a firm quote at the survey.</p>
""",
 },
},
{
 "slug": "su-hatti-boyama", "slug_en": "waterline-boot-stripe",
 "image": "/assets/images/services/boya.jpg", "date": "2027-05-26",
 "tr": {
   "category": "Boya",
   "title": "Su Hattı ve Kılavuz Şerit (Boot Stripe) Boyama",
   "excerpt": "Su hattı boyası neden önemli, kılavuz şerit nasıl temiz uygulanır ve neden ayrı bir özen ister?",
   "meta_title": "Su Hattı ve Kılavuz Şerit Boyama Rehberi | Tekne Usta",
   "meta_desc": "Su hattı ve kılavuz şerit (boot stripe) boyama: doğru hat, temiz maskeleme, dayanıklı boya ve su hattının neden ayrı özen istediği.",
   "body": """
<p>Kılavuz şerit (boot stripe), teknenin su hattını vurgulayan ince renkli bandtır. Küçük görünse de hem estetiği hem de su hattının en yıpranan bölgesini korumasıyla önemlidir.</p>
<h2>Neden ayrı özen ister?</h2>
<p>Su hattı, teknenin sürekli ıslak-kuru döngüsünde kaldığı, kir ve deniz canlılarının en çok biriktiği bölgedir. Buradaki boya daha çok aşınır; bu yüzden dayanıklı bir sistem ve ekstra kat önerilir.</p>
<h2>Temiz hat: maskeleme</h2>
<p>Kılavuz şeridin güzelliği, çizgilerin keskinliğindedir. Doğru hat belirleme, kaliteli maskeleme bandı ve boya akmadan bandın doğru zamanda alınması; temiz bir sonucun sırrıdır.</p>
<h2>Renk ve genişlik</h2>
<p>Şeridin rengi ve genişliği, teknenin hattını uzun veya dengeli gösterebilir. Gövde rengi ve <a href="/blog/tekne-ismi-grafik-uygulamasi/">grafiklerle</a> uyumlu seçilmelidir.</p>
<p>Su hattı ve kılavuz şerit uygulamasını <a href="/hizmetler/tekne-boyama-antifouling/">tekne boyama</a> hizmetimiz kapsamında, antifouling yenileme ile birlikte planlıyoruz.</p>
""",
 },
 "en": {
   "category": "Painting",
   "title": "Waterline and Boot Stripe Painting",
   "excerpt": "Why does waterline paint matter, how is a boot stripe applied cleanly, and why does it need extra care?",
   "meta_title": "Waterline and Boot Stripe Painting Guide | Tekne Usta",
   "meta_desc": "Waterline and boot stripe painting: the right line, clean masking, durable paint and why the waterline needs extra care.",
   "body": """
<p>The boot stripe is the thin coloured band emphasising a boat's waterline. Small as it looks, it matters both for looks and for protecting the waterline — the most worn zone.</p>
<h2>Why extra care?</h2>
<p>The waterline sits in a constant wet-dry cycle and is where dirt and growth build up most. Paint here wears faster; so a durable system and an extra coat are recommended.</p>
<h2>A clean line: masking</h2>
<p>The beauty of a boot stripe is in the sharpness of the lines. Setting the right line, quality masking tape and removing the tape at the right moment before the paint runs — that's the secret to a clean result.</p>
<h2>Colour and width</h2>
<p>The stripe's colour and width can make the boat's lines look longer or balanced. It should be chosen to harmonise with the hull colour and <a href="/en/blog/boat-name-graphics/">graphics</a>.</p>
<p>We plan waterline and boot stripe work under our <a href="/en/services/boat-painting-antifouling/">boat painting</a> service, alongside antifouling renewal.</p>
""",
 },
},
{
 "slug": "teak-derz-yenileme", "slug_en": "teak-seam-renewal",
 "image": "/assets/images/services/ic-mekan.jpg", "date": "2027-06-09",
 "tr": {
   "category": "Teak",
   "title": "Teak Derz Yenileme: Su Sızdırmazlığı Geri Kazanmak",
   "excerpt": "Teak güvertede siyah derzler neden açılır, ne zaman yenilenmeli ve süreç nasıl işler?",
   "meta_title": "Teak Derz Yenileme Rehberi | Tekne Usta",
   "meta_desc": "Teak derz yenileme: siyah derzlerin açılma nedenleri, ne zaman yenilenmeli ve söküp yeniden yapma süreci. Teak güvertede su sızdırmazlık.",
   "body": """
<p>Teak güvertenin siyah derzleri sadece estetik değildir; su sızdırmazlığın anahtarıdır. Derzler açıldığında su, teakın altındaki yapıya sızar ve ciddi sorunlara yol açar.</p>
<h2>Derzler neden açılır?</h2>
<p>UV, ısı ve teakın doğal hareketi zamanla derz malzemesini çatlatır, kabartır veya teak seviyesinin altına düşürür. Ayrıca yanlış temizlik (sert fırça, agresif kimyasal) derzleri hızla yıpratır.</p>
<h2>Ne zaman yenilenmeli?</h2>
<p>Derzler çatlamış, kalkmış veya su geçiriyorsa yenileme zamanı gelmiştir. Küçük sorunları ertelemek, alttaki ahşabın veya yapının zarar görmesine yol açar.</p>
<h2>Süreç</h2>
<p>Eski derz malzemesi tamamen sökülür, kanal temizlenir ve uygun esnek dolguyla yeniden yapılır. Teak yeterince kalınsa sadece derz yenileme; inceldiyse <a href="/blog/teak-guverte-bakimi/">komple döşeme</a> öneririz.</p>
<p>Teak derz yenilemeyi <a href="/hizmetler/teak-guverte-doseme/">teak güverte döşeme</a> hizmetimiz kapsamında yapıyoruz.</p>
""",
 },
 "en": {
   "category": "Teak",
   "title": "Teak Seam Renewal: Restoring Watertightness",
   "excerpt": "Why do the black seams in a teak deck open, when should they be renewed, and how does the process work?",
   "meta_title": "Teak Seam Renewal Guide | Tekne Usta",
   "meta_desc": "Teak seam renewal: why black seams open, when to renew them and the process of removing and remaking. Watertightness in a teak deck.",
   "body": """
<p>A teak deck's black seams aren't just aesthetic; they're the key to watertightness. When seams open, water seeps to the structure beneath the teak and causes serious problems.</p>
<h2>Why do seams open?</h2>
<p>UV, heat and teak's natural movement crack, lift or drop the seam material below the teak level over time. Wrong cleaning (stiff brush, aggressive chemicals) also wears seams fast.</p>
<h2>When to renew?</h2>
<p>If seams are cracked, lifted or leaking, it's time to renew. Postponing small problems damages the wood or structure beneath.</p>
<h2>The process</h2>
<p>The old seam material is fully removed, the groove cleaned and remade with the right flexible sealant. If the teak is thick enough, seam renewal alone; if thinned, we recommend a <a href="/en/blog/teak-deck-maintenance/">full deck</a>.</p>
<p>We do teak seam renewal under our <a href="/en/services/teak-deck/">teak decking</a> service.</p>
""",
 },
},
{
 "slug": "teak-guverte-fiyatlari", "slug_en": "teak-deck-cost",
 "image": "/assets/images/services/ic-mekan.jpg", "date": "2027-06-23",
 "tr": {
   "category": "Teak",
   "title": "Teak Güverte Döşeme Fiyatını Ne Belirler?",
   "excerpt": "Teak güverte maliyeti neye göre değişir? Alan, malzeme (doğal/sentetik), derz ve işçiliğin fiyata etkisi.",
   "meta_title": "Teak Güverte Döşeme Fiyatını Ne Belirler? | Tekne Usta",
   "meta_desc": "Teak güverte döşeme fiyatını belirleyen faktörler: güverte alanı, doğal veya sentetik teak, derz durumu ve işçilik. Şeffaf fiyatlandırma nasıl olmalı?",
   "body": """
<p>Teak güverte, teknenin en göz alıcı ama en emek isteyen yüzeyi olduğu için maliyeti de birçok faktöre bağlıdır. İşte fiyatı belirleyen ana kalemler.</p>
<h2>Maliyeti belirleyen faktörler</h2>
<ul>
<li><strong>Güverte alanı:</strong> İş doğrudan metrekareyle ölçeklenir.</li>
<li><strong>Malzeme:</strong> <a href="/blog/teak-vs-sentetik-teak/">Doğal teak</a> ile sentetik teak farklı fiyat aralıklarındadır.</li>
<li><strong>Mevcut durum:</strong> Yeni döşeme mi, eski teakı söküp yenileme mi? Söküm ek işçilik demektir.</li>
<li><strong>Derz ve detaylar:</strong> Köşe geçişleri, kavisler ve derz işçiliği fiyatı etkiler.</li>
</ul>
<h2>Sadece derz mi, komple mi?</h2>
<p>Teak hâlâ kalınsa <a href="/blog/teak-derz-yenileme/">derz yenileme</a> çok daha ekonomiktir. Teak inceldiyse komple döşeme gerekir; keşifte teak kalınlığını ölçüp doğru yönlendirme yaparız.</p>
<h2>Şeffaf fiyat</h2>
<p>İyi bir teklif kalem kalemdir: malzeme, söküm, döşeme, derz ve işçilik ayrı görünür. Keşif sonrası bu formatta yazılı teklif veririz.</p>
<p>Teknenize özel fiyat için <a href="/hizmetler/teak-guverte-doseme/">teak güverte döşeme</a> hizmetimiz kapsamında ücretsiz keşif yapıyoruz.</p>
""",
 },
 "en": {
   "category": "Teak",
   "title": "What Determines Teak Deck Cost?",
   "excerpt": "What makes teak deck cost vary? How area, material (natural/synthetic), seams and labour affect the price.",
   "meta_title": "What Determines Teak Deck Cost? | Tekne Usta",
   "meta_desc": "Factors that determine teak deck cost: deck area, natural or synthetic teak, seam condition and labour. What transparent pricing should look like.",
   "body": """
<p>Because a teak deck is a boat's most striking but most labour-intensive surface, its cost depends on many factors. Here are the main items that set the price.</p>
<h2>Factors that set the cost</h2>
<ul>
<li><strong>Deck area:</strong> the job scales directly with square metres.</li>
<li><strong>Material:</strong> <a href="/en/blog/teak-vs-synthetic-teak/">natural teak</a> and synthetic teak are in different price ranges.</li>
<li><strong>Current condition:</strong> a new deck, or removing and renewing old teak? Removal means extra labour.</li>
<li><strong>Seams and details:</strong> corner transitions, curves and seam work affect the price.</li>
</ul>
<h2>Seams only, or full?</h2>
<p>If the teak is still thick, <a href="/en/blog/teak-seam-renewal/">seam renewal</a> is far more economical. If thinned, a full deck is needed; we measure teak thickness at the survey and advise correctly.</p>
<h2>Transparent pricing</h2>
<p>A good quote is itemised: material, removal, laying, seams and labour shown separately. We give a written quote in this format after the survey.</p>
<p>For a price tailored to your boat, we do a free survey under our <a href="/en/services/teak-deck/">teak decking</a> service.</p>
""",
 },
},
{
 "slug": "sentetik-teak-markalari", "slug_en": "synthetic-teak-brands",
 "image": "/assets/images/services/ic-mekan.jpg", "date": "2027-07-07",
 "tr": {
   "category": "Teak",
   "title": "Sentetik Teak Seçerken Nelere Bakmalı?",
   "excerpt": "Sentetik teak markaları arasında fark nedir? Kalite, ısı, kaymazlık ve garanti açısından doğru seçim kriterleri.",
   "meta_title": "Sentetik Teak Seçim Kriterleri | Tekne Usta",
   "meta_desc": "Sentetik teak seçerken dikkat edilecekler: malzeme kalitesi, ısı yönetimi, kaymazlık, renk seçenekleri, UV direnci ve garanti. Doğru sentetik teak seçimi.",
   "body": """
<p>Sentetik teak, doğal teakın bakım yükü olmadan benzer bir görünüm sunar — ama tüm ürünler aynı kalitede değildir. Doğru seçim, sonucun görünümünü ve ömrünü belirler.</p>
<h2>Bakılması gereken kriterler</h2>
<ul>
<li><strong>Isı yönetimi:</strong> Kaliteli ürünler güneşte daha az ısınacak şekilde üretilir — özellikle koyu renklerde önemli.</li>
<li><strong>Kaymazlık:</strong> Islakken bile güvenli tutuş; çocuklu ve yoğun teknelerde kritik.</li>
<li><strong>UV ve renk kalıcılığı:</strong> Yıllarca solmadan aynı tonu koruması.</li>
<li><strong>Renk/desen seçeneği:</strong> Klasik teak tonundan modern gri/koyu seçeneklere.</li>
<li><strong>Garanti:</strong> Üreticinin verdiği garanti, kaliteye dair iyi bir göstergedir.</li>
</ul>
<h2>Uygulama da önemli</h2>
<p>En iyi malzeme bile kötü uygulamayla değerini kaybeder. Düz çizgiler, temiz köşe geçişleri ve doğru yapıştırma sistemi; sonucun hem görünümünü hem dayanıklılığını belirler.</p>
<p>Teknenize uygun sentetik teak seçimini ve uygulamasını <a href="/hizmetler/teak-guverte-doseme/">teak güverte döşeme</a> hizmetimiz kapsamında birlikte yapıyoruz. Doğal ile karşılaştırma için <a href="/blog/teak-vs-sentetik-teak/">bu yazıya</a> bakın.</p>
""",
 },
 "en": {
   "category": "Teak",
   "title": "What to Look for When Choosing Synthetic Teak",
   "excerpt": "What's the difference between synthetic teak brands? The right criteria for quality, heat, non-slip and warranty.",
   "meta_title": "Synthetic Teak Selection Criteria | Tekne Usta",
   "meta_desc": "What to consider when choosing synthetic teak: material quality, heat management, non-slip, colour options, UV resistance and warranty.",
   "body": """
<p>Synthetic teak offers a similar look without natural teak's maintenance burden — but not all products are the same quality. The right choice determines the look and life of the result.</p>
<h2>Criteria to check</h2>
<ul>
<li><strong>Heat management:</strong> quality products are made to heat up less in the sun — important especially in dark colours.</li>
<li><strong>Non-slip:</strong> safe grip even when wet; critical on boats with children and heavy use.</li>
<li><strong>UV and colour retention:</strong> holding the same tone for years without fading.</li>
<li><strong>Colour/pattern options:</strong> from classic teak tones to modern grey/dark.</li>
<li><strong>Warranty:</strong> the maker's warranty is a good indicator of quality.</li>
</ul>
<h2>Application matters too</h2>
<p>Even the best material loses its value with poor application. Straight lines, clean corner transitions and the right bonding system determine both the look and the durability.</p>
<p>We choose and lay the right synthetic teak for your boat under our <a href="/en/services/teak-deck/">teak decking</a> service. For a comparison with natural, see <a href="/en/blog/teak-vs-synthetic-teak/">this article</a>.</p>
""",
 },
},
{
 "slug": "ic-mekan-yenileme-fikirleri", "slug_en": "interior-refit-ideas",
 "image": "/assets/images/services/bakim.jpg", "date": "2027-07-21",
 "tr": {
   "category": "İç Mekan",
   "title": "Tekne İç Mekan Yenileme Fikirleri: Küçük Alanı Büyütmek",
   "excerpt": "Kabini daha ferah, aydınlık ve konforlu göstermenin pratik yolları. Küçük dokunuşlardan komple yenilemeye fikirler.",
   "meta_title": "Tekne İç Mekan Yenileme Fikirleri | Tekne Usta",
   "meta_desc": "Tekne iç mekan yenileme fikirleri: renk, aydınlatma, depolama ve döşeme ile kabini ferah ve konforlu gösterme. Küçük dokunuşlardan komple yenilemeye.",
   "body": """
<p>Teknede alan sınırlıdır; ama doğru dokunuşlarla kabin çok daha ferah, aydınlık ve keyifli hâle gelir. İşte bütçenize göre uygulanabilir yenileme fikirleri.</p>
<h2>Işık ve renk</h2>
<p>Açık renk döşeme ve yüzeyler alanı büyütür. <a href="/blog/kabin-led-aydinlatma/">LED aydınlatma</a> hem enerji tasarrufu sağlar hem kabini modern gösterir. Doğru yerlere yerleştirilen aydınlatma, küçük mekânı derinleştirir.</p>
<h2>Depolama zekâsı</h2>
<p>Teknede her santimetre değerlidir. Yatak altı çekmeceler, akıllı dolap düzeni ve çok amaçlı mobilyalar dağınıklığı azaltır, alanı büyütür.</p>
<h2>Döşeme ve doku</h2>
<p>Yıpranmış minderler ve perdeler kabini eskitir. <a href="/blog/tekne-doseme-kumas-secimi/">Deniz sınıfı kumaşlarla</a> yapılan yenileme hem estetik hem dayanıklıdır.</p>
<h2>Nereden başlamalı?</h2>
<p>Küçük bütçeyle döşeme + aydınlatma büyük fark yaratır; kapsamlı yenilemede mutfak ve dolaplar da elden geçer. İhtiyacınıza göre planı <a href="/hizmetler/ic-mekan-yenileme/">iç mekan yenileme</a> hizmetimiz kapsamında birlikte çıkarıyoruz.</p>
""",
 },
 "en": {
   "category": "Interior",
   "title": "Boat Interior Refit Ideas: Making a Small Space Feel Bigger",
   "excerpt": "Practical ways to make a cabin feel more spacious, bright and comfortable. Ideas from small touches to a full refit.",
   "meta_title": "Boat Interior Refit Ideas | Tekne Usta",
   "meta_desc": "Boat interior refit ideas: making the cabin feel spacious and comfortable with colour, lighting, storage and upholstery. From small touches to a full refit.",
   "body": """
<p>Space aboard is limited; but with the right touches a cabin becomes far more spacious, bright and enjoyable. Here are refit ideas to suit your budget.</p>
<h2>Light and colour</h2>
<p>Light-coloured upholstery and surfaces enlarge the space. <a href="/en/blog/cabin-led-lighting/">LED lighting</a> saves energy and modernises the cabin. Lighting placed in the right spots deepens a small space.</p>
<h2>Smart storage</h2>
<p>Every centimetre counts aboard. Under-berth drawers, clever locker layout and multi-purpose furniture reduce clutter and enlarge the space.</p>
<h2>Upholstery and texture</h2>
<p>Worn cushions and curtains age a cabin. A refit in <a href="/en/blog/marine-upholstery-fabric/">marine-grade fabrics</a> is both attractive and durable.</p>
<h2>Where to start?</h2>
<p>On a small budget, upholstery + lighting make a big difference; a full refit also renews the galley and lockers. We plan to your needs under our <a href="/en/services/interior-refit/">interior refit</a> service.</p>
""",
 },
},
{
 "slug": "teknede-kuf-nem-onleme", "slug_en": "preventing-mould-damp",
 "image": "/assets/images/services/bakim.jpg", "date": "2027-08-04",
 "tr": {
   "category": "İç Mekan",
   "title": "Teknede Küf ve Nem Önleme: Sağlıklı Bir İç Mekan",
   "excerpt": "Teknede nem neden birikir, küf nasıl önlenir? Havalandırma, nem tutucu ve malzeme seçimiyle pratik çözümler.",
   "meta_title": "Teknede Küf ve Nem Önleme Rehberi | Tekne Usta",
   "meta_desc": "Teknede küf ve nem önleme: havalandırma, nem tutucu, hızlı kuruyan sünger ve deniz sınıfı malzemeler. Sağlıklı ve kokusuz bir iç mekan için pratik çözümler.",
   "body": """
<p>Nem ve küf, teknede en sık şikâyet edilen konulardan biridir. Kötü koku, lekeli minderler ve sağlıksız bir kabin… İyi haber: doğru önlemlerle büyük ölçüde önlenebilir.</p>
<h2>Nem neden birikir?</h2>
<p>Kapalı kabin + sıcaklık farkı + kısıtlı hava akışı = yoğuşma. Özellikle kışın kapalı bekleyen teknelerde nem yüzeylerde toplanır ve küf başlar.</p>
<h2>Önleme yolları</h2>
<ul>
<li><strong>Havalandırma:</strong> hava akışı en etkili çözümdür; havalandırma ızgaraları ve güneşli günlerde kabini havalandırmak.</li>
<li><strong>Nem tutucu:</strong> nem çekiciler ve iyi bir <a href="/blog/tekne-kislatma-kontrol-listesi/">kışlatma</a> nemi kontrol altında tutar.</li>
<li><strong>Malzeme:</strong> <a href="/blog/tekne-doseme-kumas-secimi/">hızlı kuruyan sünger</a> ve küfe dayanıklı deniz sınıfı kumaşlar sorunu baştan azaltır.</li>
</ul>
<h2>Küf başladıysa</h2>
<p>Yüzeysel küf temizlenebilir; ama minder ve döşemeye işlemişse yenileme gerekebilir. Kaynak (nem) çözülmeden küf geri gelir.</p>
<p>Küf ve nem sorununu kalıcı çözmek için döşeme ve havalandırmayı <a href="/hizmetler/ic-mekan-yenileme/">iç mekan yenileme</a> hizmetimiz kapsamında birlikte ele alıyoruz.</p>
""",
 },
 "en": {
   "category": "Interior",
   "title": "Preventing Mould and Damp Aboard: A Healthy Interior",
   "excerpt": "Why does damp build up aboard and how is mould prevented? Practical solutions with ventilation, desiccant and material choice.",
   "meta_title": "Preventing Mould and Damp Aboard Guide | Tekne Usta",
   "meta_desc": "Preventing mould and damp aboard: ventilation, desiccant, quick-dry foam and marine-grade materials. Practical solutions for a healthy, odour-free interior.",
   "body": """
<p>Damp and mould are among the most common complaints aboard. Bad smell, stained cushions and an unhealthy cabin… The good news: with the right measures it's largely preventable.</p>
<h2>Why does damp build up?</h2>
<p>Closed cabin + temperature difference + limited airflow = condensation. Especially on boats closed up over winter, moisture collects on surfaces and mould starts.</p>
<h2>Ways to prevent it</h2>
<ul>
<li><strong>Ventilation:</strong> airflow is the most effective solution; vents and airing the cabin on sunny days.</li>
<li><strong>Desiccant:</strong> moisture absorbers and good <a href="/en/blog/boat-winterising-checklist/">winterising</a> keep damp under control.</li>
<li><strong>Materials:</strong> <a href="/en/blog/marine-upholstery-fabric/">quick-dry foam</a> and mould-resistant marine fabrics reduce the problem from the start.</li>
</ul>
<h2>If mould has started</h2>
<p>Surface mould can be cleaned; but if it's soaked into cushions and upholstery, renewal may be needed. Without solving the source (damp), mould returns.</p>
<p>To solve mould and damp for good, we address upholstery and ventilation together under our <a href="/en/services/interior-refit/">interior refit</a> service.</p>
""",
 },
},
{
 "slug": "kabin-led-aydinlatma", "slug_en": "cabin-led-lighting",
 "image": "/assets/images/services/bakim.jpg", "date": "2027-08-18",
 "tr": {
   "category": "İç Mekan",
   "title": "Tekne Kabin LED Aydınlatma: Verimli ve Şık",
   "excerpt": "Neden LED? Teknede aydınlatma yenilerken enerji, sıcaklık, renk tonu ve katman kurgusu üzerine pratik bilgiler.",
   "meta_title": "Tekne Kabin LED Aydınlatma Rehberi | Tekne Usta",
   "meta_desc": "Tekne kabin LED aydınlatma: enerji verimliliği, düşük ısı, renk tonu seçimi ve katmanlı aydınlatma. Kabini modern ve konforlu gösteren aydınlatma çözümleri.",
   "body": """
<p>Aydınlatma, bir kabinin atmosferini en hızlı değiştiren unsurdur. Eski halojen ve akkor ampullerin yerini alan LED, teknede hem verimlilik hem estetik açısından büyük avantaj sunar.</p>
<h2>Neden LED?</h2>
<p>LED, çok daha az enerji tüketir (akü ömrünüzü uzatır), az ısınır (yangın ve konfor açısından güvenli) ve uzun ömürlüdür. Teknede sınırlı enerjiyi düşününce bu avantajlar kritiktir.</p>
<h2>Renk tonu seçimi</h2>
<p>Sıcak beyaz (2700–3000K) kabini samimi ve rahat gösterir; nötr beyaz mutfak ve çalışma alanlarında işlevseldir. Doğru ton, mekânın hissini belirler.</p>
<h2>Katmanlı aydınlatma</h2>
<p>Tek bir tavan lambası yerine; genel, görev (okuma, mutfak) ve atmosfer aydınlatmasını katmanlamak kabini hem işlevsel hem ferah gösterir. Dokunmatik/dim kontroller konforu artırır.</p>
<p>Kabin aydınlatma yenilemesini <a href="/hizmetler/ic-mekan-yenileme/">iç mekan yenileme</a> hizmetimiz kapsamında, döşeme yenileme ile birlikte planlayabiliyoruz.</p>
""",
 },
 "en": {
   "category": "Interior",
   "title": "Boat Cabin LED Lighting: Efficient and Elegant",
   "excerpt": "Why LED? Practical notes on energy, heat, colour temperature and layering when renewing cabin lighting.",
   "meta_title": "Boat Cabin LED Lighting Guide | Tekne Usta",
   "meta_desc": "Boat cabin LED lighting: energy efficiency, low heat, colour temperature choice and layered lighting. Lighting solutions that make the cabin modern and comfortable.",
   "body": """
<p>Lighting is the fastest way to change a cabin's atmosphere. Replacing old halogen and incandescent bulbs, LED offers a big advantage aboard in both efficiency and style.</p>
<h2>Why LED?</h2>
<p>LED uses far less energy (extending battery life), runs cool (safer for fire and comfort) and lasts long. Given limited power aboard, these advantages are critical.</p>
<h2>Choosing colour temperature</h2>
<p>Warm white (2700–3000K) makes the cabin cosy; neutral white is functional in the galley and work areas. The right tone sets the feel of the space.</p>
<h2>Layered lighting</h2>
<p>Instead of a single ceiling light, layering general, task (reading, galley) and ambient lighting makes the cabin both functional and spacious. Touch/dim controls add comfort.</p>
<p>We plan cabin lighting renewal under our <a href="/en/services/interior-refit/">interior refit</a> service, alongside upholstery renewal.</p>
""",
 },
},
{
 "slug": "tekne-mutfagi-yenileme", "slug_en": "galley-refit",
 "image": "/assets/images/services/bakim.jpg", "date": "2027-09-01",
 "tr": {
   "category": "İç Mekan",
   "title": "Tekne Mutfağı (Galley) Yenileme: Küçük Alanda Konfor",
   "excerpt": "Teknede mutfak yenilerken depolama, tezgah, malzeme ve güvenlik açısından nelere dikkat edilmeli?",
   "meta_title": "Tekne Mutfağı (Galley) Yenileme Rehberi | Tekne Usta",
   "meta_desc": "Tekne mutfağı yenileme: depolama, tezgah malzemesi, dayanıklı yüzeyler ve güvenlik. Küçük galley alanını konforlu ve işlevsel hale getirmenin yolları.",
   "body": """
<p>Galley (tekne mutfağı), küçük olmasına rağmen seyir konforunun kalbidir. İyi tasarlanmış bir mutfak, sınırlı alanda bile keyifli bir kullanım sunar.</p>
<h2>Depolama ve düzen</h2>
<p>Teknede her göz değerlidir. Derin çekmeceler, kayma önleyici bölmeler ve dikey depolama; hem düzeni hem güvenliği artırır. Seyir sırasında eşyaların sabit kalması önemlidir.</p>
<h2>Dayanıklı yüzeyler</h2>
<p>Tezgah ve dolap yüzeyleri neme, ısıya ve tuza dayanıklı olmalı. Deniz koşullarına uygun malzeme seçimi, uzun ömrün anahtarıdır.</p>
<h2>Güvenlik</h2>
<p>Ocak sabitleme, kaymaz zemin ve iyi havalandırma; galley'de güvenliğin temelidir. Yenileme sırasında bunlar göz ardı edilmemeli.</p>
<p>Mutfak dolapları, tezgah ve depolama yenilemesini <a href="/hizmetler/ic-mekan-yenileme/">iç mekan yenileme</a> hizmetimiz kapsamında, teknenize özel ölçüyle yapıyoruz.</p>
""",
 },
 "en": {
   "category": "Interior",
   "title": "Boat Galley Refit: Comfort in a Small Space",
   "excerpt": "When refitting a galley, what to watch for in storage, worktop, materials and safety?",
   "meta_title": "Boat Galley Refit Guide | Tekne Usta",
   "meta_desc": "Boat galley refit: storage, worktop material, durable surfaces and safety. How to make a small galley comfortable and functional.",
   "body": """
<p>The galley, though small, is the heart of cruising comfort. A well-designed galley offers enjoyable use even in a limited space.</p>
<h2>Storage and layout</h2>
<p>Every locker counts aboard. Deep drawers, anti-slide compartments and vertical storage improve both order and safety. Keeping items secure under way matters.</p>
<h2>Durable surfaces</h2>
<p>Worktop and cabinet surfaces must resist damp, heat and salt. Choosing materials suited to marine conditions is the key to a long life.</p>
<h2>Safety</h2>
<p>Stove restraint, non-slip flooring and good ventilation are the basis of galley safety. These shouldn't be overlooked in a refit.</p>
<p>We do galley cabinets, worktop and storage renewal under our <a href="/en/services/interior-refit/">interior refit</a> service, made to measure for your boat.</p>
""",
 },
},
{
 "slug": "tekne-ortusu-secimi", "slug_en": "boat-cover-selection",
 "image": "/assets/images/services/bakim.jpg", "date": "2027-09-15",
 "tr": {
   "category": "Bakım",
   "title": "Tekne Örtüsü Seçimi: Kışlatmada Doğru Koruma",
   "excerpt": "Sıkı naylon mu, havalandırmalı örtü mü? Tekneyi kışın küf ve nemden koruyan doğru örtü nasıl seçilir?",
   "meta_title": "Tekne Örtüsü Seçimi Rehberi | Tekne Usta",
   "meta_desc": "Tekne örtüsü seçimi: havalandırmalı kış muhafaza örtüsü, malzeme, doğru gerginlik ve kar/su birikmesini önleme. Kışlatmada küf ve nemden korunma.",
   "body": """
<p>Kışlatmada teknenin başına gelen sorunların çoğu, yanlış örtüden kaynaklanır. İyi bir örtü tekneyi korur; kötüsü ise nemi hapsedip küf ürettir.</p>
<h2>Sıkı naylon tuzağı</h2>
<p>Ucuz ve sıkı plastik örtüler nefes almaz; içeride yoğuşan nem küfe ve kötü kokuya yol açar. "Su geçirmez" her zaman "doğru" demek değildir.</p>
<h2>Doğru örtü: havalandırmalı</h2>
<p>İdeal örtü, yağmur ve UV'yi keserken hava akışına izin verir. Nefes alabilen kumaşlar veya doğru havalandırma boşlukları bırakılmış sistemler tercih edilir.</p>
<h2>Gerginlik ve eğim</h2>
<p>Örtü, üzerinde su ve kar birikmeyecek şekilde eğimli ve gergin kurulmalı. Biriken su ağırlığı hem örtüyü hem tekneyi zorlar. İyi bir iskelet/destek sistemi bunu önler.</p>
<p>Kışlatma paketimizde doğru havalandırmalı örtü ve kurulumu <a href="/hizmetler/tekne-kislatma/">kışlatma</a> hizmetimiz kapsamında sağlıyoruz. Süreç için <a href="/blog/tekne-kislatma-kontrol-listesi/">kontrol listemize</a> bakın.</p>
""",
 },
 "en": {
   "category": "Maintenance",
   "title": "Choosing a Boat Cover: The Right Protection in Winter",
   "excerpt": "Tight plastic or a ventilated cover? How to choose the right cover that protects the boat from mould and damp in winter.",
   "meta_title": "Choosing a Boat Cover Guide | Tekne Usta",
   "meta_desc": "Choosing a boat cover: ventilated winter cover, material, correct tension and preventing snow/water pooling. Protection from mould and damp in winter.",
   "body": """
<p>Most of the problems a boat suffers over winter come from the wrong cover. A good cover protects the boat; a bad one traps damp and breeds mould.</p>
<h2>The tight-plastic trap</h2>
<p>Cheap, tight plastic covers don't breathe; condensing moisture inside causes mould and bad smell. "Waterproof" doesn't always mean "right".</p>
<h2>The right cover: ventilated</h2>
<p>The ideal cover blocks rain and UV while allowing airflow. Breathable fabrics or systems with proper ventilation gaps are preferred.</p>
<h2>Tension and slope</h2>
<p>The cover should be sloped and taut so water and snow don't pool on it. Pooled water's weight strains both cover and boat. A good frame/support system prevents this.</p>
<p>Our winterising package provides the right ventilated cover and its fitting under our <a href="/en/services/winterising-storage/">winterising</a> service. See our <a href="/en/blog/boat-winterising-checklist/">checklist</a> for the process.</p>
""",
 },
},
{
 "slug": "anot-zinc-bakimi", "slug_en": "anode-zinc-care",
 "image": "/assets/images/services/bakim.jpg", "date": "2027-09-29",
 "tr": {
   "category": "Bakım",
   "title": "Anot (Zinc) Bakımı: Galvanik Korozyondan Korunma",
   "excerpt": "Anotlar ne işe yarar, ne zaman değişir ve neden ihmal edilmemeli? Teknenin metal parçalarını koruyan sessiz kahraman.",
   "meta_title": "Tekne Anot (Zinc) Bakımı Rehberi | Tekne Usta",
   "meta_desc": "Tekne anot (zinc) bakımı: galvanik korozyon, anotların görevi, ne zaman değiştirilmeli ve doğru anot seçimi. Şaft, pervane ve metal parçaların korunması.",
   "body": """
<p>Anotlar (halk arasında "zinc"), teknenin su altındaki metal parçalarını korozyondan koruyan küçük ama kritik parçalardır. İhmal edildiğinde şaft, pervane ve diğer metaller zarar görür.</p>
<h2>Anot ne işe yarar?</h2>
<p>Su altında farklı metaller ve deniz suyu bir pil gibi davranır; bu galvanik korozyona yol açar. Anot, kendini "feda ederek" (bu yüzden 'kurban anot' denir) diğer değerli metaller yerine aşınır ve onları korur.</p>
<h2>Ne zaman değişir?</h2>
<p>Genel kural: anot yaklaşık <strong>yarısına kadar eridiyse</strong> değiştirin. Çoğu tekede sezon başında kontrol ve gerekiyorsa değişim yapılır. Tamamen erimiş anot artık koruma sağlamaz.</p>
<h2>Doğru anot</h2>
<p>Suyun tipi önemlidir: tuzlu su için çinko, acı/karışık su için alüminyum, tatlı su için magnezyum anot kullanılır. Yanlış anot koruma sağlamaz.</p>
<p>Anot kontrolü karina bakımının bir parçasıdır; <a href="/hizmetler/tekne-kislatma/">kışlatma ve bakım</a> hizmetimizde karaya çekmeyle birlikte kontrol ediyoruz. <a href="/blog/bahar-tekne-bakimi/">Bahar bakımında</a> da mutlaka bakılmalı.</p>
""",
 },
 "en": {
   "category": "Maintenance",
   "title": "Anode (Zinc) Care: Protection from Galvanic Corrosion",
   "excerpt": "What do anodes do, when are they replaced and why shouldn't they be neglected? The silent hero protecting the boat's metal parts.",
   "meta_title": "Boat Anode (Zinc) Care Guide | Tekne Usta",
   "meta_desc": "Boat anode (zinc) care: galvanic corrosion, the role of anodes, when to replace them and choosing the right anode. Protecting shaft, propeller and metal parts.",
   "body": """
<p>Anodes (commonly "zincs") are small but critical parts that protect a boat's underwater metals from corrosion. Neglected, the shaft, propeller and other metals suffer.</p>
<h2>What does an anode do?</h2>
<p>Underwater, different metals and seawater act like a battery; this causes galvanic corrosion. The anode "sacrifices itself" (hence 'sacrificial anode'), wearing away instead of the valuable metals and protecting them.</p>
<h2>When to replace?</h2>
<p>General rule: replace an anode when it has eroded to about <strong>half</strong>. On most boats, check at season start and replace if needed. A fully eroded anode no longer protects.</p>
<h2>The right anode</h2>
<p>Water type matters: zinc for salt water, aluminium for brackish/mixed water, magnesium for fresh water. The wrong anode doesn't protect.</p>
<p>Anode checking is part of hull maintenance; we check it with haul-out in our <a href="/en/services/winterising-storage/">winterising and maintenance</a> service. It should also be checked in <a href="/en/blog/spring-boat-maintenance/">spring maintenance</a>.</p>
""",
 },
},
{
 "slug": "marina-vs-cekek", "slug_en": "marina-vs-hardstand",
 "image": "/assets/images/services/bakim.jpg", "date": "2027-10-13",
 "tr": {
   "category": "Bakım",
   "title": "Marina mı Çekek mi? Bakım İçin Doğru Yer",
   "excerpt": "Tekne bakımı ve depolama için marina (suda) ile çekek (karada) arasındaki fark, maliyet ve hangisi ne zaman?",
   "meta_title": "Marina mı Çekek mi? Bakım Yeri Rehberi | Tekne Usta",
   "meta_desc": "Marina ve çekek karşılaştırması: suda mı karada mı bakım ve depolama? Maliyet, erişim, karina bakımı ve hangi iş için hangisinin uygun olduğu.",
   "body": """
<p>Tekne sahiplerinin sık karşılaştığı karar: bakım ve depolama için marinada (suda) mı kalmalı, yoksa çekeğe (karaya) mı çekilmeli? İkisinin de yeri var.</p>
<h2>Marina (suda)</h2>
<p><strong>Artıları:</strong> hızlı erişim, kolay giriş-çıkış, günlük kullanım. <strong>Sınırı:</strong> karina sürekli suda olduğu için kirlenme ve <a href="/blog/osmoz-belirtileri/">osmoz</a> riski; su altı işleri yapılamaz.</p>
<h2>Çekek (karada)</h2>
<p><strong>Artıları:</strong> karina kurur, antifouling, boya ve <a href="/blog/su-alti-yapisal-onarim/">su altı onarım</a> mümkün, osmoz riski azalır. <strong>Sınırı:</strong> çekme/indirme maliyeti ve daha az erişim.</p>
<h2>Hangi iş için hangisi?</h2>
<p>Günlük kullanım ve kısa süreli park için marina; kapsamlı bakım, boya, karina ve kışlatma için çekek doğru tercihtir. Su altını ilgilendiren her iş çekek gerektirir.</p>
<p>Karaya çekme gerektiren bakımları <a href="/hizmetler/tekne-kislatma/">kışlatma ve bakım</a> hizmetimiz kapsamında planlıyoruz. Detaylar için <a href="/blog/tekne-cekek-karaya-cekme/">çekek rehberimize</a> bakın.</p>
""",
 },
 "en": {
   "category": "Maintenance",
   "title": "Marina or Hardstand? The Right Place for Maintenance",
   "excerpt": "For maintenance and storage, the difference between a marina (afloat) and hardstand (ashore), cost and which when?",
   "meta_title": "Marina or Hardstand? A Maintenance Guide | Tekne Usta",
   "meta_desc": "Marina vs hardstand comparison: maintenance and storage afloat or ashore? Cost, access, hull maintenance and which suits which job.",
   "body": """
<p>A decision boat owners often face: for maintenance and storage, stay in the marina (afloat) or haul out to the hardstand (ashore)? Both have their place.</p>
<h2>Marina (afloat)</h2>
<p><strong>Pros:</strong> quick access, easy in-out, daily use. <strong>Limit:</strong> the hull is constantly in water, raising growth and <a href="/en/blog/osmosis-symptoms/">osmosis</a> risk; underwater work isn't possible.</p>
<h2>Hardstand (ashore)</h2>
<p><strong>Pros:</strong> the hull dries, antifouling, paint and <a href="/en/blog/underwater-structural-repair/">underwater repair</a> are possible, osmosis risk drops. <strong>Limit:</strong> haul/launch cost and less access.</p>
<h2>Which for which job?</h2>
<p>For daily use and short-term berthing, the marina; for extensive maintenance, paint, hull and winterising, the hardstand is the right choice. Any job involving the underwater section needs the hardstand.</p>
<p>We plan maintenance that needs hauling out under our <a href="/en/services/winterising-storage/">winterising and maintenance</a> service. For detail, see our <a href="/en/blog/boat-haul-out-guide/">haul-out guide</a>.</p>
""",
 },
},
{
 "slug": "tekne-sahipligi-maliyeti", "slug_en": "cost-of-boat-ownership",
 "image": "/assets/images/hakkimizda.jpg", "date": "2027-10-27",
 "tr": {
   "category": "Rehber",
   "title": "Tekne Sahibi Olmanın Yıllık Maliyeti: Gerçekçi Bir Bakış",
   "excerpt": "Teknenin fiyatı buzdağının görünen kısmı. Bağlama, bakım, kışlatma, sigorta ve onarım — yıllık gerçek maliyet.",
   "meta_title": "Tekne Sahibi Olmanın Yıllık Maliyeti | Tekne Usta",
   "meta_desc": "Tekne sahibi olmanın yıllık maliyeti: bağlama, bakım, kışlatma, sigorta, yakıt ve onarım kalemleri. Tekne almadan önce gerçekçi bütçe planlaması.",
   "body": """
<p>Tekne almadan önce en çok göz ardı edilen konu, teknenin fiyatının işin sadece başlangıcı olduğudur. Gerçek maliyet, yıllık işletme giderlerinde saklıdır. İşte gerçekçi bir tablo.</p>
<h2>Ana maliyet kalemleri</h2>
<ul>
<li><strong>Bağlama:</strong> Marina veya çekek ücreti; bölgeye ve tekne boyuna göre büyük fark eder.</li>
<li><strong>Kışlatma ve çekek:</strong> Sezon sonu <a href="/blog/tekne-kislatma-kontrol-listesi/">kışlatma</a>, karaya çekme ve depolama.</li>
<li><strong>Bakım:</strong> <a href="/blog/yillik-tekne-bakim-takvimi/">Yıllık bakım</a>, antifouling, küçük onarımlar.</li>
<li><strong>Sigorta:</strong> Tekne değeri ve kullanıma göre.</li>
<li><strong>Yakıt ve sarf:</strong> Kullanım yoğunluğuna bağlı.</li>
</ul>
<h2>Beklenmedik onarımlar</h2>
<p>Özellikle ikinci el teknelerde, ilk yıl beklenmedik onarımlar çıkabilir. Bu yüzden bütçeye bir <strong>tampon pay</strong> eklemek akıllıcadır. <a href="/blog/satin-alma-oncesi-tekne-ekspertizi/">Satın alma öncesi kontrol</a> bu sürprizleri azaltır.</p>
<h2>Maliyeti düşürmenin yolu</h2>
<p>Düzenli, önleyici bakım; büyük ve pahalı onarımların önündeki en iyi settir. İhmal, uzun vadede en pahalı seçenektir.</p>
<p>Teknenizin bakım maliyetini öngörülebilir kılmak için <a href="/hizmetler/tekne-kislatma/">bakım</a> hizmetimiz kapsamında planlı bir yaklaşım sunuyoruz.</p>
""",
 },
 "en": {
   "category": "Guide",
   "title": "The Annual Cost of Boat Ownership: A Realistic Look",
   "excerpt": "The purchase price is the tip of the iceberg. Berthing, maintenance, winterising, insurance and repairs — the real annual cost.",
   "meta_title": "The Annual Cost of Boat Ownership | Tekne Usta",
   "meta_desc": "The annual cost of boat ownership: berthing, maintenance, winterising, insurance, fuel and repair items. Realistic budgeting before buying a boat.",
   "body": """
<p>The most overlooked thing before buying a boat is that the purchase price is only the start. The real cost hides in annual running expenses. Here's a realistic picture.</p>
<h2>Main cost items</h2>
<ul>
<li><strong>Berthing:</strong> marina or hardstand fees; varies greatly by region and boat length.</li>
<li><strong>Winterising and haul-out:</strong> end-of-season <a href="/en/blog/boat-winterising-checklist/">winterising</a>, hauling out and storage.</li>
<li><strong>Maintenance:</strong> <a href="/en/blog/annual-boat-maintenance-calendar/">annual maintenance</a>, antifouling, small repairs.</li>
<li><strong>Insurance:</strong> by boat value and use.</li>
<li><strong>Fuel and consumables:</strong> depending on usage.</li>
</ul>
<h2>Unexpected repairs</h2>
<p>Especially on used boats, the first year can bring unexpected repairs. So it's wise to add a <strong>buffer</strong> to the budget. A <a href="/en/blog/pre-purchase-boat-survey/">pre-purchase check</a> reduces these surprises.</p>
<h2>How to lower the cost</h2>
<p>Regular, preventive maintenance is the best defence against big, expensive repairs. Neglect is the most expensive option long term.</p>
<p>To make your boat's maintenance cost predictable, we offer a planned approach under our <a href="/en/services/winterising-storage/">maintenance</a> service.</p>
""",
 },
},
{
 "slug": "tekne-tipleri-rehberi", "slug_en": "boat-types-guide",
 "image": "/assets/images/parallax-2.jpg", "date": "2027-11-10",
 "tr": {
   "category": "Rehber",
   "title": "Tekne Tipleri Rehberi: Motoryat, Yelkenli, RIB ve Klasik",
   "excerpt": "Hangi tekne tipi kime uygun? Motor tekne, yelkenli, RIB ve klasik ahşap teknelerin kullanımı, konforu ve bakımı.",
   "meta_title": "Tekne Tipleri Rehberi | Tekne Usta",
   "meta_desc": "Tekne tipleri rehberi: motoryat, yelkenli, RIB/bot ve klasik ahşap tekneler. Her tipin kullanımı, konforu, hızı ve bakım özellikleri karşılaştırması.",
   "body": """
<p>"Hangi tekne bana uygun?" sorusunun cevabı, kullanım amacınıza bağlı. İşte ana tekne tipleri ve karakterleri.</p>
<h2>Motor tekne / Motoryat</h2>
<p>Hız, konfor ve kolay kullanım öne çıkar. Günübirlik gezi ve konaklamalı seyir için geniş bir yelpaze sunar. Bakımda gövde, boya ve iç mekan önceliklidir.</p>
<h2>Yelkenli</h2>
<p>Rüzgârla seyrin keyfi, ekonomik yakıt ve denizle bağ. Öğrenme eğrisi vardır ama tutkulu bir kitlesi. Donanım, karina ve <a href="/blog/osmoz-belirtileri/">osmoz</a> takibi önemlidir.</p>
<h2>RIB / Bot</h2>
<p>Şişme yan tüplü, hızlı ve pratik. Günübirlik eğlence, kısa geziler ve yardımcı tekne olarak popüler. Bakımı görece basittir.</p>
<h2>Klasik ahşap</h2>
<p>Karakter ve estetik önceliğinde. Düzenli <a href="/blog/klasik-tekne-turleri/">bakım ve restorasyon</a> ister ama eşsiz bir sahiplik deneyimi sunar.</p>
<p>Hangi tipte olursa olsun, teknenizin bakım ve onarımında <a href="/hizmetler/fiberglas-onarim/">fiberglas</a> ve <a href="/hizmetler/ahsap-tekne-renovasyonu/">ahşap</a> tarafında yanınızdayız.</p>
""",
 },
 "en": {
   "category": "Guide",
   "title": "Boat Types Guide: Motoryacht, Sailboat, RIB and Classic",
   "excerpt": "Which boat type suits whom? The use, comfort and maintenance of motorboats, sailboats, RIBs and classic wooden boats.",
   "meta_title": "Boat Types Guide | Tekne Usta",
   "meta_desc": "Boat types guide: motoryacht, sailboat, RIB/tender and classic wooden boats. A comparison of each type's use, comfort, speed and maintenance traits.",
   "body": """
<p>The answer to "which boat suits me?" depends on your intended use. Here are the main boat types and their characters.</p>
<h2>Motorboat / Motoryacht</h2>
<p>Speed, comfort and easy handling stand out. Offers a wide range for day trips and overnight cruising. In maintenance, hull, paint and interior are priorities.</p>
<h2>Sailboat</h2>
<p>The joy of sailing with the wind, economical fuel and a bond with the sea. There's a learning curve but a passionate following. Rigging, hull and <a href="/en/blog/osmosis-symptoms/">osmosis</a> monitoring matter.</p>
<h2>RIB / Tender</h2>
<p>Inflatable-tubed, fast and practical. Popular for day fun, short trips and as a tender. Maintenance is relatively simple.</p>
<h2>Classic wooden</h2>
<p>Character and aesthetics first. Needs regular <a href="/en/blog/classic-boat-types/">care and restoration</a> but offers a unique ownership experience.</p>
<p>Whatever the type, we're at your side for maintenance and repair on the <a href="/en/services/fibreglass-repair/">fibreglass</a> and <a href="/en/services/wooden-boat-refit/">wood</a> side.</p>
""",
 },
},
{
 "slug": "blister-vs-osmoz-farki", "slug_en": "blister-vs-osmosis",
 "image": "/assets/images/services/fiberglas.jpg", "date": "2027-11-24",
 "tr": {
   "category": "Fiberglas",
   "title": "Blister mı Osmoz mu? Karina Kabarcıklarını Doğru Okumak",
   "excerpt": "Her kabarcık osmoz değildir. Blister ile osmos (ozmoz) arasındaki fark, nasıl ayırt edilir ve hangisi ne gerektirir?",
   "meta_title": "Blister mı Osmoz mu? Fark ve Ayırt Etme | Tekne Usta",
   "meta_desc": "Blister ile osmoz (osmos, ozmoz) arasındaki fark: karina kabarcıkları nasıl ayırt edilir, hangisi ciddi, hangisi kozmetik? Doğru tanı ve tedavi yaklaşımı.",
   "body": """
<p>Tekne karadayken su altı yüzeyde kabarcık (blister) görmek her zaman panik sebebi değildir. Halk arasında "osmos" ya da "ozmoz" diye de yazılan bu sorun, her kabarcıkla eş anlamlı değildir. Doğru tanı, gereksiz masrafı da yanlış ihmali de önler.</p>
<h2>Blister nedir?</h2>
<p>Blister, jelkotun altında oluşan içi sıvı dolu kabarcığın genel adıdır. Kaynağı her zaman osmoz olmayabilir; boya katları arasındaki tutunma sorunu, nem veya uygulama hatası da blister yapabilir.</p>
<h2>Osmoz (osmos/ozmoz) nedir?</h2>
<p>Osmoz, suyun laminata sızıp reçineyle tepkimeye girmesiyle oluşan <strong>kimyasal</strong> bir süreçtir. Ayırt edici işareti: kabarcık delindiğinde çıkan sıvının <strong>ekşi/sirke kokulu</strong> ve yapışkan olmasıdır. <a href="/blog/osmoz-belirtileri/">Osmoz belirtileri</a> yazımızda detaylandırdık.</p>
<h2>Nasıl ayırt edilir?</h2>
<ul>
<li><strong>Koku:</strong> Ekşi/asidik koku → osmoz. Kokusuz → büyük ihtimalle boya/nem kaynaklı blister.</li>
<li><strong>Katman:</strong> Kabarcık jelkot altında laminatta mı, yoksa sadece boya katlarında mı?</li>
<li><strong>Nem ölçer:</strong> Yüksek laminat nemi osmozu işaret eder.</li>
</ul>
<h2>Hangisi ne gerektirir?</h2>
<p>Boya kaynaklı blister genelde yüzey işlemiyle çözülür; osmoz ise jelkot sıyırma, kurutma ve epoksi bariyer gerektirir (bkz. <a href="/blog/osmoz-nedir-tedavisi/">osmoz tedavisi</a>). Yanlış tanı, ya gereksiz büyük iş ya da geri dönen bir sorun demektir.</p>
<p>Karinanızdaki kabarcığın gerçekten osmoz olup olmadığını <a href="/hizmetler/fiberglas-onarim/">fiberglas onarım</a> hizmetimiz kapsamında nem ölçümüyle net tespit ediyoruz.</p>
""",
 },
 "en": {
   "category": "Fibreglass",
   "title": "Blister or Osmosis? Reading Hull Blisters Correctly",
   "excerpt": "Not every blister is osmosis. The difference between a blister and osmosis, how to tell them apart and what each needs.",
   "meta_title": "Blister or Osmosis? Difference and How to Tell | Tekne Usta",
   "meta_desc": "The difference between a blister and osmosis: how to tell hull blisters apart, which is serious and which is cosmetic. Correct diagnosis and treatment approach.",
   "body": """
<p>Seeing a blister on the underwater surface when the boat is ashore isn't always cause for panic. This problem isn't synonymous with every blister. Correct diagnosis prevents both needless expense and harmful neglect.</p>
<h2>What is a blister?</h2>
<p>A blister is the general term for a fluid-filled bubble forming under the gelcoat. Its source isn't always osmosis; adhesion failure between paint coats, moisture or application error can also blister.</p>
<h2>What is osmosis?</h2>
<p>Osmosis is a <strong>chemical</strong> process where water seeps into the laminate and reacts with the resin. Its telltale sign: the fluid from a pierced blister is <strong>sour/vinegar-smelling</strong> and sticky. We detail this in our <a href="/en/blog/osmosis-symptoms/">osmosis symptoms</a> article.</p>
<h2>How to tell them apart?</h2>
<ul>
<li><strong>Smell:</strong> sour/acidic → osmosis. Odourless → likely a paint/moisture blister.</li>
<li><strong>Layer:</strong> is the blister in the laminate under the gelcoat, or only in the paint coats?</li>
<li><strong>Moisture meter:</strong> high laminate moisture points to osmosis.</li>
</ul>
<h2>What does each need?</h2>
<p>A paint blister is usually solved with surface work; osmosis needs gelcoat peeling, drying and an epoxy barrier (see <a href="/en/blog/what-is-osmosis-treatment/">osmosis treatment</a>). A wrong diagnosis means either needless big work or a returning problem.</p>
<p>We determine whether your hull blister is really osmosis with a moisture reading under our <a href="/en/services/fibreglass-repair/">fibreglass repair</a> service.</p>
""",
 },
},
{
 "slug": "metalik-efekt-boya", "slug_en": "metallic-effect-paint",
 "image": "/assets/images/services/boya.jpg", "date": "2027-12-08",
 "tr": {
   "category": "Boya",
   "title": "Tekne Metalik ve Özel Efekt Boya: Dikkat Çeken Bir Bitiş",
   "excerpt": "Metalik, sedefli ve özel efekt boyalar teknede nasıl uygulanır? Avantajları, zorlukları ve bakım gereksinimleri.",
   "meta_title": "Tekne Metalik ve Efekt Boya Rehberi | Tekne Usta",
   "meta_desc": "Tekne metalik, sedefli ve özel efekt boya: uygulama zorluğu, vernik (clear coat) katı, dayanıklılık ve bakım. Dikkat çeken bir bitiş için bilinmesi gerekenler.",
   "body": """
<p>Metalik ve sedefli efekt boyalar, tekneye limanda öne çıkan, derinlikli bir görünüm kazandırır. Ama bu bitiş, düz renklere göre daha fazla ustalık ve bakım ister.</p>
<h2>Nasıl bir görünüm sunar?</h2>
<p>Metalik pigmentler ışığı farklı açılardan yansıtarak derinlik ve hareket hissi verir. Sedef (pearl) efektler ise renk tonunu bakış açısına göre değiştirir. Özel efektler, tekneyi kalabalıkta ayrıştırır.</p>
<h2>Uygulama neden zor?</h2>
<p>Metalik boyada pigmentin homojen dağılması kritiktir; eşit olmayan uygulama "leke" ve "bulut" yapar. Bu yüzden püskürtme tekniği, kat sayısı ve mutlaka üzerine <strong>koruyucu vernik (clear coat)</strong> uygulanması şarttır. Clear coat hem parlaklığı hem UV korumasını sağlar.</p>
<h2>Bakım</h2>
<p>Efekt boyalar UV'ye ve çiziğe düz renklerden daha hassastır; düzenli koruma ve dikkatli temizlik ömrü uzatır. Onarımı da daha uzmanlık ister — bölgesel rötuş her zaman kolay değildir.</p>
<p>Teknenize metalik/efekt bir bitiş düşünüyorsanız, doğru sistem ve uygulamayı <a href="/hizmetler/tekne-boyama-antifouling/">tekne boyama</a> hizmetimiz kapsamında planlıyoruz. <a href="/blog/2k-poliuretan-boya/">2K poliüretan</a> altyapısıyla en dayanıklı sonucu alırsınız.</p>
""",
 },
 "en": {
   "category": "Painting",
   "title": "Boat Metallic and Special-Effect Paint: A Standout Finish",
   "excerpt": "How are metallic, pearl and special-effect paints applied to a boat? Their advantages, challenges and maintenance needs.",
   "meta_title": "Boat Metallic and Effect Paint Guide | Tekne Usta",
   "meta_desc": "Boat metallic, pearl and special-effect paint: application difficulty, clear coat, durability and maintenance. What to know for a standout finish.",
   "body": """
<p>Metallic and pearl effect paints give a boat a deep, standout look in the harbour. But this finish takes more skill and care than solid colours.</p>
<h2>What look does it give?</h2>
<p>Metallic pigments reflect light from different angles, giving depth and a sense of movement. Pearl effects shift the tone with the viewing angle. Special effects set the boat apart in a crowd.</p>
<h2>Why is it hard to apply?</h2>
<p>Even pigment distribution is critical in metallic paint; uneven application causes "mottling" and "clouding". So spray technique, coat count and a protective <strong>clear coat</strong> on top are essential. The clear coat provides both gloss and UV protection.</p>
<h2>Maintenance</h2>
<p>Effect paints are more sensitive to UV and scratches than solid colours; regular protection and careful cleaning extend their life. Repair also takes more expertise — a spot touch-up isn't always easy.</p>
<p>If you're considering a metallic/effect finish, we plan the right system and application under our <a href="/en/services/boat-painting-antifouling/">boat painting</a> service. With a <a href="/en/blog/2k-polyurethane-paint/">2K polyurethane</a> base you get the most durable result.</p>
""",
 },
},
{
 "slug": "sentetik-teak-alternatifleri", "slug_en": "synthetic-teak-alternatives",
 "image": "/assets/images/services/ic-mekan.jpg", "date": "2027-12-22",
 "tr": {
   "category": "Teak",
   "title": "Sentetik Teak Alternatifleri: Kortek, Flexiteek ve PVC Teak",
   "excerpt": "Doğal tik yerine sentetik teak seçenekleri: kortek, flexiteek ve EVA köpük teak. Farkları, avantajları ve kullanım alanları.",
   "meta_title": "Sentetik Teak Alternatifleri: Kortek, Flexiteek | Tekne Usta",
   "meta_desc": "Sentetik teak alternatifleri: PVC teak (Flexiteek benzeri), kortek ve EVA köpük teak. Doğal tik yerine bakım gerektirmeyen güverte seçeneklerinin karşılaştırması.",
   "body": """
<p>Doğal tik (teak) güzeldir ama pahalı ve bakım isteyen bir malzemedir. Bu yüzden bakım gerektirmeyen sentetik alternatifler giderek yaygınlaşıyor. İşte başlıca seçenekler ve farkları.</p>
<h2>PVC teak (Flexiteek tarzı)</h2>
<p>Esnek PVC bazlı, ısıyla şekil alan ve gerçek teak dokusunu taklit eden sistemler. <strong>Artıları:</strong> su geçirmez, bakımsız, dikişsiz görünüm; teknenin hattına birebir uyar. Güvertede en çok tercih edilen sentetik seçenektir.</p>
<h2>Kortek ve benzerleri</h2>
<p>Farklı markaların kompozit/PVC teak çözümleri; renk ve derz seçenekleriyle klasik teak görünümünü sunar. Kalite ve dayanıklılık markaya göre değişir; <a href="/blog/sentetik-teak-markalari/">seçim kriterlerine</a> bakın.</p>
<h2>EVA köpük teak</h2>
<p>Hafif, yumuşak ve kaymaz EVA köpük paneller; genelde kokpit, iskele ve SUP/tekne tabanlarında kullanılır. <strong>Artıları:</strong> ekonomik, konforlu, kolay uygulanır. Klasik güverte hissi doğal teak kadar değildir ama pratiktir.</p>
<h2>Hangisi size uygun?</h2>
<p>Klasik görünüm + dikişsiz kalıcılık isterseniz PVC teak; konfor + ekonomi isterseniz EVA köpük mantıklı. Doğal ile karşılaştırma için <a href="/blog/teak-vs-sentetik-teak/">bu yazıya</a> bakın.</p>
<p>Teknenize uygun sentetik teak alternatifini <a href="/hizmetler/teak-guverte-doseme/">teak güverte döşeme</a> hizmetimiz kapsamında birlikte seçip uyguluyoruz.</p>
""",
 },
 "en": {
   "category": "Teak",
   "title": "Synthetic Teak Alternatives: PVC Teak, Composite and EVA Foam",
   "excerpt": "Synthetic teak options instead of natural teak: PVC teak, composite teak and EVA foam teak. Their differences, advantages and uses.",
   "meta_title": "Synthetic Teak Alternatives: PVC Teak & EVA Foam | Tekne Usta",
   "meta_desc": "Synthetic teak alternatives: PVC teak (Flexiteek-style), composite teak and EVA foam teak. A comparison of maintenance-free deck options instead of natural teak.",
   "body": """
<p>Natural teak is beautiful but expensive and maintenance-hungry. So maintenance-free synthetic alternatives are increasingly popular. Here are the main options and their differences.</p>
<h2>PVC teak (Flexiteek-style)</h2>
<p>Flexible PVC-based systems that are heat-formed and imitate real teak grain. <strong>Pros:</strong> waterproof, maintenance-free, seamless look; conforms exactly to the boat's lines. The most popular synthetic deck option.</p>
<h2>Composite teak and similar</h2>
<p>Various brands' composite/PVC teak solutions offer the classic teak look with colour and seam options. Quality and durability vary by brand; see our <a href="/en/blog/synthetic-teak-brands/">selection criteria</a>.</p>
<h2>EVA foam teak</h2>
<p>Light, soft, non-slip EVA foam panels; usually used in cockpits, on swim platforms and SUP/boat floors. <strong>Pros:</strong> economical, comfortable, easy to fit. The classic deck feel isn't quite natural teak, but it's practical.</p>
<h2>Which suits you?</h2>
<p>For a classic look with seamless durability, PVC teak; for comfort and economy, EVA foam. For a comparison with natural, see <a href="/en/blog/teak-vs-synthetic-teak/">this article</a>.</p>
<p>We choose and fit the right synthetic teak alternative for your boat under our <a href="/en/services/teak-deck/">teak decking</a> service.</p>
""",
 },
},
{
 "slug": "tekne-perde-stor", "slug_en": "boat-curtains-blinds",
 "image": "/assets/images/services/bakim.jpg", "date": "2028-01-05",
 "tr": {
   "category": "İç Mekan",
   "title": "Tekne Perde ve Stor: Mahremiyet, Güneş ve Konfor",
   "excerpt": "Teknede perde ve stor seçimi: mahremiyet, güneş kontrolü, nem ve doğru malzeme. Kabini hem şık hem işlevsel yapmak.",
   "meta_title": "Tekne Perde ve Stor Seçimi Rehberi | Tekne Usta",
   "meta_desc": "Tekne perde ve stor: mahremiyet, güneş kontrolü, kararma (blackout), nem dayanımı ve doğru malzeme. Kabini şık ve işlevsel yapan perde çözümleri.",
   "body": """
<p>Perde ve storlar, teknenin iç mekânını hem mahremiyet hem güneş kontrolü hem de estetik açısından tamamlar. Doğru seçim, kabinin konforunu ve görünümünü belirgin biçimde artırır.</p>
<h2>Ne işe yarar?</h2>
<p>Limanda mahremiyet, seyirde güneş ve ısı kontrolü, geceleri kararma (blackout) ve genel bir düzen hissi. İyi bir perde/stor sistemi, küçük kabini daha derli toplu ve konforlu gösterir.</p>
<h2>Malzeme ve tip</h2>
<ul>
<li><strong>Deniz sınıfı kumaş:</strong> Neme, küfe ve UV'ye dayanıklı, solmayan kumaşlar; <a href="/blog/tekne-doseme-kumas-secimi/">döşeme kumaşıyla</a> uyumlu.</li>
<li><strong>Stor/plise:</strong> Az yer kaplayan, pratik güneşlik çözümleri.</li>
<li><strong>Blackout:</strong> Konaklamalı seyirde uyku konforu için kararma katmanı.</li>
</ul>
<h2>Detaylar önemli</h2>
<p>Paslanmaz raylar ve fikstürler, doğru ölçü ve nemli ortama uygun dikiş; sistemin hem görünümünü hem ömrünü belirler.</p>
<p>Perde, stor ve <a href="/blog/tekne-doseme-kumas-secimi/">döşeme</a> yenilemesini bir bütün olarak <a href="/hizmetler/ic-mekan-yenileme/">iç mekan yenileme</a> hizmetimiz kapsamında, teknenize özel ölçüyle yapıyoruz.</p>
""",
 },
 "en": {
   "category": "Interior",
   "title": "Boat Curtains and Blinds: Privacy, Sun and Comfort",
   "excerpt": "Choosing boat curtains and blinds: privacy, sun control, damp and the right material. Making the cabin both elegant and functional.",
   "meta_title": "Boat Curtains and Blinds Guide | Tekne Usta",
   "meta_desc": "Boat curtains and blinds: privacy, sun control, blackout, damp resistance and the right material. Window solutions that make the cabin elegant and functional.",
   "body": """
<p>Curtains and blinds complete a boat's interior for privacy, sun control and looks. The right choice noticeably improves the cabin's comfort and appearance.</p>
<h2>What are they for?</h2>
<p>Privacy in harbour, sun and heat control under way, blackout at night and a general sense of order. A good curtain/blind system makes a small cabin feel tidier and more comfortable.</p>
<h2>Material and type</h2>
<ul>
<li><strong>Marine-grade fabric:</strong> damp-, mould- and UV-resistant, non-fading fabrics; matched to your <a href="/en/blog/marine-upholstery-fabric/">upholstery</a>.</li>
<li><strong>Blinds/pleated:</strong> compact, practical shade solutions.</li>
<li><strong>Blackout:</strong> a blackout layer for sleep comfort on overnight cruises.</li>
</ul>
<h2>Details matter</h2>
<p>Stainless tracks and fixtures, correct measurement and stitching suited to a damp environment determine both the look and the life of the system.</p>
<p>We do curtains, blinds and <a href="/en/blog/marine-upholstery-fabric/">upholstery</a> renewal as a whole under our <a href="/en/services/interior-refit/">interior refit</a> service, made to measure for your boat.</p>
""",
 },
},
{
 "slug": "tekne-kiralama-vs-sahiplik", "slug_en": "boat-charter-vs-ownership",
 "image": "/assets/images/hakkimizda.jpg", "date": "2028-01-19",
 "tr": {
   "category": "Rehber",
   "title": "Tekne Kiralama mı Sahiplik mi? Hangisi Size Uygun?",
   "excerpt": "Tekne kiralamak mı, sahip olmak mı daha mantıklı? Maliyet, kullanım sıklığı, bakım sorumluluğu ve özgürlük açısından karşılaştırma.",
   "meta_title": "Tekne Kiralama mı Sahiplik mi? Karşılaştırma | Tekne Usta",
   "meta_desc": "Tekne kiralama ile sahiplik karşılaştırması: maliyet, kullanım sıklığı, bakım sorumluluğu ve esneklik. Hangisinin size uygun olduğuna karar verme rehberi.",
   "body": """
<p>Denize açılmanın iki yolu var: kiralamak ya da sahip olmak. Doğru tercih, ne sıklıkla kullanacağınıza, bütçenize ve bakım sorumluluğuna bakış açınıza bağlı.</p>
<h2>Tekne kiralama</h2>
<p><strong>Artıları:</strong> düşük giriş maliyeti, bakım derdi yok, farklı tekneler deneyimleme özgürlüğü. <strong>Sınırı:</strong> sık kullanıyorsanız uzun vadede pahalı; "kendi tekneniz" hissi ve kişiselleştirme yok.</p>
<h2>Tekne sahipliği</h2>
<p><strong>Artıları:</strong> istediğin zaman denize açılma özgürlüğü, kişiselleştirme, uzun vadede sık kullanımda daha ekonomik. <strong>Sınırı:</strong> <a href="/blog/tekne-sahipligi-maliyeti/">yıllık işletme maliyeti</a> (bağlama, bakım, kışlatma) ve sorumluluk.</p>
<h2>Kaba bir kural</h2>
<p>Yılda sadece birkaç kez çıkacaksanız kiralama; sezon boyunca düzenli kullanacaksanız ve tekneyle ilgilenmekten keyif alıyorsanız sahiplik daha mantıklıdır. Sahiplik düşünüyorsanız <a href="/blog/ikinci-el-tekne-alim-rehberi/">ikinci el alım rehberimiz</a> iyi bir başlangıç.</p>
<h2>Sahiplik kararı verdiyseniz</h2>
<p>Doğru tekneyi seçmek kadar, onu iyi durumda tutmak da önemli. <a href="/blog/satin-alma-oncesi-tekne-ekspertizi/">Satın alma öncesi kontrol</a> ve düzenli bakım, sahipliği keyifli kılar. Bu yolculukta <a href="/hizmetler/fiberglas-onarim/">bakım ve onarım</a> tarafında yanınızdayız.</p>
""",
 },
 "en": {
   "category": "Guide",
   "title": "Boat Charter or Ownership? Which Suits You?",
   "excerpt": "Is chartering or owning a boat more sensible? A comparison of cost, frequency of use, maintenance responsibility and freedom.",
   "meta_title": "Boat Charter or Ownership? A Comparison | Tekne Usta",
   "meta_desc": "Boat charter vs ownership comparison: cost, frequency of use, maintenance responsibility and flexibility. A guide to deciding which suits you.",
   "body": """
<p>There are two ways to get out on the water: charter or own. The right choice depends on how often you'll use it, your budget and your view of maintenance responsibility.</p>
<h2>Chartering</h2>
<p><strong>Pros:</strong> low entry cost, no maintenance worries, freedom to try different boats. <strong>Limit:</strong> expensive long-term if you use it often; no "your own boat" feeling or personalisation.</p>
<h2>Ownership</h2>
<p><strong>Pros:</strong> freedom to sail whenever you like, personalisation, more economical long-term with frequent use. <strong>Limit:</strong> <a href="/en/blog/cost-of-boat-ownership/">annual running cost</a> (berthing, maintenance, winterising) and responsibility.</p>
<h2>A rough rule</h2>
<p>If you'll only go out a few times a year, charter; if you'll use it regularly through the season and enjoy caring for a boat, ownership makes more sense. If considering ownership, our <a href="/en/blog/used-boat-buying-guide/">used boat buying guide</a> is a good start.</p>
<h2>If you've decided to own</h2>
<p>Keeping the boat in good condition matters as much as choosing the right one. A <a href="/en/blog/pre-purchase-boat-survey/">pre-purchase check</a> and regular maintenance make ownership enjoyable. We're at your side for <a href="/en/services/fibreglass-repair/">maintenance and repair</a> on that journey.</p>
""",
 },
},
{
 "slug": "kekamoz-temizligi", "slug_en": "hull-limescale-cleaning",
 "image": "/assets/images/services/fiberglas.jpg", "date": "2028-02-02",
 "tr": {
   "category": "Bakım",
   "title": "Kekamoz Temizliği: Karinadaki İnatçı Kabuğu Sökmek",
   "excerpt": "Kekamoz nedir, neden oluşur ve karinadan nasıl temizlenir? Su hattı ve gövdedeki inatçı kireç/kabuk sorununa çözüm.",
   "meta_title": "Kekamoz Temizliği Nedir, Nasıl Yapılır? | Tekne Usta",
   "meta_desc": "Kekamoz temizliği: karina ve su hattındaki inatçı kireç/kabuk tabakası nedir, neden oluşur ve nasıl güvenle temizlenir? Jelkota zarar vermeden temizlik.",
   "body": """
<p>"Kekamoz" olarak bilinen sert kabuk, teknenin su altı yüzeyinde ve su hattında zamanla biriken kireç, deniz canlısı kalıntısı ve mineral tabakasıdır. Görünüşü bozar, sürtünmeyi artırır ve ihmal edilirse jelkota yapışıp temizliği zorlaştırır.</p>
<h2>Kekamoz neden oluşur?</h2>
<p>Tekne suda kaldıkça karinaya yosun, midye ve kireç birikir. Antifouling zayıfladığında ya da tekne uzun süre hareketsiz kaldığında bu tabaka sertleşir ve normal yıkamayla çıkmaz hâle gelir.</p>
<h2>Nasıl temizlenir?</h2>
<ul>
<li><strong>Zamanında müdahale:</strong> Tekne karaya çekilir çekilmez basınçlı yıkama — kuruyup sertleşmeden çıkarmak çok daha kolaydır.</li>
<li><strong>Kontrollü kimyasal/mekanik:</strong> Sertleşmiş kabuk, jelkota zarar vermeyecek uygun yöntemle sökülür. Aşırı sert raspa jelkotu incelttiği için dikkat gerekir.</li>
<li><strong>Sonrası:</strong> Temiz yüzeye <a href="/hizmetler/tekne-boyama-antifouling/">antifouling</a> yenilenir; böylece bir sonraki sezon kabuk baştan azalır.</li>
</ul>
<h2>Önleme</h2>
<p>Düzenli karina bakımı ve zamanında antifouling yenileme, kekamozu büyük ölçüde önler. <a href="/blog/tekne-cekek-karaya-cekme/">Karaya çekme</a> ve <a href="/blog/yillik-tekne-bakim-takvimi/">yıllık bakım</a> planı bu birikimi kontrol altında tutar.</p>
<p>Karinadaki inatçı kabuğu jelkota zarar vermeden <a href="/hizmetler/tekne-kislatma/">bakım</a> hizmetimiz kapsamında temizliyoruz.</p>
""",
 },
 "en": {
   "category": "Maintenance",
   "title": "Hull Limescale/Scale Cleaning: Removing Stubborn Crust",
   "excerpt": "What is the stubborn scale on a hull, why does it form and how is it cleaned off? A solution for crust at the waterline and hull.",
   "meta_title": "Hull Scale Cleaning: What and How | Tekne Usta",
   "meta_desc": "Hull scale cleaning: what the stubborn lime/scale layer at the hull and waterline is, why it forms and how to remove it safely without harming the gelcoat.",
   "body": """
<p>The hard crust known in Turkish as "kekamoz" is a layer of scale, marine-growth residue and minerals that builds up on the underwater surface and waterline over time. It spoils the look, increases drag and, if neglected, bonds to the gelcoat and becomes hard to remove.</p>
<h2>Why does scale form?</h2>
<p>The longer a boat stays afloat, the more weed, mussels and scale accumulate on the hull. When the antifouling weakens or the boat sits idle for long, this layer hardens and won't come off with normal washing.</p>
<h2>How is it cleaned?</h2>
<ul>
<li><strong>Timely action:</strong> pressure wash as soon as the boat is hauled out — far easier to remove before it dries and hardens.</li>
<li><strong>Controlled chemical/mechanical:</strong> hardened crust is removed with a method that won't harm the gelcoat. Over-aggressive scraping thins the gelcoat, so care is needed.</li>
<li><strong>Afterwards:</strong> <a href="/en/services/boat-painting-antifouling/">antifouling</a> is renewed on the clean surface, so next season's build-up is reduced from the start.</li>
</ul>
<h2>Prevention</h2>
<p>Regular hull maintenance and timely antifouling renewal largely prevent scale. A <a href="/en/blog/boat-haul-out-guide/">haul-out</a> and <a href="/en/blog/annual-boat-maintenance-calendar/">annual maintenance</a> plan keeps this build-up under control.</p>
<p>We clean stubborn hull crust without harming the gelcoat under our <a href="/en/services/winterising-storage/">maintenance</a> service.</p>
""",
 },
},
{
 "slug": "karbon-ile-guclendirme", "slug_en": "carbon-reinforcement",
 "image": "/assets/images/services/fiberglas.jpg", "date": "2028-02-16",
 "tr": {
   "category": "Fiberglas",
   "title": "Karbon Fiber ile Tekne Güçlendirme: Ne Zaman Gerekir?",
   "excerpt": "Karbon fiber takviyesi nedir, hangi durumlarda kullanılır ve fiberglas onarıma göre avantajı nedir?",
   "meta_title": "Karbon Fiber ile Tekne Güçlendirme Rehberi | Tekne Usta",
   "meta_desc": "Karbon fiber ile tekne güçlendirme: yüksek mukavemet, düşük ağırlık ve hangi yapısal onarımlarda karbon takviyesi kullanılır? Fiberglas ile karşılaştırma.",
   "body": """
<p>Karbon fiber, havacılık ve yarış teknelerinden bilinen, çok yüksek mukavemet/ağırlık oranına sahip bir malzemedir. Tekne onarımında da belirli durumlarda, standart cam elyafına göre üstün bir güçlendirme sağlar.</p>
<h2>Karbon takviye ne zaman gerekir?</h2>
<ul>
<li><strong>Yüksek yük bölgeleri:</strong> Direk dibi, salma bağlantısı, güverte donanımı çevresi gibi tekrarlayan strese maruz noktalar.</li>
<li><strong>Ağırlık kritikse:</strong> Performans teknelerinde, güç eklerken ağırlık eklememek istendiğinde.</li>
<li><strong>Yapısal onarım:</strong> Standart <a href="/blog/su-alti-yapisal-onarim/">yapısal onarımın</a> yetersiz kaldığı, ekstra rijitlik gereken durumlar.</li>
</ul>
<h2>Fiberglas'a göre farkı</h2>
<p>Karbon, cam elyafına göre çok daha rijit ve hafiftir; ama daha pahalıdır ve doğru uygulama (reçine oranı, kür koşulları) kritiktir. Her onarım karbon gerektirmez — çoğu iş <a href="/blog/polyester-vs-epoksi-recine/">epoksi + cam elyafı</a> ile mükemmel çözülür. Karbon, gerçekten gerektiğinde devreye girer.</p>
<h2>Doğru teşhis önce gelir</h2>
<p>Karbon güçlendirme bir "her derde deva" değildir; nerede, ne kadar ve hangi yönde lif kullanılacağı mühendislik gerektirir. Yanlış uygulanan karbon, hem para israfı hem de beklenen dayanımı vermez.</p>
<p>Teknenizde karbon takviyenin gerekip gerekmediğini <a href="/hizmetler/fiberglas-onarim/">fiberglas onarım</a> hizmetimiz kapsamında değerlendiriyoruz.</p>
""",
 },
 "en": {
   "category": "Fibreglass",
   "title": "Carbon Fibre Boat Reinforcement: When Is It Needed?",
   "excerpt": "What is carbon fibre reinforcement, in which cases is it used and what's its advantage over fibreglass repair?",
   "meta_title": "Carbon Fibre Boat Reinforcement Guide | Tekne Usta",
   "meta_desc": "Carbon fibre boat reinforcement: high strength, low weight and which structural repairs use carbon. A comparison with fibreglass.",
   "body": """
<p>Carbon fibre, known from aerospace and racing boats, is a material with a very high strength-to-weight ratio. In boat repair too, in certain cases it provides reinforcement superior to standard glass fibre.</p>
<h2>When is carbon reinforcement needed?</h2>
<ul>
<li><strong>High-load areas:</strong> points under repeated stress such as the mast step, keel attachment and around deck hardware.</li>
<li><strong>When weight is critical:</strong> on performance boats, when you want to add strength without adding weight.</li>
<li><strong>Structural repair:</strong> where standard <a href="/en/blog/underwater-structural-repair/">structural repair</a> isn't enough and extra stiffness is needed.</li>
</ul>
<h2>The difference from fibreglass</h2>
<p>Carbon is far stiffer and lighter than glass fibre; but it's more expensive and correct application (resin ratio, cure conditions) is critical. Not every repair needs carbon — most jobs are perfectly solved with <a href="/en/blog/polyester-vs-epoxy-resin/">epoxy + glass fibre</a>. Carbon comes in when it's genuinely needed.</p>
<h2>Correct diagnosis comes first</h2>
<p>Carbon reinforcement isn't a cure-all; where, how much and in which direction to lay the fibres takes engineering. Wrongly applied carbon is both a waste of money and won't give the expected strength.</p>
<p>We assess whether your boat needs carbon reinforcement under our <a href="/en/services/fibreglass-repair/">fibreglass repair</a> service.</p>
""",
 },
},
{
 "slug": "ikinci-el-tekne-10-kritik-nokta", "slug_en": "used-boat-10-checks",
 "image": "/assets/images/hakkimizda.jpg", "date": "2028-03-01",
 "tr": {
   "category": "Rehber",
   "title": "İkinci El Tekne Alırken 10 Kritik Nokta",
   "excerpt": "İkinci el tekne alırken pahalı sürprizlerden kaçınmak için gövdeden donanıma 10 maddelik hızlı kontrol listesi.",
   "meta_title": "İkinci El Tekne Alırken Dikkat Edilecek 10 Nokta | Tekne Usta",
   "meta_desc": "İkinci el tekne alırken dikkat edilmesi gereken 10 kritik nokta: gövde, osmoz, güverte, teak, donanım, bakım geçmişi ve gizli maliyetler. Hızlı kontrol listesi.",
   "body": """
<p>İkinci el tekne almak heyecan verici ama riskli olabilir. Aşağıdaki 10 maddelik liste, pahalı sürprizlerden kaçınmanıza yardımcı olur. Detaylı bir bakış için <a href="/blog/satin-alma-oncesi-tekne-ekspertizi/">satın alma öncesi kontrol</a> yazımıza da bakın.</p>
<h2>1. Gövde ve karina</h2>
<p>Çatlak, çarpma izi ve önceki onarımları arayın. Su altı yüzeyi mutlaka görülmeli.</p>
<h2>2. Osmoz (osmos/ozmoz)</h2>
<p>Kabarcık ve nem izlerini kontrol edin; <a href="/blog/osmoz-belirtileri/">osmoz belirtileri</a> pazarlıkta elinizi güçlendirir.</p>
<h2>3. Gelcoat / boya durumu</h2>
<p>Solma, çatlak ve kalın boya katmanları (gizlenmiş onarım işareti) önemlidir.</p>
<h2>4. Güverte sağlamlığı</h2>
<p>Yürürken yumuşak (su almış) bölgeler, pahalı bir güverte onarımına işaret eder.</p>
<h2>5. Teak / güverte kaplaması</h2>
<p>Teak kalınlığı ve derz durumu; inceldiyse <a href="/blog/teak-guverte-fiyatlari/">döşeme maliyeti</a> çıkabilir.</p>
<h2>6. Ahşap teknede çürük</h2>
<p>Birleşim yerlerinde kararma ve yumuşama; <a href="/blog/kalafat-nedir/">kalafat</a> ve vernik durumu bakım yükünü gösterir.</p>
<h2>7. Donanım ve tesisat</h2>
<p>Elektrik, akü, pompalar ve seyir donanımının çalışır durumu.</p>
<h2>8. Bakım geçmişi</h2>
<p>Düzenli bakım kayıtları, teknenin nasıl kullanıldığını anlatır. Kayıt yoksa dikkat.</p>
<h2>9. Belgeler</h2>
<p>Ruhsat, tonilato ve satış evraklarının eksiksizliği.</p>
<h2>10. Gerçek maliyet</h2>
<p>Satın alma fiyatına bağlama, bakım ve olası onarımı ekleyin (bkz. <a href="/blog/tekne-sahipligi-maliyeti/">sahiplik maliyeti</a>).</p>
<p>Almayı düşündüğünüz tekneyi <a href="/hizmetler/fiberglas-onarim/">fiberglas</a> ve <a href="/hizmetler/ahsap-tekne-renovasyonu/">ahşap</a> tarafında birlikte değerlendirebiliriz — bize yazın.</p>
""",
 },
 "en": {
   "category": "Guide",
   "title": "10 Critical Checks When Buying a Used Boat",
   "excerpt": "A 10-point quick checklist from hull to gear to avoid expensive surprises when buying a used boat.",
   "meta_title": "10 Critical Checks When Buying a Used Boat | Tekne Usta",
   "meta_desc": "10 critical checks when buying a used boat: hull, osmosis, deck, teak, gear, maintenance history and hidden costs. A quick checklist.",
   "body": """
<p>Buying a used boat is exciting but can be risky. The 10-point list below helps you avoid expensive surprises. For a deeper look, see our <a href="/en/blog/pre-purchase-boat-survey/">pre-purchase check</a> article.</p>
<h2>1. Hull and underbody</h2>
<p>Look for cracks, impact marks and previous repairs. The underwater surface must be seen.</p>
<h2>2. Osmosis</h2>
<p>Check for blisters and moisture marks; <a href="/en/blog/osmosis-symptoms/">osmosis signs</a> strengthen your hand in negotiation.</p>
<h2>3. Gelcoat / paint condition</h2>
<p>Fading, cracks and thick paint layers (a sign of hidden repairs) matter.</p>
<h2>4. Deck soundness</h2>
<p>Soft (water-ingressed) spots underfoot point to an expensive deck repair.</p>
<h2>5. Teak / deck covering</h2>
<p>Teak thickness and seam condition; if thinned, a <a href="/en/blog/teak-deck-cost/">decking cost</a> may arise.</p>
<h2>6. Rot on wooden boats</h2>
<p>Darkening and softness at joints; <a href="/en/blog/caulking-explained/">caulking</a> and varnish condition show the maintenance burden.</p>
<h2>7. Gear and systems</h2>
<p>Electrics, battery, pumps and navigation gear in working order.</p>
<h2>8. Maintenance history</h2>
<p>Regular records tell how the boat was used. No records — be cautious.</p>
<h2>9. Documents</h2>
<p>Completeness of registration, tonnage and sale papers.</p>
<h2>10. The real cost</h2>
<p>Add berthing, maintenance and possible repair to the purchase price (see <a href="/en/blog/cost-of-boat-ownership/">cost of ownership</a>).</p>
<p>We can assess the boat you're considering together on the <a href="/en/services/fibreglass-repair/">fibreglass</a> and <a href="/en/services/wooden-boat-refit/">wood</a> side — message us.</p>
""",
 },
},
{
 "slug": "raspa-kumlama", "slug_en": "blasting-soda-blasting",
 "image": "/assets/images/services/fiberglas.jpg", "date": "2028-03-15",
 "tr": {
   "category": "Boya",
   "title": "Raspa ve Kumlama: Eski Boyayı Doğru Sökmek",
   "excerpt": "Kat kat birikmiş eski antifouling ve boya nasıl sökülür? Raspa, kumlama ve soda blasting yöntemleri, avantaj ve riskleri.",
   "meta_title": "Raspa ve Kumlama (Soda Blasting) Rehberi | Tekne Usta",
   "meta_desc": "Tekne raspa ve kumlama: kat kat birikmiş eski boya ve antifouling nasıl sökülür? Mekanik raspa, kumlama ve soda blasting yöntemlerinin farkı ve jelkot güvenliği.",
   "body": """
<p>Yıllar içinde antifouling ve boya katları birikir; yeni boya artık düzgün tutunmaz ve yüzey pürüzlenir. Bu noktada eski katmanların sökülmesi gerekir. En doğru yöntem, teknenin yüzeyine ve duruma bağlıdır.</p>
<h2>Yöntemler</h2>
<ul>
<li><strong>Mekanik raspa / zımpara:</strong> Kontrollü ama yavaş; küçük alanlar için uygun.</li>
<li><strong>Kumlama (grit blasting):</strong> Hızlı ve etkili ama agresiftir; jelkotu inceltme riski yüksek, deneyim ister.</li>
<li><strong>Soda blasting:</strong> Karbonat bazlı, daha yumuşak; jelkota daha az zarar verir, fiberglas için sık tercih edilir.</li>
<li><strong>Kimyasal sökücü:</strong> Belirli boyalarda etkili; çevre ve güvenlik önlemi gerektirir.</li>
</ul>
<h2>Jelkot güvenliği</h2>
<p>Fiber teknede en büyük risk, sökme sırasında jelkotu inceltmek veya delmektir. Bu yüzden yöntem ve basınç, yüzeyi koruyacak şekilde ayarlanmalı. Amaç boyayı almak; jelkotu değil.</p>
<h2>Sonrası</h2>
<p>Temiz yüzeye uygun <a href="/blog/boya-oncesi-yuzey-hazirligi/">yüzey hazırlığı</a> ve astar uygulanır; ardından <a href="/hizmetler/tekne-boyama-antifouling/">boya/antifouling</a> yenilenir. Osmoz şüphesi varsa bu aşama, <a href="/blog/osmoz-belirtileri/">nem kontrolü</a> için de fırsattır.</p>
<p>Eski boyayı jelkota zarar vermeden sökme işini <a href="/hizmetler/tekne-boyama-antifouling/">boya</a> hizmetimiz kapsamında yapıyoruz.</p>
""",
 },
 "en": {
   "category": "Painting",
   "title": "Blasting and Sanding: Removing Old Paint Correctly",
   "excerpt": "How is built-up old antifouling and paint removed? Sanding, grit blasting and soda blasting methods, their advantages and risks.",
   "meta_title": "Blasting and Soda Blasting Guide | Tekne Usta",
   "meta_desc": "Boat blasting and sanding: how to remove built-up old paint and antifouling. The difference between mechanical sanding, grit and soda blasting, and gelcoat safety.",
   "body": """
<p>Over the years antifouling and paint layers build up; new paint no longer bonds well and the surface roughens. At this point old layers must be removed. The right method depends on the boat's surface and condition.</p>
<h2>Methods</h2>
<ul>
<li><strong>Mechanical sanding:</strong> controlled but slow; suited to small areas.</li>
<li><strong>Grit blasting:</strong> fast and effective but aggressive; high risk of thinning the gelcoat, needs experience.</li>
<li><strong>Soda blasting:</strong> bicarbonate-based, gentler; harms the gelcoat less, often preferred for fibreglass.</li>
<li><strong>Chemical stripper:</strong> effective on certain paints; needs environmental and safety precautions.</li>
</ul>
<h2>Gelcoat safety</h2>
<p>On a fibreglass boat, the biggest risk is thinning or breaching the gelcoat during removal. So method and pressure must be set to protect the surface. The aim is to remove the paint, not the gelcoat.</p>
<h2>Afterwards</h2>
<p>The clean surface gets proper <a href="/en/blog/surface-prep-before-painting/">surface prep</a> and primer; then <a href="/en/services/boat-painting-antifouling/">paint/antifouling</a> is renewed. If osmosis is suspected, this stage is also a chance for a <a href="/en/blog/osmosis-symptoms/">moisture check</a>.</p>
<p>We remove old paint without harming the gelcoat under our <a href="/en/services/boat-painting-antifouling/">painting</a> service.</p>
""",
 },
},
{
 "slug": "gelcoat-cizik-sararma-giderme", "slug_en": "gelcoat-scratch-yellowing",
 "image": "/assets/images/services/fiberglas.jpg", "date": "2028-03-29",
 "tr": {
   "category": "Fiberglas",
   "title": "Gelcoat Çizik ve Sararma Giderme: Parlaklığı Geri Kazanmak",
   "excerpt": "Jelkottaki çizik, sararma ve su hattı lekesi nasıl giderilir? Parlatmadan bölgesel onarıma pratik çözümler.",
   "meta_title": "Gelcoat Çizik ve Sararma Giderme Rehberi | Tekne Usta",
   "meta_desc": "Gelcoat çizik ve sararma giderme: jelkottaki çizik, sararma, su hattı lekesi ve oksidasyon nasıl giderilir? Parlatma ve bölgesel onarım çözümleri.",
   "body": """
<p>Jelkot zamanla çizilir, sararır ve su hattında lekelenir. Çoğu durumda tekneyi boyamaya gerek kalmadan, doğru işlemle parlaklık büyük ölçüde geri kazanılır.</p>
<h2>Hangi sorun, hangi çözüm?</h2>
<ul>
<li><strong>Yüzeysel çizik / mat oksidasyon:</strong> Aşındırıcı pasta ve makineyle <a href="/blog/gelcoat-yenileme/">parlatma (cut &amp; polish)</a>; altındaki sağlam parlak yüzey açığa çıkar.</li>
<li><strong>Sararma:</strong> Yaşlanan beyaz jelkot krem tonuna kayar; parlatma çoğunlukla toparlar, ileri durumda bölgesel yenileme gerekir.</li>
<li><strong>Su hattı lekesi:</strong> Uygun temizleyici ve parlatma ile giderilir; inatçıysa yüzey işlemi gerekir.</li>
<li><strong>Derin çizik:</strong> Jelkota inen çizikler dolgu + parlatma ile onarılır.</li>
</ul>
<h2>Koruma</h2>
<p>Parlatma sonrası uygulanan koruyucu cila/wax, parlaklığın ömrünü uzatır ve yeni oksidasyonu geciktirir. Düzenli bakım, komple yenilemeyi yıllarca erteler (bkz. <a href="/blog/fiberglas-tekne-bakimi/">fiberglas bakımı</a>).</p>
<h2>Ne zaman yetmez?</h2>
<p>Jelkot fazla incelmiş veya geniş alanda dökülmüşse parlatma yetmez; <a href="/blog/jelkot-vs-boya/">gelcoat yenileme veya boya</a> gündeme gelir.</p>
<p>Teknenizin jelkotunu <a href="/hizmetler/fiberglas-onarim/">fiberglas onarım</a> hizmetimiz kapsamında değerlendirip en ekonomik çözümü öneriyoruz.</p>
""",
 },
 "en": {
   "category": "Fibreglass",
   "title": "Removing Gelcoat Scratches and Yellowing: Restoring Gloss",
   "excerpt": "How to remove scratches, yellowing and waterline stains from gelcoat? Practical solutions from polishing to spot repair.",
   "meta_title": "Removing Gelcoat Scratches and Yellowing | Tekne Usta",
   "meta_desc": "Removing gelcoat scratches and yellowing: how to fix scratches, yellowing, waterline stains and oxidation on gelcoat. Polishing and spot-repair solutions.",
   "body": """
<p>Gelcoat scratches, yellows and stains at the waterline over time. In most cases the gloss can be largely restored with the right process, without repainting the boat.</p>
<h2>Which problem, which solution?</h2>
<ul>
<li><strong>Surface scratch / dull oxidation:</strong> <a href="/en/blog/gelcoat-renewal/">cut &amp; polish</a> with compound and machine exposes the sound gloss beneath.</li>
<li><strong>Yellowing:</strong> ageing white gelcoat drifts to cream; polishing usually recovers it, advanced cases need a spot renewal.</li>
<li><strong>Waterline stains:</strong> removed with a suitable cleaner and polish; stubborn ones need surface work.</li>
<li><strong>Deep scratches:</strong> scratches into the gelcoat are repaired with fill + polish.</li>
</ul>
<h2>Protection</h2>
<p>A protective wax after polishing extends the gloss and delays new oxidation. Regular care postpones a full renewal for years (see <a href="/en/blog/fibreglass-boat-care/">fibreglass care</a>).</p>
<h2>When isn't it enough?</h2>
<p>If the gelcoat has thinned too far or is flaking over a wide area, polishing won't do; <a href="/en/blog/gelcoat-vs-paint/">gelcoat renewal or paint</a> comes into play.</p>
<p>We assess your gelcoat under our <a href="/en/services/fibreglass-repair/">fibreglass repair</a> service and recommend the most economical solution.</p>
""",
 },
},
{
 "slug": "sintine-boyasi", "slug_en": "bilge-paint",
 "image": "/assets/images/services/boya.jpg", "date": "2028-04-12",
 "tr": {
   "category": "Boya",
   "title": "Sintine Boyası: Teknenin Görünmeyen Ama Önemli Yüzeyi",
   "excerpt": "Sintine neden boyanır, hangi boya kullanılır ve doğru uygulama nasıl olur? Nem, yağ ve kokuya karşı koruma.",
   "meta_title": "Sintine Boyası Nedir, Nasıl Uygulanır? | Tekne Usta",
   "meta_desc": "Sintine boyası: teknenin sintine bölgesi neden boyanır, hangi boya kullanılır ve nasıl uygulanır? Neme, yağa ve kokuya dayanıklı sintine koruması.",
   "body": """
<p>Sintine (bilge), teknenin en dibindeki, suyun ve sızıntıların toplandığı bölgedir. Göz önünde olmasa da doğru boyanması hem hijyen hem koruma açısından önemlidir.</p>
<h2>Sintine neden boyanır?</h2>
<p>Sürekli nem, yağ ve tuz sintineyi yıpratır; boyasız yüzey lekelenir, kokar ve zamanla zarar görür. İyi bir sintine boyası; nemi iter, temizliği kolaylaştırır ve yüzeyi korur.</p>
<h2>Hangi boya?</h2>
<p>Sintinede neme ve yağa dayanıklı, kolay temizlenen özel boyalar kullanılır. Açık renkler tercih edilir — çünkü sintinedeki bir sızıntıyı (yağ, su) erken fark etmeyi sağlar; bu bir güvenlik avantajıdır.</p>
<h2>Doğru uygulama</h2>
<p>Sintine önce iyice temizlenip yağdan arındırılır ve kurutulur; nemli yüzeye atılan boya tutmaz. Ardından uygun astar ve boya uygulanır. Ulaşılması zor bir alan olduğu için işçilik ve erişim önemlidir.</p>
<p>Sintine boyası ve iç yüzey korumasını <a href="/hizmetler/tekne-boyama-antifouling/">boya</a> hizmetimiz kapsamında yapıyoruz; iç mekan yenilemeyle birlikte planlanabilir.</p>
""",
 },
 "en": {
   "category": "Painting",
   "title": "Bilge Paint: The Boat's Unseen but Important Surface",
   "excerpt": "Why is the bilge painted, which paint is used and how is it applied correctly? Protection against damp, oil and odour.",
   "meta_title": "What Is Bilge Paint and How to Apply It | Tekne Usta",
   "meta_desc": "Bilge paint: why the bilge is painted, which paint is used and how it's applied. Bilge protection resistant to damp, oil and odour.",
   "body": """
<p>The bilge is the lowest part of the boat, where water and leaks collect. Out of sight though it is, painting it correctly matters for both hygiene and protection.</p>
<h2>Why paint the bilge?</h2>
<p>Constant damp, oil and salt wear the bilge; an unpainted surface stains, smells and eventually suffers. A good bilge paint repels moisture, makes cleaning easier and protects the surface.</p>
<h2>Which paint?</h2>
<p>The bilge uses special paints resistant to damp and oil and easy to clean. Light colours are preferred — they help spot a leak (oil, water) early, a safety advantage.</p>
<h2>Correct application</h2>
<p>The bilge is first thoroughly cleaned, degreased and dried; paint over a damp surface won't hold. Then the right primer and paint are applied. As a hard-to-reach area, workmanship and access matter.</p>
<p>We do bilge paint and interior-surface protection under our <a href="/en/services/boat-painting-antifouling/">painting</a> service; it can be planned alongside an interior refit.</p>
""",
 },
},
{
 "slug": "boya-oncesi-yuzey-hazirligi", "slug_en": "surface-prep-before-painting",
 "image": "/assets/images/services/boya.jpg", "date": "2028-04-26",
 "tr": {
   "category": "Boya",
   "title": "Boya Öncesi Yüzey Hazırlığı: Kalıcı Bitişin Görünmeyen Sırrı",
   "excerpt": "İyi bir boya işinin %80'i hazırlıktır. Temizlik, zımpara, dolgu ve astar adımları neden bu kadar önemli?",
   "meta_title": "Boya Öncesi Yüzey Hazırlığı Adım Adım | Tekne Usta",
   "meta_desc": "Tekne boyama öncesi yüzey hazırlığı: temizlik, yağ alma, zımpara, dolgu (fairing) ve astar. Kalıcı, kabarmayan bir boya bitişi için adım adım rehber.",
   "body": """
<p>Tekne sahiplerinin en sık yaptığı hata, boyanın markasına bakıp hazırlığı küçümsemektir. Oysa kalıcı bir bitişin çoğu, boyadan önceki görünmeyen adımlarda belirlenir.</p>
<h2>Adım adım hazırlık</h2>
<ul>
<li><strong>Temizlik ve yağ alma:</strong> Yüzeydeki kir, tuz ve silikon/yağ kalıntısı temizlenir. Yağlı yüzeye boya tutmaz.</li>
<li><strong>Zımpara:</strong> Yeni katın tutunması için yüzey "diş" verecek şekilde matlaştırılır.</li>
<li><strong>Dolgu (fairing):</strong> Çukur, çizik ve düzensizlikler doldurulup düzeltilir — pürüzsüz bir zemin, pürüzsüz bir bitiş demektir.</li>
<li><strong>Astar (primer):</strong> Boyanın tutunmasını ve örtücülüğünü sağlayan kritik kat. Renk değişiminde özellikle önemlidir.</li>
</ul>
<h2>Neden bu kadar önemli?</h2>
<p>Hazırlıktan kısan bir iş kısa sürede kabarır, dökülür ve baştan yapılması gerekir — yani ucuz görünen iş pahalıya patlar. Doğru hazırlık, en dayanıklı boyanın bile ön koşuludur.</p>
<h2>Şeffaf teklifte hazırlık görünür</h2>
<p>İyi bir teklif; hazırlık, astar, kat sayısı ve işçiliği ayrı gösterir (bkz. <a href="/blog/tekne-boyama-maliyeti/">boyama maliyeti</a>). Biz bu formatta çalışır, hangi adıma ne kadar emek gittiğini net belirtiriz.</p>
<p>Yüzey hazırlığı dahil komple boya işini <a href="/hizmetler/tekne-boyama-antifouling/">tekne boyama</a> hizmetimiz kapsamında yapıyoruz.</p>
""",
 },
 "en": {
   "category": "Painting",
   "title": "Surface Prep Before Painting: The Invisible Secret to a Lasting Finish",
   "excerpt": "80% of a good paint job is prep. Why are cleaning, sanding, fairing and priming so important?",
   "meta_title": "Surface Prep Before Painting, Step by Step | Tekne Usta",
   "meta_desc": "Surface prep before boat painting: cleaning, degreasing, sanding, fairing and priming. A step-by-step guide to a lasting, non-blistering paint finish.",
   "body": """
<p>The most common mistake boat owners make is judging by the paint brand while underrating the prep. Yet most of a lasting finish is decided in the invisible steps before the paint.</p>
<h2>Prep, step by step</h2>
<ul>
<li><strong>Cleaning and degreasing:</strong> dirt, salt and silicone/oil residue are removed. Paint won't hold on a greasy surface.</li>
<li><strong>Sanding:</strong> the surface is keyed so the new coat grips.</li>
<li><strong>Fairing:</strong> dents, scratches and unevenness are filled and smoothed — a smooth base means a smooth finish.</li>
<li><strong>Primer:</strong> the critical coat that provides adhesion and coverage. Especially important in a colour change.</li>
</ul>
<h2>Why does it matter so much?</h2>
<p>A job that skimps on prep soon blisters, flakes and must be redone — so the cheap-looking job costs more. Correct prep is the precondition for even the most durable paint.</p>
<h2>Prep shows in a transparent quote</h2>
<p>A good quote shows prep, primer, coat count and labour separately (see <a href="/en/blog/boat-painting-cost/">painting cost</a>). We work in this format and state clearly how much effort each step takes.</p>
<p>We do complete painting including surface prep under our <a href="/en/services/boat-painting-antifouling/">boat painting</a> service.</p>
""",
 },
},
{
 "slug": "aluminyum-tekne-boyama", "slug_en": "aluminium-boat-painting",
 "image": "/assets/images/services/boya.jpg", "date": "2028-05-10",
 "tr": {
   "category": "Boya",
   "title": "Alüminyum Tekne Boyama: Neden Farklı, Neye Dikkat?",
   "excerpt": "Alüminyum teknelerde boya ve antifouling neden özel dikkat ister? Korozyon, bakırsız boya ve doğru astar sistemi.",
   "meta_title": "Alüminyum Tekne Boyama ve Antifouling | Tekne Usta",
   "meta_desc": "Alüminyum tekne boyama: galvanik korozyon riski, bakırsız antifouling, doğru astar sistemi ve yüzey hazırlığı. Alüminyum gövdelerde boya için bilinmesi gerekenler.",
   "body": """
<p>Alüminyum tekneler hafif ve dayanıklıdır ama boya konusunda fiberglas ve ahşaptan farklı kurallara tabidir. Yanlış boya sistemi, korozyona ve ciddi hasara yol açabilir.</p>
<h2>En kritik konu: bakırsız antifouling</h2>
<p>Standart antifouling boyaların çoğu bakır içerir. Bakır, alüminyumla temas ettiğinde <a href="/blog/anot-zinc-bakimi/">galvanik korozyonu</a> tetikler. Bu yüzden alüminyum teknelerde mutlaka <strong>bakırsız</strong> antifouling kullanılmalıdır.</p>
<h2>Doğru astar sistemi</h2>
<p>Alüminyumda boyanın tutunması ve metalin korunması için özel astar (genelde epoksi bazlı) sistemleri gerekir. Yüzey hazırlığı ve astar, alüminyumda fiberglastan daha da belirleyicidir.</p>
<h2>Yüzey hazırlığı</h2>
<p>Alüminyum yüzeyin doğru temizlenmesi ve aktive edilmesi, boyanın uzun ömürlü olması için şarttır. <a href="/blog/boya-oncesi-yuzey-hazirligi/">Yüzey hazırlığı</a> ihmal edilirse boya kısa sürede kalkar.</p>
<h2>Uzmanlık ister</h2>
<p>Alüminyum boyama, malzeme bilgisi gerektiren bir iştir; doğru ürün ve sistem seçimi kritiktir. Antifouling türleri için <a href="/blog/antifouling-secimi/">seçim rehberimize</a> bakın.</p>
<p>Alüminyum teknenizin boya ve antifouling'ini doğru sistemle <a href="/hizmetler/tekne-boyama-antifouling/">boya</a> hizmetimiz kapsamında yapıyoruz.</p>
""",
 },
 "en": {
   "category": "Painting",
   "title": "Aluminium Boat Painting: Why Different, What to Watch",
   "excerpt": "Why do paint and antifouling need special care on aluminium boats? Corrosion, copper-free paint and the right primer system.",
   "meta_title": "Aluminium Boat Painting and Antifouling | Tekne Usta",
   "meta_desc": "Aluminium boat painting: galvanic corrosion risk, copper-free antifouling, the right primer system and surface prep. What to know for painting aluminium hulls.",
   "body": """
<p>Aluminium boats are light and durable but follow different paint rules than fibreglass and wood. The wrong paint system can cause corrosion and serious damage.</p>
<h2>The critical issue: copper-free antifouling</h2>
<p>Most standard antifouling paints contain copper. In contact with aluminium, copper triggers <a href="/en/blog/anode-zinc-care/">galvanic corrosion</a>. So aluminium boats must use <strong>copper-free</strong> antifouling.</p>
<h2>The right primer system</h2>
<p>Aluminium needs special primer systems (usually epoxy-based) for adhesion and metal protection. Surface prep and primer are even more decisive on aluminium than on fibreglass.</p>
<h2>Surface prep</h2>
<p>Correctly cleaning and activating the aluminium surface is essential for durable paint. Neglect <a href="/en/blog/surface-prep-before-painting/">surface prep</a> and the paint soon lifts.</p>
<h2>It takes expertise</h2>
<p>Aluminium painting requires material knowledge; choosing the right product and system is critical. For antifouling types, see our <a href="/en/blog/choosing-antifouling/">selection guide</a>.</p>
<p>We paint and antifoul your aluminium boat with the right system under our <a href="/en/services/boat-painting-antifouling/">painting</a> service.</p>
""",
 },
},
{
 "slug": "birmanya-teak-nedir", "slug_en": "burmese-teak",
 "image": "/assets/images/services/ic-mekan.jpg", "date": "2028-05-24",
 "tr": {
   "category": "Teak",
   "title": "Birmanya Teak Nedir? Neden Denizciliğin Altın Standardı",
   "excerpt": "Birmanya tik neden en kaliteli teak sayılır? Doğal yağ içeriği, dayanıklılık ve alternatiflerinden farkı.",
   "meta_title": "Birmanya Teak (Tik) Nedir? Rehber | Tekne Usta",
   "meta_desc": "Birmanya teak nedir, neden en kaliteli tik sayılır? Doğal yağ içeriği, su ve çürüğe dayanıklılık, alternatiflerinden farkı ve güvertede kullanımı.",
   "body": """
<p>Teak (tik), denizcilikte güvertenin altın standardıdır; bunların arasında da <strong>Birmanya teak</strong> uzun yıllardır en kaliteli kabul edilir. Peki farkı nedir?</p>
<h2>Neden bu kadar değerli?</h2>
<p>Birmanya teakının en büyük özelliği, ağacın kendi bünyesindeki <strong>doğal yağ ve silika oranıdır</strong>. Bu doğal yağ, ahşabı su, çürük ve haşereye karşı içeriden korur — bu yüzden teak, tuzlu deniz ortamında bile on yıllarca dayanır.</p>
<h2>Güvertede neden tercih edilir?</h2>
<ul>
<li>Islakken bile <strong>kaymaz</strong> bir yüzey verir — güvenlik.</li>
<li>Zamanla incelse de yapısını korur; boyutsal olarak kararlıdır.</li>
<li>Doğal dokusu ve sıcak tonu, klasik prestijin simgesidir.</li>
</ul>
<h2>Alternatifler</h2>
<p>Kaynak kısıtları ve maliyet nedeniyle bugün farklı menşeli teak ve <a href="/blog/sentetik-teak-alternatifleri/">sentetik alternatifler</a> de yaygın. Doğal ile sentetik karşılaştırması için <a href="/blog/teak-vs-sentetik-teak/">bu yazıya</a> bakın.</p>
<h2>Bakım</h2>
<p>Doğal teak, kalitesi ne olursa olsun düzenli <a href="/blog/teak-guverte-bakimi/">bakım</a> ister — griye dönmeyi önlemek ve derzleri korumak için. Teak güverte döşeme ve yenilemeyi <a href="/hizmetler/teak-guverte-doseme/">bu hizmetimiz</a> kapsamında yapıyoruz.</p>
""",
 },
 "en": {
   "category": "Teak",
   "title": "What Is Burmese Teak? Why the Gold Standard of Boating",
   "excerpt": "Why is Burmese teak considered the finest? Its natural oil content, durability and how it differs from alternatives.",
   "meta_title": "What Is Burmese Teak? A Guide | Tekne Usta",
   "meta_desc": "What is Burmese teak and why is it considered the finest? Its natural oil content, resistance to water and rot, difference from alternatives and use on deck.",
   "body": """
<p>Teak is the gold standard of decking in boating; and among teaks, <strong>Burmese teak</strong> has long been considered the finest. So what sets it apart?</p>
<h2>Why so prized?</h2>
<p>Burmese teak's greatest quality is the <strong>natural oil and silica content</strong> within the wood. This natural oil protects the timber from water, rot and pests from within — which is why teak lasts decades even in a salty marine environment.</p>
<h2>Why preferred on deck?</h2>
<ul>
<li>Gives a <strong>non-slip</strong> surface even when wet — safety.</li>
<li>Keeps its structure even as it thins over time; dimensionally stable.</li>
<li>Its natural grain and warm tone are a symbol of classic prestige.</li>
</ul>
<h2>Alternatives</h2>
<p>Due to supply limits and cost, teak of other origins and <a href="/en/blog/synthetic-teak-alternatives/">synthetic alternatives</a> are now common. For a natural-vs-synthetic comparison, see <a href="/en/blog/teak-vs-synthetic-teak/">this article</a>.</p>
<h2>Care</h2>
<p>Natural teak, whatever its quality, needs regular <a href="/en/blog/teak-deck-maintenance/">care</a> — to prevent greying and protect the seams. We lay and renew teak decks under <a href="/en/services/teak-deck/">this service</a>.</p>
""",
 },
},
{
 "slug": "teak-yagi-surulmeli-mi", "slug_en": "should-you-oil-teak",
 "image": "/assets/images/services/ic-mekan.jpg", "date": "2028-06-07",
 "tr": {
   "category": "Teak",
   "title": "Teak Yağı Sürülmeli mi? Tartışmalı Konuya Net Bakış",
   "excerpt": "Teak yağı teakı korur mu yoksa zarar mı verir? Yağlama ile yağsız bakımın avantajları ve dezavantajları.",
   "meta_title": "Teak Yağı Sürülmeli mi? Uzman Görüşü | Tekne Usta",
   "meta_desc": "Teak yağı sürülmeli mi? Teak yağının avantajları, dezavantajları ve yağsız bakım alternatifi. Denizde teak güvertesi için doğru bakım kararı.",
   "body": """
<p>Teak sahiplerinin en çok tartıştığı sorulardan biri: "Teak yağı sürmeli miyim?" Cevap sandığınızdan daha nüanslı; kullanımınıza göre değişir.</p>
<h2>Teak yağının cazibesi</h2>
<p>Yağ, teaka anında sıcak ve zengin bir ton kazandırır; yeni yağlanmış bir güverte gerçekten güzel görünür. Bu kısa vadeli estetik, yağın en büyük çekiciliğidir.</p>
<h2>Ama dikkat: dezavantajları</h2>
<ul>
<li>Yağ sıcakta <strong>yapışkanlaşır</strong> ve toz/kir tutar.</li>
<li>Nemli ortamda <strong>küf ve siyah leke</strong> için zemin hazırlayabilir.</li>
<li>Düzenli yenileme ister; aksi halde eşit olmayan, lekeli bir görünüm oluşur.</li>
</ul>
<h2>Yağsız bakım alternatifi</h2>
<p>Birçok profesyonel, denizde <strong>yağsız bakımı</strong> tercih eder: düzenli nazik temizlik (damar yönünde yumuşak fırça) teakın doğal grileşmesine izin verir — ki bu grilik zarar değildir, sadece estetik bir tercihtir. Teak sağlamsa gri, sıcak tona geri getirilebilir.</p>
<h2>Karar</h2>
<p>Sıklıkla bakım yapabiliyor ve o sıcak tonu istiyorsanız yağ; düşük bakımla sağlıklı teak istiyorsanız yağsız yol mantıklı. Detay için <a href="/blog/teak-guverte-bakimi/">teak bakımı</a> yazımıza bakın.</p>
<p>Teakınızın durumuna göre doğru bakım yaklaşımını <a href="/hizmetler/teak-guverte-doseme/">teak güverte döşeme</a> hizmetimiz kapsamında birlikte belirliyoruz.</p>
""",
 },
 "en": {
   "category": "Teak",
   "title": "Should You Oil Teak? A Clear Look at a Debated Topic",
   "excerpt": "Does teak oil protect teak or harm it? The pros and cons of oiling versus oil-free care.",
   "meta_title": "Should You Oil Teak? Expert View | Tekne Usta",
   "meta_desc": "Should you oil teak? The pros and cons of teak oil and the oil-free care alternative. The right maintenance decision for a teak deck at sea.",
   "body": """
<p>One of the most debated questions among teak owners: "Should I oil my teak?" The answer is more nuanced than you'd think; it depends on your use.</p>
<h2>The appeal of teak oil</h2>
<p>Oil instantly gives teak a warm, rich tone; a freshly oiled deck really does look beautiful. This short-term aesthetic is oil's biggest draw.</p>
<h2>But beware: the downsides</h2>
<ul>
<li>Oil goes <strong>tacky</strong> in heat and holds dust/dirt.</li>
<li>In damp conditions it can set the stage for <strong>mould and black stains</strong>.</li>
<li>It needs regular renewal; otherwise you get an uneven, blotchy look.</li>
</ul>
<h2>The oil-free alternative</h2>
<p>Many professionals prefer <strong>oil-free care</strong> at sea: regular gentle cleaning (a soft brush along the grain) lets teak grey naturally — and that grey isn't damage, just an aesthetic choice. If the teak is sound, grey can be brought back to a warm tone.</p>
<h2>The decision</h2>
<p>If you can maintain it often and want that warm tone, oil; if you want healthy teak with low upkeep, the oil-free route makes sense. For detail, see our <a href="/en/blog/teak-deck-maintenance/">teak care</a> article.</p>
<p>We decide the right care approach for your teak's condition together under our <a href="/en/services/teak-deck/">teak decking</a> service.</p>
""",
 },
},
{
 "slug": "ustupu-kalafat-teknikleri", "slug_en": "oakum-caulking-techniques",
 "image": "/assets/images/services/ahsap.jpg", "date": "2028-06-21",
 "tr": {
   "category": "Ahşap",
   "title": "Üstüpü ve Geleneksel Kalafat Teknikleri",
   "excerpt": "Geleneksel kalafatta üstüpü nasıl kullanılır? Yüzyıllık bu zanaatın adımları ve modern yöntemlerle ilişkisi.",
   "meta_title": "Üstüpü ve Geleneksel Kalafat Teknikleri | Tekne Usta",
   "meta_desc": "Üstüpü ve geleneksel kalafat teknikleri: pamuk/keten üstüpünün derze çakılması, macunlama ve su sızdırmazlık. Ahşap teknede yüzyıllık kalafat zanaatı.",
   "body": """
<p><a href="/blog/kalafat-nedir/">Kalafat</a>, ahşap teknenin su üstünde kalmasını sağlayan yüzyıllık zanaattır. Geleneksel yöntemin merkezinde ise "üstüpü" vardır.</p>
<h2>Üstüpü nedir?</h2>
<p>Üstüpü, pamuk veya keten liflerinden oluşan, derzlere çakılan bir dolgu malzemesidir. Ahşap kaplamalar arasındaki derze özel keskilerle sıkıştırılarak yerleştirilir ve su geçirmez bir tıkaç oluşturur.</p>
<h2>Geleneksel adımlar</h2>
<ul>
<li><strong>Derz hazırlığı:</strong> Eski dolgu temizlenir, derz açılır.</li>
<li><strong>Üstüpü çakma:</strong> Lif, derze uygun sıkılıkta ve katmanda yerleştirilir — az olursa sızdırır, çok olursa ahşabı zorlar.</li>
<li><strong>Macunlama:</strong> Üzeri geleneksel macun veya modern esnek dolguyla kapatılır.</li>
</ul>
<h2>Ahşabın hareketiyle uyum</h2>
<p>İyi bir kalafatın sırrı, ahşabın nemle şişip kururken yaptığı harekete uyum sağlamasıdır. Fazla sert veya yanlış yerleştirilmiş üstüpü, derzin açılmasına ya da tahtayı zorlamasına yol açar. Bu yüzden kalafat, deneyim ve el hassasiyeti isteyen bir iştir.</p>
<h2>Gelenek + modern</h2>
<p>Bugün geleneksel üstüpü ile modern esnek dolguları teknenin yapısına göre birlikte kullanıyoruz. Kalafat ve ahşap işlerini <a href="/hizmetler/ahsap-tekne-renovasyonu/">ahşap tekne renovasyonu</a> hizmetimiz kapsamında yapıyoruz.</p>
""",
 },
 "en": {
   "category": "Wood",
   "title": "Oakum and Traditional Caulking Techniques",
   "excerpt": "How is oakum used in traditional caulking? The steps of this centuries-old craft and its relation to modern methods.",
   "meta_title": "Oakum and Traditional Caulking Techniques | Tekne Usta",
   "meta_desc": "Oakum and traditional caulking techniques: driving cotton/flax oakum into seams, paying and watertightness. The centuries-old caulking craft on wooden boats.",
   "body": """
<p><a href="/en/blog/caulking-explained/">Caulking</a> is the centuries-old craft that keeps a wooden boat afloat. At the heart of the traditional method is "oakum".</p>
<h2>What is oakum?</h2>
<p>Oakum is a filling material of cotton or flax fibres driven into the seams. It's set into the seam between planks with special irons, compressed to form a watertight plug.</p>
<h2>Traditional steps</h2>
<ul>
<li><strong>Seam preparation:</strong> old filling is cleaned out and the seam opened.</li>
<li><strong>Driving the oakum:</strong> the fibre is set into the seam at the right tightness and in the right layers — too little leaks, too much strains the wood.</li>
<li><strong>Paying:</strong> the top is sealed with traditional stopping or a modern flexible compound.</li>
</ul>
<h2>Working with the wood's movement</h2>
<p>The secret to good caulking is accommodating the movement the wood makes as it swells and dries with moisture. Oakum that is too hard or wrongly set causes the seam to open or strains the plank. So caulking is work that takes experience and a delicate hand.</p>
<h2>Tradition + modern</h2>
<p>Today we combine traditional oakum with modern flexible sealants according to the boat's construction. We do caulking and woodwork under our <a href="/en/services/wooden-boat-refit/">wooden boat refit</a> service.</p>
""",
 },
},
{
 "slug": "tekne-folyo-kaplama", "slug_en": "boat-vinyl-wrap",
 "image": "/assets/images/services/boya.jpg", "date": "2028-07-05",
 "tr": {
   "category": "Boya",
   "title": "Tekne Folyo Kaplama: Boyaya Alternatif mi, Tamamlayıcı mı?",
   "excerpt": "Tekne folyo (vinil wrap) kaplama nedir, boyaya göre avantaj ve dezavantajları neler? Renk değişimi için doğru seçim.",
   "meta_title": "Tekne Folyo Kaplama: Boya ile Karşılaştırma | Tekne Usta",
   "meta_desc": "Tekne folyo (vinil) kaplama nedir, boyaya göre avantajları ve sınırları? Renk değişimi, maliyet, dayanıklılık ve hangi durumda folyo, hangisinde boya?",
   "body": """
<p>Folyo (vinil) kaplama, son yıllarda otomotivden denizciliğe geçen, teknenin dış yüzeyini boyamadan renklendirme yöntemidir. Boyaya gerçek bir alternatif olabilir — ama her durumda değil.</p>
<h2>Folyo kaplama nedir?</h2>
<p>Deniz sınıfı döküm vinil bir film, teknenin yüzeyine profesyonelce uygulanır. Renk, desen ve mat/parlak seçenekleri geniştir; teknenin hattına ısıyla şekil verilerek oturtulur.</p>
<h2>Folyonun avantajları</h2>
<ul>
<li><strong>Geri dönülebilir:</strong> Sökülünce altındaki orijinal yüzey korunur — kiralık/satılık teknelerde avantaj.</li>
<li><strong>Hızlı renk değişimi:</strong> Boyamaya göre daha kısa sürede yeni bir görünüm.</li>
<li><strong>Tasarım esnekliği:</strong> Grafik ve özel desenler kolay.</li>
</ul>
<h2>Sınırları</h2>
<ul>
<li>Kalıcılık ve UV dayanımı iyi bir <a href="/blog/2k-poliuretan-boya/">2K boyaya</a> göre daha kısadır.</li>
<li>Yüzey hazırlığı yine kritiktir; kötü zeminde folyo kenarlardan kalkar.</li>
<li>Su altı (karina) için uygun değildir — orada <a href="/hizmetler/tekne-boyama-antifouling/">antifouling</a> gerekir.</li>
</ul>
<h2>Folyo mu, boya mı?</h2>
<p>Geçici/geri dönülebilir bir görünüm veya hızlı renk değişimi istiyorsanız folyo; kalıcı, en yüksek parlaklık ve uzun ömür istiyorsanız <a href="/blog/tekne-renk-degisimi/">boya</a> mantıklıdır. İkisini de teknenizin kullanımına göre değerlendiririz.</p>
<p>Renk değişimi ve dış cephe uygulamalarını <a href="/hizmetler/tekne-boyama-antifouling/">tekne boyama</a> hizmetimiz kapsamında planlıyoruz; folyo mu boya mı, birlikte karar veririz.</p>
""",
 },
 "en": {
   "category": "Painting",
   "title": "Boat Vinyl Wrap: Alternative to Paint, or Complement?",
   "excerpt": "What is boat vinyl wrap, and what are its pros and cons versus paint? The right choice for a colour change.",
   "meta_title": "Boat Vinyl Wrap: Compared with Paint | Tekne Usta",
   "meta_desc": "What is boat vinyl wrap, and its advantages and limits versus paint? Colour change, cost, durability and when to choose wrap over paint.",
   "body": """
<p>Vinyl wrap, which has moved from automotive to boating in recent years, is a way to recolour a boat's exterior without painting. It can be a real alternative to paint — but not in every case.</p>
<h2>What is a vinyl wrap?</h2>
<p>A marine-grade cast vinyl film is professionally applied to the boat's surface. Colour, pattern and matte/gloss options are wide; it's heat-formed to the boat's lines.</p>
<h2>Advantages of wrap</h2>
<ul>
<li><strong>Reversible:</strong> removed, the original surface underneath is preserved — an advantage for charter/resale boats.</li>
<li><strong>Fast colour change:</strong> a new look in less time than painting.</li>
<li><strong>Design flexibility:</strong> graphics and custom patterns are easy.</li>
</ul>
<h2>Limits</h2>
<ul>
<li>Durability and UV resistance are shorter than a good <a href="/en/blog/2k-polyurethane-paint/">2K paint</a>.</li>
<li>Surface prep is still critical; on a poor base the wrap lifts at the edges.</li>
<li>Not suitable below the waterline — that needs <a href="/en/services/boat-painting-antifouling/">antifouling</a>.</li>
</ul>
<h2>Wrap or paint?</h2>
<p>For a temporary/reversible look or a fast colour change, wrap; for permanence, the highest gloss and long life, <a href="/en/blog/boat-colour-change/">paint</a> makes sense. We weigh both against your boat's use.</p>
<p>We plan colour change and topside work under our <a href="/en/services/boat-painting-antifouling/">boat painting</a> service; wrap or paint, we decide together.</p>
""",
 },
},
{
 "slug": "robotik-karina-temizligi", "slug_en": "robotic-hull-cleaning",
 "image": "/assets/images/services/bakim.jpg", "date": "2028-07-19",
 "tr": {
   "category": "Bakım",
   "title": "Robotik Karina Temizliği: Yeni Teknoloji Neyi Değiştiriyor?",
   "excerpt": "Su altı robotik karina temizliği nedir, geleneksel yönteme göre avantajları ve sınırları neler?",
   "meta_title": "Robotik Karina Temizliği Nedir? | Tekne Usta",
   "meta_desc": "Robotik karina temizliği: su altı robotlarla tekne karinasının temizlenmesi, geleneksel çekme yöntemine göre avantajları, sınırları ve antifouling ile ilişkisi.",
   "body": """
<p>Son yıllarda gündeme gelen robotik (su altı) karina temizliği, tekneyi karaya çekmeden karinadaki yosun ve kabuğu temizleyen robot sistemlerini ifade eder. Peki bu teknoloji neyi değiştiriyor, neyi değiştirmiyor?</p>
<h2>Nasıl çalışır?</h2>
<p>Su altında hareket eden robot, karinaya tutunarak fırça/temizleme üniteleriyle yüzeydeki biyolojik birikimi (yosun, kekamoz başlangıcı) temizler — tekne suda kalırken.</p>
<h2>Avantajları</h2>
<ul>
<li><strong>Çekme gerektirmez:</strong> Sezon içinde, tekne suda kalırken sık temizlik mümkün.</li>
<li><strong>Sürekli performans:</strong> Karina temiz kalınca sürtünme ve yakıt tüketimi düşer.</li>
</ul>
<h2>Sınırları</h2>
<ul>
<li><strong>Antifouling'in yerini tutmaz:</strong> Robot temizlik, yüzeye yapışmayı önleyen <a href="/hizmetler/tekne-boyama-antifouling/">antifouling</a> katmanının yerine geçmez; agresif temizlik antifoulingi aşındırabilir.</li>
<li><strong>Yapısal işleri kapsamaz:</strong> Osmoz, boya, gelcoat ve <a href="/blog/su-alti-yapisal-onarim/">yapısal onarım</a> için tekne yine karaya çekilmelidir.</li>
<li><strong>Yaygınlık:</strong> Her bölgede/her tekede uygulanamayabilir.</li>
</ul>
<h2>Bizim yaklaşımımız</h2>
<p>Robotik temizlik, sezon içi bir <em>tamamlayıcıdır</em>; kapsamlı karina bakımı, antifouling yenileme ve onarım için <a href="/blog/tekne-cekek-karaya-cekme/">karaya çekme</a> temelli, detaylı bir hizmet sunuyoruz. Karinanızın kekamoz ve birikim durumu için <a href="/blog/kekamoz-temizligi/">bu yazıya</a> da bakın.</p>
<p>Kapsamlı karina temizliği ve bakımını <a href="/hizmetler/tekne-kislatma/">bakım</a> hizmetimiz kapsamında yapıyoruz.</p>
""",
 },
 "en": {
   "category": "Maintenance",
   "title": "Robotic Hull Cleaning: What Does the New Technology Change?",
   "excerpt": "What is underwater robotic hull cleaning, and what are its advantages and limits versus the traditional method?",
   "meta_title": "What Is Robotic Hull Cleaning? | Tekne Usta",
   "meta_desc": "Robotic hull cleaning: cleaning a boat's hull with underwater robots, its advantages over hauling out, its limits and its relationship with antifouling.",
   "body": """
<p>Robotic (underwater) hull cleaning, much discussed lately, refers to robot systems that clean weed and growth off the hull without hauling the boat out. So what does this technology change, and what doesn't it?</p>
<h2>How does it work?</h2>
<p>A robot moving underwater attaches to the hull and cleans biological build-up (weed, early scale) with brush/cleaning units — while the boat stays afloat.</p>
<h2>Advantages</h2>
<ul>
<li><strong>No haul-out:</strong> frequent in-season cleaning is possible while the boat stays in the water.</li>
<li><strong>Sustained performance:</strong> a clean hull lowers drag and fuel use.</li>
</ul>
<h2>Limits</h2>
<ul>
<li><strong>No substitute for antifouling:</strong> robot cleaning doesn't replace the <a href="/en/services/boat-painting-antifouling/">antifouling</a> layer that prevents adhesion; aggressive cleaning can erode the antifouling.</li>
<li><strong>Doesn't cover structural work:</strong> for osmosis, paint, gelcoat and <a href="/en/blog/underwater-structural-repair/">structural repair</a>, the boat must still be hauled out.</li>
<li><strong>Availability:</strong> may not be applicable in every region/for every boat.</li>
</ul>
<h2>Our approach</h2>
<p>Robotic cleaning is an in-season <em>complement</em>; for thorough hull maintenance, antifouling renewal and repair we offer a detailed <a href="/en/blog/boat-haul-out-guide/">haul-out</a>-based service. For your hull's scale and build-up, see also <a href="/en/blog/hull-limescale-cleaning/">this article</a>.</p>
<p>We do thorough hull cleaning and maintenance under our <a href="/en/services/winterising-storage/">maintenance</a> service.</p>
""",
 },
},
{
 "slug": "tekne-temizligi-detailing", "slug_en": "boat-cleaning-detailing",
 "image": "/assets/images/services/bakim.jpg", "date": "2028-08-02",
 "tr": {
   "category": "Bakım",
   "title": "Tekne Temizliği ve Detailing: Yüzeyi Korumanın İlk Adımı",
   "excerpt": "Düzenli tekne temizliği ve detailing neden önemli? İç-dış temizlik, pasta-polisaj ve koruyucu bakımın faydaları.",
   "meta_title": "Tekne Temizliği ve Detailing Rehberi | Tekne Usta",
   "meta_desc": "Tekne temizliği ve detailing: iç-dış temizlik, pasta polisaj, jelkot koruma ve düzenli bakımın faydaları. Yüzeyi ve değeri korumanın ilk adımı.",
   "body": """
<p>Temizlik ve detailing yalnızca estetik değildir; teknenin yüzeyini, değerini ve ömrünü koruyan ilk adımdır. Düzenli bakım, büyük ve pahalı onarımları geciktiren en ucuz sigortadır.</p>
<h2>Detailing neleri kapsar?</h2>
<ul>
<li><strong>Dış yüzey:</strong> Tuz, kir ve leke temizliği; <a href="/blog/gelcoat-cizik-sararma-giderme/">pasta-polisaj</a> ile parlaklığın geri kazanılması.</li>
<li><strong>Jelkot koruma:</strong> Temizlik sonrası koruyucu cila/wax ile UV ve oksidasyona karşı kalkan.</li>
<li><strong>İç mekan:</strong> Kabin, döşeme ve yüzeylerin temizliği; <a href="/blog/teknede-kuf-nem-onleme/">küf ve nem</a> kontrolü.</li>
<li><strong>Detay:</strong> Paslanmaz, cam ve fikstürlerin bakımı.</li>
</ul>
<h2>Neden düzenli olmalı?</h2>
<p>Tuz ve UV, ihmal edildiğinde jelkotu ve döşemeyi kalıcı olarak yıpratır. Düzenli detailing, <a href="/blog/gelcoat-yenileme/">komple gelcoat yenilemeyi</a> veya döşeme değişimini yıllarca erteler. Sezon başı ve sonu detailing, teknenin hem görünümünü hem değerini korur.</p>
<h2>Bakımın bir parçası</h2>
<p>Detailing'i tek başına değil, teknenin bütünsel bakım planının bir parçası olarak ele alıyoruz: yüzey koruma + <a href="/blog/yillik-tekne-bakim-takvimi/">yıllık bakım</a> + gerektiğinde onarım. Böylece tekneniz her sezon en iyi halinde olur.</p>
<p>Detailing, pasta-polisaj ve yüzey korumayı <a href="/hizmetler/fiberglas-onarim/">fiberglas</a> ve <a href="/hizmetler/ic-mekan-yenileme/">iç mekan</a> hizmetlerimizle birlikte planlıyoruz.</p>
""",
 },
 "en": {
   "category": "Maintenance",
   "title": "Boat Cleaning and Detailing: The First Step to Protecting the Surface",
   "excerpt": "Why do regular boat cleaning and detailing matter? The benefits of interior-exterior cleaning, compound-polish and protective care.",
   "meta_title": "Boat Cleaning and Detailing Guide | Tekne Usta",
   "meta_desc": "Boat cleaning and detailing: interior-exterior cleaning, compound-polish, gelcoat protection and the benefits of regular care. The first step to protecting the surface and value.",
   "body": """
<p>Cleaning and detailing aren't just cosmetic; they're the first step in protecting a boat's surface, value and life. Regular care is the cheapest insurance for delaying big, expensive repairs.</p>
<h2>What does detailing cover?</h2>
<ul>
<li><strong>Exterior:</strong> removing salt, dirt and stains; restoring gloss with <a href="/en/blog/gelcoat-scratch-yellowing/">compound-polish</a>.</li>
<li><strong>Gelcoat protection:</strong> a protective wax after cleaning shields against UV and oxidation.</li>
<li><strong>Interior:</strong> cleaning the cabin, upholstery and surfaces; <a href="/en/blog/preventing-mould-damp/">mould and damp</a> control.</li>
<li><strong>Detail:</strong> care of stainless, glass and fixtures.</li>
</ul>
<h2>Why should it be regular?</h2>
<p>Salt and UV, if neglected, permanently wear the gelcoat and upholstery. Regular detailing postpones a full <a href="/en/blog/gelcoat-renewal/">gelcoat renewal</a> or re-upholstery for years. Start- and end-of-season detailing protects both the look and the value of the boat.</p>
<h2>Part of maintenance</h2>
<p>We treat detailing not on its own but as part of the boat's holistic care plan: surface protection + <a href="/en/blog/annual-boat-maintenance-calendar/">annual maintenance</a> + repair when needed. So your boat is at its best every season.</p>
<p>We plan detailing, compound-polish and surface protection alongside our <a href="/en/services/fibreglass-repair/">fibreglass</a> and <a href="/en/services/interior-refit/">interior</a> services.</p>
""",
 },
},
{
 "slug": "refit-proje-yonetimi", "slug_en": "refit-project-management",
 "image": "/assets/images/hakkimizda.jpg", "date": "2028-08-16",
 "tr": {
   "category": "Rehber",
   "title": "Refit Proje Yönetimi: Kapsamlı Yenilemeyi Tek Elden Yürütmek",
   "excerpt": "Çok kalemli bir refit (kapsamlı yenileme) neden proje yönetimi ister? Bütçe, takvim ve koordinasyonu tek elden yönetmenin faydası.",
   "meta_title": "Refit Proje Yönetimi: Kapsamlı Tekne Yenileme | Tekne Usta",
   "meta_desc": "Refit proje yönetimi: fiberglas, boya, ahşap, teak ve iç mekanı kapsayan çok kalemli yenilemenin bütçe, takvim ve koordinasyonunu tek elden yürütmek.",
   "body": """
<p>Bir teknenin kapsamlı yenilemesi (refit) çoğu zaman tek bir iş değildir: fiberglas onarımı, boya, ahşap, teak, iç mekan ve detay işleri iç içe geçer. Bu kalemleri ayrı ayrı takip etmek hem zaman hem para kaybettirir. İşte burada <strong>proje yönetimi</strong> devreye girer.</p>
<h2>Neden tek elden yönetim?</h2>
<ul>
<li><strong>Tek muhatap:</strong> Her kalem için ayrı kişiyle uğraşmazsınız; süreci sizin adınıza biz koordine ederiz.</li>
<li><strong>Doğru sıralama:</strong> İşler yanlış sırada yapılırsa biri diğerini bozar (ör. boyadan sonra güverte işi). Doğru sıra, yeniden yapımı önler.</li>
<li><strong>Bütçe kontrolü:</strong> Kalem kalem, şeffaf bir plan; sürpriz maliyet yok.</li>
<li><strong>Takvim:</strong> Sezon planınıza uygun, gerçekçi bir teslim.</li>
</ul>
<h2>Süreç</h2>
<p>Önce kapsamlı bir <a href="/blog/satin-alma-oncesi-tekne-ekspertizi/">durum değerlendirmesi</a> yapılır ve işler önceliklendirilir. Ardından aşamalı bir plan ve kalem kalem teklif sunulur. Uygulama sırasında sizi adım adım bilgilendiririz — proje boyunca ne olduğunu her zaman bilirsiniz.</p>
<h2>Kime uygun?</h2>
<p>Birden fazla işi (ör. <a href="/hizmetler/fiberglas-onarim/">fiberglas</a> + <a href="/hizmetler/tekne-boyama-antifouling/">boya</a> + <a href="/hizmetler/teak-guverte-doseme/">teak</a>) aynı dönemde yaptıracaksanız, ya da klasik bir tekneyi baştan yeniliyorsanız, tek elden proje yönetimi zaman, para ve stres kazandırır.</p>
<p>Kapsamlı refit'inizi tek elden planlamak için <a href="/hizmetler/ahsap-tekne-renovasyonu/">renovasyon</a> ve <a href="/hizmetler/fiberglas-onarim/">onarım</a> ekibimizle ücretsiz keşifte başlayalım.</p>
""",
 },
 "en": {
   "category": "Guide",
   "title": "Refit Project Management: Running a Full Refit from One Hand",
   "excerpt": "Why does a multi-item refit need project management? The benefit of managing budget, schedule and coordination from a single point.",
   "meta_title": "Refit Project Management: Full Boat Refit | Tekne Usta",
   "meta_desc": "Refit project management: running the budget, schedule and coordination of a multi-item refit covering fibreglass, paint, wood, teak and interior from one hand.",
   "body": """
<p>A full boat refit is often not a single job: fibreglass repair, paint, wood, teak, interior and detail work interweave. Tracking these separately costs both time and money. This is where <strong>project management</strong> comes in.</p>
<h2>Why manage from one hand?</h2>
<ul>
<li><strong>One point of contact:</strong> you don't deal with a separate person for each item; we coordinate the process for you.</li>
<li><strong>The right order:</strong> done in the wrong order, one job spoils another (e.g. deck work after paint). The right sequence prevents rework.</li>
<li><strong>Budget control:</strong> an itemised, transparent plan; no surprise costs.</li>
<li><strong>Schedule:</strong> a realistic delivery that fits your season plan.</li>
</ul>
<h2>The process</h2>
<p>First a thorough <a href="/en/blog/pre-purchase-boat-survey/">condition assessment</a> is made and the work prioritised. Then a staged plan and an itemised quote are presented. During the work we keep you informed step by step — you always know what's happening.</p>
<h2>Who is it for?</h2>
<p>If you're having several jobs done in the same period (e.g. <a href="/en/services/fibreglass-repair/">fibreglass</a> + <a href="/en/services/boat-painting-antifouling/">paint</a> + <a href="/en/services/teak-deck/">teak</a>), or renewing a classic boat from the ground up, single-hand project management saves time, money and stress.</p>
<p>To plan your full refit from one hand, let's start with a free survey with our <a href="/en/services/wooden-boat-refit/">refit</a> and <a href="/en/services/fibreglass-repair/">repair</a> team.</p>
""",
 },
},
{
 "slug": "yillik-bakim-anlasmasi", "slug_en": "annual-maintenance-agreement",
 "image": "/assets/images/services/bakim.jpg", "date": "2028-08-30",
 "tr": {
   "category": "Bakım",
   "title": "Yıllık Tekne Bakım Anlaşması: Düzenli Bakımın Avantajı",
   "excerpt": "Yıllık bakım anlaşması nedir, neden mantıklı? Öngörülebilir bütçe, öncelikli randevu ve teknenin her zaman hazır olması.",
   "meta_title": "Yıllık Tekne Bakım Anlaşması / Paketi | Tekne Usta",
   "meta_desc": "Yıllık tekne bakım anlaşması: düzenli bakım paketiyle öngörülebilir bütçe, öncelikli randevu, sezon öncesi/sonrası bakım ve teknenin her zaman hazır olması.",
   "body": """
<p>Çoğu tekne sahibi bakımı ihtiyaç doğduğunda, dağınık biçimde yaptırır. Oysa <strong>yıllık bir bakım anlaşması</strong>, hem tekneyi hem bütçeyi çok daha iyi yönetmenizi sağlar.</p>
<h2>Neden mantıklı?</h2>
<ul>
<li><strong>Öngörülebilir bütçe:</strong> Yıllık bakım kalemleri baştan planlanır; sürpriz büyük masraflar azalır.</li>
<li><strong>Öncelikli randevu:</strong> Sezon yoğunluğunda (çekek alanları dolarken) önce sizin işiniz planlanır.</li>
<li><strong>Düzenlilik = daha az onarım:</strong> Küçük sorunlar büyümeden çözülür; <a href="/blog/tekne-sahipligi-maliyeti/">toplam sahiplik maliyeti</a> düşer.</li>
<li><strong>Tekne her zaman hazır:</strong> Suya inişte sürprizle uğraşmazsınız.</li>
</ul>
<h2>Neleri kapsayabilir?</h2>
<p>Sezon öncesi ve sonrası <a href="/blog/bahar-tekne-bakimi/">bakım</a>, <a href="/hizmetler/tekne-kislatma/">kışlatma</a>, <a href="/hizmetler/tekne-detailing/">detailing</a>, karina/antifouling kontrolü ve düzenli yüzey bakımı bir pakette birleştirilebilir. Kapsam teknenize ve kullanımınıza göre belirlenir.</p>
<h2>Kime uygun?</h2>
<p>Teknesini düzenli kullanan ve bakım derdiyle uğraşmak istemeyen sahipler için idealdir. Bir kez planlarsınız, gerisini biz takip ederiz.</p>
<p>Size uygun bir yıllık bakım planı için <a href="/hizmetler/tekne-kislatma/">bakım</a> hizmetimiz kapsamında ücretsiz görüşelim.</p>
""",
 },
 "en": {
   "category": "Maintenance",
   "title": "Annual Boat Maintenance Agreement: The Advantage of Regular Care",
   "excerpt": "What is an annual maintenance agreement and why does it make sense? Predictable budget, priority booking and a boat that's always ready.",
   "meta_title": "Annual Boat Maintenance Agreement / Plan | Tekne Usta",
   "meta_desc": "Annual boat maintenance agreement: a regular care plan for a predictable budget, priority booking, pre/post-season care and a boat that's always ready.",
   "body": """
<p>Most boat owners have maintenance done reactively, in a scattered way. Yet an <strong>annual maintenance agreement</strong> lets you manage both the boat and the budget far better.</p>
<h2>Why does it make sense?</h2>
<ul>
<li><strong>Predictable budget:</strong> annual items are planned in advance; surprise big costs drop.</li>
<li><strong>Priority booking:</strong> in peak season (as hardstanding fills), your work is scheduled first.</li>
<li><strong>Regularity = less repair:</strong> small problems are solved before they grow; <a href="/en/blog/cost-of-boat-ownership/">total cost of ownership</a> falls.</li>
<li><strong>Always ready:</strong> no surprises at launch.</li>
</ul>
<h2>What can it cover?</h2>
<p>Pre- and post-season <a href="/en/blog/spring-boat-maintenance/">care</a>, <a href="/en/services/winterising-storage/">winterising</a>, <a href="/en/services/boat-detailing/">detailing</a>, hull/antifouling checks and regular surface care can be combined in one plan. Scope is set to your boat and use.</p>
<h2>Who is it for?</h2>
<p>Ideal for owners who use their boat regularly and don't want to deal with maintenance. You plan once, we track the rest.</p>
<p>For a yearly plan that suits you, let's talk at no cost under our <a href="/en/services/winterising-storage/">maintenance</a> service.</p>
""",
 },
},
{
 "slug": "epoksi-macun-nedir", "slug_en": "epoxy-filler-putty",
 "image": "/assets/images/services/fiberglas.jpg", "date": "2028-09-13",
 "tr": {
   "category": "Fiberglas",
   "title": "Epoksi Macun Nedir ve Nasıl Uygulanır?",
   "excerpt": "Epoksi macun ne işe yarar, hangi hasarlarda kullanılır ve doğru uygulama nasıl olur? Çatlak ve boşluk onarımının temeli.",
   "meta_title": "Epoksi Macun Nedir ve Nasıl Uygulanır? | Tekne Usta",
   "meta_desc": "Epoksi macun nedir, nasıl uygulanır? İki bileşenli epoksi macunun çatlak, boşluk ve yüzey onarımında kullanımı; ahşap, fiberglas ve metalde uygulama ipuçları.",
   "body": """
<p>Epoksi macun (dolgu), tekne onarımının en çok kullanılan malzemelerinden biridir. İki bileşenli (reçine + sertleştirici) bu sistem, karıştırıldığında sertleşerek çatlak, boşluk ve düzensizlikleri yapısal olarak doldurur.</p>
<h2>Ne işe yarar?</h2>
<ul>
<li><strong>Çatlak ve boşluk doldurma:</strong> Fiberglas, ahşap ve metalde hasarlı bölgeleri kapatır.</li>
<li><strong>Yüzey düzeltme (fairing):</strong> Boya öncesi pürüzsüz zemin oluşturur (bkz. <a href="/blog/boya-oncesi-yuzey-hazirligi/">yüzey hazırlığı</a>).</li>
<li><strong>Su geçirmezlik:</strong> Kürlendiğinde suya dayanıklı, sağlam bir dolgu sağlar.</li>
</ul>
<h2>Doğru uygulama</h2>
<p>Yüzey temiz, kuru ve yağdan arınmış olmalı. Reçine ve sertleştirici <strong>doğru oranda</strong> karıştırılır; yanlış oran kürlenmeyi bozar. Kürlenme sonrası zımparalanır. İnce katlar, kalın tek kata göre daha az kabarcık ve daha iyi sonuç verir.</p>
<h2>Polyester macun mu, epoksi macun mu?</h2>
<p>Epoksi macun, polyestere göre daha güçlü yapışır ve su geçirmezliği yüksektir; su altı ve yapısal işlerde tercih edilir. Farklar için <a href="/blog/polyester-vs-epoksi-recine/">polyester vs epoksi</a> yazımıza bakın.</p>
<p>Yapısal onarım ve fairing işlerini <a href="/hizmetler/fiberglas-onarim/">fiberglas onarım</a> hizmetimiz kapsamında, doğru malzeme ve teknikle yapıyoruz.</p>
""",
 },
 "en": {
   "category": "Fibreglass",
   "title": "What Is Epoxy Filler and How Is It Applied?",
   "excerpt": "What is epoxy filler used for, on which damage, and how is it applied correctly? The basis of crack and void repair.",
   "meta_title": "What Is Epoxy Filler and How to Apply It? | Tekne Usta",
   "meta_desc": "What is epoxy filler and how is it applied? Using two-part epoxy filler for cracks, voids and surface repair on wood, fibreglass and metal, with application tips.",
   "body": """
<p>Epoxy filler is one of the most used materials in boat repair. This two-part system (resin + hardener) cures when mixed, structurally filling cracks, voids and unevenness.</p>
<h2>What is it for?</h2>
<ul>
<li><strong>Filling cracks and voids:</strong> closes damaged areas in fibreglass, wood and metal.</li>
<li><strong>Fairing:</strong> creates a smooth base before painting (see <a href="/en/blog/surface-prep-before-painting/">surface prep</a>).</li>
<li><strong>Waterproofing:</strong> once cured, gives a durable, water-resistant fill.</li>
</ul>
<h2>Correct application</h2>
<p>The surface must be clean, dry and grease-free. Resin and hardener are mixed in the <strong>right ratio</strong>; a wrong ratio ruins the cure. After curing it's sanded. Thin layers give fewer bubbles and better results than one thick layer.</p>
<h2>Polyester filler or epoxy filler?</h2>
<p>Epoxy filler bonds more strongly than polyester and is more waterproof; it's preferred for underwater and structural work. For the differences, see our <a href="/en/blog/polyester-vs-epoxy-resin/">polyester vs epoxy</a> article.</p>
<p>We do structural repair and fairing under our <a href="/en/services/fibreglass-repair/">fibreglass repair</a> service with the right material and technique.</p>
""",
 },
},
{
 "slug": "epoksi-uygulama-hatalari", "slug_en": "epoxy-application-mistakes",
 "image": "/assets/images/services/fiberglas.jpg", "date": "2028-09-27",
 "tr": {
   "category": "Fiberglas",
   "title": "Epoksi Uygulamasında En Sık Yapılan 6 Hata",
   "excerpt": "Yanlış karışım oranından sıcaklığa; epokside yapışma, kabarcık ve kürlenme sorunlarına yol açan önlenebilir hatalar.",
   "meta_title": "Epoksi Uygulama Hataları: Kaçınılması Gerekenler | Tekne Usta",
   "meta_desc": "Epoksi uygulamasında sık yapılan hatalar: yanlış karışım oranı, kötü yüzey hazırlığı, sıcaklık/nem, kalın kat ve amine blush. Sağlam bir epoksi uygulaması için ipuçları.",
   "body": """
<p>Epoksi güçlü bir malzemedir ama küçük uygulama hataları bile yapışma sorunu, kabarcık, matlaşma veya eksik kürlenmeye yol açar. İşte en sık ve tamamen önlenebilir hatalar.</p>
<h2>1. Yanlış karışım oranı</h2>
<p>Reçine/sertleştirici oranı yanlışsa epoksi doğru kürlenmez — yapışkan kalır veya kırılgan olur. Üreticinin oranına harfiyen uyulmalı.</p>
<h2>2. Kötü yüzey hazırlığı</h2>
<p>Kirli, yağlı veya parlak yüzeye epoksi tutmaz. Zımpara ve temizlik şarttır.</p>
<h2>3. Yanlış sıcaklık/nem</h2>
<p>Çok soğukta kürlenme durur, çok sıcakta hızlanıp sorun çıkar. Nemli havada yüzeyde "amine blush" (yağlı film) oluşabilir.</p>
<h2>4. Kalın tek kat</h2>
<p>Kalın uygulama ısı üretir, kabarcık ve çatlak yapar. İnce katlar daha güvenlidir.</p>
<h2>5. Amine blush'ı yıkamamak</h2>
<p>Katlar arası oluşan yağlı filmi yıkamadan üzerine uygulama yapmak yapışmayı bozar.</p>
<h2>6. Yetersiz kürlenme süresi</h2>
<p>Tam kürlenmeden zımpara veya boya, sonucu bozar. Sabır gerekir.</p>
<p>Epoksi işlerini doğru koşul ve teknikle <a href="/hizmetler/fiberglas-onarim/">fiberglas onarım</a> hizmetimiz kapsamında yapıyoruz. Malzeme için <a href="/blog/epoksi-macun-nedir/">epoksi macun</a> yazımıza bakın.</p>
""",
 },
 "en": {
   "category": "Fibreglass",
   "title": "The 6 Most Common Epoxy Application Mistakes",
   "excerpt": "From wrong mix ratio to temperature; the preventable mistakes that cause adhesion, bubble and curing problems with epoxy.",
   "meta_title": "Epoxy Application Mistakes to Avoid | Tekne Usta",
   "meta_desc": "Common epoxy application mistakes: wrong mix ratio, poor surface prep, temperature/humidity, thick coats and amine blush. Tips for a sound epoxy application.",
   "body": """
<p>Epoxy is a strong material, but even small application mistakes cause adhesion problems, bubbles, dullness or incomplete curing. Here are the most common — and entirely preventable — mistakes.</p>
<h2>1. Wrong mix ratio</h2>
<p>If the resin/hardener ratio is off, epoxy won't cure right — it stays tacky or turns brittle. Follow the maker's ratio exactly.</p>
<h2>2. Poor surface prep</h2>
<p>Epoxy won't hold on a dirty, greasy or glossy surface. Sanding and cleaning are essential.</p>
<h2>3. Wrong temperature/humidity</h2>
<p>Curing stalls when too cold and speeds up problematically when too hot. In damp air an "amine blush" (greasy film) can form.</p>
<h2>4. One thick coat</h2>
<p>A thick application generates heat, causing bubbles and cracks. Thin coats are safer.</p>
<h2>5. Not washing off amine blush</h2>
<p>Applying over the greasy film between coats without washing ruins adhesion.</p>
<h2>6. Insufficient cure time</h2>
<p>Sanding or painting before full cure spoils the result. Patience is needed.</p>
<p>We do epoxy work under the right conditions and technique in our <a href="/en/services/fibreglass-repair/">fibreglass repair</a> service. For materials, see our <a href="/en/blog/epoxy-filler-putty/">epoxy filler</a> article.</p>
""",
 },
},
{
 "slug": "uv-koruma-kaplama", "slug_en": "uv-protection-coating",
 "image": "/assets/images/services/boya.jpg", "date": "2028-10-11",
 "tr": {
   "category": "Boya",
   "title": "UV Işınları ve Tekne Yüzeyi Koruması",
   "excerpt": "Güneşin UV ışınları tekneyi nasıl yıpratır ve UV koruma kaplamaları neyi değiştirir? Rengi ve parlaklığı korumanın yolu.",
   "meta_title": "UV Koruma: Tekne Yüzeyini Güneşten Korumak | Tekne Usta",
   "meta_desc": "UV ışınları ve tekne yüzeyi koruması: güneşin jelkot, boya ve ahşaba etkisi, UV koruyucu kaplama ve wax ile rengin solmasını, çatlamayı önleme.",
   "body": """
<p>Deniz ortamında teknenin en büyük düşmanlarından biri güneştir. UV ışınları zamanla jelkotu soldurur, boyayı matlaştırır, ahşabı grileştirir ve yüzeyde çatlaklara yol açar. UV koruma, bu süreci ciddi biçimde yavaşlatır.</p>
<h2>UV teknede neyi yıpratır?</h2>
<ul>
<li><strong>Jelkot/boya:</strong> Renk solar, parlaklık gider, mikro çatlaklar oluşur.</li>
<li><strong>Ahşap/vernik:</strong> Vernik çatlar, ahşap grileşir (bkz. <a href="/blog/ahsap-tekne-vernik-bakimi/">vernik bakımı</a>).</li>
<li><strong>Döşeme:</strong> Kumaşlar solar; deniz sınıfı UV dirençli kumaş önemlidir.</li>
</ul>
<h2>Koruma yolları</h2>
<ul>
<li><strong>Koruyucu wax/cila:</strong> Jelkot üzerine düzenli uygulanan koruma UV'yi yansıtır ve oksidasyonu geciktirir.</li>
<li><strong>UV dayanımlı boya sistemleri:</strong> Kaliteli <a href="/blog/2k-poliuretan-boya/">2K boyalar</a> UV emici katkılar içerir.</li>
<li><strong>Örtü:</strong> Kullanılmadığında iyi bir <a href="/blog/tekne-ortusu-secimi/">örtü</a> en basit korumadır.</li>
</ul>
<h2>Düzenlilik esas</h2>
<p>UV koruma tek seferlik değil, düzenli bir bakım işidir. <a href="/hizmetler/tekne-detailing/">Detailing</a> paketlerimizde temizlik sonrası koruyucu uygulamayı da yapıyoruz — böylece rengi ve parlaklığı yıllarca korursunuz.</p>
""",
 },
 "en": {
   "category": "Painting",
   "title": "UV Rays and Protecting Your Boat's Surface",
   "excerpt": "How do the sun's UV rays wear a boat, and what do UV protection coatings change? The way to keep colour and gloss.",
   "meta_title": "UV Protection: Shielding a Boat Surface from the Sun | Tekne Usta",
   "meta_desc": "UV rays and boat surface protection: the sun's effect on gelcoat, paint and wood, and preventing fading and cracking with UV protective coatings and wax.",
   "body": """
<p>In the marine environment, one of a boat's biggest enemies is the sun. UV rays fade the gelcoat, dull the paint, grey the wood and cause surface cracks over time. UV protection significantly slows this process.</p>
<h2>What does UV wear on a boat?</h2>
<ul>
<li><strong>Gelcoat/paint:</strong> colour fades, gloss goes, micro-cracks form.</li>
<li><strong>Wood/varnish:</strong> varnish cracks, wood greys (see <a href="/en/blog/wooden-boat-varnish-care/">varnish care</a>).</li>
<li><strong>Upholstery:</strong> fabrics fade; UV-resistant marine fabric matters.</li>
</ul>
<h2>Ways to protect</h2>
<ul>
<li><strong>Protective wax:</strong> a protection regularly applied over the gelcoat reflects UV and delays oxidation.</li>
<li><strong>UV-resistant paint systems:</strong> quality <a href="/en/blog/2k-polyurethane-paint/">2K paints</a> contain UV absorbers.</li>
<li><strong>Cover:</strong> when not in use, a good <a href="/en/blog/boat-cover-selection/">cover</a> is the simplest protection.</li>
</ul>
<h2>Regularity is key</h2>
<p>UV protection isn't a one-off but regular care. Our <a href="/en/services/boat-detailing/">detailing</a> packages include protective application after cleaning — so you keep colour and gloss for years.</p>
""",
 },
},
{
 "slug": "astar-primer-nedir", "slug_en": "primer-importance",
 "image": "/assets/images/services/boya.jpg", "date": "2028-10-25",
 "tr": {
   "category": "Boya",
   "title": "Astar (Primer) Nedir ve Neden Önemli?",
   "excerpt": "Astar boyanın altında görünmez ama sonucu belirler. Astar ne işe yarar, hangi tür ne zaman kullanılır?",
   "meta_title": "Astar (Primer) Nedir, Neden Önemli? | Tekne Usta",
   "meta_desc": "Astar (primer) nedir, neden önemli? Boya öncesi astarın yapışma, örtücülük ve korozyon koruması sağlaması; antifouling ve dış cephe için doğru astar seçimi.",
   "body": """
<p>Astar (primer), boyanın altına uygulanan ve gözle görünmeyen ama sonucu belirleyen kattır. İyi bir boya işinin sırrı çoğu zaman doğru astardadır.</p>
<h2>Astar ne işe yarar?</h2>
<ul>
<li><strong>Yapışma:</strong> Boyanın yüzeye sağlam tutunmasını sağlar.</li>
<li><strong>Örtücülük:</strong> Alttaki rengi ve düzensizlikleri kapatır — özellikle <a href="/blog/tekne-renk-degisimi/">renk değişiminde</a> kritik.</li>
<li><strong>Korozyon koruması:</strong> Metal yüzeylerde (özellikle <a href="/blog/aluminyum-tekne-boyama/">alüminyum</a>) metali korur.</li>
<li><strong>Bariyer:</strong> Osmoz sonrası epoksi bariyer, suyu içeri almaz.</li>
</ul>
<h2>Doğru astar seçimi</h2>
<p>Astar; yüzeye (fiberglas, ahşap, metal), boya tipine ve amaca göre seçilir. Antifouling öncesi astar ile dış cephe astarı farklıdır. Yanlış astar, boyanın kısa sürede kalkmasına yol açar.</p>
<h2>Astar atlanırsa ne olur?</h2>
<p>Astarsız veya yanlış astarla yapılan boya; kabarır, dökülür ve baştan yapılması gerekir. Bu yüzden astar, <a href="/blog/boya-oncesi-yuzey-hazirligi/">yüzey hazırlığının</a> ayrılmaz bir parçasıdır.</p>
<p>Doğru astar ve boya sistemini <a href="/hizmetler/tekne-boyama-antifouling/">tekne boyama</a> hizmetimiz kapsamında belirliyoruz.</p>
""",
 },
 "en": {
   "category": "Painting",
   "title": "What Is Primer and Why Does It Matter?",
   "excerpt": "Primer is invisible under the paint but decides the result. What does primer do, and which type when?",
   "meta_title": "What Is Primer and Why Does It Matter? | Tekne Usta",
   "meta_desc": "What is primer and why does it matter? How primer provides adhesion, coverage and corrosion protection before paint; choosing the right primer for antifouling and topside.",
   "body": """
<p>Primer is the coat applied under the paint — invisible, but it decides the result. The secret to a good paint job is often the right primer.</p>
<h2>What does primer do?</h2>
<ul>
<li><strong>Adhesion:</strong> makes the paint grip the surface firmly.</li>
<li><strong>Coverage:</strong> hides the underlying colour and unevenness — critical especially in a <a href="/en/blog/boat-colour-change/">colour change</a>.</li>
<li><strong>Corrosion protection:</strong> protects the metal on metal surfaces (especially <a href="/en/blog/aluminium-boat-painting/">aluminium</a>).</li>
<li><strong>Barrier:</strong> after osmosis, the epoxy barrier keeps water out.</li>
</ul>
<h2>Choosing the right primer</h2>
<p>Primer is chosen by surface (fibreglass, wood, metal), paint type and purpose. A primer before antifouling differs from a topside primer. The wrong primer makes the paint lift quickly.</p>
<h2>What if primer is skipped?</h2>
<p>Paint done without primer or with the wrong one blisters, flakes and must be redone. So primer is an inseparable part of <a href="/en/blog/surface-prep-before-painting/">surface prep</a>.</p>
<p>We determine the right primer and paint system in our <a href="/en/services/boat-painting-antifouling/">boat painting</a> service.</p>
""",
 },
},
{
 "slug": "tente-branda-bimini", "slug_en": "marine-canvas-covers",
 "image": "/assets/images/services/bakim.jpg", "date": "2028-11-08",
 "tr": {
   "category": "İç Mekan",
   "title": "Tekne Tente, Branda ve Bimini: Güneş, Yağmur ve Konfor",
   "excerpt": "Bimini, tente ve branda seçimi: güneş-yağmur koruması, malzeme, dikiş kalitesi ve teknenize özel ölçü.",
   "meta_title": "Tekne Tente, Branda ve Bimini Rehberi | Tekne Usta",
   "meta_desc": "Tekne tente, branda ve bimini: güneş ve yağmur koruması, deniz sınıfı kumaş, UV dayanımlı dikiş, kaplama brandası ve teknenize özel ölçü. Marine tekstil rehberi.",
   "body": """
<p>Tente, branda ve bimini; teknede hem konforu hem korumayı belirleyen dış mekan tekstilleridir. İyi seçilmiş bir sistem güneşi, yağmuru ve UV'yi keser; teknenizi ve sizi korur.</p>
<h2>Başlıca tipler</h2>
<ul>
<li><strong>Bimini:</strong> Kokpit üzerinde güneşlik; seyir konforunun temeli.</li>
<li><strong>Sprayhood / kaplama tentesi:</strong> Yağmur ve serpintiye karşı koruma.</li>
<li><strong>Kışlama/koruma brandası:</strong> Tekne beklerken UV ve nemden koruma (bkz. <a href="/blog/tekne-ortusu-secimi/">örtü seçimi</a>).</li>
</ul>
<h2>Malzeme ve dikiş</h2>
<p>Deniz koşullarına uygun, UV'ye dayanıklı ve su itici kumaş; UV dayanımlı iplik ve paslanmaz fikstürler şarttır. En iyi kumaş bile zayıf dikişle kısa ömürlü olur — dikiş kalitesi belirleyicidir.</p>
<h2>Ölçüye özel</h2>
<p>Tente ve brandalar teknenin hattına özel ölçülmeli; hazır ölçü nadiren tam oturur. Doğru gerginlik hem görünümü hem su akışını (birikme yapmaması) belirler.</p>
<p>Marine tekstil ve döşeme işlerini <a href="/hizmetler/ic-mekan-yenileme/">iç mekan yenileme</a> hizmetimiz kapsamında, döşeme yenileme ile birlikte planlıyoruz.</p>
""",
 },
 "en": {
   "category": "Interior",
   "title": "Boat Biminis, Covers and Canvas: Sun, Rain and Comfort",
   "excerpt": "Choosing biminis, sprayhoods and covers: sun-rain protection, material, stitch quality and a made-to-measure fit.",
   "meta_title": "Boat Bimini, Cover and Canvas Guide | Tekne Usta",
   "meta_desc": "Boat biminis, covers and canvas: sun and rain protection, marine-grade fabric, UV-resistant stitching, storage covers and a made-to-measure fit. Marine canvas guide.",
   "body": """
<p>Biminis, sprayhoods and covers are the exterior textiles that shape both comfort and protection aboard. A well-chosen system blocks sun, rain and UV; it protects your boat and you.</p>
<h2>Main types</h2>
<ul>
<li><strong>Bimini:</strong> a sunshade over the cockpit; the basis of cruising comfort.</li>
<li><strong>Sprayhood:</strong> protection against rain and spray.</li>
<li><strong>Storage cover:</strong> protection from UV and damp while the boat waits (see <a href="/en/blog/boat-cover-selection/">cover selection</a>).</li>
</ul>
<h2>Material and stitching</h2>
<p>Fabric suited to marine conditions — UV-resistant and water-repellent — plus UV-resistant thread and stainless fixtures are essential. Even the best fabric is short-lived with weak stitching — stitch quality is decisive.</p>
<h2>Made to measure</h2>
<p>Biminis and covers should be measured to the boat's lines; off-the-shelf sizes rarely fit exactly. Correct tension determines both the look and water run-off (no pooling).</p>
<p>We plan marine canvas and upholstery work under our <a href="/en/services/interior-refit/">interior refit</a> service, alongside upholstery renewal.</p>
""",
 },
},
{
 "slug": "kaydirmaz-guverte-kaplama", "slug_en": "non-slip-deck-coating",
 "image": "/assets/images/services/ic-mekan.jpg", "date": "2028-11-22",
 "tr": {
   "category": "Teak",
   "title": "Kaydırmaz Güverte Kaplaması: Güvenlik ve Konfor",
   "excerpt": "Fiberglas güvertede kaymayı önleyen kaplama seçenekleri nelerdir? Islakken güvenli bir yürüyüş yüzeyi için çözümler.",
   "meta_title": "Kaydırmaz Güverte Kaplaması Rehberi | Tekne Usta",
   "meta_desc": "Kaydırmaz güverte kaplaması: fiberglas güvertede kaymayı önleyen katkılı boya, doku desenleri ve EVA/sentetik seçenekler. Islakken güvenli güverte için çözümler.",
   "body": """
<p>Güverte, teknenin en çok yürünen ve ıslanan yüzeyidir. Zamanla kaydırmaz dokusu aşınan bir güverte güvenlik riski oluşturur. Kaydırmaz kaplama, hem güvenliği hem konforu geri kazandırır.</p>
<h2>Seçenekler</h2>
<ul>
<li><strong>Katkılı kaydırmaz boya:</strong> Boyaya eklenen özel katkılarla dokulu, tutuşlu bir yüzey; ekonomik ve yenilenebilir.</li>
<li><strong>Kalıp/desen dokusu:</strong> Uygulama sırasında oluşturulan kaydırmaz desen.</li>
<li><strong>EVA / sentetik kaplama:</strong> Yapıştırılan yumuşak, kaymaz paneller (bkz. <a href="/blog/sentetik-teak-alternatifleri/">sentetik teak alternatifleri</a>).</li>
</ul>
<h2>Hangi durumda ne?</h2>
<p>Mevcut kaydırmaz dokusu aşınmış fiberglas güvertede katkılı boya pratik ve ekonomiktir. Daha konforlu ve sıcak bir his isteyen, özellikle çocuklu tekneler için EVA panel mantıklıdır. Doğal görünüm önceliğinizse <a href="/hizmetler/teak-guverte-doseme/">teak</a> alternatiftir.</p>
<h2>Hazırlık önemli</h2>
<p>Kaplamanın tutması için yüzey doğru hazırlanmalı (bkz. <a href="/blog/boya-oncesi-yuzey-hazirligi/">yüzey hazırlığı</a>); aksi halde kaplama kenarlardan kalkar.</p>
<p>Kaydırmaz güverte çözümlerini <a href="/hizmetler/teak-guverte-doseme/">güverte</a> ve <a href="/hizmetler/tekne-boyama-antifouling/">boya</a> hizmetlerimiz kapsamında uyguluyoruz.</p>
""",
 },
 "en": {
   "category": "Teak",
   "title": "Non-Slip Deck Coating: Safety and Comfort",
   "excerpt": "What are the coating options that prevent slipping on a fibreglass deck? Solutions for a safe walking surface when wet.",
   "meta_title": "Non-Slip Deck Coating Guide | Tekne Usta",
   "meta_desc": "Non-slip deck coating: additive non-slip paint, textured patterns and EVA/synthetic options that prevent slipping on a fibreglass deck. Solutions for a safe deck when wet.",
   "body": """
<p>The deck is a boat's most walked-on and wettest surface. A deck whose non-slip texture has worn creates a safety risk. Non-slip coating restores both safety and comfort.</p>
<h2>Options</h2>
<ul>
<li><strong>Additive non-slip paint:</strong> special additives in the paint give a textured, grippy surface; economical and renewable.</li>
<li><strong>Moulded/pattern texture:</strong> a non-slip pattern formed during application.</li>
<li><strong>EVA / synthetic coating:</strong> bonded soft, non-slip panels (see <a href="/en/blog/synthetic-teak-alternatives/">synthetic teak alternatives</a>).</li>
</ul>
<h2>Which when?</h2>
<p>On a fibreglass deck with worn non-slip texture, additive paint is practical and economical. For a more comfortable, warmer feel, especially on boats with children, EVA panels make sense. If a natural look is your priority, <a href="/en/services/teak-deck/">teak</a> is the alternative.</p>
<h2>Prep matters</h2>
<p>The surface must be prepped correctly for the coating to hold (see <a href="/en/blog/surface-prep-before-painting/">surface prep</a>); otherwise the coating lifts at the edges.</p>
<p>We apply non-slip deck solutions under our <a href="/en/services/teak-deck/">deck</a> and <a href="/en/services/boat-painting-antifouling/">painting</a> services.</p>
""",
 },
},
{
 "slug": "marina-secimi-rehberi", "slug_en": "choosing-a-marina",
 "image": "/assets/images/hakkimizda.jpg", "date": "2028-12-07",
 "tr": {
   "category": "Rehber",
   "title": "Marina Seçimi Rehberi: Tekneniz İçin Doğru Liman",
   "excerpt": "Marina seçerken konum, korunaklılık, hizmetler, çekek imkânı ve maliyet. Doğru limanı seçmenin kriterleri.",
   "meta_title": "Marina Seçimi Rehberi | Tekne Usta",
   "meta_desc": "Marina seçimi rehberi: konum, korunaklılık, çekek/servis imkânları, güvenlik ve maliyet. Tekneniz için doğru limanı seçerken dikkat edilecekler.",
   "body": """
<p>Teknenizin bağlanacağı marina, hem keyfinizi hem bütçenizi hem de bakım kolaylığınızı doğrudan etkiler. Doğru seçim için şu kriterlere bakın.</p>
<h2>Konum ve erişim</h2>
<p>Evinize/işinize yakınlık, tekneyi ne sıklıkla kullanacağınızı belirler. Uzak bir marina, güzel de olsa zamanla "gitmeye üşendiğiniz" bir yer olabilir.</p>
<h2>Korunaklılık</h2>
<p>Marinanın rüzgâr ve dalgaya karşı korunaklı olması, hem güvenlik hem teknenin yıpranması açısından kritik. Açık, dalga alan bir liman tekneyi daha çok yorar.</p>
<h2>Servis ve çekek imkânı</h2>
<p>Marinanın veya yakınının <a href="/blog/tekne-cekek-karaya-cekme/">çekek/karaya çekme</a> imkânı, bakım ve onarımı çok kolaylaştırır. Servis sağlayıcılara (bizim gibi) erişim de önemli.</p>
<h2>Maliyet</h2>
<p>Bağlama ücreti tekne boyuna ve bölgeye göre büyük değişir. Yıllık <a href="/blog/tekne-sahipligi-maliyeti/">sahiplik maliyetinin</a> en büyük kalemlerinden biridir; peşinen hesaplayın.</p>
<h2>Güvenlik ve topluluk</h2>
<p>Kamera/güvenlik, ponton kalitesi ve marina topluluğu deneyimi belirler. Karar öncesi marinayı ziyaret edip mevcut tekne sahipleriyle konuşun.</p>
<p>Hangi marinada olursanız olun, İstanbul ve Ege'deki birçok limanda <a href="/#bolgeler">yerinde servis</a> veriyoruz — bakım için marinaya bağlı kalmazsınız.</p>
""",
 },
 "en": {
   "category": "Guide",
   "title": "Choosing a Marina: The Right Berth for Your Boat",
   "excerpt": "Location, shelter, services, haul-out and cost when choosing a marina. The criteria for picking the right berth.",
   "meta_title": "Choosing a Marina Guide | Tekne Usta",
   "meta_desc": "Choosing a marina guide: location, shelter, haul-out/service options, security and cost. What to consider when picking the right berth for your boat.",
   "body": """
<p>The marina where you berth directly affects your enjoyment, budget and ease of maintenance. Look at these criteria to choose well.</p>
<h2>Location and access</h2>
<p>Proximity to home/work determines how often you'll use the boat. A distant marina, however lovely, can become somewhere you "can't be bothered" to go.</p>
<h2>Shelter</h2>
<p>Shelter from wind and waves is critical for both safety and wear. An open, wave-exposed harbour tires the boat more.</p>
<h2>Service and haul-out</h2>
<p>A <a href="/en/blog/boat-haul-out-guide/">haul-out</a> option at or near the marina makes maintenance far easier. Access to service providers (like us) matters too.</p>
<h2>Cost</h2>
<p>Berthing fees vary greatly by boat length and region. It's one of the biggest items in annual <a href="/en/blog/cost-of-boat-ownership/">cost of ownership</a>; calculate it upfront.</p>
<h2>Security and community</h2>
<p>Cameras/security, pontoon quality and the marina community shape the experience. Visit before deciding and talk to current owners.</p>
<p>Whatever marina you're in, we offer <a href="/en/#bolgeler">on-site service</a> at many harbours across Istanbul and the Aegean — you're not tied to the marina for maintenance.</p>
""",
 },
},
{
 "slug": "yeni-tekne-sahibi-rehberi", "slug_en": "new-boat-owner-guide",
 "image": "/assets/images/parallax-2.jpg", "date": "2028-12-21",
 "tr": {
   "category": "Rehber",
   "title": "Yeni Tekne Sahibi Rehberi: İlk Sezonda Bilmeniz Gerekenler",
   "excerpt": "Teknenizi yeni aldınız — peki şimdi ne yapmalı? Bakım, belgeler, güvenlik ve ilk sezon kontrol listesi.",
   "meta_title": "Yeni Tekne Sahibi Rehberi | Tekne Usta",
   "meta_desc": "Yeni tekne sahibi rehberi: ilk sezonda bakım, belgeler, güvenlik ekipmanı, karina/antifouling ve düzenli bakım alışkanlıkları. Yeni başlayanlar için yol haritası.",
   "body": """
<p>Tebrikler, artık bir tekneniz var! İlk sezon hem heyecanlı hem de öğrenme dolu geçer. İşte başlangıçta yolunuzu kolaylaştıracak temel rehber.</p>
<h2>Teknenizi tanıyın</h2>
<p>Motor, elektrik, sintine pompası, seyir donanımı ve güvenlik ekipmanının yerini ve çalışmasını öğrenin. Bir "tekne el kitabı/dosyası" oluşturun.</p>
<h2>İlk bakım değerlendirmesi</h2>
<p>Özellikle ikinci else, sezona başlamadan bir <a href="/blog/satin-alma-oncesi-tekne-ekspertizi/">durum değerlendirmesi</a> yaptırın: karina, <a href="/blog/osmoz-belirtileri/">osmoz</a>, gelcoat/boya ve güverte kontrolü. Sorunları büyümeden yakalarsınız.</p>
<h2>Düzenli bakım alışkanlığı</h2>
<p>Bakımı "arıza çıkınca" değil, <a href="/blog/yillik-tekne-bakim-takvimi/">takvimli</a> yapın. Sezon öncesi ve sonrası bakım, teknenin ömrünü ve değerini korur; toplam maliyeti düşürür.</p>
<h2>Belgeler ve güvenlik</h2>
<p>Ruhsat, sigorta ve gerekli güvenlik ekipmanlarını (can yeleği, yangın söndürücü vb.) eksiksiz tutun. Detaylar için tekne sigortası ve mevzuatı ayrıca araştırın.</p>
<h2>Doğru ekiple çalışın</h2>
<p>Güvendiğiniz, şeffaf fiyatlı bir servisle çalışmak yeni sahiplik deneyimini çok rahatlatır. İlk değerlendirme için <a href="/#teklif-al">ücretsiz keşif</a> alabilirsiniz.</p>
""",
 },
 "en": {
   "category": "Guide",
   "title": "New Boat Owner Guide: What to Know in Your First Season",
   "excerpt": "You've just bought a boat — now what? Maintenance, documents, safety and a first-season checklist.",
   "meta_title": "New Boat Owner Guide | Tekne Usta",
   "meta_desc": "New boat owner guide: first-season maintenance, documents, safety gear, hull/antifouling and regular care habits. A roadmap for beginners.",
   "body": """
<p>Congratulations, you now own a boat! The first season is full of excitement and learning. Here's a basic guide to ease your way at the start.</p>
<h2>Get to know your boat</h2>
<p>Learn the location and operation of the engine, electrics, bilge pump, navigation and safety gear. Build a "boat manual/file".</p>
<h2>A first condition assessment</h2>
<p>Especially if used, have a <a href="/en/blog/pre-purchase-boat-survey/">condition assessment</a> before the season: hull, <a href="/en/blog/osmosis-symptoms/">osmosis</a>, gelcoat/paint and deck. You catch problems before they grow.</p>
<h2>A regular maintenance habit</h2>
<p>Maintain on a <a href="/en/blog/annual-boat-maintenance-calendar/">schedule</a>, not "when something breaks". Pre- and post-season care protects the boat's life and value and lowers total cost.</p>
<h2>Documents and safety</h2>
<p>Keep registration, insurance and required safety gear (life jackets, extinguisher, etc.) complete. Research boat insurance and regulations separately for detail.</p>
<h2>Work with the right team</h2>
<p>Working with a trusted, transparently priced service makes new ownership much easier. Get a <a href="/en/#teklif-al">free survey</a> for a first assessment.</p>
""",
 },
},
{
 "slug": "tekne-sigortasi-rehberi", "slug_en": "boat-insurance-guide",
 "image": "/assets/images/hakkimizda.jpg", "date": "2029-01-04",
 "tr": {
   "category": "Rehber",
   "title": "Tekne Sigortası ve Bakımın Rolü: Bilmeniz Gerekenler",
   "excerpt": "Tekne sigortası türleri, kapsam ve bakımın sigortayla ilişkisi. Genel bilgilendirme rehberi.",
   "meta_title": "Tekne Sigortası Rehberi: Bakımla İlişkisi | Tekne Usta",
   "meta_desc": "Tekne sigortası rehberi: kasko ve sorumluluk sigortası, kapsam, ekspertiz ve düzenli bakımın sigortayla ilişkisi. Genel bilgilendirme.",
   "body": """
<p>Tekne sigortası, beklenmedik hasar ve sorumluluklara karşı önemli bir koruma. Bu yazı genel bir bilgilendirmedir; kesin kapsam için sigortacınıza danışın.</p>
<h2>Başlıca türler</h2>
<ul>
<li><strong>Tekne kasko:</strong> Teknenin kendisine gelen hasarları (çarpma, fırtına, yangın vb.) kapsar.</li>
<li><strong>Sorumluluk (3. şahıs):</strong> Başka tekne/kişilere verilebilecek zararları kapsar; bazı marinalar zorunlu tutar.</li>
</ul>
<h2>Bakımın sigortayla ilişkisi</h2>
<p>Çoğu poliçe, teknenin "denize elverişli" ve bakımlı tutulmasını bekler. İhmalden kaynaklı hasarlar (ör. bakımsızlıktan su alma) kapsam dışı kalabilir. Düzenli <a href="/blog/yillik-tekne-bakim-takvimi/">bakım</a> ve kayıt tutmak, olası bir hasar talebinde işinizi kolaylaştırır.</p>
<h2>Ekspertiz</h2>
<p>Özellikle yaşlı teknelerde sigortacı bir <a href="/blog/satin-alma-oncesi-tekne-ekspertizi/">tekne ekspertizi</a> isteyebilir. Karina, gövde ve donanımın durumu hem primi hem kapsamı etkiler.</p>
<h2>Pratik öneri</h2>
<p>Poliçe alırken kapsamı, muafiyetleri ve "denize elverişlilik" şartlarını net okuyun. Teknenizin bakım kayıtlarını düzenli tutun — bunlar hem sigorta hem satış değeri için değerlidir.</p>
<p>Sigorta öncesi/sonrası durum değerlendirmesi için <a href="/hizmetler/fiberglas-onarim/">gövde/karina kontrolü</a> tarafında yardımcı olabiliriz.</p>
""",
 },
 "en": {
   "category": "Guide",
   "title": "Boat Insurance and the Role of Maintenance: What to Know",
   "excerpt": "Types of boat insurance, cover and how maintenance relates to it. A general information guide.",
   "meta_title": "Boat Insurance Guide: The Role of Maintenance | Tekne Usta",
   "meta_desc": "Boat insurance guide: hull and liability cover, survey and how regular maintenance relates to insurance. General information.",
   "body": """
<p>Boat insurance is important protection against unexpected damage and liability. This article is general information; consult your insurer for exact cover.</p>
<h2>Main types</h2>
<ul>
<li><strong>Hull insurance:</strong> covers damage to the boat itself (impact, storm, fire, etc.).</li>
<li><strong>Third-party liability:</strong> covers damage to other boats/people; some marinas require it.</li>
</ul>
<h2>How maintenance relates to insurance</h2>
<p>Most policies expect the boat to be kept "seaworthy" and maintained. Damage from neglect (e.g. leaks from poor maintenance) may fall outside cover. Regular <a href="/en/blog/annual-boat-maintenance-calendar/">maintenance</a> and keeping records make a possible claim easier.</p>
<h2>Survey</h2>
<p>Especially on older boats, an insurer may require a <a href="/en/blog/pre-purchase-boat-survey/">boat survey</a>. Hull and gear condition affect both premium and cover.</p>
<h2>Practical tip</h2>
<p>Read cover, deductibles and "seaworthiness" conditions carefully. Keep your maintenance records tidy — valuable for both insurance and resale.</p>
<p>For a pre/post-insurance condition assessment, we can help on the <a href="/en/services/fibreglass-repair/">hull/underbody</a> side.</p>
""",
 },
},
{
 "slug": "tekne-zemini-vinil", "slug_en": "boat-flooring-vinyl",
 "image": "/assets/images/services/bakim.jpg", "date": "2029-01-18",
 "tr": {
   "category": "İç Mekan",
   "title": "Tekne Zemini: Vinil, Halı ve Kaymaz Seçenekler",
   "excerpt": "Tekne iç ve kokpit zemininde vinil, deniz halısı ve kaymaz kaplama seçenekleri. Konfor, dayanıklılık ve bakım.",
   "meta_title": "Tekne Zemini: Vinil ve Halı Seçenekleri | Tekne Usta",
   "meta_desc": "Tekne zemini seçenekleri: deniz vinili, marin halı ve kaymaz kaplamalar. İç mekan ve kokpit için konfor, dayanıklılık ve temizlik açısından karşılaştırma.",
   "body": """
<p>Zemin, teknenin hem görünümünü hem konforunu hem güvenliğini etkiler. Doğru malzeme, ıslak ve tuzlu ortamda uzun ömür sağlar.</p>
<h2>Deniz vinili</h2>
<p>Su geçirmez, kolay temizlenen ve dayanıklı; ahşap/teak görünümlü desenleri de var. Kokpit ve ıslak alanlar için popüler. Bakımı kolaydır.</p>
<h2>Marin halı</h2>
<p>Sıcak, konforlu bir his verir; iç mekân/kabin için tercih edilir. Deniz sınıfı, çabuk kuruyan ve küfe dayanıklı olması şart — normal halı teknede küflenir.</p>
<h2>Kaymaz kaplamalar</h2>
<p>Islakken güvenlik için kokpit ve güvertede kaymaz zemin önemli. <a href="/blog/kaydirmaz-guverte-kaplama/">Kaydırmaz kaplama</a> veya EVA panel çözümleri kullanılabilir.</p>
<h2>Hangisi nerede?</h2>
<p>Islak/dış alanlarda vinil veya EVA; kuru iç kabinlerde marin halı mantıklı. Karışık kullanım da mümkün. Seçim, kullanımınıza ve estetiğe göre yapılır.</p>
<p>Zemin yenilemesini <a href="/hizmetler/ic-mekan-yenileme/">iç mekan yenileme</a> hizmetimiz kapsamında, döşemeyle birlikte planlıyoruz.</p>
""",
 },
 "en": {
   "category": "Interior",
   "title": "Boat Flooring: Vinyl, Carpet and Non-Slip Options",
   "excerpt": "Vinyl, marine carpet and non-slip options for boat interior and cockpit floors. Comfort, durability and care.",
   "meta_title": "Boat Flooring: Vinyl and Carpet Options | Tekne Usta",
   "meta_desc": "Boat flooring options: marine vinyl, marine carpet and non-slip coverings. A comparison for interior and cockpit in comfort, durability and cleaning.",
   "body": """
<p>Flooring affects a boat's look, comfort and safety. The right material lasts in a wet, salty environment.</p>
<h2>Marine vinyl</h2>
<p>Waterproof, easy to clean and durable; comes in wood/teak-look patterns too. Popular for cockpits and wet areas. Low maintenance.</p>
<h2>Marine carpet</h2>
<p>Gives a warm, comfortable feel; preferred for interiors/cabins. It must be marine-grade, quick-drying and mould-resistant — ordinary carpet grows mould aboard.</p>
<h2>Non-slip coverings</h2>
<p>Non-slip flooring matters for safety when wet in the cockpit and on deck. <a href="/en/blog/non-slip-deck-coating/">Non-slip coating</a> or EVA panels can be used.</p>
<h2>Which where?</h2>
<p>Vinyl or EVA in wet/exterior areas; marine carpet in dry cabins. Mixed use is fine too. Choose by your use and aesthetics.</p>
<p>We plan flooring renewal under our <a href="/en/services/interior-refit/">interior refit</a> service, alongside upholstery.</p>
""",
 },
},
{
 "slug": "minder-sunger-degisimi", "slug_en": "cushion-foam-replacement",
 "image": "/assets/images/services/bakim.jpg", "date": "2029-02-01",
 "tr": {
   "category": "İç Mekan",
   "title": "Tekne Minder ve Sünger Değişimi: Konforun Yenilenmesi",
   "excerpt": "Çökmüş minderler ve nem tutan süngerler teknede konforu bitirir. Doğru sünger ve kumaşla yenileme.",
   "meta_title": "Tekne Minder ve Sünger Değişimi | Tekne Usta",
   "meta_desc": "Tekne minder ve sünger değişimi: çökmüş sünger, hızlı kuruyan drenajlı sünger, deniz sınıfı kumaş ve ölçüye özel dikim. Kabin ve kokpit konforunu yenileme.",
   "body": """
<p>Minderler teknede en çok yıpranan parçalardandır: sünger çöker, kumaş solar, nem tutar. İyi haber — komple iç mekan yenilemeye gerek kalmadan sadece minder/sünger değişimi büyük fark yaratır.</p>
<h2>Doğru sünger</h2>
<p>Teknede standart sünger su tutar ve küflenir. Özellikle dış mekân (kokpit) minderlerinde <strong>hızlı kuruyan, drenajlı sünger</strong> nemi geçirir. İç mekânda konfor için doğru yoğunluk seçilir.</p>
<h2>Doğru kumaş</h2>
<p><a href="/blog/tekne-doseme-kumas-secimi/">Deniz sınıfı kumaş</a> — UV, tuz ve küfe dayanıklı, solmayan. En iyi sünger bile yanlış kumaşla kısa ömürlü olur.</p>
<h2>Ölçüye özel dikim</h2>
<p>Minderler teknenin oturma/yatak alanına özel ölçülüp dikilir. Doğru kalıp ve UV dayanımlı iplik; hem görünümü hem ömrü belirler.</p>
<h2>Sadece minder mi, komple mi?</h2>
<p>İstediğiniz kadarını yapabiliriz — sadece kokpit minderleri, sadece kabin, ya da hepsi. Perde/stor ile birlikte de planlanabilir (bkz. <a href="/blog/tekne-perde-stor/">perde ve stor</a>).</p>
<p>Minder ve sünger yenilemeyi <a href="/hizmetler/ic-mekan-yenileme/">iç mekan yenileme</a> hizmetimiz kapsamında yapıyoruz.</p>
""",
 },
 "en": {
   "category": "Interior",
   "title": "Boat Cushion and Foam Replacement: Renewing Comfort",
   "excerpt": "Collapsed cushions and damp-holding foam end comfort aboard. Renewal with the right foam and fabric.",
   "meta_title": "Boat Cushion and Foam Replacement | Tekne Usta",
   "meta_desc": "Boat cushion and foam replacement: collapsed foam, quick-dry draining foam, marine-grade fabric and made-to-measure sewing. Renewing cabin and cockpit comfort.",
   "body": """
<p>Cushions are among the most worn parts aboard: foam collapses, fabric fades, damp lingers. The good news — just cushion/foam replacement makes a big difference without a full interior refit.</p>
<h2>The right foam</h2>
<p>Standard foam holds water and grows mould aboard. Especially for exterior (cockpit) cushions, <strong>quick-dry draining foam</strong> lets moisture through. Indoors, the right density is chosen for comfort.</p>
<h2>The right fabric</h2>
<p><a href="/en/blog/marine-upholstery-fabric/">Marine-grade fabric</a> — UV-, salt- and mould-resistant, non-fading. Even the best foam is short-lived with the wrong fabric.</p>
<h2>Made-to-measure sewing</h2>
<p>Cushions are measured and sewn specifically for the boat's seating/berths. The right pattern and UV-resistant thread determine both look and life.</p>
<h2>Cushions only, or full?</h2>
<p>We do as much as you want — just cockpit cushions, just the cabin, or all. It can be planned with curtains/blinds too (see <a href="/en/blog/boat-curtains-blinds/">curtains and blinds</a>).</p>
<p>We do cushion and foam renewal under our <a href="/en/services/interior-refit/">interior refit</a> service.</p>
""",
 },
},
{
 "slug": "kokpit-eva-doseme", "slug_en": "cockpit-eva-decking",
 "image": "/assets/images/services/ic-mekan.jpg", "date": "2029-02-15",
 "tr": {
   "category": "Teak",
   "title": "Kokpit EVA Döşeme: Yumuşak, Kaymaz ve Bakımsız",
   "excerpt": "EVA köpük döşeme kokpit ve güvertede konfor + güvenlik sunar. Teak ve vinile göre avantajları.",
   "meta_title": "Kokpit EVA Köpük Döşeme Rehberi | Tekne Usta",
   "meta_desc": "Kokpit EVA köpük döşeme: yumuşak, kaymaz, bakımsız güverte kaplaması. Teak ve vinile göre avantajları, kullanım alanları ve uygulama.",
   "body": """
<p>EVA köpük döşeme, son yıllarda kokpit ve güvertede popülerleşen; yumuşak, kaymaz ve bakım gerektirmeyen bir kaplama. Özellikle konfor ve güvenlik önceliğindeyse iyi bir seçenek.</p>
<h2>Avantajları</h2>
<ul>
<li><strong>Yumuşak ve konforlu:</strong> Uzun süre ayakta durmak veya çocuklu kullanım için ideal.</li>
<li><strong>Kaymaz:</strong> Islakken bile güvenli tutuş.</li>
<li><strong>Bakımsız:</strong> Doğal <a href="/blog/teak-guverte-bakimi/">teakın</a> aksine yağ/vernik istemez; suyla temizlenir.</li>
<li><strong>Isı:</strong> Güneşte doğal teak kadar ısınmaz (renge bağlı).</li>
</ul>
<h2>Teak ve vinile göre</h2>
<p>Klasik teak görünümü ve prestiji istiyorsanız <a href="/blog/teak-vs-sentetik-teak/">doğal/sentetik teak</a>; ıslak alanda su geçirmezlik istiyorsanız <a href="/blog/tekne-zemini-vinil/">vinil</a>; konfor + kaymazlık önceliğinizse EVA mantıklı.</p>
<h2>Uygulama</h2>
<p>EVA paneller teknenin kalıbına göre kesilip yapıştırılır. Doğru yüzey hazırlığı, kenar/köşe kesimi ve yapıştırma; sonucun görünümünü ve ömrünü belirler.</p>
<p>Kokpit EVA döşemeyi <a href="/hizmetler/teak-guverte-doseme/">güverte döşeme</a> hizmetimiz kapsamında uyguluyoruz.</p>
""",
 },
 "en": {
   "category": "Teak",
   "title": "Cockpit EVA Decking: Soft, Non-Slip and Maintenance-Free",
   "excerpt": "EVA foam decking offers comfort + safety in the cockpit and on deck. Its advantages over teak and vinyl.",
   "meta_title": "Cockpit EVA Foam Decking Guide | Tekne Usta",
   "meta_desc": "Cockpit EVA foam decking: soft, non-slip, maintenance-free deck covering. Its advantages over teak and vinyl, uses and application.",
   "body": """
<p>EVA foam decking has grown popular for cockpits and decks in recent years; a soft, non-slip covering that needs no maintenance. A good option especially when comfort and safety are the priority.</p>
<h2>Advantages</h2>
<ul>
<li><strong>Soft and comfortable:</strong> ideal for long standing or use with children.</li>
<li><strong>Non-slip:</strong> safe grip even when wet.</li>
<li><strong>Maintenance-free:</strong> unlike natural <a href="/en/blog/teak-deck-maintenance/">teak</a> it needs no oil/varnish; cleans with water.</li>
<li><strong>Heat:</strong> doesn't get as hot as natural teak in the sun (colour-dependent).</li>
</ul>
<h2>Versus teak and vinyl</h2>
<p>If you want the classic teak look and prestige, <a href="/en/blog/teak-vs-synthetic-teak/">natural/synthetic teak</a>; for waterproofing in wet areas, <a href="/en/blog/boat-flooring-vinyl/">vinyl</a>; if comfort + non-slip is your priority, EVA makes sense.</p>
<h2>Application</h2>
<p>EVA panels are cut to the boat's template and bonded. Correct surface prep, edge/corner cutting and bonding determine the look and life.</p>
<p>We apply cockpit EVA decking under our <a href="/en/services/teak-deck/">decking</a> service.</p>
""",
 },
},
{
 "slug": "teak-temizligi-diy", "slug_en": "teak-cleaning-diy",
 "image": "/assets/images/services/ic-mekan.jpg", "date": "2029-03-01",
 "tr": {
   "category": "Teak",
   "title": "Teak Güverte Temizliği: Kendin Yap Rehberi (Doğru Yöntem)",
   "excerpt": "Teakı zarar vermeden nasıl temizlersiniz? Doğru fırça, yön ve kimyasal; yaygın hatalar ve ne zaman profesyonel gerekir.",
   "meta_title": "Teak Güverte Temizliği DIY Rehberi | Tekne Usta",
   "meta_desc": "Teak güverte temizliği DIY: doğru fırça ve yön, yumuşak deterjan, sert kimyasaldan kaçınma ve teakı inceltmeden temizleme. Yaygın hatalar ve profesyonel sınırı.",
   "body": """
<p>Teak temizliği doğru yapıldığında basit; yanlış yapıldığında teakı yıllar boyu inceltir. İşte teakı zarar vermeden temizlemenin pratik yolu.</p>
<h2>Doğru yöntem</h2>
<ul>
<li><strong>Yumuşak fırça, damar yönünde:</strong> Sert fırça veya damara dik fırçalama, yumuşak yaz damarını aşındırır ve teakı "olur olmaz" hale getirir.</li>
<li><strong>Yumuşak deterjan + bol su:</strong> Nazik bir deniz sabunu çoğu zaman yeterli. Derzlerde kir biriktirmeyin.</li>
<li><strong>Enine değil, hafif basınç:</strong> Amaç yüzeydeki kiri almak, teak aşındırmak değil.</li>
</ul>
<h2>Kaçınılması gerekenler</h2>
<ul>
<li>Sert, asitli "teak temizleyiciler"i sık kullanmak — hızlı sonuç verir ama teakı erozyona uğratır.</li>
<li>Yüksek basınçlı yıkama — yumuşak damarı söker, derzleri kaldırır.</li>
</ul>
<h2>Grileşme normaldir</h2>
<p>Gri renk zarar değil, doğal oksidasyondur. Teak sağlamsa gri, nazik temizlikle sıcak tona döner. Yağ tartışması için <a href="/blog/teak-yagi-surulmeli-mi/">bu yazıya</a> bakın.</p>
<h2>Ne zaman profesyonel?</h2>
<p>Derzler açılmış, teak incelmiş veya lekeler çıkmıyorsa DIY sınırı gelmiştir; <a href="/blog/teak-derz-yenileme/">derz yenileme</a> ya da restorasyon gerekebilir. <a href="/hizmetler/teak-guverte-doseme/">Teak bakım/yenileme</a> tarafında yardımcı oluyoruz.</p>
""",
 },
 "en": {
   "category": "Teak",
   "title": "Teak Deck Cleaning: A DIY Guide (The Right Way)",
   "excerpt": "How to clean teak without harming it? The right brush, direction and chemical; common mistakes and when a pro is needed.",
   "meta_title": "Teak Deck Cleaning DIY Guide | Tekne Usta",
   "meta_desc": "Teak deck cleaning DIY: the right brush and direction, mild detergent, avoiding harsh chemicals and cleaning without thinning the teak. Common mistakes and the pro threshold.",
   "body": """
<p>Teak cleaning is simple done right; done wrong it thins the teak over the years. Here's the practical way to clean teak without harm.</p>
<h2>The right method</h2>
<ul>
<li><strong>Soft brush, along the grain:</strong> a stiff brush or brushing across the grain erodes the soft summer grain and makes teak uneven.</li>
<li><strong>Mild detergent + plenty of water:</strong> a gentle boat soap is usually enough. Don't let dirt build up in the seams.</li>
<li><strong>Light pressure:</strong> the aim is to lift surface dirt, not to sand the teak.</li>
</ul>
<h2>What to avoid</h2>
<ul>
<li>Frequent use of harsh, acidic "teak cleaners" — fast results but they erode teak.</li>
<li>High-pressure washing — it tears the soft grain and lifts seams.</li>
</ul>
<h2>Greying is normal</h2>
<p>Grey isn't damage but natural oxidation. If the teak is sound, grey returns to a warm tone with gentle cleaning. For the oiling debate, see <a href="/en/blog/should-you-oil-teak/">this article</a>.</p>
<h2>When a pro?</h2>
<p>If seams have opened, the teak has thinned or stains won't lift, you've hit the DIY limit; <a href="/en/blog/teak-seam-renewal/">seam renewal</a> or restoration may be needed. We help on the <a href="/en/services/teak-deck/">teak care/renewal</a> side.</p>
""",
 },
},
{
 "slug": "ahsap-epoksi-cold-molding", "slug_en": "cold-molding-epoxy",
 "image": "/assets/images/services/ahsap.jpg", "date": "2029-03-15",
 "tr": {
   "category": "Ahşap",
   "title": "Cold-Molding: Epoksi ile Modern Ahşap Tekne Yapımı",
   "excerpt": "Cold-molding (soğuk kalıplama) nedir? İnce ahşap katmanların epoksiyle laminasyonu; dayanıklılık ve onarımdaki yeri.",
   "meta_title": "Cold-Molding: Epoksi ile Ahşap Laminasyon | Tekne Usta",
   "meta_desc": "Cold-molding (soğuk kalıplama) nedir? İnce ahşap kaplama katmanlarının epoksiyle çapraz laminasyonu, avantajları ve klasik ahşap tekne onarımındaki kullanımı.",
   "body": """
<p>Cold-molding (soğuk kalıplama), ince ahşap kaplama katmanlarının çapraz yönlerde epoksiyle laminasyonuyla güçlü, hafif ve su geçirmez bir gövde oluşturma tekniğidir. Geleneksel ahşap ile modern kompozitin en iyi yönlerini birleştirir.</p>
<h2>Nasıl çalışır?</h2>
<p>Birkaç kat ince ahşap, birbirine çapraz açıyla ve aralarına epoksi konarak yapıştırılır. Sonuç: tek parça ahşaptan çok daha rijit, çatlamaya ve neme dirençli bir yapı.</p>
<h2>Avantajları</h2>
<ul>
<li>Yüksek mukavemet/ağırlık oranı.</li>
<li>Epoksi sayesinde su geçirmezlik → <a href="/blog/ahsap-curuk-onarimi/">çürük</a> ve şişme riski düşer.</li>
<li>Geleneksel kalafat ihtiyacını azaltır.</li>
</ul>
<h2>Onarımdaki yeri</h2>
<p>Klasik ahşap teknelerin yapısal onarımında ve güçlendirmesinde cold-molding teknikleri kullanılabilir. Ancak her tekneye uygun değildir; özgün yapıya ve teknenin karakterine göre <a href="/blog/epoksi-ile-ahsap-guclendirme/">epoksi güçlendirme</a> ile birlikte değerlendirilir.</p>
<h2>Doğru karar</h2>
<p>Cold-molding uzmanlık ister; yanlış uygulanırsa katmanlar ayrılabilir. Teknenizin durumuna en uygun yöntemi <a href="/hizmetler/ahsap-tekne-renovasyonu/">ahşap tekne renovasyonu</a> hizmetimiz kapsamında değerlendiriyoruz.</p>
""",
 },
 "en": {
   "category": "Wood",
   "title": "Cold-Molding: Modern Wooden Boat Building with Epoxy",
   "excerpt": "What is cold-molding? Laminating thin wood veneers with epoxy; durability and its place in repair.",
   "meta_title": "Cold-Molding: Wood Lamination with Epoxy | Tekne Usta",
   "meta_desc": "What is cold-molding? Cross-laminating thin wood veneers with epoxy, its advantages and use in classic wooden boat repair.",
   "body": """
<p>Cold-molding is a technique of forming a strong, light, waterproof hull by laminating thin wood veneers in cross directions with epoxy. It combines the best of traditional wood and modern composite.</p>
<h2>How does it work?</h2>
<p>Several layers of thin wood are bonded at crossing angles with epoxy between them. The result: a structure far stiffer than solid wood, resistant to cracking and moisture.</p>
<h2>Advantages</h2>
<ul>
<li>High strength-to-weight ratio.</li>
<li>Waterproofing from the epoxy → lower <a href="/en/blog/wood-rot-repair/">rot</a> and swelling risk.</li>
<li>Reduces the need for traditional caulking.</li>
</ul>
<h2>Its place in repair</h2>
<p>Cold-molding techniques can be used in the structural repair and reinforcement of classic wooden boats. But it isn't right for every boat; it's weighed together with <a href="/en/blog/epoxy-wood-reinforcement/">epoxy reinforcement</a> according to the original structure and the boat's character.</p>
<h2>The right decision</h2>
<p>Cold-molding takes expertise; applied wrong, the layers can delaminate. We assess the method best suited to your boat under our <a href="/en/services/wooden-boat-refit/">wooden boat refit</a> service.</p>
""",
 },
},
{
 "slug": "ahsap-tekne-kislatma", "slug_en": "wooden-boat-winterising",
 "image": "/assets/images/services/ahsap.jpg", "date": "2029-03-29",
 "tr": {
   "category": "Ahşap",
   "title": "Ahşap Tekne Kışlatma: Nem ve Kuruma Dengesinin İnceliği",
   "excerpt": "Ahşap tekneyi kışlatmak fiberglastan farklıdır: aşırı kuruma da su almak kadar zararlıdır. Doğru yaklaşım.",
   "meta_title": "Ahşap Tekne Kışlatma Rehberi | Tekne Usta",
   "meta_desc": "Ahşap tekne kışlatma: nem-kuruma dengesi, havalandırma, derz koruması ve karada saklama. Ahşap teknenin kışı hasarsız geçirmesi için özel öneriler.",
   "body": """
<p>Ahşap tekneyi kışlatmak, fiberglastan farklı bir hassasiyet ister. Ahşap "yaşayan" bir malzemedir; nemle şişer, kuruyunca büzülür. Kışlatmanın sırrı bu dengeyi korumaktır — aşırı kuruma, su almak kadar zararlı olabilir.</p>
<h2>Aşırı kuruma tehlikesi</h2>
<p>Karada, güneşli ve rüzgârlı bir ortamda hızla kuruyan ahşap, derzlerin açılmasına ve <a href="/blog/kalafat-nedir/">kalafatın</a> gevşemesine yol açar. Bahar suya inişte tekne bir süre su alabilir (tahtalar tekrar şişene kadar). Bu yüzden ahşap teknede gölge, havalandırma ve nem dengesi önemlidir.</p>
<h2>Doğru kışlatma</h2>
<ul>
<li><strong>Havalandırma + gölge:</strong> Doğrudan güneşte pişirmeyen, hava alan bir örtü/konum.</li>
<li><strong>Derz ve vernik kontrolü:</strong> Kış öncesi <a href="/blog/ahsap-tekne-vernik-bakimi/">vernik</a> ve derz durumunu gözden geçir.</li>
<li><strong>Çürük taraması:</strong> Nemin sıkıştığı köşelerde <a href="/blog/ahsap-curuk-onarimi/">çürük</a> başlangıcı ara.</li>
</ul>
<h2>Bahar dönüşü</h2>
<p>Suya inişte tekneyi ilk günler takip et; hafif su alma normal olabilir ama sürerse derz/kalafat gerekebilir. Ahşap tekne kışlatma ve bahar bakımını <a href="/hizmetler/tekne-kislatma/">kışlatma</a> ve <a href="/hizmetler/ahsap-tekne-renovasyonu/">ahşap renovasyon</a> hizmetlerimizle birlikte planlıyoruz.</p>
""",
 },
 "en": {
   "category": "Wood",
   "title": "Wooden Boat Winterising: The Fine Balance of Damp and Drying",
   "excerpt": "Winterising a wooden boat differs from fibreglass: over-drying is as harmful as taking on water. The right approach.",
   "meta_title": "Wooden Boat Winterising Guide | Tekne Usta",
   "meta_desc": "Wooden boat winterising: the damp-drying balance, ventilation, seam protection and storing ashore. Special tips for a wooden boat to come through winter unharmed.",
   "body": """
<p>Winterising a wooden boat needs a different care than fibreglass. Wood is a "living" material; it swells with moisture and shrinks as it dries. The secret to winterising is keeping this balance — over-drying can be as harmful as taking on water.</p>
<h2>The danger of over-drying</h2>
<p>Ashore, in a sunny, windy spot, rapidly drying wood opens the seams and loosens the <a href="/en/blog/caulking-explained/">caulking</a>. At spring launch the boat may leak for a while (until the planks swell again). So shade, ventilation and moisture balance matter for a wooden boat.</p>
<h2>Correct winterising</h2>
<ul>
<li><strong>Ventilation + shade:</strong> a cover/position that airs out without baking in direct sun.</li>
<li><strong>Seam and varnish check:</strong> review <a href="/en/blog/wooden-boat-varnish-care/">varnish</a> and seam condition before winter.</li>
<li><strong>Rot scan:</strong> look for early <a href="/en/blog/wood-rot-repair/">rot</a> in corners where damp is trapped.</li>
</ul>
<h2>Spring return</h2>
<p>Watch the boat the first days after launch; slight leaking can be normal but if it persists, seams/caulking may be needed. We plan wooden boat winterising and spring care with our <a href="/en/services/winterising-storage/">winterising</a> and <a href="/en/services/wooden-boat-refit/">wooden refit</a> services.</p>
""",
 },
},
{
 "slug": "klasik-tekne-degeri", "slug_en": "classic-boat-value",
 "image": "/assets/images/services/ahsap.jpg", "date": "2029-04-12",
 "tr": {
   "category": "Rehber",
   "title": "Klasik Ahşap Teknenin Değeri: Restorasyon Yatırım mı?",
   "excerpt": "Klasik bir ahşap tekneyi restore etmek mantıklı bir yatırım mı? Değeri belirleyen faktörler ve karar.",
   "meta_title": "Klasik Tekne Değeri: Restorasyon Yatırım mı? | Tekne Usta",
   "meta_desc": "Klasik ahşap tekne değeri ve restorasyon: özgünlük, işçilik kalitesi, tarihçe ve duygusal değer. Restorasyonun maddi ve manevi getirisi.",
   "body": """
<p>Klasik bir ahşap tekneyi restore etmek çoğu zaman salt bir maliyet-getiri hesabı değildir; ama değeri belirleyen somut faktörler de vardır. İşte karar verirken dikkate alınacaklar.</p>
<h2>Değeri belirleyen faktörler</h2>
<ul>
<li><strong>Özgünlük:</strong> Orijinal ahşap, donanım ve hatların korunması değeri artırır.</li>
<li><strong>İşçilik kalitesi:</strong> İyi bir <a href="/blog/ahsap-tekne-restorasyon-vaka/">restorasyon</a>, teknenin hem ömrünü hem piyasa değerini yükseltir.</li>
<li><strong>Tarihçe ve nadirlik:</strong> Bilinen bir yapımcı/model, belgeli geçmiş değer katar.</li>
</ul>
<h2>Maddi vs manevi getiri</h2>
<p>Klasik tekneler her zaman "kâr" için restore edilmez; çoğu sahip için asıl getiri, eşsiz bir tekneyi yaşatmanın verdiği tatmindir. Yine de doğru yapılmış bir restorasyon, ihmal edilmiş bir tekneye göre çok daha kolay alıcı bulur.</p>
<h2>Akıllı restorasyon</h2>
<p>Aşamalı plan, özgün dokuya saygı ve gereksiz "aşırı yenileme"den kaçınmak; hem bütçeyi hem değeri korur. <a href="/blog/kalafat-nedir/">Kalafat</a>, <a href="/blog/ahsap-curuk-onarimi/">çürük onarımı</a> ve <a href="/blog/ahsap-tekne-vernik-bakimi/">vernik</a> gibi temel işler önceliklidir.</p>
<p>Klasik teknenizin durumunu ve restorasyon planını <a href="/hizmetler/ahsap-tekne-renovasyonu/">ahşap tekne renovasyonu</a> hizmetimiz kapsamında ücretsiz değerlendiriyoruz.</p>
""",
 },
 "en": {
   "category": "Guide",
   "title": "The Value of a Classic Wooden Boat: Is Restoration an Investment?",
   "excerpt": "Is restoring a classic wooden boat a sensible investment? The factors that set its value and how to decide.",
   "meta_title": "Classic Boat Value: Is Restoration an Investment? | Tekne Usta",
   "meta_desc": "Classic wooden boat value and restoration: originality, workmanship quality, history and emotional value. The material and personal return of restoration.",
   "body": """
<p>Restoring a classic wooden boat is often not a pure cost-return calculation; but there are concrete factors that set its value. Here's what to weigh when deciding.</p>
<h2>Factors that set value</h2>
<ul>
<li><strong>Originality:</strong> preserving original wood, hardware and lines raises value.</li>
<li><strong>Workmanship quality:</strong> a good <a href="/en/blog/wooden-restoration-case-study/">restoration</a> lifts both the boat's life and market value.</li>
<li><strong>History and rarity:</strong> a known builder/model and documented past add value.</li>
</ul>
<h2>Material vs emotional return</h2>
<p>Classic boats aren't always restored for "profit"; for most owners the real return is the satisfaction of keeping a unique boat alive. Still, a properly done restoration finds a buyer far more easily than a neglected boat.</p>
<h2>Smart restoration</h2>
<p>A staged plan, respect for the original character and avoiding needless "over-restoration" protect both budget and value. Core work like <a href="/en/blog/caulking-explained/">caulking</a>, <a href="/en/blog/wood-rot-repair/">rot repair</a> and <a href="/en/blog/wooden-boat-varnish-care/">varnish</a> comes first.</p>
<p>We assess your classic boat's condition and restoration plan for free under our <a href="/en/services/wooden-boat-refit/">wooden boat refit</a> service.</p>
""",
 },
},
{
 "slug": "teak-kalinligi-olcumu", "slug_en": "teak-thickness-check",
 "image": "/assets/images/services/ic-mekan.jpg", "date": "2029-04-26",
 "tr": {
   "category": "Teak",
   "title": "Teak Kalınlığı: Ne Zaman Yenileme, Ne Zaman Bakım Yeter?",
   "excerpt": "Teak güverte ne kadar inceldi? Kalınlığın önemi, ölçüm ve derz yenileme mi komple döşeme mi kararı.",
   "meta_title": "Teak Kalınlığı ve Yenileme Kararı | Tekne Usta",
   "meta_desc": "Teak güverte kalınlığı: neden önemli, nasıl anlaşılır ve ne zaman derz yenileme yeter, ne zaman komple döşeme gerekir? Doğru karar için rehber.",
   "body": """
<p>Teak güvertede en kritik soru çoğu zaman şudur: teak hâlâ yeterince kalın mı? Kalınlık, sadece derzleri yenilemenin mi yoksa komple döşemenin mi gerektiğini belirler.</p>
<h2>Kalınlık neden önemli?</h2>
<p>Teak zamanla temizlik, zımpara ve doğal aşınmayla incelir. Vida başları yüzeye yaklaştıysa veya derz kanalları sığlaştıysa, teak ömrünün sonuna yaklaşmış demektir. Fazla ince teak, derz tutmaz ve altına su sızdırır.</p>
<h2>Nasıl anlaşılır?</h2>
<ul>
<li>Derz derinliğinin belirgin azalması.</li>
<li>Vida tapalarının (bung) görünmeye başlaması.</li>
<li>Yer yer teakın altındaki yapıştırıcının/alt yüzeyin görünmesi.</li>
</ul>
<h2>Karar</h2>
<p>Teak yeterince kalınsa <a href="/blog/teak-derz-yenileme/">derz yenileme</a> ekonomik ve yeterlidir. İnceldiyse komple döşeme gerekir; bu noktada doğal ile <a href="/blog/sentetik-teak-alternatifleri/">sentetik teak</a> alternatiflerini de değerlendirmek mantıklı. Fiyatı belirleyen faktörler için <a href="/blog/teak-guverte-fiyatlari/">teak fiyatları</a> yazımıza bakın.</p>
<p>Keşifte teak kalınlığını yerinde ölçüp sizi doğru yönlendiriyoruz — gereksiz komple döşeme önermeyiz. <a href="/hizmetler/teak-guverte-doseme/">Teak güverte döşeme</a> hizmetimizle yanınızdayız.</p>
""",
 },
 "en": {
   "category": "Teak",
   "title": "Teak Thickness: When to Renew and When Care Is Enough?",
   "excerpt": "How thin has your teak deck worn? Why thickness matters, how to check it, and the seam-renewal vs full-deck decision.",
   "meta_title": "Teak Thickness and the Renewal Decision | Tekne Usta",
   "meta_desc": "Teak deck thickness: why it matters, how to tell and when seam renewal is enough versus a full deck. A guide to the right decision.",
   "body": """
<p>On a teak deck the most critical question is often: is the teak still thick enough? Thickness determines whether just renewing the seams will do, or a full deck is needed.</p>
<h2>Why does thickness matter?</h2>
<p>Teak thins over time with cleaning, sanding and natural wear. If screw heads are nearing the surface or seam grooves have shallowed, the teak is near the end of its life. Too-thin teak won't hold seams and lets water seep beneath.</p>
<h2>How to tell?</h2>
<ul>
<li>Noticeably reduced seam depth.</li>
<li>Screw bungs starting to show.</li>
<li>The adhesive/sub-surface showing through in places.</li>
</ul>
<h2>The decision</h2>
<p>If the teak is thick enough, <a href="/en/blog/teak-seam-renewal/">seam renewal</a> is economical and enough. If thinned, a full deck is needed; at that point it's sensible to weigh natural vs <a href="/en/blog/synthetic-teak-alternatives/">synthetic teak</a>. For price factors, see our <a href="/en/blog/teak-deck-cost/">teak cost</a> article.</p>
<p>We measure teak thickness on site at the survey and advise you correctly — we don't recommend a needless full deck. We're with you through our <a href="/en/services/teak-deck/">teak decking</a> service.</p>
""",
 },
},
{
 "slug": "osmozdan-korunma", "slug_en": "osmosis-prevention",
 "image": "/assets/images/services/fiberglas.jpg", "date": "2029-05-10",
 "tr": {
   "category": "Fiberglas",
   "title": "Osmozdan Korunma: Önleyici Bakımla Sorunu Baştan Engellemek",
   "excerpt": "Osmoz tedavi edilmeden önce önlenebilir mi? Bariyer kat, karina bakımı ve nem kontrolüyle koruyucu yaklaşım.",
   "meta_title": "Osmozdan Korunma: Önleyici Bakım | Tekne Usta",
   "meta_desc": "Osmozdan korunma: epoksi bariyer kat, düzenli karina bakımı, nem kontrolü ve kışlatmada kurutma. Fiber teknede osmozu baştan engellemenin yolları.",
   "body": """
<p>Osmozu <a href="/blog/osmoz-nedir-tedavisi/">tedavi etmek</a> maliyetli ve uzun bir iştir. İyi haber: doğru önleyici bakımla riski ciddi biçimde azaltmak mümkün. En iyi osmoz tedavisi, hiç başlamamasıdır.</p>
<h2>Koruyucu bariyer kat</h2>
<p>Yeni veya sağlam teknelerde su altına uygulanan <strong>epoksi bariyer kat</strong>, suyun laminata sızmasını zorlaştırır. Uzun vadede en etkili korumadır; yeni tekne alırken düşünülebilecek bir yatırımdır.</p>
<h2>Karinayı kuru tutmak</h2>
<p>Teknenin uzun süre sürekli suda kalması riski artırır. Sezon sonu <a href="/hizmetler/tekne-kislatma/">karaya çekip</a> karinanın kurumasına izin vermek, nemi düşürür. <a href="/blog/kisin-tekne-nerede-saklanir/">Karada kışlatma</a> bu açıdan avantajlıdır.</p>
<h2>Düzenli kontrol</h2>
<p>Her sezon karada <a href="/blog/osmoz-belirtileri/">osmoz belirtisi</a> ve nem taraması yapmak, sorunu erken yakalar. Erken müdahale, komple tedaviden çok daha ucuzdur.</p>
<h2>Antifouling ve yüzey bütünlüğü</h2>
<p>Sağlam bir <a href="/blog/antifouling-secimi/">antifouling</a> ve çiziksiz jelkot, suyun giriş yollarını kapatır. Yüzeydeki hasarları büyümeden onarmak korumanın parçasıdır.</p>
<p>Teknenize koruyucu bariyer kat veya karina değerlendirmesi için <a href="/hizmetler/fiberglas-onarim/">fiberglas onarım</a> hizmetimiz kapsamında ücretsiz keşif yapıyoruz.</p>
""",
 },
 "en": {
   "category": "Fibreglass",
   "title": "Osmosis Prevention: Stopping the Problem Before It Starts",
   "excerpt": "Can osmosis be prevented before treatment? A protective approach with barrier coat, hull care and moisture control.",
   "meta_title": "Osmosis Prevention: Preventive Care | Tekne Usta",
   "meta_desc": "Osmosis prevention: epoxy barrier coat, regular hull care, moisture control and drying at winterising. Ways to stop osmosis before it starts on a fibreglass boat.",
   "body": """
<p><a href="/en/blog/what-is-osmosis-treatment/">Treating</a> osmosis is a costly, lengthy job. The good news: with the right preventive care the risk can be greatly reduced. The best osmosis treatment is never starting at all.</p>
<h2>Protective barrier coat</h2>
<p>On new or sound boats, an <strong>epoxy barrier coat</strong> applied below the waterline makes it harder for water to seep into the laminate. It's the most effective long-term protection and worth considering when buying a new boat.</p>
<h2>Keeping the hull dry</h2>
<p>A boat kept constantly afloat for long periods is at higher risk. Hauling out at season's end and letting the hull dry lowers moisture. <a href="/en/blog/winter-boat-storage/">Storing ashore</a> is an advantage here.</p>
<h2>Regular checks</h2>
<p>Scanning for <a href="/en/blog/osmosis-symptoms/">osmosis signs</a> and moisture ashore each season catches the problem early. Early action is far cheaper than a full treatment.</p>
<h2>Antifouling and surface integrity</h2>
<p>Sound <a href="/en/blog/choosing-antifouling/">antifouling</a> and a scratch-free gelcoat close water's entry paths. Repairing surface damage before it grows is part of prevention.</p>
<p>For a protective barrier coat or hull assessment, we do a free survey under our <a href="/en/services/fibreglass-repair/">fibreglass repair</a> service.</p>
""",
 },
},
{
 "slug": "yat-boyama", "slug_en": "yacht-painting",
 "image": "/assets/images/parallax-1.jpg", "date": "2029-05-24",
 "tr": {
   "category": "Boya",
   "title": "Yat Boyama: Süperyat Kalitesinde Bir Bitiş İçin",
   "excerpt": "Yat boyama neden özel bir iştir? Büyük yüzey, 2K poliüretan, yüzey hazırlığı ve maliyeti belirleyen faktörler.",
   "meta_title": "Yat Boyama Rehberi: Fiyat ve Süreç | Tekne Usta",
   "meta_desc": "Yat boyama: 2K poliüretan sistemler, dış cephe ve antifouling, yüzey hazırlığı ve maliyeti belirleyen faktörler. İstanbul ve Ege'de yat boyama hizmeti.",
   "body": """
<p>Yat boyama, küçük tekne boyamaktan çok daha kapsamlı bir iştir; büyük yüzey, yüksek beklenti ve kalıcı bir parlaklık gerektirir. Doğru sistem ve titiz işçilik olmadan, pahalı görünen bir iş kısa sürede hayal kırıklığı yaratır.</p>
<h2>Yatlarda hangi boya?</h2>
<p>Süperyat parlaklığı için genelde <a href="/blog/2k-poliuretan-boya/">2K poliüretan</a> sistemler tercih edilir: derin parlaklık, yüksek UV direnci, uzun ömür. Su altında ise doğru <a href="/blog/antifouling-secimi/">antifouling</a> seçilir.</p>
<h2>Maliyeti ne belirler?</h2>
<p>Yat boyama fiyatı; boy/yüzey alanı, kat sayısı, renk değişimi ve en önemlisi <a href="/blog/boya-oncesi-yuzey-hazirligi/">yüzey hazırlığının</a> kapsamıyla belirlenir. Detay için <a href="/blog/tekne-boyama-maliyeti/">boyama maliyeti</a> yazımıza bakın.</p>
<h2>Neden yüzey hazırlığı kritik?</h2>
<p>Büyük yüzeyde en küçük kusur bile belli olur. Doğru zımpara, dolgu (fairing) ve astar; pürüzsüz, aynalı bir bitişin ön koşuludur. Biz teklifi kalem kalem veririz; hangi adıma ne emek gittiği nettir.</p>
<p>Yatınızın boya ve antifouling işini <a href="/hizmetler/tekne-boyama-antifouling/">tekne boyama</a> hizmetimiz ve <a href="/tekneler/yat-motoryat/">yat & motoryat</a> bakım kapsamında yapıyoruz. <a href="#teklif-al">Ücretsiz keşif</a> alın.</p>
""",
 },
 "en": {
   "category": "Painting",
   "title": "Yacht Painting: For a Superyacht-Grade Finish",
   "excerpt": "Why is yacht painting a special job? Large surface, 2K polyurethane, surface prep and the factors that set the cost.",
   "meta_title": "Yacht Painting Guide: Cost and Process | Tekne Usta",
   "meta_desc": "Yacht painting: 2K polyurethane systems, topside and antifouling, surface prep and cost factors. Yacht painting service in Istanbul and the Aegean.",
   "body": """
<p>Yacht painting is far more involved than painting a small boat; it needs a large surface, high expectations and lasting gloss. Without the right system and meticulous work, a cheap-looking job soon disappoints.</p>
<h2>Which paint on yachts?</h2>
<p>For superyacht gloss, <a href="/en/blog/2k-polyurethane-paint/">2K polyurethane</a> systems are usually preferred: deep gloss, high UV resistance, long life. Below the waterline, the right <a href="/en/blog/choosing-antifouling/">antifouling</a> is chosen.</p>
<h2>What sets the cost?</h2>
<p>Yacht painting cost is set by length/area, coat count, colour change and above all the extent of <a href="/en/blog/surface-prep-before-painting/">surface prep</a>. For detail, see our <a href="/en/blog/boat-painting-cost/">painting cost</a> article.</p>
<h2>Why is surface prep critical?</h2>
<p>On a large surface, the smallest flaw shows. Correct sanding, fairing and primer are the precondition for a smooth, mirror finish. We quote itemised; how much effort each step takes is clear.</p>
<p>We do your yacht's paint and antifouling under our <a href="/en/services/boat-painting-antifouling/">boat painting</a> service and <a href="/en/boats/yacht-motoryacht/">yacht & motoryacht</a> care. Get a <a href="#teklif-al">free survey</a>.</p>
""",
 },
},
{
 "slug": "yat-kislatma", "slug_en": "yacht-winterising",
 "image": "/assets/images/services/bakim.jpg", "date": "2029-06-07",
 "tr": {
   "category": "Bakım",
   "title": "Yat Kışlatma: Sezonu Doğru Kapatmak",
   "excerpt": "Yatınızı kışa hazırlarken karaya çekme, karina, örtü ve gözetimli depolama. Bahara sorunsuz çıkmanın yolu.",
   "meta_title": "Yat Kışlatma Rehberi | Tekne Usta",
   "meta_desc": "Yat kışlatma: karaya çekme, karina temizliği ve kontrolü, havalandırmalı örtü ve gözetimli depolama. İstanbul ve Ege'de yat kışlatma hizmeti.",
   "body": """
<p>Yat kışlatma, sezon sonu yapılan ve bahar bakımını büyük ölçüde kolaylaştıran kritik bir iştir. İyi kışlatılmış bir yat, sezona sorunsuz ve erken başlar.</p>
<h2>Kışlatma kapsamı</h2>
<ul>
<li><a href="/blog/tekne-cekek-karaya-cekme/">Karaya çekme</a> ve basınçlı yıkama</li>
<li>Karina, <a href="/blog/anot-zinc-bakimi/">anot</a> ve boya durumu kontrolü</li>
<li>İç mekan havalandırması ve <a href="/blog/teknede-kuf-nem-onleme/">nem/küf</a> önlemi</li>
<li><a href="/blog/tekne-ortusu-secimi/">Havalandırmalı örtü</a> ve gözetimli depolama</li>
</ul>
<h2>Neden karada?</h2>
<p>Yatı karada kışlatmak karinanın kurumasını sağlar, <a href="/blog/osmozdan-korunma/">osmoz riskini</a> azaltır ve bakım işlerini kolaylaştırır. <a href="/blog/kisin-tekne-nerede-saklanir/">Depolama seçenekleri</a> için ayrı yazımıza bakın.</p>
<h2>Bahar planı</h2>
<p>Kış boyunca yatınızı takip eder, sezon açılışında karina ve boyayı birlikte değerlendiririz. Not: motor-mekanik kışlatma kapsamımız dışında; güvendiğimiz servislere yönlendiriyoruz.</p>
<p>Yat kışlatmayı <a href="/hizmetler/tekne-kislatma/">kışlatma</a> hizmetimiz ve <a href="/tekneler/yat-motoryat/">yat & motoryat</a> bakım kapsamında yapıyoruz. Erken rezervasyon için <a href="#teklif-al">bize yazın</a>.</p>
""",
 },
 "en": {
   "category": "Maintenance",
   "title": "Yacht Winterising: Closing the Season Right",
   "excerpt": "Haul-out, hull, cover and supervised storage when preparing your yacht for winter. The way to a trouble-free spring.",
   "meta_title": "Yacht Winterising Guide | Tekne Usta",
   "meta_desc": "Yacht winterising: haul-out, hull cleaning and checks, ventilated cover and supervised storage. Yacht winterising service in Istanbul and the Aegean.",
   "body": """
<p>Yacht winterising is a critical end-of-season job that greatly eases spring maintenance. A well-winterised yacht starts the season early and trouble-free.</p>
<h2>Scope of winterising</h2>
<ul>
<li><a href="/en/blog/boat-haul-out-guide/">Haul-out</a> and pressure wash</li>
<li>Hull, <a href="/en/blog/anode-zinc-care/">anode</a> and paint condition checks</li>
<li>Interior ventilation and <a href="/en/blog/preventing-mould-damp/">damp/mould</a> measures</li>
<li><a href="/en/blog/boat-cover-selection/">Ventilated cover</a> and supervised storage</li>
</ul>
<h2>Why ashore?</h2>
<p>Winterising the yacht ashore lets the hull dry, lowers <a href="/en/blog/osmosis-prevention/">osmosis risk</a> and eases maintenance. See our separate article on <a href="/en/blog/winter-boat-storage/">storage options</a>.</p>
<h2>Spring plan</h2>
<p>We monitor your yacht through winter and assess hull and paint together at launch. Note: engine/mechanical winterising is outside our scope; we refer you to trusted services.</p>
<p>We do yacht winterising under our <a href="/en/services/winterising-storage/">winterising</a> service and <a href="/en/boats/yacht-motoryacht/">yacht & motoryacht</a> care. To book early, <a href="#teklif-al">message us</a>.</p>
""",
 },
},
{
 "slug": "yelkenli-kislatma", "slug_en": "sailboat-winterising",
 "image": "/assets/images/parallax-2.jpg", "date": "2029-06-21",
 "tr": {
   "category": "Bakım",
   "title": "Yelkenli Kışlatma: Gövde, Karina ve Nem Dengesi",
   "excerpt": "Yelkenlinizi kışa hazırlarken karina, antifouling, iç mekan nemi ve ahşap detaylar. Sezona hazır çıkmak.",
   "meta_title": "Yelkenli Kışlatma Rehberi | Tekne Usta",
   "meta_desc": "Yelkenli kışlatma: karaya çekme, karina ve antifouling kontrolü, iç mekan nem/küf önlemi, ahşap detay bakımı ve havalandırmalı örtü. İstanbul ve Ege'de yelkenli servisi.",
   "body": """
<p>Yelkenli kışlatma, gövde ve karina bakımının yanı sıra iç mekan nemini de doğru yönetmeyi gerektirir. İyi kışlatılmış bir yelkenli sezona sorunsuz başlar.</p>
<h2>Kışlatma kapsamı</h2>
<ul>
<li><a href="/blog/tekne-cekek-karaya-cekme/">Karaya çekme</a>, yıkama ve karina kontrolü</li>
<li><a href="/blog/antifouling-secimi/">Antifouling</a> ve <a href="/blog/osmoz-belirtileri/">osmoz</a> durumu</li>
<li>İç mekan havalandırması, <a href="/blog/teknede-kuf-nem-onleme/">nem/küf</a> önlemi</li>
<li>Klasik ahşap yelkenlilerde <a href="/blog/ahsap-tekne-kislatma/">ahşap kışlatma</a> inceliği</li>
</ul>
<h2>Ahşap yelkenlilere dikkat</h2>
<p>Klasik ahşap yelkenlilerde aşırı kuruma da su almak kadar zararlıdır; havalandırma ve nem dengesi önemlidir. <a href="/blog/ahsap-tekne-kislatma/">Ahşap kışlatma</a> yazımızda detaylandırdık.</p>
<h2>Kapsamımız</h2>
<p>Gövde, karina, iç mekan ve ahşap tarafında tam hizmet; direk/arma ve motor işleri kapsam dışı. Yelkenli kışlatmayı <a href="/hizmetler/tekne-kislatma/">kışlatma</a> hizmetimiz ve <a href="/tekneler/yelkenli/">yelkenli</a> bakım kapsamında yapıyoruz.</p>
<p>Erken rezervasyon için <a href="#teklif-al">bize yazın</a>.</p>
""",
 },
 "en": {
   "category": "Maintenance",
   "title": "Sailboat Winterising: Hull, Underbody and Damp Balance",
   "excerpt": "Hull, antifouling, interior damp and wood details when preparing your sailboat for winter. Starting the season ready.",
   "meta_title": "Sailboat Winterising Guide | Tekne Usta",
   "meta_desc": "Sailboat winterising: haul-out, hull and antifouling checks, interior damp/mould control, wood detail care and ventilated cover in Istanbul and the Aegean.",
   "body": """
<p>Sailboat winterising requires managing interior damp as well as hull and underbody care. A well-winterised sailboat starts the season trouble-free.</p>
<h2>Scope of winterising</h2>
<ul>
<li><a href="/en/blog/boat-haul-out-guide/">Haul-out</a>, wash and hull check</li>
<li><a href="/en/blog/choosing-antifouling/">Antifouling</a> and <a href="/en/blog/osmosis-symptoms/">osmosis</a> condition</li>
<li>Interior ventilation, <a href="/en/blog/preventing-mould-damp/">damp/mould</a> measures</li>
<li>On classic wooden sailboats, <a href="/en/blog/wooden-boat-winterising/">wooden winterising</a> nuance</li>
</ul>
<h2>Care on wooden sailboats</h2>
<p>On classic wooden sailboats, over-drying is as harmful as taking on water; ventilation and moisture balance matter. We detail this in our <a href="/en/blog/wooden-boat-winterising/">wooden winterising</a> article.</p>
<h2>Our scope</h2>
<p>Full service on hull, underbody, interior and wood; mast/rigging and engine work are out of scope. We do sailboat winterising under our <a href="/en/services/winterising-storage/">winterising</a> service and <a href="/en/boats/sailboat/">sailboat</a> care.</p>
<p>To book early, <a href="#teklif-al">message us</a>.</p>
""",
 },
},
{
 "slug": "yelkenli-osmoz", "slug_en": "sailboat-osmosis",
 "image": "/assets/images/services/fiberglas.jpg", "date": "2029-07-05",
 "tr": {
   "category": "Fiberglas",
   "title": "Yelkenli Osmoz: Fiberglas Yelkenlilerde Karina Sorunu",
   "excerpt": "Fiberglas yelkenlilerde osmoz neden sık görülür, nasıl anlaşılır ve tedavi edilir?",
   "meta_title": "Yelkenli Osmoz Tedavisi Rehberi | Tekne Usta",
   "meta_desc": "Yelkenli osmoz: fiberglas yelkenlilerde osmoz belirtileri, nem ölçümü, jelkot sıyırma-kurutma-bariyer tedavisi ve korunma. İstanbul ve Ege'de yelkenli osmoz servisi.",
   "body": """
<p>Fiberglas yelkenliler uzun süre suda kaldığından, karinada osmoz sık karşılaşılan bir sorundur. Erken yakalandığında yönetilebilir; ihmal edilince karina baştan elden geçer.</p>
<h2>Yelkenlilerde neden sık?</h2>
<p>Sezon boyunca sürekli suda kalan, kışın da her zaman karaya çekilmeyen yelkenlilerde laminat nemi artar. Bu da <a href="/blog/osmoz-nedir-tedavisi/">osmoz</a> için zemin hazırlar.</p>
<h2>Belirti ve tanı</h2>
<p>Su altında kabarcık, ekşi koku ve yüksek nem ölçer değeri osmozu işaret eder (bkz. <a href="/blog/osmoz-belirtileri/">osmoz belirtileri</a>). <a href="/blog/blister-vs-osmoz-farki/">Blister mi osmoz mu</a> ayrımı önemlidir.</p>
<h2>Tedavi</h2>
<p>Jelkot sıyırma, <strong>tam kurutma</strong>, epoksi bariyer ve antifouling adımlarıyla tedavi edilir. Kurutma atlanırsa sorun geri döner. Korunma için <a href="/blog/osmozdan-korunma/">önleyici bakıma</a> bakın.</p>
<p>Yelkenlinizin karina/osmoz işini <a href="/hizmetler/fiberglas-onarim/">fiberglas onarım</a> hizmetimiz ve <a href="/tekneler/yelkenli/">yelkenli</a> bakım kapsamında yapıyoruz. Nem ölçümlü <a href="#teklif-al">ücretsiz keşif</a> alın.</p>
""",
 },
 "en": {
   "category": "Fibreglass",
   "title": "Sailboat Osmosis: The Hull Problem on Fibreglass Sailboats",
   "excerpt": "Why is osmosis common on fibreglass sailboats, how do you spot it and treat it?",
   "meta_title": "Sailboat Osmosis Treatment Guide | Tekne Usta",
   "meta_desc": "Sailboat osmosis: symptoms on fibreglass sailboats, moisture reading, gelcoat-peel-dry-barrier treatment and prevention in Istanbul and the Aegean.",
   "body": """
<p>Because fibreglass sailboats stay afloat for long periods, osmosis is a common hull problem. Caught early it's manageable; neglected, the whole hull needs work.</p>
<h2>Why common on sailboats?</h2>
<p>On sailboats kept constantly afloat and not always hauled out in winter, laminate moisture rises. This sets the stage for <a href="/en/blog/what-is-osmosis-treatment/">osmosis</a>.</p>
<h2>Symptoms and diagnosis</h2>
<p>Underwater blisters, a sour smell and a high moisture reading point to osmosis (see <a href="/en/blog/osmosis-symptoms/">osmosis symptoms</a>). The <a href="/en/blog/blister-vs-osmosis/">blister vs osmosis</a> distinction matters.</p>
<h2>Treatment</h2>
<p>Treated with gelcoat peeling, <strong>full drying</strong>, epoxy barrier and antifouling. Skip drying and the problem returns. For prevention, see <a href="/en/blog/osmosis-prevention/">preventive care</a>.</p>
<p>We do your sailboat's hull/osmosis work under our <a href="/en/services/fibreglass-repair/">fibreglass repair</a> service and <a href="/en/boats/sailboat/">sailboat</a> care. Get a <a href="#teklif-al">free survey</a> with a moisture reading.</p>
""",
 },
},
{
 "slug": "gulet-boyama", "slug_en": "gulet-painting",
 "image": "/assets/images/parallax-3.jpg", "date": "2029-07-19",
 "tr": {
   "category": "Boya",
   "title": "Gulet Boyama: Büyük Ahşap Gövdede Kalıcı Bitiş",
   "excerpt": "Guletlerde dış cephe boyama, vernik ve antifouling; büyük ahşap yüzeyde doğru sistem ve bakım.",
   "meta_title": "Gulet Boyama ve Vernik Rehberi | Tekne Usta",
   "meta_desc": "Gulet boyama: büyük ahşap gövdede dış cephe boyama, vernik, antifouling ve yüzey hazırlığı. Ege ve İstanbul'da gulet boya-vernik servisi.",
   "body": """
<p>Guletlerin büyük ahşap gövdesi, hem estetik hem koruma açısından düzenli boya ve vernik bakımı ister. Doğru sistem ve işçilik, hem görünümü hem ahşabı yıllarca korur.</p>
<h2>Boya mı, vernik mi?</h2>
<p>Guletlerde gövdenin bir kısmı boyalı, açık ahşap detaylar vernikli olur. Vernik doğal dokuyu gösterir ama daha çok bakım ister; boya daha korunaklıdır. Karar ahşabın durumuna göre verilir (bkz. <a href="/blog/ahsap-tekne-boyama/">ahşap tekne boyama</a>).</p>
<h2>Yüzey hazırlığı</h2>
<p>Büyük yüzeyde <a href="/blog/boya-oncesi-yuzey-hazirligi/">yüzey hazırlığı</a> belirleyicidir; eski katmanların doğru sökülmesi ve sağlam zemin şarttır. Su altında ise <a href="/blog/antifouling-secimi/">antifouling</a> yenilenir.</p>
<h2>Sezon planı</h2>
<p>Ticari guletlerde boya-vernik bakımı sezon öncesi planlanmalı. Çok kalemli işleri <a href="/blog/refit-proje-yonetimi/">tek elden</a> yürütüyoruz.</p>
<p>Gulet boyama ve verniğini <a href="/hizmetler/tekne-boyama-antifouling/">boya</a> ve <a href="/hizmetler/ahsap-tekne-renovasyonu/">ahşap renovasyon</a> hizmetlerimiz, <a href="/tekneler/gulet/">gulet</a> bakım kapsamında yapıyoruz. <a href="#teklif-al">Teklif alın</a>.</p>
""",
 },
 "en": {
   "category": "Painting",
   "title": "Gulet Painting: A Lasting Finish on a Large Wooden Hull",
   "excerpt": "Topside painting, varnish and antifouling on gulets; the right system and care on a large wooden surface.",
   "meta_title": "Gulet Painting and Varnish Guide | Tekne Usta",
   "meta_desc": "Gulet painting: topside painting, varnish, antifouling and surface prep on a large wooden hull. Gulet paint-varnish service in the Aegean and Istanbul.",
   "body": """
<p>A gulet's large wooden hull needs regular paint and varnish care for both looks and protection. The right system and workmanship protect both the appearance and the wood for years.</p>
<h2>Paint or varnish?</h2>
<p>On gulets, part of the hull is painted and exposed wood details are varnished. Varnish shows the natural grain but needs more care; paint is more protective. The decision follows the wood's condition (see <a href="/en/blog/wooden-boat-painting/">wooden boat painting</a>).</p>
<h2>Surface prep</h2>
<p>On a large surface, <a href="/en/blog/surface-prep-before-painting/">surface prep</a> is decisive; correctly stripping old layers and a sound base are essential. Below the waterline, <a href="/en/blog/choosing-antifouling/">antifouling</a> is renewed.</p>
<h2>Season plan</h2>
<p>On commercial gulets, paint-varnish care should be planned pre-season. We run multi-item work <a href="/en/blog/refit-project-management/">from one hand</a>.</p>
<p>We do gulet painting and varnish under our <a href="/en/services/boat-painting-antifouling/">painting</a> and <a href="/en/services/wooden-boat-refit/">wooden refit</a> services and <a href="/en/boats/gulet/">gulet</a> care. <a href="#teklif-al">Get a quote</a>.</p>
""",
 },
},
{
 "slug": "fiber-tekne-boyama", "slug_en": "fibreglass-boat-painting",
 "image": "/assets/images/services/boya.jpg", "date": "2029-08-02",
 "tr": {
   "category": "Boya",
   "title": "Fiber Tekne Boyama: Gelcoat mı, Boya mı?",
   "excerpt": "Fiber teknede dış cephe yenileme: jelkot parlatma/yenileme mi, komple boya mı? Karar ve süreç.",
   "meta_title": "Fiber Tekne Boyama Rehberi | Tekne Usta",
   "meta_desc": "Fiber tekne boyama: gelcoat yenileme ile boya arasında karar, 2K poliüretan, antifouling ve yüzey hazırlığı. İstanbul ve Ege'de fiber tekne boya servisi.",
   "body": """
<p>Fiber (fiberglas) teknede dış yüzey yıprandığında iki yol vardır: mevcut jelkotu yenilemek ya da profesyonel boya sistemi uygulamak. Doğru karar teknenin durumuna bağlı.</p>
<h2>Jelkot mu, boya mı?</h2>
<p>Jelkot sağlamsa <a href="/blog/gelcoat-yenileme/">parlatma/yenileme</a> ekonomiktir. Renk değişimi veya süperyat parlaklığı için <a href="/blog/2k-poliuretan-boya/">2K poliüretan</a> boya tercih edilir. Karar için <a href="/blog/jelkot-vs-boya/">jelkot mu boya mı</a> yazımıza bakın.</p>
<h2>Yüzey hazırlığı ve antifouling</h2>
<p>Her iki yolda da <a href="/blog/boya-oncesi-yuzey-hazirligi/">yüzey hazırlığı</a> belirleyicidir. Su altında doğru <a href="/blog/antifouling-secimi/">antifouling</a> uygulanır. Maliyet kalemleri için <a href="/blog/tekne-boyama-maliyeti/">boyama maliyeti</a> yazımıza bakın.</p>
<p>Fiber tekne boyama ve antifouling'i <a href="/hizmetler/tekne-boyama-antifouling/">boya</a> hizmetimiz ve <a href="/tekneler/fiber-tekne/">fiber tekne</a> bakım kapsamında yapıyoruz. <a href="#teklif-al">Ücretsiz keşif</a> alın.</p>
""",
 },
 "en": {
   "category": "Painting",
   "title": "Fibreglass Boat Painting: Gelcoat or Paint?",
   "excerpt": "Renewing a fibreglass exterior: gelcoat polish/renewal or a full repaint? The decision and process.",
   "meta_title": "Fibreglass Boat Painting Guide | Tekne Usta",
   "meta_desc": "Fibreglass boat painting: deciding between gelcoat renewal and paint, 2K polyurethane, antifouling and surface prep in Istanbul and the Aegean.",
   "body": """
<p>When a fibreglass exterior wears out, there are two routes: renew the existing gelcoat or apply a professional paint system. The right decision depends on the boat's condition.</p>
<h2>Gelcoat or paint?</h2>
<p>If the gelcoat is sound, <a href="/en/blog/gelcoat-renewal/">polish/renewal</a> is economical. For a colour change or superyacht gloss, <a href="/en/blog/2k-polyurethane-paint/">2K polyurethane</a> paint is preferred. See <a href="/en/blog/gelcoat-vs-paint/">gelcoat or paint</a>.</p>
<h2>Surface prep and antifouling</h2>
<p>In both routes, <a href="/en/blog/surface-prep-before-painting/">surface prep</a> is decisive. Below the waterline the right <a href="/en/blog/choosing-antifouling/">antifouling</a> is applied. For cost items, see <a href="/en/blog/boat-painting-cost/">painting cost</a>.</p>
<p>We do fibreglass boat painting and antifouling under our <a href="/en/services/boat-painting-antifouling/">painting</a> service and <a href="/en/boats/fibreglass-boat/">fibreglass boat</a> care. Get a <a href="#teklif-al">free survey</a>.</p>
""",
 },
},
{
 "slug": "rib-bot-tamiri", "slug_en": "rib-tender-repair",
 "image": "/assets/images/services/fiberglas.jpg", "date": "2029-08-16",
 "tr": {
   "category": "Fiberglas",
   "title": "RIB ve Bot Tamiri: Fiberglas Gövde Onarımı",
   "excerpt": "RIB ve botlarda çarpma, çatlak ve gelcoat onarımı; hızlı ve temiz fiberglas tamir.",
   "meta_title": "RIB ve Bot Tamiri Rehberi | Tekne Usta",
   "meta_desc": "RIB ve bot tamiri: fiberglas gövde çatlak/kırık onarımı, gelcoat yenileme, kaydırmaz güverte ve antifouling. İstanbul ve Ege'de RIB/bot tamir servisi.",
   "body": """
<p>RIB ve botlar günübirlik yoğun kullanıldığından çarpma, çizik ve çatlak sık görülür. Fiberglas gövde onarımını hızlı, temiz ve dayanıklı yapıyoruz.</p>
<h2>Sık yapılan onarımlar</h2>
<ul>
<li><a href="/blog/fiberglas-catlak-onarimi/">Çatlak ve kırık onarımı</a></li>
<li><a href="/blog/gelcoat-cizik-sararma-giderme/">Gelcoat çizik/sararma giderme</a> ve parlatma</li>
<li><a href="/blog/kaydirmaz-guverte-kaplama/">Kaydırmaz güverte</a> yenileme</li>
<li>Su altı <a href="/blog/antifouling-secimi/">antifouling</a></li>
</ul>
<h2>Kapsam</h2>
<p>Fiberglas gövde tarafında tam hizmet veriyoruz; şişme yan tüp (pontoon) onarımı ve motor işleri kapsamımız dışında. Yapısal hasarda <a href="/blog/polyester-vs-epoksi-recine/">doğru reçine</a> ile kalıcı onarım yapılır.</p>
<p>RIB/bot tamirini <a href="/hizmetler/fiberglas-onarim/">fiberglas onarım</a> hizmetimiz ve <a href="/tekneler/rib-bot/">RIB / bot</a> bakım kapsamında yapıyoruz. <a href="#teklif-al">Teklif alın</a>.</p>
""",
 },
 "en": {
   "category": "Fibreglass",
   "title": "RIB and Tender Repair: Fibreglass Hull Repair",
   "excerpt": "Impact, crack and gelcoat repair on RIBs and tenders; fast, clean fibreglass repair.",
   "meta_title": "RIB and Tender Repair Guide | Tekne Usta",
   "meta_desc": "RIB and tender repair: fibreglass hull crack/break repair, gelcoat renewal, non-slip deck and antifouling in Istanbul and the Aegean.",
   "body": """
<p>Because RIBs and tenders are heavily used day boats, impact, scratches and cracks are common. We do fibreglass hull repair fast, clean and durable.</p>
<h2>Common repairs</h2>
<ul>
<li><a href="/en/blog/fibreglass-crack-repair/">Crack and break repair</a></li>
<li><a href="/en/blog/gelcoat-scratch-yellowing/">Gelcoat scratch/yellowing removal</a> and polish</li>
<li><a href="/en/blog/non-slip-deck-coating/">Non-slip deck</a> renewal</li>
<li>Underwater <a href="/en/blog/choosing-antifouling/">antifouling</a></li>
</ul>
<h2>Scope</h2>
<p>We provide full service on the fibreglass hull; inflatable tube (pontoon) repair and engine work are outside our scope. For structural damage, a lasting repair is made with the <a href="/en/blog/polyester-vs-epoxy-resin/">right resin</a>.</p>
<p>We do RIB/tender repair under our <a href="/en/services/fibreglass-repair/">fibreglass repair</a> service and <a href="/en/boats/rib-tender/">RIB / tender</a> care. <a href="#teklif-al">Get a quote</a>.</p>
""",
 },
},
{
 "slug": "surat-teknesi-boyama", "slug_en": "speedboat-painting",
 "image": "/assets/images/services/boya.jpg", "date": "2029-08-30",
 "tr": {
   "category": "Boya",
   "title": "Sürat Teknesi Boyama: Hız İçin Pürüzsüz Karina",
   "excerpt": "Sürat teknelerinde boya, sert antifouling ve gelcoat; performans için doğru sistem.",
   "meta_title": "Sürat Teknesi Boyama Rehberi | Tekne Usta",
   "meta_desc": "Sürat teknesi boyama: dış cephe boya, sert (hard) antifouling, gelcoat ve pasta-polisaj. İstanbul ve Ege'de sürat teknesi boya servisi.",
   "body": """
<p>Sürat teknelerinde karinanın pürüzsüzlüğü doğrudan hız ve yakıt demektir. Doğru boya ve antifouling sistemiyle teknenizi hızlı ve parlak tutuyoruz.</p>
<h2>Hangi antifouling?</h2>
<p>Yüksek hızlı ve sık çekilen teknelerde aşınmayan <strong>sert matris antifouling</strong> daha uygundur; pürüzsüz yüzey performans sağlar. Detay için <a href="/blog/antifouling-secimi/">antifouling seçim rehberine</a> bakın.</p>
<h2>Gelcoat ve parlaklık</h2>
<p>Parlak bir gövde için düzenli <a href="/blog/gelcoat-yenileme/">gelcoat</a> bakımı ve pasta-polisaj öneriyoruz. Renk değişimi veya süperyat parlaklığı için <a href="/blog/2k-poliuretan-boya/">2K poliüretan</a> uygulanır.</p>
<p>Sürat teknesi boyama ve antifouling'i <a href="/hizmetler/tekne-boyama-antifouling/">boya</a> hizmetimiz ve <a href="/tekneler/surat-teknesi/">sürat teknesi</a> bakım kapsamında yapıyoruz. <a href="#teklif-al">Teklif alın</a>.</p>
""",
 },
 "en": {
   "category": "Painting",
   "title": "Speedboat Painting: A Smooth Hull for Speed",
   "excerpt": "Paint, hard antifouling and gelcoat on speedboats; the right system for performance.",
   "meta_title": "Speedboat Painting Guide | Tekne Usta",
   "meta_desc": "Speedboat painting: topside paint, hard antifouling, gelcoat and compound-polish in Istanbul and the Aegean.",
   "body": """
<p>On speedboats, a smooth hull directly means speed and fuel. With the right paint and antifouling system, we keep your boat fast and glossy.</p>
<h2>Which antifouling?</h2>
<p>On fast, frequently hauled boats, non-eroding <strong>hard matrix antifouling</strong> suits better; a smooth surface delivers performance. For detail, see the <a href="/en/blog/choosing-antifouling/">antifouling guide</a>.</p>
<h2>Gelcoat and gloss</h2>
<p>For a glossy hull we recommend regular <a href="/en/blog/gelcoat-renewal/">gelcoat</a> care and compound-polish. For a colour change or superyacht gloss, <a href="/en/blog/2k-polyurethane-paint/">2K polyurethane</a> is applied.</p>
<p>We do speedboat painting and antifouling under our <a href="/en/services/boat-painting-antifouling/">painting</a> service and <a href="/en/boats/speedboat/">speedboat</a> care. <a href="#teklif-al">Get a quote</a>.</p>
""",
 },
},
{
 "slug": "yat-teak-doseme", "slug_en": "yacht-teak-deck",
 "image": "/assets/images/services/ic-mekan.jpg", "date": "2029-09-13",
 "tr": {
   "category": "Teak",
   "title": "Yat Teak Döşeme: Güvertede Prestij ve Güvenlik",
   "excerpt": "Yatlarda teak güverte döşeme, yenileme ve derz onarımı; doğal ve sentetik seçenekler.",
   "meta_title": "Yat Teak Güverte Döşeme Rehberi | Tekne Usta",
   "meta_desc": "Yat teak döşeme: yeni teak güverte, eski teak yenileme, derz onarımı ve doğal/sentetik seçenekler. İstanbul ve Ege'de yat teak güverte servisi.",
   "body": """
<p>Teak güverte, bir yatın en göz alıcı ve prestijli yüzeyidir; aynı zamanda ıslakken güvenli bir yürüyüş alanı sağlar. Yatlarda teak döşeme, yenileme ve derz onarımını titiz işçilikle yapıyoruz.</p>
<h2>Yeni döşeme mi, yenileme mi?</h2>
<p>Teak yeterince kalınsa <a href="/blog/teak-derz-yenileme/">derz yenileme</a> ekonomiktir; inceldiyse komple döşeme gerekir. Karar için <a href="/blog/teak-kalinligi-olcumu/">teak kalınlığı</a> yazımıza bakın.</p>
<h2>Doğal mı, sentetik mi?</h2>
<p>Klasik prestij için doğal teak, bakımsız pratiklik için <a href="/blog/sentetik-teak-alternatifleri/">sentetik teak</a>. Karşılaştırma: <a href="/blog/teak-vs-sentetik-teak/">teak vs sentetik</a>. Fiyat kalemleri için <a href="/blog/teak-guverte-fiyatlari/">teak fiyatları</a>.</p>
<p>Yat teak döşemeyi <a href="/hizmetler/teak-guverte-doseme/">teak güverte döşeme</a> hizmetimiz ve <a href="/tekneler/yat-motoryat/">yat & motoryat</a> bakım kapsamında yapıyoruz. Keşifte teak kalınlığını ölçüp doğru yönlendiririz. <a href="#teklif-al">Teklif alın</a>.</p>
""",
 },
 "en": {
   "category": "Teak",
   "title": "Yacht Teak Decking: Prestige and Safety on Deck",
   "excerpt": "Teak deck laying, renewal and seam repair on yachts; natural and synthetic options.",
   "meta_title": "Yacht Teak Decking Guide | Tekne Usta",
   "meta_desc": "Yacht teak decking: new teak deck, old teak renewal, seam repair and natural/synthetic options in Istanbul and the Aegean.",
   "body": """
<p>A teak deck is a yacht's most eye-catching, prestigious surface, and also a safe walking area when wet. We do teak laying, renewal and seam repair on yachts with meticulous craftsmanship.</p>
<h2>New deck or renewal?</h2>
<p>If the teak is thick enough, <a href="/en/blog/teak-seam-renewal/">seam renewal</a> is economical; if thinned, a full deck is needed. See our <a href="/en/blog/teak-thickness-check/">teak thickness</a> article to decide.</p>
<h2>Natural or synthetic?</h2>
<p>Natural teak for classic prestige, <a href="/en/blog/synthetic-teak-alternatives/">synthetic teak</a> for maintenance-free practicality. Compare: <a href="/en/blog/teak-vs-synthetic-teak/">teak vs synthetic</a>. For price items, <a href="/en/blog/teak-deck-cost/">teak cost</a>.</p>
<p>We do yacht teak decking under our <a href="/en/services/teak-deck/">teak decking</a> service and <a href="/en/boats/yacht-motoryacht/">yacht & motoryacht</a> care. We measure teak thickness at the survey and advise correctly. <a href="#teklif-al">Get a quote</a>.</p>
""",
 },
},
{
 "slug": "yat-detailing", "slug_en": "yacht-detailing",
 "image": "/assets/images/parallax-1.jpg", "date": "2029-09-27",
 "tr": {
   "category": "Bakım",
   "title": "Yat Detailing: Yüzeyi ve Değeri Korumak",
   "excerpt": "Yatlarda iç-dış temizlik, pasta-polisaj ve jelkot koruma; düzenli detailing yatın değerini korur.",
   "meta_title": "Yat Detailing ve Temizlik Rehberi | Tekne Usta",
   "meta_desc": "Yat detailing: dış yüzey yıkama, pasta-polisaj, jelkot/boya koruma, iç mekan temizliği ve sezon paketleri. İstanbul ve Ege'de yat detailing hizmeti.",
   "body": """
<p>Yat detailing sadece estetik değildir; yüzeyi, değeri ve ömrü koruyan en ucuz bakımdır. Düzenli detailing, komple boya veya döşeme yenilemeyi yıllarca erteler.</p>
<h2>Detailing neleri kapsar?</h2>
<ul>
<li>Dış yüzey: <a href="/blog/gelcoat-cizik-sararma-giderme/">pasta-polisaj</a> ve parlaklık</li>
<li>Jelkot/boya koruma: <a href="/blog/uv-koruma-kaplama/">UV'ye karşı wax</a></li>
<li>İç mekan: kabin, döşeme ve <a href="/blog/teknede-kuf-nem-onleme/">nem/küf</a> önlemi</li>
<li>Paslanmaz, cam ve detay bakımı</li>
</ul>
<h2>Sezon paketleri</h2>
<p>Sezon öncesi ve sonrası detailing, yatın hem görünümünü hem piyasa değerini korur. Düzenli bir <a href="/blog/yillik-bakim-anlasmasi/">yıllık bakım anlaşmasıyla</a> öngörülebilir hale getirilebilir.</p>
<p>Yat detailing'i <a href="/hizmetler/tekne-detailing/">temizlik & detailing</a> hizmetimiz ve <a href="/tekneler/yat-motoryat/">yat & motoryat</a> bakım kapsamında yapıyoruz. <a href="#teklif-al">Teklif alın</a>.</p>
""",
 },
 "en": {
   "category": "Maintenance",
   "title": "Yacht Detailing: Protecting Surface and Value",
   "excerpt": "Interior-exterior cleaning, compound-polish and gelcoat protection on yachts; regular detailing protects value.",
   "meta_title": "Yacht Detailing and Cleaning Guide | Tekne Usta",
   "meta_desc": "Yacht detailing: exterior wash, compound-polish, gelcoat/paint protection, interior cleaning and season packages in Istanbul and the Aegean.",
   "body": """
<p>Yacht detailing isn't just cosmetic; it's the cheapest care that protects surface, value and life. Regular detailing postpones a full repaint or re-upholstery for years.</p>
<h2>What does detailing cover?</h2>
<ul>
<li>Exterior: <a href="/en/blog/gelcoat-scratch-yellowing/">compound-polish</a> and gloss</li>
<li>Gelcoat/paint protection: <a href="/en/blog/uv-protection-coating/">wax against UV</a></li>
<li>Interior: cabin, upholstery and <a href="/en/blog/preventing-mould-damp/">damp/mould</a> measures</li>
<li>Stainless, glass and detail care</li>
</ul>
<h2>Season packages</h2>
<p>Pre- and post-season detailing protects both the look and the market value. It can be made predictable with a regular <a href="/en/blog/annual-maintenance-agreement/">annual maintenance agreement</a>.</p>
<p>We do yacht detailing under our <a href="/en/services/boat-detailing/">cleaning & detailing</a> service and <a href="/en/boats/yacht-motoryacht/">yacht & motoryacht</a> care. <a href="#teklif-al">Get a quote</a>.</p>
""",
 },
},
{
 "slug": "yat-ic-mekan-yenileme", "slug_en": "yacht-interior-refit",
 "image": "/assets/images/services/bakim.jpg", "date": "2029-10-11",
 "tr": {
   "category": "İç Mekan",
   "title": "Yat İç Mekan Yenileme: Konfor ve Estetik",
   "excerpt": "Yatlarda döşeme, kabin, mutfak ve aydınlatma yenileme; konforu ve değeri artıran iç mekan.",
   "meta_title": "Yat İç Mekan Yenileme Rehberi | Tekne Usta",
   "meta_desc": "Yat iç mekan yenileme: döşeme ve kumaş, kabin ve mutfak, LED aydınlatma, perde ve nem/küf çözümü. İstanbul ve Ege'de yat iç mekan yenileme hizmeti.",
   "body": """
<p>Yatın iç mekânı, konforun ve değerin kalbidir. Yıpranmış döşeme, eskiyen kabin ve yetersiz aydınlatma yatı olduğundan eski gösterir. İç mekânı baştan ele alıp hem estetiği hem işlevi yeniliyoruz.</p>
<h2>Yat iç mekan hizmetleri</h2>
<ul>
<li><a href="/blog/tekne-doseme-kumas-secimi/">Deniz sınıfı kumaş</a> ve <a href="/blog/minder-sunger-degisimi/">sünger</a> ile döşeme yenileme</li>
<li>Kabin, mutfak (<a href="/blog/tekne-mutfagi-yenileme/">galley</a>) ve dolap yenileme</li>
<li><a href="/blog/kabin-led-aydinlatma/">LED aydınlatma</a> ve <a href="/blog/tekne-perde-stor/">perde/stor</a></li>
<li><a href="/blog/teknede-kuf-nem-onleme/">Nem/küf</a> önlemi</li>
</ul>
<h2>Deniz koşullarına uygun malzeme</h2>
<p>Yatta kullanılan kumaş, sünger ve yüzeyler neme, tuza ve UV'ye dayanıklı olmalı. Doğru malzeme, yenilemenin uzun ömürlü olmasını sağlar.</p>
<p>Yat iç mekan yenilemeyi <a href="/hizmetler/ic-mekan-yenileme/">iç mekan yenileme</a> hizmetimiz ve <a href="/tekneler/yat-motoryat/">yat & motoryat</a> bakım kapsamında yapıyoruz. <a href="#teklif-al">Teklif alın</a>.</p>
""",
 },
 "en": {
   "category": "Interior",
   "title": "Yacht Interior Refit: Comfort and Style",
   "excerpt": "Upholstery, cabin, galley and lighting renewal on yachts; an interior that raises comfort and value.",
   "meta_title": "Yacht Interior Refit Guide | Tekne Usta",
   "meta_desc": "Yacht interior refit: upholstery and fabric, cabin and galley, LED lighting, curtains and damp/mould solutions in Istanbul and the Aegean.",
   "body": """
<p>A yacht's interior is the heart of comfort and value. Worn upholstery, a tired cabin and poor lighting make a yacht look older than it is. We take the interior in hand and renew both looks and function.</p>
<h2>Yacht interior services</h2>
<ul>
<li>Upholstery renewal with <a href="/en/blog/marine-upholstery-fabric/">marine-grade fabric</a> and <a href="/en/blog/cushion-foam-replacement/">foam</a></li>
<li>Cabin, galley (<a href="/en/blog/galley-refit/">galley</a>) and cabinetry renewal</li>
<li><a href="/en/blog/cabin-led-lighting/">LED lighting</a> and <a href="/en/blog/boat-curtains-blinds/">curtains/blinds</a></li>
<li><a href="/en/blog/preventing-mould-damp/">Damp/mould</a> measures</li>
</ul>
<h2>Materials for marine conditions</h2>
<p>Fabric, foam and surfaces used on a yacht must resist damp, salt and UV. The right materials make the refit last.</p>
<p>We do yacht interior refit under our <a href="/en/services/interior-refit/">interior refit</a> service and <a href="/en/boats/yacht-motoryacht/">yacht & motoryacht</a> care. <a href="#teklif-al">Get a quote</a>.</p>
""",
 },
},
{
 "slug": "yelkenli-boyama", "slug_en": "sailboat-painting",
 "image": "/assets/images/services/boya.jpg", "date": "2029-10-25",
 "tr": {
   "category": "Boya",
   "title": "Yelkenli Boyama: Dış Cephe ve Antifouling",
   "excerpt": "Yelkenlilerde dış cephe boyama, antifouling ve gelcoat; doğru sistemle uzun ömürlü bitiş.",
   "meta_title": "Yelkenli Boyama Rehberi | Tekne Usta",
   "meta_desc": "Yelkenli boyama: dış cephe boya, antifouling, gelcoat ve yüzey hazırlığı. İstanbul ve Ege'de yelkenli boya ve antifouling servisi.",
   "body": """
<p>Yelkenli boyama, hem estetik hem koruma açısından önemli bir iştir. Dış cephe, kılavuz şerit ve su altı antifouling'i doğru sistemle uzun ömürlü yapıyoruz.</p>
<h2>Dış cephe ve antifouling</h2>
<p>Dış cephede kalıcı parlaklık için <a href="/blog/2k-poliuretan-boya/">2K poliüretan</a>, su altında yelkenlinin kullanımına uygun <a href="/blog/antifouling-secimi/">antifouling</a> seçilir. Yüzey sağlamsa <a href="/blog/gelcoat-yenileme/">gelcoat yenileme</a> de bir seçenektir.</p>
<h2>Yüzey hazırlığı</h2>
<p>Kalıcı bir bitişin sırrı <a href="/blog/boya-oncesi-yuzey-hazirligi/">yüzey hazırlığındadır</a>: doğru zımpara, dolgu ve astar. Maliyet kalemleri için <a href="/blog/tekne-boyama-maliyeti/">boyama maliyeti</a> yazımıza bakın.</p>
<p>Yelkenli boyama ve antifouling'i <a href="/hizmetler/tekne-boyama-antifouling/">boya</a> hizmetimiz ve <a href="/tekneler/yelkenli/">yelkenli</a> bakım kapsamında yapıyoruz. <a href="#teklif-al">Teklif alın</a>.</p>
""",
 },
 "en": {
   "category": "Painting",
   "title": "Sailboat Painting: Topside and Antifouling",
   "excerpt": "Topside painting, antifouling and gelcoat on sailboats; a long-lasting finish with the right system.",
   "meta_title": "Sailboat Painting Guide | Tekne Usta",
   "meta_desc": "Sailboat painting: topside paint, antifouling, gelcoat and surface prep. Sailboat paint and antifouling service in Istanbul and the Aegean.",
   "body": """
<p>Sailboat painting matters for both looks and protection. We do topside, boot stripe and underwater antifouling with the right system for a long-lasting finish.</p>
<h2>Topside and antifouling</h2>
<p>For lasting topside gloss, <a href="/en/blog/2k-polyurethane-paint/">2K polyurethane</a>; below the waterline, an <a href="/en/blog/choosing-antifouling/">antifouling</a> suited to the sailboat's use. If the surface is sound, <a href="/en/blog/gelcoat-renewal/">gelcoat renewal</a> is also an option.</p>
<h2>Surface prep</h2>
<p>The secret to a lasting finish is in <a href="/en/blog/surface-prep-before-painting/">surface prep</a>: correct sanding, filling and primer. For cost items, see <a href="/en/blog/boat-painting-cost/">painting cost</a>.</p>
<p>We do sailboat painting and antifouling under our <a href="/en/services/boat-painting-antifouling/">painting</a> service and <a href="/en/boats/sailboat/">sailboat</a> care. <a href="#teklif-al">Get a quote</a>.</p>
""",
 },
},
{
 "slug": "gulet-ic-mekan", "slug_en": "gulet-interior-refit",
 "image": "/assets/images/services/bakim.jpg", "date": "2029-11-08",
 "tr": {
   "category": "İç Mekan",
   "title": "Gulet İç Mekan Yenileme: Kabin, Salon ve Döşeme",
   "excerpt": "Guletlerde kabin, salon, mutfak ve döşeme yenileme; konaklamalı kullanıma uygun dayanıklı iç mekan.",
   "meta_title": "Gulet İç Mekan Yenileme Rehberi | Tekne Usta",
   "meta_desc": "Gulet iç mekan yenileme: kabin ve salon, döşeme ve kumaş, mutfak, aydınlatma ve nem/küf çözümü. Ege'de gulet iç mekan yenileme hizmeti.",
   "body": """
<p>Guletler konaklamalı ve çoğu zaman ticari kullanıldığından iç mekan hem konforlu hem dayanıklı olmalı. Kabin, salon, mutfak ve döşemeyi yoğun kullanıma uygun malzemelerle yeniliyoruz.</p>
<h2>Gulet iç mekan hizmetleri</h2>
<ul>
<li>Kabin ve salon döşeme, <a href="/blog/tekne-doseme-kumas-secimi/">deniz sınıfı kumaş</a> ve <a href="/blog/minder-sunger-degisimi/">sünger</a></li>
<li>Mutfak (<a href="/blog/tekne-mutfagi-yenileme/">galley</a>) ve dolap yenileme</li>
<li><a href="/blog/kabin-led-aydinlatma/">Aydınlatma</a> ve <a href="/blog/tekne-perde-stor/">perde</a></li>
<li><a href="/blog/teknede-kuf-nem-onleme/">Nem/küf</a> önlemi (çok kabinli guletlerde kritik)</li>
</ul>
<h2>Dayanıklılık önceliği</h2>
<p>Misafir kullanan guletlerde döşeme çok yıpranır; lekeye ve aşınmaya dayanıklı, kolay temizlenen malzemeler tercih edilir.</p>
<p>Gulet iç mekan yenilemeyi <a href="/hizmetler/ic-mekan-yenileme/">iç mekan yenileme</a> hizmetimiz ve <a href="/tekneler/gulet/">gulet</a> bakım kapsamında yapıyoruz. <a href="#teklif-al">Teklif alın</a>.</p>
""",
 },
 "en": {
   "category": "Interior",
   "title": "Gulet Interior Refit: Cabins, Saloon and Upholstery",
   "excerpt": "Cabin, saloon, galley and upholstery renewal on gulets; a durable interior for overnight use.",
   "meta_title": "Gulet Interior Refit Guide | Tekne Usta",
   "meta_desc": "Gulet interior refit: cabins and saloon, upholstery and fabric, galley, lighting and damp/mould solutions. Gulet interior refit in the Aegean.",
   "body": """
<p>Because gulets are used for overnight stays and often commercially, the interior must be both comfortable and durable. We renew cabins, saloon, galley and upholstery with materials suited to heavy use.</p>
<h2>Gulet interior services</h2>
<ul>
<li>Cabin and saloon upholstery, <a href="/en/blog/marine-upholstery-fabric/">marine-grade fabric</a> and <a href="/en/blog/cushion-foam-replacement/">foam</a></li>
<li>Galley (<a href="/en/blog/galley-refit/">galley</a>) and cabinetry renewal</li>
<li><a href="/en/blog/cabin-led-lighting/">Lighting</a> and <a href="/en/blog/boat-curtains-blinds/">curtains</a></li>
<li><a href="/en/blog/preventing-mould-damp/">Damp/mould</a> measures (critical on multi-cabin gulets)</li>
</ul>
<h2>Durability first</h2>
<p>On guest-carrying gulets the upholstery wears heavily; stain- and wear-resistant, easy-clean materials are preferred.</p>
<p>We do gulet interior refit under our <a href="/en/services/interior-refit/">interior refit</a> service and <a href="/en/boats/gulet/">gulet</a> care. <a href="#teklif-al">Get a quote</a>.</p>
""",
 },
},
{
 "slug": "fiber-tekne-kislatma", "slug_en": "fibreglass-boat-winterising",
 "image": "/assets/images/services/bakim.jpg", "date": "2029-11-22",
 "tr": {
   "category": "Bakım",
   "title": "Fiber Tekne Kışlatma: Osmoz Riskini Azaltmak",
   "excerpt": "Fiber tekneyi kışlatmak: karaya çekme, karina kurutma, örtü ve osmozdan korunma.",
   "meta_title": "Fiber Tekne Kışlatma Rehberi | Tekne Usta",
   "meta_desc": "Fiber tekne kışlatma: karaya çekme, karina temizliği ve kurutma, havalandırmalı örtü ve osmozdan korunma. İstanbul ve Ege'de fiber tekne kışlatma hizmeti.",
   "body": """
<p>Fiber teknede kışlatmanın en önemli faydalarından biri karinanın kurumasına izin vererek <a href="/blog/osmozdan-korunma/">osmoz riskini</a> azaltmasıdır. İyi kışlatılmış bir fiber tekne sezona sorunsuz başlar.</p>
<h2>Kışlatma kapsamı</h2>
<ul>
<li><a href="/blog/tekne-cekek-karaya-cekme/">Karaya çekme</a> ve basınçlı yıkama</li>
<li>Karina, <a href="/blog/osmoz-belirtileri/">osmoz</a> ve <a href="/blog/anot-zinc-bakimi/">anot</a> kontrolü</li>
<li>İç mekan havalandırması, <a href="/blog/teknede-kuf-nem-onleme/">nem/küf</a> önlemi</li>
<li><a href="/blog/tekne-ortusu-secimi/">Havalandırmalı örtü</a> ve depolama</li>
</ul>
<h2>Neden karada?</h2>
<p>Sürekli suda kalan fiber teknede laminat nemi artar. Karada kışlatmak nemi düşürür ve karina bakımını kolaylaştırır. <a href="/blog/kisin-tekne-nerede-saklanir/">Depolama seçenekleri</a> için ayrı yazımıza bakın.</p>
<p>Fiber tekne kışlatmayı <a href="/hizmetler/tekne-kislatma/">kışlatma</a> hizmetimiz ve <a href="/tekneler/fiber-tekne/">fiber tekne</a> bakım kapsamında yapıyoruz. <a href="#teklif-al">Erken rezervasyon</a> için bize yazın.</p>
""",
 },
 "en": {
   "category": "Maintenance",
   "title": "Fibreglass Boat Winterising: Lowering Osmosis Risk",
   "excerpt": "Winterising a fibreglass boat: haul-out, hull drying, cover and osmosis prevention.",
   "meta_title": "Fibreglass Boat Winterising Guide | Tekne Usta",
   "meta_desc": "Fibreglass boat winterising: haul-out, hull cleaning and drying, ventilated cover and osmosis prevention in Istanbul and the Aegean.",
   "body": """
<p>One of the key benefits of winterising a fibreglass boat is letting the hull dry, lowering <a href="/en/blog/osmosis-prevention/">osmosis risk</a>. A well-winterised fibreglass boat starts the season trouble-free.</p>
<h2>Scope of winterising</h2>
<ul>
<li><a href="/en/blog/boat-haul-out-guide/">Haul-out</a> and pressure wash</li>
<li>Hull, <a href="/en/blog/osmosis-symptoms/">osmosis</a> and <a href="/en/blog/anode-zinc-care/">anode</a> checks</li>
<li>Interior ventilation, <a href="/en/blog/preventing-mould-damp/">damp/mould</a> measures</li>
<li><a href="/en/blog/boat-cover-selection/">Ventilated cover</a> and storage</li>
</ul>
<h2>Why ashore?</h2>
<p>On a fibreglass boat kept constantly afloat, laminate moisture rises. Winterising ashore lowers moisture and eases hull care. See our separate article on <a href="/en/blog/winter-boat-storage/">storage options</a>.</p>
<p>We do fibreglass boat winterising under our <a href="/en/services/winterising-storage/">winterising</a> service and <a href="/en/boats/fibreglass-boat/">fibreglass boat</a> care. Message us to <a href="#teklif-al">book early</a>.</p>
""",
 },
},
{
 "slug": "aluminyum-tekne-antifouling", "slug_en": "aluminium-boat-antifouling",
 "image": "/assets/images/services/boya.jpg", "date": "2029-12-06",
 "tr": {
   "category": "Boya",
   "title": "Alüminyum Tekne Antifouling: Bakırsız Sistem Şart",
   "excerpt": "Alüminyum teknelerde neden bakırsız antifouling gerekir? Korozyon riski ve doğru sistem.",
   "meta_title": "Alüminyum Tekne Antifouling Rehberi | Tekne Usta",
   "meta_desc": "Alüminyum tekne antifouling: bakırsız (copper-free) boya, galvanik korozyon riski, doğru astar sistemi ve uygulama. İstanbul ve Ege'de alüminyum tekne servisi.",
   "body": """
<p>Alüminyum teknelerde antifouling seçimi, fiber ve ahşap teknelerden farklı ve kritik bir konudur. Yanlış boya galvanik korozyona yol açar; bu yüzden mutlaka <strong>bakırsız</strong> sistem kullanılır.</p>
<h2>Neden bakırsız?</h2>
<p>Bakır içeren antifouling, alüminyumla temas ettiğinde <a href="/blog/anot-zinc-bakimi/">galvanik korozyonu</a> tetikler ve gövdeye ciddi zarar verir. Alüminyumda yalnızca <strong>bakır içermeyen</strong> formüller güvenlidir.</p>
<h2>Doğru astar sistemi</h2>
<p>Alüminyumda boyanın tutunması ve metalin korunması için özel (genelde epoksi) <a href="/blog/astar-primer-nedir/">astar sistemi</a> gerekir. Yüzey hazırlığı da fiberden daha belirleyicidir (bkz. <a href="/blog/aluminyum-tekne-boyama/">alüminyum tekne boyama</a>).</p>
<p>Alüminyum tekne antifouling'i <a href="/hizmetler/tekne-boyama-antifouling/">boya</a> hizmetimiz ve <a href="/tekneler/aluminyum-tekne/">alüminyum tekne</a> bakım kapsamında yapıyoruz. <em>Not: alüminyum kaynak/yapısal işler kapsamımız dışındadır.</em> <a href="#teklif-al">Teklif alın</a>.</p>
""",
 },
 "en": {
   "category": "Painting",
   "title": "Aluminium Boat Antifouling: Copper-Free Is Essential",
   "excerpt": "Why do aluminium boats need copper-free antifouling? Corrosion risk and the right system.",
   "meta_title": "Aluminium Boat Antifouling Guide | Tekne Usta",
   "meta_desc": "Aluminium boat antifouling: copper-free paint, galvanic corrosion risk, the right primer system and application in Istanbul and the Aegean.",
   "body": """
<p>Antifouling choice on aluminium boats is a different and critical matter than on fibreglass and wood. The wrong paint causes galvanic corrosion; so a <strong>copper-free</strong> system is essential.</p>
<h2>Why copper-free?</h2>
<p>Copper-based antifouling in contact with aluminium triggers <a href="/en/blog/anode-zinc-care/">galvanic corrosion</a> and seriously damages the hull. On aluminium, only <strong>copper-free</strong> formulas are safe.</p>
<h2>The right primer system</h2>
<p>Aluminium needs a special (usually epoxy) <a href="/en/blog/primer-importance/">primer system</a> for adhesion and metal protection. Surface prep is even more decisive than on fibreglass (see <a href="/en/blog/aluminium-boat-painting/">aluminium boat painting</a>).</p>
<p>We do aluminium boat antifouling under our <a href="/en/services/boat-painting-antifouling/">painting</a> service and <a href="/en/boats/aluminium-boat/">aluminium boat</a> care. <em>Note: aluminium welding/structural work is outside our scope.</em> <a href="#teklif-al">Get a quote</a>.</p>
""",
 },
},
{
 "slug": "yat-bakimi", "slug_en": "yacht-maintenance",
 "image": "/assets/images/parallax-1.jpg", "date": "2030-01-10",
 "tr": {
   "category": "Bakım",
   "title": "Yat Bakımı: Değerini ve Konforunu Koruyan Servis",
   "excerpt": "Yat bakımı neleri kapsar? Karina, gelcoat, teak, iç mekan ve sezonluk kontroller — tek elden.",
   "meta_title": "Yat Bakımı ve Servisi: Kapsam ve Sıklık | Tekne Usta",
   "meta_desc": "Yat bakımı ve servisi: karina-antifouling, gelcoat, teak, iç mekan ve sezonluk kontroller. İstanbul ve Ege'de tek elden yat bakım hizmeti.",
   "body": """
<p>Yat bakımı, teknenin hem değerini hem de kullanım konforunu korumanın en ekonomik yoludur. Küçük sorunlar zamanında görülürse büyük onarımlara dönüşmez. Biz motor ve mekanik dışında; gövde, yüzey, ahşap ve iç mekan tarafında tek elden servis veriyoruz.</p>
<h2>Yat bakımı neleri kapsar?</h2>
<p>Kapsamlı bir yat bakımı; su altında <a href="/blog/antifouling-secimi/">antifouling</a> ve <a href="/blog/anot-zinc-bakimi/">anot</a> kontrolü, gövdede <a href="/blog/gelcoat-yenileme/">gelcoat</a> ve boya bakımı, <a href="/blog/teak-guverte-bakimi/">teak güverte</a> temizliği, iç mekanda nem/küf kontrolü ve genel <a href="/hizmetler/tekne-detailing/">detailing</a> içerir.</p>
<h2>Ne sıklıkla?</h2>
<p>Yatlarda yıllık bir bakım programı idealdir; sezon açılışı ve kapanışı iki doğal kontrol noktasıdır. Detaylı takvim için <a href="/blog/yillik-tekne-bakim-takvimi/">yıllık bakım takvimi</a> yazımıza bakın; düzenli müşteriler için <a href="/blog/yillik-bakim-anlasmasi/">yıllık bakım anlaşması</a> da sunuyoruz.</p>
<h2>Neden tek elden?</h2>
<p>Boya, teak, gelcoat ve iç mekan farklı ustalık ister; bunları tek bir sorumluyla yürütmek hem kaliteyi hem takibi kolaylaştırır. Çok kalemli işleri <a href="/blog/refit-proje-yonetimi/">proje yönetimiyle</a> koordine ederiz.</p>
<p>Yatınızın bakımını <a href="/tekneler/yat-motoryat/">yat & motoryat</a> kapsamında yapıyoruz. <a href="/#bolgeler">İstanbul ve Ege</a>'de <a href="#teklif-al">ücretsiz keşif</a> alın.</p>
""",
 },
 "en": {
   "category": "Maintenance",
   "title": "Yacht Maintenance: Service That Protects Value and Comfort",
   "excerpt": "What does yacht maintenance cover? Underbody, gelcoat, teak, interior and seasonal checks — from one hand.",
   "meta_title": "Yacht Maintenance and Service: Scope and Frequency | Tekne Usta",
   "meta_desc": "Yacht maintenance and service: underbody-antifouling, gelcoat, teak, interior and seasonal checks. Single-hand yacht care in Istanbul and the Aegean.",
   "body": """
<p>Yacht maintenance is the most economical way to protect both the value and the comfort of a boat. Small problems caught in time don't turn into big repairs. Apart from engine and mechanics, we provide single-hand service on hull, surface, wood and interior.</p>
<h2>What does yacht maintenance cover?</h2>
<p>Comprehensive yacht maintenance includes underwater <a href="/en/blog/choosing-antifouling/">antifouling</a> and <a href="/en/blog/anode-zinc-care/">anode</a> checks, <a href="/en/blog/gelcoat-renewal/">gelcoat</a> and paint care on the hull, <a href="/en/blog/teak-deck-maintenance/">teak deck</a> cleaning, damp/mould checks in the interior and general <a href="/en/services/boat-detailing/">detailing</a>.</p>
<h2>How often?</h2>
<p>An annual programme is ideal for yachts; season opening and closing are two natural checkpoints. For a detailed calendar, see our <a href="/en/blog/annual-boat-maintenance-calendar/">annual maintenance calendar</a>; for regular clients we also offer an <a href="/en/blog/annual-maintenance-agreement/">annual maintenance agreement</a>.</p>
<h2>Why from one hand?</h2>
<p>Paint, teak, gelcoat and interior each require different craft; running them under one lead makes both quality and tracking easier. We coordinate multi-item work with <a href="/en/blog/refit-project-management/">project management</a>.</p>
<p>We maintain your yacht under <a href="/en/boats/yacht-motoryacht/">yacht & motoryacht</a> care. Get a <a href="#teklif-al">free survey</a> in <a href="/en/#bolgeler">Istanbul and the Aegean</a>.</p>
""",
 },
},
{
 "slug": "yat-refit", "slug_en": "yacht-refit",
 "image": "/assets/images/parallax-2.jpg", "date": "2030-01-13",
 "tr": {
   "category": "Renovasyon",
   "title": "Yat Refit: Kapsamlı Yenileme Nasıl Planlanır?",
   "excerpt": "Yat refit nedir, ne zaman gerekir? Boya, teak, iç mekan ve gövde yenilemesini tek projede toplamak.",
   "meta_title": "Yat Refit Rehberi: Kapsam, Süreç, Planlama | Tekne Usta",
   "meta_desc": "Yat refit: boya, teak, iç mekan ve gövde yenilemesini tek projede planlama. Kapsam, sıralama ve maliyet mantığı. İstanbul ve Ege'de yat refit.",
   "body": """
<p>Refit, bir yatın birden çok kaleminin (boya, teak, iç mekan, gövde) planlı bir projede birlikte yenilenmesidir. Tek tek yapılan işlere göre hem daha ekonomik hem de daha tutarlı bir sonuç verir; tekne bir kez çekilir, tüm işler koordine edilir.</p>
<h2>Yat refit ne zaman gerekir?</h2>
<p>Genelde 10+ yaşındaki yatlarda, ikinci el alım sonrası ya da uzun bir kullanım döneminden sonra düşünülür. <a href="/blog/satin-alma-oncesi-tekne-ekspertizi/">Ekspertiz</a> raporu, hangi kalemlerin öncelikli olduğunu netleştirir.</p>
<h2>Refit kapsamına neler girer?</h2>
<p>Sık kalemler: dış cephe <a href="/hizmetler/tekne-boyama-antifouling/">boya</a> ve renk değişimi, <a href="/hizmetler/teak-guverte-doseme/">teak güverte</a> yenileme, <a href="/hizmetler/ic-mekan-yenileme/">iç mekan</a> döşeme/mobilya, <a href="/blog/gelcoat-cizik-sararma-giderme/">gelcoat</a> restorasyonu. Motor ve mekanik işler kapsamımız dışındadır.</p>
<h2>Sıralama ve planlama</h2>
<p>Refit'te sıra önemlidir; yapısal ve boya işleri döşemeden önce gelir. Biz işi kalem kalem, <a href="/blog/refit-proje-yonetimi/">proje yönetimiyle</a> planlıyor, her adımın süresini ve maliyetini şeffaf veriyoruz.</p>
<p>Yat refit'i <a href="/tekneler/yat-motoryat/">yat & motoryat</a> kapsamında yürütüyoruz. <a href="#teklif-al">Ücretsiz keşif</a> ile başlayalım.</p>
""",
 },
 "en": {
   "category": "Renovation",
   "title": "Yacht Refit: How to Plan a Comprehensive Renewal",
   "excerpt": "What is a yacht refit and when is it needed? Bringing paint, teak, interior and hull work into one project.",
   "meta_title": "Yacht Refit Guide: Scope, Process, Planning | Tekne Usta",
   "meta_desc": "Yacht refit: planning paint, teak, interior and hull renewal in one project. Scope, sequencing and cost logic. Yacht refit in Istanbul and the Aegean.",
   "body": """
<p>A refit is the planned, combined renewal of several items on a yacht (paint, teak, interior, hull). Compared with piecemeal work it is both more economical and more consistent; the boat is hauled once and all work is coordinated.</p>
<h2>When is a yacht refit needed?</h2>
<p>It's usually considered on yachts 10+ years old, after a used purchase, or after a long period of use. A <a href="/en/blog/pre-purchase-boat-survey/">survey</a> report clarifies which items are priority.</p>
<h2>What's included in a refit?</h2>
<p>Common items: topside <a href="/en/services/boat-painting-antifouling/">paint</a> and colour change, <a href="/en/services/teak-deck/">teak deck</a> renewal, <a href="/en/services/interior-refit/">interior</a> upholstery/joinery, <a href="/en/blog/gelcoat-scratch-yellowing/">gelcoat</a> restoration. Engine and mechanical work are outside our scope.</p>
<h2>Sequencing and planning</h2>
<p>Order matters in a refit; structural and paint work come before upholstery. We plan item by item with <a href="/en/blog/refit-project-management/">project management</a>, giving the duration and cost of each step transparently.</p>
<p>We run yacht refits under <a href="/en/boats/yacht-motoryacht/">yacht & motoryacht</a> care. Let's start with a <a href="#teklif-al">free survey</a>.</p>
""",
 },
},
{
 "slug": "motoryat-bakimi", "slug_en": "motoryacht-maintenance",
 "image": "/assets/images/parallax-3.jpg", "date": "2030-01-16",
 "tr": {
   "category": "Bakım",
   "title": "Motoryat Bakımı: Geniş Yüzey, Yüksek Beklenti",
   "excerpt": "Motoryat bakımında öncelikler: geniş gelcoat yüzeyi, karina, swim platform ve detailing.",
   "meta_title": "Motoryat Bakımı ve Servisi Rehberi | Tekne Usta",
   "meta_desc": "Motoryat bakımı: geniş gelcoat yüzeyi, karina-antifouling, swim platform teak'i ve detailing. İstanbul ve Ege'de motoryat servisi.",
   "body": """
<p>Motoryatlar genelde geniş fiberglas yüzeye ve yüksek görünürlüğe sahiptir; bu yüzden yüzey bakımı ve parlaklık, algılanan kaliteyi doğrudan belirler. Motor ve mekanik dışında; gövde, yüzey ve iç mekan tarafında servis veriyoruz.</p>
<h2>Öncelikli kalemler</h2>
<p>Geniş <a href="/blog/gelcoat-yenileme/">gelcoat</a> yüzeyi düzenli cila ve <a href="/blog/uv-koruma-kaplama/">UV koruma</a> ister; su altında <a href="/blog/antifouling-secimi/">antifouling</a> ve <a href="/blog/anot-zinc-bakimi/">anot</a> takibi gerekir. Swim platform ve güvertedeki <a href="/hizmetler/teak-guverte-doseme/">teak</a> ayrı bir bakım kalemidir.</p>
<h2>Detailing farkı</h2>
<p>Motoryatta bitiş kalitesi fark yaratır; profesyonel <a href="/hizmetler/tekne-detailing/">detailing</a>, <a href="/blog/kekamoz-temizligi/">kireç/kekamoz temizliği</a> ve cila ile gövde ilk günkü görünümüne yaklaşır.</p>
<h2>Sezonluk kontrol</h2>
<p>Sezon açılış-kapanışında bir kontrol, küçük sorunları büyümeden yakalar. <a href="/blog/yillik-tekne-bakim-takvimi/">Yıllık takvim</a> ile planlıyoruz.</p>
<p>Motoryat bakımını <a href="/tekneler/yat-motoryat/">yat & motoryat</a> kapsamında yapıyoruz. <a href="#teklif-al">Ücretsiz keşif</a> alın.</p>
""",
 },
 "en": {
   "category": "Maintenance",
   "title": "Motoryacht Maintenance: Large Surface, High Expectations",
   "excerpt": "Priorities in motoryacht care: large gelcoat surface, underbody, swim platform and detailing.",
   "meta_title": "Motoryacht Maintenance and Service Guide | Tekne Usta",
   "meta_desc": "Motoryacht maintenance: large gelcoat surface, underbody-antifouling, swim platform teak and detailing. Motoryacht service in Istanbul and the Aegean.",
   "body": """
<p>Motoryachts usually have a large fibreglass surface and high visibility; so surface care and gloss directly set the perceived quality. Apart from engine and mechanics, we serve the hull, surface and interior.</p>
<h2>Priority items</h2>
<p>A large <a href="/en/blog/gelcoat-renewal/">gelcoat</a> surface needs regular polish and <a href="/en/blog/uv-protection-coating/">UV protection</a>; below the waterline, <a href="/en/blog/choosing-antifouling/">antifouling</a> and <a href="/en/blog/anode-zinc-care/">anode</a> monitoring are needed. Teak on the swim platform and deck is a separate care item (<a href="/en/services/teak-deck/">teak decking</a>).</p>
<h2>The detailing difference</h2>
<p>On a motoryacht, finish quality makes the difference; professional <a href="/en/services/boat-detailing/">detailing</a>, <a href="/en/blog/hull-limescale-cleaning/">limescale cleaning</a> and polish bring the hull close to day-one condition.</p>
<h2>Seasonal check</h2>
<p>A check at season open and close catches small problems before they grow. We plan it with an <a href="/en/blog/annual-boat-maintenance-calendar/">annual calendar</a>.</p>
<p>We maintain motoryachts under <a href="/en/boats/yacht-motoryacht/">yacht & motoryacht</a> care. Get a <a href="#teklif-al">free survey</a>.</p>
""",
 },
},
{
 "slug": "yelkenli-bakimi", "slug_en": "sailboat-maintenance",
 "image": "/assets/images/parallax-2.jpg", "date": "2030-01-19",
 "tr": {
   "category": "Bakım",
   "title": "Yelkenli Bakımı: Karina, Osmoz ve İç Mekan",
   "excerpt": "Yelkenli bakımında kapsamımız: karina, osmoz takibi, teak ve iç mekan. Direk/arma ve motor hariç.",
   "meta_title": "Yelkenli Tekne Bakımı ve Tamiri Rehberi | Tekne Usta",
   "meta_desc": "Yelkenli bakımı ve tamiri: karina-antifouling, osmoz takibi, gelcoat, teak ve iç mekan. Direk/arma ve motor hariç. İstanbul ve Ege'de yelkenli servisi.",
   "body": """
<p>Yelkenliler çoğunlukla uzun süre suda kalır; bu da karina, osmoz ve yüzey bakımını öne çıkarır. Kapsamımız gövde, yüzey, teak ve iç mekandır; direk/arma ve motor işleri bizim dışımızdadır.</p>
<h2>Karina ve osmoz</h2>
<p>Uzun süre suda kalan yelkenlilerde <a href="/blog/osmoz-belirtileri/">osmoz belirtilerini</a> düzenli izlemek önemlidir; erken tedavi maliyeti düşürür (bkz. <a href="/blog/osmoz-nedir-tedavisi/">osmoz tedavisi</a>). Karina <a href="/blog/antifouling-secimi/">antifouling</a> ve <a href="/blog/robotik-karina-temizligi/">temizliği</a> yıllık kalemdir.</p>
<h2>Yüzey ve teak</h2>
<p>Gövdede <a href="/blog/gelcoat-yenileme/">gelcoat</a> bakımı, güvertede <a href="/hizmetler/teak-guverte-doseme/">teak</a> temizliği yapılır. İç mekanda nem ve küf kontrolü, uzun demirlemelerde kritiktir.</p>
<h2>Neyi yapmıyoruz?</h2>
<p>Direk, arma, yelken ve motor işleri uzmanlık alanımız değildir; bu kalemleri dürüstçe yönlendiririz. Gövde, boya, teak ve iç mekan tarafında ise tam hizmet veririz.</p>
<p>Yelkenli bakımını <a href="/tekneler/yelkenli/">yelkenli</a> kapsamında yapıyoruz. <a href="#teklif-al">Ücretsiz keşif</a> alın.</p>
""",
 },
 "en": {
   "category": "Maintenance",
   "title": "Sailboat Maintenance: Underbody, Osmosis and Interior",
   "excerpt": "Our scope in sailboat care: underbody, osmosis monitoring, teak and interior. Mast/rigging and engine excluded.",
   "meta_title": "Sailboat Maintenance and Repair Guide | Tekne Usta",
   "meta_desc": "Sailboat maintenance and repair: underbody-antifouling, osmosis monitoring, gelcoat, teak and interior. Mast/rigging and engine excluded. Sailboat service in Istanbul and the Aegean.",
   "body": """
<p>Sailboats often stay afloat for long periods, which brings underbody, osmosis and surface care to the fore. Our scope is hull, surface, teak and interior; mast/rigging and engine work are outside us.</p>
<h2>Underbody and osmosis</h2>
<p>On sailboats kept long afloat, regularly monitoring <a href="/en/blog/osmosis-symptoms/">osmosis symptoms</a> matters; early treatment lowers cost (see <a href="/en/blog/what-is-osmosis-treatment/">osmosis treatment</a>). Underbody <a href="/en/blog/choosing-antifouling/">antifouling</a> and <a href="/en/blog/robotic-hull-cleaning/">cleaning</a> are annual items.</p>
<h2>Surface and teak</h2>
<p><a href="/en/blog/gelcoat-renewal/">Gelcoat</a> care on the hull and <a href="/en/services/teak-deck/">teak</a> cleaning on deck are done. Damp and mould control in the interior is critical on long moorings.</p>
<h2>What we don't do</h2>
<p>Mast, rigging, sails and engine are not our expertise; we refer these items honestly. On hull, paint, teak and interior we provide full service.</p>
<p>We maintain sailboats under <a href="/en/boats/sailboat/">sailboat</a> care. Get a <a href="#teklif-al">free survey</a>.</p>
""",
 },
},
{
 "slug": "gulet-bakimi", "slug_en": "gulet-maintenance",
 "image": "/assets/images/services/ahsap.jpg", "date": "2030-01-22",
 "tr": {
   "category": "Bakım",
   "title": "Gulet Bakımı: Ticari Kullanıma Hazır Tutmak",
   "excerpt": "Gulet bakımı neden farklıdır? Ahşap gövde, kalafat, teak ve sezon öncesi hazırlık.",
   "meta_title": "Gulet Bakımı Rehberi: Kapsam ve Sezon Hazırlığı | Tekne Usta",
   "meta_desc": "Gulet bakımı: ahşap gövde bakımı, kalafat kontrolü, teak güverte, vernik ve sezon öncesi hazırlık. Ege ve İstanbul'da gulet servisi.",
   "body": """
<p>Guletler çoğunlukla ticari kullanılır; sezon içinde aksama, doğrudan gelir kaybıdır. Bu yüzden gulet bakımının kalbi, sezon öncesi kapsamlı bir hazırlıktır. Ahşap ve karma gövde guletlerde bu işi geleneksel ustalıkla yapıyoruz.</p>
<h2>Ahşap gövde ve kalafat</h2>
<p>Ahşap guletlerde <a href="/blog/kalafat-nedir/">kalafat</a> derzlerinin ve <a href="/blog/ahsap-tekne-vernik-bakimi/">verniğin</a> düzenli kontrolü şarttır; küçük açılmalar su almaya dönüşmeden çözülmeli (bkz. <a href="/blog/ustupu-kalafat-teknikleri/">üstüpü/kalafat teknikleri</a>).</p>
<h2>Teak ve güverte</h2>
<p>Yoğun ayak trafiği gören <a href="/hizmetler/teak-guverte-doseme/">teak güverte</a>, düzenli temizlik ve derz bakımı ister. Su altında karina ve <a href="/blog/antifouling-secimi/">antifouling</a> yıllık kalemdir.</p>
<h2>Sezon öncesi program</h2>
<p>Çok kalemli hazırlığı <a href="/blog/refit-proje-yonetimi/">proje yönetimiyle</a> koordine ediyor, sezonu aksatmayacak bir takvimle planlıyoruz. Düzenli işletmeler için <a href="/blog/yillik-bakim-anlasmasi/">yıllık anlaşma</a> uygundur.</p>
<p>Gulet bakımını <a href="/tekneler/gulet/">gulet</a> kapsamında yapıyoruz. <a href="#teklif-al">Ücretsiz keşif</a> alın.</p>
""",
 },
 "en": {
   "category": "Maintenance",
   "title": "Gulet Maintenance: Keeping It Charter-Ready",
   "excerpt": "Why is gulet care different? Wooden hull, caulking, teak and pre-season preparation.",
   "meta_title": "Gulet Maintenance Guide: Scope and Season Prep | Tekne Usta",
   "meta_desc": "Gulet maintenance: wooden hull care, caulking checks, teak deck, varnish and pre-season prep. Gulet service in the Aegean and Istanbul.",
   "body": """
<p>Gulets are mostly used commercially; downtime in season is direct lost revenue. So the heart of gulet care is a comprehensive pre-season preparation. We do this with traditional craft on wooden and composite-hull gulets.</p>
<h2>Wooden hull and caulking</h2>
<p>On wooden gulets, regular checks of <a href="/en/blog/caulking-explained/">caulking</a> seams and <a href="/en/blog/wooden-boat-varnish-care/">varnish</a> are essential; small openings must be solved before they take on water (see <a href="/en/blog/oakum-caulking-techniques/">oakum/caulking techniques</a>).</p>
<h2>Teak and deck</h2>
<p>The heavily-walked <a href="/en/services/teak-deck/">teak deck</a> needs regular cleaning and seam care. Below the waterline, underbody and <a href="/en/blog/choosing-antifouling/">antifouling</a> are annual items.</p>
<h2>Pre-season programme</h2>
<p>We coordinate the multi-item prep with <a href="/en/blog/refit-project-management/">project management</a>, planning a schedule that won't disrupt the season. For regular operators, an <a href="/en/blog/annual-maintenance-agreement/">annual agreement</a> is suitable.</p>
<p>We maintain gulets under <a href="/en/boats/gulet/">gulet</a> care. Get a <a href="#teklif-al">free survey</a>.</p>
""",
 },
},
{
 "slug": "gulet-refit", "slug_en": "gulet-refit",
 "image": "/assets/images/parallax-3.jpg", "date": "2030-01-25",
 "tr": {
   "category": "Renovasyon",
   "title": "Gulet Refit ve Restorasyon: Geleneği Koruyarak Yenilemek",
   "excerpt": "Gulet refit kapsamı: ahşap restorasyon, kalafat, teak, boya ve iç mekan — özgün dokuyu koruyarak.",
   "meta_title": "Gulet Refit ve Restorasyon Rehberi | Tekne Usta",
   "meta_desc": "Gulet refit ve restorasyon: ahşap gövde onarımı, kalafat, teak güverte, vernik-boya ve iç mekan yenileme. Ege ve İstanbul'da gulet refit hizmeti.",
   "body": """
<p>Gulet refit, ticari değeri ve özgün karakteri korurken teknenin birden çok kalemini birlikte yenilemektir. Ahşap gövdeli guletlerde bu iş, modern malzemeyle geleneksel ustalığı dengelemeyi gerektirir.</p>
<h2>Ahşap restorasyon</h2>
<p>Çürük ve yorulmuş bölgeler <a href="/blog/ahsap-curuk-onarimi/">onarılır</a>, gerektiğinde <a href="/blog/epoksi-ile-ahsap-guclendirme/">epoksi ile güçlendirilir</a>. Kalafat derzleri <a href="/blog/kalafat-nedir/">yenilenir</a>; hedef, özgün dokuyu bozmadan sağlamlaştırmaktır.</p>
<h2>Teak, boya, iç mekan</h2>
<p>Kapsama sık giren kalemler: <a href="/hizmetler/teak-guverte-doseme/">teak güverte</a> yenileme, gövde <a href="/hizmetler/tekne-boyama-antifouling/">boya ve vernik</a>, <a href="/hizmetler/ic-mekan-yenileme/">kabin/salon</a> döşeme. Su altında karina ve antifouling de dahil edilir.</p>
<h2>Planlama</h2>
<p>Refit'te yapısal ve boya işleri iç mekandan önce gelir. İşi kalem kalem, <a href="/blog/refit-proje-yonetimi/">proje yönetimiyle</a> planlıyor, sezon takvimini gözeterek yürütüyoruz. Motor/mekanik kapsamımız dışındadır.</p>
<p>Gulet refit'i <a href="/tekneler/gulet/">gulet</a> ve <a href="/hizmetler/ahsap-tekne-renovasyonu/">ahşap renovasyon</a> kapsamında yapıyoruz. <a href="#teklif-al">Ücretsiz keşif</a> alın.</p>
""",
 },
 "en": {
   "category": "Renovation",
   "title": "Gulet Refit and Restoration: Renewing While Preserving Tradition",
   "excerpt": "Gulet refit scope: wooden restoration, caulking, teak, paint and interior — preserving original character.",
   "meta_title": "Gulet Refit and Restoration Guide | Tekne Usta",
   "meta_desc": "Gulet refit and restoration: wooden hull repair, caulking, teak deck, varnish-paint and interior renewal. Gulet refit service in the Aegean and Istanbul.",
   "body": """
<p>A gulet refit renews several items of the boat together while preserving its commercial value and original character. On wooden-hulled gulets this requires balancing modern materials with traditional craft.</p>
<h2>Wooden restoration</h2>
<p>Rotten and fatigued areas are <a href="/en/blog/wood-rot-repair/">repaired</a> and, where needed, <a href="/en/blog/epoxy-wood-reinforcement/">reinforced with epoxy</a>. Caulking seams are <a href="/en/blog/caulking-explained/">renewed</a>; the goal is to strengthen without spoiling the original character.</p>
<h2>Teak, paint, interior</h2>
<p>Common items: <a href="/en/services/teak-deck/">teak deck</a> renewal, hull <a href="/en/services/boat-painting-antifouling/">paint and varnish</a>, <a href="/en/services/interior-refit/">cabin/saloon</a> upholstery. Underbody and antifouling are included below the waterline.</p>
<h2>Planning</h2>
<p>In a refit, structural and paint work come before the interior. We plan item by item with <a href="/en/blog/refit-project-management/">project management</a>, working around the season calendar. Engine/mechanics are outside our scope.</p>
<p>We do gulet refits under <a href="/en/boats/gulet/">gulet</a> and <a href="/en/services/wooden-boat-refit/">wooden restoration</a> care. Get a <a href="#teklif-al">free survey</a>.</p>
""",
 },
},
{
 "slug": "sisme-bot-tamiri", "slug_en": "inflatable-boat-repair",
 "image": "/assets/images/services/fiberglas.jpg", "date": "2030-01-28",
 "tr": {
   "category": "Onarım",
   "title": "Şişme Bot ve RIB Tamiri: Hypalon mu PVC mi?",
   "excerpt": "Şişme bot tamirinde malzeme farkı: Hypalon ve PVC. Delik, dikiş ve valf onarımı; RIB gövde işleri.",
   "meta_title": "Şişme Bot ve RIB Tamiri Rehberi | Tekne Usta",
   "meta_desc": "Şişme bot tamiri: Hypalon ve PVC farkı, delik-yama, dikiş ve valf onarımı; RIB'lerde fiberglas gövde işleri. İstanbul ve Ege'de servis.",
   "body": """
<p>Şişme botlarda ve RIB'lerde tamir, malzemeyle başlar: tüpler <strong>Hypalon (CSM)</strong> ya da <strong>PVC</strong> olabilir ve her biri farklı yapıştırıcı ve teknik ister. Yanlış malzemeyle yapılan yama kısa sürede açılır.</p>
<h2>Hypalon ve PVC farkı</h2>
<p>Hypalon UV ve kimyasala daha dayanıklı, uzun ömürlüdür; PVC daha ekonomiktir ama güneşte daha çabuk yorulur. Doğru teşhis, doğru yamanın ön koşuludur.</p>
<h2>Tüp tarafı onarımlar</h2>
<p>Sık işler: delik/yırtık yama, dikiş ve ek yeri açılması, valf değişimi, tüp ile gövde birleşiminin (kızak) yeniden yapıştırılması. Tüpün tamamen yorulduğu durumlarda yama yerine yenileme daha doğru olabilir.</p>
<h2>RIB gövde işleri</h2>
<p>RIB'lerde sert fiberglas gövde ayrı bir kalemdir; <a href="/blog/fiberglas-catlak-onarimi/">çatlak onarımı</a>, <a href="/blog/gelcoat-yenileme/">gelcoat</a> ve <a href="/blog/antifouling-secimi/">antifouling</a> tarafında hizmet veriyoruz.</p>
<p>Şişme bot ve RIB işlerini <a href="/tekneler/rib-bot/">RIB / bot</a> kapsamında yürütüyoruz. <a href="#teklif-al">Ücretsiz keşif</a> alın.</p>
""",
 },
 "en": {
   "category": "Repair",
   "title": "Inflatable and RIB Repair: Hypalon or PVC?",
   "excerpt": "The material difference in inflatable repair: Hypalon vs PVC. Punctures, seams and valves; RIB hull work.",
   "meta_title": "Inflatable Boat and RIB Repair Guide | Tekne Usta",
   "meta_desc": "Inflatable boat repair: Hypalon vs PVC, puncture patching, seam and valve repair; fibreglass hull work on RIBs. Service in Istanbul and the Aegean.",
   "body": """
<p>Repair on inflatables and RIBs starts with the material: tubes may be <strong>Hypalon (CSM)</strong> or <strong>PVC</strong>, and each needs different adhesive and technique. A patch made with the wrong material soon lifts.</p>
<h2>Hypalon vs PVC</h2>
<p>Hypalon is more resistant to UV and chemicals and lasts longer; PVC is cheaper but fatigues faster in the sun. Correct diagnosis is the precondition for a correct patch.</p>
<h2>Tube-side repairs</h2>
<p>Common jobs: puncture/tear patching, seam and joint separation, valve replacement, re-bonding the tube-to-hull joint. Where a tube is fully fatigued, replacement can be better than patching.</p>
<h2>RIB hull work</h2>
<p>On RIBs the rigid fibreglass hull is a separate item; we serve <a href="/en/blog/fibreglass-crack-repair/">crack repair</a>, <a href="/en/blog/gelcoat-renewal/">gelcoat</a> and <a href="/en/blog/choosing-antifouling/">antifouling</a>.</p>
<p>We handle inflatable and RIB work under <a href="/en/boats/rib-tender/">RIB / tender</a> care. Get a <a href="#teklif-al">free survey</a>.</p>
""",
 },
},
{
 "slug": "bot-boyama", "slug_en": "tender-painting",
 "image": "/assets/images/services/boya.jpg", "date": "2030-01-31",
 "tr": {
   "category": "Boya",
   "title": "Bot Boyama ve RIB Bakımı: Küçük Tekne, Doğru Sistem",
   "excerpt": "Bot boyama ve RIB bakımı: fiberglas gövde boyası, antifouling, gelcoat tazeleme ve rutin bakım.",
   "meta_title": "Bot Boyama ve RIB Bakımı Rehberi | Tekne Usta",
   "meta_desc": "Bot boyama: fiberglas gövde boyası, antifouling, gelcoat tazeleme; RIB bakımı ve karina temizliği. İstanbul ve Ege'de bot servisi.",
   "body": """
<p>Küçük olmaları botların ve RIB'lerin bakımını basitleştirmez; doğru boya sistemi ve düzenli bakım, hem görünümü hem değeri korur. Sert fiberglas gövdede tam hizmet veriyoruz (şişme tüp tarafı için <a href="/blog/sisme-bot-tamiri/">şişme bot tamiri</a>).</p>
<h2>Gövde boyası ve gelcoat</h2>
<p>Fiberglas gövdede seçenek, <a href="/blog/jelkot-vs-boya/">gelcoat tazeleme</a> ya da <a href="/blog/2k-poliuretan-boya/">2K boya</a>dır. Sararmış/çizik yüzeylerde çoğu zaman <a href="/blog/gelcoat-cizik-sararma-giderme/">gelcoat restorasyonu</a> yeterli olur.</p>
<h2>Antifouling</h2>
<p>Suda kalan bot ve RIB'lerde <a href="/blog/antifouling-secimi/">antifouling</a> düzenli yenilenir; karina temizliği performansı korur.</p>
<h2>Rutin bakım</h2>
<p>Küçük teknede de <a href="/blog/anot-zinc-bakimi/">anot</a> kontrolü ve yüzey bakımı ihmal edilmemeli. Sezon açılış-kapanışında kısa bir kontrol yeterlidir.</p>
<p>Bot ve RIB boyama-bakımını <a href="/tekneler/rib-bot/">RIB / bot</a> ve <a href="/hizmetler/tekne-boyama-antifouling/">boya</a> kapsamında yapıyoruz. <a href="#teklif-al">Ücretsiz keşif</a> alın.</p>
""",
 },
 "en": {
   "category": "Painting",
   "title": "Tender Painting and RIB Care: Small Boat, Right System",
   "excerpt": "Tender painting and RIB care: fibreglass hull paint, antifouling, gelcoat refresh and routine maintenance.",
   "meta_title": "Tender Painting and RIB Care Guide | Tekne Usta",
   "meta_desc": "Tender painting: fibreglass hull paint, antifouling, gelcoat refresh; RIB care and underbody cleaning. Tender service in Istanbul and the Aegean.",
   "body": """
<p>Being small doesn't simplify the care of tenders and RIBs; the right paint system and regular care protect both looks and value. We provide full service on the rigid fibreglass hull (for the inflatable tube side, see <a href="/en/blog/inflatable-boat-repair/">inflatable boat repair</a>).</p>
<h2>Hull paint and gelcoat</h2>
<p>On a fibreglass hull the choice is <a href="/en/blog/gelcoat-vs-paint/">gelcoat refresh</a> or <a href="/en/blog/2k-polyurethane-paint/">2K paint</a>. On yellowed/scratched surfaces, <a href="/en/blog/gelcoat-scratch-yellowing/">gelcoat restoration</a> is often enough.</p>
<h2>Antifouling</h2>
<p>On tenders and RIBs kept afloat, <a href="/en/blog/choosing-antifouling/">antifouling</a> is renewed regularly; underbody cleaning preserves performance.</p>
<h2>Routine care</h2>
<p>Even on a small boat, <a href="/en/blog/anode-zinc-care/">anode</a> checks and surface care shouldn't be neglected. A short check at season open and close is enough.</p>
<p>We do tender and RIB painting-care under <a href="/en/boats/rib-tender/">RIB / tender</a> and <a href="/en/services/boat-painting-antifouling/">painting</a> care. Get a <a href="#teklif-al">free survey</a>.</p>
""",
 },
},
{
 "slug": "surat-teknesi-bakimi", "slug_en": "speedboat-maintenance",
 "image": "/assets/images/parallax-1.jpg", "date": "2030-02-03",
 "tr": {
   "category": "Bakım",
   "title": "Sürat Teknesi Bakımı: Hız İçin Pürüzsüz Karina",
   "excerpt": "Sürat teknesi bakımı: pürüzsüz karina, gelcoat parlaklığı, antifouling ve detailing.",
   "meta_title": "Sürat Teknesi Bakımı ve Servisi Rehberi | Tekne Usta",
   "meta_desc": "Sürat teknesi bakımı: pürüzsüz karina, gelcoat parlaklığı, doğru antifouling ve detailing. İstanbul ve Ege'de sürat teknesi servisi.",
   "body": """
<p>Sürat teknelerinde performans, büyük ölçüde karinanın pürüzsüzlüğüne bağlıdır; kaba ya da kirlenmiş bir gövde hem hızı hem yakıt verimini düşürür. Motor dışında; gövde, yüzey ve karina tarafında servis veriyoruz.</p>
<h2>Pürüzsüz karina</h2>
<p>Düzgün bir <a href="/blog/su-hatti-boyama/">su hattı</a> ve pürüzsüz karina için doğru <a href="/blog/antifouling-secimi/">antifouling</a> ve düzenli <a href="/blog/robotik-karina-temizligi/">temizlik</a> önemlidir. Yüzeydeki kabalık doğrudan hız kaybıdır.</p>
<h2>Gelcoat ve parlaklık</h2>
<p>Sürat tekneleri genelde parlak gelcoat yüzeye sahiptir; <a href="/blog/gelcoat-yenileme/">gelcoat bakımı</a> ve <a href="/hizmetler/tekne-detailing/">detailing</a> ile ilk günkü görünüm korunur.</p>
<h2>Sezonluk kontrol</h2>
<p>Anot, karina ve yüzey kontrolü sezon başında yapılır. Küçük gövde <a href="/blog/fiberglas-catlak-onarimi/">çatlakları</a> büyümeden onarılmalı.</p>
<p>Sürat teknesi bakımını <a href="/tekneler/surat-teknesi/">sürat teknesi</a> kapsamında yapıyoruz. <a href="#teklif-al">Ücretsiz keşif</a> alın.</p>
""",
 },
 "en": {
   "category": "Maintenance",
   "title": "Speedboat Maintenance: A Smooth Hull for Speed",
   "excerpt": "Speedboat care: smooth underbody, gelcoat gloss, antifouling and detailing.",
   "meta_title": "Speedboat Maintenance and Service Guide | Tekne Usta",
   "meta_desc": "Speedboat maintenance: smooth underbody, gelcoat gloss, the right antifouling and detailing. Speedboat service in Istanbul and the Aegean.",
   "body": """
<p>On speedboats, performance depends largely on how smooth the hull is; a rough or fouled hull cuts both speed and fuel efficiency. Apart from the engine, we serve the hull, surface and underbody.</p>
<h2>A smooth underbody</h2>
<p>For a clean <a href="/en/blog/waterline-boot-stripe/">waterline</a> and smooth hull, the right <a href="/en/blog/choosing-antifouling/">antifouling</a> and regular <a href="/en/blog/robotic-hull-cleaning/">cleaning</a> matter. Roughness on the surface is direct speed loss.</p>
<h2>Gelcoat and gloss</h2>
<p>Speedboats usually have a glossy gelcoat surface; <a href="/en/blog/gelcoat-renewal/">gelcoat care</a> and <a href="/en/services/boat-detailing/">detailing</a> preserve the day-one look.</p>
<h2>Seasonal check</h2>
<p>Anode, underbody and surface checks are done at season start. Small hull <a href="/en/blog/fibreglass-crack-repair/">cracks</a> should be repaired before they grow.</p>
<p>We maintain speedboats under <a href="/en/boats/speedboat/">speedboat</a> care. Get a <a href="#teklif-al">free survey</a>.</p>
""",
 },
},
{
 "slug": "fiber-tekne-tamiri", "slug_en": "fibreglass-boat-repair",
 "image": "/assets/images/services/fiberglas.jpg", "date": "2030-02-06",
 "tr": {
   "category": "Onarım",
   "title": "Fiber Tekne Tamiri: Çatlaktan Yapısal Onarıma",
   "excerpt": "Fiber (fiberglas) tekne tamiri: jelkot çatlağı, delik, delaminasyon ve su altı yapısal onarım.",
   "meta_title": "Fiber Tekne Tamiri Rehberi: Çatlak ve Yapısal | Tekne Usta",
   "meta_desc": "Fiber (fiberglas) tekne tamiri: jelkot çatlağı onarımı, delik-delaminasyon, laminasyon ve su altı yapısal onarım. İstanbul ve Ege'de fiber tekne servisi.",
   "body": """
<p>Fiberglas tekneler dayanıklıdır ama darbeler, yaşlanma ve nem zamanla çatlak, delik ve delaminasyona yol açar. Doğru reçine ve laminasyon tekniğiyle bu hasarların çoğu kalıcı biçimde onarılır.</p>
<h2>Yüzey mi, yapısal mı?</h2>
<p>Yüzeysel <a href="/blog/gelcoat-cizik-sararma-giderme/">jelkot çatlakları</a> kozmetiktir; hızlı çözülür. Ancak laminata inen çatlaklar, delaminasyon ve su altı hasarları <a href="/blog/su-alti-yapisal-onarim/">yapısal onarım</a> gerektirir; ihmal edilmemeli.</p>
<h2>Reçine ve teknik</h2>
<p>Onarımın ömrü, doğru <a href="/blog/polyester-vs-epoksi-recine/">reçine seçimi</a> ve laminasyon kalitesine bağlıdır. Gerektiğinde <a href="/blog/karbon-ile-guclendirme/">karbon takviyesi</a> ile bölge güçlendirilir.</p>
<h2>Osmoz ayrı bir konu</h2>
<p>Su altında kabarcık görülüyorsa bu çoğu zaman <a href="/blog/osmoz-nedir-tedavisi/">osmoz</a>dur ve farklı bir süreç ister (bkz. <a href="/blog/blister-vs-osmoz-farki/">blister vs osmoz</a>).</p>
<p>Fiber tekne tamirini <a href="/tekneler/fiber-tekne/">fiber tekne</a> ve <a href="/hizmetler/fiberglas-onarim/">fiberglas onarım</a> kapsamında yapıyoruz. <a href="#teklif-al">Ücretsiz keşif</a> alın.</p>
""",
 },
 "en": {
   "category": "Repair",
   "title": "Fibreglass Boat Repair: From Cracks to Structural Work",
   "excerpt": "Fibreglass boat repair: gelcoat cracks, holes, delamination and underwater structural repair.",
   "meta_title": "Fibreglass Boat Repair Guide: Cracks and Structural | Tekne Usta",
   "meta_desc": "Fibreglass boat repair: gelcoat crack repair, holes-delamination, lamination and underwater structural repair. Fibreglass boat service in Istanbul and the Aegean.",
   "body": """
<p>Fibreglass boats are durable, but impacts, ageing and moisture eventually cause cracks, holes and delamination. With the right resin and lamination technique, most of this damage is repaired permanently.</p>
<h2>Surface or structural?</h2>
<p>Superficial <a href="/en/blog/gelcoat-scratch-yellowing/">gelcoat cracks</a> are cosmetic and solved quickly. But cracks reaching the laminate, delamination and underwater damage need <a href="/en/blog/underwater-structural-repair/">structural repair</a> and shouldn't be neglected.</p>
<h2>Resin and technique</h2>
<p>The life of a repair depends on the right <a href="/en/blog/polyester-vs-epoxy-resin/">resin choice</a> and lamination quality. Where needed, the area is strengthened with <a href="/en/blog/carbon-reinforcement/">carbon reinforcement</a>.</p>
<h2>Osmosis is a separate matter</h2>
<p>If you see blisters below the waterline, it's often <a href="/en/blog/what-is-osmosis-treatment/">osmosis</a> and needs a different process (see <a href="/en/blog/blister-vs-osmosis/">blister vs osmosis</a>).</p>
<p>We do fibreglass boat repair under <a href="/en/boats/fibreglass-boat/">fibreglass boat</a> and <a href="/en/services/fibreglass-repair/">fibreglass repair</a> care. Get a <a href="#teklif-al">free survey</a>.</p>
""",
 },
},
{
 "slug": "ahsap-tekne-bakimi", "slug_en": "wooden-boat-maintenance",
 "image": "/assets/images/services/ahsap.jpg", "date": "2030-02-09",
 "tr": {
   "category": "Bakım",
   "title": "Ahşap Tekne Bakımı: Vernik, Kalafat ve Nem Yönetimi",
   "excerpt": "Ahşap tekne bakımı: vernik döngüsü, kalafat kontrolü, çürük önleme ve kışlatma.",
   "meta_title": "Ahşap Tekne Bakımı Rehberi: Vernik ve Kalafat | Tekne Usta",
   "meta_desc": "Ahşap tekne bakımı: vernik bakım döngüsü, kalafat kontrolü, çürük önleme, nem yönetimi ve kışlatma. İstanbul ve Ege'de ahşap tekne servisi.",
   "body": """
<p>Ahşap tekne, düzenli bakımla onlarca yıl yaşar; ihmal edildiğinde ise sorunlar hızla büyür. Bakımın özü, suyu ahşaptan uzak tutmak: sağlam vernik/boya, sıkı kalafat ve iyi havalandırma.</p>
<h2>Vernik ve boya döngüsü</h2>
<p>Ahşapta koruyucu katman süreklidir; <a href="/blog/ahsap-tekne-vernik-bakimi/">vernik bakımı</a> döngüsü aksarsa güneş ve su ahşaba ulaşır. Düzenli ince katlar, tam soyup yeniden yapmaktan çok daha ekonomiktir.</p>
<h2>Kalafat ve çürük önleme</h2>
<p><a href="/blog/kalafat-nedir/">Kalafat</a> derzleri kontrol edilir; açılmalar su almaya dönüşmeden kapatılır. Nemli, havasız bölgeler <a href="/blog/ahsap-curuk-onarimi/">çürüğün</a> başlangıcıdır; erken tespit kritiktir.</p>
<h2>Nem ve kışlatma</h2>
<p>İç mekanda havalandırma, küf ve nemi önler. Kışın doğru <a href="/blog/ahsap-tekne-kislatma/">ahşap tekne kışlatması</a>, ahşabın aşırı kurumasını da engeller.</p>
<p>Ahşap tekne bakımını <a href="/tekneler/ahsap-tekne/">ahşap tekne</a> ve <a href="/hizmetler/ahsap-tekne-renovasyonu/">ahşap renovasyon</a> kapsamında yapıyoruz. <a href="#teklif-al">Ücretsiz keşif</a> alın.</p>
""",
 },
 "en": {
   "category": "Maintenance",
   "title": "Wooden Boat Maintenance: Varnish, Caulking and Moisture Management",
   "excerpt": "Wooden boat care: the varnish cycle, caulking checks, rot prevention and winterising.",
   "meta_title": "Wooden Boat Maintenance Guide: Varnish and Caulking | Tekne Usta",
   "meta_desc": "Wooden boat maintenance: varnish care cycle, caulking checks, rot prevention, moisture management and winterising. Wooden boat service in Istanbul and the Aegean.",
   "body": """
<p>A wooden boat lasts for decades with regular care; neglected, its problems grow fast. The essence of care is keeping water away from the wood: sound varnish/paint, tight caulking and good ventilation.</p>
<h2>The varnish and paint cycle</h2>
<p>On wood the protective layer is continuous; if the <a href="/en/blog/wooden-boat-varnish-care/">varnish care</a> cycle slips, sun and water reach the wood. Regular thin coats are far cheaper than stripping and redoing entirely.</p>
<h2>Caulking and rot prevention</h2>
<p><a href="/en/blog/caulking-explained/">Caulking</a> seams are checked; openings are closed before they take on water. Damp, unventilated areas are where <a href="/en/blog/wood-rot-repair/">rot</a> starts; early detection is critical.</p>
<h2>Moisture and winterising</h2>
<p>Ventilation in the interior prevents mould and damp. Proper <a href="/en/blog/wooden-boat-winterising/">wooden boat winterising</a> also stops the wood from over-drying in winter.</p>
<p>We maintain wooden boats under <a href="/en/boats/wooden-boat/">wooden boat</a> and <a href="/en/services/wooden-boat-refit/">wooden restoration</a> care. Get a <a href="#teklif-al">free survey</a>.</p>
""",
 },
},
{
 "slug": "sezon-ortasi-bakim", "slug_en": "mid-season-maintenance",
 "image": "/assets/images/parallax-1.jpg", "date": "2030-06-15",
 "tr": {
   "category": "Sezonluk",
   "title": "Sezon Ortası Tekne Bakımı: Yaz Boyunca Formda Tutmak",
   "excerpt": "Yaz ortasında teknenizi neden ve nasıl kontrol etmeli? Karina, yüzey ve küçük onarımlar sezonu kurtarır.",
   "meta_title": "Sezon Ortası Tekne Bakımı Rehberi | Tekne Usta",
   "meta_desc": "Yaz ortasında tekne bakımı: karina/antifouling kontrolü, yüzey ve teak temizliği, küçük onarımlar. Sezonu aksatmadan formda kalın. İstanbul ve Ege.",
   "body": """
<p>Bakım denince akla sezon açılışı ve kışlatma gelir; oysa yaz ortasında yapılan kısa bir kontrol, sezonun kalanını kurtarır. Yoğun kullanım döneminde küçük sorunlar hızla büyür.</p>
<h2>Karina ve performans</h2>
<p>Yaz ortasında karinaya yosun/kabuk birikmesi hız ve yakıt verimini düşürür. Kısa bir <a href="/blog/robotik-karina-temizligi/">karina temizliği</a> ve <a href="/blog/antifouling-secimi/">antifouling</a> durumunun gözden geçirilmesi çoğu zaman yeterlidir. <a href="/blog/anot-zinc-bakimi/">Anot</a> durumu da kontrol edilmeli.</p>
<h2>Yüzey ve teak</h2>
<p>Tuz ve güneş, gövdeyi ve güverteyi yorar. Ara bir <a href="/hizmetler/tekne-detailing/">detailing</a>, <a href="/blog/kekamoz-temizligi/">kireç lekesi temizliği</a> ve <a href="/blog/teak-guverte-bakimi/">teak bakımı</a> hem görünümü hem malzeme ömrünü korur.</p>
<h2>Küçük onarımları erteleme</h2>
<p>Sezon içinde fark ettiğin küçük bir <a href="/blog/fiberglas-catlak-onarimi/">çatlak</a> ya da jelkot çiziği, kışa kadar beklerse büyür. Yaz ortası, bunları hızlı çözmenin tam zamanı. Genel plan için <a href="/blog/yillik-tekne-bakim-takvimi/">yıllık bakım takvimine</a> bakın.</p>
<p>Yerinde kısa bir kontrol için <a href="#teklif-al">ücretsiz keşif</a> alın.</p>
""",
 },
 "en": {
   "category": "Seasonal",
   "title": "Mid-Season Boat Maintenance: Staying in Shape All Summer",
   "excerpt": "Why and how to check your boat mid-summer? Underbody, surface and small repairs save the season.",
   "meta_title": "Mid-Season Boat Maintenance Guide | Tekne Usta",
   "meta_desc": "Mid-summer boat maintenance: underbody/antifouling check, surface and teak cleaning, small repairs. Stay in shape without disrupting the season. Istanbul and the Aegean.",
   "body": """
<p>Maintenance usually brings to mind season opening and winterising; yet a short mid-summer check saves the rest of the season. In peak use, small problems grow fast.</p>
<h2>Underbody and performance</h2>
<p>Mid-summer weed/shell build-up on the hull cuts speed and fuel efficiency. A short <a href="/en/blog/robotic-hull-cleaning/">hull cleaning</a> and a review of the <a href="/en/blog/choosing-antifouling/">antifouling</a> condition is often enough. <a href="/en/blog/anode-zinc-care/">Anode</a> status should be checked too.</p>
<h2>Surface and teak</h2>
<p>Salt and sun tire the hull and deck. An interim <a href="/en/services/boat-detailing/">detailing</a>, <a href="/en/blog/hull-limescale-cleaning/">limescale cleaning</a> and <a href="/en/blog/teak-deck-maintenance/">teak care</a> protect both looks and material life.</p>
<h2>Don't defer small repairs</h2>
<p>A small <a href="/en/blog/fibreglass-crack-repair/">crack</a> or gelcoat scratch you notice in season grows if it waits until winter. Mid-summer is the right time to solve them fast. For the overall plan, see the <a href="/en/blog/annual-boat-maintenance-calendar/">annual maintenance calendar</a>.</p>
<p>For a short on-site check, get a <a href="#teklif-al">free survey</a>.</p>
""",
 },
},
{
 "slug": "yaz-tekne-koruma", "slug_en": "summer-boat-protection",
 "image": "/assets/images/services/boya.jpg", "date": "2030-06-28",
 "tr": {
   "category": "Sezonluk",
   "title": "Yaz Güneşinde Tekne Koruması: Jelkot, Teak ve Vernik",
   "excerpt": "Yaz güneşi ve tuz teknenize ne yapar? UV koruma, jelkot cilası ve teak/vernik bakımıyla önlem.",
   "meta_title": "Yaz Güneşinde Tekne Koruma Rehberi | Tekne Usta",
   "meta_desc": "Yazın tekne koruması: UV hasarına karşı jelkot cilası, teak ve vernik bakımı, doğru örtü. Güneş ve tuzdan malzemeyi koruyun. İstanbul ve Ege.",
   "body": """
<p>Yaz, teknenin en çok kullanıldığı ama malzemenin en çok yorulduğu dönemdir. UV ışınları ve tuz; jelkotu matlaştırır, teak'i grileştirir, verniği çatlatır. Doğru önlemle bu yıpranma büyük ölçüde yavaşlar.</p>
<h2>Jelkot ve UV</h2>
<p>Parlak jelkot, güneşte oksitlenir ve matlaşır. Sezonluk cila ve <a href="/blog/uv-koruma-kaplama/">UV koruyucu kaplama</a>, rengi ve parlaklığı korur; ileride gereken <a href="/blog/gelcoat-yenileme/">gelcoat yenileme</a> ihtiyacını erteler.</p>
<h2>Teak ve vernik</h2>
<p>Teak güneşte doğal olarak grileşir; düzenli <a href="/blog/teak-guverte-bakimi/">teak bakımı</a> bunu yönetir. Ahşap yüzeylerde <a href="/blog/ahsap-tekne-vernik-bakimi/">vernik</a> katmanı güneşe karşı ilk savunmadır; ince ara katlar çatlamayı önler.</p>
<h2>Örtü ve gölge</h2>
<p>Kullanılmadığı günlerde tekneyi güneşten korumak en ucuz bakımdır. Doğru <a href="/hizmetler/tente-branda/">tente/branda</a> hem iç mekanı hem güverteyi korur.</p>
<p>Yaz koruma paketini <a href="/hizmetler/tekne-detailing/">detailing</a> kapsamında yapıyoruz. <a href="#teklif-al">Ücretsiz keşif</a> alın.</p>
""",
 },
 "en": {
   "category": "Seasonal",
   "title": "Summer Sun Protection: Gelcoat, Teak and Varnish",
   "excerpt": "What do summer sun and salt do to your boat? UV protection, gelcoat polish and teak/varnish care as prevention.",
   "meta_title": "Summer Boat Sun Protection Guide | Tekne Usta",
   "meta_desc": "Summer boat protection: gelcoat polish against UV, teak and varnish care, the right cover. Protect materials from sun and salt. Istanbul and the Aegean.",
   "body": """
<p>Summer is when a boat is used most but its materials tire most. UV rays and salt dull the gelcoat, grey the teak and crack the varnish. With the right prevention, this wear slows considerably.</p>
<h2>Gelcoat and UV</h2>
<p>Glossy gelcoat oxidises and dulls in the sun. A seasonal polish and <a href="/en/blog/uv-protection-coating/">UV protective coating</a> preserve colour and gloss and defer the eventual need for <a href="/en/blog/gelcoat-renewal/">gelcoat renewal</a>.</p>
<h2>Teak and varnish</h2>
<p>Teak naturally greys in the sun; regular <a href="/en/blog/teak-deck-maintenance/">teak care</a> manages this. On wood surfaces the <a href="/en/blog/wooden-boat-varnish-care/">varnish</a> layer is the first defence against the sun; thin interim coats prevent cracking.</p>
<h2>Cover and shade</h2>
<p>Protecting the boat from the sun on unused days is the cheapest maintenance. The right <a href="/en/services/marine-canvas/">canvas/cover</a> protects both interior and deck.</p>
<p>We do the summer protection package under <a href="/en/services/boat-detailing/">detailing</a>. Get a <a href="#teklif-al">free survey</a>.</p>
""",
 },
},
{
 "slug": "sonbahar-kislatma-hazirlik", "slug_en": "autumn-winterising-prep",
 "image": "/assets/images/parallax-2.jpg", "date": "2030-10-05",
 "tr": {
   "category": "Sezonluk",
   "title": "Sonbahar: Kışlatmaya Hazırlık Rehberi",
   "excerpt": "Sezon kapanırken ne yapılmalı? Kışlatma öncesi kontrol, temizlik ve onarım planı.",
   "meta_title": "Sonbahar Kışlatmaya Hazırlık Rehberi | Tekne Usta",
   "meta_desc": "Sonbaharda kışlatmaya hazırlık: sezon sonu kontrol, karina temizliği, nem yönetimi ve kış onarımlarını planlama. İstanbul ve Ege'de kışlatma servisi.",
   "body": """
<p>Sonbahar, teknenin kışa doğru hazırlandığı kritik geçiş dönemidir. İyi bir kışlatma hazırlığı, kışı hasarsız geçirmenin ve gelecek sezona hazır girmenin anahtarıdır.</p>
<h2>Sezon sonu kontrolü</h2>
<p>Karaya çekmeden önce gövde, karina ve güverte kontrol edilir; yaz boyu biriken hasarlar not edilir. Ayrıntılı liste için <a href="/blog/tekne-kislatma-kontrol-listesi/">kışlatma kontrol listemize</a> bakın.</p>
<h2>Temizlik ve nem</h2>
<p>Karina temizlenir, iç mekan kurutulur ve havalandırma sağlanır; <a href="/blog/teknede-kuf-nem-onleme/">küf ve nem</a> kışın en büyük düşmandır. Kapalı tekne aylarca nemle baş başa kalmamalı.</p>
<h2>Kış, onarım için doğru zaman</h2>
<p>Kışlatma, yalnızca "bekletme" değil; boya, teak, fiberglas ve iç mekan işleri için de en uygun dönemdir — tekne zaten karada ve kullanım dışıdır. Yaz boyu biriken işleri kışa planlamak akıllıcadır. Kışlatmayı <a href="/hizmetler/tekne-kislatma/">kışlatma & bakım</a> kapsamında yapıyoruz.</p>
<p>Sezon sonu keşfi için <a href="#teklif-al">ücretsiz keşif</a> alın.</p>
""",
 },
 "en": {
   "category": "Seasonal",
   "title": "Autumn: A Guide to Preparing for Winterising",
   "excerpt": "What to do as the season closes? Pre-winterising checks, cleaning and a repair plan.",
   "meta_title": "Autumn Winterising Preparation Guide | Tekne Usta",
   "meta_desc": "Autumn winterising prep: end-of-season checks, underbody cleaning, moisture management and planning winter repairs. Winterising service in Istanbul and the Aegean.",
   "body": """
<p>Autumn is the critical transition when a boat is prepared for winter. Good winterising prep is the key to getting through winter undamaged and starting the next season ready.</p>
<h2>End-of-season check</h2>
<p>Before haul-out, hull, underbody and deck are checked; damage accumulated over summer is noted. For a detailed list, see our <a href="/en/blog/boat-winterising-checklist/">winterising checklist</a>.</p>
<h2>Cleaning and moisture</h2>
<p>The underbody is cleaned, the interior dried and ventilated; <a href="/en/blog/preventing-mould-damp/">mould and damp</a> are the biggest enemies in winter. A closed-up boat shouldn't sit alone with moisture for months.</p>
<h2>Winter is the right time to repair</h2>
<p>Winterising isn't just "storage"; it's also the best window for paint, teak, fibreglass and interior work — the boat is already ashore and out of use. Planning the summer's accumulated jobs for winter is smart. We do winterising under <a href="/en/services/winterising-storage/">winterising & maintenance</a>.</p>
<p>For an end-of-season survey, get a <a href="#teklif-al">free survey</a>.</p>
""",
 },
},
{
 "slug": "kis-hasari-onarimi", "slug_en": "winter-damage-repair",
 "image": "/assets/images/services/fiberglas.jpg", "date": "2030-11-02",
 "tr": {
   "category": "Sezonluk",
   "title": "Kış Hasarı Onarımı: Bahar Açılışında Neler Çıkar?",
   "excerpt": "Kış boyunca teknede hangi hasarlar oluşur? Nem, çatlak, osmoz ve donma etkileri.",
   "meta_title": "Kış Hasarı Onarımı Rehberi | Tekne Usta",
   "meta_desc": "Kış hasarı: nem/küf, jelkot çatlağı, osmoz ve donma etkileri. Bahar açılışında nelere bakılır, nasıl onarılır. İstanbul ve Ege'de onarım servisi.",
   "body": """
<p>İyi kışlatılsa bile tekne, kış boyunca nem, sıcaklık değişimi ve hareketsizlikten etkilenir. Bahar açılışında bu izleri erken görmek, sezonu sorunsuz açmanın anahtarıdır. Bu yazı, mevcut <a href="/blog/bahar-tekne-bakimi/">bahar bakımı</a> rehberini tamamlar.</p>
<h2>Nem ve küf</h2>
<p>Kapalı kalan iç mekanda <a href="/blog/teknede-kuf-nem-onleme/">küf ve nem</a> en sık görülen kış hasarıdır. Döşeme, minder ve ahşap yüzeyler kontrol edilir; erken müdahale kalıcı lekeyi önler.</p>
<h2>Çatlak ve donma</h2>
<p>Sıcaklık değişimleri jelkotta ince <a href="/blog/fiberglas-catlak-onarimi/">çatlaklar</a> oluşturabilir; suyun donması dar boşluklarda hasarı büyütür. Su altında ise <a href="/blog/osmoz-belirtileri/">osmoz belirtileri</a> kışın fark edilmeden ilerleyebilir.</p>
<h2>Bahar açılış kontrolü</h2>
<p>Denize indirmeden önce gövde, karina, anot ve iç mekan tek tek gözden geçirilir. Küçük hasarları burada yakalamak, sezon içinde sürprizi önler. Onarımları <a href="/hizmetler/fiberglas-onarim/">fiberglas onarım</a> ve ilgili hizmetler kapsamında yapıyoruz.</p>
<p>Bahar açılış kontrolü için <a href="#teklif-al">ücretsiz keşif</a> alın.</p>
""",
 },
 "en": {
   "category": "Seasonal",
   "title": "Winter Damage Repair: What Shows Up at Spring Launch?",
   "excerpt": "What damage forms on a boat over winter? Moisture, cracks, osmosis and freeze effects.",
   "meta_title": "Winter Damage Repair Guide | Tekne Usta",
   "meta_desc": "Winter damage: damp/mould, gelcoat cracks, osmosis and freeze effects. What to check at spring launch and how to repair. Repair service in Istanbul and the Aegean.",
   "body": """
<p>Even well winterised, a boat is affected by moisture, temperature swings and inactivity over winter. Spotting these signs early at spring launch is the key to a smooth season start. This article complements our <a href="/en/blog/spring-boat-maintenance/">spring maintenance</a> guide.</p>
<h2>Moisture and mould</h2>
<p>In a closed-up interior, <a href="/en/blog/preventing-mould-damp/">mould and damp</a> are the most common winter damage. Upholstery, cushions and wood surfaces are checked; early action prevents permanent staining.</p>
<h2>Cracks and freeze</h2>
<p>Temperature swings can create fine <a href="/en/blog/fibreglass-crack-repair/">cracks</a> in the gelcoat; freezing water enlarges damage in tight gaps. Below the waterline, <a href="/en/blog/osmosis-symptoms/">osmosis symptoms</a> can progress unnoticed over winter.</p>
<h2>Spring launch check</h2>
<p>Before splashing, hull, underbody, anodes and interior are reviewed one by one. Catching small damage here prevents surprises in season. We do repairs under <a href="/en/services/fibreglass-repair/">fibreglass repair</a> and related services.</p>
<p>For a spring launch check, get a <a href="#teklif-al">free survey</a>.</p>
""",
 },
},
]

# ==================================================================== COST ESTIMATOR
# ⚠️ YAYIN ÖNCESI DÜZENLE: Aşağıdaki rakamlar ÖRNEK/PLACEHOLDER değerlerdir.
# Gerçek taban fiyatlarını (metre başına min/max TL ve minimum iş bedeli) buraya gir.
# Araç, kesin fiyat değil bir "tahmini başlangıç aralığı" gösterir ve WhatsApp'a yönlendirir.
PRICING = {
    "currency": "₺",
    "round_to": 500,          # sonuçlar bu katına yuvarlanır
    # her hizmet: metre başına min/max (TL) ve minimum iş bedeli (TL)
    "services": [
        {"key": "fiberglas",  "svc_slug": "fiberglas-onarim",        "tr": "Fiberglas Onarım & Osmoz", "en": "Fibreglass Repair & Osmosis", "per_m_min": 4000,  "per_m_max": 12000, "min": 20000, "note_tr": "Osmozda kurutma süresine göre değişir", "note_en": "Varies with osmosis drying time"},
        {"key": "ahsap",      "svc_slug": "ahsap-tekne-renovasyonu", "tr": "Ahşap Renovasyon",         "en": "Wooden Refit",               "per_m_min": 5000,  "per_m_max": 16000, "min": 25000, "note_tr": "Kapsama göre çok değişkendir", "note_en": "Highly variable by scope"},
        {"key": "boya",       "svc_slug": "tekne-boyama-antifouling","tr": "Boya & Antifouling",       "en": "Painting & Antifouling",     "per_m_min": 3000,  "per_m_max": 8000,  "min": 12000, "note_tr": "Sadece antifouling daha düşüktür", "note_en": "Antifouling-only is lower"},
        {"key": "teak",       "svc_slug": "teak-guverte-doseme",     "tr": "Teak Güverte Döşeme",      "en": "Teak Decking",               "per_m_min": 8000,  "per_m_max": 20000, "min": 30000, "note_tr": "Doğal/sentetik ve alana göre", "note_en": "By natural/synthetic and area"},
        {"key": "icmekan",    "svc_slug": "ic-mekan-yenileme",       "tr": "İç Mekan Yenileme",        "en": "Interior Refit",             "per_m_min": 4000,  "per_m_max": 12000, "min": 15000, "note_tr": "Döşeme mi komple mi?", "note_en": "Upholstery only or full?"},
        {"key": "kislatma",   "svc_slug": "tekne-kislatma",          "tr": "Kışlatma & Bakım",         "en": "Winterising & Care",         "per_m_min": 1200,  "per_m_max": 3500,  "min": 7000,  "note_tr": "Çekme ve örtü tipine göre", "note_en": "By haul-out and cover type"},
    ],
    # tekne durumu çarpanı
    "condition": [
        {"key": "iyi",  "tr": "İyi durumda",   "en": "Good condition",     "factor": 0.85},
        {"key": "orta", "tr": "Orta / normal", "en": "Average",            "factor": 1.0},
        {"key": "kotu", "tr": "Kötü / bakımsız","en": "Poor / neglected",  "factor": 1.3},
    ],
}

TOOL_I18N = {
    "tr": {
        "meta_title": "Tekne Bakım & Onarım Maliyet Tahmini | Tekne Usta",
        "meta_desc": "Tekne boyutu ve hizmete göre tekne tamiri, boya, osmoz, teak ve kışlatma için tahmini maliyet aralığı. Kesin teklif için ücretsiz keşif.",
        "h1": "Tekne Maliyet Tahmin Aracı",
        "sub": "Teknenizin boyu ve istediğiniz hizmete göre tahmini bir başlangıç aralığı görün. Kesin fiyat, ücretsiz keşif sonrası kalem kalem verilir.",
        "len_label": "Tekne boyu (metre)",
        "svc_label": "Hizmet",
        "cond_label": "Teknenin durumu",
        "result_label": "Tahmini başlangıç aralığı",
        "disclaimer": "Bu yalnızca bir tahmindir; kesin fiyat teknenin durumuna göre değişir ve ücretsiz keşifle belirlenir. Yüksek gösterip caydırmak değil, doğru beklenti oluşturmak amacındayız.",
        "cta": "Bu iş için kesin teklif al (WhatsApp)",
        "wa_lead": "Merhaba, maliyet aracını kullandım. Kesin teklif istiyorum:",
        "from": "başlangıç",
    },
    "en": {
        "meta_title": "Boat Maintenance & Repair Cost Estimate | Tekne Usta",
        "meta_desc": "Estimated cost range for boat repair, painting, osmosis, teak and winterising by boat size and service. Exact quote after a free survey.",
        "h1": "Boat Cost Estimator",
        "sub": "See an estimated starting range based on your boat's length and the service you need. The exact price is itemised after a free survey.",
        "len_label": "Boat length (metres)",
        "svc_label": "Service",
        "cond_label": "Boat condition",
        "result_label": "Estimated starting range",
        "disclaimer": "This is only an estimate; the exact price depends on the boat's condition and is set by a free survey. Our aim is to set the right expectation, not to deter you with a high figure.",
        "cta": "Get an exact quote for this (WhatsApp)",
        "wa_lead": "Hello, I used the cost tool. I'd like an exact quote:",
        "from": "from",
    },
}

# ==================================================================== LEGAL PAGES
# NOT: Bu bir şablon KVKK/Gizlilik metnidir. Yayın öncesi şirketin resmi unvanı,
# adresi ve varsa VERBIS bilgileriyle güncellenmeli; hukuki inceleme önerilir.
LEGAL = [
    {
        "slug": "gizlilik", "slug_en": "privacy",
        "tr": {
            "title": "Gizlilik ve KVKK Aydınlatma Metni",
            "sub": "Kişisel verilerinizin işlenmesine ilişkin bilgilendirme.",
            "meta_title": "Gizlilik ve KVKK Aydınlatma Metni | Tekne Usta",
            "meta_desc": "Tekne Usta gizlilik politikası ve KVKK aydınlatma metni: iletişim formu ve WhatsApp üzerinden paylaşılan kişisel verilerin işlenme amacı, hukuki sebebi ve haklarınız.",
            "body": """
<p><em>Son güncelleme: 2026. Bu metin bir şablondur; yayına almadan önce şirketin resmi unvanı ve iletişim bilgileriyle güncellenmesi ve hukuki inceleme önerilir.</em></p>
<h2>Veri Sorumlusu</h2>
<p>Tekne Usta ("biz"), bu web sitesi (tekneusta.com) üzerinden paylaştığınız kişisel verilerin veri sorumlusudur. İletişim: <a href="tel:+905321738978">+90 532 173 89 78</a>.</p>
<h2>Hangi Verileri Topluyoruz?</h2>
<p>Teklif formu ve WhatsApp üzerinden bize ilettiğiniz <strong>ad, telefon numarası, tekne bilgisi ve mesaj içeriği</strong> gibi verileri topluyoruz. Sitemizde reklam amaçlı takip çerezi kullanmıyoruz.</p>
<h2>Verilerinizi Neden İşliyoruz?</h2>
<p>Verileriniz yalnızca <strong>talebinize dönüş yapmak, keşif ve teklif sürecini yürütmek ve hizmeti sağlamak</strong> amacıyla işlenir. Bu, KVKK m.5 kapsamında "bir sözleşmenin kurulması/ifası" ve "meşru menfaat" hukuki sebeplerine dayanır.</p>
<h2>Verileriniz Paylaşılır mı?</h2>
<p>Verilerinizi pazarlama amacıyla üçüncü taraflara satmayız veya kiralamayız. İletişim yalnızca sizinle iletişim amacıyla kullanılır.</p>
<h2>Saklama Süresi</h2>
<p>Verileriniz, talebinizin gerektirdiği süre boyunca ve ilgili yasal yükümlülükler çerçevesinde saklanır; amaç ortadan kalktığında silinir veya anonim hale getirilir.</p>
<h2>KVKK Kapsamındaki Haklarınız</h2>
<p>KVKK m.11 uyarınca; verilerinizin işlenip işlenmediğini öğrenme, düzeltilmesini veya silinmesini isteme, işlemeye itiraz etme ve diğer haklarınıza sahipsiniz. Talepleriniz için yukarıdaki iletişim kanallarından bize ulaşabilirsiniz.</p>
""",
        },
        "en": {
            "title": "Privacy Policy",
            "sub": "Information about how we handle your personal data.",
            "meta_title": "Privacy Policy | Tekne Usta",
            "meta_desc": "Tekne Usta privacy policy: the purpose, legal basis and your rights regarding personal data shared via the contact form and WhatsApp.",
            "body": """
<p><em>Last updated: 2026. This is a template; before going live it should be updated with the company's legal details and reviewed legally.</em></p>
<h2>Data Controller</h2>
<p>Tekne Usta ("we") is the controller of the personal data you share via this website (tekneusta.com). Contact: <a href="tel:+905321738978">+90 532 173 89 78</a>.</p>
<h2>What Data We Collect</h2>
<p>Via the quote form and WhatsApp we collect data you provide such as your <strong>name, phone number, boat details and message</strong>. We do not use advertising tracking cookies on our site.</p>
<h2>Why We Process Your Data</h2>
<p>Your data is processed only to <strong>respond to your request, run the survey and quote process, and provide the service</strong>. This is based on the performance of a contract and our legitimate interest.</p>
<h2>Do We Share Your Data?</h2>
<p>We do not sell or rent your data to third parties for marketing. Your details are used only to contact you.</p>
<h2>Retention</h2>
<p>Your data is kept for as long as your request requires and under applicable legal obligations; once the purpose ends it is deleted or anonymised.</p>
<h2>Your Rights</h2>
<p>You have the right to know whether your data is processed, to request its correction or deletion, to object to processing and other rights. Contact us through the channels above for any request.</p>
""",
        },
    },
]

# ==================================================================== GLOSSARY (Sözlük Hub)
GLOSSARY = [
 {"tr": {"t": "Osmoz", "d": "Fiberglas teknede jelkot altına sızan suyun laminatla tepkimeye girip kabarcık oluşturması.", "u": "/blog/osmoz-nedir-tedavisi/"},
  "en": {"t": "Osmosis", "d": "Water seeping under the gelcoat and reacting with the laminate to form blisters on a fibreglass boat.", "u": "/en/blog/what-is-osmosis-treatment/"}},
 {"tr": {"t": "Blister", "d": "Su altı yüzeyde jelkot altında oluşan içi sıvı dolu kabarcık; her blister osmoz değildir.", "u": "/blog/blister-vs-osmoz-farki/"},
  "en": {"t": "Blister", "d": "A fluid-filled bubble under the gelcoat on the underwater surface; not every blister is osmosis.", "u": "/en/blog/blister-vs-osmosis/"}},
 {"tr": {"t": "Gelcoat (Jelkot)", "d": "Fiberglas teknenin dış yüzeyindeki renkli, parlak koruyucu katman.", "u": "/blog/gelcoat-yenileme/"},
  "en": {"t": "Gelcoat", "d": "The coloured, glossy protective outer layer of a fibreglass boat.", "u": "/en/blog/gelcoat-renewal/"}},
 {"tr": {"t": "Antifouling (Zehirli boya)", "d": "Karinayı yosun, midye gibi deniz canlılarının yapışmasından koruyan su altı boyası.", "u": "/blog/antifouling-secimi/"},
  "en": {"t": "Antifouling", "d": "Underwater paint that protects the hull from marine growth like weed and mussels.", "u": "/en/blog/choosing-antifouling/"}},
 {"tr": {"t": "Fiberglas (GRP)", "d": "Cam elyafı ve reçineden üretilen, teknelerde en yaygın gövde malzemesi.", "u": "/hizmetler/fiberglas-onarim/"},
  "en": {"t": "Fibreglass (GRP)", "d": "Glass fibre and resin composite, the most common boat hull material.", "u": "/en/services/fibreglass-repair/"}},
 {"tr": {"t": "Epoksi", "d": "Yüksek yapışma ve su geçirmezlik sağlayan reçine; yapısal onarım ve bariyer katında tercih edilir.", "u": "/blog/polyester-vs-epoksi-recine/"},
  "en": {"t": "Epoxy", "d": "A resin with high adhesion and waterproofing; preferred for structural repair and barrier coats.", "u": "/en/blog/polyester-vs-epoxy-resin/"}},
 {"tr": {"t": "Polyester reçine", "d": "Teknelerin çoğunun üretildiği, ekonomik ve orijinal laminatla uyumlu reçine.", "u": "/blog/polyester-vs-epoksi-recine/"},
  "en": {"t": "Polyester resin", "d": "The economical resin most boats are built with, compatible with the original laminate.", "u": "/en/blog/polyester-vs-epoxy-resin/"}},
 {"tr": {"t": "Epoksi macun (Dolgu / Fairing)", "d": "Çatlak, boşluk ve düzensizlikleri doldurup pürüzsüz yüzey oluşturan iki bileşenli dolgu.", "u": "/blog/epoksi-macun-nedir/"},
  "en": {"t": "Epoxy filler (Fairing)", "d": "A two-part filler that fills cracks and unevenness to create a smooth surface.", "u": "/en/blog/epoxy-filler-putty/"}},
 {"tr": {"t": "Kalafat", "d": "Ahşap teknede kaplama tahtaları arasındaki derzlerin su geçirmez hale getirilmesi.", "u": "/blog/kalafat-nedir/"},
  "en": {"t": "Caulking", "d": "Making the seams between planks watertight on a wooden boat.", "u": "/en/blog/caulking-explained/"}},
 {"tr": {"t": "Üstüpü", "d": "Geleneksel kalafatta derzlere çakılan pamuk/keten lifi dolgu malzemesi.", "u": "/blog/ustupu-kalafat-teknikleri/"},
  "en": {"t": "Oakum", "d": "The cotton/flax fibre driven into seams in traditional caulking.", "u": "/en/blog/oakum-caulking-techniques/"}},
 {"tr": {"t": "Teak (Tik)", "d": "Doğal yağı sayesinde suya dayanıklı, güvertede kullanılan değerli ahşap.", "u": "/hizmetler/teak-guverte-doseme/"},
  "en": {"t": "Teak", "d": "A prized, water-resistant wood used for decks thanks to its natural oils.", "u": "/en/services/teak-deck/"}},
 {"tr": {"t": "Sentetik teak", "d": "Bakım gerektirmeyen PVC/EVA bazlı, teak görünümlü güverte kaplaması.", "u": "/blog/sentetik-teak-alternatifleri/"},
  "en": {"t": "Synthetic teak", "d": "Maintenance-free PVC/EVA-based deck covering that looks like teak.", "u": "/en/blog/synthetic-teak-alternatives/"}},
 {"tr": {"t": "Kekamoz", "d": "Karinada biriken sert kireç/kabuk tabakası; sürtünmeyi artırır, temizlenmesi gerekir.", "u": "/blog/kekamoz-temizligi/"},
  "en": {"t": "Hull scale", "d": "The hard lime/crust layer that builds up on the hull, increasing drag and needing removal.", "u": "/en/blog/hull-limescale-cleaning/"}},
 {"tr": {"t": "Raspa / Kumlama", "d": "Kat kat birikmiş eski boya/antifouling'in mekanik veya soda blasting ile sökülmesi.", "u": "/blog/raspa-kumlama/"},
  "en": {"t": "Blasting", "d": "Removing built-up old paint/antifouling by sanding or soda blasting.", "u": "/en/blog/blasting-soda-blasting/"}},
 {"tr": {"t": "Kışlatma", "d": "Sezon sonu tekneyi karaya çekme, yıkama, örtme ve güvenli depolama işlemleri.", "u": "/hizmetler/tekne-kislatma/"},
  "en": {"t": "Winterising", "d": "End-of-season haul-out, wash-down, covering and safe storage of the boat.", "u": "/en/services/winterising-storage/"}},
 {"tr": {"t": "Çekek", "d": "Teknenin karaya çekildiği alan; su altı işleri burada yapılır.", "u": "/blog/tekne-cekek-karaya-cekme/"},
  "en": {"t": "Hardstand / Haul-out", "d": "The area where a boat is hauled ashore; underwater work is done here.", "u": "/en/blog/boat-haul-out-guide/"}},
 {"tr": {"t": "Anot (Zinc)", "d": "Su altı metalleri galvanik korozyondan koruyan, kendini feda eden kurban parça.", "u": "/blog/anot-zinc-bakimi/"},
  "en": {"t": "Anode (Zinc)", "d": "A sacrificial part that protects underwater metals from galvanic corrosion.", "u": "/en/blog/anode-zinc-care/"}},
 {"tr": {"t": "2K poliüretan", "d": "İki bileşenli, çok dayanıklı ve yüksek parlaklıklı süperyat kalitesinde boya.", "u": "/blog/2k-poliuretan-boya/"},
  "en": {"t": "2K polyurethane", "d": "A two-part, highly durable, high-gloss superyacht-grade paint.", "u": "/en/blog/2k-polyurethane-paint/"}},
 {"tr": {"t": "Astar (Primer)", "d": "Boyanın altına uygulanan; yapışma, örtücülük ve korozyon koruması sağlayan kat.", "u": "/blog/astar-primer-nedir/"},
  "en": {"t": "Primer", "d": "The coat applied under paint for adhesion, coverage and corrosion protection.", "u": "/en/blog/primer-importance/"}},
 {"tr": {"t": "Sintine", "d": "Teknenin en dibindeki, su ve sızıntının toplandığı bölge; özel boyayla korunur.", "u": "/blog/sintine-boyasi/"},
  "en": {"t": "Bilge", "d": "The lowest part of the boat where water collects; protected with special paint.", "u": "/en/blog/bilge-paint/"}},
 {"tr": {"t": "Bimini / Tente", "d": "Kokpit üzerinde güneş ve yağmurdan koruyan kumaş örtü.", "u": "/blog/tente-branda-bimini/"},
  "en": {"t": "Bimini / Canvas", "d": "A fabric cover over the cockpit protecting from sun and rain.", "u": "/en/blog/marine-canvas-covers/"}},
 {"tr": {"t": "Cold-molding", "d": "İnce ahşap katmanların epoksiyle çapraz laminasyonu; güçlü, hafif ve su geçirmez gövde.", "u": "/blog/ahsap-epoksi-cold-molding/"},
  "en": {"t": "Cold-molding", "d": "Cross-laminating thin wood veneers with epoxy for a strong, light, waterproof hull.", "u": "/en/blog/cold-molding-epoxy/"}},
 {"tr": {"t": "Refit", "d": "Teknenin kapsamlı, çok kalemli yenilenmesi; genelde tek elden proje yönetimi ister.", "u": "/blog/refit-proje-yonetimi/"},
  "en": {"t": "Refit", "d": "A comprehensive, multi-item renewal of a boat; usually needs single-hand project management.", "u": "/en/blog/refit-project-management/"}},
 {"tr": {"t": "Detailing", "d": "İç-dış temizlik, pasta-polisaj ve jelkot koruma ile teknenin yüzeyini yenileme.", "u": "/hizmetler/tekne-detailing/"},
  "en": {"t": "Detailing", "d": "Renewing the boat's surface with interior-exterior cleaning, compound-polish and gelcoat protection.", "u": "/en/services/boat-detailing/"}},
]

# ==================================================================== BOAT TYPES (Tekne Tipleri)
BOATTYPES = [
{
 "slug": "yat-motoryat", "slug_en": "yacht-motoryacht", "image": "/assets/images/parallax-1.jpg",
 "tr": {
   "name": "Yat & Motoryat",
   "short": "Yat ve motoryat tamiri, bakımı, boyası ve refit; her sistemde uzmanlık.",
   "hero_title": "Yat ve Motoryat Bakım, Onarım ve Refit",
   "hero_sub": "Fiberglas onarımından boyaya, teak'ten iç mekana, detailing'den kışlatmaya — yat ve motoryatınız için tek elden profesyonel bakım.",
   "meta_title": "Yat & Motoryat Tamiri, Bakımı ve Refit | Tekne Usta",
   "meta_desc": "Yat ve motoryat tamiri, bakımı, boyama (antifouling), fiberglas/osmoz onarımı, teak döşeme, iç mekan yenileme ve kışlatma. İstanbul ve Ege'de tek elden yat servisi.",
   "body": """
<h2>Yat ve motoryatınız için bütünsel bakım</h2>
<p>Yat ve motoryatlar, birçok sistemin bir arada olduğu, yüksek beklentili teknelerdir. <strong>Tekne Usta</strong> olarak yat bakım ve onarımını tek elden yürütüyor; her kalemi şeffaf bir planla koordine ediyoruz.</p>
<h2>Yatınıza sunduğumuz hizmetler</h2>
<ul>
<li><a href="/hizmetler/fiberglas-onarim/">Fiberglas onarım ve osmoz tedavisi</a></li>
<li><a href="/hizmetler/tekne-boyama-antifouling/">Boya ve antifouling</a></li>
<li><a href="/hizmetler/teak-guverte-doseme/">Teak güverte döşeme</a></li>
<li><a href="/hizmetler/ic-mekan-yenileme/">İç mekan yenileme</a></li>
<li><a href="/hizmetler/tekne-detailing/">Temizlik & detailing</a></li>
<li><a href="/hizmetler/tekne-kislatma/">Kışlatma ve bakım</a></li>
</ul>
<h2>Kapsamlı refit tek elden</h2>
<p>Birden çok iş aynı dönemde yapılacaksa, <a href="/blog/refit-proje-yonetimi/">refit proje yönetimi</a> ile bütçe, takvim ve koordinasyonu sizin adınıza yürütürüz. Motor-mekanik işleri kapsamımız dışında; bu alanda güvendiğimiz servislere yönlendiriyoruz.</p>
<p>Yatınız İstanbul marinalarından Bodrum, Göcek ve Marmaris'e kadar hangi bölgedeyse <a href="/#bolgeler">yerinde keşif</a> yapıyoruz. Ücretsiz değerlendirme için <a href="#teklif-al">teklif formunu</a> doldurun.</p>
""",
 },
 "en": {
   "name": "Yacht & Motoryacht",
   "short": "Yacht and motoryacht repair, maintenance, painting and refit; expertise in every system.",
   "hero_title": "Yacht and Motoryacht Maintenance, Repair and Refit",
   "hero_sub": "From fibreglass repair to paint, teak to interior, detailing to winterising — single-hand professional care for your yacht and motoryacht.",
   "meta_title": "Yacht & Motoryacht Repair, Maintenance and Refit | Tekne Usta",
   "meta_desc": "Yacht and motoryacht repair, maintenance, painting (antifouling), fibreglass/osmosis repair, teak decking, interior refit and winterising. Single-hand yacht service in Istanbul and the Aegean.",
   "body": """
<h2>Holistic care for your yacht and motoryacht</h2>
<p>Yachts and motoryachts are high-expectation boats with many systems combined. At <strong>Tekne Usta</strong> we run yacht maintenance and repair from one hand, coordinating every item with a transparent plan.</p>
<h2>Services for your yacht</h2>
<ul>
<li><a href="/en/services/fibreglass-repair/">Fibreglass repair & osmosis treatment</a></li>
<li><a href="/en/services/boat-painting-antifouling/">Painting & antifouling</a></li>
<li><a href="/en/services/teak-deck/">Teak decking</a></li>
<li><a href="/en/services/interior-refit/">Interior refit</a></li>
<li><a href="/en/services/boat-detailing/">Cleaning & detailing</a></li>
<li><a href="/en/services/winterising-storage/">Winterising & maintenance</a></li>
</ul>
<h2>A full refit from one hand</h2>
<p>If several jobs happen in the same period, our <a href="/en/blog/refit-project-management/">refit project management</a> handles budget, schedule and coordination for you. Engine/mechanical work is outside our scope; we refer you to trusted services.</p>
<p>Wherever your yacht is — from Istanbul's marinas to Bodrum, Göcek and Marmaris — we do an <a href="/en/#bolgeler">on-site survey</a>. For a free assessment, fill in the <a href="#teklif-al">quote form</a>.</p>
""",
 },
},
{
 "slug": "yelkenli", "slug_en": "sailboat", "image": "/assets/images/parallax-2.jpg",
 "tr": {
   "name": "Yelkenli Tekne",
   "short": "Yelkenli tekne tamiri, bakımı, boyası, teak ve kışlatma.",
   "hero_title": "Yelkenli Tekne Tamiri ve Bakımı",
   "hero_sub": "Fiberglas ve klasik ahşap yelkenliler için osmoz, boya, teak, iç mekan ve kışlatma hizmetleri.",
   "meta_title": "Yelkenli Tekne Tamiri ve Bakımı | Tekne Usta",
   "meta_desc": "Yelkenli tekne tamiri, bakımı, osmoz tedavisi, antifouling boya, teak döşeme, ahşap yelkenli restorasyonu ve kışlatma. İstanbul ve Ege'de yelkenli servisi.",
   "body": """
<h2>Yelkenli sahiplerine özel bakım</h2>
<p>Yelkenli tekneler, gövde bakımı ve estetiğiyle özenli bir ilgi ister. Fiberglas ve klasik ahşap yelkenlilerde osmoz, boya, teak ve iç mekan işlerini deneyimle yapıyoruz.</p>
<h2>Yelkenliniz için hizmetler</h2>
<ul>
<li><a href="/hizmetler/fiberglas-onarim/">Fiberglas onarım ve osmoz tedavisi</a></li>
<li><a href="/hizmetler/tekne-boyama-antifouling/">Boya ve antifouling</a></li>
<li><a href="/hizmetler/teak-guverte-doseme/">Teak güverte döşeme</a></li>
<li><a href="/hizmetler/ahsap-tekne-renovasyonu/">Klasik ahşap yelkenli restorasyonu</a></li>
<li><a href="/hizmetler/ic-mekan-yenileme/">İç mekan yenileme</a></li>
<li><a href="/hizmetler/tekne-kislatma/">Kışlatma ve bakım</a></li>
</ul>
<h2>Kapsamımız</h2>
<p>Gövde, karina, boya, teak ve iç mekan tarafında tam hizmet veriyoruz. Direk, arma ve seyir donanımı (rigging) ile motor-mekanik işleri kapsamımız dışında; bunlar için ilgili servislere yönlendiriyoruz. Klasik ahşap yelkenlilerde <a href="/blog/kalafat-nedir/">kalafat</a> ve <a href="/blog/ahsap-tekne-vernik-bakimi/">vernik</a> işleri uzmanlığımızdır.</p>
<p>Yelkenliniz hangi marinada olursa olsun <a href="/#bolgeler">yerinde keşif</a> yapıyoruz. <a href="#teklif-al">Ücretsiz teklif</a> alın.</p>
""",
 },
 "en": {
   "name": "Sailboat",
   "short": "Sailboat repair, maintenance, painting, teak and winterising.",
   "hero_title": "Sailboat Repair and Maintenance",
   "hero_sub": "Osmosis, paint, teak, interior and winterising for fibreglass and classic wooden sailboats.",
   "meta_title": "Sailboat Repair and Maintenance | Tekne Usta",
   "meta_desc": "Sailboat repair, maintenance, osmosis treatment, antifouling, teak decking, classic wooden sailboat restoration and winterising in Istanbul and the Aegean.",
   "body": """
<h2>Care tailored to sailboat owners</h2>
<p>Sailboats need attentive care in hull maintenance and aesthetics. We handle osmosis, paint, teak and interior work on fibreglass and classic wooden sailboats with experience.</p>
<h2>Services for your sailboat</h2>
<ul>
<li><a href="/en/services/fibreglass-repair/">Fibreglass repair & osmosis treatment</a></li>
<li><a href="/en/services/boat-painting-antifouling/">Painting & antifouling</a></li>
<li><a href="/en/services/teak-deck/">Teak decking</a></li>
<li><a href="/en/services/wooden-boat-refit/">Classic wooden sailboat restoration</a></li>
<li><a href="/en/services/interior-refit/">Interior refit</a></li>
<li><a href="/en/services/winterising-storage/">Winterising & maintenance</a></li>
</ul>
<h2>Our scope</h2>
<p>We provide full service on hull, underbody, paint, teak and interior. Mast, rigging and engine/mechanical work are outside our scope; we refer you to relevant services. On classic wooden sailboats, <a href="/en/blog/caulking-explained/">caulking</a> and <a href="/en/blog/wooden-boat-varnish-care/">varnish</a> are our specialty.</p>
<p>Wherever your sailboat is berthed, we do an <a href="/en/#bolgeler">on-site survey</a>. Get a <a href="#teklif-al">free quote</a>.</p>
""",
 },
},
{
 "slug": "gulet", "slug_en": "gulet", "image": "/assets/images/parallax-3.jpg",
 "tr": {
   "name": "Gulet",
   "short": "Gulet bakımı, refit, ahşap restorasyon, teak ve boya.",
   "hero_title": "Gulet Bakım, Refit ve Restorasyon",
   "hero_sub": "Ahşap ve karma gövde guletler için kalafat, teak, boya, iç mekan ve kapsamlı refit.",
   "meta_title": "Gulet Bakım, Refit ve Restorasyon | Tekne Usta",
   "meta_desc": "Gulet bakımı, refit, ahşap restorasyon, kalafat, teak güverte, boya ve iç mekan yenileme. Ege ve İstanbul'da gulet servisi.",
   "body": """
<h2>Guletlere özel kapsamlı bakım</h2>
<p>Guletler, geniş ahşap yapıları ve konaklamalı kullanımıyla düzenli ve kapsamlı bakım ister. Ahşap ve karma gövde guletlerde restorasyon, kalafat, teak ve boya işlerini yapıyoruz.</p>
<h2>Guletiniz için hizmetler</h2>
<ul>
<li><a href="/hizmetler/ahsap-tekne-renovasyonu/">Ahşap restorasyon ve kalafat</a></li>
<li><a href="/hizmetler/teak-guverte-doseme/">Teak güverte döşeme</a></li>
<li><a href="/hizmetler/tekne-boyama-antifouling/">Boya ve antifouling</a></li>
<li><a href="/hizmetler/ic-mekan-yenileme/">İç mekan ve kabin yenileme</a></li>
<li><a href="/hizmetler/tekne-kislatma/">Kışlatma ve bakım</a></li>
</ul>
<h2>Kapsamlı refit</h2>
<p>Ticari kullanılan guletlerde sezon öncesi bakım kritik; küçük sorunlar sezonu aksatmadan çözülmeli. Çok kalemli işleri <a href="/blog/refit-proje-yonetimi/">tek elden proje yönetimi</a> ile planlıyoruz. Ahşap bakımında <a href="/blog/ustupu-kalafat-teknikleri/">geleneksel kalafat</a> ve modern epoksiyi birlikte kullanıyoruz.</p>
<p>Göcek, Bodrum, Marmaris ve Fethiye başta olmak üzere <a href="/#bolgeler">Ege genelinde</a> hizmet veriyoruz. <a href="#teklif-al">Teklif alın</a>.</p>
""",
 },
 "en": {
   "name": "Gulet",
   "short": "Gulet maintenance, refit, wooden restoration, teak and paint.",
   "hero_title": "Gulet Maintenance, Refit and Restoration",
   "hero_sub": "Caulking, teak, paint, interior and comprehensive refit for wooden and composite-hull gulets.",
   "meta_title": "Gulet Maintenance, Refit and Restoration | Tekne Usta",
   "meta_desc": "Gulet maintenance, refit, wooden restoration, caulking, teak decking, paint and interior renewal in the Aegean and Istanbul.",
   "body": """
<h2>Comprehensive care tailored to gulets</h2>
<p>Gulets, with their large wooden structures and overnight use, need regular, comprehensive care. We do restoration, caulking, teak and paint on wooden and composite-hull gulets.</p>
<h2>Services for your gulet</h2>
<ul>
<li><a href="/en/services/wooden-boat-refit/">Wooden restoration & caulking</a></li>
<li><a href="/en/services/teak-deck/">Teak decking</a></li>
<li><a href="/en/services/boat-painting-antifouling/">Painting & antifouling</a></li>
<li><a href="/en/services/interior-refit/">Interior & cabin renewal</a></li>
<li><a href="/en/services/winterising-storage/">Winterising & maintenance</a></li>
</ul>
<h2>Comprehensive refit</h2>
<p>On commercially used gulets, pre-season care is critical; small problems must be solved without disrupting the season. We plan multi-item work with <a href="/en/blog/refit-project-management/">single-hand project management</a>. In wood care we combine <a href="/en/blog/oakum-caulking-techniques/">traditional caulking</a> with modern epoxy.</p>
<p>We serve <a href="/en/#bolgeler">across the Aegean</a>, especially Göcek, Bodrum, Marmaris and Fethiye. <a href="#teklif-al">Get a quote</a>.</p>
""",
 },
},
{
 "slug": "rib-bot", "slug_en": "rib-tender", "image": "/assets/images/services/fiberglas.jpg",
 "tr": {
   "name": "RIB / Bot",
   "short": "RIB ve bot tamiri, fiberglas onarım, boya ve bakım.",
   "hero_title": "RIB ve Bot Tamiri & Bakımı",
   "hero_sub": "Fiberglas onarım, gelcoat, boya-antifouling ve genel bakım ile RIB ve botunuz sezona hazır.",
   "meta_title": "RIB ve Bot Tamiri, Bakımı | Tekne Usta",
   "meta_desc": "RIB ve bot tamiri, fiberglas onarım, gelcoat yenileme, antifouling boya, kaydırmaz güverte ve genel bakım. İstanbul ve Ege'de RIB/bot servisi.",
   "body": """
<h2>RIB ve botlar için pratik, hızlı bakım</h2>
<p>RIB ve botlar günübirlik yoğun kullanılan, dayanıklı ama bakım isteyen teknelerdir. Fiberglas gövde onarımı, gelcoat ve boya işlerini hızlı ve temiz yapıyoruz.</p>
<h2>RIB / botunuz için hizmetler</h2>
<ul>
<li><a href="/hizmetler/fiberglas-onarim/">Fiberglas onarım ve gelcoat</a></li>
<li><a href="/hizmetler/tekne-boyama-antifouling/">Boya ve antifouling</a></li>
<li><a href="/hizmetler/tekne-detailing/">Temizlik & detailing</a></li>
<li><a href="/hizmetler/tekne-kislatma/">Kışlatma ve bakım</a></li>
</ul>
<h2>Sık karşılaşılan işler</h2>
<p>Çarpma ve <a href="/blog/fiberglas-catlak-onarimi/">çatlak onarımı</a>, <a href="/blog/gelcoat-cizik-sararma-giderme/">gelcoat çizik/sararma</a> giderme, <a href="/blog/kaydirmaz-guverte-kaplama/">kaydırmaz güverte</a> ve su altı <a href="/blog/antifouling-secimi/">antifouling</a> RIB/botlarda en sık yaptığımız işler. Şişme yan tüp (pontoon) onarımı kapsamımız dışındadır.</p>
<p>İstanbul ve Ege'de <a href="/#bolgeler">yerinde servis</a>. <a href="#teklif-al">Teklif alın</a>.</p>
""",
 },
 "en": {
   "name": "RIB / Tender",
   "short": "RIB and tender repair, fibreglass repair, paint and maintenance.",
   "hero_title": "RIB and Tender Repair & Maintenance",
   "hero_sub": "Fibreglass repair, gelcoat, paint-antifouling and general care to get your RIB and tender season-ready.",
   "meta_title": "RIB and Tender Repair, Maintenance | Tekne Usta",
   "meta_desc": "RIB and tender repair, fibreglass repair, gelcoat renewal, antifouling, non-slip deck and general maintenance in Istanbul and the Aegean.",
   "body": """
<h2>Practical, fast care for RIBs and tenders</h2>
<p>RIBs and tenders are heavily used day boats — durable but needing care. We do fibreglass hull repair, gelcoat and paint work fast and clean.</p>
<h2>Services for your RIB / tender</h2>
<ul>
<li><a href="/en/services/fibreglass-repair/">Fibreglass repair & gelcoat</a></li>
<li><a href="/en/services/boat-painting-antifouling/">Painting & antifouling</a></li>
<li><a href="/en/services/boat-detailing/">Cleaning & detailing</a></li>
<li><a href="/en/services/winterising-storage/">Winterising & maintenance</a></li>
</ul>
<h2>Common jobs</h2>
<p>Impact and <a href="/en/blog/fibreglass-crack-repair/">crack repair</a>, <a href="/en/blog/gelcoat-scratch-yellowing/">gelcoat scratch/yellowing</a> removal, <a href="/en/blog/non-slip-deck-coating/">non-slip deck</a> and underwater <a href="/en/blog/choosing-antifouling/">antifouling</a> are our most common RIB/tender jobs. Inflatable tube (pontoon) repair is outside our scope.</p>
<p><a href="/en/#bolgeler">On-site service</a> in Istanbul and the Aegean. <a href="#teklif-al">Get a quote</a>.</p>
""",
 },
},
{
 "slug": "surat-teknesi", "slug_en": "speedboat", "image": "/assets/images/services/boya.jpg",
 "tr": {
   "name": "Sürat Teknesi",
   "short": "Sürat teknesi bakımı, fiberglas onarım, boya ve gelcoat.",
   "hero_title": "Sürat Teknesi Bakımı ve Onarımı",
   "hero_sub": "Yüksek hızlı tekneler için fiberglas onarım, sert antifouling, gelcoat ve detailing.",
   "meta_title": "Sürat Teknesi Bakımı ve Onarımı | Tekne Usta",
   "meta_desc": "Sürat teknesi bakımı, fiberglas onarım, gelcoat yenileme, sert (hard) antifouling boya ve detailing. İstanbul ve Ege'de sürat teknesi servisi.",
   "body": """
<h2>Sürat teknenizin performansı için</h2>
<p>Sürat teknelerinde karinanın pürüzsüzlüğü performansı ve yakıtı doğrudan etkiler. Fiberglas onarım, gelcoat ve doğru <a href="/blog/antifouling-secimi/">antifouling</a> seçimiyle teknenizi hızlı ve temiz tutuyoruz.</p>
<h2>Sürat tekneniz için hizmetler</h2>
<ul>
<li><a href="/hizmetler/fiberglas-onarim/">Fiberglas onarım ve gelcoat</a></li>
<li><a href="/hizmetler/tekne-boyama-antifouling/">Boya ve sert antifouling</a></li>
<li><a href="/hizmetler/tekne-detailing/">Pasta-polisaj & detailing</a></li>
<li><a href="/hizmetler/tekne-kislatma/">Kışlatma ve bakım</a></li>
</ul>
<h2>Neden sert antifouling?</h2>
<p>Yüksek hızlı ve sık çekilen teknelerde, aşınmayan <strong>sert matris antifouling</strong> daha uygundur; pürüzsüz karina hız ve verimlilik demektir. Detay için <a href="/blog/antifouling-secimi/">antifouling seçim rehberimize</a> bakın. Parlak bir gövde için düzenli <a href="/blog/gelcoat-yenileme/">gelcoat</a> bakımı ve pasta-polisaj öneriyoruz.</p>
<p>İstanbul ve Ege'de <a href="/#bolgeler">yerinde keşif</a>. <a href="#teklif-al">Teklif alın</a>.</p>
""",
 },
 "en": {
   "name": "Speedboat",
   "short": "Speedboat maintenance, fibreglass repair, paint and gelcoat.",
   "hero_title": "Speedboat Maintenance and Repair",
   "hero_sub": "Fibreglass repair, hard antifouling, gelcoat and detailing for high-speed boats.",
   "meta_title": "Speedboat Maintenance and Repair | Tekne Usta",
   "meta_desc": "Speedboat maintenance, fibreglass repair, gelcoat renewal, hard antifouling and detailing in Istanbul and the Aegean.",
   "body": """
<h2>For your speedboat's performance</h2>
<p>On speedboats, a smooth hull directly affects performance and fuel. With fibreglass repair, gelcoat and the right <a href="/en/blog/choosing-antifouling/">antifouling</a>, we keep your boat fast and clean.</p>
<h2>Services for your speedboat</h2>
<ul>
<li><a href="/en/services/fibreglass-repair/">Fibreglass repair & gelcoat</a></li>
<li><a href="/en/services/boat-painting-antifouling/">Paint & hard antifouling</a></li>
<li><a href="/en/services/boat-detailing/">Compound-polish & detailing</a></li>
<li><a href="/en/services/winterising-storage/">Winterising & maintenance</a></li>
</ul>
<h2>Why hard antifouling?</h2>
<p>On fast, frequently hauled boats, non-eroding <strong>hard matrix antifouling</strong> suits better; a smooth hull means speed and efficiency. For detail, see our <a href="/en/blog/choosing-antifouling/">antifouling guide</a>. For a glossy hull we recommend regular <a href="/en/blog/gelcoat-renewal/">gelcoat</a> care and compound-polish.</p>
<p><a href="/en/#bolgeler">On-site survey</a> in Istanbul and the Aegean. <a href="#teklif-al">Get a quote</a>.</p>
""",
 },
},
{
 "slug": "fiber-tekne", "slug_en": "fibreglass-boat", "image": "/assets/images/services/fiberglas.jpg",
 "tr": {
   "name": "Fiber Tekne",
   "short": "Fiber (fiberglas) tekne tamiri, osmoz, gelcoat ve boya.",
   "hero_title": "Fiber Tekne Tamiri ve Bakımı",
   "hero_sub": "Fiberglas gövdeli teknelerde osmoz tedavisi, çatlak onarımı, gelcoat ve boya.",
   "meta_title": "Fiber Tekne Tamiri ve Bakımı | Tekne Usta",
   "meta_desc": "Fiber (fiberglas) tekne tamiri, osmoz tedavisi, gelcoat yenileme, çatlak/kırık onarımı, antifouling boya ve bakım. İstanbul ve Ege'de fiber tekne servisi.",
   "body": """
<h2>Fiber teknenizde uzman eli</h2>
<p>Fiber (fiberglas/GRP) tekneler dayanıklıdır ama osmoz, gelcoat solması ve çatlak gibi sorunlar yaşar. Bu alanda en güçlü olduğumuz konularda size tam hizmet veriyoruz.</p>
<h2>Fiber tekneniz için hizmetler</h2>
<ul>
<li><a href="/hizmetler/fiberglas-onarim/">Fiberglas onarım ve osmoz tedavisi</a></li>
<li><a href="/hizmetler/tekne-boyama-antifouling/">Boya ve antifouling</a></li>
<li><a href="/hizmetler/teak-guverte-doseme/">Teak / kaydırmaz güverte</a></li>
<li><a href="/hizmetler/ic-mekan-yenileme/">İç mekan yenileme</a></li>
<li><a href="/hizmetler/tekne-kislatma/">Kışlatma ve bakım</a></li>
</ul>
<h2>Sık yapılan işler</h2>
<p><a href="/blog/osmoz-nedir-tedavisi/">Osmoz tedavisi</a>, <a href="/blog/fiberglas-catlak-onarimi/">çatlak/kırık onarımı</a>, <a href="/blog/gelcoat-yenileme/">gelcoat yenileme</a> ve <a href="/blog/su-alti-yapisal-onarim/">su altı yapısal onarım</a> fiber teknelerde uzmanlığımızdır. Reçine uyumu için <a href="/blog/polyester-vs-epoksi-recine/">polyester vs epoksi</a> yazımıza bakın.</p>
<p>İstanbul ve Ege'de <a href="/#bolgeler">yerinde keşif</a>. <a href="#teklif-al">Ücretsiz teklif</a> alın.</p>
""",
 },
 "en": {
   "name": "Fibreglass Boat",
   "short": "Fibreglass boat repair, osmosis, gelcoat and paint.",
   "hero_title": "Fibreglass Boat Repair and Maintenance",
   "hero_sub": "Osmosis treatment, crack repair, gelcoat and paint for fibreglass-hulled boats.",
   "meta_title": "Fibreglass Boat Repair and Maintenance | Tekne Usta",
   "meta_desc": "Fibreglass boat repair, osmosis treatment, gelcoat renewal, crack/break repair, antifouling and maintenance in Istanbul and the Aegean.",
   "body": """
<h2>A craftsman's hand on your fibreglass boat</h2>
<p>Fibreglass (GRP) boats are durable but face osmosis, gelcoat fading and cracks. We provide full service in exactly the areas where we're strongest.</p>
<h2>Services for your fibreglass boat</h2>
<ul>
<li><a href="/en/services/fibreglass-repair/">Fibreglass repair & osmosis treatment</a></li>
<li><a href="/en/services/boat-painting-antifouling/">Painting & antifouling</a></li>
<li><a href="/en/services/teak-deck/">Teak / non-slip deck</a></li>
<li><a href="/en/services/interior-refit/">Interior refit</a></li>
<li><a href="/en/services/winterising-storage/">Winterising & maintenance</a></li>
</ul>
<h2>Common jobs</h2>
<p><a href="/en/blog/what-is-osmosis-treatment/">Osmosis treatment</a>, <a href="/en/blog/fibreglass-crack-repair/">crack/break repair</a>, <a href="/en/blog/gelcoat-renewal/">gelcoat renewal</a> and <a href="/en/blog/underwater-structural-repair/">underwater structural repair</a> are our specialty on fibreglass boats. For resin compatibility, see <a href="/en/blog/polyester-vs-epoxy-resin/">polyester vs epoxy</a>.</p>
<p><a href="/en/#bolgeler">On-site survey</a> in Istanbul and the Aegean. Get a <a href="#teklif-al">free quote</a>.</p>
""",
 },
},
{
 "slug": "ahsap-tekne", "slug_en": "wooden-boat", "image": "/assets/images/services/ahsap.jpg",
 "tr": {
   "name": "Ahşap Tekne",
   "short": "Ahşap tekne tamiri, restorasyon, kalafat, vernik ve teak.",
   "hero_title": "Ahşap Tekne Tamiri, Bakımı ve Restorasyonu",
   "hero_sub": "Klasik ahşap teknelerde özgün dokuyu koruyarak kalafat, çürük onarımı, vernik ve teak.",
   "meta_title": "Ahşap Tekne Tamiri ve Restorasyonu | Tekne Usta",
   "meta_desc": "Ahşap tekne tamiri, bakımı, restorasyonu, kalafat, çürük onarımı, vernik, teak ve kışlatma. İstanbul ve Ege'de ahşap tekne servisi, özgün dokuya saygılı işçilik.",
   "body": """
<h2>Ahşap tekneniz güvenli ellerde</h2>
<p>Ahşap tekneler sabır ve ustalık ister. Geleneksel kalafat ve marangozluğu modern epoksiyle birleştirerek, teknenizin özgün dokusunu bozmadan sağlamlaştırıyoruz.</p>
<h2>Ahşap tekneniz için hizmetler</h2>
<ul>
<li><a href="/hizmetler/ahsap-tekne-renovasyonu/">Ahşap renovasyon, kalafat ve çürük onarımı</a></li>
<li><a href="/hizmetler/teak-guverte-doseme/">Teak güverte döşeme</a></li>
<li><a href="/hizmetler/tekne-boyama-antifouling/">Boya, vernik ve antifouling</a></li>
<li><a href="/hizmetler/ic-mekan-yenileme/">İç mekan yenileme</a></li>
<li><a href="/hizmetler/tekne-kislatma/">Kışlatma ve bakım</a></li>
</ul>
<h2>Uzmanlık alanlarımız</h2>
<p><a href="/blog/kalafat-nedir/">Kalafat</a>, <a href="/blog/ahsap-curuk-onarimi/">çürük onarımı</a>, <a href="/blog/ahsap-tekne-vernik-bakimi/">vernik bakımı</a> ve <a href="/blog/epoksi-ile-ahsap-guclendirme/">epoksi güçlendirme</a> ahşap teknelerde uzmanlığımızdır. Klasik tekne değeri için <a href="/blog/klasik-tekne-degeri/">bu yazıya</a>, kışlatma inceliği için <a href="/blog/ahsap-tekne-kislatma/">bu yazıya</a> bakın.</p>
<p>İstanbul ve Ege'de <a href="/#bolgeler">yerinde keşif</a>. <a href="#teklif-al">Teklif alın</a>.</p>
""",
 },
 "en": {
   "name": "Wooden Boat",
   "short": "Wooden boat repair, restoration, caulking, varnish and teak.",
   "hero_title": "Wooden Boat Repair, Maintenance and Restoration",
   "hero_sub": "Caulking, rot repair, varnish and teak on classic wooden boats, preserving their original character.",
   "meta_title": "Wooden Boat Repair and Restoration | Tekne Usta",
   "meta_desc": "Wooden boat repair, maintenance, restoration, caulking, rot repair, varnish, teak and winterising in Istanbul and the Aegean, with respect for original character.",
   "body": """
<h2>Your wooden boat in safe hands</h2>
<p>Wooden boats demand patience and skill. Combining traditional caulking and joinery with modern epoxy, we strengthen your boat without spoiling its original character.</p>
<h2>Services for your wooden boat</h2>
<ul>
<li><a href="/en/services/wooden-boat-refit/">Wooden refit, caulking & rot repair</a></li>
<li><a href="/en/services/teak-deck/">Teak decking</a></li>
<li><a href="/en/services/boat-painting-antifouling/">Paint, varnish & antifouling</a></li>
<li><a href="/en/services/interior-refit/">Interior refit</a></li>
<li><a href="/en/services/winterising-storage/">Winterising & maintenance</a></li>
</ul>
<h2>Our specialties</h2>
<p><a href="/en/blog/caulking-explained/">Caulking</a>, <a href="/en/blog/wood-rot-repair/">rot repair</a>, <a href="/en/blog/wooden-boat-varnish-care/">varnish care</a> and <a href="/en/blog/epoxy-wood-reinforcement/">epoxy reinforcement</a> are our specialty on wooden boats. For classic boat value see <a href="/en/blog/classic-boat-value/">this article</a>, and for winterising nuance <a href="/en/blog/wooden-boat-winterising/">this one</a>.</p>
<p><a href="/en/#bolgeler">On-site survey</a> in Istanbul and the Aegean. <a href="#teklif-al">Get a quote</a>.</p>
""",
 },
},
{
 "slug": "aluminyum-tekne", "slug_en": "aluminium-boat", "image": "/assets/images/services/boya.jpg",
 "tr": {
   "name": "Alüminyum Tekne",
   "short": "Alüminyum tekne boyama, bakırsız antifouling ve yüzey bakımı.",
   "hero_title": "Alüminyum Tekne Boyama ve Bakımı",
   "hero_sub": "Alüminyum gövdelerde korozyona karşı bakırsız antifouling, doğru astar sistemi ve yüzey bakımı.",
   "meta_title": "Alüminyum Tekne Boyama ve Bakımı | Tekne Usta",
   "meta_desc": "Alüminyum tekne boyama, bakırsız antifouling, doğru astar sistemi, yüzey hazırlığı ve detailing. İstanbul ve Ege'de alüminyum tekne boya servisi.",
   "body": """
<h2>Alüminyum teknelerde doğru boya sistemi</h2>
<p>Alüminyum tekneler boya konusunda özel kurallara tabidir; yanlış sistem korozyona yol açar. Bu alanda doğru astar ve <strong>bakırsız antifouling</strong> ile hizmet veriyoruz.</p>
<h2>Alüminyum tekneniz için hizmetler</h2>
<ul>
<li><a href="/hizmetler/tekne-boyama-antifouling/">Boya ve bakırsız antifouling</a></li>
<li><a href="/hizmetler/tekne-detailing/">Yüzey bakımı & detailing</a></li>
<li><a href="/hizmetler/tekne-kislatma/">Kışlatma ve bakım</a></li>
</ul>
<h2>En kritik konu: bakırsız antifouling</h2>
<p>Bakır içeren boyalar alüminyumla temas ettiğinde <a href="/blog/anot-zinc-bakimi/">galvanik korozyonu</a> tetikler; bu yüzden mutlaka <strong>bakırsız</strong> formül ve doğru <a href="/blog/astar-primer-nedir/">astar sistemi</a> kullanılır. Detay için <a href="/blog/aluminyum-tekne-boyama/">alüminyum tekne boyama</a> yazımıza bakın. <em>Not: alüminyum kaynak ve yapısal işler kapsamımız dışındadır; boya ve yüzey tarafında hizmet veriyoruz.</em></p>
<p>İstanbul ve Ege'de <a href="/#bolgeler">yerinde keşif</a>. <a href="#teklif-al">Teklif alın</a>.</p>
""",
 },
 "en": {
   "name": "Aluminium Boat",
   "short": "Aluminium boat painting, copper-free antifouling and surface care.",
   "hero_title": "Aluminium Boat Painting and Care",
   "hero_sub": "Copper-free antifouling against corrosion, the right primer system and surface care for aluminium hulls.",
   "meta_title": "Aluminium Boat Painting and Care | Tekne Usta",
   "meta_desc": "Aluminium boat painting, copper-free antifouling, the right primer system, surface prep and detailing in Istanbul and the Aegean.",
   "body": """
<h2>The right paint system on aluminium boats</h2>
<p>Aluminium boats follow special paint rules; the wrong system causes corrosion. We serve this area with the right primer and <strong>copper-free antifouling</strong>.</p>
<h2>Services for your aluminium boat</h2>
<ul>
<li><a href="/en/services/boat-painting-antifouling/">Paint & copper-free antifouling</a></li>
<li><a href="/en/services/boat-detailing/">Surface care & detailing</a></li>
<li><a href="/en/services/winterising-storage/">Winterising & maintenance</a></li>
</ul>
<h2>The critical issue: copper-free antifouling</h2>
<p>Copper-based paints in contact with aluminium trigger <a href="/en/blog/anode-zinc-care/">galvanic corrosion</a>; so a <strong>copper-free</strong> formula and the right <a href="/en/blog/primer-importance/">primer system</a> are essential. For detail see our <a href="/en/blog/aluminium-boat-painting/">aluminium boat painting</a> article. <em>Note: aluminium welding and structural work are outside our scope; we serve on the paint and surface side.</em></p>
<p><a href="/en/#bolgeler">On-site survey</a> in Istanbul and the Aegean. <a href="#teklif-al">Get a quote</a>.</p>
""",
 },
},
]

# ==================================================================== TYPE x LOCATION (curated) — Dalga 3
TYPE_LOCATION = [
{
 "slug": "gocek-yat-motoryat", "slug_en": "gocek-yacht-motoryacht", "image": "/assets/images/parallax-3.jpg",
 "tr": {
   "name": "Yat & Motoryat Bakımı", "region_name": "Göcek", "region_url": "/bolgeler/gocek/",
   "hero_title": "Göcek'te Yat ve Motoryat Bakım-Onarım",
   "hero_sub": "D-Marin Göcek, Club Marina ve Marinturk çevresindeki yat ve motoryatlar için fiberglas, boya, teak ve kışlatma.",
   "meta_title": "Göcek Yat & Motoryat Bakım-Onarım | Tekne Usta",
   "meta_desc": "Göcek'te yat ve motoryat bakımı, fiberglas onarımı, boya-antifouling, teak döşeme ve kışlatma. D-Marin Göcek, Club Marina ve Marinturk çevresinde servis.",
   "body": """
<p>Göcek, Türkiye'nin en yoğun yat üslerinden biri; <strong>D-Marin Göcek, Club Marina ve Marinturk</strong> çevresinde çok sayıda yat ve motoryat kışlar ve bakım görür. Bu tekneler için tek elden bakım ve onarım sunuyoruz.</p>
<h2>Göcek'te yatınıza sunduğumuz hizmetler</h2>
<ul>
<li><a href="/hizmetler/fiberglas-onarim/">Fiberglas onarım ve osmoz tedavisi</a></li>
<li><a href="/hizmetler/tekne-boyama-antifouling/">Boya ve antifouling</a></li>
<li><a href="/hizmetler/teak-guverte-doseme/">Teak güverte döşeme</a></li>
<li><a href="/hizmetler/tekne-detailing/">Detailing</a> ve <a href="/hizmetler/ic-mekan-yenileme/">iç mekan yenileme</a></li>
<li><a href="/hizmetler/tekne-kislatma/">Kışlatma ve bakım</a></li>
</ul>
<p>Göcek'in korunaklı koyları sezon boyunca yoğun kullanım demek; sezon öncesi ve sonrası bakım kritik. Yat bakımı hakkında genel bilgi için <a href="/tekneler/yat-motoryat/">yat & motoryat</a> sayfamıza, Göcek'teki diğer hizmetler için <a href="/bolgeler/gocek/">Göcek bölge sayfamıza</a> bakın.</p>
<p>Ücretsiz yerinde keşif için <a href="#teklif-al">teklif formunu</a> doldurun.</p>
""",
 },
 "en": {
   "name": "Yacht & Motoryacht Care", "region_name": "Göcek", "region_url": "/en/regions/gocek/",
   "hero_title": "Yacht and Motoryacht Care in Göcek",
   "hero_sub": "Fibreglass, paint, teak and winterising for yachts and motoryachts around D-Marin Göcek, Club Marina and Marinturk.",
   "meta_title": "Göcek Yacht & Motoryacht Care | Tekne Usta",
   "meta_desc": "Yacht and motoryacht care, fibreglass repair, painting-antifouling, teak decking and winterising in Göcek. Service around D-Marin Göcek, Club Marina and Marinturk.",
   "body": """
<p>Göcek is one of Turkey's busiest yacht bases; many yachts and motoryachts winter and are maintained around <strong>D-Marin Göcek, Club Marina and Marinturk</strong>. We offer single-hand care and repair for these boats.</p>
<h2>Services for your yacht in Göcek</h2>
<ul>
<li><a href="/en/services/fibreglass-repair/">Fibreglass repair & osmosis treatment</a></li>
<li><a href="/en/services/boat-painting-antifouling/">Painting & antifouling</a></li>
<li><a href="/en/services/teak-deck/">Teak decking</a></li>
<li><a href="/en/services/boat-detailing/">Detailing</a> and <a href="/en/services/interior-refit/">interior refit</a></li>
<li><a href="/en/services/winterising-storage/">Winterising & maintenance</a></li>
</ul>
<p>Göcek's sheltered bays mean heavy seasonal use; pre- and post-season care is critical. For general info on yacht care see our <a href="/en/boats/yacht-motoryacht/">yacht & motoryacht</a> page, and for other services in Göcek our <a href="/en/regions/gocek/">Göcek region page</a>.</p>
<p>For a free on-site survey, fill in the <a href="#teklif-al">quote form</a>.</p>
""",
 },
},
{
 "slug": "gocek-gulet", "slug_en": "gocek-gulet", "image": "/assets/images/parallax-2.jpg",
 "tr": {
   "name": "Gulet Bakım & Refit", "region_name": "Göcek", "region_url": "/bolgeler/gocek/",
   "hero_title": "Göcek'te Gulet Bakım, Refit ve Restorasyon",
   "hero_sub": "Mavi yolculuk guletleri için ahşap restorasyon, kalafat, teak, boya ve iç mekan yenileme.",
   "meta_title": "Göcek Gulet Bakım, Refit ve Restorasyon | Tekne Usta",
   "meta_desc": "Göcek'te gulet bakımı, refit, ahşap restorasyon, kalafat, teak ve iç mekan yenileme. Skopea koyları ve Göcek marinaları çevresinde gulet servisi.",
   "body": """
<p>Göcek ve çevresindeki Skopea koyları, mavi yolculuk guletlerinin kalbidir. Ahşap ve karma gövde guletlerde kapsamlı bakım, refit ve restorasyon yapıyoruz.</p>
<h2>Göcek'te guletinize hizmetler</h2>
<ul>
<li><a href="/hizmetler/ahsap-tekne-renovasyonu/">Ahşap restorasyon ve kalafat</a></li>
<li><a href="/hizmetler/teak-guverte-doseme/">Teak güverte döşeme</a></li>
<li><a href="/hizmetler/tekne-boyama-antifouling/">Boya, vernik ve antifouling</a></li>
<li><a href="/hizmetler/ic-mekan-yenileme/">Kabin ve salon yenileme</a></li>
<li><a href="/hizmetler/tekne-kislatma/">Kışlatma ve bakım</a></li>
</ul>
<p>Ticari kullanılan guletlerde sezon öncesi bakım şart; küçük sorunlar sezonu aksatmadan çözülmeli. Çok kalemli işleri <a href="/blog/refit-proje-yonetimi/">tek elden proje yönetimiyle</a> yürütürüz. Genel bilgi için <a href="/tekneler/gulet/">gulet</a> ve <a href="/bolgeler/gocek/">Göcek</a> sayfalarımıza bakın.</p>
<p>Sezon öncesi <a href="#teklif-al">ücretsiz keşif</a> için bize yazın.</p>
""",
 },
 "en": {
   "name": "Gulet Maintenance & Refit", "region_name": "Göcek", "region_url": "/en/regions/gocek/",
   "hero_title": "Gulet Maintenance, Refit and Restoration in Göcek",
   "hero_sub": "Wooden restoration, caulking, teak, paint and interior renewal for blue-cruise gulets.",
   "meta_title": "Göcek Gulet Maintenance, Refit and Restoration | Tekne Usta",
   "meta_desc": "Gulet maintenance, refit, wooden restoration, caulking, teak and interior renewal in Göcek. Gulet service around the Skopea bays and Göcek marinas.",
   "body": """
<p>Göcek and the surrounding Skopea bays are the heart of blue-cruise gulets. We do comprehensive care, refit and restoration on wooden and composite-hull gulets.</p>
<h2>Services for your gulet in Göcek</h2>
<ul>
<li><a href="/en/services/wooden-boat-refit/">Wooden restoration & caulking</a></li>
<li><a href="/en/services/teak-deck/">Teak decking</a></li>
<li><a href="/en/services/boat-painting-antifouling/">Paint, varnish & antifouling</a></li>
<li><a href="/en/services/interior-refit/">Cabin and saloon renewal</a></li>
<li><a href="/en/services/winterising-storage/">Winterising & maintenance</a></li>
</ul>
<p>On commercial gulets, pre-season care is essential; small problems must be solved without disrupting the season. We run multi-item work with <a href="/en/blog/refit-project-management/">single-hand project management</a>. For general info, see our <a href="/en/boats/gulet/">gulet</a> and <a href="/en/regions/gocek/">Göcek</a> pages.</p>
<p>For a pre-season <a href="#teklif-al">free survey</a>, message us.</p>
""",
 },
},
{
 "slug": "bodrum-yat-motoryat", "slug_en": "bodrum-yacht-motoryacht", "image": "/assets/images/parallax-1.jpg",
 "tr": {
   "name": "Yat & Motoryat Bakımı", "region_name": "Bodrum", "region_url": "/bolgeler/bodrum/",
   "hero_title": "Bodrum'da Yat ve Motoryat Bakım-Onarım",
   "hero_sub": "Yalıkavak Marina ve Milta Bodrum Marina çevresindeki yat ve motoryatlar için fiberglas, boya, teak ve detailing.",
   "meta_title": "Bodrum Yat & Motoryat Bakım-Onarım | Tekne Usta",
   "meta_desc": "Bodrum'da yat ve motoryat bakımı, fiberglas onarımı, boya-antifouling, teak döşeme ve detailing. Yalıkavak ve Milta Bodrum Marina çevresinde servis.",
   "body": """
<p>Bodrum, Ege'nin en canlı yat merkezlerinden; <strong>Yalıkavak Marina ve Milta Bodrum Marina</strong> çevresinde çok sayıda yat ve motoryat bakım görür. Bu premium teknelere detay ve bitiş kalitesiyle hizmet veriyoruz.</p>
<h2>Bodrum'da yatınıza hizmetler</h2>
<ul>
<li><a href="/hizmetler/fiberglas-onarim/">Fiberglas onarım ve gelcoat</a></li>
<li><a href="/hizmetler/tekne-boyama-antifouling/">Boya ve antifouling</a></li>
<li><a href="/hizmetler/teak-guverte-doseme/">Teak güverte döşeme</a></li>
<li><a href="/hizmetler/tekne-detailing/">Detailing</a> ve <a href="/hizmetler/ic-mekan-yenileme/">iç mekan yenileme</a></li>
<li><a href="/hizmetler/tekne-kislatma/">Kışlatma ve bakım</a></li>
</ul>
<p>Özellikle Yalıkavak gibi prestijli üslerde detay ve bitiş kalitesi fark yaratır. Genel bilgi için <a href="/tekneler/yat-motoryat/">yat & motoryat</a>, Bodrum için <a href="/bolgeler/bodrum/">Bodrum</a> ve <a href="/bolgeler/yalikavak/">Yalıkavak</a> sayfalarımıza bakın.</p>
<p><a href="#teklif-al">Ücretsiz keşif</a> alın.</p>
""",
 },
 "en": {
   "name": "Yacht & Motoryacht Care", "region_name": "Bodrum", "region_url": "/en/regions/bodrum/",
   "hero_title": "Yacht and Motoryacht Care in Bodrum",
   "hero_sub": "Fibreglass, paint, teak and detailing for yachts and motoryachts around Yalıkavak Marina and Milta Bodrum Marina.",
   "meta_title": "Bodrum Yacht & Motoryacht Care | Tekne Usta",
   "meta_desc": "Yacht and motoryacht care, fibreglass repair, painting-antifouling, teak decking and detailing in Bodrum. Service around Yalıkavak and Milta Bodrum Marina.",
   "body": """
<p>Bodrum is one of the Aegean's liveliest yachting hubs; many yachts and motoryachts are maintained around <strong>Yalıkavak Marina and Milta Bodrum Marina</strong>. We serve these premium boats with detail and finish quality.</p>
<h2>Services for your yacht in Bodrum</h2>
<ul>
<li><a href="/en/services/fibreglass-repair/">Fibreglass repair & gelcoat</a></li>
<li><a href="/en/services/boat-painting-antifouling/">Painting & antifouling</a></li>
<li><a href="/en/services/teak-deck/">Teak decking</a></li>
<li><a href="/en/services/boat-detailing/">Detailing</a> and <a href="/en/services/interior-refit/">interior refit</a></li>
<li><a href="/en/services/winterising-storage/">Winterising & maintenance</a></li>
</ul>
<p>Especially at prestigious bases like Yalıkavak, detail and finish quality make the difference. For general info see <a href="/en/boats/yacht-motoryacht/">yacht & motoryacht</a>, and for Bodrum our <a href="/en/regions/bodrum/">Bodrum</a> and <a href="/en/regions/yalikavak/">Yalıkavak</a> pages.</p>
<p>Get a <a href="#teklif-al">free survey</a>.</p>
""",
 },
},
{
 "slug": "bodrum-gulet", "slug_en": "bodrum-gulet", "image": "/assets/images/services/ahsap.jpg",
 "tr": {
   "name": "Gulet Bakım & Refit", "region_name": "Bodrum", "region_url": "/bolgeler/bodrum/",
   "hero_title": "Bodrum'da Gulet Bakım, Refit ve Restorasyon",
   "hero_sub": "Bodrum'un ahşap tekne geleneğindeki guletler için restorasyon, kalafat, teak ve boya.",
   "meta_title": "Bodrum Gulet Bakım, Refit ve Restorasyon | Tekne Usta",
   "meta_desc": "Bodrum'da gulet bakımı, refit, ahşap restorasyon, kalafat, teak ve boya. Bodrum'un gulet geleneğine uygun ustalıkla servis.",
   "body": """
<p>Bodrum, ahşap gulet inşa geleneğinin merkezidir; bölgede çok sayıda ahşap ve karma gövde gulet bakım ve refit görür. Bu geleneğe uygun ustalıkla çalışıyoruz.</p>
<h2>Bodrum'da guletinize hizmetler</h2>
<ul>
<li><a href="/hizmetler/ahsap-tekne-renovasyonu/">Ahşap restorasyon ve kalafat</a></li>
<li><a href="/hizmetler/teak-guverte-doseme/">Teak güverte döşeme</a></li>
<li><a href="/hizmetler/tekne-boyama-antifouling/">Boya, vernik ve antifouling</a></li>
<li><a href="/hizmetler/ic-mekan-yenileme/">Kabin ve salon yenileme</a></li>
<li><a href="/hizmetler/tekne-kislatma/">Kışlatma ve bakım</a></li>
</ul>
<p>Ahşap bakımında <a href="/blog/ustupu-kalafat-teknikleri/">geleneksel kalafat</a> ile modern epoksiyi birlikte kullanıyor, özgün dokuyu koruyoruz. Genel bilgi için <a href="/tekneler/gulet/">gulet</a> ve <a href="/bolgeler/bodrum/">Bodrum</a> sayfalarımıza bakın.</p>
<p>Sezon öncesi <a href="#teklif-al">ücretsiz keşif</a> için bize yazın.</p>
""",
 },
 "en": {
   "name": "Gulet Maintenance & Refit", "region_name": "Bodrum", "region_url": "/en/regions/bodrum/",
   "hero_title": "Gulet Maintenance, Refit and Restoration in Bodrum",
   "hero_sub": "Restoration, caulking, teak and paint for gulets in Bodrum's wooden boatbuilding tradition.",
   "meta_title": "Bodrum Gulet Maintenance, Refit and Restoration | Tekne Usta",
   "meta_desc": "Gulet maintenance, refit, wooden restoration, caulking, teak and paint in Bodrum. Craftsmanship suited to Bodrum's gulet tradition.",
   "body": """
<p>Bodrum is the heart of the wooden gulet building tradition; many wooden and composite-hull gulets are maintained and refitted in the area. We work with craftsmanship suited to this tradition.</p>
<h2>Services for your gulet in Bodrum</h2>
<ul>
<li><a href="/en/services/wooden-boat-refit/">Wooden restoration & caulking</a></li>
<li><a href="/en/services/teak-deck/">Teak decking</a></li>
<li><a href="/en/services/boat-painting-antifouling/">Paint, varnish & antifouling</a></li>
<li><a href="/en/services/interior-refit/">Cabin and saloon renewal</a></li>
<li><a href="/en/services/winterising-storage/">Winterising & maintenance</a></li>
</ul>
<p>In wood care we combine <a href="/en/blog/oakum-caulking-techniques/">traditional caulking</a> with modern epoxy, preserving the original character. For general info, see our <a href="/en/boats/gulet/">gulet</a> and <a href="/en/regions/bodrum/">Bodrum</a> pages.</p>
<p>For a pre-season <a href="#teklif-al">free survey</a>, message us.</p>
""",
 },
},
{
 "slug": "bodrum-yelkenli", "slug_en": "bodrum-sailboat", "image": "/assets/images/parallax-2.jpg",
 "tr": {
   "name": "Yelkenli Bakımı", "region_name": "Bodrum", "region_url": "/bolgeler/bodrum/",
   "hero_title": "Bodrum'da Yelkenli Tekne Tamiri ve Bakımı",
   "hero_sub": "Bodrum ve Yalıkavak çevresindeki yelkenliler için osmoz, boya, teak ve kışlatma.",
   "meta_title": "Bodrum Yelkenli Tamiri ve Bakımı | Tekne Usta",
   "meta_desc": "Bodrum'da yelkenli tekne tamiri, osmoz tedavisi, antifouling boya, teak ve kışlatma. Yalıkavak ve Bodrum marinaları çevresinde yelkenli servisi.",
   "body": """
<p>Bodrum ve Yalıkavak çevresi, yelkenli sahiplerinin yoğun olduğu bir bölge. Fiberglas ve klasik ahşap yelkenlilerde osmoz, boya, teak ve iç mekan işlerini yapıyoruz.</p>
<h2>Bodrum'da yelkenlinize hizmetler</h2>
<ul>
<li><a href="/hizmetler/fiberglas-onarim/">Fiberglas onarım ve osmoz tedavisi</a></li>
<li><a href="/hizmetler/tekne-boyama-antifouling/">Boya ve antifouling</a></li>
<li><a href="/hizmetler/teak-guverte-doseme/">Teak güverte döşeme</a></li>
<li><a href="/hizmetler/ic-mekan-yenileme/">İç mekan yenileme</a></li>
<li><a href="/hizmetler/tekne-kislatma/">Kışlatma ve bakım</a></li>
</ul>
<p>Direk, arma ve motor işleri kapsamımız dışında; gövde, karina, boya ve iç mekan tarafında tam hizmet veriyoruz. Genel bilgi için <a href="/tekneler/yelkenli/">yelkenli</a> ve <a href="/bolgeler/bodrum/">Bodrum</a> sayfalarımıza bakın.</p>
<p><a href="#teklif-al">Ücretsiz keşif</a> alın.</p>
""",
 },
 "en": {
   "name": "Sailboat Care", "region_name": "Bodrum", "region_url": "/en/regions/bodrum/",
   "hero_title": "Sailboat Repair and Maintenance in Bodrum",
   "hero_sub": "Osmosis, paint, teak and winterising for sailboats around Bodrum and Yalıkavak.",
   "meta_title": "Bodrum Sailboat Repair and Maintenance | Tekne Usta",
   "meta_desc": "Sailboat repair, osmosis treatment, antifouling, teak and winterising in Bodrum. Sailboat service around Yalıkavak and Bodrum marinas.",
   "body": """
<p>Bodrum and Yalıkavak are areas with many sailboat owners. We do osmosis, paint, teak and interior work on fibreglass and classic wooden sailboats.</p>
<h2>Services for your sailboat in Bodrum</h2>
<ul>
<li><a href="/en/services/fibreglass-repair/">Fibreglass repair & osmosis treatment</a></li>
<li><a href="/en/services/boat-painting-antifouling/">Painting & antifouling</a></li>
<li><a href="/en/services/teak-deck/">Teak decking</a></li>
<li><a href="/en/services/interior-refit/">Interior refit</a></li>
<li><a href="/en/services/winterising-storage/">Winterising & maintenance</a></li>
</ul>
<p>Mast, rigging and engine work are outside our scope; we provide full service on hull, underbody, paint and interior. For general info, see our <a href="/en/boats/sailboat/">sailboat</a> and <a href="/en/regions/bodrum/">Bodrum</a> pages.</p>
<p>Get a <a href="#teklif-al">free survey</a>.</p>
""",
 },
},
{
 "slug": "marmaris-yelkenli", "slug_en": "marmaris-sailboat", "image": "/assets/images/parallax-1.jpg",
 "tr": {
   "name": "Yelkenli Bakımı", "region_name": "Marmaris", "region_url": "/bolgeler/marmaris/",
   "hero_title": "Marmaris'te Yelkenli Tekne Tamiri ve Bakımı",
   "hero_sub": "Netsel Marmaris Marina ve Yat Marin çevresindeki yelkenliler için osmoz, boya, teak ve kışlatma.",
   "meta_title": "Marmaris Yelkenli Tamiri ve Bakımı | Tekne Usta",
   "meta_desc": "Marmaris'te yelkenli tekne tamiri, osmoz tedavisi, antifouling boya, teak ve kışlatma. Netsel Marmaris Marina ve Yat Marin çevresinde yelkenli servisi.",
   "body": """
<p>Marmaris, hem yerli hem yabancı yelkenli sahipleri için önemli bir üs; <strong>Netsel Marmaris Marina ve Yat Marin</strong> çevresinde çok sayıda yelkenli kışlar ve bakım görür. Bu tekneler için tam hizmet veriyoruz.</p>
<h2>Marmaris'te yelkenlinize hizmetler</h2>
<ul>
<li><a href="/hizmetler/fiberglas-onarim/">Fiberglas onarım ve osmoz tedavisi</a></li>
<li><a href="/hizmetler/tekne-boyama-antifouling/">Boya ve antifouling</a></li>
<li><a href="/hizmetler/teak-guverte-doseme/">Teak güverte döşeme</a></li>
<li><a href="/hizmetler/ic-mekan-yenileme/">İç mekan yenileme</a></li>
<li><a href="/hizmetler/tekne-kislatma/">Kışlatma ve bakım</a></li>
</ul>
<p>Uzun süre suda kalan yelkenlilerde karina ve <a href="/blog/osmoz-belirtileri/">osmoz</a> takibi önemli. Direk/arma ve motor işleri kapsam dışı. Genel bilgi için <a href="/tekneler/yelkenli/">yelkenli</a> ve <a href="/bolgeler/marmaris/">Marmaris</a> sayfalarımıza bakın.</p>
<p><a href="#teklif-al">Ücretsiz keşif</a> alın.</p>
""",
 },
 "en": {
   "name": "Sailboat Care", "region_name": "Marmaris", "region_url": "/en/regions/marmaris/",
   "hero_title": "Sailboat Repair and Maintenance in Marmaris",
   "hero_sub": "Osmosis, paint, teak and winterising for sailboats around Netsel Marmaris Marina and Yat Marin.",
   "meta_title": "Marmaris Sailboat Repair and Maintenance | Tekne Usta",
   "meta_desc": "Sailboat repair, osmosis treatment, antifouling, teak and winterising in Marmaris. Sailboat service around Netsel Marmaris Marina and Yat Marin.",
   "body": """
<p>Marmaris is an important base for both local and foreign sailboat owners; many sailboats winter and are maintained around <strong>Netsel Marmaris Marina and Yat Marin</strong>. We provide full service for these boats.</p>
<h2>Services for your sailboat in Marmaris</h2>
<ul>
<li><a href="/en/services/fibreglass-repair/">Fibreglass repair & osmosis treatment</a></li>
<li><a href="/en/services/boat-painting-antifouling/">Painting & antifouling</a></li>
<li><a href="/en/services/teak-deck/">Teak decking</a></li>
<li><a href="/en/services/interior-refit/">Interior refit</a></li>
<li><a href="/en/services/winterising-storage/">Winterising & maintenance</a></li>
</ul>
<p>On sailboats kept long afloat, hull and <a href="/en/blog/osmosis-symptoms/">osmosis</a> monitoring matter. Mast/rigging and engine work are out of scope. For general info, see our <a href="/en/boats/sailboat/">sailboat</a> and <a href="/en/regions/marmaris/">Marmaris</a> pages.</p>
<p>Get a <a href="#teklif-al">free survey</a>.</p>
""",
 },
},
{
 "slug": "fethiye-gulet", "slug_en": "fethiye-gulet", "image": "/assets/images/parallax-3.jpg",
 "tr": {
   "name": "Gulet Bakım & Refit", "region_name": "Fethiye", "region_url": "/bolgeler/fethiye/",
   "hero_title": "Fethiye'de Gulet Bakım, Refit ve Restorasyon",
   "hero_sub": "Ece Saray Marina ve Fethiye körfezindeki guletler için ahşap restorasyon, kalafat, teak ve boya.",
   "meta_title": "Fethiye Gulet Bakım, Refit ve Restorasyon | Tekne Usta",
   "meta_desc": "Fethiye'de gulet bakımı, refit, ahşap restorasyon, kalafat, teak ve boya. Ece Marina ve Fethiye körfezi çevresinde gulet servisi.",
   "body": """
<p>Fethiye ve komşu Göcek, mavi yolculuk guletlerinin yoğun olduğu bir bölge. <strong>Ece Saray Marina</strong> ve körfez çevresindeki guletler için kapsamlı bakım, refit ve restorasyon yapıyoruz.</p>
<h2>Fethiye'de guletinize hizmetler</h2>
<ul>
<li><a href="/hizmetler/ahsap-tekne-renovasyonu/">Ahşap restorasyon ve kalafat</a></li>
<li><a href="/hizmetler/teak-guverte-doseme/">Teak güverte döşeme</a></li>
<li><a href="/hizmetler/tekne-boyama-antifouling/">Boya, vernik ve antifouling</a></li>
<li><a href="/hizmetler/ic-mekan-yenileme/">Kabin ve salon yenileme</a></li>
<li><a href="/hizmetler/tekne-kislatma/">Kışlatma ve bakım</a></li>
</ul>
<p>Ticari guletlerde sezon öncesi bakım kritik; çok kalemli işleri <a href="/blog/refit-proje-yonetimi/">tek elden</a> yürütüyoruz. Genel bilgi için <a href="/tekneler/gulet/">gulet</a> ve <a href="/bolgeler/fethiye/">Fethiye</a> sayfalarımıza bakın.</p>
<p>Sezon öncesi <a href="#teklif-al">ücretsiz keşif</a> için bize yazın.</p>
""",
 },
 "en": {
   "name": "Gulet Maintenance & Refit", "region_name": "Fethiye", "region_url": "/en/regions/fethiye/",
   "hero_title": "Gulet Maintenance, Refit and Restoration in Fethiye",
   "hero_sub": "Wooden restoration, caulking, teak and paint for gulets around Ece Saray Marina and Fethiye bay.",
   "meta_title": "Fethiye Gulet Maintenance, Refit and Restoration | Tekne Usta",
   "meta_desc": "Gulet maintenance, refit, wooden restoration, caulking, teak and paint in Fethiye. Gulet service around Ece Marina and Fethiye bay.",
   "body": """
<p>Fethiye and neighbouring Göcek form an area with many blue-cruise gulets. We do comprehensive care, refit and restoration for gulets around <strong>Ece Saray Marina</strong> and the bay.</p>
<h2>Services for your gulet in Fethiye</h2>
<ul>
<li><a href="/en/services/wooden-boat-refit/">Wooden restoration & caulking</a></li>
<li><a href="/en/services/teak-deck/">Teak decking</a></li>
<li><a href="/en/services/boat-painting-antifouling/">Paint, varnish & antifouling</a></li>
<li><a href="/en/services/interior-refit/">Cabin and saloon renewal</a></li>
<li><a href="/en/services/winterising-storage/">Winterising & maintenance</a></li>
</ul>
<p>On commercial gulets, pre-season care is critical; we run multi-item work <a href="/en/blog/refit-project-management/">from one hand</a>. For general info, see our <a href="/en/boats/gulet/">gulet</a> and <a href="/en/regions/fethiye/">Fethiye</a> pages.</p>
<p>For a pre-season <a href="#teklif-al">free survey</a>, message us.</p>
""",
 },
},
{
 "slug": "istanbul-yat-motoryat", "slug_en": "istanbul-yacht-motoryacht", "image": "/assets/images/parallax-1.jpg",
 "tr": {
   "name": "Yat & Motoryat Bakımı", "region_name": "İstanbul", "region_url": "/bolgeler/istanbul/",
   "hero_title": "İstanbul'da Yat ve Motoryat Bakım-Onarım",
   "hero_sub": "Tuzla, Pendik, Ataköy ve Kalamış marinalarındaki yat ve motoryatlar için fiberglas, boya, teak ve kışlatma.",
   "meta_title": "İstanbul Yat & Motoryat Bakım-Onarım | Tekne Usta",
   "meta_desc": "İstanbul'da yat ve motoryat bakımı, fiberglas onarımı, boya-antifouling, teak döşeme ve kışlatma. Tuzla, Pendik, Ataköy ve Kalamış marinalarında servis.",
   "body": """
<p>İstanbul, iki yakasındaki marinalarıyla yoğun bir yat trafiğine sahip. <strong>Tuzla, Pendik, Viaport, Ataköy ve Kalamış</strong> çevresindeki yat ve motoryatlar için tek elden bakım ve onarım sunuyoruz; çekek gerektiren işlerde de esneğiz.</p>
<h2>İstanbul'da yatınıza hizmetler</h2>
<ul>
<li><a href="/hizmetler/fiberglas-onarim/">Fiberglas onarım ve osmoz tedavisi</a></li>
<li><a href="/hizmetler/tekne-boyama-antifouling/">Boya ve antifouling</a></li>
<li><a href="/hizmetler/teak-guverte-doseme/">Teak güverte döşeme</a></li>
<li><a href="/hizmetler/tekne-detailing/">Detailing</a> ve <a href="/hizmetler/ic-mekan-yenileme/">iç mekan yenileme</a></li>
<li><a href="/hizmetler/tekne-kislatma/">Kışlatma ve bakım</a></li>
</ul>
<p>Tuzla'nın çekek imkânları kapsamlı işler için avantaj. Genel bilgi için <a href="/tekneler/yat-motoryat/">yat & motoryat</a>, İstanbul için <a href="/bolgeler/istanbul/">İstanbul</a> ve <a href="/bolgeler/tuzla/">Tuzla</a> sayfalarımıza bakın.</p>
<p><a href="#teklif-al">Ücretsiz keşif</a> alın.</p>
""",
 },
 "en": {
   "name": "Yacht & Motoryacht Care", "region_name": "Istanbul", "region_url": "/en/regions/istanbul/",
   "hero_title": "Yacht and Motoryacht Care in Istanbul",
   "hero_sub": "Fibreglass, paint, teak and winterising for yachts and motoryachts at Tuzla, Pendik, Ataköy and Kalamış marinas.",
   "meta_title": "Istanbul Yacht & Motoryacht Care | Tekne Usta",
   "meta_desc": "Yacht and motoryacht care, fibreglass repair, painting-antifouling, teak decking and winterising in Istanbul. Service at Tuzla, Pendik, Ataköy and Kalamış marinas.",
   "body": """
<p>Istanbul has heavy yacht traffic with marinas on both sides. We offer single-hand care and repair for yachts and motoryachts around <strong>Tuzla, Pendik, Viaport, Ataköy and Kalamış</strong>, and we're flexible for jobs needing haul-out.</p>
<h2>Services for your yacht in Istanbul</h2>
<ul>
<li><a href="/en/services/fibreglass-repair/">Fibreglass repair & osmosis treatment</a></li>
<li><a href="/en/services/boat-painting-antifouling/">Painting & antifouling</a></li>
<li><a href="/en/services/teak-deck/">Teak decking</a></li>
<li><a href="/en/services/boat-detailing/">Detailing</a> and <a href="/en/services/interior-refit/">interior refit</a></li>
<li><a href="/en/services/winterising-storage/">Winterising & maintenance</a></li>
</ul>
<p>Tuzla's hardstanding is an advantage for extensive work. For general info see <a href="/en/boats/yacht-motoryacht/">yacht & motoryacht</a>, and for Istanbul our <a href="/en/regions/istanbul/">Istanbul</a> and <a href="/en/regions/tuzla/">Tuzla</a> pages.</p>
<p>Get a <a href="#teklif-al">free survey</a>.</p>
""",
 },
},
]
