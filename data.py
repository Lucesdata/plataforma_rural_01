import pandas as pd

# Cargar los datos del archivo proporcionado
file_path = 'valor_salida_caudal_1_.csv'  # Asegúrate de que esta ruta sea válida
sensor_data = pd.read_csv(file_path)

file_path2 = 'valor_salida_caudal_1_casca.csv'  # Asegúrate de que esta ruta sea válida
sensor_data2 = pd.read_csv(file_path2)

file_path3 = 'valor_salida_caudal_1_soledad.csv'  # Asegúrate de que esta ruta sea válida
sensor_data3 = pd.read_csv(file_path3)

file_path4 = 'valor_salida_caudal_1_voragine.csv'  # Asegúrate de que esta ruta sea válida
sensor_data4 = pd.read_csv(file_path4)

# Verifica si las columnas están correctamente nombradas
if 'Hour' not in sensor_data.columns or 'Average' not in sensor_data.columns:
    raise ValueError("El archivo CSV debe contener las columnas 'Hour' y 'Average'.")

if 'Hour' not in sensor_data2.columns or 'Average' not in sensor_data2.columns:
    raise ValueError("El archivo CSV debe contener las columnas 'Hour' y 'Average'.")

if 'Hour' not in sensor_data3.columns or 'Average' not in sensor_data3.columns:
    raise ValueError("El archivo CSV debe contener las columnas 'Hour' y 'Average'.")

if 'Hour' not in sensor_data4.columns or 'Average' not in sensor_data4.columns:
    raise ValueError("El archivo CSV debe contener las columnas 'Hour' y 'Average'.")

# Procesar los datos para la PTAP Campoalegre
sensor_data['Fecha'] = pd.to_datetime(sensor_data['Hour']).dt.date
campoalegre_daily = sensor_data.groupby('Fecha')['Average'].mean().reset_index()

sensor_data2['Fecha'] = pd.to_datetime(sensor_data2['Hour']).dt.date
cascajal_daily = sensor_data2.groupby('Fecha')['Average'].mean().reset_index()

sensor_data3['Fecha'] = pd.to_datetime(sensor_data3['Hour']).dt.date
soledad_daily = sensor_data3.groupby('Fecha')['Average'].mean().reset_index()

sensor_data4['Fecha'] = pd.to_datetime(sensor_data4['Hour']).dt.date
voragine_daily = sensor_data4.groupby('Fecha')['Average'].mean().reset_index()

# Renombrar las columnas para que coincidan con la estructura de datos
campoalegre_daily.columns = ['Fecha', 'valor_salida_caudal_1']
cascajal_daily.columns = ['Fecha', 'valor_salida_caudal_1']
soledad_daily.columns = ['Fecha', 'valor_salida_caudal_1']
voragine_daily.columns = ['Fecha', 'valor_salida_caudal_1']

# Información general de las plantas
data = {
    "PLANTA": [
        "PTAP Cascajal", "PTAP Campoalegre", "PTAP Soledad", "PTAP Carbonero",
        "PTAP Voragine", "PTAP Los Mangos", "PTAP La Sirena", "PTAP Km 18",
        "PTAP Montebello", "PTAP Pichinde"
    ],
    "NOMBRE": [
        "ASOCASCAJAL", "ACOPS", "ACUABUITRERA", "ACUABUITRERA",
        "ASOVORAGINE", "J.A.A. Alto los Mangos", "ASUAP La Sirena", "ACUA 18",
        "SERVIAGUAS", "ACUAPICHINDÉ"
    ],
    "VEREDA": [
        "Cascajal", "Campoalegre", "Soledad", "Carbonero",
        "Voragine", "Alto Los Mangos", "La Sirena", "Kilometro 18",
        "Montebello", "Pichinde"
    ],
    "CORREGIMIENTO": [
        "Hormiguero", "Montebello", "Buitrera", "Buitrera",
        "Pance", "Buitrera", "Buitrera", "La Elvira",
        "Montebello", "Pichinde"
    ],
    "FUENTE": [
        "Pozo profundo", "Bocatoma", "Bocatoma", "Bocatoma",
        "Bocatoma", "Bocatoma", "Bocatoma", "Bocatoma",
        "Bocatoma", "Bocatoma"
    ],
    "CAUDAL DISEÑO": [
        12.61, 8.1, 12.0, 12.0,
        3.0, 3.5, 18.0, 1.0,
        34.0, 1.2
    ],
    "CAUDAL CONCESION": [
        12.61, 12.2, 12.0, 12.0,
        3.0, 3.5, 18.0, 0.6,
        7.5, 6.3
    ],
    "TIPO DE PLANTA": [
        "Compacta", "FIME", "FIME", "FIME",
        "FIME", "FIME", "FIME", "FIME",
        "Convencional", "FIME"
    ],
    "Usuarios": [
        427, 996, 1811, 0,
        90, 533, 1120, 62,
        3020, 293
    ],
    "Población": [
        1708, 3984, 7244, 0,
        360, 2132, 4480, 248,
        12080, 1172
    ],
    "LATITUD": [
        3.31742, 3.46988, 3.38795, 3.37828,
        3.34090, 3.39228, 3.40170, 3.51468,
        3.50268, 3.44003
    ],
    "LONGITUD": [
        -76.51000, -76.55201, -76.59043, -76.59383,
        -76.59922, -76.58783, -76.57929, -76.62290,
        -76.56131, -76.62250
    ],
    "IMAGEN": [
        "/assets/cascajal.png", "/assets/campoalegre.png", "/assets/soledad.png", "/assets/carbonero.png",
        "/assets/voragine.png", "/assets/los_mangos.png", "/assets/sirena.png", "/assets/km18.png",
        "/assets/montebello.png", "/assets/pichinde.png"
    ]
}

data_sensores = {
    
    "PTAP Cascajal": {
        "Fecha": cascajal_daily['Fecha'].tolist(),
        "valor_salida_caudal_1": cascajal_daily['valor_salida_caudal_1'].tolist()
    },
    "PTAP Campoalegre": {
        "Fecha": campoalegre_daily['Fecha'].tolist(),
        "valor_salida_caudal_1": campoalegre_daily['valor_salida_caudal_1'].tolist()
    },
    "PTAP Soledad": {
        "Fecha": soledad_daily['Fecha'].tolist(),
        "valor_salida_caudal_1": soledad_daily['valor_salida_caudal_1'].tolist()
    },
    "PTAP Voragine": {
        "Fecha": voragine_daily['Fecha'].tolist(),
        "valor_salida_caudal_1": voragine_daily['valor_salida_caudal_1'].tolist()
    }
}

# Crear DataFrame para información general
df = pd.DataFrame(data)

# Función para obtener los datos de sensores de una planta específica
def get_sensor_data(planta):
    if planta in data_sensores:
        return pd.DataFrame(data_sensores[planta])
    else:
        return pd.DataFrame()
    



