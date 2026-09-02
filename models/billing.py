from datetime import datetime
from config.database import get_db_connection

class Billing:
    def __init__(self, patient_id, invoice_number, amount, description="",
                 payment_method="Cash", status="Pending", notes=""):
        self.id = None
        self.patient_id = patient_id
        self.invoice_number = invoice_number
        self.amount = amount
        self.description = description
        self.payment_method = payment_method  # Cash, Card, Online Transfer, Cheque
        self.status = status  # Pending, Paid, Partially Paid, Cancelled
        self.notes = notes
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def save(self):
        """Save billing record to database"""
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO billing 
            (patient_id, invoice_number, amount, description, payment_method,
             status, notes, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (self.patient_id, self.invoice_number, self.amount, self.description,
              self.payment_method, self.status, self.notes, self.created_at, self.updated_at))
        
        conn.commit()
        self.id = cursor.lastrowid
        conn.close()
        return self.id
    
    @staticmethod
    def get_by_id(billing_id):
        """Get billing record by ID"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM billing WHERE id = ?', (billing_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            billing = Billing(
                patient_id=row['patient_id'],
                invoice_number=row['invoice_number'],
                amount=row['amount'],
                description=row['description'],
                payment_method=row['payment_method'],
                status=row['status'],
                notes=row['notes']
            )
            billing.id = row['id']
            billing.created_at = row['created_at']
            billing.updated_at = row['updated_at']
            return billing
        return None
    
    @staticmethod
    def get_by_patient(patient_id):
        """Get all billing records for a patient"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'SELECT * FROM billing WHERE patient_id = ? ORDER BY created_at DESC',
            (patient_id,)
        )
        rows = cursor.fetchall()
        conn.close()
        
        billings = []
        for row in rows:
            billing = Billing(
                patient_id=row['patient_id'],
                invoice_number=row['invoice_number'],
                amount=row['amount'],
                description=row['description'],
                payment_method=row['payment_method'],
                status=row['status'],
                notes=row['notes']
            )
            billing.id = row['id']
            billing.created_at = row['created_at']
            billing.updated_at = row['updated_at']
            billings.append(billing)
        
        return billings
    
    @staticmethod
    def get_all():
        """Get all billing records"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM billing ORDER BY created_at DESC')
        rows = cursor.fetchall()
        conn.close()
        
        billings = []
        for row in rows:
            billing = Billing(
                patient_id=row['patient_id'],
                invoice_number=row['invoice_number'],
                amount=row['amount'],
                description=row['description'],
                payment_method=row['payment_method'],
                status=row['status'],
                notes=row['notes']
            )
            billing.id = row['id']
            billing.created_at = row['created_at']
            billing.updated_at = row['updated_at']
            billings.append(billing)
        
        return billings
    
    @staticmethod
    def get_pending_payments():
        """Get all pending payments"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'SELECT * FROM billing WHERE status IN ("Pending", "Partially Paid") ORDER BY created_at DESC'
        )
        rows = cursor.fetchall()
        conn.close()
        
        billings = []
        for row in rows:
            billing = Billing(
                patient_id=row['patient_id'],
                invoice_number=row['invoice_number'],
                amount=row['amount'],
                description=row['description'],
                payment_method=row['payment_method'],
                status=row['status'],
                notes=row['notes']
            )
            billing.id = row['id']
            billing.created_at = row['created_at']
            billing.updated_at = row['updated_at']
            billings.append(billing)
        
        return billings
    
    def update(self):
        """Update billing record in database"""
        conn = get_db_connection()
        cursor = conn.cursor()
        self.updated_at = datetime.now()
        
        cursor.execute('''
            UPDATE billing 
            SET patient_id=?, invoice_number=?, amount=?, description=?,
                payment_method=?, status=?, notes=?, updated_at=?
            WHERE id=?
        ''', (self.patient_id, self.invoice_number, self.amount, self.description,
              self.payment_method, self.status, self.notes, self.updated_at, self.id))
        
        conn.commit()
        conn.close()
    
    def delete(self):
        """Delete billing record from database"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM billing WHERE id = ?', (self.id,))
        conn.commit()
        conn.close()
    
    def __repr__(self):
        return f"<Billing {self.id}: Invoice {self.invoice_number} - {self.amount}>"
