from datetime import datetime
from config.database import get_db_connection

class Consultation:
    def __init__(self, patient_id, consultation_date, symptoms=None, findings=None,
                 vital_signs=None, diagnosis=None, clinical_observation=None, 
                 consultation_notes=None):
        self.id = None
        self.patient_id = patient_id
        self.consultation_date = consultation_date
        self.symptoms = symptoms
        self.findings = findings
        self.vital_signs = vital_signs
        self.diagnosis = diagnosis
        self.clinical_observation = clinical_observation
        self.consultation_notes = consultation_notes
        self.created_at = datetime.now()
    
    def save(self):
        """Save consultation to database"""
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO consultations 
            (patient_id, consultation_date, symptoms, findings, vital_signs, 
             diagnosis, clinical_observation, consultation_notes, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (self.patient_id, self.consultation_date, self.symptoms, self.findings,
              self.vital_signs, self.diagnosis, self.clinical_observation,
              self.consultation_notes, self.created_at))
        
        conn.commit()
        self.id = cursor.lastrowid
        conn.close()
        return self.id
    
    @staticmethod
    def get_by_id(consultation_id):
        """Get consultation by ID"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM consultations WHERE id = ?', (consultation_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            consultation = Consultation(
                patient_id=row['patient_id'],
                consultation_date=row['consultation_date'],
                symptoms=row['symptoms'],
                findings=row['findings'],
                vital_signs=row['vital_signs'],
                diagnosis=row['diagnosis'],
                clinical_observation=row['clinical_observation'],
                consultation_notes=row['consultation_notes']
            )
            consultation.id = row['id']
            consultation.created_at = row['created_at']
            return consultation
        return None
    
    @staticmethod
    def get_by_patient(patient_id):
        """Get all consultations for a patient"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'SELECT * FROM consultations WHERE patient_id = ? ORDER BY consultation_date DESC',
            (patient_id,)
        )
        rows = cursor.fetchall()
        conn.close()
        
        consultations = []
        for row in rows:
            consultation = Consultation(
                patient_id=row['patient_id'],
                consultation_date=row['consultation_date'],
                symptoms=row['symptoms'],
                findings=row['findings'],
                vital_signs=row['vital_signs'],
                diagnosis=row['diagnosis'],
                clinical_observation=row['clinical_observation'],
                consultation_notes=row['consultation_notes']
            )
            consultation.id = row['id']
            consultation.created_at = row['created_at']
            consultations.append(consultation)
        
        return consultations
    
    def update(self):
        """Update consultation in database"""
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE consultations 
            SET consultation_date=?, symptoms=?, findings=?, vital_signs=?,
                diagnosis=?, clinical_observation=?, consultation_notes=?
            WHERE id=?
        ''', (self.consultation_date, self.symptoms, self.findings, self.vital_signs,
              self.diagnosis, self.clinical_observation, self.consultation_notes, self.id))
        
        conn.commit()
        conn.close()
    
    def delete(self):
        """Delete consultation from database"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM consultations WHERE id = ?', (self.id,))
        conn.commit()
        conn.close()
    
    def __repr__(self):
        return f"<Consultation {self.id}: Patient {self.patient_id} on {self.consultation_date}>"
