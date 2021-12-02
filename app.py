from flask import Flask, render_template
from application import main
from application.model.DAO.lista_produtos_dao import ProdutosDao


app = Flask(__name__)

lista_Produtos = ProdutosDao().listarProdutos()

@app.route("/", methods = ['GET'])
def home():
    return render_template("index.html", lista_Produtos =lista_Produtos)

