import pandas as pd
import os

RAW_PATH = 'data/raw'
PROCESSED_PATH = 'data/processed'

# Cargar datasets
sales = pd.read_csv(os.path.join(RAW_PATH, 'sales.csv'))
products = pd.read_csv(os.path.join(RAW_PATH, 'products.csv'))
stores = pd.read_csv(os.path.join(RAW_PATH, 'stores.csv'))
clients = pd.read_csv(os.path.join(RAW_PATH, 'clients.csv'))

# Limpiar y normalizar columnas
sales['sale_date'] = pd.to_datetime(sales['sale_date'])
sales['quantity'] = sales['quantity'].astype(int)

# Unir con productos y tiendas
df = sales.merge(products, on='product_id', how='left')           .merge(stores, on='store_id', how='left')           .merge(clients, on='client_id', how='left')

# Calcular valor total
df['total_value'] = df['price'] * df['quantity']

# Guardar dataset procesado
df.to_csv(os.path.join(PROCESSED_PATH, 'sales_enriched.csv'), index=False)

print("✅ ETL ejecutado correctamente. Archivo generado: sales_enriched.csv")
