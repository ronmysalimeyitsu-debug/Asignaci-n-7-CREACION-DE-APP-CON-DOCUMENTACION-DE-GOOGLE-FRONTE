from flask import Flask, render_template, request, jsonify
import sqlite3
import os

app = Flask(__name__)
DB_NAME = 'database.db'

def init_db():
    """Inicializa la base de datos SQLite con una tabla optimizada para textos legales."""
    if not os.path.exists(DB_NAME):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS leyes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                codigo TEXT NOT NULL,
                articulo TEXT NOT NULL,
                titulo TEXT NOT NULL,
                contenido TEXT NOT NULL
            )
        ''')
        
        # Datos de prueba iniciales de leyes fundamentales
        sample_data = [
            ("Código Civil", "Artículo 1", "De las leyes y sus efectos", "La ley es obligatoria desde el día de su publicación en la Gaceta Oficial o desde la fecha posterior que ella misma determine."),
            ("Código Penal", "Artículo 1", "Principio de Legalidad", "Nadie podrá ser castigado por un hecho que no estuviere expresamente previsto como punible por la ley, ni con penas que ella no hubiere establecido previamente."),
            ("Constitución", "Artículo 5", "Soberanía Popular", "La soberanía reside intransferiblemente en el pueblo, quien la ejerce directamente en la forma prevista en esta Constitución y en la ley, y e indirectamente, mediante el sufragio."),
            ("LOPPNA", "Artículo 45", "Derecho a la Información", "Todos los niños, niñas y adolescentes tienen derecho a buscar, recibir y difundir informaciones e ideas de todo género...")
        ]
        
        cursor.executemany(
            "INSERT INTO leyes (codigo, articulo, titulo, contenido) VALUES (?, ?, ?, ?)", 
            sample_data
        )
        
        conn.commit()
        conn.close()

def consultar_codigo_externo(termino):
    """
    Función complementaria que amplía el repertorio de leyes venezolanas 
    (CPC, COPP, LOPNNA, Contencioso Administrativo, etc.) de manera transparente 
    sin alterar la estructura base de SQLite existente.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Directorio extendido de leyes fundamentales de Venezuela para soporte dinámico
    leyes_extendidas = [
        ("Código de Procedimiento Civil", "Artículo 1", "Reglas Procedimentales", "El proceso civil se sustanciará y decidirá con arreglo a las formas legales establecidas en este Código."),
        ("Código Orgánico Procesal Penal", "Artículo 1", "Juicio Previo y Debido Proceso", "Nadie podrá ser condenado sin un juicio previo, oral y público, realizado sin dilaciones indebidas..."),
        ("Ley Orgánica para la Protección de Niños, Niñas y Adolescentes (LOPNNA)", "Artículo 8", "Interés Superior del Niño", "El interés superior del niño es un principio de interpretación y aplicación de esta Ley, el cual es de obligatorio cumplimiento."),
        ("Ley Orgánica de la Jurisdicción Contencioso Administrativa", "Artículo 4", "Control de la Legalidad", "La Jurisdicción Contencioso Administrativa controla la legalidad de los actos, acciones y omisiones de la Administración Pública."),
        ("Ley Orgánica de Procedimientos Administrativos", "Artículo 1", "Ámbito de Aplicación", "La Administración Pública Nacional y la de los Estados regirán sus procedimientos por las normas contenidas en esta Ley.")
    ]
    
    # Verificamos si ya existen en la base de datos para incorporarlas si el usuario las busca
    termino_lower = termino.lower()
    for codigo, articulo, titulo, contenido in leyes_extendidas:
        if termino_lower in codigo.lower() or termino_lower in contenido.lower():
            # Comprobar si ya está registrado para evitar duplicados exactos
            cursor.execute("SELECT id FROM leyes WHERE codigo = ? AND articulo = ?", (codigo, articulo))
            if not cursor.fetchone():
                cursor.execute(
                    "INSERT INTO leyes (codigo, articulo, titulo, contenido) VALUES (?, ?, ?, ?)",
                    (codigo, articulo, titulo, contenido)
                )
                conn.commit()
                
    conn.close()

@app.route('/')
def index():
    """Renderiza la vista principal de la aplicación estilo DevTools."""
    return render_template('index.html')

@app.route('/api/buscar', methods=['GET'])
def buscar_leyes():
    """Endpoint de la API REST para la búsqueda dinámica y asíncrona de artículos legales."""
    query = request.args.get('q', '').strip()
    
    # Expande dinámicamente el repertorio legal si el término coincide
    if query:
        consultar_codigo_externo(query)
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    search_pattern = f"%{query}%"
    cursor.execute('''
        SELECT id, codigo, articulo, titulo, contenido 
        FROM leyes 
        WHERE codigo LIKE ? OR articulo LIKE ? OR titulo LIKE ? OR contenido LIKE ?
    ''', (search_pattern, search_pattern, search_pattern, search_pattern))
    
    rows = cursor.fetchall()
    conn.close()
    
    resultados = [
        {
            "id": row[0],
            "codigo": row[1],
            "articulo": row[2],
            "titulo": row[3],
            "contenido": row[4]
        }
        for row in rows
    ]
    
    return jsonify(resultados)

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)