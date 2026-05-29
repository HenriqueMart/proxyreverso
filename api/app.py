from flask import Flask, request, jsonify
from database import mysql, init_db

app = Flask(__name__)
init_db(app)

@app.route('/clientes', methods=['GET'])
def listar_clientes():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM clientes")
    rows = cur.fetchall()
    cur.close()
    clientes = [{"id": r[0], "nome": r[1], "email": r[2]} for r in rows]
    return jsonify(clientes)

@app.route('/clientes/<int:id>', methods=['GET'])
def buscar_cliente(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM clientes WHERE id = %s", (id,))
    r = cur.fetchone()
    cur.close()
    if not r:
        return jsonify({"erro": "Cliente não encontrado"}), 404
    return jsonify({"id": r[0], "nome": r[1], "email": r[2]})

@app.route('/clientes', methods=['POST'])
def criar_cliente():
    dados = request.get_json()
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO clientes (nome, email) VALUES (%s, %s)",
                (dados['nome'], dados['email']))
    mysql.connection.commit()
    cur.close()
    return jsonify({"mensagem": "Cliente criado"}), 201

@app.route('/clientes/<int:id>', methods=['PUT'])
def atualizar_cliente(id):
    dados = request.get_json()
    cur = mysql.connection.cursor()
    cur.execute("UPDATE clientes SET nome=%s, email=%s WHERE id=%s",
                (dados['nome'], dados['email'], id))
    mysql.connection.commit()
    cur.close()
    return jsonify({"mensagem": "Cliente atualizado"})

@app.route('/clientes/<int:id>', methods=['DELETE'])
def deletar_cliente(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM clientes WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()
    return jsonify({"mensagem": "Cliente deletado"})

@app.route('/produtos', methods=['GET'])
def listar_produtos():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM produtos")
    rows = cur.fetchall()
    cur.close()
    produtos = [{"id": r[0], "nome": r[1], "preco": float(r[2]), "estoque": r[3]} for r in rows]
    return jsonify(produtos)

@app.route('/produtos/<int:id>', methods=['GET'])
def buscar_produto(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM produtos WHERE id = %s", (id,))
    r = cur.fetchone()
    cur.close()
    if not r:
        return jsonify({"erro": "Produto não encontrado"}), 404
    return jsonify({"id": r[0], "nome": r[1], "preco": float(r[2]), "estoque": r[3]})

@app.route('/produtos', methods=['POST'])
def criar_produto():
    dados = request.get_json()
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO produtos (nome, preco, estoque) VALUES (%s, %s, %s)",
                (dados['nome'], dados['preco'], dados.get('estoque', 0)))
    mysql.connection.commit()
    cur.close()
    return jsonify({"mensagem": "Produto criado"}), 201

@app.route('/produtos/<int:id>', methods=['PUT'])
def atualizar_produto(id):
    dados = request.get_json()
    cur = mysql.connection.cursor()
    cur.execute("UPDATE produtos SET nome=%s, preco=%s, estoque=%s WHERE id=%s",
                (dados['nome'], dados['preco'], dados['estoque'], id))
    mysql.connection.commit()
    cur.close()
    return jsonify({"mensagem": "Produto atualizado"})

@app.route('/produtos/<int:id>', methods=['DELETE'])
def deletar_produto(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM produtos WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()
    return jsonify({"mensagem": "Produto deletado"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)