#!/usr/bin/env python3
"""IndexNow ping — Bing (ChatGPT araması Bing indeksini kullanır), Yandex, Seznam vb.
Deploy'dan SONRA çalıştır (key dosyası canlıda olmalı).

  python3 _src/indexnow.py            # son commit'te değişen HTML sayfaları
  python3 _src/indexnow.py --since X  # X commit'inden bu yana değişenler
  python3 _src/indexnow.py --all      # sitemap'teki tüm URL'ler (ilk kurulum)
"""
import os, re, sys, json, subprocess, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEXNOW_KEY = "08e8b09e20c77e4eb149a94686492354"  # public; build.py'deki ile aynı, kök dizinde <key>.txt
DOMAIN = "https://www.tekneusta.com"

HOST = re.sub(r"^https?://", "", DOMAIN).rstrip("/")

def sitemap_urls():
    xml = open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read()
    return re.findall(r"<loc>(.*?)</loc>", xml)

def changed_urls(since):
    out = subprocess.run(["git", "-C", ROOT, "diff", "--name-only", since, "HEAD"],
                         capture_output=True, text=True, check=True).stdout.split()
    urls = []
    for f in out:
        if not f.endswith("index.html") or f.startswith(("_src/", ".gsc/")):
            continue
        path = "/" + f[:-len("index.html")]
        urls.append(DOMAIN.rstrip("/") + path)
    live = set(sitemap_urls())
    return [u for u in urls if u in live]

def ping(urls):
    if not urls:
        print("Gönderilecek URL yok."); return
    for i in range(0, len(urls), 10000):
        body = json.dumps({"host": HOST, "key": INDEXNOW_KEY,
                           "keyLocation": f"{DOMAIN.rstrip('/')}/{INDEXNOW_KEY}.txt",
                           "urlList": urls[i:i + 10000]}).encode()
        req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body,
                                     headers={"Content-Type": "application/json; charset=utf-8"})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                print(f"IndexNow: {len(urls[i:i+10000])} URL → HTTP {r.status}")
        except urllib.error.HTTPError as e:
            print(f"IndexNow hata: HTTP {e.code} {e.read()[:200]!r}")

if __name__ == "__main__":
    a = sys.argv[1:]
    if "--all" in a:
        ping(sitemap_urls())
    else:
        since = a[a.index("--since") + 1] if "--since" in a else "HEAD~1"
        ping(changed_urls(since))
