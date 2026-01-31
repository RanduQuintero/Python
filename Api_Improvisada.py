from fastapi import FastAPI

app = FastAPI()

cursos = [
    {"id": 1, "curso": "Python", "nivel": "Basico", "precio": 100},
    {"id": 2, "curso": "SQL", "nivel": "Intermedio", "precio": 120},
    {"id": 3, "curso": "Power BI", "nivel": "Avanzado", "precio": 150},
    {"id": 4, "curso": "Machine Learning", "nivel": "Avanzado", "precio": 200},
    {"id": 5, "curso": "Excel", "nivel": "Basico", "precio": 80}
]
productos = [
    {"id": 101, "producto": "Laptop", "categoria": "Tecnología", "precio": 1200},
    {"id": 102, "producto": "Mouse", "categoria": "Tecnología", "precio": 25},
    {"id": 103, "producto": "Teclado", "categoria": "Tecnología", "precio": 45},
    {"id": 104, "producto": "Monitor", "categoria": "Tecnología", "precio": 300},
    {"id": 105, "producto": "Impresora", "categoria": "Oficina", "precio": 180}
]

@app.get("/cursos")
def obtener_cursos():
    return cursos

@app.get("/productos")
def obtener_cursos():
    return productos
