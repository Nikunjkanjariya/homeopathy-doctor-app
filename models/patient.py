from datetime import datetime
from config.database import get_db_connection

class Patient:
    def __init__(self, first_name, last_name, phone, date_of_birth=None, 
                 gender=None, email=None, address=None, city=None, 
                 state=None, pincode=None, occupation=None, marital_status=None):
        self.id = None
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.phone = phone
        self.email = email
        self.address = address
        self.city = city
        self.state = state
        self.pincode = pincode
        self.occupation = occupation
        self.marital_status = marital_status
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def save(self):
        """Save patient to database"""
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO patients 
            (first_name, last_name, date_of_birth, gender, phone, email, 
             address, city, state, pincode, occupation, marital_status, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (self.first_name, self.last_name, self.date_of_birth, self.gender, 
              self.phone, self.email, self.address, self.city, self.state, 
              self.pincode, self.occupation, self.marital_status, 
              self.created_at, self.updated_at))
        
        conn.commit()
        self.id = cursor.lastrowid
        conn.close()
        return self.id
    
    @staticmethod
    def get_by_id(patient_id):
        """Get patient by ID"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM patients WHERE id = ?', (patient_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            patient = Patient(
                first_name=row['first_name'],
                last_name=row['last_name'],
                phone=row['phone'],
                date_of_birth=row['date_of_birth'],
                gender=row['gender'],
                email=row['email'],
                address=row['address'],
                city=row['city'],
                state=row['state'],
                pincode=row['pincode'],
                occupation=row['occupation'],
                marital_status=row['marital_status']
            )
            patient.id = row['id']
            patient.created_at = row['created_at']
            patient.updated_at = row['updated_at']
            return patient
        return None
    
    @staticmethod
    def get_all():
        """Get all patients"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM patients ORDER BY created_at DESC')
        rows = cursor.fetchall()
        conn.close()
        
        patients = []
        for row in rows:
            patient = Patient(
                first_name=row['first_name'],
                last_name=row['last_name'],
                phone=row['phone'],
                date_of_birth=row['date_of_birth'],
                gender=row['gender'],
                email=row['email'],
                address=row['address'],
                city=row['city'],
                state=row['state'],
                pincode=row['pincode'],
                occupation=row['occupation'],
                marital_status=row['marital_status']
            )
            patient.id = row['id']
            patient.created_at = row['created_at']
            patient.updated_at = row['updated_at']
            patients.append(patient)
        
        return patients
    
    @staticmethod
    def search(search_term):
        """Search patients by name or phone"""
        conn = get_db_connection()
        cursor = conn.cursor()
        query = '''
            SELECT * FROM patients 
            WHERE first_name LIKE ? OR last_name LIKE ? OR phone LIKE ?
            ORDER BY created_at DESC
        '''
        search_pattern = f"%{search_term}%"
        cursor.execute(query, (search_pattern, search_pattern, search_pattern))
        rows = cursor.fetchall()
        conn.close()
        
        patients = []
        for row in rows:
            patient = Patient(
                first_name=row['first_name'],
                last_name=row['last_name'],
                phone=row['phone'],
                date_of_birth=row['date_of_birth'],
                gender=row['gender'],
                email=row['email'],
                address=row['address'],
                city=row['city'],
                state=row['state'],
                pincode=row['pincode'],
                occupation=row['occupation'],
                marital_status=row['marital_status']
            )
            patient.id = row['id']
            patient.created_at = row['created_at']
            patient.updated_at = row['updated_at']
            patients.append(patient)
        
        return patients
    
    def update(self):
        """Update patient in database"""
        conn = get_db_connection()
        cursor = conn.cursor()
        self.updated_at = datetime.now()
        
        cursor.execute('''
            UPDATE patients 
            SET first_name=?, last_name=?, date_of_birth=?, gender=?, phone=?, email=?,
                address=?, city=?, state=?, pincode=?, occupation=?, marital_status=?, updated_at=?
            WHERE id=?
        ''', (self.first_name, self.last_name, self.date_of_birth, self.gender,
              self.phone, self.email, self.address, self.city, self.state,
              self.pincode, self.occupation, self.marital_status, self.updated_at, self.id))
        
        conn.commit()
        conn.close()
    
    def delete(self):
        """Delete patient from database"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM patients WHERE id = ?', (self.id,))
        conn.commit()
        conn.close()
    
    def full_name(self):
        """Get full name"""
        return f"{self.first_name} {self.last_name}"
    
    def __repr__(self):
        return f"<Patient {self.id}: {self.full_name()} - {self.phone}>"
