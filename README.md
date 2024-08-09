### HeaderScanner performs checks for security headers and software banners on websites. The script identifies if essential headers are present and detects banners that may expose sensitive information about the server and the technologies used.

- Checks: Essential security headers.
- Detects: Software banners that may reveal sensitive information.
- Color:
  - Green for present headers and safe banners.
  - Red for missing headers.

### Usage:
- -u or `--url`: Base URL of the target site.
- `python3 headers_scanner.py -u http://example.com`

![checkheaders](https://github.com/user-attachments/assets/ee1e4dfd-20ab-4172-8005-4782dc4459d6)

### Dependencies:
- requests: Library for making HTTP requests -> `pip install requests`
- argparse: Standard library for command-line argument parsing -> `pip install argparse`
- colorama: Library for colored terminal text -> `pip install colorama`

