from config.database import get_db_connection
from models.materia_medica_full import MateriaMediaFullDatabase

def init_all_databases():
    """Initialize all databases including Materia Medica"""
    # Initialize Materia Medica
    try:
        MateriaMediaFullDatabase.init_full_materia_medica()
    except Exception as e:
        print(f"Error initializing Materia Medica: {str(e)}")

def get_medicine_by_name(medicine_name):
    """Get medicine details"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute('SELECT * FROM materia_medica_full WHERE medicine_name = ?', (medicine_name,))
        result = cursor.fetchone()
    except:
        cursor.execute('SELECT * FROM materia_medica WHERE medicine_name = ?', (medicine_name,))
        result = cursor.fetchone()
    
    conn.close()
    return dict(result) if result else None

def search_medicines(search_term):
    """Search medicines by various criteria"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
            SELECT medicine_name, common_name, indications 
            FROM materia_medica_full 
            WHERE medicine_name LIKE ? OR indications LIKE ? OR keynote_symptoms LIKE ?
        ''', (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%"))
        results = cursor.fetchall()
    except:
        cursor.execute('''
            SELECT medicine_name, common_name, indications 
            FROM materia_medica 
            WHERE medicine_name LIKE ? OR indications LIKE ? OR keynote_symptoms LIKE ?
        ''', (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%"))
        results = cursor.fetchall()
    
    conn.close()
    return [dict(row) for row in results]

def get_all_medicines():
    """Get list of all medicines"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute('SELECT medicine_name, common_name, abbreviation FROM materia_medica_full ORDER BY medicine_name')
        results = cursor.fetchall()
    except:
        cursor.execute('SELECT medicine_name, common_name, abbreviation FROM materia_medica ORDER BY medicine_name')
        results = cursor.fetchall()
    
    conn.close()
    return [dict(row) for row in results]
