# -*- coding: utf-8 -*-
"""Static site generator for Tekne Usta. Run:  python3 _src/build.py"""
import os, json, datetime, shutil
import xml.sax.saxutils as SU
from jinja2 import Environment, FileSystemLoader, select_autoescape
import content as C

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)            # site root (published dir)
TPL = os.path.join(HERE, "templates")
SITE = C.SITE
DOMAIN = SITE["domain"]
YEAR = datetime.date.today().year

env = Environment(loader=FileSystemLoader(TPL), autoescape=select_autoescape(["html"]))

urls = []  # (loc, priority) for sitemap

def j(obj):
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":"))

def relativize(html, rel_path):
    """Rewrite root-absolute internal URLs (="/... and url(/...) to page-relative
    paths so the site works both on file:// preview and on the server. Absolute
    https:// URLs (canonical, og, schema, sitemap) are untouched."""
    depth = rel_path.count("/")
    prefix = "../" * depth  # "" for root-level pages
    # Relativise href/src attributes (work locally + deployed).
    html = html.replace('="/', '="' + prefix)
    # NOTE: CSS url() background images (in inline custom properties consumed by the
    # external stylesheet) are intentionally left ABSOLUTE ("/assets/..."). Relative
    # url() inside a custom property is resolved by browsers against the stylesheet's
    # location (/assets/css/), which breaks the path. Absolute paths always resolve
    # correctly on the deployed site regardless of where they're used.
    return html

def write(rel_path, html):
    out = os.path.join(ROOT, rel_path)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    if rel_path.endswith(".html"):
        html = relativize(html, rel_path)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)

def abs_url(path):
    return DOMAIN.rstrip("/") + path

# ---- generated blog cover thumbnails (branded SVG; swap for real photos later) --
def _wrap_title(title, maxc=24, maxlines=4):
    words, lines, cur = title.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 <= maxc:
            cur = (cur + " " + w).strip()
        else:
            if cur:
                lines.append(cur)
            cur = w
        if len(lines) >= maxlines:
            break
    if cur and len(lines) < maxlines:
        lines.append(cur)
    if len(lines) == maxlines:
        lines[-1] = (lines[-1][:maxc - 1] + "…") if len(lines[-1]) > maxc else lines[-1]
    return lines[:maxlines]

def gen_thumb(title, category):
    lines = _wrap_title(title)
    start_y = 232 - (len(lines) - 1) * 22
    tspans = "".join(
        '<tspan x="46" dy="{}">{}</tspan>'.format("0" if i == 0 else "1.18em", SU.escape(l))
        for i, l in enumerate(lines))
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 400" role="img">'
        '<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#0A3D5C"/><stop offset="1" stop-color="#062A42"/></linearGradient></defs>'
        '<rect width="640" height="400" fill="url(#g)"/>'
        '<g fill="none" stroke="#DEB86B" stroke-width="2" opacity="0.13">'
        '<circle cx="540" cy="150" r="120"/><path d="M540 20v260M410 150h260"/>'
        '<path d="M500 300a40 40 0 0 0 80 0" /></g>'
        '<text x="46" y="66" fill="#DEB86B" font-family="Arial, sans-serif" font-size="17" '
        'letter-spacing="3">{cat}</text>'
        '<rect x="46" y="82" width="52" height="3" fill="#C4933A"/>'
        '<text x="46" y="{y}" fill="#FFFFFF" font-family="Georgia, \'Times New Roman\', serif" '
        'font-size="33" font-weight="500">{ts}</text>'
        '<text x="46" y="366" fill="#8AAFC8" font-family="Arial, sans-serif" font-size="13" '
        'letter-spacing="4">TEKNE USTA</text>'
        '</svg>'
    ).format(cat=SU.escape(category.upper()), y=start_y, ts=tspans)

# ---- localized list builders -------------------------------------------------
def services_for(lang):
    out = []
    for s in C.SERVICES:
        d = s[lang]
        url = f"/hizmetler/{s['slug']}/" if lang == "tr" else f"/en/services/{s['slug_en']}/"
        out.append({**d, "slug": s["slug"], "slug_en": s["slug_en"], "image": s["image"], "url": url,
                    "deep": s.get("deep", {}).get(lang, "")})
    return out

def regions_for(lang):
    out = []
    for r in C.REGIONS:
        d = r[lang]
        url = f"/bolgeler/{r['slug']}/" if lang == "tr" else f"/en/regions/{r['slug']}/"
        out.append({**d, "slug": r["slug"], "image": r["image"], "url": url})
    return out

def boattypes_for(lang):
    out = []
    for b in C.BOATTYPES:
        d = b[lang]
        url = f"/tekneler/{b['slug']}/" if lang == "tr" else f"/en/boats/{b['slug_en']}/"
        out.append({**d, "slug": b["slug"], "slug_en": b["slug_en"], "image": b["image"], "url": url})
    return out

def posts_for(lang):
    out = []
    for p in C.POSTS:
        d = p[lang]
        url = f"/blog/{p['slug']}/" if lang == "tr" else f"/en/blog/{p['slug_en']}/"
        out.append({**d, "slug": p["slug"], "slug_en": p["slug_en"], "image": p["image"], "date": p["date"], "url": url})
    return out

def testimonials_for(lang):
    return [{"initials": t["initials"], "name": t["name"], "boat": t["boat"], "body": t[lang]} for t in C.TESTIMONIALS]

def glossary_for(lang):
    return [{"t": g[lang]["t"], "d": g[lang]["d"], "u": g[lang]["u"]} for g in C.GLOSSARY]

def glossary_schema(lang, gl):
    return {"@context": "https://schema.org", "@type": "DefinedTermSet",
            "name": "Tekne Bakım Sözlüğü" if lang == "tr" else "Boat Care Glossary",
            "inLanguage": lang,
            "hasDefinedTerm": [{"@type": "DefinedTerm", "name": t["t"], "description": t["d"], "url": abs_url(t["u"])} for t in gl]}

# ---- schema builders ---------------------------------------------------------
def local_business_schema():
    return {
        "@context": "https://schema.org", "@type": ["LocalBusiness", "HomeAndConstructionBusiness"],
        "@id": DOMAIN + "/#business", "name": SITE["brand"],
        "description": "İstanbul ve Ege'de profesyonel tekne tamiri, bakımı ve renovasyonu. Fiberglas onarımı, osmoz tedavisi, gelcoat, antifouling, ahşap tekne restorasyonu, teak güverte döşeme, iç mekan yenileme ve kışlatma.",
        "url": DOMAIN, "telephone": SITE["phone_e164"], "email": SITE["email"],
        "image": abs_url("/assets/images/hakkimizda.jpg"),
        "address": {"@type": "PostalAddress", "streetAddress": "Kültür Mah.", "addressLocality": "Beşiktaş", "addressRegion": "İstanbul", "postalCode": "34340", "addressCountry": "TR"},
        "geo": {"@type": "GeoCoordinates", "latitude": "41.0430", "longitude": "29.0075"},
        "areaServed": [{"@type": "City", "name": n} for n in ["İstanbul", "Bodrum", "Göcek", "Marmaris", "Fethiye"]],
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
            "opens": "08:00", "closes": "18:00"}],
        "priceRange": "$$",
        "foundingDate": SITE["founded"],
        # NOTE: aggregateRating gerçek/görünür yorumlar toplanınca eklenecek (Google politikası).
        "sameAs": [SITE["instagram"]],
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Tekne Hizmetleri",
            "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["tr"]["name"], "description": s["tr"]["short"]}} for s in C.SERVICES]},
    }

def website_schema(lang):
    return {"@context": "https://schema.org", "@type": "WebSite", "name": SITE["brand"],
            "url": DOMAIN + ("/" if lang == "tr" else "/en/"), "inLanguage": lang,
            "publisher": {"@id": DOMAIN + "/#business"}}

def faq_schema(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": f["q"],
                            "acceptedAnswer": {"@type": "Answer", "text": f["a"]}} for f in faqs]}

def breadcrumb_schema(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": nm, "item": abs_url(u)}
                                for i, (nm, u) in enumerate(items)]}

def service_schema(svc, lang):
    return {"@context": "https://schema.org", "@type": "Service",
            "name": svc["name"], "description": svc["hero_sub"],
            "serviceType": svc["name"], "provider": {"@id": DOMAIN + "/#business"},
            "areaServed": [{"@type": "City", "name": n} for n in ["İstanbul", "Bodrum", "Göcek", "Marmaris", "Fethiye"]],
            "url": abs_url(svc["url"]), "inLanguage": lang}

def article_schema(post, lang):
    return {"@context": "https://schema.org", "@type": "BlogPosting",
            "headline": post["title"], "description": post["excerpt"],
            "image": abs_url(post["image"]), "datePublished": post["date"], "dateModified": post["date"],
            "inLanguage": lang, "author": {"@type": "Organization", "name": SITE["brand"]},
            "publisher": {"@id": DOMAIN + "/#business"},
            "mainEntityOfPage": {"@type": "WebPage", "@id": abs_url(post["url"])}}

# ---- page context ------------------------------------------------------------
def base_ctx(lang, path_tr, path_en, meta_title, meta_desc, schemas, nav_solid=True,
             og_image=None, og_type="website", extra=None):
    path = path_tr if lang == "tr" else path_en
    ctx = {
        "site": SITE, "t": {**C.I18N[lang], "home": C.HOME[lang]}, "year": YEAR,
        "services": services_for(lang), "regions": regions_for(lang),
        "testimonials": testimonials_for(lang),
        "page": {
            "lang": lang, "meta_title": meta_title, "meta_desc": meta_desc,
            "canonical": abs_url(path), "href_tr": abs_url(path_tr), "href_en": abs_url(path_en),
            "home": "/" if lang == "tr" else "/en/",
            "blog_url": "/blog/" if lang == "tr" else "/en/blog/",
            "tool_url": "/arac/maliyet-tahmini/" if lang == "tr" else "/en/tools/cost-estimate/",
            "privacy_url": "/gizlilik/" if lang == "tr" else "/en/privacy/",
            "glossary_url": "/sozluk/" if lang == "tr" else "/en/glossary/",
            "nav_solid": nav_solid, "og_image": og_image, "og_type": og_type,
            "schemas": [j(s) for s in schemas],
        },
    }
    if extra:
        ctx.update(extra)
    return ctx

def render(template, ctx, out_path, priority="0.7"):
    html = env.get_template(template).render(**ctx)
    write(out_path, html)
    urls.append((abs_url(ctx["page"]["canonical"].replace(DOMAIN, "")), priority))

# ============================================================ BUILD
def build():
    for lang in ("tr", "en"):
        H = C.HOME[lang]
        svcs = services_for(lang)
        home_faqs = [f for s in svcs[:2] for f in s["faqs"]] + [
            {"q": ("Keşif ve fiyat teklifi ücretli mi?" if lang == "tr" else "Is the survey and quote free?"),
             "a": ("Hayır, tamamen ücretsizdir. Teknenizi yerinde inceleyerek 48 saat içinde kalem kalem yazılı teklif sunuyoruz." if lang == "tr"
                   else "No, it's completely free. We inspect your boat on site and send an itemised written quote within 48 hours.")},
            {"q": ("İşçilik garantisi veriyor musunuz?" if lang == "tr" else "Do you offer a workmanship warranty?"),
             "a": ("Evet, tüm onarım ve işçilik çalışmalarında garanti veriyoruz. Kapsam ve süre teklifte belirtilir." if lang == "tr"
                   else "Yes, we warranty all repair and workmanship. Scope and duration are stated in the quote.")},
        ]
        # ---- HOME
        mt = ("Tekne Tamiri, Bakımı ve Renovasyonu | İstanbul & Ege — Tekne Usta" if lang == "tr"
              else "Boat Repair, Maintenance & Refit | Istanbul & Aegean — Tekne Usta")
        md = ("İstanbul ve Ege'de tekne tamiri, fiberglas onarımı, osmoz tedavisi, antifouling boya, ahşap renovasyon, teak döşeme ve kışlatma. Ücretsiz keşif, 48 saat yazılı teklif, işçilik garantisi." if lang == "tr"
              else "Boat repair, fibreglass repair, osmosis treatment, antifouling, wooden refit, teak decking and winterising in Istanbul and the Aegean. Free survey, 48-hour written quote, workmanship warranty.")
        ctx = base_ctx(lang, "/", "/en/", mt, md,
                       [local_business_schema(), website_schema(lang), faq_schema(home_faqs)],
                       nav_solid=False)
        ctx["faqs"] = home_faqs
        ctx["boattypes"] = boattypes_for(lang)
        render("home.html", ctx, ("index.html" if lang == "tr" else "en/index.html"), priority="1.0")

        # ---- SERVICES
        for s in C.SERVICES:
            d = s[lang]
            url_tr, url_en = f"/hizmetler/{s['slug']}/", f"/en/services/{s['slug_en']}/"
            svc = {**d, "slug": s["slug"], "slug_en": s["slug_en"], "image": s["image"],
                   "url": url_tr if lang == "tr" else url_en,
                   "deep": s.get("deep", {}).get(lang, "")}
            crumb = [(C.I18N[lang]["nav"]["home"], "/" if lang == "tr" else "/en/"),
                     (C.I18N[lang]["nav"]["services"], ("/#hizmetler" if lang == "tr" else "/en/#hizmetler")),
                     (d["name"], svc["url"])]
            schemas = [service_schema(svc, lang), faq_schema(d["faqs"]), breadcrumb_schema(crumb)]
            ctx = base_ctx(lang, url_tr, url_en, d["meta_title"], d["meta_desc"], schemas,
                           og_image=s["image"], extra={"svc": svc, "faqs": d["faqs"]})
            out = (f"hizmetler/{s['slug']}/index.html" if lang == "tr" else f"en/services/{s['slug_en']}/index.html")
            render("service.html", ctx, out, priority="0.9")

        # ---- REGIONS
        for r in C.REGIONS:
            d = r[lang]
            url_tr, url_en = f"/bolgeler/{r['slug']}/", f"/en/regions/{r['slug']}/"
            region = {**d, "slug": r["slug"], "image": r["image"], "url": url_tr if lang == "tr" else url_en}
            reg_faqs = home_faqs[-2:]
            crumb = [(C.I18N[lang]["nav"]["home"], "/" if lang == "tr" else "/en/"),
                     (C.I18N[lang]["nav"]["regions"], ("/#bolgeler" if lang == "tr" else "/en/#bolgeler")),
                     (d["name"], region["url"])]
            schemas = [breadcrumb_schema(crumb), faq_schema(reg_faqs)]
            ctx = base_ctx(lang, url_tr, url_en, d["meta_title"], d["meta_desc"], schemas,
                           og_image=r["image"], extra={"region": region, "faqs": reg_faqs})
            out = (f"bolgeler/{r['slug']}/index.html" if lang == "tr" else f"en/regions/{r['slug']}/index.html")
            render("region.html", ctx, out, priority="0.8")

        # ---- BOAT TYPES (tekne tipi pillar sayfaları)
        for b in C.BOATTYPES:
            d = b[lang]
            url_tr, url_en = f"/tekneler/{b['slug']}/", f"/en/boats/{b['slug_en']}/"
            bt = {**d, "slug": b["slug"], "image": b["image"], "url": url_tr if lang == "tr" else url_en}
            crumb = [(C.I18N[lang]["nav"]["home"], "/" if lang == "tr" else "/en/"),
                     (C.I18N[lang]["boattype"]["label"], ("/#tipler" if lang == "tr" else "/en/#tipler")),
                     (d["name"], bt["url"])]
            schemas = [breadcrumb_schema(crumb), faq_schema(home_faqs[-2:])]
            ctx = base_ctx(lang, url_tr, url_en, d["meta_title"], d["meta_desc"], schemas,
                           og_image=b["image"], extra={"bt": bt, "boattypes": boattypes_for(lang), "faqs": home_faqs[-2:]})
            out = (f"tekneler/{b['slug']}/index.html" if lang == "tr" else f"en/boats/{b['slug_en']}/index.html")
            render("boattype.html", ctx, out, priority="0.8")

        # ---- TYPE x LOCATION (curated local landing pages)
        for tl0 in C.TYPE_LOCATION:
            d = tl0[lang]
            url_tr, url_en = f"/tekneler/{tl0['slug']}/", f"/en/boats/{tl0['slug_en']}/"
            tl = {**d, "image": tl0["image"], "url": url_tr if lang == "tr" else url_en}
            crumb = [(C.I18N[lang]["nav"]["home"], "/" if lang == "tr" else "/en/"),
                     (d["region_name"], d["region_url"]),
                     (d["name"], tl["url"])]
            schemas = [breadcrumb_schema(crumb), faq_schema(home_faqs[-2:])]
            ctx = base_ctx(lang, url_tr, url_en, d["meta_title"], d["meta_desc"], schemas,
                           og_image=tl0["image"], extra={"tl": tl, "faqs": home_faqs[-2:]})
            out = (f"tekneler/{tl0['slug']}/index.html" if lang == "tr" else f"en/boats/{tl0['slug_en']}/index.html")
            render("typeloc.html", ctx, out, priority="0.7")

        # ---- BLOG INDEX
        posts = posts_for(lang)
        for post in posts:
            tslug = post["slug"] if lang == "tr" else post["slug_en"]
            thumb_rel = f"assets/images/blog/{'en-' if lang == 'en' else ''}{tslug}.svg"
            write(thumb_rel, gen_thumb(post["title"], post["category"]))
            post["thumb"] = "/" + thumb_rel
        bmt = ("Tekne Bakım Rehberi & Blog | Tekne Usta" if lang == "tr" else "Boat Care Guide & Blog | Tekne Usta")
        bmd = ("Osmoz, antifouling, teak bakımı ve tekne kışlatma üzerine tekne sahipleri için pratik, uzman rehberler." if lang == "tr"
               else "Practical, expert guides for boat owners on osmosis, antifouling, teak care and winterising.")
        ctx = base_ctx(lang, "/blog/", "/en/blog/", bmt, bmd, [website_schema(lang)], extra={"posts": posts})
        render("blog_index.html", ctx, ("blog/index.html" if lang == "tr" else "en/blog/index.html"), priority="0.6")

        # ---- ARTICLES
        for p in C.POSTS:
            d = p[lang]
            url_tr, url_en = f"/blog/{p['slug']}/", f"/en/blog/{p['slug_en']}/"
            post = {**d, "image": p["image"], "date": p["date"], "url": url_tr if lang == "tr" else url_en}
            crumb = [(C.I18N[lang]["nav"]["home"], "/" if lang == "tr" else "/en/"),
                     (C.I18N[lang]["nav"]["blog"], "/blog/" if lang == "tr" else "/en/blog/"),
                     (d["title"], post["url"])]
            schemas = [article_schema(post, lang), breadcrumb_schema(crumb)]
            ctx = base_ctx(lang, url_tr, url_en, d["meta_title"], d["meta_desc"], schemas,
                           og_image=p["image"], og_type="article", extra={"post": post})
            out = (f"blog/{p['slug']}/index.html" if lang == "tr" else f"en/blog/{p['slug_en']}/index.html")
            render("article.html", ctx, out, priority="0.6")

        # ---- COST ESTIMATOR TOOL
        ti = C.TOOL_I18N[lang]
        ctx = base_ctx(lang, "/arac/maliyet-tahmini/", "/en/tools/cost-estimate/",
                       ti["meta_title"], ti["meta_desc"], [website_schema(lang)],
                       extra={"tool": ti, "pricing": C.PRICING, "pricing_json": j(C.PRICING)})
        render("tool.html", ctx,
               ("arac/maliyet-tahmini/index.html" if lang == "tr" else "en/tools/cost-estimate/index.html"),
               priority="0.8")

        # ---- LEGAL PAGES
        for lg in C.LEGAL:
            d = lg[lang]
            ctx = base_ctx(lang, f"/{lg['slug']}/", f"/en/{lg['slug_en']}/", d["meta_title"], d["meta_desc"], [])
            ctx.update({"ptitle": d["title"], "psub": d["sub"], "pbody": d["body"]})
            render("plain.html", ctx,
                   (f"{lg['slug']}/index.html" if lang == "tr" else f"en/{lg['slug_en']}/index.html"),
                   priority="0.3")

        # ---- GLOSSARY (Sözlük Hub)
        gl = glossary_for(lang)
        gtitle = "Tekne Bakım Sözlüğü" if lang == "tr" else "Boat Care Glossary"
        gintro = ("Tekne tamiri, bakımı ve renovasyonunda sık geçen terimlerin sade açıklamaları; her terim ilgili rehber veya hizmete bağlanır."
                  if lang == "tr" else
                  "Plain explanations of common boat repair, maintenance and refit terms; each links to the relevant guide or service.")
        gmt = gtitle + " | " + SITE["brand"]
        gmd = ("Osmoz, gelcoat, antifouling, kalafat, teak, kekamoz, anot ve daha fazlası — tekne bakım terimleri sözlüğü."
               if lang == "tr" else
               "Osmosis, gelcoat, antifouling, caulking, teak, anode and more — a boat care terms glossary.")
        ctx = base_ctx(lang, "/sozluk/", "/en/glossary/", gmt, gmd, [glossary_schema(lang, gl)],
                       extra={"glossary": gl, "gtitle": gtitle, "gintro": gintro})
        render("glossary.html", ctx,
               ("sozluk/index.html" if lang == "tr" else "en/glossary/index.html"), priority="0.6")

    # ---- 404 (Turkish default)
    ctx = base_ctx("tr", "/404.html", "/404.html", "Sayfa Bulunamadı | Tekne Usta",
                   "Aradığınız sayfa bulunamadı.", [])
    ctx.update({"ptitle": "Sayfa Bulunamadı", "psub": "Aradığınız sayfa taşınmış veya kaldırılmış olabilir.",
                "pbody": '<p>Aradığınız sayfayı bulamadık. <a href="/">Ana sayfaya dönün</a> veya <a href="/#hizmetler">hizmetlerimize</a> göz atın.</p>'})
    write("404.html", env.get_template("plain.html").render(**ctx))

    write_sitemap()
    write_robots()
    write_llms()
    print(f"Built {len(urls)} pages.")

def write_sitemap():
    seen, items = set(), []
    for loc, pr in urls:
        if loc in seen: continue
        seen.add(loc)
        items.append(f"  <url><loc>{loc}</loc><changefreq>monthly</changefreq><priority>{pr}</priority></url>")
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(items) + "\n</urlset>\n"
    write("sitemap.xml", xml)

def write_robots():
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")

def write_llms():
    """Machine-friendly summary for LLMs / AI assistants (emerging GEO convention)."""
    S, R, P = services_for("tr"), regions_for("tr"), posts_for("tr")
    cornerstone = ["osmoz-nedir-tedavisi", "antifouling-secimi", "tekne-boyama-maliyeti",
                   "teak-guverte-bakimi", "tekne-kislatma-kontrol-listesi",
                   "ikinci-el-tekne-alim-rehberi", "fiber-mi-ahsap-tekne",
                   "satin-alma-oncesi-tekne-ekspertizi", "refit-proje-yonetimi"]
    bymap = {p["slug"]: p for p in P}
    L = [f"# {SITE['brand']}", "",
         "> İstanbul ve Ege'de profesyonel tekne tamiri, bakımı ve renovasyonu. Fiberglas onarımı ve "
         "osmoz tedavisi, antifouling boya, ahşap tekne restorasyonu, teak güverte döşeme, iç mekan "
         "yenileme, kışlatma ve detailing. Ücretsiz keşif, 48 saatte yazılı teklif, işçilik garantisi. "
         "Aracısız, doğrudan ustayla çalışılır.", "",
         f"İletişim: {SITE['phone_display']} · WhatsApp: https://wa.me/{SITE['wa']} · {SITE['email']}", "",
         "## Hizmetler"]
    L += [f"- [{s['name']}]({abs_url(s['url'])}): {s['short']}" for s in S]
    L += ["", "## Hizmet Bölgeleri"]
    L += [f"- [{r['name']}]({abs_url(r['url'])})" for r in R]
    L += ["", "## Rehber (öne çıkan içerikler)"]
    L += [f"- [{bymap[sl]['title']}]({abs_url(bymap[sl]['url'])}): {bymap[sl]['excerpt']}"
          for sl in cornerstone if sl in bymap]
    L += [f"- [Tüm blog ({len(P)} makale)]({abs_url('/blog/')})", ""]
    write("llms.txt", "\n".join(L) + "\n")

if __name__ == "__main__":
    build()
