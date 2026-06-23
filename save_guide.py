from pathlib import Path


def save_guide(content: str, country_name: str, guide_type: str):
    folder = Path("saved_guides")
    folder.mkdir(exist_ok=True)

    filename = f"{country_name}_{guide_type}_guide.txt"

    file_path = folder / filename
    file_path.write_text(content, encoding="utf-8")

    return file_path