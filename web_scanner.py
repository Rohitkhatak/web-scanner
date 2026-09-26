#!/usr/bin/env python3
"""
Simple Web Scanner - Educational Purpose Only
Authorized testing ke liye hi use karein.
"""

import requests
import socket
import ssl
import sys
import argparse
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse, urljoin
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

__version__ = "1.0.0"

COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3306, 3389, 8080, 8443]
COMMON_DIRS = [
    'admin', 'login', 'wp-admin', 'phpmyadmin', 'backup', 'config', 'robots.txt',
    'sitemap.xml', '.git/HEAD', '.env', 'api', 'uploads', 'images', 'css', 'js'
]

def print_banner():
    print("=" * 50)
    print("       Simple Web Scanner v" + __version__)
    print("       Educational Purpose Only")
    print("=" * 50)

def scan_headers(url):
    print(f"\n[+] Scanning headers for {url}")
    try:
        r = requests.get(url, timeout=5, verify=False)
        print(f"Status Code: {r.status_code}")
        print(f"Server: {r.headers.get('Server', 'N/A')}")
        security_headers = [
            'X-Frame-Options', 'X-XSS-Protection', 'Content-Security-Policy',
            'Strict-Transport-Security', 'X-Content-Type-Options'
        ]
        for h in security_headers:
            print(f"{h}: {r.headers.get(h, 'Not Set')}")
    except Exception as e:
        print(f"Error: {e}")

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((host, port))
            if result == 0:
                return port
    except Exception:
        pass
    return None

def scan_ports(host, ports):
    print(f"\n[+] Scanning common ports on {host}")
    open_ports = []
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(scan_port, host, port): port for port in ports}
        for future in futures:
            port = futures[future]
            if future.result():
                open_ports.append(port)
                print(f"Port {port} is OPEN")
    if not open_ports:
        print("No common open ports found.")

def scan_directories(base_url):
    print(f"\n[+] Scanning common directories on {base_url}")
    base_url = base_url.rstrip('/') + '/'
    for d in COMMON_DIRS:
        url = urljoin(base_url, d)
        try:
            r = requests.get(url, timeout=3, verify=False, allow_redirects=False)
            if r.status_code in [200, 301, 302, 403]:
                print(f"{url} -> {r.status_code}")
        except Exception:
            pass

def scan_ssl(host):
    print(f"\n[+] SSL Certificate Info for {host}")
    try:
        context = ssl.create_default_context()
        with socket.create_connection((host, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                cert = ssock.getpeercert()
                print(f"Subject: {cert.get('subject')}")
                print(f"Issuer: {cert.get('issuer')}")
                print(f"Valid from: {cert.get('notBefore')}")
                print(f"Valid till: {cert.get('notAfter')}")
    except Exception as e:
        print(f"SSL Error: {e}")

def main():
    print_banner()
    parser = argparse.ArgumentParser(description="Simple Web Scanner - Educational Purpose Only")
    parser.add_argument("url", help="Target URL (e.g., https://example.com)")
    parser.add_argument("--ports", action="store_true", help="Scan common ports")
    parser.add_argument("--dirs", action="store_true", help="Scan common directories")
    parser.add_argument("--ssl", action="store_true", help="Check SSL certificate")
    parser.add_argument("--all", action="store_true", help="Run all scans")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    args = parser.parse_args()

    confirm = input("Kya aapke paas is target ko scan karne ki permission hai? (yes/no): ")
    if confirm.lower() != 'yes':
        print("Permission ke bina scan nahi kar sakte. Exiting.")
        sys.exit(1)

    parsed = urlparse(args.url)
    host = parsed.hostname
    if not host:
        print("Invalid URL")
        sys.exit(1)

    scan_headers(args.url)

    if args.ports or args.all:
        scan_ports(host, COMMON_PORTS)
    if args.dirs or args.all:
        scan_directories(args.url)
    if args.ssl or args.all:
        scan_ssl(host)

if __name__ == "__main__":
    main()
