import os

# Function to hide a specific file from the directory listing
def list_files(hidden_file='malicious_file.txt'):
    try:
        # Get the list of files and directories in the current directory
        files = os.listdir('.')

        # Filter out the file you want to hide using a list comprehension
        visible_files = [file for file in files if file != hidden_file]

        # Print visible files
        for file in visible_files:
            print(file)

    except Exception as e:
        # Handle any exception (like permission issues, etc.)
        print(f"Error accessing directory: {e}")

# Call the function, hiding 'malicious_file.txt'
list_files()
