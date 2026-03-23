from backend.Database.database import engine

try:
    conn = engine.connect()
    print("Connected successfully 🚀")
    conn.close()
except Exception as e:
    print("Error:", e)