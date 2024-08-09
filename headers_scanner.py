import argparse
import requests
from colorama import Fore, Style, init

init(autoreset=True)

recommended_headers = [
    "Content-Security-Policy",
    "Content-Type",
    "Cross-Origin-Embedder-Policy",
    "Cross-Origin-Opener-Policy",
    "Permissions-Policy",
    "Referrer-Policy",
    "Server",
    "Strict-Transport-Security",
    "Vary",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "X-XSS-Protection"
]

dangerous_headers = [
    "X-Powered-By",
    "X-AspNet-Version",
    "X-AspNetMvc-Version",
    "X-PHP-Version",
    "X-Backend-Server",
    "X-Generator",
    "X-Drupal-Cache",
    "X-Jenkins",
    "X-Pingback",
    "X-Page-Speed",
    "X-Runtime",
    "X-Amz-Cf-Id",
    "X-Amz-Request-Id",
    "Via"
]

def checkHeaders(url):
    try:
        response = requests.get(url)
    
        headers = response.headers
        
        print(f"Checking headers for: {url}\n")
        
        print("Recommended headers check:")
        for header in recommended_headers:
            if header in headers:
                print(f"{Fore.GREEN}[+] {header}: {headers[header]}")
            else:
                print(f"{Fore.RED}[-] {header}")

        found_banners = []
        
        for header in headers:
            if header in dangerous_headers or "version" in header.lower():
                found_banners.append(f"{Fore.GREEN}[+] {header}: {headers[header]}")
        
        if found_banners:
            print("\nDangerous banners:")
            for item in found_banners:
                print(item)
        
    except requests.RequestException as e:
        print(f"Error accessing URL {url}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Verify HTTP headers!")
    
    parser.add_argument("-u", "--url", required=True, help="Target URL")
    
    args = parser.parse_args()
    
    checkHeaders(args.url)
    
if __name__ == "__main__":
    main()
