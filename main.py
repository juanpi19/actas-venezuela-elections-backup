import requests
import random

####################################################
# APIs endpoints
# https://gdp.theempire.tech/api/data?cdi=v25160168 
# https://elecciones2024ve.s3.amazonaws.com/AG8A001761_819592_2024-07-29-0001.jpg
####################################################


# Dictionaries
venezolano_data_dict = {'nombre': [], 
                        'apellido': [], 
                        'cedula': [],
                        'estado': [],
                        'municipio': [],
                        'parroquia': [],
                        'centro_votacion': [],
                        'acta_jpg': []}


cedula_api_endpoint = "https://gdp.theempire.tech/api/data?cdi=v"
foto_acta_api_endpoint = "https://elecciones2024ve.s3.amazonaws.com/"

def randomize_cedula_number():
    return random.randint(20000, 30000000)


# Centro De Votacion informacion
# for _ in range(100):
#     response = requests.get(cedula_api_endpoint + f"{randomize_cedula_number()}")

#     # Guardando Data
#     venezolano_data_dict['nombre'] = 
#     venezolano_data_dict['apellido'] =
#     venezolano_data_dict['cedula'] = 
#     venezolano_data_dict['estado'] = 
#     venezolano_data_dict['municipio'] = 
#     venezolano_data_dict['parroquia'] = 
#     venezolano_data_dict['centro_votacion'] = 
#     venezolano_data_dict['acta_jpg'] = 




# EXAMPLE

dict_ = {
        "Person": {
            "RE_CO_FULLID": "V25160168",
            "RE_DS_FIRST_NAME": "JOSE DOMINGO",
            "RE_DS_SECOND_NAME": "MARIANO",
            "RE_DS_FIRST_LASTNAME": "HERRERA",
            "RE_DS_SECOND_LASTNAME": "SOSA",
            "RE_CD_GENDER": "M",
            "RE_DT_BIRTHDATE": "1993-05-17T00:00:00.000Z",
            "RE_CD_STATE": "16",
            "RE_DS_CNE_ID": "160101004",
            "RE_NU_TOMO": None,
            "IT_CD_ROW": 8,
            "IT_CD_PAGE": 28,
            "TB_DS_TABLE": 2,
            "TB_NU_COUNT": 704,
            "TB_DS_TERM_MIN": "48",
            "TB_DS_TERM_MAX": "99",
            "TB_DS_CODE_QR": None,
            "RE_DS_TERM_ID": 68,
            "ST_DS_STATE": "EDO. PORTUGUESA",
            "MU_DS_MUN": "MP. ARAURE",
            "PA_DS_PAR": "CM. ARAURE",
            "PC_CO_CNE": "160101004",
            "PC_DS_CENTER": "UNIDAD EDUCATIVA ESTADAL DON JUAN DE JESUS SOTELDO GOITIA",
            "PC_DS_ADDRESS": "BARRIO LIMONCITO DERECHA AVENIDA 35. IZQUIERDA AVENIDA 34. FRENTE CALLE 09 AVENIDA 10 CON CALLE 5 BARRIO LIMONCITO ARAURE CASA",
            "AU_CO_CREATE_USER": "1",
            "AU_CO_DROP_USER": None,
            "AU_CO_MODIFY_USER": "1",
            "AU_DT_CREATE_DATE": "2024-03-10T05:16:53.080Z",
            "AU_DT_DROP_DATE": None,
            "AU_DT_MODIFY_DATE": "2024-06-07T04:10:50.743Z"
        },
        "acta": {
            "DO_CD_DOCUMENT": "58347",
            "DO_DS_NAME": "AG8A001761_819592_2024-07-29-0001.jpg",
            "DO_DS_BUCKET": "elecciones2024ve",
            "DO_CD_SESSION": "77d1b1f7-b733-4534-a1e9-50eba19988b0",
            "DO_CD_TYPE": None,
            "DO_DS_SERIAL": "AG8A001761",
            "DO_BO_BOUND": None,
            "DO_BO_DUPLICATE": None,
            "DO_BO_AUTO_DETECT": None,
            "DO_NU_QUALITY": None,
            "DO_BO_PUBLISH": None,
            "DO_CD_CHANNEL": 0,
            "DO_CD_STATE": "16",
            "DO_CD_MUN": "211",
            "DO_CD_PAR": "695",
            "DO_CD_CENTER": "5503",
            "DO_CO_CNE_CENTER": "160101004",
            "DO_CD_TABLE": "18552",
            "DO_NU_TABLE": "2",
            "DO_CD_PUBLISH": None,
            "DO_CO_STAGE": "TT",
            "DO_DT_A1": "2024-07-29T19:58:16.963Z",
            "DO_DT_P1": None,
            "DO_DT_P2": None,
            "DO_DT_RC": None,
            "AU_DT_TAKE": None,
            "AU_CO_TAKE": None,
            "DO_BO_TOTALIZED": None,
            "DO_CD_SESSION_AUTO": "c4f13686-d924-4242-8f2b-bce7e441a8a0",
            "DO_BO_MASKED": None,
            "DO_DS_RAWDATA": None,
            "DO_BO_MASKED_SESSION": None,
            "AU_CO_CREATE_USER": "2",
            "AU_CO_MODIFY_USER": "1",
            "AU_CO_DROP_USER": None,
            "AU_DT_CREATE_DATE": "2024-07-29T19:54:51.423Z",
            "AU_DT_MODIFY_DATE": "2024-07-29T19:58:16.963Z",
            "AU_DT_DROP_DATE": None
        }
    }


# print(dict_['acta']['DO_DS_NAME'])

# response = requests.get("https://gdp.theempire.tech/api/data?cdi=v25160168", verify=False)
# print(response.get_status)


# import requests

# url = "https://gdp.theempire.tech/api/data?cdi=v25160168"
# response = requests.get(url, verify=False)

# if response.status_code == 200:
#     data = response.json()
#     print(data)
# else:
#     print(f"Failed to retrieve data: {response.status_code}")


import requests
import ssl

url = "https://gdp.theempire.tech/api/data?cdi=v25160168"
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

response = requests.get(url, verify=False)





