# -*- coding: utf-8 -*-
"""Static site generator for Tekne Usta. Run:  python3 _src/build.py"""
import os, json, datetime, shutil
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
    html = html.replace('="/', '="' + prefix)
    html = html.replace("url('/", "url('" + prefix)
    html = html.replace('url("/', 'url("' + prefix)
    html = html.replace("url(/", "url(" + prefix)
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

# ---- localized list builders -------------------------------------------------
def services_for(lang):
    out = []
    for s in C.SERVICES:
        d = s[lang]
        url = f"/hizmetler/{s['slug']}/" if lang == "tr" else f"/en/services/{s['slug_en']}/"
        out.append({**d, "slug": s["slug"], "slug_en": s["slug_en"], "image": s["image"], "url": url})
    return out

def regions_for(lang):
    out = []
    for r in C.REGIONS:
        d = r[lang]
        url = f"/bolgeler/{r['slug']}/" if lang == "tr" else f"/en/regions/{r['slug']}/"
        out.append({**d, "slug": r["slug"], "image": r["image"], "url": url})
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

# ---- schema builders ---------------------------------------------------------
def local_business_schema():
    return {
        "@context": "https://schema.org", "@type": ["LocalBusiness", "HomeAndConstructionBusiness"],
        "@id": DOMAIN + "/#business", "name": SITE["brand"],
        "description": "İstanbul ve Ege'de profesyonel tekne tamiri, bakımı ve renovasyonu. Fiberglas onarımı, osmoz tedavisi, gelcoat, antifouling, ahşap tekne restorasyonu, teak güverte döşeme, iç mekan yenileme ve kışlatma.",
        "url": DOMAIN, "telephone": SITE["phone_e164"], "email": SITE["email"],
        "image": abs_url("/assets/images/hakkimizda.jpg"),
        "address": {"@type": "PostalAddress", "addressLocality": "İstanbul", "addressRegion": "İstanbul", "addressCountry": "TR"},
        "geo": {"@type": "GeoCoordinates", "latitude": "40.8330", "longitude": "29.3000"},
        "areaServed": [{"@type": "City", "name": n} for n in ["İstanbul", "Bodrum", "Göcek", "Marmaris", "Fethiye"]],
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
            "opens": "08:00", "closes": "18:00"}],
        "priceRange": "$$",
        "foundingDate": SITE["founded"],
        "aggregateRating": {"@type": "AggregateRating", "ratingValue": SITE["rating"], "reviewCount": SITE["review_count"]},
        "sameAs": [SITE["instagram"], SITE["youtube"]],
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
        render("home.html", ctx, ("index.html" if lang == "tr" else "en/index.html"), priority="1.0")

        # ---- SERVICES
        for s in C.SERVICES:
            d = s[lang]
            url_tr, url_en = f"/hizmetler/{s['slug']}/", f"/en/services/{s['slug_en']}/"
            svc = {**d, "slug": s["slug"], "slug_en": s["slug_en"], "image": s["image"],
                   "url": url_tr if lang == "tr" else url_en}
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

        # ---- BLOG INDEX
        posts = posts_for(lang)
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

    # ---- 404 (Turkish default)
    ctx = base_ctx("tr", "/404.html", "/404.html", "Sayfa Bulunamadı | Tekne Usta",
                   "Aradığınız sayfa bulunamadı.", [])
    ctx.update({"ptitle": "Sayfa Bulunamadı", "psub": "Aradığınız sayfa taşınmış veya kaldırılmış olabilir.",
                "pbody": '<p>Aradığınız sayfayı bulamadık. <a href="/">Ana sayfaya dönün</a> veya <a href="/#hizmetler">hizmetlerimize</a> göz atın.</p>'})
    write("404.html", env.get_template("plain.html").render(**ctx))

    write_sitemap()
    write_robots()
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

if __name__ == "__main__":
    build()
