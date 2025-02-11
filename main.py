import os
from groq import Groq
import json
from markdown import Markdown

# Load the Groq API key from a JSON file
with open('secrets.json') as f:
    api_key_data = json.load(f)
groq_api_key = api_key_data['GROQ_API_KEY']

# Set up the Groq API client
client = Groq(
    api_key=groq_api_key,
)

while True:
    # Get the book title and author from the user
    book_title = input("Enter the book title: ")
    book_author = input("Enter the book author: ")

    book_info = book_title.replace(" ", "-") + "_" + book_author.replace(" ", "-")
    # Create a folder with the book title and author as the folder name
    folder_name = book_info
    os.makedirs(folder_name, exist_ok=True)

    # Create a markdown file about the book
    md_file_path = os.path.join(folder_name, "README.md")
    md = Markdown()
    with open(md_file_path, "w") as f:
        f.write("# " + book_title + "\n")
        f.write("## Author: " + book_author + "\n")
        f.write("## Description: (insert description here)\n")

    # Use the Groq API to generate a markdown file about the book
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "you are a librarian searching for book summaries and info."
            },
            {
                "role": "user",
                "content": f"Provide a brief summary of the book '{book_title}' by {book_author}. Give some information about the author. Provide links to top google search results of book",
            }
        ],
        model="llama3-8b-8192",
    )

    if chat_completion.choices:
        book_data = chat_completion.choices[0].message.content
        with open(md_file_path, "a") as f:
            f.write(book_data)
    else:
        print("Error fetching book data from Groq API")

    print(f"Book folder created: {folder_name}")
    print(f"Markdown file created: {md_file_path}")

    response = input("Continue creating book folders and markdown files? (y/n): ")
    if response.lower() != 'y':
        break

print("Book creation process complete.")
