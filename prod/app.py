import streamlit as st
import pandas as pd
import numpy as np
import pickle

#file_in = open('modelo_6v.pkl','rb')
model = pickle.load(open('modelo_6v.pkl','rb'))

def prediction(df):
    predicted = model.predict(df)
    probas =  model.predict_proba(df)
    if predicted[0] == 0:
          pred = "NADA"
    elif predicted[0] == 1:
        pred = "PRIMARIA"
    elif predicted[0] == 2:
        pred = "SECUNDARIA"
    elif predicted[0] == 3:
        pred = "PREPARATORIA"
    elif predicted[0] == 4:
        pred = "UNIVERSIDAD"
    else:
        prediction = "POSGRADO"
    prediction= f"""{pred} \n
    PROBABILIDAD DE QUE TU MAXIMO NIVEL DE ESTUDIOS SEA:\n
        1. NINGUN NIVEL: {round(probas[:,0][0]*100, 1)}%
        2. PRIMARIA: {round(probas[:,1][0]*100,1)}%
        3. SECUNDARIA: {round(probas[:,2][0]*100,1)}%
        4. PREPARATORIA: {round(probas[:,3][0]*100,1)}%
        5. UNIVERSIDAD: {round(probas[:,4][0]*100,1)}%
        6. POSGRADO: {round(probas[:,5][0]*100,1)}%
    """
    return prediction

def main():
    html_temp = """
    <style>
        .reportview-container {
            background-color: #e9e3e3;
            font-family: Arial, sans-serif;
        }
        .big-font {
            font-size: 3em !important;
            color: rgb(8, 123, 8) !important;
        }
        h2 {
            color: rgb(8, 123, 8);
        }
    </style>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    st.markdown('<div class="big-font">Cuestionario para determinar tu nivel academico</div>', unsafe_allow_html=True)
    mun_options = {
    "Azcapotzalco": "002",
    "Coyoacán": "003",
    "Cuajimalpa de Morelos": "004",
    "Gustavo A. Madero": "005",
    "Iztacalco": "006",
    "Iztapalapa": "007",
    "La Magdalena Contreras": "008",
    "Milpa Alta": "009",
    "Álvaro Obregón": "010",
    "Tláhuac": "011",
    "Tlalpan": "012",
    "Xochimilco": "013",
    "Benito Juárez": "014",
    "Cuauhtémoc": "015",
    "Miguel Hidalgo": "016",
    "Venustiano Carranza": "017",
    "Demarcación territorial no especificada": "999"}
    municipio = st.selectbox('Municipio o Demarcación territorial:',
                            options=mun_options)

    sex_options = {
    "Hombre": "1",
    "Mujer": "3"}
    sexo = st.selectbox('Sexo:', options=sex_options)

    edad = st.number_input('Edad:', min_value=0, max_value=130)

    edo_options = {
    "Aguascalientes": "01",
    "Baja California": "02",
    "Baja California Sur": "03",
    "Campeche": "04",
    "Coahuila": "05",
    "Colima": "06",
    "Chiapas": "07",
    "Chihuahua": "08",
    "Ciudad de México": "09",
    "Durango": "10",
    "Guanajuato": "11",
    "Guerrero": "12",
    "Hidalgo": "13",
    "Jalisco": "14",
    "México": "15",
    "Michoacán": "16",
    "Morelos": "17",
    "Nayarit": "18",
    "Nuevo León": "19",
    "Oaxaca": "20",
    "Puebla": "21",
    "Querétaro": "22",
    "Quintana Roo": "23",
    "San Luis Potosí": "24",
    "Sinaloa": "25",
    "Sonora": "26",
    "Tabasco": "27",
    "Tamaulipas": "28",
    "Tlaxcala": "29",
    "Veracruz": "30",
    "Yucatán": "31",
    "Zacatecas": "32"}
    estadoNacimiento = st.selectbox('¿En qué estado de la República Mexicana nació?',
                                    options=edo_options)

    closed_options1 = {
    "Si": "1",
    "No": "3",
    "No especificado": "9",
    "Blanco por pase":np.NaN}
    nacionalidadMexicana = st.selectbox('¿Tiene nacionalidad mexicana?',
                                        options=closed_options1)

    sal_options = {
    "Seguro Social (IMSS)": "01",
    "ISSSTE": "02",
    "ISSSTE estatal": "03",
    "PEMEX, Defensa o Marina": "04",
    "Centro de Salud u Hospital de la SSA, Seguro Popular o Instituto de Salud para el Bienestar": "05",
    "IMSS-PROSPERA o IMSS-BIENESTAR": "06",
    "Consultorio, clínica u hospital privado": "07",
    "Consultorio de farmacia": "08",
    "Otro lugar": "09",
    "No se atiende": "10",
    "No especificado": "99"}
    atencionSalud = st.selectbox('Cuando tiene problemas de salud, ¿en dónde se atiende?',
                                  options=sal_options)

    afromexicano = st.selectbox('Por sus antepasados y de acuerdo con sus costumbres y tradiciones, ¿se considera afromexicano(a), negro(a) o afrodescendiente?',
                        options=closed_options1)

    acta_options = {
    "la República Mexicana": "1",
    "otro país": "2",
    "Entonces, ¿no tiene registro de nacimiento?": "3",
    "No especificado": "9"}
    actaNacimiento = st.selectbox('¿Tiene acta de nacimiento o está inscrita(o) en el registro civil de:',
                                  options=acta_options)
    rel_options = {
    "Católica": "1101",
    "Católico ortodoxo": "1201",
    "Anabautista/Menonita": "1301",
    "Anglicana/Episcopal": "1302",
    "Bautista": "1303",
    "Luterana": "1304",
    "Metodista": "1305",
    "Presbiteriana": "1306",
    "Otras protestantes": "1307",
    "Amistad Cristiana": "1311",
    "Asambleas de Dios": "1312",
    "Iglesia Apostólica de la Fe en Cristo Jesús": "1313",
    "Iglesia de Dios": "1314",
    "Iglesia de Dios de la Profecía": "1315",
    "Iglesia de Dios en México del Evangelio Completo": "1316",
    "Príncipe de Paz": "1317",
    "Otras asociaciones pentecostales": "1318",
    "Iglesia Cristiana Interdenominacional": "1321",
    "Iglesia del Dios Vivo, Columna y Apoyo de la Verdad, la Luz del Mundo": "1322",
    "Iglesia de Cristo": "1323",
    "Iglesia del Nazareno": "1324",
    "Movimientos Sincréticos Judaicos Neoisraelitas": "1325",
    "Otras cristianas evangélicas": "1326",
    "Adventista del Séptimo Día": "1331",
    "Iglesia de Jesucristo de los Santos de los Últimos Días (Mormón)": "1332",
    "Testigo de Jehová": "1333",
    "Cristiana": "1341",
    "Evangélica": "1342",
    "Pentecostal": "1343",
    "Protestante": "1344",
    "Judía": "2101",
    "Islámica": "2201",
    "Budista": "2301",
    "Hinduista": "2302",
    "Otras de origen oriental": "2303",
    "New Age y Escuelas esotéricas": "2401",
    "Raíces étnicas": "2501",
    "Raíces afro": "2601",
    "Espiritualista": "2701",
    "Cultos populares": "2801",
    "Otros movimientos religiosos": "2901",
    "Ninguna religión": "3101",
    "Ateos": "3102",
    "Agnósticos": "3103",
    "Sin adscripción religiosa (creyente)": "3104",
    "Religión no especificada": "9999"}
    religion = st.selectbox('¿Cuál es la religión que profesa?',
                        options=rel_options)

    # Discapacidad
    disability = st.selectbox('¿En su vida diaria tiene alguna discapacidad?', options=closed_options1)
    dis_options = {
        "No tiene dificultad": "1",
        "Lo hace con poca dificultad": "2",
        "Lo hace con mucha dificultad": "3",
        "No puede hacerlo": "4",
        "Se desconoce el grado de la discapacidad": "8",
        "No especificado": "9"}
    dis_mental_options = {
    "Si": "6",
    "No": "5",
    "No especificado": "9"}
    if disability == 'Si':
        # Dificultad para ver
        dis_ver = st.selectbox('¿Tiene dificultad para ver, aun usando lentes?', options=dis_options)

        # Dificultad para oír
        dis_oir = st.selectbox('¿Tiene dificultad para oír, aun usando aparato auditivo?', options=dis_options)

        # Dificultad para caminar
        dis_caminar = st.selectbox('¿Tiene dificultad para caminar, subir o bajar?', options=dis_options)

        # Dificultad para recordar o concentrarse
        dis_recordar = st.selectbox('¿Tiene dificultad para recordar o concentrarse?', options=dis_options)

        # Dificultad para bañarse, vestirse o comer
        dis_banarse = st.selectbox('¿Tiene dificultad para bañarse, vestirse o comer?', options=dis_options)

        # Dificultad para hablar o comunicarse
        dis_hablar = st.selectbox('¿Tiene dificultad para hablar o comunicarse (por ejemplo: entender o ser entendido por otros)?',
                                options=dis_options)

        # Problema o condición mental
        #dis_mental_options = ['No', 'Sí', 'No especificado']
        dis_mental = st.selectbox('¿Tiene algún problema o condición mental (Autismo, síndrome de Down, esquizofrenia, etcétera)',
                                options=dis_mental_options)

    if disability == 'No':
        dis_ver="No tiene dificultad"
        dis_oir="No tiene dificultad"
        dis_caminar="No tiene dificultad"
        dis_recordar="No tiene dificultad"
        dis_banarse="No tiene dificultad"
        dis_hablar="No tiene dificultad"
        dis_mental="No"
    if disability == 'No especificado':
        dis_ver="No especificado"
        dis_oir="No especificado"
        dis_caminar="No especificado"
        dis_recordar="No especificado"
        dis_banarse="No especificado"
        dis_hablar="No especificado"
        dis_mental="No especificado"

    lengua_indigena=st.selectbox('¿Habla algún dialecto o lengua indígena?', options=closed_options1)

    # Dialecto o lengua indígena habla
    dialecto_options = {
    "Kickapoo": "0101",
    "Pápago": "0201",
    "Pima": "0202",
    "Tepehuano del norte": "0203",
    "Tepehuano del sur": "0204",
    "Tarahumara": "0205",
    "Guarijío": "0206",
    "Yaqui": "0207",
    "Mayo": "0208",
    "Cora": "0209",
    "Huichol": "0210",
    "Náhuatl": "0211",
    "Paipai": "0301",
    "Cucapá": "0303",
    "Kumiai": "0304",
    "Kiliwa": "0305",
    "Seri": "0401",
    "Otomí": "0501",
    "Mazahua": "0502",
    "Matlatzinca": "0503",
    "Tlahuica": "0504",
    "Pame": "0505",
    "Chichimeco Jonaz": "0506",
    "Chinanteco": "0507",
    "Tlapaneco": "0508",
    "Mazateco": "0509",
    "Ixcateco": "0510",
    "Chocholteco": "0511",
    "Popoluca": "0512",
    "Zapoteco": "0513",
    "Chatino": "0514",
    "Amuzgo": "0515",
    "Mixteco": "0516",
    "Cuicateco": "0517",
    "Triqui": "0518",
    "Huasteco": "0601",
    "Maya": "0602",
    "Lacandón": "0603",
    "Ch'ol": "0604",
    "Chontal de Tabasco": "0605",
    "Tseltal": "0606",
    "Tsotsil": "0607",
    "Q’anjob’al": "0608",
    "Akateko": "0609",
    "Jakalteko": "0610",
    "Qato'k": "0611",
    "Chuj": "0612",
    "Tojolabal": "0613",
    "Q’eqchi’": "0614",
    "K’iche’": "0615",
    "Kaqchikel": "0616",
    "Teko": "0617",
    "Mam": "0618",
    "Awakateko": "0619",
    "Ixil": "0620",
    "Totonaco": "0701",
    "Tepehua": "0702",
    "Tarasco": "0801",
    "Mixe": "0901",
    "Sayulteco": "0902",
    "Oluteco": "0903",
    "Texistepequeño": "0904",
    "Ayapaneco": "0905",
    "Popoluca de la Sierra": "0906",
    "Zoque": "0907",
    "Chontal de Oaxaca": "1001",
    "Huave": "1101",
    "Otras lenguas indígenas de América": "8000",
    "No especificado": "9000",
    "Chontal insuficientemente especificado": "9010",
    "Tepehuano insuficientemente especificado":"9020",
    "Popoluca insuficientemente especificado":"9030",
    "Blanco por pase":np.NaN}

    if lengua_indigena == 'Si':
        # Dialecto o lengua indígena habla
        dialecto = st.selectbox("¿Qué dialecto o lengua indígena habla?", options=dialecto_options)
        # ¿Habla también español?
        indigena_espanol = st.selectbox('¿Habla también español?', options=closed_options1)
        # ¿Entiende algún dialecto o lengua indígena?
        indigena_entiende = st.selectbox('¿Entiende algún dialecto o lengua indígena?', options=closed_options1)
    if lengua_indigena == 'No':
        dialecto='Blanco por pase'
        indigena_espanol='Blanco por pase'
        indigena_entiende='Blanco por pase'
        
    # De acuerdo con su cultura, ¿se considera indígena?
    considera_indigena = st.selectbox('De acuerdo con su cultura, ¿se considera indígena?', options=closed_options1)

    # ¿Sabe leer y escribir un recado?
    sabe_leer_escribir_recado = st.selectbox('¿Sabe leer y escribir un recado?', options=closed_options1)
    RESIDENCIA_5_ANIOS =  st.selectbox('¿Hace 5 años residía en el mismo lugar?', options=closed_options1)

    motivo_cambio_residencia_options = {
        "Buscar trabajo": "0101",
        "Cambio u oferta de trabajo": "0102",
        "Despido o conclusión de trabajo": "0103",
        "Distancia al trabajo": "0104",
        "Jubilación o pensión": "0105",
        "Otros motivos laborales": "0109",
        "Costo de la vivienda (compra o renta)": "0201",
        "Situación económica": "0209",
        "Reunirse con la familia": "0301",
        "Matrimonio o unión de algún familiar": "0302",
        "Divorcio o separación de algún familiar": "0303",
        "Falleció o nació algún familiar": "0304",
        "Cuidar a algún familiar": "0305",
        "Situación laboral de algún familiar": "0306",
        "Situación escolar de algún familiar": "0307",
        "Otros motivos familiares": "0309",
        "Se casó o unió": "0401",
        "Divorcio o separación": "0402",
        "Cuidados de salud": "0403",
        "Motivos de edad": "0404",
        "Mejorar calidad de vida": "0405",
        "Independizarse": "0406",
        "Otros motivos personales": "0409",
        "Estudiar": "0501",
        "Término de estudios": "0502",
        "Distancia a la escuela": "0503",
        "Otros motivos educativos": "0509",
        "Inseguridad delictiva o violencia": "0601",
        "Violencia intrafamiliar": "0602",
        "Motivos políticos y de gobierno": "0603",
        "Motivos de servicios asistenciales": "0604",
        "Otros motivos sociales, ambientales o de servicios": "0609",
        "Desastres naturales": "0701",
        "Otros desastres": "0709",
        "Lo deportaron (regresaron)": "0801",
        "Motivos legales y administrativos": "0809",
        "Adquisición, venta o construcción de vivienda": "0901",
        "Mejorar condiciones de vivienda (no económica)": "0902",
        "Término de contrato y otros motivos de renta": "0903",
        "Ubicación de la vivienda": "0905",
        "Cambio de domicilio sin causa específica": "0906",
        "Otras situaciones de la vivienda": "0909",
        "Evangelizar y motivos misioneros": "1001",
        "Persecución religiosa": "1002",
        "Otros motivos religiosos": "1009",
        "Causa de migración no especificada": "9999",
        'Blanco por pase':np.NaN}
    if RESIDENCIA_5_ANIOS=='No':
        motivo_cambio_residencia = st.selectbox('¿Por qué dejó de vivir en donde residía antes?',
                                                options=motivo_cambio_residencia_options)

    if RESIDENCIA_5_ANIOS=='Si':
        motivo_cambio_residencia='Blanco por pase'

    edo_civil_options = {
    "Vive con su pareja en unión libre": "1",
    "Está separada(o)": "2",
    "Está divorciada(o)": "3",
    "Es viuda(o)": "4",
    "Está casada(o) sólo por el civil": "5",
    "Está casada(o) sólo religiosamente": "6",
    "Está casada(o) civil y religiosamente": "7",
    "Está soltera(o)": "8",
    "No especificado": "9"}
    edo_civil = st.selectbox('Actualmente',options=edo_civil_options)

    actividad_semana_pasada_options = {
    "Se declara que busca trabajo y en la verificación se rescata que trabaja": "13",
    "Trabajó": "10",
    "Se declara que es jubilado o pensionado y en la verificación se rescata que trabaja": "14",
    "Se declara que es estudiante y en la verificación se rescata que trabaja": "15",
    "Se dedica a los quehaceres del hogar y en la verificación se rescata que trabaja": "16",
    "Se declara que tiene alguna limitación física o mental permanente que le impide trabajar y en la verificación se rescata que trabaja": "17",
    "Se declara en otra situación de actividad y en la verificación se rescata que trabaja": "18",
    "No se tiene información en condición de actividad y en la verificación se rescata que trabaja": "19",
    "Tenía trabajo pero no trabajó": "20",
    "Buscó trabajo": "30",
    "Es pensionada(o) o jubilada(o)": "40",
    "Es estudiante": "50",
    "Se dedica a los quehaceres del hogar": "60",
    "Está incapacitado permanentemente para trabajar": "70",
    "No trabaja": "80",
    "No especificado": "99"}

    actividad_semana_pasada = st.selectbox('La semana pasada usted:', options=actividad_semana_pasada_options)
    ocupacion_options = {
        "Funcionarios, directores y jefes": "1",
        "Profesionistas y técnicos": "2",
        "Trabajadores auxiliares en actividades administrativas": "3",
        "Comerciantes, empleados en ventas y agentes de ventas": "4",
        "Trabajadores en servicios personales y de vigilancia": "5",
        "Trabajadores en actividades agrícolas, ganaderas, forestales, caza y pesca": "6",
        "Trabajadores artesanales, en la construcción y otros oficios": "7",
        "Operadores de maquinaria industrial, ensambladores, choferes y conductores de transporte": "8",
        "Trabajadores en actividades elementales y de apoyo": "9",
        "No especificado": "999",
        "Blanco por pase": np.NaN}
    trabajo_options = {
        "empleada(o) u obrera(o)?": "1",
        "jornalera(o) o peón(a)?": "2",
        "ayudante con pago?": "3",
        "patrón(a) o empleador(a)? (Tiene trabajadores por un sueldo)": "4",
        "trabajador(a) por cuenta propia? (No tiene trabajadores por un sueldo)": "5",
        "trabajador(a) sin pago?": "6",
        "No especificado": "9",
        "Blanco por pase": np.NaN}
    options_sino = {
        "Si": "1",
        "No": "3",
        "No especificado": "9",
        "Blanco por pase": np.NaN}
    actividad_economica_options =  {
        "Agricultura, cría y explotación de animales, aprovechamiento forestal, pesca y caza": "1110",
        "Minería": "21",
        "Generación, transmisión, distribución y comercialización de energía eléctrica, suministro de agua y de gas natural por ductos al consumidor final": "22",
        "Construcción": "23",
        "Industrias manufactureras": "31",
        "Comercio al por mayor": "43",
        "Comercio al por menor": "46",
        "Transportes, correos y almacenamiento": "48",
        "Información en medios masivos": "51",
        "Servicios financieros y de seguros": "52",
        "Servicios inmobiliarios y de alquiler de bienes muebles e intangibles": "53",
        "Servicios profesionales, científicos y técnicos": "54",
        "Corporativos": "55",
        "Servicios de apoyo a los negocios y manejo de residuos, y servicios de remediación": "56",
        "Servicios educativos": "61",
        "Servicios de salud y de asistencia social": "62",
        "Servicios de esparcimiento, culturales y deportivos, y otros servicios recreativos": "71",
        "Servicios de alojamiento temporal y de preparación de alimentos y bebidas": "72",
        "Otros servicios excepto actividades gubernamentales": "81",
        "Actividades legislativas, gubernamentales, de impartición de justicia y de organismos internacionales y extraterritoriales": "93",
        "Descripciones insuficientemente especificadas general de sector de actividad": "99",
        "No especificado": "9999",
        "Blanco por pase": np.NaN}
    tiempo_traslado_options = {
        "Hasta 15 minutos": "1",
        "16 a 30 minutos": "2",
        "31 minutos a 1 hora": "3",
        "Más de 1 hora y hasta 2 horas": "4",
        "Más de 2 horas": "5",
        "No es posible determinarlo": "6",
        "No se traslada": "7",
        "No especificado": "9",
        "Blanco por pase": np.NaN}
    medio_transporte_options = {
        "Caminando": "01",
        "Bicicleta": "02",
        "Metro, tren ligero, tren suburbano": "03",
        "Trolebús": "04",
        "Metrobús (autobús en carril confinado)": "05",
        "Camión, autobús, combi, colectivo": "06",
        "Transporte de personal": "07",
        "Taxi (sitio, calle, otro)": "08",
        "Taxi (App Internet)": "09",
        "Motocicleta o motoneta": "10",
        "Automóvil o camioneta": "11",
        "Otro": "12",
        "No especificado": "99",
        "Blanco por pase":np.NaN}
    if actividad_semana_pasada=="Trabajó":
        ocupacion = st.selectbox('¿Cuál fue su ocupación la semana pasada? (Según Clasificador de Ocupaciones)', 
                                options=ocupacion_options)
        # ¿En ese trabajo fue?
        en_ese_trabajo = st.selectbox('¿En ese trabajo fue?', options=trabajo_options)

        # ¿Tiene por su trabajo aguinaldo?
        tiene_aguinaldo = st.selectbox('¿Tiene por su trabajo aguinaldo?', options=options_sino)

        vacaciones = st.selectbox('Vacaciones con goce de sueldo?', options=options_sino)

        # Servicio médico (IMSS, ISSSTE u otro)?
        servicio_medico = st.selectbox('Servicio médico (IMSS, ISSSTE u otro)?', options=options_sino)

        # Reparto de utilidades?
        reparto_utilidades = st.selectbox('Reparto de utilidades?', options=options_sino)

        # Licencia o incapacidad con goce de sueldo?
        licencia_incapacidad = st.selectbox('Licencia o incapacidad con goce de sueldo?', options=options_sino)

        # AFORE o SAR (ahorro para el retiro)?
        afore_sar = st.selectbox('AFORE o SAR (ahorro para el retiro)?', options=options_sino)

        # Crédito para la vivienda? por pase"
        credito_vivienda = st.selectbox('Crédito para la vivienda?', options=options_sino)
        # ¿Cuánto gana por ese trabajo?
        ganancias = st.number_input('¿Cuánto gana por ese trabajo?', min_value=0, max_value=999998)

        # ¿Cuántas horas trabajó la semana pasada?
        horas_trabajadas = st.number_input('¿Cuántas horas trabajó la semana pasada?', min_value=0, max_value=140)

        # ¿A qué se dedica el negocio, empresa o lugar donde trabajó?
        actividad_economica = st.selectbox('¿A qué se dedica el negocio, empresa o lugar donde trabajó?', options=actividad_economica_options)

        # ¿Cuánto tiempo hace de aquí a su trabajo?
        tiempo_traslado = st.selectbox('¿Cuánto tiempo hace de aquí a su trabajo?', options=tiempo_traslado_options)

        medio_transporte = st.selectbox('¿Cómo acostumbra ir de aquí a su trabajo?', options=medio_transporte_options)

    if actividad_semana_pasada!="Trabajó":
        ocupacion='Blanco por pase'
        en_ese_trabajo="Blanco por pase"
        tiene_aguinaldo="Blanco por pase"
        vacaciones="Blanco por pase"
        servicio_medico="Blanco por pase"
        reparto_utilidades="Blanco por pase"
        licencia_incapacidad="Blanco por pase"
        afore_sar="Blanco por pase"
        credito_vivienda="Blanco por pase"
        ganancias=0
        horas_trabajadas=0
        actividad_economica="Blanco por pase"
        tiempo_traslado="Blanco por pase"
        medio_transporte="Blanco por pase"

    hijos_vivos = st.number_input("En total, ¿cuántas hijas e hijos que nacieron vivos ha tenido?", min_value=0, max_value=25, value=0)

    hijos_muertos = st.number_input("De las hijas e hijos que nacieron vivos, ¿cuántos han muerto?", min_value=0, max_value=25, value=0)

    hijos_viven = st.number_input("¿Cuántas de las hijas e hijos viven actualmente?", min_value=0, max_value=25, value=0)

    ultimo_hijo_vive = st.selectbox("Esta última hija o hijo de , ¿vive actualmente?", options=options_sino)

    ultimo_hijo_lugar_options = {
    "En esta vivienda": "01",
    "En otra vivienda": "96",
    "No especificado": "99",
    "Blanco por pase": np.NaN}
    ultimo_hijo_lugar = st.selectbox("¿Dónde vive esta última hija o hijo de (NOMBRE)?", options=ultimo_hijo_lugar_options)

    tamanio_localidad_options = {
    "Menos de 2,500 habitantes": "1",
    "De 2,500 a 14,999 habitantes": "2",
    "De 15,000 a 49,999 habitantes": "3",
    "De 50,000 a 99,999 habitantes": "4",
    "100,000 y más habitantes": "5"}
    tamanio_localidad = st.selectbox("Tamaño de localidad:", options=tamanio_localidad_options)
        
    # Now, you would typically create a DataFrame out of these inputs and pass it to the prediction function
    df = pd.DataFrame()
    columns=['MUN', 'NUMPER', 'SEXO', 'EDAD','ENT_PAIS_NAC', 'NACIONALIDAD',
       'SERSALUD', 'AFRODES', 'REGIS_NAC', 'RELIGION', 'DIS_VER', 'DIS_OIR', 'DIS_CAMINAR', 'DIS_RECORDAR',
       'DIS_BANARSE', 'DIS_HABLAR', 'DIS_MENTAL', 'HLENGUA', 'QDIALECT_INALI', 'HESPANOL', 'ELENGUA',
       'PERTE_INDIGENA', 'ALFABET', 'MIGRANTE', 'CAUSA_MIG_V',
       'SITUA_CONYUGAL', 'CONACT', 'OCUPACION', 'SITTRA',
       'AGUINALDO', 'VACACIONES', 'SERVICIO_MEDICO', 'UTILIDADES',
       'INCAP_SUELDO', 'SAR_AFORE', 'CREDITO_VIVIENDA', 'INGTRMEN', 'HORTRA',
       'ACTIVIDADES_C','TIE_TRASLADO_TRAB','MED_TRASLADO_TRAB1',
       'HIJOS_NAC_VIVOS', 'HIJOS_FALLECIDOS', 'HIJOS_SOBREVIV', 'SOBREVIVENCIA', 'IDENT_HIJO',  'TAMLOC']

    #st.write(mun_options[municipio])
    values = [mun_options[municipio], 1, sex_options[sexo], edad,  edo_options[estadoNacimiento], closed_options1[nacionalidadMexicana],
            sal_options[atencionSalud], closed_options1[afromexicano], acta_options[actaNacimiento], rel_options[religion], dis_options[dis_ver],
            dis_options[dis_oir], dis_options[dis_caminar], dis_options[dis_recordar], dis_options[dis_banarse], dis_options[dis_hablar],
            dis_mental_options[dis_mental], closed_options1[lengua_indigena], dialecto_options[dialecto], closed_options1[indigena_espanol], 
            closed_options1[indigena_entiende], closed_options1[considera_indigena], closed_options1[sabe_leer_escribir_recado], closed_options1[RESIDENCIA_5_ANIOS],
            motivo_cambio_residencia_options[motivo_cambio_residencia], edo_civil_options[edo_civil], actividad_semana_pasada_options[actividad_semana_pasada],
            ocupacion_options[ocupacion], trabajo_options[en_ese_trabajo], options_sino[tiene_aguinaldo], options_sino[vacaciones], options_sino[servicio_medico],
            options_sino[reparto_utilidades], options_sino[licencia_incapacidad], options_sino[afore_sar], options_sino[credito_vivienda],
            ganancias, horas_trabajadas, actividad_economica_options[actividad_economica], tiempo_traslado_options[tiempo_traslado],
            medio_transporte_options[medio_transporte], hijos_vivos, hijos_muertos, hijos_viven, options_sino[ultimo_hijo_vive], 
            ultimo_hijo_lugar_options[ultimo_hijo_lugar], tamanio_localidad_options[tamanio_localidad]
            ]
    # result = prediction(df)

    # Submit button
    submit_button = st.button('Enviar')

    if submit_button:
        # Perform some action e.g., prediction using the collected inputs
        st.write('Cuestionario enviado!')

    if submit_button:
        df = pd.DataFrame(data=[values],
                          columns=columns)
        df = df.astype(np.float64)
        prediction_result = prediction(df)
        st.success(f'El resultado es: {prediction_result}')

if __name__ == '__main__':
    main()
