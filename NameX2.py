import re

def extract_names_and_emails(filename):
    # Regular expression for matching email addresses
    email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    # Regular expression for matching names (firstname.lastname or firstinitial.lastname)
    name_regex = r'\b[A-Z][a-z]*\.[A-Z][a-z]*\b|\b[A-Z]\.[A-Z][a-z]*\b'
    
    names = set()
    emails = set()
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Find all email addresses in the line
                emails.update(re.findall(email_regex, line))
                
                # Find all names in the line
                names.update(re.findall(name_regex, line))
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please check the file name and try again.")
        return [], []
    
    return list(names), list(emails)

def main():
    input_file = input("Please enter the name of the text file to parse: ")
    names, emails = extract_names_and_emails(input_file)
    
    if names or emails:
        print("Extracted Names:")
        for name in names:
            print(name)
        
        print("\nExtracted Emails:")
        for email in emails:
            print(email)
    else:
        print("No names or emails found.")

if __name__ == "__main__":
    main()
