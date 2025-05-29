import csv, json
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

# Load data
def load_csv(file_path):
    with open(file_path, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

data_dir = Path("data")
profile = load_csv(data_dir / "Profile.csv")[0]
positions = load_csv(data_dir / "Positions.csv")
skills = [row["Name"] for row in load_csv(data_dir / "Skills.csv")]

# Store as JSON (optional step for reuse)
output_data = {
    "profile": profile,
    "positions": positions,
    "skills": skills,
}
Path("data/processed_data.json").write_text(json.dumps(output_data, indent=2), encoding="utf-8")

# Render with Jinja2
env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("index.html.j2")
output_html = template.render(**output_data)

# Save to site folder
Path("site/index.html").write_text(output_html, encoding="utf-8")