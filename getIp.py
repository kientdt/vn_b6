import requests

def get_public_ip():
    response = requests.get('https://api.ipify.org?format=json')
    ip_data = response.json()
    return ip_data['ip']

public_ip = get_public_ip()
print(f'Your public IP address is: {public_ip}')
