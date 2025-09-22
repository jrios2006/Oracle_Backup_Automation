#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Librerías propias para el registro 
# InicializoDatosLog()

def InicializoDatosLog():
    '''Inicializo un diccionario de datos para trazar el log con los datos básicos
    Datos de Ejecutable
    Datos del sistema operativo
    Datos de la conexión de red
    Instancia
    Tipo de mensaje
    Depende de como hayamos definido la tabla de Log (Log_Scripts)'''
    from lib.lug_uuid import ObtengoIDInstanciaLog
    from lib.lug_metadatos import ObtenerMetadatosIpConexion, ObtenerMetadatosPrograma, ObtenerMetadatosPlataforma 

    DatosLog = {
        "instancia" : ObtengoIDInstanciaLog(),
        "resultado" : "Ejecuntadose",
        "tipo_mensaje" : "INFO",
        "parametros" : {
            "Programa" : ObtenerMetadatosPrograma(),
            "Sistema" : ObtenerMetadatosPlataforma(),
            "Red" : ObtenerMetadatosIpConexion()
        },
        "nombre_script" : ObtenerMetadatosPrograma()['NombrePrograma']

    }
    return DatosLog

def AnotarLogs(DataLogInicial, ParametrosIniciales, Credenciales,
               categoria_script=None, tipo_mensaje=None, resultado=None, observaciones=None, cabeceras=None, mensaje=None):
    '''Anto logs usando una plantilla inicial DataLogs, luego puedes añadir más campos según la tabla de Logs'''
    from lib.lug_bbdd import InsertarRegistro
    DataLog = DataLogInicial.copy()
    if categoria_script:
        DataLog['categoria_script'] = categoria_script
    if observaciones:
        DataLog['observaciones'] = observaciones
    if tipo_mensaje:
         DataLog['tipo_mensaje'] = tipo_mensaje
    if resultado: 
         DataLog['resultado'] = resultado
    if cabeceras: 
         DataLog['cabeceras'] = cabeceras
    if mensaje: 
         DataLog['mensaje'] = mensaje

    resultado = InsertarRegistro(Credenciales=Credenciales['BBDD'], Tabla=ParametrosIniciales['TablaLogs'], Datos=DataLog)
    #print(resultado)
    del DataLog

def AnotarLogsOracle(DataLogInicial, ParametrosIniciales, Credenciales,
               categoria_script=None, tipo_mensaje=None, resultado=None, observaciones=None, cabeceras=None, mensaje=None):
    '''Anto logs usando una plantilla inicial DataLogs, luego puedes añadir más campos según la tabla de Logs'''
    from lib.lug_bbdd import InsertarRegistroOracle
    DataLog = DataLogInicial.copy()
    if categoria_script:
        DataLog['categoria_script'] = categoria_script
    if observaciones:
        DataLog['observaciones'] = observaciones
    if tipo_mensaje:
         DataLog['tipo_mensaje'] = tipo_mensaje
    if resultado: 
         DataLog['resultado'] = resultado
    if cabeceras: 
         DataLog['cabeceras'] = cabeceras
    if mensaje: 
         DataLog['mensaje'] = mensaje

    resultado = InsertarRegistroOracle(Credenciales=Credenciales['BBDD'], Tabla=ParametrosIniciales['TablaLogs'], Datos=DataLog)
    #print(resultado)
    del DataLog