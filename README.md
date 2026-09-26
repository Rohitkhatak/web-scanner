
# 🛡️ Simple Web Scanner

A lightweight Python-based web scanning tool for **educational purposes only**. It performs basic reconnaissance on web targets including HTTP security headers, common open ports, common directories/files, and SSL certificate information.

> ⚠️ **DISCLAIMER**: This tool is intended for **authorized security testing and educational purposes only**. Do NOT use it against any system without explicit written permission. The author is not responsible for any misuse or damage caused by this tool.

---

## ✨ Features

- 🔍 **HTTP Security Headers Check** — Detects missing security headers like CSP, HSTS, X-Frame-Options, etc.
- 🌐 **Port Scanner** — Scans common ports (21, 22, 80, 443, 3306, etc.) using multi-threading.
- 📂 **Directory/File Discovery** — Checks for common paths like `/admin`, `/login`, `.env`, `.git/HEAD`, etc.
- 🔐 **SSL Certificate Info** — Retrieves certificate subject, issuer, and validity dates.
- 🧵 **Multi-threaded** — Fast port scanning using `ThreadPoolExecutor`.
- ✅ **Permission Prompt** — Asks for confirmation before scanning any target.

---

## 📦 Installation

### Prerequisites
- Python 3.6 or higher
- pip

### Steps

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/web-scanner.git
cd web-scanner

# (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## 🚀 Usage

```bash
python web_scanner.py <URL> [options]
```

### Options

| Flag       | Description                          |
|------------|--------------------------------------|
| `--ports`  | Scan common open ports               |
| `--dirs`   | Scan common directories and files    |
| `--ssl`    | Fetch SSL certificate information    |
| `--all`    | Run all scans                        |
| `--version`| Show tool version                    |
| `-h`       | Show help message                    |

### Examples

```bash
# Scan only headers
python web_scanner.py https://example.com

# Scan ports
python web_scanner.py https://example.com --ports

# Scan directories
python web_scanner.py https://example.com --dirs

# Full scan
python web_scanner.py https://example.com --all
```

### Sample Output

```
==================================================
       Simple Web Scanner v1.0.0
       Educational Purpose Only
==================================================
Kya aapke paas is target ko scan karne ki permission hai? (yes/no): yes

[+] Scanning headers for https://example.com
Status Code: 200
Server: ECS (dcb/7F83)
X-Frame-Options: Not Set
...

[+] Scanning common ports on example.com
Port 80 is OPEN
Port 443 is OPEN
...
```

---

## 🗂️ Project Structure

```
web-scanner/
├── web_scanner.py       # Main scanner script
├── requirements.txt     # Python dependencies
├── README.md            # Documentation
├── LICENSE              # MIT License
├── CONTRIBUTING.md      # Contribution guidelines
└── .gitignore           # Git ignore rules
```

---

## ⚖️ Legal & Ethical Notice

- Use this tool **only** on systems you own or have **written permission** to test.
- Unauthorized scanning is **illegal** under laws like the IT Act (India), CFAA (USA), and similar laws worldwide.
- The developer assumes **no liability** for misuse.

---

## 🤝 Contributing

Pull requests are welcome! Please read `CONTRIBUTING.md` first.

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## ⭐ Support

If you find this project useful, please give it a ⭐ on GitHub!
