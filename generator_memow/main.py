# Import
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

# Form results
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # pobierz wybrany obraz
        selected_image = request.form.get('image-selector')

        # Realizacja #2. Otrzymywanie tekstu
        
        
        

        # Realizacja #3. Potwierdzenie umieszczenia tekstu
        

        # Realizacja #3. Odbiór koloru tekstu
        

        return render_template('index.html', 
                               # Wyświetlanie wybranego obrazu
                               selected_image=selected_image, 

                               # Zadanie #2. Wyświetlanie tekstu
                               
                               
                               # Zadanie #3.Wizualizacja koloru
                               
                               # Zadanie #3. Wyświetlanie pozycjonowania tekstu

                               )
    else:
        # # Domyślne wyświetlanie pierwszego obrazu
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)
