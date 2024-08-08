from flask import Flask, render_template, request, send_file
from io import BytesIO
import qrcode
import json
import datetime

app = Flask(__name__)

def get_location(ip_address):
    try:
        response = requests.get(f'http://ipinfo.io/{ip_address}/json')
        data = response.json()
        location = {
            'city': data.get('city', 'Unknown'),
            'region': data.get('region', 'Unknown'),
            'country': data.get('country', 'Unknown')
        }
        return location
    except Exception as e:
        print(f"Error fetching location: {str(e)}")
        return {'city': 'Unknown', 'region': 'Unknown', 'country': 'Unknown'}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        img = qrcode.make(text)
        buffer = BytesIO()
        img.save(buffer, 'PNG')
        buffer.seek(0)
        ip_address = request.remote_addr
        location = get_location(ip_address)
        log_visit(ip_address, text, location) 
        return send_file(buffer, mimetype='image/png', as_attachment=True, download_name='qrcode.png')
    return render_template('home.html')

def log_visit(ip_address, text, location):
    log_entry = {
        'timestamp': datetime.datetime.now().isoformat(),
        'ip_address': ip_address, 
        'text': text, 
        'location': location 
    }
    try:
        with open('db/users_visits.json', 'r') as f:
            data = json.load(f) 
    except FileNotFoundError:
        data = []  
    
    data.append(log_entry)  
    
    with open('db/users_visits.json', 'w') as f:
        json.dump(data, f, indent=4) 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
