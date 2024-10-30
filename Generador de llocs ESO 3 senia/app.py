from flask import Flask, render_template
import subprocess  # Para ejecutar scripts

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejecutar')
def ejecutar():
    # Aquí puedes llamar a tu archivo Python
    # Por ejemplo, si tienes un script llamado 'script.py'
    resultado = subprocess.run(['python', 'script.py'], capture_output=True, text=True)
    return f"<pre>{resultado.stdout}</pre>"

if __name__ == '__main__':
    app.run(debug=True)

