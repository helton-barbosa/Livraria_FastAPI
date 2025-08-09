from fastapi import FastAPI

app = FastAPI()

# Planejamento da API Livraria
# / ----------------------------> boas vindas [Endpoint criada]
# /list-books ------------------> listar todos os livros
# /list-book-by-index/{index} --> listar um livro
# /get-random-boom -------------> sugerir um livro aleatório
# /add-book --------------------> adicionar um novo livro

@app.get("/")
async def home():
    return "Seja bem-vindo à Livraria!"

