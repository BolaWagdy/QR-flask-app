import json

def analyze_visits(log_file='users_visits.json'):
    try:
        with open(log_file, 'r') as f:
            data = json.load(f)
        ip_addresses = {entry['ip_address'] for entry in data} 
        unique_visits = len(ip_addresses)  
        print(f'Unique visits: {unique_visits}')
    except FileNotFoundError:
        print('Log file not found.') 

if __name__ == "__main__":
    analyze_visits() 
