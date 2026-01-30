import sys


def main() -> int:  
    for filename in sys.argv[1:]:
        print(filename)
        if filename.endswith(".md"):
            process_file(filename)
    return 0

def process_file(filename: str) -> str:
    business_approver_section = False
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines:
        if "Business Approvers" in line:
            business_approver_section = True
        if not business_approver_section or ":" not in line:
            continue
        _, right = line.split(":", 1)
        right = right.strip().strip('\n')
        if not right in ["Y", "N"]:
            raise ValueError(f'Approvers need a "Y" or "N" for each approver. Did not get in {filename}')


if __name__ == "__main__":
    main()