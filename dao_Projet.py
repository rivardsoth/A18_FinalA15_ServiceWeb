from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import datetime
from flasgger import swag_from, Swagger

app = Flask(__name__)
CORS(app)
app.config['SWAGGER']={
    'title': 'Gestion de Projet A15 Examen Final',
    'version':1.0

}

# Configuration de la base de données SQLite3
db_name = 'A15Final.db'

#commentaire
# Creer la base de donnee
def create_table():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Projet (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Code_Projet TEXT,
            Description TEXT
        )
    ''')
    conn.commit()
    conn.close()


# Route pour enregistrer les données de température
@app.route('/projet', methods=['POST'])
def ajouter_Projet():
    """

     Example endpoint for adding a projet.
    ---
        parameters:
          - name: code_projet
            in: path
            type: String
            required: true
          - name: Description
            in: path
            type: String
            required: true
        responses:
          201:
            description: Project that was added
    """
    data = request.json

    Code_Projet = data.get('Code_Projet')
    Description = data.get('Description')

    # Affichez la réponse
    print(Code_Projet)
    print(Description)

    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Projet (Code_Projet, Description) VALUES (?, ?)',
                       (Code_Projet, Description))
        conn.commit()
        conn.close()
        return jsonify({"message": "Données enregistrées avec succès"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route pour afficher toutes les données de la base de données
@app.route('/afficherTout', methods=['GET'])
def get_all_temperature_data():
        try:
            conn = sqlite3.connect(db_name)
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Projet')
            data = cursor.fetchall()
            conn.close()

            # Convertir les données en une liste de dictionnaires
            data_list = []
            for row in data:
                data_dict = {
                    'id': row[0],
                    'Code_Projet': row[1],
                    'Description': row[2]
                }
                data_list.append(data_dict)

            return jsonify(data_list)
        except Exception as e:
            return jsonify({"error": str(e)}), 500


# pour demarrer l'application
if __name__ == '__main__':
    swagger = Swagger(app)
    create_table()
    app.run(host='0.0.0.0',debug=True)
