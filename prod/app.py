import streamlit as st
import pandas as pd
import numpy as np
import pickle

file_in = open('modelo_6v.pkl')
model = pickle.load(file_in)

def prediction(df):
    result =  model.predict(df)
    if result[0] == 0:
          prediction = "NADA"
    elif result[0] == 1:
        prediction = "PRIMARIA"
    elif result[0] == 2:
        prediction = "SECUNDARIA"
    elif result[0] == 3:
        prediction = "PREPARATORIA"
    elif result[0] == 4:
        prediction = "UNIVERSIDAD"
    else:
        prediction = "POSGRADO"
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

    municipio = st.selectbox('Municipio o Demarcación territorial:',
                            options=['Azcapotzalco', 'Coyoacán', 'Cuajimalpa de Morelos', 'Gustavo A. Madero',
                                     'Iztacalco', 'Iztapalapa', 'La Magdalena Contreras', 'Milpa Alta',
                                     'Álvaro Obregón', 'Tláhuac', 'Tlalpan', 'Xochimilco', 'Benito Juárez',
                                     'Cuauhtémoc', 'Miguel Hidalgo', 'Venustiano Carranza',
                                     'Demarcación territorial no especificada'])

    sexo = st.selectbox('Sexo:', options=['Hombre', 'Mujer'])

    edad = st.number_input('Edad:', min_value=0, max_value=130)

    # New questions
    estadoNacimiento = st.selectbox('¿En qué estado de la República Mexicana nació?',
                                    options=['Aguascalientes', 'Baja California', 'Baja California Sur', 'Campeche',
                                             'Coahuila', 'Colima', 'Chiapas', 'Chihuahua', 'Ciudad de México', 'Durango',
                                             'Guanajuato', 'Guerrero', 'Hidalgo', 'Jalisco', 'México', 'Michoacán',
                                             'Morelos', 'Nayarit', 'Nuevo León', 'Oaxaca', 'Puebla', 'Querétaro',
                                             'Quintana Roo', 'San Luis Potosí', 'Sinaloa', 'Sonora', 'Tabasco',
                                             'Tamaulipas', 'Tlaxcala', 'Veracruz', 'Yucatán', 'Zacatecas'])

    nacionalidadMexicana = st.selectbox('¿Tiene nacionalidad mexicana?',
                                        options=['Sí', 'No', 'No especificado'])

    atencionSalud = st.selectbox('Cuando tiene problemas de salud, ¿en dónde se atiende?',
                                  options=['Seguro Social (IMSS)', 'ISSSTE', 'ISSSTE estatal', 'PEMEX, Defensa o Marina',
                                           'Centro de Salud u Hospital de la SSA, Seguro Popular o Instituto de Salud para el Bienestar',
                                           'IMSS-PROSPERA o IMSS-BIENESTAR', 'Consultorio, clínica u hospital privado',
                                           'Consultorio de farmacia', 'Otro lugar', 'No se atiende', 'No especificado'])

    afromexicano = st.selectbox('Por sus antepasados y de acuerdo con sus costumbres y tradiciones, ¿se considera afromexicano(a), negro(a) o afrodescendiente?',
                        options=['Sí', 'No', 'No especificado'])

    actaNacimiento = st.selectbox('¿Tiene acta de nacimiento o está inscrita(o) en el registro civil de:',
                                  options=['la República Mexicana', 'otro país', 'Entonces, ¿no tiene registro de nacimiento?', 'No especificado'])

    religion = st.selectbox('¿Cuál es la religión que profesa?',
                        options=['Católica', 'Católico ortodoxo', 'Anabautista/Menonita', 'Anglicana/Episcopal', 'Bautista',
                                 'Luterana', 'Metodista', 'Presbiteriana', 'Otras protestantes', 'Amistad Cristiana', 
                                 'Asambleas de Dios', 'Iglesia Apostólica de la Fe en Cristo Jesús', 'Iglesia de Dios', 
                                 'Iglesia de Dios de la Profecía', 'Iglesia de Dios en México del Evangelio Completo',
                                 'Príncipe de Paz', 'Otras asociaciones pentecostales', 'Iglesia Cristiana Interdenominacional', 
                                 'Iglesia del Dios Vivo, Columna y Apoyo de la Verdad, la Luz del Mundo', 'Iglesia de Cristo', 
                                 'Iglesia del Nazareno', 'Movimientos Sincréticos Judaicos Neoisraelitas', 'Otras cristianas evangélicas',
                                 'Adventista del Séptimo Día', 'Iglesia de Jesucristo de los Santos de los Últimos Días (Mormón)', 
                                 'Testigo de Jehová', 'Cristiana', 'Evangélica', 'Pentecostal', 'Protestante', 'Judía', 'Islámica', 
                                 'Budista', 'Hinduista', 'Otras de origen oriental', 'New Age y Escuelas esotéricas', 'Raíces étnicas',
                                 'Raíces afro', 'Espiritualista', 'Cultos populares', 'Otros movimientos religiosos', 'Ninguna religión', 
                                 'Ateos', 'Agnósticos', 'Sin adscripción religiosa (creyente)', 'Religión no especificada'])

        # Discapacidad
    disability_options = ['Si', 'No', 'No especificado']
    disability = st.selectbox('¿En su vida diaria tiene alguna discapacidad?', options=disability_options)

    if disability == 'Si':
        # Dificultad para ver
        dis_options = ['No tiene dificultad', 'Lo hace con poca dificultad', 'Lo hace con mucha dificultad',
                        'No puede hacerlo', 'Se desconoce el grado de la discapacidad', 'No especificado']
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
        dis_mental_options = ['No', 'Sí', 'No especificado']
        dis_mental = st.selectbox('¿Tiene algún problema o condición mental (Autismo, síndrome de Down, esquizofrenia, etcétera)',
                                options=dis_mental_options)

    lengua_indigena=st.selectbox('¿Habla algún dialecto o lengua indígena?', options=['Si', 'No', 'No especificado'])

    # Dialecto o lengua indígena habla
    dialecto_options = {
    "0101": "Kickapoo",
    "0201": "Pápago",
    "0202": "Pima",
    "0203": "Tepehuano del norte",
    "0204": "Tepehuano del sur",
    "0205": "Tarahumara",
    "0206": "Guarijío",
    "0207": "Yaqui",
    "0208": "Mayo",
    "0209": "Cora",
    "0210": "Huichol",
    "0211": "Náhuatl",
    "0301": "Paipai",
    "0303": "Cucapá",
    "0304": "Kumiai",
    "0305": "Kiliwa",
    "0401": "Seri",
    "0501": "Otomí",
    "0502": "Mazahua",
    "0503": "Matlatzinca",
    "0504": "Tlahuica",
    "0505": "Pame",
    "0506": "Chichimeco Jonaz",
    "0507": "Chinanteco",
    "0508": "Tlapaneco",
    "0509": "Mazateco",
    "0510": "Ixcateco",
    "0511": "Chocholteco",
    "0512": "Popoluca",
    "0513": "Zapoteco",
    "0514": "Chatino",
    "0515": "Amuzgo",
    "0516": "Mixteco",
    "0517": "Cuicateco",
    "0518": "Triqui",
    "0601": "Huasteco",
    "0602": "Maya",
    "0603": "Lacandón",
    "0604": "Ch'ol",
    "0605": "Chontal de Tabasco",
    "0606": "Tseltal",
    "0607": "Tsotsil",
    "0608": "Q’anjob’al",
    "0609": "Akateko",
    "0610": "Jakalteko",
    "0611": "Qato'k",
    "0612": "Chuj",
    "0613": "Tojolabal",
    "0614": "Q’eqchi’",
    "0615": "K’iche’",
    "0616": "Kaqchikel",
    "0617": "Teko",
    "0618": "Mam",
    "0619": "Awakateko",
    "0620": "Ixil",
    "0701": "Totonaco",
    "0702": "Tepehua",
    "0801": "Tarasco",
    "0901": "Mixe",
    "0902": "Sayulteco",
    "0903": "Oluteco",
    "0904": "Texistepequeño",
    "0905": "Ayapaneco",
    "0906": "Popoluca de la Sierra",
    "0907": "Zoque",
    "1001": "Chontal de Oaxaca",
    "1101": "Huave",
    "8000": "Otras lenguas indígenas de América",
    "9000": "No especificado",
    "9010": 'Chontal insuficientemente especificado',
    "9020": "Tepehuano insuficientemente especificado",
    "9030": "Popoluca insuficientemente especificado"}

    if lengua_indigena == 'Si':
        # Dialecto o lengua indígena habla
        dialecto = st.selectbox("¿Qué dialecto o lengua indígena habla?", options=dialecto_options)
        # ¿Habla también español?
        indigena_espanol_options = {
            "1": "Sí",
            "3": "No",
            "9": "No especificado"
        }
        indigena_espanol = st.selectbox('¿Habla también español?', options=indigena_espanol_options)

        # ¿Entiende algún dialecto o lengua indígena?
        indigena_entiende_options = {
            "5": "Sí",
            "7": "No",
            "9": "No especificado"
        }
        indigena_entiende = st.selectbox('¿Entiende algún dialecto o lengua indígena?', options=indigena_entiende_options)

    # Now, you would typically create a DataFrame out of these inputs and pass it to the prediction function
    # df = pd.DataFrame([municipio, sexo, edad, estadoNacimiento, nacionalidadMexicana, atencionSalud, afromexicano, actaNacimiento])
    # result = prediction(df)

    # Submit button
    if st.button('Enviar'):
        # Perform some action e.g., prediction using the collected inputs
        st.write('Button pressed!')



    submit_button = st.button('Enviar')

    if submit_button:
        df = pd.DataFrame(data=[[municipio, sexo, edad]],
                          columns=['municipio', 'sexo', 'edad'])

        prediction_result = prediction(df)
        st.success(f'El resultado es: {prediction_result}')

if __name__ == '__main__':
    main()
