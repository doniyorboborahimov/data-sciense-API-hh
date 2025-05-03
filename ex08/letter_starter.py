import sys

def get_name_from_email(email, filepath='employees.tsv'):
    try:
        with open(filepath, 'r') as f:
            lines = f.read().strip().split('\n')[1:]  # skip header
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return None

    for line in lines:
        name, surname, mail = line.split('\t')
        if mail.lower() == email.lower():
            return name
    return None

def print_welcome_letter(name):
    print(f"Dear {name}, welcome to our team. "
          "We are sure that it will be a pleasure to work with you. "
          "That’s a precondition for the professionals that our company hires.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 letter_starter.py <email>")
    else:
        name = get_name_from_email(sys.argv[1])
        if name:
            print_welcome_letter(name)
