import ast
from datetime import datetime
import requests
import re
import os

import time
import timeit

from azure.storage.blob import BlobServiceClient
from azure.cosmos import CosmosClient

def get_access_token():
    url = os.environ["OAUTH_URL"]
    headers = {
        "Content-Type": os.environ["OAUTH_CONTENT_TYPE"],
        "Cookie": os.environ["OAUTH_COOKIE"]
    }

    data = {
        "grant_type": "client_credentials",
        "client_id": os.environ["OAUTH_CLIENT_ID"],
        "scope": os.environ["OAUTH_SCOPE"],
        "client_secret": os.environ["OAUTH_CLIENT_SECRET"]
    }
    try:
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()  # Check for any error in the response

        # Assuming the API returns JSON data
        access_token = response.json().get('access_token')
        return access_token
    except requests.exceptions.RequestException as e:
        #print(f"Error occurred: {e}")
        return None

###########################################################################################
# Data con URL, Path y demás para extracción de datos 
def data_blob():
    # Conexión al contenedor de blobs
    storage_service_client = BlobServiceClient.from_connection_string(os.environ["DATA_BLOB_STORAGE_SERVICE_CLIENT"])

    # Nombre del archivo y ruta en el contenedor
    Container_name = os.environ["DATA_BLOB_CONTAINER_NAME"] 
    data = os.environ["DATA_BLOB_DATA"]

    # Obtener una referencia al blob
    blob_client = storage_service_client.get_blob_client(container=Container_name, blob=data)

    # Descargar el contenido del blob
    infor = blob_client.download_blob().readall()
    infor = infor.decode('UTF-8')

    infor = infor.replace("\n",",")
    split_data = infor.split(",")

    return split_data


URL = os.environ["URL_MAREIGUA"]
KEY = os.environ["KEY_MAREIGUA"]
client = CosmosClient(URL, credential=KEY)
DATABASE_NAME = os.environ["DATABASE_MAREIGUA"]
database = client.get_database_client(DATABASE_NAME)
CONTAINER_NAME = os.environ["CONTAINER_NAME_MAREIGUA"]
container = database.get_container_client(CONTAINER_NAME)

data_cons = data_blob()
 
url = data_cons [0]+data_cons [1]
x_name = data_cons [2]
access_token = get_access_token()
access_token = str ('Bearer '+access_token)

# Cabeceras adicionales que deseas enviar
headers = {'X-RqUID': '123456', 'X-AppId': '426','X-Channel': 'TC Digital','X-CompanyId': '0023','X-Name': x_name, 'Authorization' : access_token}


# Realizar la solicitud GET con las cabeceras adicionales
response = requests.get(url,access_token, headers=headers)

data = response.text


# Comprobar el código de estado de la respuesta
if response.status_code == 200:
    # La solicitud fue exitosa
    data = response.text
        
    data = data.replace('\n', '|')
    data = data.replace(';', ',') 
    data = data.replace('Fecha_de_Consulta"', '"Fecha_de_Consulta"')
    data = data.replace('\r"', '')
    pairs = data.split("|")

    ind = pairs[0]
    ind = ind.split(",")

    clean_ind = []

    for palabra in ind:
        palabra_sin_r = palabra.replace('\r', '')
        clean_ind.append(palabra_sin_r)

    dict_clear_2 = []

    for i in range(1, len(pairs)):
        diccio = pairs[i]
        diccio = diccio.split(",")
        
        dict_clear = []
        
        for palabra in diccio:
            palabra_sin_r = palabra.replace('\r', '')
            dict_clear.append(palabra_sin_r)

        if dict_clear != ['']:
            dict_clear_2.append(dict_clear)

    for i in dict_clear_2:
        diccionario = dict(zip(clean_ind, i))

        # Datetime de ingesta
        iso_date = datetime.now().replace(microsecond=0).isoformat()

        # ID Ingesta en Cosmosdb
        id_unico =  diccionario["Tipo_de_Documento"]+"-"+diccionario["Numero_de_Documento"]


############################################################################
############### REVISAR LOS NOMBRES DE LA ESTRUCTURA FINAL #################
############################################################################




        estructura = {}
        estructura["Fecha_de_Consulta"] = diccionario["Fecha_de_Consulta"]

        
        dict_person = {}
        general_sumary = {}

        contributions_1 = {}
        contributions_2 = {}
        contributions_3 = {}
        contributions_4 = {}
        contributions_5 = {}
        contributions_6 = {}
        contributions_7 = {}
        contributions_8 = {}
        contributions_9 = {}
        contributions_10 = {}
        contributions_11 = {}
        contributions_12 = {}

        contributionPeriods_1 = {}
        contributionPeriods_2 = {}
        contributionPeriods_3 = {}
        contributionPeriods_4 = {}
        contributionPeriods_5 = {}
        contributionPeriods_6 = {}
        contributionPeriods_7 = {}
        contributionPeriods_8 = {}
        contributionPeriods_9 = {}
        contributionPeriods_10 = {}
        contributionPeriods_11 = {}
        contributionPeriods_12 = {}

        contributionPeriods_1_2 = {}
        contributionPeriods_2_2 = {}
        contributionPeriods_3_2 = {}
        contributionPeriods_4_2 = {}
        contributionPeriods_5_2 = {}
        contributionPeriods_6_2 = {}
        contributionPeriods_7_2 = {}
        contributionPeriods_8_2 = {}
        contributionPeriods_9_2 = {}
        contributionPeriods_10_2 = {}
        contributionPeriods_11_2 = {}
        contributionPeriods_12_2 = {}

        contributionPeriods_1_3 = {}
        contributionPeriods_2_3 = {}
        contributionPeriods_3_3 = {}
        contributionPeriods_4_3 = {}
        contributionPeriods_5_3 = {}
        contributionPeriods_6_3 = {}
        contributionPeriods_7_3 = {}
        contributionPeriods_8_3 = {}
        contributionPeriods_9_3 = {}
        contributionPeriods_10_3 = {}
        contributionPeriods_11_3 = {}
        contributionPeriods_12_3 = {}

        contributionPeriods_1_4 = {}
        contributionPeriods_2_4 = {}
        contributionPeriods_3_4 = {}
        contributionPeriods_4_4 = {}
        contributionPeriods_5_4 = {}
        contributionPeriods_6_4 = {}
        contributionPeriods_7_4 = {}
        contributionPeriods_8_4 = {}
        contributionPeriods_9_4 = {}
        contributionPeriods_10_4 = {}
        contributionPeriods_11_4 = {}
        contributionPeriods_12_4 = {}

        contributionPeriods_1_5 = {}
        contributionPeriods_2_5 = {}
        contributionPeriods_3_5 = {}
        contributionPeriods_4_5 = {}
        contributionPeriods_5_5 = {}
        contributionPeriods_6_5 = {}
        contributionPeriods_7_5 = {}
        contributionPeriods_8_5 = {}
        contributionPeriods_9_5 = {}
        contributionPeriods_10_5 = {}
        contributionPeriods_11_5 = {}
        contributionPeriods_12_5 = {}

        contributionPeriods_1_6 = {}
        contributionPeriods_2_6 = {}
        contributionPeriods_3_6 = {}
        contributionPeriods_4_6 = {}
        contributionPeriods_5_6 = {}
        contributionPeriods_6_6 = {}
        contributionPeriods_7_6 = {}
        contributionPeriods_8_6 = {}
        contributionPeriods_9_6 = {}
        contributionPeriods_10_6 = {}
        contributionPeriods_11_6 = {}
        contributionPeriods_12_6 = {}

        contributionPeriods_1_7 = {}
        contributionPeriods_2_7 = {}
        contributionPeriods_3_7 = {}
        contributionPeriods_4_7 = {}
        contributionPeriods_5_7 = {}
        contributionPeriods_6_7 = {}
        contributionPeriods_7_7 = {}
        contributionPeriods_8_7 = {}
        contributionPeriods_9_7 = {}
        contributionPeriods_10_7 = {}
        contributionPeriods_11_7 = {}
        contributionPeriods_12_7 = {}

        contributionPeriods_1_8 = {}
        contributionPeriods_2_8 = {}
        contributionPeriods_3_8 = {}
        contributionPeriods_4_8 = {}
        contributionPeriods_5_8 = {}
        contributionPeriods_6_8 = {}
        contributionPeriods_7_8 = {}
        contributionPeriods_8_8 = {}
        contributionPeriods_9_8 = {}
        contributionPeriods_10_8 = {}
        contributionPeriods_11_8 = {}
        contributionPeriods_12_8 = {}

        contributionPeriods_1_9 = {}
        contributionPeriods_2_9 = {}
        contributionPeriods_3_9 = {}
        contributionPeriods_4_9 = {}
        contributionPeriods_5_9 = {}
        contributionPeriods_6_9 = {}
        contributionPeriods_7_9 = {}
        contributionPeriods_8_9 = {}
        contributionPeriods_9_9 = {}
        contributionPeriods_10_9 = {}
        contributionPeriods_11_9 = {}
        contributionPeriods_12_9 = {}

        contributionPeriods_1_10 = {}
        contributionPeriods_2_10 = {}
        contributionPeriods_3_10 = {}
        contributionPeriods_4_10 = {}
        contributionPeriods_5_10 = {}
        contributionPeriods_6_10 = {}
        contributionPeriods_7_10 = {}
        contributionPeriods_8_10 = {}
        contributionPeriods_9_10 = {}
        contributionPeriods_10_10 = {}
        contributionPeriods_11_10 = {}
        contributionPeriods_12_10 = {}

        contributionPeriods_1_11 = {}
        contributionPeriods_2_11 = {}
        contributionPeriods_3_11 = {}
        contributionPeriods_4_11 = {}
        contributionPeriods_5_11 = {}
        contributionPeriods_6_11 = {}
        contributionPeriods_7_11 = {}
        contributionPeriods_8_11 = {}
        contributionPeriods_9_11 = {}
        contributionPeriods_10_11 = {}
        contributionPeriods_11_11 = {}
        contributionPeriods_12_11 = {}

        contributionPeriods_1_12 = {}
        contributionPeriods_2_12 = {}
        contributionPeriods_3_12 = {}
        contributionPeriods_4_12 = {}
        contributionPeriods_5_12 = {}
        contributionPeriods_6_12 = {}
        contributionPeriods_7_12 = {}
        contributionPeriods_8_12 = {}
        contributionPeriods_9_12 = {}
        contributionPeriods_10_12 = {}
        contributionPeriods_11_12 = {}
        contributionPeriods_12_12 = {}

        contributions = []


        for i in diccionario:
            #estructura de person
            if i == "Id_Consulta":
                dict_person["queryId"] = diccionario[i]
            if i == "Respuesta":
                dict_person["response"] = diccionario[i]
            if i == "Tipo_de_Documento":
                dict_person["typeDocument"] = diccionario[i]
            if i == "Numero_de_Documento":
                dict_person["numberDocument"] = diccionario[i]
            if i == "Primer_Nombre":
                dict_person["firstName"] = diccionario[i]
            if i == "Segundo_Nombre":
                dict_person["middleName"] = diccionario[i]
            if i == "Primer_Apellido":
                dict_person["lastName"] = diccionario[i]
            if i == "Segundo_Apellido":
                dict_person["secondLastName"] = diccionario[i]
            if i == "EPS":
                dict_person["EPSName"] = diccionario[i]
            if i == "AFP":
                dict_person["AFPName"] = diccionario[i]

            #estructura de person.general_sumary
            if i == "Promedio_Ingresos_del_cotizante":
                general_sumary["averageCurAmt"] = diccionario[i]
            if i == "Mediana_Ingresos_del_cotizante":
                general_sumary["mediamCurAmt"] = diccionario[i]
            if i == "Desviacion_estandar":
                general_sumary["standardDeviation"] = diccionario[i]
            if i == "Ingreso_minimo_del_cotizante":
                general_sumary["min"] = diccionario[i]
            if i == "Ingreso_maximo_del_cotizante":
                general_sumary["max"] = diccionario[i]
            if i == "Pendiente_de_ingresos":
                general_sumary["slope"] = diccionario[i]
            if i == "Tendencia_de_ingresos":
                general_sumary["tendency"] = diccionario[i]
            if i == "Meses_continuidad":
                general_sumary["monthCount"] = diccionario[i]
            if i == "Cantidad_fuentes_de_ingreso":
                general_sumary["contributorsCount"] = diccionario[i]
            if i == "Percentil_general":
                general_sumary["overallPercentile"] = diccionario[i]

#######################################################################################################
######################################### EMPLEADOR 1 #################################################
#######################################################################################################

            #estructura de person.contributions_1
            if i == "Tipo_de_documento_del_empleador_1": #puede estar hasta 12 veces
                contributions_1["typeDocument"] = diccionario[i]
            if i == "Numero_de_documento_del_empleador_1":
                contributions_1["numberDocument"] = diccionario[i]
            if i == "Razon_Social_del_empleador_1":
                contributions_1["fullName"] = diccionario[i]
            if i == "Actividad_econ_empleador_1":
                contributions_1["businessType"] = diccionario[i]
            if i == "Descripcion_actividad_empleador_1":
                contributions_1["businessDesc"] = diccionario[i]
            if i == "Clase_aportante_1":
                contributions_1["contributingClass"] = diccionario[i]
            if i == "Tipo_de_Cotizante_empleador_1":
                contributions_1["typeContribution"] = diccionario[i]
            if i == "Piso_Proteccion_Social_1":
                contributions_1["socialProteccion"] = diccionario[i]
            if i == "Tiene_Salario_Integral_Actualmente_empleador_1":
                contributions_1["integralSalary"] = diccionario[i]
            if i == "Tiene_Novedad_Ingreso_Actualmente_empleador_1":
                contributions_1["newEntryFlag"] = diccionario[i]
            if i == "Tiene_Novedad_Retiro_Actualmente_empleado_1":
                contributions_1["retirementEntryFlag"] = diccionario[i]
            if i == "Tiene_Variacion_Temporal_Actualmente_empleador_1":
                contributions_1["temporarySalaryVariationFlag"] = diccionario[i]
            if i == "Tiene_Variacion_Permantente_Actualmente_empleador_1":
                contributions_1["permanentSalaryVariationFlag"] = diccionario[i]
            if i == "Tiene_Licencia_No_Remunerada_Actualmente_empleador_1":
                contributions_1["unpaidLeaveFlag"] = diccionario[i]
            if i == "Nivel_Riesgo_empleador_1":
                contributions_1["riskLevel"] = diccionario[i]
            if i == "Promedio_Ingresos_del_empleador_1":
                contributions_1["averageCurAmt"] = diccionario[i]
            if i == "Mediana_Ingresos_del_empleador_1":
                contributions_1["mediamCurAmt"] = diccionario[i]
            if i == "Ingreso_minimo_del_empleador_1":
                contributions_1["min"] = diccionario[i]
            if i == "Ingreso_maximo_del_empleador_1":
                contributions_1["max"] = diccionario[i]

            #estructura de person.contributionPeriods_1
            if i == "Ingresos_Pago_1_1":
                contributionPeriods_1["curAmt"] = diccionario[i]
            if i == "Anio_Pago_1_1":
                contributionPeriods_1["expYear"] = diccionario[i]
            if i == "Mes_Pago_1_1":
                contributionPeriods_1["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_1_1":
                contributionPeriods_1["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_2
            if i == "Ingresos_Pago_2_1":
                contributionPeriods_2["curAmt"] = diccionario[i]
            if i == "Anio_Pago_2_1":
                contributionPeriods_2["expYear"] = diccionario[i]
            if i == "Mes_Pago_2_1":
                contributionPeriods_2["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_2_1":
                contributionPeriods_2["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_3
            if i == "Ingresos_Pago_3_1":
                contributionPeriods_3["curAmt"] = diccionario[i]
            if i == "Anio_Pago_3_1":
                contributionPeriods_3["expYear"] = diccionario[i]
            if i == "Mes_Pago_3_1":
                contributionPeriods_3["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_3_1":
                contributionPeriods_3["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_4
            if i == "Ingresos_Pago_4_1":
                contributionPeriods_4["curAmt"] = diccionario[i]
            if i == "Anio_Pago_4_1":
                contributionPeriods_4["expYear"] = diccionario[i]
            if i == "Mes_Pago_4_1":
                contributionPeriods_4["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_4_1":
                contributionPeriods_4["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_5
            if i == "Ingresos_Pago_5_1":
                contributionPeriods_5["curAmt"] = diccionario[i]
            if i == "Anio_Pago_5_1":
                contributionPeriods_5["expYear"] = diccionario[i]
            if i == "Mes_Pago_5_1":
                contributionPeriods_5["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_5_1":
                contributionPeriods_5["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_6
            if i == "Ingresos_Pago_6_1":
                contributionPeriods_6["curAmt"] = diccionario[i]
            if i == "Anio_Pago_6_1":
                contributionPeriods_6["expYear"] = diccionario[i]
            if i == "Mes_Pago_6_1":
                contributionPeriods_6["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_6_1":
                contributionPeriods_6["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_7
            if i == "Ingresos_Pago_7_1":
                contributionPeriods_7["curAmt"] = diccionario[i]
            if i == "Anio_Pago_7_1":
                contributionPeriods_7["expYear"] = diccionario[i]
            if i == "Mes_Pago_7_1":
                contributionPeriods_7["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_7_1":
                contributionPeriods_7["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_8
            if i == "Ingresos_Pago_8_1":
                contributionPeriods_8["curAmt"] = diccionario[i]
            if i == "Anio_Pago_8_1":
                contributionPeriods_8["expYear"] = diccionario[i]
            if i == "Mes_Pago_8_1":
                contributionPeriods_8["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_8_1":
                contributionPeriods_8["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_9
            if i == "Ingresos_Pago_9_1":
                contributionPeriods_9["curAmt"] = diccionario[i]
            if i == "Anio_Pago_9_1":
                contributionPeriods_9["expYear"] = diccionario[i]
            if i == "Mes_Pago_9_1":
                contributionPeriods_9["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_9_1":
                contributionPeriods_9["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_10
            if i == "Ingresos_Pago_10_1":
                contributionPeriods_10["curAmt"] = diccionario[i]
            if i == "Anio_Pago_10_1":
                contributionPeriods_10["expYear"] = diccionario[i]
            if i == "Mes_Pago_10_1":
                contributionPeriods_10["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_10_1":
                contributionPeriods_10["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_11
            if i == "Ingresos_Pago_11_1":
                contributionPeriods_11["curAmt"] = diccionario[i]
            if i == "Anio_Pago_11_1":
                contributionPeriods_11["expYear"] = diccionario[i]
            if i == "Mes_Pago_11_1":
                contributionPeriods_11["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_11_1":
                contributionPeriods_11["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_12
            if i == "Ingresos_Pago_12_1":
                contributionPeriods_12["curAmt"] = diccionario[i]
            if i == "Anio_Pago_12_1":
                contributionPeriods_12["expYear"] = diccionario[i]
            if i == "Mes_Pago_12_1":
                contributionPeriods_12["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_12_1":
                contributionPeriods_12["paymentInd"] = diccionario[i]

#######################################################################################################
######################################### EMPLEADOR 2 #################################################
#######################################################################################################


            #estructura de person.contributions_2
            if i == "Tipo_de_documento_del_empleador_2": #puede estar hasta 12 veces
                contributions_2["typeDocument"] = diccionario[i]
            if i == "Numero_de_documento_del_empleador_2":
                contributions_2["numberDocument"] = diccionario[i]
            if i == "Razon_Social_del_empleador_2":
                contributions_2["fullName"] = diccionario[i]
            if i == "Actividad_econ_empleador_2":
                contributions_2["businessType"] = diccionario[i]
            if i == "Descripcion_actividad_empleador_2":
                contributions_2["businessDesc"] = diccionario[i]
            if i == "Clase_aportante_2":
                contributions_2["contributingClass"] = diccionario[i]
            if i == "Tipo_de_Cotizante_empleador_2":
                contributions_2["typeContribution"] = diccionario[i]
            if i == "Piso_Proteccion_Social_2":
                contributions_2["socialProteccion"] = diccionario[i]
            if i == "Tiene_Salario_Integral_Actualmente_empleador_2":
                contributions_2["integralSalary"] = diccionario[i]
            if i == "Tiene_Novedad_Ingreso_Actualmente_empleador_2":
                contributions_2["newEntryFlag"] = diccionario[i]
            if i == "Tiene_Novedad_Retiro_Actualmente_empleado_2":
                contributions_2["retirementEntryFlag"] = diccionario[i]
            if i == "Tiene_Variacion_Temporal_Actualmente_empleador_2":
                contributions_2["temporarySalaryVariationFlag"] = diccionario[i]
            if i == "Tiene_Variacion_Permantente_Actualmente_empleador_2":
                contributions_2["permanentSalaryVariationFlag"] = diccionario[i]
            if i == "Tiene_Licencia_No_Remunerada_Actualmente_empleador_2":
                contributions_2["unpaidLeaveFlag"] = diccionario[i]
            if i == "Nivel_Riesgo_empleador_2":
                contributions_2["riskLevel"] = diccionario[i]
            if i == "Promedio_Ingresos_del_empleador_2":
                contributions_2["averageCurAmt"] = diccionario[i]
            if i == "Mediana_Ingresos_del_empleador_2":
                contributions_2["mediamCurAmt"] = diccionario[i]
            if i == "Ingreso_minimo_del_empleador_2":
                contributions_2["min"] = diccionario[i]
            if i == "Ingreso_maximo_del_empleador_2":
                contributions_2["max"] = diccionario[i]

            #estructura de person.contributionPeriods_1_2
            if i == "Ingresos_Pago_1_2":
                contributionPeriods_1_2["curAmt"] = diccionario[i]
            if i == "Anio_Pago_1_2":
                contributionPeriods_1_2["expYear"] = diccionario[i]
            if i == "Mes_Pago_1_2":
                contributionPeriods_1_2["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_1_2":
                contributionPeriods_1_2["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_2_2
            if i == "Ingresos_Pago_2_2":
                contributionPeriods_2_2["curAmt"] = diccionario[i]
            if i == "Anio_Pago_2_2":
                contributionPeriods_2_2["expYear"] = diccionario[i]
            if i == "Mes_Pago_2_2":
                contributionPeriods_2_2["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_2_2":
                contributionPeriods_2_2["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_3_2
            if i == "Ingresos_Pago_3_2":
                contributionPeriods_3_2["curAmt"] = diccionario[i]
            if i == "Anio_Pago_3_2":
                contributionPeriods_3_2["expYear"] = diccionario[i]
            if i == "Mes_Pago_3_2":
                contributionPeriods_3_2["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_3_2":
                contributionPeriods_3_2["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_4_2
            if i == "Ingresos_Pago_4_2":
                contributionPeriods_4_2["curAmt"] = diccionario[i]
            if i == "Anio_Pago_4_2":
                contributionPeriods_4_2["expYear"] = diccionario[i]
            if i == "Mes_Pago_4_2":
                contributionPeriods_4_2["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_4_2":
                contributionPeriods_4_2["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_5_2
            if i == "Ingresos_Pago_5_2":
                contributionPeriods_5_2["curAmt"] = diccionario[i]
            if i == "Anio_Pago_5_2":
                contributionPeriods_5_2["expYear"] = diccionario[i]
            if i == "Mes_Pago_5_2":
                contributionPeriods_5_2["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_5_2":
                contributionPeriods_5_2["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_6_2
            if i == "Ingresos_Pago_6_2":
                contributionPeriods_6_2["curAmt"] = diccionario[i]
            if i == "Anio_Pago_6_2":
                contributionPeriods_6_2["expYear"] = diccionario[i]
            if i == "Mes_Pago_6_2":
                contributionPeriods_6_2["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_6_2":
                contributionPeriods_6_2["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_7_2
            if i == "Ingresos_Pago_7_2":
                contributionPeriods_7_2["curAmt"] = diccionario[i]
            if i == "Anio_Pago_7_2":
                contributionPeriods_7_2["expYear"] = diccionario[i]
            if i == "Mes_Pago_7_2":
                contributionPeriods_7_2["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_7_2":
                contributionPeriods_7_2["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_8_2
            if i == "Ingresos_Pago_8_2":
                contributionPeriods_8_2["curAmt"] = diccionario[i]
            if i == "Anio_Pago_8_2":
                contributionPeriods_8_2["expYear"] = diccionario[i]
            if i == "Mes_Pago_8_2":
                contributionPeriods_8_2["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_8_2":
                contributionPeriods_8_2["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_9_2
            if i == "Ingresos_Pago_9_2":
                contributionPeriods_9_2["curAmt"] = diccionario[i]
            if i == "Anio_Pago_9_2":
                contributionPeriods_9_2["expYear"] = diccionario[i]
            if i == "Mes_Pago_9_2":
                contributionPeriods_9_2["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_9_2":
                contributionPeriods_9_2["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_10_2
            if i == "Ingresos_Pago_10_2":
                contributionPeriods_10_2["curAmt"] = diccionario[i]
            if i == "Anio_Pago_10_2":
                contributionPeriods_10_2["expYear"] = diccionario[i]
            if i == "Mes_Pago_10_2":
                contributionPeriods_10_2["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_10_2":
                contributionPeriods_10_2["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_11_2
            if i == "Ingresos_Pago_11_2":
                contributionPeriods_11_2["curAmt"] = diccionario[i]
            if i == "Anio_Pago_11_2":
                contributionPeriods_11_2["expYear"] = diccionario[i]
            if i == "Mes_Pago_11_2":
                contributionPeriods_11_2["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_11_2":
                contributionPeriods_11_2["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_12_2
            if i == "Ingresos_Pago_12_2":
                contributionPeriods_12_2["curAmt"] = diccionario[i]
            if i == "Anio_Pago_12_2":
                contributionPeriods_12_2["expYear"] = diccionario[i]
            if i == "Mes_Pago_12_2":
                contributionPeriods_12_2["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_12_2":
                contributionPeriods_12_2["paymentInd"] = diccionario[i]

#######################################################################################################
######################################### EMPLEADOR 3 #################################################
#######################################################################################################

            #estructura de person.contributions_3
            if i == "Tipo_de_documento_del_empleador_3": #puede estar hasta 12 veces
                contributions_3["typeDocument"] = diccionario[i]
            if i == "Numero_de_documento_del_empleador_3":
                contributions_3["numberDocument"] = diccionario[i]
            if i == "Razon_Social_del_empleador_3":
                contributions_3["fullName"] = diccionario[i]
            if i == "Actividad_econ_empleador_3":
                contributions_3["businessType"] = diccionario[i]
            if i == "Descripcion_actividad_empleador_3":
                contributions_3["businessDesc"] = diccionario[i]
            if i == "Clase_aportante_3":
                contributions_3["contributingClass"] = diccionario[i]
            if i == "Tipo_de_Cotizante_empleador_3":
                contributions_3["typeContribution"] = diccionario[i]
            if i == "Piso_Proteccion_Social_3":
                contributions_3["socialProteccion"] = diccionario[i]
            if i == "Tiene_Salario_Integral_Actualmente_empleador_3":
                contributions_3["integralSalary"] = diccionario[i]
            if i == "Tiene_Novedad_Ingreso_Actualmente_empleador_3":
                contributions_3["newEntryFlag"] = diccionario[i]
            if i == "Tiene_Novedad_Retiro_Actualmente_empleado_3":
                contributions_3["retirementEntryFlag"] = diccionario[i]
            if i == "Tiene_Variacion_Temporal_Actualmente_empleador_3":
                contributions_3["temporarySalaryVariationFlag"] = diccionario[i]
            if i == "Tiene_Variacion_Permantente_Actualmente_empleador_3":
                contributions_3["permanentSalaryVariationFlag"] = diccionario[i]
            if i == "Tiene_Licencia_No_Remunerada_Actualmente_empleador_3":
                contributions_3["unpaidLeaveFlag"] = diccionario[i]
            if i == "Nivel_Riesgo_empleador_3":
                contributions_3["riskLevel"] = diccionario[i]
            if i == "Promedio_Ingresos_del_empleador_3":
                contributions_3["averageCurAmt"] = diccionario[i]
            if i == "Mediana_Ingresos_del_empleador_3":
                contributions_3["mediamCurAmt"] = diccionario[i]
            if i == "Ingreso_minimo_del_empleador_3":
                contributions_3["min"] = diccionario[i]
            if i == "Ingreso_maximo_del_empleador_3":
                contributions_3["max"] = diccionario[i]

            #estructura de person.contributionPeriods_1_3
            if i == "Ingresos_Pago_1_3":
                contributionPeriods_1_3["curAmt"] = diccionario[i]
            if i == "Anio_Pago_1_3":
                contributionPeriods_1_3["expYear"] = diccionario[i]
            if i == "Mes_Pago_1_3":
                contributionPeriods_1_3["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_1_3":
                contributionPeriods_1_3["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_2_3
            if i == "Ingresos_Pago_2_3":
                contributionPeriods_2_3["curAmt"] = diccionario[i]
            if i == "Anio_Pago_2_3":
                contributionPeriods_2_3["expYear"] = diccionario[i]
            if i == "Mes_Pago_2_3":
                contributionPeriods_2_3["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_2_3":
                contributionPeriods_2_3["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_3_3
            if i == "Ingresos_Pago_3_3":
                contributionPeriods_3_3["curAmt"] = diccionario[i]
            if i == "Anio_Pago_3_3":
                contributionPeriods_3_3["expYear"] = diccionario[i]
            if i == "Mes_Pago_3_3":
                contributionPeriods_3_3["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_3_3":
                contributionPeriods_3_3["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_4_3
            if i == "Ingresos_Pago_4_3":
                contributionPeriods_4_3["curAmt"] = diccionario[i]
            if i == "Anio_Pago_4_3":
                contributionPeriods_4_3["expYear"] = diccionario[i]
            if i == "Mes_Pago_4_3":
                contributionPeriods_4_3["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_4_3":
                contributionPeriods_4_3["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_5_3
            if i == "Ingresos_Pago_5_3":
                contributionPeriods_5_3["curAmt"] = diccionario[i]
            if i == "Anio_Pago_5_3":
                contributionPeriods_5_3["expYear"] = diccionario[i]
            if i == "Mes_Pago_5_3":
                contributionPeriods_5_3["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_5_3":
                contributionPeriods_5_3["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_6_3
            if i == "Ingresos_Pago_6_3":
                contributionPeriods_6_3["curAmt"] = diccionario[i]
            if i == "Anio_Pago_6_3":
                contributionPeriods_6_3["expYear"] = diccionario[i]
            if i == "Mes_Pago_6_3":
                contributionPeriods_6_3["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_6_3":
                contributionPeriods_6_3["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_7_3
            if i == "Ingresos_Pago_7_3":
                contributionPeriods_7_3["curAmt"] = diccionario[i]
            if i == "Anio_Pago_7_3":
                contributionPeriods_7_3["expYear"] = diccionario[i]
            if i == "Mes_Pago_7_3":
                contributionPeriods_7_3["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_7_3":
                contributionPeriods_7_3["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_8_3
            if i == "Ingresos_Pago_8_3":
                contributionPeriods_8_3["curAmt"] = diccionario[i]
            if i == "Anio_Pago_8_3":
                contributionPeriods_8_3["expYear"] = diccionario[i]
            if i == "Mes_Pago_8_3":
                contributionPeriods_8_3["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_8_3":
                contributionPeriods_8_3["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_9_3
            if i == "Ingresos_Pago_9_3":
                contributionPeriods_9_3["curAmt"] = diccionario[i]
            if i == "Anio_Pago_9_3":
                contributionPeriods_9_3["expYear"] = diccionario[i]
            if i == "Mes_Pago_9_3":
                contributionPeriods_9_3["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_9_3":
                contributionPeriods_9_3["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_10_3
            if i == "Ingresos_Pago_10_3":
                contributionPeriods_10_3["curAmt"] = diccionario[i]
            if i == "Anio_Pago_10_3":
                contributionPeriods_10_3["expYear"] = diccionario[i]
            if i == "Mes_Pago_10_3":
                contributionPeriods_10_3["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_10_3":
                contributionPeriods_10_3["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_11_3
            if i == "Ingresos_Pago_11_3":
                contributionPeriods_11_3["curAmt"] = diccionario[i]
            if i == "Anio_Pago_11_3":
                contributionPeriods_11_3["expYear"] = diccionario[i]
            if i == "Mes_Pago_11_3":
                contributionPeriods_11_3["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_11_3":
                contributionPeriods_11_3["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_12_3
            if i == "Ingresos_Pago_12_3":
                contributionPeriods_12_3["curAmt"] = diccionario[i]
            if i == "Anio_Pago_12_3":
                contributionPeriods_12_3["expYear"] = diccionario[i]
            if i == "Mes_Pago_12_3":
                contributionPeriods_12_3["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_12_3":
                contributionPeriods_12_3["paymentInd"] = diccionario[i]

#######################################################################################################
######################################### EMPLEADOR 4 #################################################
#######################################################################################################

            #estructura de person.contributions_4
            if i == "Tipo_de_documento_del_empleador_4": #puede estar hasta 12 veces
                contributions_4["typeDocument"] = diccionario[i]
            if i == "Numero_de_documento_del_empleador_4":
                contributions_4["numberDocument"] = diccionario[i]
            if i == "Razon_Social_del_empleador_4":
                contributions_4["fullName"] = diccionario[i]
            if i == "Actividad_econ_empleador_4":
                contributions_4["businessType"] = diccionario[i]
            if i == "Descripcion_actividad_empleador_4":
                contributions_4["businessDesc"] = diccionario[i]
            if i == "Clase_aportante_4":
                contributions_4["contributingClass"] = diccionario[i]
            if i == "Tipo_de_Cotizante_empleador_4":
                contributions_4["typeContribution"] = diccionario[i]
            if i == "Piso_Proteccion_Social_4":
                contributions_4["socialProteccion"] = diccionario[i]
            if i == "Tiene_Salario_Integral_Actualmente_empleador_4":
                contributions_4["integralSalary"] = diccionario[i]
            if i == "Tiene_Novedad_Ingreso_Actualmente_empleador_4":
                contributions_4["newEntryFlag"] = diccionario[i]
            if i == "Tiene_Novedad_Retiro_Actualmente_empleado_4":
                contributions_4["retirementEntryFlag"] = diccionario[i]
            if i == "Tiene_Variacion_Temporal_Actualmente_empleador_4":
                contributions_4["temporarySalaryVariationFlag"] = diccionario[i]
            if i == "Tiene_Variacion_Permantente_Actualmente_empleador_4":
                contributions_4["permanentSalaryVariationFlag"] = diccionario[i]
            if i == "Tiene_Licencia_No_Remunerada_Actualmente_empleador_4":
                contributions_4["unpaidLeaveFlag"] = diccionario[i]
            if i == "Nivel_Riesgo_empleador_4":
                contributions_4["riskLevel"] = diccionario[i]
            if i == "Promedio_Ingresos_del_empleador_4":
                contributions_4["averageCurAmt"] = diccionario[i]
            if i == "Mediana_Ingresos_del_empleador_4":
                contributions_4["mediamCurAmt"] = diccionario[i]
            if i == "Ingreso_minimo_del_empleador_4":
                contributions_4["min"] = diccionario[i]
            if i == "Ingreso_maximo_del_empleador_4":
                contributions_4["max"] = diccionario[i]

            #estructura de person.contributionPeriods_1_4
            if i == "Ingresos_Pago_1_4":
                contributionPeriods_1_4["curAmt"] = diccionario[i]
            if i == "Anio_Pago_1_4":
                contributionPeriods_1_4["expYear"] = diccionario[i]
            if i == "Mes_Pago_1_4":
                contributionPeriods_1_4["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_1_4":
                contributionPeriods_1_4["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_2_4
            if i == "Ingresos_Pago_2_4":
                contributionPeriods_2_4["curAmt"] = diccionario[i]
            if i == "Anio_Pago_2_4":
                contributionPeriods_2_4["expYear"] = diccionario[i]
            if i == "Mes_Pago_2_4":
                contributionPeriods_2_4["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_2_4":
                contributionPeriods_2_4["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_3_4
            if i == "Ingresos_Pago_3_4":
                contributionPeriods_3_4["curAmt"] = diccionario[i]
            if i == "Anio_Pago_3_4":
                contributionPeriods_3_4["expYear"] = diccionario[i]
            if i == "Mes_Pago_3_4":
                contributionPeriods_3_4["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_3_4":
                contributionPeriods_3_4["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_4_4
            if i == "Ingresos_Pago_4_4":
                contributionPeriods_4_4["curAmt"] = diccionario[i]
            if i == "Anio_Pago_4_4":
                contributionPeriods_4_4["expYear"] = diccionario[i]
            if i == "Mes_Pago_4_4":
                contributionPeriods_4_4["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_4_4":
                contributionPeriods_4_4["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_5_4
            if i == "Ingresos_Pago_5_4":
                contributionPeriods_5_4["curAmt"] = diccionario[i]
            if i == "Anio_Pago_5_4":
                contributionPeriods_5_4["expYear"] = diccionario[i]
            if i == "Mes_Pago_5_4":
                contributionPeriods_5_4["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_5_4":
                contributionPeriods_5_4["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_6_4
            if i == "Ingresos_Pago_6_4":
                contributionPeriods_6_4["curAmt"] = diccionario[i]
            if i == "Anio_Pago_6_4":
                contributionPeriods_6_4["expYear"] = diccionario[i]
            if i == "Mes_Pago_6_4":
                contributionPeriods_6_4["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_6_4":
                contributionPeriods_6_4["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_7_4
            if i == "Ingresos_Pago_7_4":
                contributionPeriods_7_4["curAmt"] = diccionario[i]
            if i == "Anio_Pago_7_4":
                contributionPeriods_7_4["expYear"] = diccionario[i]
            if i == "Mes_Pago_7_4":
                contributionPeriods_7_4["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_7_4":
                contributionPeriods_7_4["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_8_4
            if i == "Ingresos_Pago_8_4":
                contributionPeriods_8_4["curAmt"] = diccionario[i]
            if i == "Anio_Pago_8_4":
                contributionPeriods_8_4["expYear"] = diccionario[i]
            if i == "Mes_Pago_8_4":
                contributionPeriods_8_4["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_8_4":
                contributionPeriods_8_4["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_9_4
            if i == "Ingresos_Pago_9_4":
                contributionPeriods_9_4["curAmt"] = diccionario[i]
            if i == "Anio_Pago_9_4":
                contributionPeriods_9_4["expYear"] = diccionario[i]
            if i == "Mes_Pago_9_4":
                contributionPeriods_9_4["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_9_4":
                contributionPeriods_9_4["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_10_4
            if i == "Ingresos_Pago_10_4":
                contributionPeriods_10_4["curAmt"] = diccionario[i]
            if i == "Anio_Pago_10_4":
                contributionPeriods_10_4["expYear"] = diccionario[i]
            if i == "Mes_Pago_10_4":
                contributionPeriods_10_4["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_10_4":
                contributionPeriods_10_4["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_11_4
            if i == "Ingresos_Pago_11_4":
                contributionPeriods_11_4["curAmt"] = diccionario[i]
            if i == "Anio_Pago_11_4":
                contributionPeriods_11_4["expYear"] = diccionario[i]
            if i == "Mes_Pago_11_4":
                contributionPeriods_11_4["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_11_4":
                contributionPeriods_11_4["paymentInd"] = diccionario[i]
            
            #estructura de person.contributionPeriods_12_4
            if i == "Ingresos_Pago_12_4":
                contributionPeriods_12_4["curAmt"] = diccionario[i]
            if i == "Anio_Pago_12_4":
                contributionPeriods_12_4["expYear"] = diccionario[i]
            if i == "Mes_Pago_12_4":
                contributionPeriods_12_4["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_12_4":
                contributionPeriods_12_4["paymentInd"] = diccionario[i]

#######################################################################################################
######################################### EMPLEADOR 5 #################################################
#######################################################################################################


            #estructura de person.contributions_5
            if i == "Tipo_de_documento_del_empleador_5": #puede estar hasta 12 veces
                contributions_5["typeDocument"] = diccionario[i]
            if i == "Numero_de_documento_del_empleador_5":
                contributions_5["numberDocument"] = diccionario[i]
            if i == "Razon_Social_del_empleador_5":
                contributions_5["fullName"] = diccionario[i]
            if i == "Actividad_econ_empleador_5":
                contributions_5["businessType"] = diccionario[i]
            if i == "Descripcion_actividad_empleador_5":
                contributions_5["businessDesc"] = diccionario[i]
            if i == "Clase_aportante_5":
                contributions_5["contributingClass"] = diccionario[i]
            if i == "Tipo_de_Cotizante_empleador_5":
                contributions_5["typeContribution"] = diccionario[i]
            if i == "Piso_Proteccion_Social_5":
                contributions_5["socialProteccion"] = diccionario[i]
            if i == "Tiene_Salario_Integral_Actualmente_empleador_5":
                contributions_5["integralSalary"] = diccionario[i]
            if i == "Tiene_Novedad_Ingreso_Actualmente_empleador_5":
                contributions_5["newEntryFlag"] = diccionario[i]
            if i == "Tiene_Novedad_Retiro_Actualmente_empleado_5":
                contributions_5["retirementEntryFlag"] = diccionario[i]
            if i == "Tiene_Variacion_Temporal_Actualmente_empleador_5":
                contributions_5["temporarySalaryVariationFlag"] = diccionario[i]
            if i == "Tiene_Variacion_Permantente_Actualmente_empleador_5":
                contributions_5["permanentSalaryVariationFlag"] = diccionario[i]
            if i == "Tiene_Licencia_No_Remunerada_Actualmente_empleador_5":
                contributions_5["unpaidLeaveFlag"] = diccionario[i]
            if i == "Nivel_Riesgo_empleador_5":
                contributions_5["riskLevel"] = diccionario[i]
            if i == "Promedio_Ingresos_del_empleador_5":
                contributions_5["averageCurAmt"] = diccionario[i]
            if i == "Mediana_Ingresos_del_empleador_5":
                contributions_5["mediamCurAmt"] = diccionario[i]
            if i == "Ingreso_minimo_del_empleador_5":
                contributions_5["min"] = diccionario[i]
            if i == "Ingreso_maximo_del_empleador_5":
                contributions_5["max"] = diccionario[i]

            #estructura de person.contributionPeriods_1_5
            if i == "Ingresos_Pago_1_5":
                contributionPeriods_1_5["curAmt"] = diccionario[i]
            if i == "Anio_Pago_1_5":
                contributionPeriods_1_5["expYear"] = diccionario[i]
            if i == "Mes_Pago_1_5":
                contributionPeriods_1_5["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_1_5":
                contributionPeriods_1_5["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_2_5
            if i == "Ingresos_Pago_2_5":
                contributionPeriods_2_5["curAmt"] = diccionario[i]
            if i == "Anio_Pago_2_5":
                contributionPeriods_2_5["expYear"] = diccionario[i]
            if i == "Mes_Pago_2_5":
                contributionPeriods_2_5["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_2_5":
                contributionPeriods_2_5["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_3_5
            if i == "Ingresos_Pago_3_5":
                contributionPeriods_3_5["curAmt"] = diccionario[i]
            if i == "Anio_Pago_3_5":
                contributionPeriods_3_5["expYear"] = diccionario[i]
            if i == "Mes_Pago_3_5":
                contributionPeriods_3_5["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_3_5":
                contributionPeriods_3_5["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_4_5
            if i == "Ingresos_Pago_4_5":
                contributionPeriods_4_5["curAmt"] = diccionario[i]
            if i == "Anio_Pago_4_5":
                contributionPeriods_4_5["expYear"] = diccionario[i]
            if i == "Mes_Pago_4_5":
                contributionPeriods_4_5["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_4_5":
                contributionPeriods_4_5["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_5_5
            if i == "Ingresos_Pago_5_5":
                contributionPeriods_5_5["curAmt"] = diccionario[i]
            if i == "Anio_Pago_5_5":
                contributionPeriods_5_5["expYear"] = diccionario[i]
            if i == "Mes_Pago_5_5":
                contributionPeriods_5_5["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_5_5":
                contributionPeriods_5_5["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_6_5
            if i == "Ingresos_Pago_6_5":
                contributionPeriods_6_5["curAmt"] = diccionario[i]
            if i == "Anio_Pago_6_5":
                contributionPeriods_6_5["expYear"] = diccionario[i]
            if i == "Mes_Pago_6_5":
                contributionPeriods_6_5["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_6_5":
                contributionPeriods_6_5["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_7_5
            if i == "Ingresos_Pago_7_5":
                contributionPeriods_7_5["curAmt"] = diccionario[i]
            if i == "Anio_Pago_7_5":
                contributionPeriods_7_5["expYear"] = diccionario[i]
            if i == "Mes_Pago_7_5":
                contributionPeriods_7_5["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_7_5":
                contributionPeriods_7_5["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_8_5
            if i == "Ingresos_Pago_8_5":
                contributionPeriods_8_5["curAmt"] = diccionario[i]
            if i == "Anio_Pago_8_5":
                contributionPeriods_8_5["expYear"] = diccionario[i]
            if i == "Mes_Pago_8_5":
                contributionPeriods_8_5["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_8_5":
                contributionPeriods_8_5["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_9_5
            if i == "Ingresos_Pago_9_5":
                contributionPeriods_9_5["curAmt"] = diccionario[i]
            if i == "Anio_Pago_9_5":
                contributionPeriods_9_5["expYear"] = diccionario[i]
            if i == "Mes_Pago_9_5":
                contributionPeriods_9_5["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_9_5":
                contributionPeriods_9_5["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_10_5
            if i == "Ingresos_Pago_10_5":
                contributionPeriods_10_5["curAmt"] = diccionario[i]
            if i == "Anio_Pago_10_5":
                contributionPeriods_10_5["expYear"] = diccionario[i]
            if i == "Mes_Pago_10_5":
                contributionPeriods_10_5["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_10_5":
                contributionPeriods_10_5["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_11_5
            if i == "Ingresos_Pago_11_5":
                contributionPeriods_11_5["curAmt"] = diccionario[i]
            if i == "Anio_Pago_11_5":
                contributionPeriods_11_5["expYear"] = diccionario[i]
            if i == "Mes_Pago_11_5":
                contributionPeriods_11_5["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_11_5":
                contributionPeriods_11_5["paymentInd"] = diccionario[i]
            
            #estructura de person.contributionPeriods_12_5
            if i == "Ingresos_Pago_12_5":
                contributionPeriods_12_5["curAmt"] = diccionario[i]
            if i == "Anio_Pago_12_5":
                contributionPeriods_12_5["expYear"] = diccionario[i]
            if i == "Mes_Pago_12_5":
                contributionPeriods_12_5["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_12_5":
                contributionPeriods_12_5["paymentInd"] = diccionario[i]

#######################################################################################################
######################################### EMPLEADOR 6 #################################################
#######################################################################################################


            #estructura de person.contributions_6
            if i == "Tipo_de_documento_del_empleador_6": #puede estar hasta 12 veces
                contributions_6["typeDocument"] = diccionario[i]
            if i == "Numero_de_documento_del_empleador_6":
                contributions_6["numberDocument"] = diccionario[i]
            if i == "Razon_Social_del_empleador_6":
                contributions_6["fullName"] = diccionario[i]
            if i == "Actividad_econ_empleador_6":
                contributions_6["businessType"] = diccionario[i]
            if i == "Descripcion_actividad_empleador_6":
                contributions_6["businessDesc"] = diccionario[i]
            if i == "Clase_aportante_6":
                contributions_6["contributingClass"] = diccionario[i]
            if i == "Tipo_de_Cotizante_empleador_6":
                contributions_6["typeContribution"] = diccionario[i]
            if i == "Piso_Proteccion_Social_6":
                contributions_6["socialProteccion"] = diccionario[i]
            if i == "Tiene_Salario_Integral_Actualmente_empleador_6":
                contributions_6["integralSalary"] = diccionario[i]
            if i == "Tiene_Novedad_Ingreso_Actualmente_empleador_6":
                contributions_6["newEntryFlag"] = diccionario[i]
            if i == "Tiene_Novedad_Retiro_Actualmente_empleado_6":
                contributions_6["retirementEntryFlag"] = diccionario[i]
            if i == "Tiene_Variacion_Temporal_Actualmente_empleador_6":
                contributions_6["temporarySalaryVariationFlag"] = diccionario[i]
            if i == "Tiene_Variacion_Permantente_Actualmente_empleador_6":
                contributions_6["permanentSalaryVariationFlag"] = diccionario[i]
            if i == "Tiene_Licencia_No_Remunerada_Actualmente_empleador_6":
                contributions_6["unpaidLeaveFlag"] = diccionario[i]
            if i == "Nivel_Riesgo_empleador_6":
                contributions_6["riskLevel"] = diccionario[i]
            if i == "Promedio_Ingresos_del_empleador_6":
                contributions_6["averageCurAmt"] = diccionario[i]
            if i == "Mediana_Ingresos_del_empleador_6":
                contributions_6["mediamCurAmt"] = diccionario[i]
            if i == "Ingreso_minimo_del_empleador_6":
                contributions_6["min"] = diccionario[i]
            if i == "Ingreso_maximo_del_empleador_6":
                contributions_6["max"] = diccionario[i]

            #estructura de person.contributionPeriods_1_6
            if i == "Ingresos_Pago_1_6":
                contributionPeriods_1_6["curAmt"] = diccionario[i]
            if i == "Anio_Pago_1_6":
                contributionPeriods_1_6["expYear"] = diccionario[i]
            if i == "Mes_Pago_1_6":
                contributionPeriods_1_6["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_1_6":
                contributionPeriods_1_6["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_2_6
            if i == "Ingresos_Pago_2_6":
                contributionPeriods_2_6["curAmt"] = diccionario[i]
            if i == "Anio_Pago_2_6":
                contributionPeriods_2_6["expYear"] = diccionario[i]
            if i == "Mes_Pago_2_6":
                contributionPeriods_2_6["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_2_6":
                contributionPeriods_2_6["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_3_6
            if i == "Ingresos_Pago_3_6":
                contributionPeriods_3_6["curAmt"] = diccionario[i]
            if i == "Anio_Pago_3_6":
                contributionPeriods_3_6["expYear"] = diccionario[i]
            if i == "Mes_Pago_3_6":
                contributionPeriods_3_6["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_3_6":
                contributionPeriods_3_6["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_4_6
            if i == "Ingresos_Pago_4_6":
                contributionPeriods_4_6["curAmt"] = diccionario[i]
            if i == "Anio_Pago_4_6":
                contributionPeriods_4_6["expYear"] = diccionario[i]
            if i == "Mes_Pago_4_6":
                contributionPeriods_4_6["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_4_6":
                contributionPeriods_4_6["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_5_6
            if i == "Ingresos_Pago_5_6":
                contributionPeriods_5_6["curAmt"] = diccionario[i]
            if i == "Anio_Pago_5_6":
                contributionPeriods_5_6["expYear"] = diccionario[i]
            if i == "Mes_Pago_5_6":
                contributionPeriods_5_6["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_5_6":
                contributionPeriods_5_6["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_6_6
            if i == "Ingresos_Pago_6_6":
                contributionPeriods_6_6["curAmt"] = diccionario[i]
            if i == "Anio_Pago_6_6":
                contributionPeriods_6_6["expYear"] = diccionario[i]
            if i == "Mes_Pago_6_6":
                contributionPeriods_6_6["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_6_6":
                contributionPeriods_6_6["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_7_6
            if i == "Ingresos_Pago_7_6":
                contributionPeriods_7_6["curAmt"] = diccionario[i]
            if i == "Anio_Pago_7_6":
                contributionPeriods_7_6["expYear"] = diccionario[i]
            if i == "Mes_Pago_7_6":
                contributionPeriods_7_6["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_7_6":
                contributionPeriods_7_6["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_8_6
            if i == "Ingresos_Pago_8_6":
                contributionPeriods_8_6["curAmt"] = diccionario[i]
            if i == "Anio_Pago_8_6":
                contributionPeriods_8_6["expYear"] = diccionario[i]
            if i == "Mes_Pago_8_6":
                contributionPeriods_8_6["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_8_6":
                contributionPeriods_8_6["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_9_6
            if i == "Ingresos_Pago_9_6":
                contributionPeriods_9_6["curAmt"] = diccionario[i]
            if i == "Anio_Pago_9_6":
                contributionPeriods_9_6["expYear"] = diccionario[i]
            if i == "Mes_Pago_9_6":
                contributionPeriods_9_6["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_9_6":
                contributionPeriods_9_6["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_10_6
            if i == "Ingresos_Pago_10_6":
                contributionPeriods_10_6["curAmt"] = diccionario[i]
            if i == "Anio_Pago_10_6":
                contributionPeriods_10_6["expYear"] = diccionario[i]
            if i == "Mes_Pago_10_6":
                contributionPeriods_10_6["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_10_6":
                contributionPeriods_10_6["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_11_6
            if i == "Ingresos_Pago_11_6":
                contributionPeriods_11_6["curAmt"] = diccionario[i]
            if i == "Anio_Pago_11_6":
                contributionPeriods_11_6["expYear"] = diccionario[i]
            if i == "Mes_Pago_11_6":
                contributionPeriods_11_6["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_11_6":
                contributionPeriods_11_6["paymentInd"] = diccionario[i]
            
            #estructura de person.contributionPeriods_12_6
            if i == "Ingresos_Pago_12_6":
                contributionPeriods_12_6["curAmt"] = diccionario[i]
            if i == "Anio_Pago_12_6":
                contributionPeriods_12_6["expYear"] = diccionario[i]
            if i == "Mes_Pago_12_6":
                contributionPeriods_12_6["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_12_6":
                contributionPeriods_12_6["paymentInd"] = diccionario[i]

#######################################################################################################
######################################### EMPLEADOR 7 #################################################
#######################################################################################################


            #estructura de person.contributions_7
            if i == "Tipo_de_documento_del_empleador_7": #puede estar hasta 12 veces
                contributions_7["typeDocument"] = diccionario[i]
            if i == "Numero_de_documento_del_empleador_7":
                contributions_7["numberDocument"] = diccionario[i]
            if i == "Razon_Social_del_empleador_7":
                contributions_7["fullName"] = diccionario[i]
            if i == "Actividad_econ_empleador_7":
                contributions_7["businessType"] = diccionario[i]
            if i == "Descripcion_actividad_empleador_7":
                contributions_7["businessDesc"] = diccionario[i]
            if i == "Clase_aportante_7":
                contributions_7["contributingClass"] = diccionario[i]
            if i == "Tipo_de_Cotizante_empleador_7":
                contributions_7["typeContribution"] = diccionario[i]
            if i == "Piso_Proteccion_Social_7":
                contributions_7["socialProteccion"] = diccionario[i]
            if i == "Tiene_Salario_Integral_Actualmente_empleador_7":
                contributions_7["integralSalary"] = diccionario[i]
            if i == "Tiene_Novedad_Ingreso_Actualmente_empleador_7":
                contributions_7["newEntryFlag"] = diccionario[i]
            if i == "Tiene_Novedad_Retiro_Actualmente_empleado_7":
                contributions_7["retirementEntryFlag"] = diccionario[i]
            if i == "Tiene_Variacion_Temporal_Actualmente_empleador_7":
                contributions_7["temporarySalaryVariationFlag"] = diccionario[i]
            if i == "Tiene_Variacion_Permantente_Actualmente_empleador_7":
                contributions_7["permanentSalaryVariationFlag"] = diccionario[i]
            if i == "Tiene_Licencia_No_Remunerada_Actualmente_empleador_7":
                contributions_7["unpaidLeaveFlag"] = diccionario[i]
            if i == "Nivel_Riesgo_empleador_7":
                contributions_7["riskLevel"] = diccionario[i]
            if i == "Promedio_Ingresos_del_empleador_7":
                contributions_7["averageCurAmt"] = diccionario[i]
            if i == "Mediana_Ingresos_del_empleador_7":
                contributions_7["mediamCurAmt"] = diccionario[i]
            if i == "Ingreso_minimo_del_empleador_7":
                contributions_7["min"] = diccionario[i]
            if i == "Ingreso_maximo_del_empleador_7":
                contributions_7["max"] = diccionario[i]

            #estructura de person.contributionPeriods_1_7
            if i == "Ingresos_Pago_1_7":
                contributionPeriods_1_7["curAmt"] = diccionario[i]
            if i == "Anio_Pago_1_7":
                contributionPeriods_1_7["expYear"] = diccionario[i]
            if i == "Mes_Pago_1_7":
                contributionPeriods_1_7["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_1_7":
                contributionPeriods_1_7["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_2_7
            if i == "Ingresos_Pago_2_7":
                contributionPeriods_2_7["curAmt"] = diccionario[i]
            if i == "Anio_Pago_2_7":
                contributionPeriods_2_7["expYear"] = diccionario[i]
            if i == "Mes_Pago_2_7":
                contributionPeriods_2_7["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_2_7":
                contributionPeriods_2_7["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_3_7
            if i == "Ingresos_Pago_3_7":
                contributionPeriods_3_7["curAmt"] = diccionario[i]
            if i == "Anio_Pago_3_7":
                contributionPeriods_3_7["expYear"] = diccionario[i]
            if i == "Mes_Pago_3_7":
                contributionPeriods_3_7["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_3_7":
                contributionPeriods_3_7["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_4_7
            if i == "Ingresos_Pago_4_7":
                contributionPeriods_4_7["curAmt"] = diccionario[i]
            if i == "Anio_Pago_4_7":
                contributionPeriods_4_7["expYear"] = diccionario[i]
            if i == "Mes_Pago_4_7":
                contributionPeriods_4_7["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_4_7":
                contributionPeriods_4_7["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_5_7
            if i == "Ingresos_Pago_5_7":
                contributionPeriods_5_7["curAmt"] = diccionario[i]
            if i == "Anio_Pago_5_7":
                contributionPeriods_5_7["expYear"] = diccionario[i]
            if i == "Mes_Pago_5_7":
                contributionPeriods_5_7["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_5_7":
                contributionPeriods_5_7["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_6_7
            if i == "Ingresos_Pago_6_7":
                contributionPeriods_6_7["curAmt"] = diccionario[i]
            if i == "Anio_Pago_6_7":
                contributionPeriods_6_7["expYear"] = diccionario[i]
            if i == "Mes_Pago_6_7":
                contributionPeriods_6_7["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_6_7":
                contributionPeriods_6_7["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_7_7
            if i == "Ingresos_Pago_7_7":
                contributionPeriods_7_7["curAmt"] = diccionario[i]
            if i == "Anio_Pago_7_7":
                contributionPeriods_7_7["expYear"] = diccionario[i]
            if i == "Mes_Pago_7_7":
                contributionPeriods_7_7["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_7_7":
                contributionPeriods_7_7["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_8_7
            if i == "Ingresos_Pago_8_7":
                contributionPeriods_8_7["curAmt"] = diccionario[i]
            if i == "Anio_Pago_8_7":
                contributionPeriods_8_7["expYear"] = diccionario[i]
            if i == "Mes_Pago_8_7":
                contributionPeriods_8_7["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_8_7":
                contributionPeriods_8_7["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_9_7
            if i == "Ingresos_Pago_9_7":
                contributionPeriods_9_7["curAmt"] = diccionario[i]
            if i == "Anio_Pago_9_7":
                contributionPeriods_9_7["expYear"] = diccionario[i]
            if i == "Mes_Pago_9_7":
                contributionPeriods_9_7["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_9_7":
                contributionPeriods_9_7["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_10_7
            if i == "Ingresos_Pago_10_7":
                contributionPeriods_10_7["curAmt"] = diccionario[i]
            if i == "Anio_Pago_10_7":
                contributionPeriods_10_7["expYear"] = diccionario[i]
            if i == "Mes_Pago_10_7":
                contributionPeriods_10_7["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_10_7":
                contributionPeriods_10_7["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_11_7
            if i == "Ingresos_Pago_11_7":
                contributionPeriods_11_7["curAmt"] = diccionario[i]
            if i == "Anio_Pago_11_7":
                contributionPeriods_11_7["expYear"] = diccionario[i]
            if i == "Mes_Pago_11_7":
                contributionPeriods_11_7["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_11_7":
                contributionPeriods_11_7["paymentInd"] = diccionario[i]
            
            #estructura de person.contributionPeriods_12_7
            if i == "Ingresos_Pago_12_7":
                contributionPeriods_12_7["curAmt"] = diccionario[i]
            if i == "Anio_Pago_12_7":
                contributionPeriods_12_7["expYear"] = diccionario[i]
            if i == "Mes_Pago_12_7":
                contributionPeriods_12_7["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_12_7":
                contributionPeriods_12_7["paymentInd"] = diccionario[i]


#######################################################################################################
######################################### EMPLEADOR 8 #################################################
#######################################################################################################


            #estructura de person.contributions_8
            if i == "Tipo_de_documento_del_empleador_8": #puede estar hasta 12 veces
                contributions_8["typeDocument"] = diccionario[i]
            if i == "Numero_de_documento_del_empleador_8":
                contributions_8["numberDocument"] = diccionario[i]
            if i == "Razon_Social_del_empleador_8":
                contributions_8["fullName"] = diccionario[i]
            if i == "Actividad_econ_empleador_8":
                contributions_8["businessType"] = diccionario[i]
            if i == "Descripcion_actividad_empleador_8":
                contributions_8["businessDesc"] = diccionario[i]
            if i == "Clase_aportante_8":
                contributions_8["contributingClass"] = diccionario[i]
            if i == "Tipo_de_Cotizante_empleador_8":
                contributions_8["typeContribution"] = diccionario[i]
            if i == "Piso_Proteccion_Social_8":
                contributions_8["socialProteccion"] = diccionario[i]
            if i == "Tiene_Salario_Integral_Actualmente_empleador_8":
                contributions_8["integralSalary"] = diccionario[i]
            if i == "Tiene_Novedad_Ingreso_Actualmente_empleador_8":
                contributions_8["newEntryFlag"] = diccionario[i]
            if i == "Tiene_Novedad_Retiro_Actualmente_empleado_8":
                contributions_8["retirementEntryFlag"] = diccionario[i]
            if i == "Tiene_Variacion_Temporal_Actualmente_empleador_8":
                contributions_8["temporarySalaryVariationFlag"] = diccionario[i]
            if i == "Tiene_Variacion_Permantente_Actualmente_empleador_8":
                contributions_8["permanentSalaryVariationFlag"] = diccionario[i]
            if i == "Tiene_Licencia_No_Remunerada_Actualmente_empleador_8":
                contributions_8["unpaidLeaveFlag"] = diccionario[i]
            if i == "Nivel_Riesgo_empleador_8":
                contributions_8["riskLevel"] = diccionario[i]
            if i == "Promedio_Ingresos_del_empleador_8":
                contributions_8["averageCurAmt"] = diccionario[i]
            if i == "Mediana_Ingresos_del_empleador_8":
                contributions_8["mediamCurAmt"] = diccionario[i]
            if i == "Ingreso_minimo_del_empleador_8":
                contributions_8["min"] = diccionario[i]
            if i == "Ingreso_maximo_del_empleador_8":
                contributions_8["max"] = diccionario[i]

            #estructura de person.contributionPeriods_1_8
            if i == "Ingresos_Pago_1_8":
                contributionPeriods_1_8["curAmt"] = diccionario[i]
            if i == "Anio_Pago_1_8":
                contributionPeriods_1_8["expYear"] = diccionario[i]
            if i == "Mes_Pago_1_8":
                contributionPeriods_1_8["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_1_8":
                contributionPeriods_1_8["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_2_8
            if i == "Ingresos_Pago_2_8":
                contributionPeriods_2_8["curAmt"] = diccionario[i]
            if i == "Anio_Pago_2_8":
                contributionPeriods_2_8["expYear"] = diccionario[i]
            if i == "Mes_Pago_2_8":
                contributionPeriods_2_8["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_2_8":
                contributionPeriods_2_8["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_3_8
            if i == "Ingresos_Pago_3_8":
                contributionPeriods_3_8["curAmt"] = diccionario[i]
            if i == "Anio_Pago_3_8":
                contributionPeriods_3_8["expYear"] = diccionario[i]
            if i == "Mes_Pago_3_8":
                contributionPeriods_3_8["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_3_8":
                contributionPeriods_3_8["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_4_8
            if i == "Ingresos_Pago_4_8":
                contributionPeriods_4_8["curAmt"] = diccionario[i]
            if i == "Anio_Pago_4_8":
                contributionPeriods_4_8["expYear"] = diccionario[i]
            if i == "Mes_Pago_4_8":
                contributionPeriods_4_8["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_4_8":
                contributionPeriods_4_8["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_5_8
            if i == "Ingresos_Pago_5_8":
                contributionPeriods_5_8["curAmt"] = diccionario[i]
            if i == "Anio_Pago_5_8":
                contributionPeriods_5_8["expYear"] = diccionario[i]
            if i == "Mes_Pago_5_8":
                contributionPeriods_5_8["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_5_8":
                contributionPeriods_5_8["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_6_8
            if i == "Ingresos_Pago_6_8":
                contributionPeriods_6_8["curAmt"] = diccionario[i]
            if i == "Anio_Pago_6_8":
                contributionPeriods_6_8["expYear"] = diccionario[i]
            if i == "Mes_Pago_6_8":
                contributionPeriods_6_8["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_6_8":
                contributionPeriods_6_8["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_7_8
            if i == "Ingresos_Pago_7_8":
                contributionPeriods_7_8["curAmt"] = diccionario[i]
            if i == "Anio_Pago_7_8":
                contributionPeriods_7_8["expYear"] = diccionario[i]
            if i == "Mes_Pago_7_8":
                contributionPeriods_7_8["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_7_8":
                contributionPeriods_7_8["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_8_8
            if i == "Ingresos_Pago_8_8":
                contributionPeriods_8_8["curAmt"] = diccionario[i]
            if i == "Anio_Pago_8_8":
                contributionPeriods_8_8["expYear"] = diccionario[i]
            if i == "Mes_Pago_8_8":
                contributionPeriods_8_8["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_8_8":
                contributionPeriods_8_8["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_9_8
            if i == "Ingresos_Pago_9_8":
                contributionPeriods_9_8["curAmt"] = diccionario[i]
            if i == "Anio_Pago_9_8":
                contributionPeriods_9_8["expYear"] = diccionario[i]
            if i == "Mes_Pago_9_8":
                contributionPeriods_9_8["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_9_8":
                contributionPeriods_9_8["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_10_8
            if i == "Ingresos_Pago_10_8":
                contributionPeriods_10_8["curAmt"] = diccionario[i]
            if i == "Anio_Pago_10_8":
                contributionPeriods_10_8["expYear"] = diccionario[i]
            if i == "Mes_Pago_10_8":
                contributionPeriods_10_8["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_10_8":
                contributionPeriods_10_8["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_11_8
            if i == "Ingresos_Pago_11_8":
                contributionPeriods_11_8["curAmt"] = diccionario[i]
            if i == "Anio_Pago_11_8":
                contributionPeriods_11_8["expYear"] = diccionario[i]
            if i == "Mes_Pago_11_8":
                contributionPeriods_11_8["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_11_8":
                contributionPeriods_11_8["paymentInd"] = diccionario[i]
            
            #estructura de person.contributionPeriods_12_8
            if i == "Ingresos_Pago_12_8":
                contributionPeriods_12_8["curAmt"] = diccionario[i]
            if i == "Anio_Pago_12_8":
                contributionPeriods_12_8["expYear"] = diccionario[i]
            if i == "Mes_Pago_12_8":
                contributionPeriods_12_8["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_12_8":
                contributionPeriods_12_8["paymentInd"] = diccionario[i]

#######################################################################################################
######################################### EMPLEADOR 9 #################################################
#######################################################################################################


            #estructura de person.contributions_9
            if i == "Tipo_de_documento_del_empleador_9": #puede estar hasta 12 veces
                contributions_9["typeDocument"] = diccionario[i]
            if i == "Numero_de_documento_del_empleador_9":
                contributions_9["numberDocument"] = diccionario[i]
            if i == "Razon_Social_del_empleador_9":
                contributions_9["fullName"] = diccionario[i]
            if i == "Actividad_econ_empleador_9":
                contributions_9["businessType"] = diccionario[i]
            if i == "Descripcion_actividad_empleador_9":
                contributions_9["businessDesc"] = diccionario[i]
            if i == "Clase_aportante_9":
                contributions_9["contributingClass"] = diccionario[i]
            if i == "Tipo_de_Cotizante_empleador_9":
                contributions_9["typeContribution"] = diccionario[i]
            if i == "Piso_Proteccion_Social_9":
                contributions_9["socialProteccion"] = diccionario[i]
            if i == "Tiene_Salario_Integral_Actualmente_empleador_9":
                contributions_9["integralSalary"] = diccionario[i]
            if i == "Tiene_Novedad_Ingreso_Actualmente_empleador_9":
                contributions_9["newEntryFlag"] = diccionario[i]
            if i == "Tiene_Novedad_Retiro_Actualmente_empleado_9":
                contributions_9["retirementEntryFlag"] = diccionario[i]
            if i == "Tiene_Variacion_Temporal_Actualmente_empleador_9":
                contributions_9["temporarySalaryVariationFlag"] = diccionario[i]
            if i == "Tiene_Variacion_Permantente_Actualmente_empleador_9":
                contributions_9["permanentSalaryVariationFlag"] = diccionario[i]
            if i == "Tiene_Licencia_No_Remunerada_Actualmente_empleador_9":
                contributions_9["unpaidLeaveFlag"] = diccionario[i]
            if i == "Nivel_Riesgo_empleador_9":
                contributions_9["riskLevel"] = diccionario[i]
            if i == "Promedio_Ingresos_del_empleador_9":
                contributions_9["averageCurAmt"] = diccionario[i]
            if i == "Mediana_Ingresos_del_empleador_9":
                contributions_9["mediamCurAmt"] = diccionario[i]
            if i == "Ingreso_minimo_del_empleador_9":
                contributions_9["min"] = diccionario[i]
            if i == "Ingreso_maximo_del_empleador_9":
                contributions_9["max"] = diccionario[i]

            #estructura de person.contributionPeriods_1_9
            if i == "Ingresos_Pago_1_9":
                contributionPeriods_1_9["curAmt"] = diccionario[i]
            if i == "Anio_Pago_1_9":
                contributionPeriods_1_9["expYear"] = diccionario[i]
            if i == "Mes_Pago_1_9":
                contributionPeriods_1_9["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_1_9":
                contributionPeriods_1_9["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_2_9
            if i == "Ingresos_Pago_2_9":
                contributionPeriods_2_9["curAmt"] = diccionario[i]
            if i == "Anio_Pago_2_9":
                contributionPeriods_2_9["expYear"] = diccionario[i]
            if i == "Mes_Pago_2_9":
                contributionPeriods_2_9["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_2_9":
                contributionPeriods_2_9["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_3_9
            if i == "Ingresos_Pago_3_9":
                contributionPeriods_3_9["curAmt"] = diccionario[i]
            if i == "Anio_Pago_3_9":
                contributionPeriods_3_9["expYear"] = diccionario[i]
            if i == "Mes_Pago_3_9":
                contributionPeriods_3_9["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_3_9":
                contributionPeriods_3_9["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_4_9
            if i == "Ingresos_Pago_4_9":
                contributionPeriods_4_9["curAmt"] = diccionario[i]
            if i == "Anio_Pago_4_9":
                contributionPeriods_4_9["expYear"] = diccionario[i]
            if i == "Mes_Pago_4_9":
                contributionPeriods_4_9["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_4_9":
                contributionPeriods_4_9["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_5_9
            if i == "Ingresos_Pago_5_9":
                contributionPeriods_5_9["curAmt"] = diccionario[i]
            if i == "Anio_Pago_5_9":
                contributionPeriods_5_9["expYear"] = diccionario[i]
            if i == "Mes_Pago_5_9":
                contributionPeriods_5_9["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_5_9":
                contributionPeriods_5_9["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_6_9
            if i == "Ingresos_Pago_6_9":
                contributionPeriods_6_9["curAmt"] = diccionario[i]
            if i == "Anio_Pago_6_9":
                contributionPeriods_6_9["expYear"] = diccionario[i]
            if i == "Mes_Pago_6_9":
                contributionPeriods_6_9["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_6_9":
                contributionPeriods_6_9["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_7_9
            if i == "Ingresos_Pago_7_9":
                contributionPeriods_7_9["curAmt"] = diccionario[i]
            if i == "Anio_Pago_7_9":
                contributionPeriods_7_9["expYear"] = diccionario[i]
            if i == "Mes_Pago_7_9":
                contributionPeriods_7_9["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_7_9":
                contributionPeriods_7_9["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_8_9
            if i == "Ingresos_Pago_8_9":
                contributionPeriods_8_9["curAmt"] = diccionario[i]
            if i == "Anio_Pago_8_9":
                contributionPeriods_8_9["expYear"] = diccionario[i]
            if i == "Mes_Pago_8_9":
                contributionPeriods_8_9["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_8_9":
                contributionPeriods_8_9["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_9_9
            if i == "Ingresos_Pago_9_9":
                contributionPeriods_9_9["curAmt"] = diccionario[i]
            if i == "Anio_Pago_9_9":
                contributionPeriods_9_9["expYear"] = diccionario[i]
            if i == "Mes_Pago_9_9":
                contributionPeriods_9_9["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_9_9":
                contributionPeriods_9_9["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_10_9
            if i == "Ingresos_Pago_10_9":
                contributionPeriods_10_9["curAmt"] = diccionario[i]
            if i == "Anio_Pago_10_9":
                contributionPeriods_10_9["expYear"] = diccionario[i]
            if i == "Mes_Pago_10_9":
                contributionPeriods_10_9["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_10_9":
                contributionPeriods_10_9["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_11_9
            if i == "Ingresos_Pago_11_9":
                contributionPeriods_11_9["curAmt"] = diccionario[i]
            if i == "Anio_Pago_11_9":
                contributionPeriods_11_9["expYear"] = diccionario[i]
            if i == "Mes_Pago_11_9":
                contributionPeriods_11_9["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_11_9":
                contributionPeriods_11_9["paymentInd"] = diccionario[i]
            
            #estructura de person.contributionPeriods_12_9
            if i == "Ingresos_Pago_12_9":
                contributionPeriods_12_9["curAmt"] = diccionario[i]
            if i == "Anio_Pago_12_9":
                contributionPeriods_12_9["expYear"] = diccionario[i]
            if i == "Mes_Pago_12_9":
                contributionPeriods_12_9["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_12_9":
                contributionPeriods_12_9["paymentInd"] = diccionario[i]
        
#######################################################################################################
######################################### EMPLEADOR 10 #################################################
#######################################################################################################


            #estructura de person.contributions_10
            if i == "Tipo_de_documento_del_empleador_10": #puede estar hasta 12 veces
                contributions_10["typeDocument"] = diccionario[i]
            if i == "Numero_de_documento_del_empleador_10":
                contributions_10["numberDocument"] = diccionario[i]
            if i == "Razon_Social_del_empleador_10":
                contributions_10["fullName"] = diccionario[i]
            if i == "Actividad_econ_empleador_10":
                contributions_10["businessType"] = diccionario[i]
            if i == "Descripcion_actividad_empleador_10":
                contributions_10["businessDesc"] = diccionario[i]
            if i == "Clase_aportante_10":
                contributions_10["contributingClass"] = diccionario[i]
            if i == "Tipo_de_Cotizante_empleador_10":
                contributions_10["typeContribution"] = diccionario[i]
            if i == "Piso_Proteccion_Social_10":
                contributions_10["socialProteccion"] = diccionario[i]
            if i == "Tiene_Salario_Integral_Actualmente_empleador_10":
                contributions_10["integralSalary"] = diccionario[i]
            if i == "Tiene_Novedad_Ingreso_Actualmente_empleador_10":
                contributions_10["newEntryFlag"] = diccionario[i]
            if i == "Tiene_Novedad_Retiro_Actualmente_empleado_10":
                contributions_10["retirementEntryFlag"] = diccionario[i]
            if i == "Tiene_Variacion_Temporal_Actualmente_empleador_10":
                contributions_10["temporarySalaryVariationFlag"] = diccionario[i]
            if i == "Tiene_Variacion_Permantente_Actualmente_empleador_10":
                contributions_10["permanentSalaryVariationFlag"] = diccionario[i]
            if i == "Tiene_Licencia_No_Remunerada_Actualmente_empleador_10":
                contributions_10["unpaidLeaveFlag"] = diccionario[i]
            if i == "Nivel_Riesgo_empleador_10":
                contributions_10["riskLevel"] = diccionario[i]
            if i == "Promedio_Ingresos_del_empleador_10":
                contributions_10["averageCurAmt"] = diccionario[i]
            if i == "Mediana_Ingresos_del_empleador_10":
                contributions_10["mediamCurAmt"] = diccionario[i]
            if i == "Ingreso_minimo_del_empleador_10":
                contributions_10["min"] = diccionario[i]
            if i == "Ingreso_maximo_del_empleador_10":
                contributions_10["max"] = diccionario[i]

            #estructura de person.contributionPeriods_1_10
            if i == "Ingresos_Pago_1_10":
                contributionPeriods_1_10["curAmt"] = diccionario[i]
            if i == "Anio_Pago_1_10":
                contributionPeriods_1_10["expYear"] = diccionario[i]
            if i == "Mes_Pago_1_10":
                contributionPeriods_1_10["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_1_10":
                contributionPeriods_1_10["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_2_10
            if i == "Ingresos_Pago_2_10":
                contributionPeriods_2_10["curAmt"] = diccionario[i]
            if i == "Anio_Pago_2_10":
                contributionPeriods_2_10["expYear"] = diccionario[i]
            if i == "Mes_Pago_2_10":
                contributionPeriods_2_10["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_2_10":
                contributionPeriods_2_10["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_3_10
            if i == "Ingresos_Pago_3_10":
                contributionPeriods_3_10["curAmt"] = diccionario[i]
            if i == "Anio_Pago_3_10":
                contributionPeriods_3_10["expYear"] = diccionario[i]
            if i == "Mes_Pago_3_10":
                contributionPeriods_3_10["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_3_10":
                contributionPeriods_3_10["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_4_10
            if i == "Ingresos_Pago_4_10":
                contributionPeriods_4_10["curAmt"] = diccionario[i]
            if i == "Anio_Pago_4_10":
                contributionPeriods_4_10["expYear"] = diccionario[i]
            if i == "Mes_Pago_4_10":
                contributionPeriods_4_10["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_4_10":
                contributionPeriods_4_10["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_5_10
            if i == "Ingresos_Pago_5_10":
                contributionPeriods_5_10["curAmt"] = diccionario[i]
            if i == "Anio_Pago_5_10":
                contributionPeriods_5_10["expYear"] = diccionario[i]
            if i == "Mes_Pago_5_10":
                contributionPeriods_5_10["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_5_10":
                contributionPeriods_5_10["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_6_10
            if i == "Ingresos_Pago_6_10":
                contributionPeriods_6_10["curAmt"] = diccionario[i]
            if i == "Anio_Pago_6_10":
                contributionPeriods_6_10["expYear"] = diccionario[i]
            if i == "Mes_Pago_6_10":
                contributionPeriods_6_10["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_6_10":
                contributionPeriods_6_10["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_7_10
            if i == "Ingresos_Pago_7_10":
                contributionPeriods_7_10["curAmt"] = diccionario[i]
            if i == "Anio_Pago_7_10":
                contributionPeriods_7_10["expYear"] = diccionario[i]
            if i == "Mes_Pago_7_10":
                contributionPeriods_7_10["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_7_10":
                contributionPeriods_7_10["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_8_10
            if i == "Ingresos_Pago_8_10":
                contributionPeriods_8_10["curAmt"] = diccionario[i]
            if i == "Anio_Pago_8_10":
                contributionPeriods_8_10["expYear"] = diccionario[i]
            if i == "Mes_Pago_8_10":
                contributionPeriods_8_10["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_8_10":
                contributionPeriods_8_10["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_9_10
            if i == "Ingresos_Pago_9_10":
                contributionPeriods_9_10["curAmt"] = diccionario[i]
            if i == "Anio_Pago_9_10":
                contributionPeriods_9_10["expYear"] = diccionario[i]
            if i == "Mes_Pago_9_10":
                contributionPeriods_9_10["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_9_10":
                contributionPeriods_9_10["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_10_10
            if i == "Ingresos_Pago_10_10":
                contributionPeriods_10_10["curAmt"] = diccionario[i]
            if i == "Anio_Pago_10_10":
                contributionPeriods_10_10["expYear"] = diccionario[i]
            if i == "Mes_Pago_10_10":
                contributionPeriods_10_10["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_10_10":
                contributionPeriods_10_10["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_11_10
            if i == "Ingresos_Pago_11_10":
                contributionPeriods_11_10["curAmt"] = diccionario[i]
            if i == "Anio_Pago_11_10":
                contributionPeriods_11_10["expYear"] = diccionario[i]
            if i == "Mes_Pago_11_10":
                contributionPeriods_11_10["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_11_10":
                contributionPeriods_11_10["paymentInd"] = diccionario[i]
            
            #estructura de person.contributionPeriods_12_10
            if i == "Ingresos_Pago_12_10":
                contributionPeriods_12_10["curAmt"] = diccionario[i]
            if i == "Anio_Pago_12_10":
                contributionPeriods_12_10["expYear"] = diccionario[i]
            if i == "Mes_Pago_12_10":
                contributionPeriods_12_10["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_12_10":
                contributionPeriods_12_10["paymentInd"] = diccionario[i]

#######################################################################################################
######################################### EMPLEADOR 11 #################################################
#######################################################################################################


            #estructura de person.contributions_11
            if i == "Tipo_de_documento_del_empleador_11": #puede estar hasta 12 veces
                contributions_11["typeDocument"] = diccionario[i]
            if i == "Numero_de_documento_del_empleador_11":
                contributions_11["numberDocument"] = diccionario[i]
            if i == "Razon_Social_del_empleador_11":
                contributions_11["fullName"] = diccionario[i]
            if i == "Actividad_econ_empleador_11":
                contributions_11["businessType"] = diccionario[i]
            if i == "Descripcion_actividad_empleador_11":
                contributions_11["businessDesc"] = diccionario[i]
            if i == "Clase_aportante_11":
                contributions_11["contributingClass"] = diccionario[i]
            if i == "Tipo_de_Cotizante_empleador_11":
                contributions_11["typeContribution"] = diccionario[i]
            if i == "Piso_Proteccion_Social_11":
                contributions_11["socialProteccion"] = diccionario[i]
            if i == "Tiene_Salario_Integral_Actualmente_empleador_11":
                contributions_11["integralSalary"] = diccionario[i]
            if i == "Tiene_Novedad_Ingreso_Actualmente_empleador_11":
                contributions_11["newEntryFlag"] = diccionario[i]
            if i == "Tiene_Novedad_Retiro_Actualmente_empleado_11":
                contributions_11["retirementEntryFlag"] = diccionario[i]
            if i == "Tiene_Variacion_Temporal_Actualmente_empleador_11":
                contributions_11["temporarySalaryVariationFlag"] = diccionario[i]
            if i == "Tiene_Variacion_Permantente_Actualmente_empleador_11":
                contributions_11["permanentSalaryVariationFlag"] = diccionario[i]
            if i == "Tiene_Licencia_No_Remunerada_Actualmente_empleador_11":
                contributions_11["unpaidLeaveFlag"] = diccionario[i]
            if i == "Nivel_Riesgo_empleador_11":
                contributions_11["riskLevel"] = diccionario[i]
            if i == "Promedio_Ingresos_del_empleador_11":
                contributions_11["averageCurAmt"] = diccionario[i]
            if i == "Mediana_Ingresos_del_empleador_11":
                contributions_11["mediamCurAmt"] = diccionario[i]
            if i == "Ingreso_minimo_del_empleador_11":
                contributions_11["min"] = diccionario[i]
            if i == "Ingreso_maximo_del_empleador_11":
                contributions_11["max"] = diccionario[i]

            #estructura de person.contributionPeriods_1_11
            if i == "Ingresos_Pago_1_11":
                contributionPeriods_1_11["curAmt"] = diccionario[i]
            if i == "Anio_Pago_1_11":
                contributionPeriods_1_11["expYear"] = diccionario[i]
            if i == "Mes_Pago_1_11":
                contributionPeriods_1_11["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_1_11":
                contributionPeriods_1_11["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_2_11
            if i == "Ingresos_Pago_2_11":
                contributionPeriods_2_11["curAmt"] = diccionario[i]
            if i == "Anio_Pago_2_11":
                contributionPeriods_2_11["expYear"] = diccionario[i]
            if i == "Mes_Pago_2_11":
                contributionPeriods_2_11["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_2_11":
                contributionPeriods_2_11["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_3_11
            if i == "Ingresos_Pago_3_11":
                contributionPeriods_3_11["curAmt"] = diccionario[i]
            if i == "Anio_Pago_3_11":
                contributionPeriods_3_11["expYear"] = diccionario[i]
            if i == "Mes_Pago_3_11":
                contributionPeriods_3_11["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_3_11":
                contributionPeriods_3_11["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_4_11
            if i == "Ingresos_Pago_4_11":
                contributionPeriods_4_11["curAmt"] = diccionario[i]
            if i == "Anio_Pago_4_11":
                contributionPeriods_4_11["expYear"] = diccionario[i]
            if i == "Mes_Pago_4_11":
                contributionPeriods_4_11["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_4_11":
                contributionPeriods_4_11["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_5_11
            if i == "Ingresos_Pago_5_11":
                contributionPeriods_5_11["curAmt"] = diccionario[i]
            if i == "Anio_Pago_5_11":
                contributionPeriods_5_11["expYear"] = diccionario[i]
            if i == "Mes_Pago_5_11":
                contributionPeriods_5_11["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_5_11":
                contributionPeriods_5_11["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_6_11
            if i == "Ingresos_Pago_6_11":
                contributionPeriods_6_11["curAmt"] = diccionario[i]
            if i == "Anio_Pago_6_11":
                contributionPeriods_6_11["expYear"] = diccionario[i]
            if i == "Mes_Pago_6_11":
                contributionPeriods_6_11["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_6_11":
                contributionPeriods_6_11["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_7_11
            if i == "Ingresos_Pago_7_11":
                contributionPeriods_7_11["curAmt"] = diccionario[i]
            if i == "Anio_Pago_7_11":
                contributionPeriods_7_11["expYear"] = diccionario[i]
            if i == "Mes_Pago_7_11":
                contributionPeriods_7_11["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_7_11":
                contributionPeriods_7_11["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_8_11
            if i == "Ingresos_Pago_8_11":
                contributionPeriods_8_11["curAmt"] = diccionario[i]
            if i == "Anio_Pago_8_11":
                contributionPeriods_8_11["expYear"] = diccionario[i]
            if i == "Mes_Pago_8_11":
                contributionPeriods_8_11["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_8_11":
                contributionPeriods_8_11["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_9_11
            if i == "Ingresos_Pago_9_11":
                contributionPeriods_9_11["curAmt"] = diccionario[i]
            if i == "Anio_Pago_9_11":
                contributionPeriods_9_11["expYear"] = diccionario[i]
            if i == "Mes_Pago_9_11":
                contributionPeriods_9_11["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_9_11":
                contributionPeriods_9_11["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_10_11
            if i == "Ingresos_Pago_10_11":
                contributionPeriods_10_11["curAmt"] = diccionario[i]
            if i == "Anio_Pago_10_11":
                contributionPeriods_10_11["expYear"] = diccionario[i]
            if i == "Mes_Pago_10_11":
                contributionPeriods_10_11["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_10_11":
                contributionPeriods_10_11["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_11_11
            if i == "Ingresos_Pago_11_11":
                contributionPeriods_11_11["curAmt"] = diccionario[i]
            if i == "Anio_Pago_11_11":
                contributionPeriods_11_11["expYear"] = diccionario[i]
            if i == "Mes_Pago_11_11":
                contributionPeriods_11_11["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_11_11":
                contributionPeriods_11_11["paymentInd"] = diccionario[i]
            
            #estructura de person.contributionPeriods_12_11
            if i == "Ingresos_Pago_12_11":
                contributionPeriods_12_11["curAmt"] = diccionario[i]
            if i == "Anio_Pago_12_11":
                contributionPeriods_12_11["expYear"] = diccionario[i]
            if i == "Mes_Pago_12_11":
                contributionPeriods_12_11["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_12_11":
                contributionPeriods_12_11["paymentInd"] = diccionario[i]

#######################################################################################################
######################################### EMPLEADOR 12 #################################################
#######################################################################################################


            #estructura de person.contributions_12
            if i == "Tipo_de_documento_del_empleador_12": #puede estar hasta 12 veces
                contributions_12["typeDocument"] = diccionario[i]
            if i == "Numero_de_documento_del_empleador_12":
                contributions_12["numberDocument"] = diccionario[i]
            if i == "Razon_Social_del_empleador_12":
                contributions_12["fullName"] = diccionario[i]
            if i == "Actividad_econ_empleador_12":
                contributions_12["businessType"] = diccionario[i]
            if i == "Descripcion_actividad_empleador_12":
                contributions_12["businessDesc"] = diccionario[i]
            if i == "Clase_aportante_12":
                contributions_12["contributingClass"] = diccionario[i]
            if i == "Tipo_de_Cotizante_empleador_12":
                contributions_12["typeContribution"] = diccionario[i]
            if i == "Piso_Proteccion_Social_12":
                contributions_12["socialProteccion"] = diccionario[i]
            if i == "Tiene_Salario_Integral_Actualmente_empleador_12":
                contributions_12["integralSalary"] = diccionario[i]
            if i == "Tiene_Novedad_Ingreso_Actualmente_empleador_12":
                contributions_12["newEntryFlag"] = diccionario[i]
            if i == "Tiene_Novedad_Retiro_Actualmente_empleado_12":
                contributions_12["retirementEntryFlag"] = diccionario[i]
            if i == "Tiene_Variacion_Temporal_Actualmente_empleador_12":
                contributions_12["temporarySalaryVariationFlag"] = diccionario[i]
            if i == "Tiene_Variacion_Permantente_Actualmente_empleador_12":
                contributions_12["permanentSalaryVariationFlag"] = diccionario[i]
            if i == "Tiene_Licencia_No_Remunerada_Actualmente_empleador_12":
                contributions_12["unpaidLeaveFlag"] = diccionario[i]
            if i == "Nivel_Riesgo_empleador_12":
                contributions_12["riskLevel"] = diccionario[i]
            if i == "Promedio_Ingresos_del_empleador_12":
                contributions_12["averageCurAmt"] = diccionario[i]
            if i == "Mediana_Ingresos_del_empleador_12":
                contributions_12["mediamCurAmt"] = diccionario[i]
            if i == "Ingreso_minimo_del_empleador_12":
                contributions_12["min"] = diccionario[i]
            if i == "Ingreso_maximo_del_empleador_12":
                contributions_12["max"] = diccionario[i]

            #estructura de person.contributionPeriods_1_12
            if i == "Ingresos_Pago_1_12":
                contributionPeriods_1_12["curAmt"] = diccionario[i]
            if i == "Anio_Pago_1_12":
                contributionPeriods_1_12["expYear"] = diccionario[i]
            if i == "Mes_Pago_1_12":
                contributionPeriods_1_12["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_1_12":
                contributionPeriods_1_12["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_2_12
            if i == "Ingresos_Pago_2_12":
                contributionPeriods_2_12["curAmt"] = diccionario[i]
            if i == "Anio_Pago_2_12":
                contributionPeriods_2_12["expYear"] = diccionario[i]
            if i == "Mes_Pago_2_12":
                contributionPeriods_2_12["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_2_12":
                contributionPeriods_2_12["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_3_12
            if i == "Ingresos_Pago_3_12":
                contributionPeriods_3_12["curAmt"] = diccionario[i]
            if i == "Anio_Pago_3_12":
                contributionPeriods_3_12["expYear"] = diccionario[i]
            if i == "Mes_Pago_3_12":
                contributionPeriods_3_12["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_3_12":
                contributionPeriods_3_12["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_4_12
            if i == "Ingresos_Pago_4_12":
                contributionPeriods_4_12["curAmt"] = diccionario[i]
            if i == "Anio_Pago_4_12":
                contributionPeriods_4_12["expYear"] = diccionario[i]
            if i == "Mes_Pago_4_12":
                contributionPeriods_4_12["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_4_12":
                contributionPeriods_4_12["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_5_12
            if i == "Ingresos_Pago_5_12":
                contributionPeriods_5_12["curAmt"] = diccionario[i]
            if i == "Anio_Pago_5_12":
                contributionPeriods_5_12["expYear"] = diccionario[i]
            if i == "Mes_Pago_5_12":
                contributionPeriods_5_12["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_5_12":
                contributionPeriods_5_12["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_6_12
            if i == "Ingresos_Pago_6_12":
                contributionPeriods_6_12["curAmt"] = diccionario[i]
            if i == "Anio_Pago_6_12":
                contributionPeriods_6_12["expYear"] = diccionario[i]
            if i == "Mes_Pago_6_12":
                contributionPeriods_6_12["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_6_12":
                contributionPeriods_6_12["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_7_12
            if i == "Ingresos_Pago_7_12":
                contributionPeriods_7_12["curAmt"] = diccionario[i]
            if i == "Anio_Pago_7_12":
                contributionPeriods_7_12["expYear"] = diccionario[i]
            if i == "Mes_Pago_7_12":
                contributionPeriods_7_12["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_7_12":
                contributionPeriods_7_12["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_8_12
            if i == "Ingresos_Pago_8_12":
                contributionPeriods_8_12["curAmt"] = diccionario[i]
            if i == "Anio_Pago_8_12":
                contributionPeriods_8_12["expYear"] = diccionario[i]
            if i == "Mes_Pago_8_12":
                contributionPeriods_8_12["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_8_12":
                contributionPeriods_8_12["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_9_12
            if i == "Ingresos_Pago_9_12":
                contributionPeriods_9_12["curAmt"] = diccionario[i]
            if i == "Anio_Pago_9_12":
                contributionPeriods_9_12["expYear"] = diccionario[i]
            if i == "Mes_Pago_9_12":
                contributionPeriods_9_12["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_9_12":
                contributionPeriods_9_12["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_10_12
            if i == "Ingresos_Pago_10_12":
                contributionPeriods_10_12["curAmt"] = diccionario[i]
            if i == "Anio_Pago_10_12":
                contributionPeriods_10_12["expYear"] = diccionario[i]
            if i == "Mes_Pago_10_12":
                contributionPeriods_10_12["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_10_12":
                contributionPeriods_10_12["paymentInd"] = diccionario[i]

            #estructura de person.contributionPeriods_11_12
            if i == "Ingresos_Pago_11_12":
                contributionPeriods_11_12["curAmt"] = diccionario[i]
            if i == "Anio_Pago_11_12":
                contributionPeriods_11_12["expYear"] = diccionario[i]
            if i == "Mes_Pago_11_12":
                contributionPeriods_11_12["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_11_12":
                contributionPeriods_11_12["paymentInd"] = diccionario[i]
            
            #estructura de person.contributionPeriods_12_12
            if i == "Ingresos_Pago_12_12":
                contributionPeriods_12_12["curAmt"] = diccionario[i]
            if i == "Anio_Pago_12_12":
                contributionPeriods_12_12["expYear"] = diccionario[i]
            if i == "Mes_Pago_12_12":
                contributionPeriods_12_12["expMonth"] = diccionario[i]
            if i == "Pago_Realizado_12_12":
                contributionPeriods_12_12["paymentInd"] = diccionario[i]

#############################################################################################################
####################################### EMPLEADOR 1 #########################################################
#############################################################################################################
        est_contr_1 = {}
        
        contributionPeriods_cont_1 = []

        contributionPeriods_cont_1.append(contributionPeriods_1.copy())
        contributionPeriods_cont_1.append(contributionPeriods_2.copy())
        contributionPeriods_cont_1.append(contributionPeriods_3.copy())
        contributionPeriods_cont_1.append(contributionPeriods_4.copy())
        contributionPeriods_cont_1.append(contributionPeriods_5.copy())
        contributionPeriods_cont_1.append(contributionPeriods_6.copy())
        contributionPeriods_cont_1.append(contributionPeriods_7.copy())
        contributionPeriods_cont_1.append(contributionPeriods_8.copy())
        contributionPeriods_cont_1.append(contributionPeriods_9.copy())
        contributionPeriods_cont_1.append(contributionPeriods_10.copy())
        contributionPeriods_cont_1.append(contributionPeriods_11.copy())
        contributionPeriods_cont_1.append(contributionPeriods_12.copy())
        
        est_contr_1 ["contributions"] = contributions_1
        est_contr_1 ["contributions"]["contributionPeriods"] = contributionPeriods_cont_1

        contr_1 = est_contr_1["contributions"]

        #print (contr_1)

#############################################################################################################
####################################### EMPLEADOR 2 #########################################################
#############################################################################################################

        est_contr_2 = {}
        
        contributionPeriods_cont_2 = []

        contributionPeriods_cont_2.append(contributionPeriods_1_2.copy())
        contributionPeriods_cont_2.append(contributionPeriods_2_2.copy())
        contributionPeriods_cont_2.append(contributionPeriods_3_2.copy())
        contributionPeriods_cont_2.append(contributionPeriods_4_2.copy())
        contributionPeriods_cont_2.append(contributionPeriods_5_2.copy())
        contributionPeriods_cont_2.append(contributionPeriods_6_2.copy())
        contributionPeriods_cont_2.append(contributionPeriods_7_2.copy())
        contributionPeriods_cont_2.append(contributionPeriods_8_2.copy())
        contributionPeriods_cont_2.append(contributionPeriods_9_2.copy())
        contributionPeriods_cont_2.append(contributionPeriods_10_2.copy())
        contributionPeriods_cont_2.append(contributionPeriods_11_2.copy())
        contributionPeriods_cont_2.append(contributionPeriods_12_2.copy())

        est_contr_2 ["contributions"] = contributions_2
        est_contr_2 ["contributions"]["contributionPeriods"] = contributionPeriods_cont_2

        contr_2 = est_contr_2["contributions"]

#############################################################################################################
####################################### EMPLEADOR 3 #########################################################
#############################################################################################################
        est_contr_3 = {}
        
        contributionPeriods_cont_3 = []

        contributionPeriods_cont_3.append(contributionPeriods_1_3.copy())
        contributionPeriods_cont_3.append(contributionPeriods_2_3.copy())
        contributionPeriods_cont_3.append(contributionPeriods_3_3.copy())
        contributionPeriods_cont_3.append(contributionPeriods_4_3.copy())
        contributionPeriods_cont_3.append(contributionPeriods_5_3.copy())
        contributionPeriods_cont_3.append(contributionPeriods_6_3.copy())
        contributionPeriods_cont_3.append(contributionPeriods_7_3.copy())
        contributionPeriods_cont_3.append(contributionPeriods_8_3.copy())
        contributionPeriods_cont_3.append(contributionPeriods_9_3.copy())
        contributionPeriods_cont_3.append(contributionPeriods_10_3.copy())
        contributionPeriods_cont_3.append(contributionPeriods_11_3.copy())
        contributionPeriods_cont_3.append(contributionPeriods_12_3.copy())

        est_contr_3 ["contributions"] = contributions_3
        est_contr_3 ["contributions"]["contributionPeriods"] = contributionPeriods_cont_3

        contr_3 = est_contr_3["contributions"]

#############################################################################################################
####################################### EMPLEADOR 4 #########################################################
#############################################################################################################
        est_contr_4 = {}
        
        contributionPeriods_cont_4 = []

        contributionPeriods_cont_4.append(contributionPeriods_1_4.copy())
        contributionPeriods_cont_4.append(contributionPeriods_2_4.copy())
        contributionPeriods_cont_4.append(contributionPeriods_3_4.copy())
        contributionPeriods_cont_4.append(contributionPeriods_4_4.copy())
        contributionPeriods_cont_4.append(contributionPeriods_5_4.copy())
        contributionPeriods_cont_4.append(contributionPeriods_6_4.copy())
        contributionPeriods_cont_4.append(contributionPeriods_7_4.copy())
        contributionPeriods_cont_4.append(contributionPeriods_8_4.copy())
        contributionPeriods_cont_4.append(contributionPeriods_9_4.copy())
        contributionPeriods_cont_4.append(contributionPeriods_10_4.copy())
        contributionPeriods_cont_4.append(contributionPeriods_11_4.copy())
        contributionPeriods_cont_4.append(contributionPeriods_12_4.copy())

        est_contr_4 ["contributions"] = contributions_4
        est_contr_4 ["contributions"]["contributionPeriods"] = contributionPeriods_cont_4

        contr_4 = est_contr_4["contributions"]

#############################################################################################################
####################################### EMPLEADOR 5 #########################################################
#############################################################################################################
        est_contr_5 = {}
        
        contributionPeriods_cont_5 = []

        contributionPeriods_cont_5.append(contributionPeriods_1_5.copy())
        contributionPeriods_cont_5.append(contributionPeriods_2_5.copy())
        contributionPeriods_cont_5.append(contributionPeriods_3_5.copy())
        contributionPeriods_cont_5.append(contributionPeriods_4_5.copy())
        contributionPeriods_cont_5.append(contributionPeriods_5_5.copy())
        contributionPeriods_cont_5.append(contributionPeriods_6_5.copy())
        contributionPeriods_cont_5.append(contributionPeriods_7_5.copy())
        contributionPeriods_cont_5.append(contributionPeriods_8_5.copy())
        contributionPeriods_cont_5.append(contributionPeriods_9_5.copy())
        contributionPeriods_cont_5.append(contributionPeriods_10_5.copy())
        contributionPeriods_cont_5.append(contributionPeriods_11_5.copy())
        contributionPeriods_cont_5.append(contributionPeriods_12_5.copy())

        est_contr_5 ["contributions"] = contributions_5
        est_contr_5 ["contributions"]["contributionPeriods"] = contributionPeriods_cont_5

        contr_5 = est_contr_5["contributions"]

#############################################################################################################
####################################### EMPLEADOR 6 #########################################################
#############################################################################################################
        est_contr_6 = {}
        
        contributionPeriods_cont_6 = []

        contributionPeriods_cont_6.append(contributionPeriods_1_6.copy())
        contributionPeriods_cont_6.append(contributionPeriods_2_6.copy())
        contributionPeriods_cont_6.append(contributionPeriods_3_6.copy())
        contributionPeriods_cont_6.append(contributionPeriods_4_6.copy())
        contributionPeriods_cont_6.append(contributionPeriods_5_6.copy())
        contributionPeriods_cont_6.append(contributionPeriods_6_6.copy())
        contributionPeriods_cont_6.append(contributionPeriods_7_6.copy())
        contributionPeriods_cont_6.append(contributionPeriods_8_6.copy())
        contributionPeriods_cont_6.append(contributionPeriods_9_6.copy())
        contributionPeriods_cont_6.append(contributionPeriods_10_6.copy())
        contributionPeriods_cont_6.append(contributionPeriods_11_6.copy())
        contributionPeriods_cont_6.append(contributionPeriods_12_6.copy())

        est_contr_6 ["contributions"] = contributions_6
        est_contr_6 ["contributions"]["contributionPeriods"] = contributionPeriods_cont_6

        contr_6 = est_contr_6["contributions"]

#############################################################################################################
####################################### EMPLEADOR 7 #########################################################
#############################################################################################################
        est_contr_7 = {}
        
        contributionPeriods_cont_7 = []

        contributionPeriods_cont_7.append(contributionPeriods_1_7.copy())
        contributionPeriods_cont_7.append(contributionPeriods_2_7.copy())
        contributionPeriods_cont_7.append(contributionPeriods_3_7.copy())
        contributionPeriods_cont_7.append(contributionPeriods_4_7.copy())
        contributionPeriods_cont_7.append(contributionPeriods_5_7.copy())
        contributionPeriods_cont_7.append(contributionPeriods_6_7.copy())
        contributionPeriods_cont_7.append(contributionPeriods_7_7.copy())
        contributionPeriods_cont_7.append(contributionPeriods_8_7.copy())
        contributionPeriods_cont_7.append(contributionPeriods_9_7.copy())
        contributionPeriods_cont_7.append(contributionPeriods_10_7.copy())
        contributionPeriods_cont_7.append(contributionPeriods_11_7.copy())
        contributionPeriods_cont_7.append(contributionPeriods_12_7.copy())

        est_contr_7 ["contributions"] = contributions_7
        est_contr_7 ["contributions"]["contributionPeriods"] = contributionPeriods_cont_7

        contr_7 = est_contr_7["contributions"]

#############################################################################################################
####################################### EMPLEADOR 8 #########################################################
#############################################################################################################
        est_contr_8 = {}
        
        contributionPeriods_cont_8 = []

        contributionPeriods_cont_8.append(contributionPeriods_1_8.copy())
        contributionPeriods_cont_8.append(contributionPeriods_2_8.copy())
        contributionPeriods_cont_8.append(contributionPeriods_3_8.copy())
        contributionPeriods_cont_8.append(contributionPeriods_4_8.copy())
        contributionPeriods_cont_8.append(contributionPeriods_5_8.copy())
        contributionPeriods_cont_8.append(contributionPeriods_6_8.copy())
        contributionPeriods_cont_8.append(contributionPeriods_7_8.copy())
        contributionPeriods_cont_8.append(contributionPeriods_8_8.copy())
        contributionPeriods_cont_8.append(contributionPeriods_9_8.copy())
        contributionPeriods_cont_8.append(contributionPeriods_10_8.copy())
        contributionPeriods_cont_8.append(contributionPeriods_11_8.copy())
        contributionPeriods_cont_8.append(contributionPeriods_12_8.copy())

        est_contr_8 ["contributions"] = contributions_8
        est_contr_8 ["contributions"]["contributionPeriods"] = contributionPeriods_cont_8

        contr_8 = est_contr_8["contributions"]

#############################################################################################################
####################################### EMPLEADOR 9 #########################################################
#############################################################################################################
        est_contr_9 = {}
        
        contributionPeriods_cont_9 = []

        contributionPeriods_cont_9.append(contributionPeriods_1_9.copy())
        contributionPeriods_cont_9.append(contributionPeriods_2_9.copy())
        contributionPeriods_cont_9.append(contributionPeriods_3_9.copy())
        contributionPeriods_cont_9.append(contributionPeriods_4_9.copy())
        contributionPeriods_cont_9.append(contributionPeriods_5_9.copy())
        contributionPeriods_cont_9.append(contributionPeriods_6_9.copy())
        contributionPeriods_cont_9.append(contributionPeriods_7_9.copy())
        contributionPeriods_cont_9.append(contributionPeriods_8_9.copy())
        contributionPeriods_cont_9.append(contributionPeriods_9_9.copy())
        contributionPeriods_cont_9.append(contributionPeriods_10_9.copy())
        contributionPeriods_cont_9.append(contributionPeriods_11_9.copy())
        contributionPeriods_cont_9.append(contributionPeriods_12_9.copy())

        est_contr_9 ["contributions"] = contributions_9
        est_contr_9 ["contributions"]["contributionPeriods"] = contributionPeriods_cont_9

        contr_9 = est_contr_9["contributions"]

#############################################################################################################
####################################### EMPLEADOR 10 #########################################################
#############################################################################################################
        est_contr_10 = {}
        
        contributionPeriods_cont_10 = []

        contributionPeriods_cont_10.append(contributionPeriods_1_10.copy())
        contributionPeriods_cont_10.append(contributionPeriods_2_10.copy())
        contributionPeriods_cont_10.append(contributionPeriods_3_10.copy())
        contributionPeriods_cont_10.append(contributionPeriods_4_10.copy())
        contributionPeriods_cont_10.append(contributionPeriods_5_10.copy())
        contributionPeriods_cont_10.append(contributionPeriods_6_10.copy())
        contributionPeriods_cont_10.append(contributionPeriods_7_10.copy())
        contributionPeriods_cont_10.append(contributionPeriods_8_10.copy())
        contributionPeriods_cont_10.append(contributionPeriods_9_10.copy())
        contributionPeriods_cont_10.append(contributionPeriods_10_10.copy())
        contributionPeriods_cont_10.append(contributionPeriods_11_10.copy())
        contributionPeriods_cont_10.append(contributionPeriods_12_10.copy())

        est_contr_10 ["contributions"] = contributions_10
        est_contr_10 ["contributions"]["contributionPeriods"] = contributionPeriods_cont_10

        contr_10 = est_contr_10["contributions"]

#############################################################################################################
####################################### EMPLEADOR 11 #########################################################
#############################################################################################################
        est_contr_11 = {}
        
        contributionPeriods_cont_11 = []

        contributionPeriods_cont_11.append(contributionPeriods_1_11.copy())
        contributionPeriods_cont_11.append(contributionPeriods_2_11.copy())
        contributionPeriods_cont_11.append(contributionPeriods_3_11.copy())
        contributionPeriods_cont_11.append(contributionPeriods_4_11.copy())
        contributionPeriods_cont_11.append(contributionPeriods_5_11.copy())
        contributionPeriods_cont_11.append(contributionPeriods_6_11.copy())
        contributionPeriods_cont_11.append(contributionPeriods_7_11.copy())
        contributionPeriods_cont_11.append(contributionPeriods_8_11.copy())
        contributionPeriods_cont_11.append(contributionPeriods_9_11.copy())
        contributionPeriods_cont_11.append(contributionPeriods_10_11.copy())
        contributionPeriods_cont_11.append(contributionPeriods_11_11.copy())
        contributionPeriods_cont_11.append(contributionPeriods_12_11.copy())

        est_contr_11 ["contributions"] = contributions_11
        est_contr_11 ["contributions"]["contributionPeriods"] = contributionPeriods_cont_11

        contr_11 = est_contr_11["contributions"]

#############################################################################################################
####################################### EMPLEADOR 12 #########################################################
#############################################################################################################
        est_contr_12 = {}
        
        contributionPeriods_cont_12 = []

        contributionPeriods_cont_12.append(contributionPeriods_1_12.copy())
        contributionPeriods_cont_12.append(contributionPeriods_2_12.copy())
        contributionPeriods_cont_12.append(contributionPeriods_3_12.copy())
        contributionPeriods_cont_12.append(contributionPeriods_4_12.copy())
        contributionPeriods_cont_12.append(contributionPeriods_5_12.copy())
        contributionPeriods_cont_12.append(contributionPeriods_6_12.copy())
        contributionPeriods_cont_12.append(contributionPeriods_7_12.copy())
        contributionPeriods_cont_12.append(contributionPeriods_8_12.copy())
        contributionPeriods_cont_12.append(contributionPeriods_9_12.copy())
        contributionPeriods_cont_12.append(contributionPeriods_10_12.copy())
        contributionPeriods_cont_12.append(contributionPeriods_11_12.copy())
        contributionPeriods_cont_12.append(contributionPeriods_12_12.copy())

        est_contr_12 ["contributions"] = contributions_12
        est_contr_12 ["contributions"]["contributionPeriods"] = contributionPeriods_cont_12

        contr_12 = est_contr_12["contributions"]

#############################################################################################################
######################## UNIR LOS CONTRIBUTION PERIODS EN UNA LISTA #########################################
#############################################################################################################

        all_contribution_Periods = []

        all_contribution_Periods.append(contr_1)
        all_contribution_Periods.append(contr_2)
        all_contribution_Periods.append(contr_3)
        all_contribution_Periods.append(contr_4)
        all_contribution_Periods.append(contr_5)
        all_contribution_Periods.append(contr_6)
        all_contribution_Periods.append(contr_7)
        all_contribution_Periods.append(contr_8)
        all_contribution_Periods.append(contr_9)
        all_contribution_Periods.append(contr_10)
        all_contribution_Periods.append(contr_11)
        all_contribution_Periods.append(contr_12)

        estructura["person"] = dict_person
        estructura ["person"]["contributions"] = all_contribution_Periods

        person = estructura["person"]
        expDt = estructura["Fecha_de_Consulta"]
        expDt = datetime.strptime(expDt, '%d/%m/%Y %H:%M:%S %p')
        expDt = expDt.isoformat() 
        container.upsert_item({'id': id_unico, 'expDt':expDt, 'person' : person})

else:
    # La solicitud no fue exitosa
    print("Error al realizar la solicitud:", response.status_code)