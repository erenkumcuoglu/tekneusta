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
}

# ------------------------------------------------------------------ UI strings
I18N = {
    "tr": {
        "nav": {"home": "Ana Sayfa", "services": "Hizmetler", "regions": "Bölgeler",
                "about": "Hakkımızda", "blog": "Blog", "cta": "Teklif Al"},
        "footer": {
            "tag": "Tekne tamiri, renovasyon ve bakımında güvenilir usta eli. Her tekneye, her hasara özel çözüm.",
            "contact": "İletişim", "wa": "WhatsApp'tan Yaz", "rights": "Tüm hakları saklıdır.",
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
            "privacy": "Bilgileriniz yalnızca sizinle iletişim amacıyla kullanılır.",
            "success_title": "Talebiniz Alındı", "success_text": "24 saat içinde ustamız sizi arayacak. Teşekkür ederiz.",
            "lead": "Merhaba, tekneusta.com üzerinden teklif talebi:",
        },
    },
    "en": {
        "nav": {"home": "Home", "services": "Services", "regions": "Regions",
                "about": "About", "blog": "Blog", "cta": "Get a Quote"},
        "footer": {
            "tag": "The trusted craftsman for boat repair, refit and maintenance. A tailored solution for every boat and every job.",
            "contact": "Contact", "wa": "Message on WhatsApp", "rights": "All rights reserved.",
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
            {"num": "4.9", "label": "Ortalama Puan"}, {"num": "%100", "label": "İşçilik Garantisi"},
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
        "test_label": "Müşteri Görüşleri", "test_title": "Tekne Sahipleri Ne Diyor?",
    },
    "en": {
        "badge": "Boat Repair · Refit · Maintenance",
        "h1": "Your Boat, in <em>Master Hands</em>",
        "sub": "From fibreglass repair to wooden refit, professional painting to winterising — we make your boat seaworthy again.",
        "cta1": "Get a Free Quote", "cta2": "Explore Services", "scroll": "Scroll", "detail": "Details →",
        "stats": [
            {"num": "15+", "label": "Years Experience"}, {"num": "300+", "label": "Projects Completed"},
            {"num": "4.9", "label": "Average Rating"}, {"num": "100%", "label": "Workmanship Warranty"},
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
]
