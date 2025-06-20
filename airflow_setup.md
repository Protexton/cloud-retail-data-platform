# ⚙️ Configuración local de Apache Airflow (Simulada)

Este proyecto incluye un DAG para simular el flujo de orquestación de datos de ventas en un entorno retail.

## 🛠 Requisitos

- Python 3.8+
- Apache Airflow
- pip install apache-airflow

## 📂 Estructura

El DAG `sales_etl_pipeline` contiene tres tareas:

1. **extract_data** – Carga de datos de origen
2. **transform_data** – Limpieza, joins, enriquecimiento
3. **load_data** – Exportación al modelo final

## ▶️ Cómo simular la ejecución

Puedes ejecutar los scripts directamente con Python para probar el flujo de datos sin desplegar un entorno Airflow completo.

Para desplegar con Airflow real:

```bash
export AIRFLOW_HOME=~/airflow
airflow db init
airflow users create --username iker --firstname Iker --lastname Reina --role Admin --email iker@example.com
airflow webserver -p 8080
airflow scheduler
```

Y luego cargar el DAG desde la carpeta `/dags`.

