# 🛍️ Cloud Retail Data Platform

Este proyecto simula una **infraestructura moderna de datos** para una cadena ficticia de retail que opera con múltiples tiendas físicas y canal online.

## 🎯 Objetivo

Diseñar una plataforma de datos integral que permita:

- Gestionar y analizar ventas, stock, opiniones y clientes.
- Optimizar decisiones de negocio con dashboards ejecutivos.
- Orquestar pipelines de procesamiento como en un entorno real.
- Estar preparada para escalar en AWS o cualquier entorno cloud.

---

## 🧱 Arquitectura de referencia

```
[ Datos brutos ] → [ ETL con Python ] → [ PostgreSQL ] → [ Orquestación con Airflow ] → [ Visualización con Power BI/Tableau ]
```

---

## 📁 Estructura del repositorio

- `data/raw/`: Datos originales simulados (ventas, clientes, productos…)
- `scripts/`: Código Python de procesamiento, validación y carga
- `sql/`: Consultas SQL para análisis y reporting
- `notebooks/`: Exploración y visualización de los datos
- `dags/`: DAGs simulados para orquestación con Apache Airflow
- `dashboards/`: Capturas y enlaces a informes en Power BI o Looker Studio

---

## 🧪 Dataset generado

- **Clientes:** 50 usuarios con ciudad, email, nombre
- **Tiendas:** 5 localizaciones con nombre y ciudad
- **Productos:** 20 referencias por categoría (ropa, hogar…)
- **Ventas:** 200 transacciones con fechas y cantidades
- **Opiniones:** 100 reseñas con puntuación y texto

---

## 🔧 Stack utilizado

| Componente        | Herramienta                     |
|-------------------|---------------------------------|
| Lenguaje          | Python 3 + SQL                  |
| Procesamiento     | pandas, numpy                   |
| Orquestación      | Apache Airflow (estructura real)|
| Visualización     | Looker Studio                   |
| Base de datos     | PostgreSQL                      |
| Cloud (simulado)  | AWS S3, Glue, Redshift          |

---

## 📊 Visualización de datos

Consulta el dashboard interactivo desarrollado con Google Looker Studio:

👉 [Ver dashboard en línea](https://lookerstudio.google.com/reporting/916a736a-77fb-42b2-b042-10b7b7a8425a)

Este informe muestra los principales KPIs del negocio simulando una solución profesional para la dirección comercial:
- Ventas por tienda
- Evolución temporal de ingresos
- Productos más vendidos
- Ticket medio por cliente

---

## 📊 Resultados esperados

- KPIs clave por tienda, producto y categoría
- Productos más vendidos y peor valorados
- Opiniones de clientes segmentadas por rating
- Dashboards interactivos para dirección

---

## 🧠 Autor

Iker Vaca Reina · [GitHub: Protexton](https://github.com/Protexton)
