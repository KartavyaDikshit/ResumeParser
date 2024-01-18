import os

def parse_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def check_keywords(text, keywords):
    for keyword in keywords:
        if keyword.lower() in text.lower():
            return True
    return False

def main():
    # Define the keywords file and resume file
    keywords_file = 'keywords.txt'
    resume_file = 'Resume.txt'

    # Read keywords from the file
    with open(keywords_file, 'r') as f:
        keywords = [line.strip() for line in f.readlines()]

    # Parse the resume text
    resume_text = parse_text(resume_file)

    # Check keywords and decide whether to accept or reject the resume
    if check_keywords(resume_text, keywords):
        print("Accepted: Resume.txt")
        # Here you can add any further processing for accepted resumes
    else:
        print("Rejected: Resume.txt")

if __name__ == "__main__":
    main()
