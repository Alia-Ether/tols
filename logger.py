#│-----------------------------------------------------------│
#│  Link: t.me/FrontendVSCode                 │ 
#│  Author: Frontend & LED (𝙰𝚕𝚒𝚊 𝙴𝚝𝚑𝚎𝚛 𖤍) 🌷 │ 
#│  lang: python                              │
#│  [VS-HASH-01] ΞΩ77Λβ99PPHD8A71             │ 
#│  build:3.10.15                             │ 
#│-----------------------------------------------------------│



from datetime import datetime

LOG = "activity.log"


def log(msg):
    with open(LOG, "a") as f:
        f.write(f"[{datetime.now()}] {msg}\n")