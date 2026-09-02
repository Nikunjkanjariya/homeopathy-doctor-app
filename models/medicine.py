from datetime import datetime
from config.database import get_db_connection

class Medicine:
    def __init__(self, name, potencies="", therapeutic_use="",
                 symptoms="", dosage_recommendation=""):
        self.id = None
        self.name = name
        self.potencies = potencies
        self.therapeutic_use = therapeutic_use
        self.symptoms = symptoms
        self.dosage_recommendation = dosage_recommendation
    
    def save(self):
        """Save medicine to database"""
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO medicines (name, potencies, therapeutic_use, symptoms, dosage_recommendation)
            VALUES (?, ?, ?, ?, ?)
        ''', (self.name, self.potencies, self.therapeutic_use, self.symptoms, self.dosage_recommendation))
        
        conn.commit()
        self.id = cursor.lastrowid
        conn.close()
        return self.id
    
    @staticmethod
    def get_all():
        """Get all medicines"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM medicines ORDER BY name')
        rows = cursor.fetchall()
        conn.close()
        
        medicines = []
        for row in rows:
            medicine = Medicine(
                name=row['name'],
                potencies=row['potencies'],
                therapeutic_use=row['therapeutic_use'],
                symptoms=row['symptoms'],
                dosage_recommendation=row['dosage_recommendation']
            )
            medicine.id = row['id']
            medicines.append(medicine)
        
        return medicines
    
    @staticmethod
    def search(search_term):
        """Search medicines by name"""
        conn = get_db_connection()
        cursor = conn.cursor()
        query = 'SELECT * FROM medicines WHERE name LIKE ? OR symptoms LIKE ? ORDER BY name'
        search_pattern = f"%{search_term}%"
        cursor.execute(query, (search_pattern, search_pattern))
        rows = cursor.fetchall()
        conn.close()
        
        medicines = []
        for row in rows:
            medicine = Medicine(
                name=row['name'],
                potencies=row['potencies'],
                therapeutic_use=row['therapeutic_use'],
                symptoms=row['symptoms'],
                dosage_recommendation=row['dosage_recommendation']
            )
            medicine.id = row['id']
            medicines.append(medicine)
        
        return medicines
    
    def __repr__(self):
        return f"<Medicine {self.id}: {self.name}>"
