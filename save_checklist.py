from pathlib import Path

def save_checklist(content: str, filename: str) :
    folder = Path("saved_checklist")
    folder.mkdir(exist_ok=True)

    file_path = folder / filename
    file_path.write_text(content, encoding="utf-8")
    print("checklist saved successfully")
    return
   