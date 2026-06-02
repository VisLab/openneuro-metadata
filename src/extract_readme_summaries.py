import os
import json
import re
from pathlib import Path

def extract_readme_info(filepath):
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    lines = content.split("\n")
    
    sections = []
    summary_lines = []
    key_information = []
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check if the next line is an underline (e.g., ==== or ----)
        is_underlined_header = False
        if i + 1 < len(lines):
            next_line = lines[i+1].strip()
            if len(next_line) >= 3 and set(next_line).issubset({"=", "-", "*"}):
                # Also ensure the current line isn't empty, and isn't just symbols itself
                if line and not set(line).issubset({"=", "-", "*"}):
                    is_underlined_header = True

        # Extract headers
        if re.match(r"^(#+)\s", line) or re.match(r"^[A-Z0-9\s]+:$", line) or re.match(r"^[A-Z0-9\s_]{3,}$", line) or is_underlined_header:
            header_text = line.lstrip("# \t").strip(":")
            if header_text and not set(header_text).issubset({"=", "-", "*"}):
                if header_text not in sections:
                    sections.append(header_text)
        elif line.startswith("- ") or line.startswith("* "):
            if len(key_information) < 5:  # Grab up to 5 list items as key info
                key_information.append(line.lstrip("- *"))
        elif len(summary_lines) < 3 and not line.startswith("#"):
            # Grab first few sentences for a basic summary
            summary_lines.append(line)
            
    summary = " ".join(summary_lines[:3]) if summary_lines else ""
    
    return {
        "summary": summary,
        "sections": sections,
        "key_information": key_information,
        "content_length": len(content),
    }

def main():
    base_dir = Path(__file__).resolve().parent.parent / "datasets" / "dataset_repos"
    output_file = Path(__file__).resolve().parent.parent / ".status" / "README_summaries.json"
    
    results = []
    if not base_dir.exists():
        print(f"Directory {base_dir} not found.")
        return

    for ds_folder in base_dir.iterdir():
        if ds_folder.is_dir() and ds_folder.name.startswith("ds"):
            readme_path = None
            for candidate in ["README.md", "README", "README.txt"]:
                target = ds_folder / candidate
                if target.exists():
                    readme_path = target
                    break
            
            if readme_path:
                info = extract_readme_info(readme_path)
                info["dataset"] = ds_folder.name
                info["file_name"] = readme_path.name
                results.append(info)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
        
    print(f"Processed {len(results)} README files and wrote to {output_file}")

if __name__ == "__main__":
    main()

