# ETL Simple de Cobertura Móvil en Colombia con Docker

Este repositorio contiene una sencilla ETL (Extracción, Transformación y Carga) implementada en Python para procesar datos de cobertura móvil en Colombia, obtenidos de la plataforma de datos abiertos del gobierno colombiano. La ETL está empaquetada en una imagen de Docker para facilitar su ejecución y despliegue.

## Descripción de la ETL

La ETL realiza los siguientes pasos:

1.  **Extracción:** Los datos son extraídos desde una API pública en formato JSON que contiene información sobre la cobertura de redes móviles en Colombia.
**Link de extracción:** https://www.datos.gov.co/resource/9mey-c8s8.json
3.  **Transformación:** Los datos extraídos son transformados utilizando la librería `pandas` de Python. Las transformaciones incluyen:
    * Renombrar la columna 'cobertuta\_4g' a 'cobertura\_4g' (corrección de un error tipográfico).
    * Convertir los valores de las columnas de cobertura ('cabecera\_municipal', 'cobertura\_2g', 'cobertura\_3g', 'cobertura\_hspa\_hspa\_dc', 'cobertura\_4g', 'cobertura\_lte', 'cobertura\_5g') de los valores 'S' y 'N' a representaciones numéricas `1` y `0` respectivamente. Los valores nulos se mantienen sin cambios.
    * Renombrar varias columnas para mejorar la legibilidad ('a\_o' a 'AÑO').
4.  **Carga:** Los datos transformados son cargados a un archivo CSV llamado `cobertura_movil_transformado.csv` y son utilizados en el siguiente tablero: https://public.tableau.com/views/ComparacindeCoberturaentreDepartamentosencolombia/Hoja2?:language=es-ES&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

## Contenido del Repositorio

* `app.py`: El script de Python que contiene la lógica de la ETL
* `Dockerfile`: El archivo de configuración para construir la imagen de Docker que empaqueta la ETL.
* `requirements.txt`: Archivo que lista las dependencias de Python necesarias.
* `cobertura_movil_transformado.csv` (se generará después de ejecutar la ETL dentro del contenedor Docker).


## Instrucciones de Uso

1.  **Clonar el repositorio (opcional):**
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd <nombre_del_repositorio>
    ```

2.  **Construir la imagen de Docker:**
    Asegúrarse de estar en el mismo directorio donde se encuentra el `Dockerfile` y ejecutar el siguiente comando en la terminal:
    ```bash
    docker build -t etl-cobertura-movil .
    ```
    Este comando construirá una imagen de Docker llamada `etl-cobertura-movil` utilizando las instrucciones del `Dockerfile`.

3.  **Ejecutar la ETL dentro de un contenedor Docker:**
    Una vez que la imagen se haya construido exitosamente, ejecuta un contenedor basado en esa imagen con el siguiente comando:
    ```bash
    docker run etl-cobertura-movil
    ```
    Este comando ejecutará el script `app.py` dentro del contenedor Docker. El script extraerá los datos, los transformará e imprimirá las primeras filas transformadas en la consola, además de guardar el resultado en el archivo `cobertura_movil_transformado.csv` dentro del sistema de archivos del contenedor.

