### config.py ###

# Scheme: "postgres+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"
import psycopg2



DATABASE_URI = 'postgres+psycopg2://postgres:1234@localhost:5432/Excelcior'


conn = psycopg2.connect(host="localhost",database="Excelcior", user="postgres", password="1234")
cur = conn.cursor()