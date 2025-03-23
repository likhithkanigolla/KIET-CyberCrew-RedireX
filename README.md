# KIET-CyberCrew-RedireX

KIET-CyberCrew-RedireX is a tool designed to detect open redirect vulnerabilities in web applications. It helps security researchers and penetration testers identify URLs that are susceptible to redirection attacks.

## Features

- Fast and efficient open redirect vulnerability scanning
- Customizable payloads and detection patterns
- Concurrent scanning capabilities
- Easy to use command-line interface

## Installation

```bash
git clone https://github.com/likhithkanigolla/KIET-CyberCrew-RedireX.git
cd KIET-CyberCrew-RedireX
pip install -r requirements.txt
```

## Usage

Basic usage with a list of URLs:

```bash
python3 KIET-CyberCrew-RedireX.py -k FUZZ -c 1 < urls.txt
```

Where:
- `-k FUZZ`: Specifies the keyword to replace in URLs (FUZZ will be replaced with payload)
- `-c 1`: Sets concurrency level to 1 (number of simultaneous requests)
- `urls.txt`: A file containing target URLs, one per line

## Input Format

Your `urls.txt` file should contain URLs with the FUZZ keyword marking where the payload should be inserted:

```
https://example.com/redirect?url=FUZZ
https://example.com/redirect.php?url=FUZZ
https://example.com/redirect?next=FUZZ
```

## Advanced Options

```
  -h, --help            Show help message
  -k KEYWORD, --keyword KEYWORD
                        Keyword to replace with payloads (default: FUZZ)
  -p PAYLOAD_FILE, --payload-file PAYLOAD_FILE
                        File containing payloads (default: payloads.txt)
  -c CONCURRENCY, --concurrency CONCURRENCY
                        Number of concurrent requests (default: 10)
  -t TIMEOUT, --timeout TIMEOUT
                        Request timeout in seconds (default: 5)
  -o OUTPUT, --output OUTPUT
                        Output file to save results
  -v, --verbose         Enable verbose output
```

## Example

1. Create a file named `urls.txt` with potential vulnerable URLs:
   ```
   https://example.com/redirect?url=FUZZ
   https://vulnerable-site.com/redirect?next=FUZZ
   ```

2. Run KIET-CyberCrew-RedireX:
   ```bash
   python3 KIET-CyberCrew-RedireX.py -k FUZZ -c 1 < urls.txt
   ```

3. Review the results to identify vulnerable endpoints.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
