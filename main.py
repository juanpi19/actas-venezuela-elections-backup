import requests
import random
import csv
from concurrent.futures import ThreadPoolExecutor, as_completed
import warnings
warnings.filterwarnings("ignore")

####################################################
# APIs endpoints
# https://gdp.theempire.tech/api/data?cdi=v25160168 
# https://elecciones2024ve.s3.amazonaws.com/AG8A001761_819592_2024-07-29-0001.jpg
####################################################

venezolano_data_dict = {'nombre_primer': [], 
                        'apellido_primer': [], 
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

def fetch_data(cedula):
    url = cedula_api_endpoint + str(cedula)
    try:
        response = requests.get(url, verify=False)
        if response.status_code == 200:
            print(f"Cedula {cedula} found")
            return response.json()
        else:
            print(f"Failed to fetch data for cedula {cedula}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error fetching data for cedula {cedula}: {str(e)}")
    return None

def process_data(datos):
    if datos:
        try:
            if datos['acta']['DO_DS_SERIAL'] not in venezolano_data_dict['acta_jpg']:
                venezolano_data_dict['nombre_primer'].append(datos['Person']['RE_DS_FIRST_NAME'])
                venezolano_data_dict['apellido_primer'].append(datos['Person']['RE_DS_FIRST_LASTNAME'])
                venezolano_data_dict['cedula'].append(datos['Person']['RE_CO_FULLID'])
                venezolano_data_dict['estado'].append(datos['Person']['ST_DS_STATE'])
                venezolano_data_dict['municipio'].append(datos['Person']['MU_DS_MUN'])
                venezolano_data_dict['parroquia'].append(datos['Person']['PA_DS_PAR'])
                venezolano_data_dict['centro_votacion'].append(datos['Person']['PC_DS_CENTER'])
                venezolano_data_dict['acta_jpg'].append(foto_acta_api_endpoint + f"{datos['acta']['DO_DS_NAME']}") # DO_DS_NAME
                print(f"Data added: Cedula {datos['Person']['RE_CO_FULLID']}, Acta {datos['acta']['DO_DS_NAME']}")
            else:
                print("Centro de votacion ya contado")
        except KeyError as e:
            # print(f"KeyError while processing data: {str(e)}")
            print(f"Data structure: {datos}")
    else:
        print("No data to process")

def save_to_csv(data_dict, filename='venezolano_data.csv'):
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data_dict.keys())  # Write header
            writer.writerows(zip(*data_dict.values()))  # Write data
        print(f"Data successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving data to CSV: {str(e)}")

def main():
    cedulas = [randomize_cedula_number() for _ in range(1000)]
    #print(f"Generated cedulas: {cedulas}")

    with ThreadPoolExecutor(max_workers=20) as executor:
        n = 0
        print(n)
        future_to_cedula = {executor.submit(fetch_data, cedula): cedula for cedula in cedulas}
        for future in as_completed(future_to_cedula):
            cedula = future_to_cedula[future]
            try:
                datos = future.result()
                process_data(datos)
            except Exception as e:
                print(f"Error processing cedula {cedula}: {str(e)}")
            print(n)
            n+=1

    print("Final dictionary content:")
    for key, value in venezolano_data_dict.items():
        print(f"{key}: {value}")

    save_to_csv(venezolano_data_dict)

if __name__ == "__main__":
    main()







