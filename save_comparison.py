from pathlib import Path


def save_comparison(
    content: str,
    country1_name: str,
    country2_name: str
):
    folder = Path("saved_comparisons")
    folder.mkdir(exist_ok=True)

    filename = (
        f"{country1_name}_vs_{country2_name}.txt"
    )

    file_path = folder / filename
    file_path.write_text(content, encoding="utf-8")

    return file_path