from pathlib import Path

def save_guide(content: str, filename: str) :
    folder = Path("saved_guides")
    folder.mkdir(exist_ok=True)

    file_path = folder / filename
    file_path.write_text(content, encoding="utf-8")
    print("Guide saved successfully")
    return 