from flask import Flask, request, jsonify
from flask_cors import CORS
import csv

app = Flask(__name__)
CORS(app)  # Permet aux requêtes de la page web d'accéder au serveur

def ajouter_nom_csv(nom, defi, fichier="noms.csv"):
    with open(fichier, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([nom, defi])

@app.route('/ajouter', methods=['POST'])
def ajouter():
    data = request.json
    nom = data.get("nom")
    defi = data.get("defi")
    
    if not nom or not defi:
        return jsonify({"message": "Données invalides"}), 400
    
    ajouter_nom_csv(nom, defi)
    return jsonify({"message": "Données enregistrées avec succès"}), 200

if __name__ == '__main__':
    print("✅ Serveur en cours d'exécution sur http://127.0.0.1:5000/")
    app.run(debug=True)
