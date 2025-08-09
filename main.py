from fastapi import FastAPI

app = FastAPI()

BOOK_DATABASE = [
    "Programando em Turbo Pascal 7.0",
    "Absolute FreeBSD - The Complete Guide to FreeBSD",
    "Aplicações iOS com Lazarus",
    "Linux A Bíblia",
    "Think Python",
    "Robust Python",
]

# Planejamento da API Livraria
# / ----------------------------> boas vindas [Endpoint criada]
# /list-books ------------------> listar todos os livros [Endpoint criada]
# /list-book-by-index/{index} --> listar um livro
# /get-random-boom -------------> sugerir um livro aleatório
# /add-book --------------------> adicionar um novo livro

@app.get("/")
async def home():
    return "Seja bem-vindo à Livraria!"

@app.get("/list-books")
async def list_books():
    return { "books": [BOOK_DATABASE] }

