#│-----------------------------------------------------------│
#│  Link: t.me/FrontendVSCode                 │ 
#│  Author: Frontend & LED (𝙰𝚕𝚒𝚊 𝙴𝚝𝚑𝚎𝚛 𖤍) 🌷 │ 
#│  lang: python                              │
#│  [VS-HASH-01] ΞΩ77Λβ99PPHD8A71             │ 
#│  build:3.10.15                             │ 
#│-----------------------------------------------------------│





from docx import Document
from pathlib import Path

def main():
    template_path = Path("tols/files/template.docx")

    if not template_path.exists():
        print("❌ Шаблон не найден!")
        return

    doc = Document(template_path)

    data = {
        "{{number}}": "2024/015",
        "{{city}}": "Москва",
        "{{date}}": "28.03.2025",
        "{{client}}": "Иванов И.И.",
        "{{amount}}": "150000"
    }

    for paragraph in doc.paragraphs:
        for key, value in data.items():
            if key in paragraph.text:
                paragraph.text = paragraph.text.replace(key, value)

    output_filename = "tols/files/filled_contract.docx"
    doc.save(output_filename)
    print(f"✅ Документ создан: {output_filename}")


if __name__ == "__main__":
    main()