import sys

def extract_names(file_path):
    try:
        with open(file_path, 'r') as f:
            lines = f.read().strip().split('\n')
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return

    with open('employees.tsv', 'w') as out:
        out.write("Name\tSurname\tE-mail\n")
        for email in lines:
            if '@' in email and '.' in email:
                parts = email.split('@')[0].split('.')
                if len(parts) == 2:
                    name, surname = parts
                    name = name.capitalize()
                    surname = surname.capitalize()
                    out.write(f"{name}\t{surname}\t{email}\n")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 names_extractor.py <path_to_file>")
    else:
        extract_names(sys.argv[1])
