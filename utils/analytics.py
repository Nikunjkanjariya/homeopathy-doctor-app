from config.database import get_db_connection
from datetime import datetime, timedelta

class Analytics:
    @staticmethod
    def get_total_patients():
        """Get total number of patients"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) as count FROM patients')
        result = cursor.fetchone()
        conn.close()
        return result['count']
    
    @staticmethod
    def get_total_consultations():
        """Get total consultations"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) as count FROM consultations')
        result = cursor.fetchone()
        conn.close()
        return result['count']
    
    @staticmethod
    def get_total_prescriptions():
        """Get total prescriptions issued"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) as count FROM prescriptions')
        result = cursor.fetchone()
        conn.close()
        return result['count']
    
    @staticmethod
    def get_total_revenue():
        """Get total revenue from paid invoices"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT SUM(amount) as total FROM billing WHERE status = "Paid"')
        result = cursor.fetchone()
        conn.close()
        return result['total'] or 0
    
    @staticmethod
    def get_pending_payments():
        """Get total pending payments"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT SUM(amount) as total FROM billing WHERE status IN ("Pending", "Partially Paid")')
        result = cursor.fetchone()
        conn.close()
        return result['total'] or 0
    
    @staticmethod
    def get_this_month_consultations():
        """Get consultations this month"""
        conn = get_db_connection()
        cursor = conn.cursor()
        today = datetime.now()
        first_day = today.replace(day=1).strftime('%Y-%m-%d')
        cursor.execute(
            'SELECT COUNT(*) as count FROM consultations WHERE consultation_date >= ?',
            (first_day,)
        )
        result = cursor.fetchone()
        conn.close()
        return result['count']
    
    @staticmethod
    def get_this_month_revenue():
        """Get revenue this month"""
        conn = get_db_connection()
        cursor = conn.cursor()
        today = datetime.now()
        first_day = today.replace(day=1).strftime('%Y-%m-%d')
        cursor.execute(
            'SELECT SUM(amount) as total FROM billing WHERE status = "Paid" AND created_at >= ?',
            (first_day,)
        )
        result = cursor.fetchone()
        conn.close()
        return result['total'] or 0
    
    @staticmethod
    def get_top_medicines():
        """Get top 10 prescribed medicines"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT medicine_name, COUNT(*) as count 
            FROM prescriptions 
            GROUP BY medicine_name 
            ORDER BY count DESC 
            LIMIT 10
        ''')
        results = cursor.fetchall()
        conn.close()
        return results
    
    @staticmethod
    def get_patient_visit_frequency():
        """Get patient visit patterns"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT p.id, p.first_name, p.last_name, COUNT(c.id) as visits
            FROM patients p
            LEFT JOIN consultations c ON p.id = c.patient_id
            GROUP BY p.id
            ORDER BY visits DESC
            LIMIT 20
        ''')
        results = cursor.fetchall()
        conn.close()
        return results
    
    @staticmethod
    def get_upcoming_appointments_count():
        """Get count of upcoming appointments"""
        conn = get_db_connection()
        cursor = conn.cursor()
        today = datetime.now().strftime('%Y-%m-%d')
        cursor.execute(
            'SELECT COUNT(*) as count FROM appointments WHERE appointment_date >= ? AND status = "Scheduled"',
            (today,)
        )
        result = cursor.fetchone()
        conn.close()
        return result['count']
    
    @staticmethod
    def get_today_appointments_count():
        """Get count of today's appointments"""
        conn = get_db_connection()
        cursor = conn.cursor()
        today = datetime.now().strftime('%Y-%m-%d')
        cursor.execute(
            'SELECT COUNT(*) as count FROM appointments WHERE appointment_date = ?',
            (today,)
        )
        result = cursor.fetchone()
        conn.close()
        return result['count']
