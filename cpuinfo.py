#│-----------------------------------------------------------│
#│  Link: t.me/FrontendVSCode                 │ 
#│  Author: Frontend & LED (𝙰𝚕𝚒𝚊 𝙴𝚝𝚑𝚎𝚛 𖤍) 🌷 │ 
#│  lang: python                              │
#│  [VS-HASH-01] ΞΩ77Λβ99PPHD8A71             │ 
#│  build:3.10.15                             │ 
#│-----------------------------------------------------------│



import os

def detect_cpu():
    cores = []
    try:
        for cpu in os.listdir("/sys/devices/system/cpu/"):
            if cpu.startswith("cpu") and cpu[3:].isdigit():
                path = f"/sys/devices/system/cpu/{cpu}/cpufreq/cpuinfo_max_freq"
                if os.path.exists(path):
                    with open(path) as f:
                        cores.append(int(f.read()))
    except:
        pass

    if not cores:
        return "Не удалось определить"

    big = max(cores)
    little = min(cores)
    return f"big ≈ {big//1000}MHz | LITTLE ≈ {little//1000}MHz"