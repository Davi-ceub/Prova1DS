from fastapi import FastAPI, HTTPException
from Banco import Banco
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
db = Banco()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/parceiros")
def get_parceiros():
    return db.listar_parceiros()

@app.post("/parceiros")
def create_parceiro(nome: str, idade: int, planeta: str):
    if db.add_parceiro(nome, idade, planeta):
        return {"message": "Parceiro criado!"}
    raise HTTPException(status_code=400, detail="Nome duplicado!")

@app.put("/parceiros/{id}")
def update_parceiro(id: int, nome: str, idade: int, planeta: str):
    db.atualizar_parceiro(id, nome, idade, planeta)
    return {"message": "Parceiro atualizado!"}

@app.delete("/parceiros/{id}")
def delete_parceiro(id: int):
    db.deletar_parceiro(id)
    return {"message": "Parceiro deletado!"}


@app.get("/personagens")
def get_personagens():
    return db.listar_personagens()
