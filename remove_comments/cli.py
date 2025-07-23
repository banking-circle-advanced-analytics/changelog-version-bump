import sys
import re
from pathlib import Path
import subprocess


def main() -> int:  
    for filename in sys.argv[1:]:
        print(filename)
        if filename.endswith(".md"):
            process_file(filename)
    return 0

def process_file(filename: str) -> str:
    content = Path(filename).read_text(encoding="utf-8")
    # Remove full-line comments and inline comments
    cleaned = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    # Remove blank lines that result
    cleaned = '\n'.join(line for line in cleaned.splitlines() if line.strip())
    new_cleaned = []
    for line in cleaned.splitlines():
        if not (line.startswith('#') or line.startswith('-')):        
            line = "- " + line

        new_cleaned.append(line)
    cleaned = '\n'.join(line for line in new_cleaned)
    Path(filename).write_text(cleaned + '\n', encoding="utf-8")
    # Automatically add file back
    subprocess.run(["git", "add", filename], check=True, stdout=subprocess.PIPE)

if __name__ == "__main__":
    main()