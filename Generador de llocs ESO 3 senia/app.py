from flask import Flask

app = Flask(__name__)

@app.route('/ejecutar', methods=['GET'])
def ejecutar():
    # Aquí va la lógica que deseas ejecutar
    return "¡El script se ha ejecutado correctamente!"

if __name__ == '__main__':
    app.run(debug=True)
