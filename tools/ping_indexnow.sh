#!/bin/sh
# Submit every live URL to IndexNow (Bing, Yandex, Seznam, Naver). Run after a deploy.
KEY=ae1d07cfddbda2f2b7cdc7c134b6ba72
python3 - "$KEY" <<'PY'
import json,sys,urllib.request,os
key=sys.argv[1]; root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
urls=[u for u in open(os.path.join(root,"tools","indexnow_urls.txt")).read().split() if u]
body=json.dumps({"host":"www.setlsleep.com","key":key,"keyLocation":"https://www.setlsleep.com/%s.txt"%key,"urlList":urls}).encode()
r=urllib.request.urlopen(urllib.request.Request("https://api.indexnow.org/indexnow",body,{"Content-Type":"application/json; charset=utf-8"}))
print("IndexNow HTTP",r.status,"for",len(urls),"URLs")
PY
