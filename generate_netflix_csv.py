import pandas as pd
import random
from datetime import datetime, timedelta

# Lista de películas
peliculas = [
    "El Padrino", "Forrest Gump", "La Lista de Schindler", "El Señor de los Anillos: La Comunidad del Anillo",
    "Titanic", "Pulp Fiction", "El Rey León", "El Caballero de la Noche", "La La Land", "Toy Story",
    "Regreso al Futuro", "El Silencio de los Corderos", "Matrix", "Ciudadano Kane", "Volver al Futuro",
    "El Gran Dictador", "Gladiator", "La Vida es Bella", "Harry Potter y la Piedra Filosofal", "El Resplandor",
    "El Club de la Pelea", "Amélie", "La Guerra de las Galaxias", "Joker", "El Señor de los Anillos: El Retorno del Rey",
    "Los Siete Samuráis", "La Naranja Mecánica", "Interestelar", "La Sociedad de los Poetas Muertos", "Ciudad de Dios",
    "Casablanca", "El Laberinto del Fauno", "El Viaje de Chihiro", "El Gran Hotel Budapest", "Psicosis", "El Irlandés",
    "La Roca", "El Rey Arturo", "Memento", "Interstellar", "Los Miserables", "Shrek", "Terminator 2: El Juicio Final",
    "E.T. el Extraterrestre", "Nemo", "Wall-E", "Buscando a Nemo", "Up", "Amor Sin Barreras", "2001: Odisea del Espacio",
    "Blade Runner", "Indiana Jones: En Busca del Arca Perdida", "El Club de los Cinco", "La Princesa Mononoke",
    "El Planeta de los Simios", "Kill Bill", "El Mago de Oz", "Aladdin", "Avatar", "El Hombre Araña", "12 Hombres en Pugna",
    "Casino Royale", "American History X", "La Bella y la Bestia", "El Rescate del Soldado Ryan", "La Delgada Línea Roja",
    "La Historia Interminable", "Los Cazafantasmas", "Grease", "Scream", "Superman", "El Rey Arturo: La Leyenda de la Espada",
    "Los Increíbles", "Batman Begins", "Bambi", "Coco", "Rápido y Furioso", "El Exorcista", "El Show de Truman",
    "El Último Samurai", "El Cisne Negro", "El Gran Torino", "Lo que el Viento se Llevó", "La Forma del Agua",
    "La Pantera Rosa", "El Pianista", "La Vida de Pi", "La Cenicienta", "El Árbol de la Vida", "El Gran Lebowski",
    "El Efecto Mariposa", "Mary Poppins", "La Dama y el Vagabundo", "La Bella Durmiente", "Los Goonies",
    "El Bueno, el Malo y el Feo", "El Abuelo Espía", "El Mago de Oz", "El Cascanueces y los Cuatro Reinos",
    "El Guardián Invisible"
]

# Generar fechas de lanzamiento aleatorias en el rango de los últimos 50 años
#fecha_actual = datetime.now()
#fecha_lanzamiento = [fecha_actual - timedelta(days=random.randint(365*50, 0)) for a in range(len(peliculas))]

num_of_dates = 100
fecha_actual =  datetime.now()
fecha_lanzamiento = [fecha_actual.date() - timedelta(days=random.randint(0, 365*50))  for _ in range(len(peliculas))]



# Lista de clasificaciones posibles
clasificaciones = ['PG', 'PG-13', 'R', 'NC-17']

# Generar clasificación aleatoria para cada película
clasificacion = [random.choice(clasificaciones) for _ in range(len(peliculas))]

# Generar duraciones aleatorias en minutos
duracion = [random.randint(60, 180) for _ in range(len(peliculas))]

# Crear DataFrame
df = pd.DataFrame({'ID': range(1, len(peliculas)+1),
                   'Pelicula': peliculas,
                   'Fecha de Lanzamiento': fecha_lanzamiento,
                   'Clasificacion': clasificacion,
                   'Duracion (min)': duracion})

df["Fecha de Lanzamiento"] = pd.to_datetime(df["Fecha de Lanzamiento"])
# Agregar columna 'anio_lanzamiento' con el año de la fecha de lanzamiento
df['anio_lanzamiento'] = df['Fecha de Lanzamiento'].dt.year

# Guardar DataFrame como CSV
df.to_csv('peliculas_con_anio.csv', index=False)

print("Archivo 'peliculas_con_anio.csv' generado exitosamente.")
