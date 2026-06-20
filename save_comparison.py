from pathlib import Path

def save_comparison(content: str, filename: str):
    folder = Path("saved_comparisons")
    folder.mkdir(exist_ok=True)

    file_path = folder / filename
    file_path.write_text(content, encoding="utf-8")

    print("Comparison saved successfully.")