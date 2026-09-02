from config.database import get_db_connection

class MateriaMediaSearch:
    """Search and retrieve Materia Medica information"""
    
    @staticmethod
    def get_by_medicine_name(medicine_name):
        """Get medicine details by name"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'SELECT * FROM materia_medica WHERE medicine_name LIKE ?',
            (f"%{medicine_name}%",)
        )
        row = cursor.fetchone()
        conn.close()
        return dict(row) if row else None
    
    @staticmethod
    def search_by_indication(indication):
        """Search medicines by indication/condition"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'SELECT medicine_name, indications FROM materia_medica WHERE indications LIKE ?',
            (f"%{indication}%",)
        )
        results = cursor.fetchall()
        conn.close()
        return [dict(row) for row in results]
    
    @staticmethod
    def search_by_symptom(symptom):
        """Search medicines by symptom"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT medicine_name, keynote_symptoms, physical_symptoms 
            FROM materia_medica 
            WHERE keynote_symptoms LIKE ? OR physical_symptoms LIKE ?
        ''', (f"%{symptom}%", f"%{symptom}%"))
        results = cursor.fetchall()
        conn.close()
        return [dict(row) for row in results]
    
    @staticmethod
    def get_all_medicines():
        """Get list of all medicines"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id, medicine_name, common_name FROM materia_medica ORDER BY medicine_name')
        results = cursor.fetchall()
        conn.close()
        return [dict(row) for row in results]
    
    @staticmethod
    def get_medicines_by_potency(potency):
        """Get medicines available in specific potency"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'SELECT medicine_name, potencies FROM materia_medica WHERE potencies LIKE ?',
            (f"%{potency}%",)
        )
        results = cursor.fetchall()
        conn.close()
        return [dict(row) for row in results]
    
    @staticmethod
    def get_complementary_medicines(medicine_name):
        """Get complementary medicines for a given medicine"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'SELECT complementary_medicines FROM materia_medica WHERE medicine_name = ?',
            (medicine_name,)
        )
        result = cursor.fetchone()
        conn.close()
        if result and result['complementary_medicines']:
            return result['complementary_medicines'].split(', ')
        return []
    
    @staticmethod
    def get_incompatible_medicines(medicine_name):
        """Get incompatible medicines for a given medicine"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'SELECT incompatible_medicines FROM materia_medica WHERE medicine_name = ?',
            (medicine_name,)
        )
        result = cursor.fetchone()
        conn.close()
        if result and result['incompatible_medicines']:
            return result['incompatible_medicines'].split(', ')
        return []
    
    @staticmethod
    def search_constitutional_type(type_name):
        """Search medicines for a constitutional type"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'SELECT medicine_name, constitutional_type FROM materia_medica WHERE constitutional_type LIKE ?',
            (f"%{type_name}%",)
        )
        results = cursor.fetchall()
        conn.close()
        return [dict(row) for row in results]
    
    @staticmethod
    def get_detailed_medicine_info(medicine_name):
        """Get complete information about a medicine"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'SELECT * FROM materia_medica WHERE medicine_name = ?',
            (medicine_name,)
        )
        result = cursor.fetchone()
        conn.close()
        return dict(result) if result else None
