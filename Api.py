from flask import Flask, request, jsonify
from Banco import Banco


app = Flask(__name__)
db = Banco()

@app.route("/parceiros", methods=["GET"])
def get_parceiros():
    return jsonify(db.listar_parceiros())


@app.route("/parceiros", methods=["POST"])
def create_parceiro():
    data = request.json

    nome = data.get("nome")
    idade = data.get("idade")
    planeta = data.get("planeta")

    if db.add_parceiro(nome, idade, planeta):
        return jsonify({"message": "Parceiro criado!"}), 201

    return jsonify({"detail": "Nome duplicado!"}), 400


@app.route("/parceiros/<int:id>", methods=["PUT"])
def update_parceiro(id):
    data = request.json

    nome = data.get("nome")
    idade = data.get("idade")
    planeta = data.get("planeta")

    db.atualizar_parceiro(id, nome, idade, planeta)
    return jsonify({"message": "Parceiro atualizado!"})


@app.route("/parceiros/<int:id>", methods=["DELETE"])
def delete_parceiro(id):
    db.deletar_parceiro(id)
    return jsonify({"message": "Parceiro deletado!"})



@app.route("/personagens", methods=["GET"])
def get_personagens():
    return jsonify(db.listar_personagens())


if __name__ == "__main__":
    app.run(debug=True)
