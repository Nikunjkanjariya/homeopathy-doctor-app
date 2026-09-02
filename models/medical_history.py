from datetime import datetime
from config.database import get_db_connection

class MedicalHistory:
    def __init__(self, patient_id, chief_complaint, past_medical_history="",
                 family_history="", allergies="", lifestyle_habits="",
                 vaccination_history="", current_medications="",
                 mental_state="", physical_constitution=""):
        self.id = None
        self.patient_id = patient_id
        self.chief_complaint = chief_complaint
        self.past_medical_history = past_medical_history
        self.family_history = family_history
        self.allergies = allergies
        self.lifestyle_habits = lifestyle_habits
        self.vaccination_history = vaccination_history
        self.current_medications = current_medications
        self.mental_state = mental_state
        self.physical_constitution = physical_constitution
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def save(self):
        """Save medical history to database"""
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO medical_history 
            (patient_id, chief_complaint, past_medical_history, family_history,
             allergies, lifestyle_habits, vaccination_history, current_medications,
             mental_state, physical_constitution, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (self.patient_id, self.chief_complaint, self.past_medical_history,
              self.family_history, self.allergies, self.lifestyle_habits,
              self.vaccination_history, self.current_medications,
              self.mental_state, self.physical_constitution,
              self.created_at, self.updated_at))
        
        conn.commit()
        self.id = cursor.lastrowid
        conn.close()
        return self.id
    
    @staticmethod
    def get_by_patient(patient_id):
        """Get medical history for a patient"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM medical_history WHERE patient_id = ? ORDER BY created_at DESC LIMIT 1',
                      (patient_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            medical_history = MedicalHistory(
                patient_id=row['patient_id'],
                chief_complaint=row['chief_complaint'],
                past_medical_history=row['past_medical_history'],
                family_history=row['family_history'],
                allergies=row['allergies'],
                lifestyle_habits=row['lifestyle_habits'],
                vaccination_history=row['vaccination_history'],
                current_medications=row['current_medications'],
                mental_state=row['mental_state'],
                physical_constitution=row['physical_constitution']
            )
            medical_history.id = row['id']
            medical_history.created_at = row['created_at']
            medical_history.updated_at = row['updated_at']
            return medical_history
        return None
    
    def update(self):
        """Update medical history in database"""
        conn = get_db_connection()
        cursor = conn.cursor()
        self.updated_at = datetime.now()
        
        cursor.execute('''
            UPDATE medical_history 
            SET chief_complaint=?, past_medical_history=?, family_history=?,
                allergies=?, lifestyle_habits=?, vaccination_history=?,
                current_medications=?, mental_state=?, physical_constitution=?, updated_at=?
            WHERE id=?
        ''', (self.chief_complaint, self.past_medical_history, self.family_history,
              self.allergies, self.lifestyle_habits, self.vaccination_history,
              self.current_medications, self.mental_state, self.physical_constitution,
              self.updated_at, self.id))
        
        conn.commit()
        conn.close()
    
    def __repr__(self):
        return f"<MedicalHistory {self.id}: Patient {self.patient_id}>"
