# Apache Spark PoC en Python

Este proyecto es una Prueba de Concepto (PoC) para demostrar cómo utilizar Apache Spark con Python para analizar datos de un archivo de texto. El proyecto utiliza PySpark para la escritura de scripts de análisis.

## Requisitos

- Python 3.6 o superior
- pip (Python package installer)

## Configuración del Entorno

### 1. Descargar el proyecto

Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/tu_usuario/apache-spark-poc.git
cd apache-spark-poc
```

### 2. Genera el archivo de prueba que analisaremos con Spark.
```bash 
/bin/python3 /src/main/com/jerech/spark/random-text.py
```
Puedes modificar la palabra clave que deseas que contenga el archivo y el tamaño del archivo a generar.
Valores por defecto 
KEY_WORD = "fraude"
FILE_SIZE_MB = 500

## Análisis existencia de parabra clave "fraude" como ejemplo

### 1. Corre script para analizar archivo previamente generado.
```bash 
/bin/python3 /src/main/com/jerech/spark/search-word.py
```
### 2. Verifica en la consola los resultados obtenidos
Como resultado, en la consola, vas a encontrar los indices de filas que contienen la palabra clave "fraude".


