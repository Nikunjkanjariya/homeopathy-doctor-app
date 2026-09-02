from datetime import datetime
from config.database import get_db_connection

class Prescription:
    def __init__(self, patient_id, medicine_name, potency, dosage, frequency,
                 prescribed_date, consultation_id=None, duration=None, quantity=None,
                 manufacturer=None, price=None, notes=None):
        self.id = None
        self.patient_id = patient_id
        self.consultation_id = consultation_id
        self.medicine_name = medicine_name
        self.potency = potency
        self.dosage = dosage
        self.frequency = frequency
        self.duration = duration
        self.quantity = quantity
        self.manufacturer = manufacturer
        self.price = price
        self.notes = notes
        self.prescribed_date = prescribed_date
        self.created_at = datetime.now()
    
    def save(self):
        """Save prescription to database"""
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO prescriptions 
            (patient_id, consultation_id, medicine_name, potency, dosage, frequency,
             duration, quantity, manufacturer, price, notes, prescribed_date, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (self.patient_id, self.consultation_id, self.medicine_name, self.potency,
              self.dosage, self.frequency, self.duration, self.quantity, self.manufacturer,
              self.price, self.notes, self.prescribed_date, self.created_at))
        
        conn.commit()
        self.id = cursor.lastrowid
        conn.close()
        return self.id
    
    @staticmethod
    def get_by_id(prescription_id):
        """Get prescription by ID"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM prescriptions WHERE id = ?', (prescription_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            prescription = Prescription(
                patient_id=row['patient_id'],
                medicine_name=row['medicine_name'],
                potency=row['potency'],
                dosage=row['dosage'],
                frequency=row['frequency'],
                prescribed_date=row['prescribed_date'],
                consultation_id=row['consultation_id'],
                duration=row['duration'],
                quantity=row['quantity'],
                manufacturer=row['manufacturer'],
                price=row['price'],
                notes=row['notes']
            )
            prescription.id = row['id']
            prescription.created_at = row['created_at']
            return prescription
        return None
    
    @staticmethod
    def get_by_patient(patient_id):
        """Get all prescriptions for a patient"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'SELECT * FROM prescriptions WHERE patient_id = ? ORDER BY prescribed_date DESC',
            (patient_id,)
        )
        rows = cursor.fetchall()
        conn.close()
        
        prescriptions = []
        for row in rows:
            prescription = Prescription(
                patient_id=row['patient_id'],
                medicine_name=row['medicine_name'],
                potency=row['potency'],
                dosage=row['dosage'],
                frequency=row['frequency'],
                prescribed_date=row['prescribed_date'],
                consultation_id=row['consultation_id'],
                duration=row['duration'],
                quantity=row['quantity'],
                manufacturer=row['manufacturer'],
                price=row['price'],
                notes=row['notes']
            )
            prescription.id = row['id']
            prescription.created_at = row['created_at']
            prescriptions.append(prescription)
        
        return prescriptions
    
    def update(self):
        """Update prescription in database"""
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE prescriptions 
            SET medicine_name=?, potency=?, dosage=?, frequency=?, duration=?,
                quantity=?, manufacturer=?, price=?, notes=?, prescribed_date=?
            WHERE id=?
        ''', (self.medicine_name, self.potency, self.dosage, self.frequency,
              self.duration, self.quantity, self.manufacturer, self.price, self.notes,
              self.prescribed_date, self.id))
        
        conn.commit()
        conn.close()
    
    def delete(self):
        """Delete prescription from database"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM prescriptions WHERE id = ?', (self.id,))
        conn.commit()
        conn.close()
    
    def __repr__(self):
        return f"<Prescription {self.id}: {self.medicine_name} {self.potency}>"
