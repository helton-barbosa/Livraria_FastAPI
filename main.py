from fastapi import FastAPI, HTTPException
from random import choice
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
# /list-book-by-index/{index} --> listar um livro [Endpoint criada]
# /get-random-book -------------> sugerir um livro aleatório [Endpoint criada]
# /add-book --------------------> adicionar um novo livro [Endpoint criada]

@app.get("/")
async def home() -> str:
    return "Seja bem-vindo à Livraria!"

@app.get("/list-books")
async def list_books():
    return { "books": BOOK_DATABASE }

@app.get("/list-book-by-index/{index}")
async def list_book_by_index(index: int):
    if index < 0 or index >= len(BOOK_DATABASE):
        raise HTTPException(404, "Index out of range")
    else:
        return { "books": BOOK_DATABASE[index] }

@app.get("/get-random-book")
async def get_random_book():
    livro_sorteado = choice(BOOK_DATABASE)
    return { "books": livro_sorteado }

@app.post("/add-book")
async def add_book(book: str):
    BOOK_DATABASE.append(book)
    return { "message": f"Book '{book}' was added!" }

