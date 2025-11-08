"""
Get the public IP address (https://checkip.amazonaws.com/)
"""

import requests
import logging

def get_public_ip():
    try:
        response = requests.get("https://checkip.amazonaws.com/", timeout=5)
        response.raise_for_status()
        ip_address = response.text.strip()
        return ip_address
    except requests.RequestException as e:
        raise TimeoutError(f"Failed to get public IP address: {e}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    get_public_ip()