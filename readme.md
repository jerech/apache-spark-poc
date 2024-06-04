# Apache Spark PoC en Python

Este proyecto es una Prueba de Concepto (PoC) para demostrar cómo utilizar Apache Spark con Python para analizar datos de un archivo de texto. El proyecto utiliza PySpark para la escritura de scripts de análisis de palabra clave en archivo de gran tamaño.

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

### 2. Genera el archivo de prueba para analizar con Spark.
Ejecuta en consola
```bash 
cd src
python3 file_generator.py
```
Puedes modificar la palabra clave que deseas que contenga el archivo y el tamaño del archivo a generar en constants.py.
Valores por defecto 
``KEY_WORD = "wordtosearch"``
``FILE_SIZE_MB = 500``

## Análisis existencia de parabra clave "wordtosearch" como ejemplo

### 1. Corre script para analizar archivo previamente generado.
Ejecuta en consola para obtener las filas en las que se encontro la palabra a buscar
```bash 
python3 search_word.py
```
### 2. Verifica en la consola los resultados obtenidos
Como resultado, en la consola, vas a encontrar los indices de filas que contienen la palabra clave "wordtosearch" ordenadas por cantidad de ocurrencias desc.

## Correr tests
Dirigete al directorio src

Ejecuta en consola
```bash 
cd /path/to/project/src
```

Luego ejecuta el comando
```bash 
python3 -m unittest discover tests
```

