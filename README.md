# whois-domain-explorer

[![Python Version](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A Python-based tool to explore domains and IP addresses. Retrieve **WHOIS information** for domains and detailed **IP info** such as location, ISP, and organization. Perfect for network reconnaissance, cybersecurity tasks, or just exploring the internet.

## Features

- Lookup WHOIS data for domain names.
- Gather IP information (country, city, ISP, ASN, etc.).
- Clear and readable console output.
- Supports both domains and IP addresses seamlessly.

## Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/GhaliAmli/whois-domain-explorer.git
cd whois-domain-explorer
pip install -r requirements.txt
````

`requirements.txt` should include:

```
python-whois
requests
```

## Usage

Run the tool and enter a domain or IP address when prompted:

```bash
python main.py
```

Example:

```
Enter an IP or domain: example.com
```

* If a domain is entered, WHOIS information will be displayed.
* If an IP address is entered, location, ISP, and other details will be shown.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
