import socket
import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

# Function 1: Port scanner
def scan_ports(target, ports=[80, 443, 8080]):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

# Function 2: HTTP headers check
def check_http_headers(url):
    try:
        res = requests.get(url)
        headers = res.headers
        security_headers = [
            'Content-Security-Policy',
            'X-Content-Type-Options',
            'X-Frame-Options',
            'Strict-Transport-Security',
            'Referrer-Policy'
        ]
        found_headers = {header: headers.get(header, 'Not Found') for header in security_headers}
        return found_headers
    except requests.RequestException as e:
        return {"error": str(e)}

# Function 3: XSS basic check
def check_xss(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)

    if not query_params:
        return "No GET parameters to test for XSS."

    xss_test_script = "<script>alert('XSS')</script>"
    vulnerable_params = []

    for param in query_params:
        original_values = query_params[param]
        test_values = [xss_test_script]
        
        for val in test_values:
            query_params[param] = val
            new_query = urlencode(query_params, doseq=True)
            new_url = urlunparse(parsed_url._replace(query=new_query))

            try:
                res = requests.get(new_url)
                if xss_test_script in res.text:
                    vulnerable_params.append(param)
            except requests.RequestException:
                pass

        query_params[param] = original_values

    if vulnerable_params:
        return f"⚠️ Possible XSS vulnerability found in parameters: {', '.join(vulnerable_params)}"
    else:
        return "✅ No XSS vulnerability found in GET parameters."

# Main function
def main():
    target = input("Enter the target URL (with http:// or https://): ").strip()
    if not target:
        print("No URL provided. Exiting...")
        return

    print(f"\n🔍 Scanning target: {target}\n")

    domain = target.split("//")[-1].split("/")[0]

    print("🌐 Checking open ports...")
    open_ports = scan_ports(domain)
    print(f"✅ Open ports found: {open_ports}" if open_ports else "❌ No open ports or host unreachable.")

    print("\n🛡️ Checking HTTP security headers...")
    headers = check_http_headers(target)
    if "error" in headers:
        print(f"❌ Error fetching headers: {headers['error']}")
    else:
        for header, value in headers.items():
            print(f"{header}: {value}")

    print("\n💉 Checking for XSS vulnerabilities...")
    xss_result = check_xss(target)
    print(xss_result)

if __name__ == "__main__":
    main()
