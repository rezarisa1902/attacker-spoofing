from flask import Flask
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
        <input type="button" value="Click Me" onclick="alert('Anda Telah Masuk ke Halaman Facebook!')">
    </body>
    </html>
    """

if __name__ == '__main__':
    # Buka browser otomatis ke localhost:8080
    webbrowser.open("http://localhost:8080")
    # Jalankan server di port 8080
    app.run(host='0.0.0.0', port=8080, debug=True)