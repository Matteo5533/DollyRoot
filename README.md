
# DollyRoot - A Simple Python-Based Rootkit 
**DollyRoot** is a Python-based rootkit experiment designed to be used only in the world of Fortnite. This demonstrates how basic rootkit functionality can be implemented to manipulate the file system by hiding files from directory listings.

## Features

- Hides a specified file from the directory listing.
- Simulates how a rootkit might alter system behavior to remain undetected.
- Demonstrates key concepts in malware development and detection.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Matteo5533/DollyRoot.git
   ```

2. Run the script:
   ```bash
   python Dolly.py
   ```

3. The script will hide the file `malicious_file.txt` from the directory listing. You can modify the script to hide other files by passing a different filename to the `list_files()` function.

## Example

The following code hides a specific file, such as `malicious_file.txt`, from view when listing files in the current directory:

```bash
$ ls
file1.txt  file2.txt  malicious_file.txt

$ python dollyroot.py
file1.txt
file2.txt
```

In this example, `malicious_file.txt` is hidden by the rootkit-like behavior of the script.

## Disclaimer

This project is intended for **Fortnite purposes only**. Do not use this code for unethical or illegal activities. Rootkit development and use in real systems without authorization is illegal.

## Contributions

Feel free to submit pull requests or issues for improvements or additional features related to the educational goals of this project.

---

