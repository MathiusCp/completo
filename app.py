from flask import Flask, render_template_string

app = Flask(__name__)

# --- Plantilla base ---
base_html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{{ titulo }}</title>
    <style>
        body {
            margin: 0;
            font-family: "Segoe UI", sans-serif;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            text-align: center;
            padding: 40px;
        }
        .card {
            background: rgba(255,255,255,0.15);
            backdrop-filter: blur(6px);
            border-radius: 15px;
            padding: 30px;
            max-width: 600px;
            margin: auto;
            box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        }
        h1, h2 {
            margin-top: 0;
        }
        a {
            color: #ffe082;
            text-decoration: none;
            font-weight: bold;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="card">
        {{ contenido }}
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    contenido = "<h1>Un servidor me trajo aquí 😱</h1><p>Y ahora no puedo salir... <br>Pero al menos la vista está bonita 🌈</p>"
    return render_template_string(base_html, titulo="Inicio", contenido=contenido)

@app.route('/saludo/<nombre>')
def saludo(nombre):
    contenido = f"<h2>Hola {nombre} 👋</h2><p>Bienvenido a <strong>pgmoreno.byronrm.com</strong></p>"
    return render_template_string(base_html, titulo="Saludo", contenido=contenido)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234)
