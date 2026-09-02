from datetime import datetime, timedelta
from config.database import get_db_connection

class Appointment:
    def __init__(self, patient_id, appointment_date, appointment_time, 
                 reason=None, status="Scheduled", doctor_notes=None):
        self.id = None
        self.patient_id = patient_id
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time
        self.reason = reason
        self.status = status  # Scheduled, Completed, Cancelled, Rescheduled
        self.doctor_notes = doctor_notes
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def save(self):
        """Save appointment to database"""
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO appointments 
            (patient_id, appointment_date, appointment_time, reason, status, 
             doctor_notes, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (self.patient_id, self.appointment_date, self.appointment_time,
              self.reason, self.status, self.doctor_notes, self.created_at, self.updated_at))
        
        conn.commit()
        self.id = cursor.lastrowid
        conn.close()
        return self.id
    
    @staticmethod
    def get_by_id(appointment_id):
        """Get appointment by ID"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM appointments WHERE id = ?', (appointment_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            appointment = Appointment(
                patient_id=row['patient_id'],
                appointment_date=row['appointment_date'],
                appointment_time=row['appointment_time'],
                reason=row['reason'],
                status=row['status'],
                doctor_notes=row['doctor_notes']
            )
            appointment.id = row['id']
            appointment.created_at = row['created_at']
            appointment.updated_at = row['updated_at']
            return appointment
        return None
    
    @staticmethod
    def get_by_patient(patient_id):
        """Get all appointments for a patient"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'SELECT * FROM appointments WHERE patient_id = ? ORDER BY appointment_date DESC',
            (patient_id,)
        )
        rows = cursor.fetchall()
        conn.close()
        
        appointments = []
        for row in rows:
            appointment = Appointment(
                patient_id=row['patient_id'],
                appointment_date=row['appointment_date'],
                appointment_time=row['appointment_time'],
                reason=row['reason'],
                status=row['status'],
                doctor_notes=row['doctor_notes']
            )
            appointment.id = row['id']
            appointment.created_at = row['created_at']
            appointment.updated_at = row['updated_at']
            appointments.append(appointment)
        
        return appointments
    
    @staticmethod
    def get_upcoming():
        """Get upcoming appointments"""
        conn = get_db_connection()
        cursor = conn.cursor()
        today = datetime.now().strftime('%Y-%m-%d')
        cursor.execute(
            'SELECT * FROM appointments WHERE appointment_date >= ? AND status = "Scheduled" ORDER BY appointment_date ASC',
            (today,)
        )
        rows = cursor.fetchall()
        conn.close()
        
        appointments = []
        for row in rows:
            appointment = Appointment(
                patient_id=row['patient_id'],
                appointment_date=row['appointment_date'],
                appointment_time=row['appointment_time'],
                reason=row['reason'],
                status=row['status'],
                doctor_notes=row['doctor_notes']
            )
            appointment.id = row['id']
            appointment.created_at = row['created_at']
            appointment.updated_at = row['updated_at']
            appointments.append(appointment)
        
        return appointments
    
    @staticmethod
    def get_today_appointments():
        """Get today's appointments"""
        conn = get_db_connection()
        cursor = conn.cursor()
        today = datetime.now().strftime('%Y-%m-%d')
        cursor.execute(
            'SELECT * FROM appointments WHERE appointment_date = ? ORDER BY appointment_time ASC',
            (today,)
        )
        rows = cursor.fetchall()
        conn.close()
        
        appointments = []
        for row in rows:
            appointment = Appointment(
                patient_id=row['patient_id'],
                appointment_date=row['appointment_date'],
                appointment_time=row['appointment_time'],
                reason=row['reason'],
                status=row['status'],
                doctor_notes=row['doctor_notes']
            )
            appointment.id = row['id']
            appointment.created_at = row['created_at']
            appointment.updated_at = row['updated_at']
            appointments.append(appointment)
        
        return appointments
    
    def update(self):
        """Update appointment in database"""
        conn = get_db_connection()
        cursor = conn.cursor()
        self.updated_at = datetime.now()
        
        cursor.execute('''
            UPDATE appointments 
            SET patient_id=?, appointment_date=?, appointment_time=?, reason=?,
                status=?, doctor_notes=?, updated_at=?
            WHERE id=?
        ''', (self.patient_id, self.appointment_date, self.appointment_time,
              self.reason, self.status, self.doctor_notes, self.updated_at, self.id))
        
        conn.commit()
        conn.close()
    
    def delete(self):
        """Delete appointment from database"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM appointments WHERE id = ?', (self.id,))
        conn.commit()
        conn.close()
    
    def __repr__(self):
        return f"<Appointment {self.id}: Patient {self.patient_id} on {self.appointment_date} at {self.appointment_time}>"
