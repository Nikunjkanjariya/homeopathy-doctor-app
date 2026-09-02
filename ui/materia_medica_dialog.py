from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QTableWidget, QTableWidgetItem, QTextEdit, QComboBox, QTabWidget, QWidget
)
from PyQt6.QtCore import Qt
from config.database import get_db_connection

class MateriaMediaDialog(QDialog):
    """Dialog to view and search Materia Medica database"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Materia Medica - Homeopathic Medicines Database")
        self.setGeometry(100, 100, 1200, 700)
        self.setup_ui()
        self.load_all_medicines()
    
    def setup_ui(self):
        layout = QVBoxLayout()
        
        # Create tabs
        self.tabs = QTabWidget()
        
        # Tab 1: Browse All Medicines
        self.setup_browse_tab()
        
        # Tab 2: Search by Indication
        self.setup_indication_tab()
        
        # Tab 3: Search by Symptom
        self.setup_symptom_tab()
        
        # Tab 4: Medicine Details
        self.setup_details_tab()
        
        layout.addWidget(self.tabs)
        self.setLayout(layout)
    
    def setup_browse_tab(self):
        """Setup browse all medicines tab"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Search box
        search_layout = QHBoxLayout()
        search_layout.addWidget(QLabel("Search Medicine:"))
        self.browse_search = QLineEdit()
        self.browse_search.setPlaceholderText("Enter medicine name...")
        self.browse_search.textChanged.connect(self.search_medicines)
        search_layout.addWidget(self.browse_search)
        layout.addLayout(search_layout)
        
        # Medicines table
        self.medicines_table = QTableWidget()
        self.medicines_table.setColumnCount(4)
        self.medicines_table.setHorizontalHeaderLabels(["Medicine Name", "Common Name", "Abbreviation", "Indications"])
        self.medicines_table.itemSelectionChanged.connect(self.on_medicine_selected)
        layout.addWidget(self.medicines_table)
        
        widget.setLayout(layout)
        self.tabs.addTab(widget, "Browse Medicines")
    
    def setup_indication_tab(self):
        """Setup search by indication tab"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Search box
        search_layout = QHBoxLayout()
        search_layout.addWidget(QLabel("Search by Indication:"))
        self.indication_search = QLineEdit()
        self.indication_search.setPlaceholderText("e.g., fever, pain, cough...")
        search_btn = QPushButton("Search")
        search_btn.clicked.connect(self.search_by_indication)
        search_layout.addWidget(self.indication_search)
        search_layout.addWidget(search_btn)
        layout.addLayout(search_layout)
        
        # Results table
        self.indication_table = QTableWidget()
        self.indication_table.setColumnCount(2)
        self.indication_table.setHorizontalHeaderLabels(["Medicine", "Indications"])
        self.indication_table.itemSelectionChanged.connect(self.on_medicine_selected_indication)
        layout.addWidget(self.indication_table)
        
        widget.setLayout(layout)
        self.tabs.addTab(widget, "Search by Indication")
    
    def setup_symptom_tab(self):
        """Setup search by symptom tab"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Search box
        search_layout = QHBoxLayout()
        search_layout.addWidget(QLabel("Search by Symptom:"))
        self.symptom_search = QLineEdit()
        self.symptom_search.setPlaceholderText("e.g., burning, stitching, headache...")
        search_btn = QPushButton("Search")
        search_btn.clicked.connect(self.search_by_symptom)
        search_layout.addWidget(self.symptom_search)
        search_layout.addWidget(search_btn)
        layout.addLayout(search_layout)
        
        # Results table
        self.symptom_table = QTableWidget()
        self.symptom_table.setColumnCount(3)
        self.symptom_table.setHorizontalHeaderLabels(["Medicine", "Keynote Symptoms", "Physical Symptoms"])
        self.symptom_table.itemSelectionChanged.connect(self.on_medicine_selected_symptom)
        layout.addWidget(self.symptom_table)
        
        widget.setLayout(layout)
        self.tabs.addTab(widget, "Search by Symptom")
    
    def setup_details_tab(self):
        """Setup medicine details view tab"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Medicine selector
        selector_layout = QHBoxLayout()
        selector_layout.addWidget(QLabel("Select Medicine:"))
        self.medicine_combo = QComboBox()
        self.medicine_combo.currentIndexChanged.connect(self.show_medicine_details)
        selector_layout.addWidget(self.medicine_combo)
        layout.addLayout(selector_layout)
        
        # Details text area
        self.details_text = QTextEdit()
        self.details_text.setReadOnly(True)
        layout.addWidget(self.details_text)
        
        widget.setLayout(layout)
        self.tabs.addTab(widget, "Medicine Details")
    
    def load_all_medicines(self):
        """Load all medicines from database"""
        conn = get_db_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute('SELECT medicine_name, common_name, abbreviation, indications FROM materia_medica_full ORDER BY medicine_name')
            medicines = cursor.fetchall()
        except:
            # Fallback to old table if new one doesn't exist
            cursor.execute('SELECT medicine_name, common_name, abbreviation, indications FROM materia_medica ORDER BY medicine_name')
            medicines = cursor.fetchall()
        
        conn.close()
        
        # Load in browse table
        self.medicines_table.setRowCount(len(medicines))
        self.medicine_combo.clear()
        
        for row, medicine in enumerate(medicines):
            self.medicines_table.setItem(row, 0, QTableWidgetItem(medicine['medicine_name']))
            self.medicines_table.setItem(row, 1, QTableWidgetItem(medicine['common_name'] or ""))
            self.medicines_table.setItem(row, 2, QTableWidgetItem(medicine['abbreviation'] or ""))
            self.medicines_table.setItem(row, 3, QTableWidgetItem(medicine['indications'][:50] + "..." if len(medicine['indications']) > 50 else medicine['indications']))
            
            # Add to combo box
            self.medicine_combo.addItem(medicine['medicine_name'])
    
    def search_medicines(self):
        """Search medicines by name"""
        search_term = self.browse_search.text().lower()
        
        for row in range(self.medicines_table.rowCount()):
            item = self.medicines_table.item(row, 0)
            if item and search_term in item.text().lower():
                self.medicines_table.setRowHidden(row, False)
            elif item:
                self.medicines_table.setRowHidden(row, True)
    
    def search_by_indication(self):
        """Search medicines by indication"""
        indication = self.indication_search.text()
        if not indication:
            return
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute(
                'SELECT medicine_name, indications FROM materia_medica_full WHERE indications LIKE ?',
                (f"%{indication}%",)
            )
        except:
            cursor.execute(
                'SELECT medicine_name, indications FROM materia_medica WHERE indications LIKE ?',
                (f"%{indication}%",)
            )
        
        results = cursor.fetchall()
        conn.close()
        
        self.indication_table.setRowCount(len(results))
        for row, medicine in enumerate(results):
            self.indication_table.setItem(row, 0, QTableWidgetItem(medicine['medicine_name']))
            self.indication_table.setItem(row, 1, QTableWidgetItem(medicine['indications']))
    
    def search_by_symptom(self):
        """Search medicines by symptom"""
        symptom = self.symptom_search.text()
        if not symptom:
            return
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                SELECT medicine_name, keynote_symptoms, physical_symptoms 
                FROM materia_medica_full 
                WHERE keynote_symptoms LIKE ? OR physical_symptoms LIKE ?
            ''', (f"%{symptom}%", f"%{symptom}%"))
        except:
            cursor.execute('''
                SELECT medicine_name, keynote_symptoms, physical_symptoms 
                FROM materia_medica 
                WHERE keynote_symptoms LIKE ? OR physical_symptoms LIKE ?
            ''', (f"%{symptom}%", f"%{symptom}%"))
        
        results = cursor.fetchall()
        conn.close()
        
        self.symptom_table.setRowCount(len(results))
        for row, medicine in enumerate(results):
            self.symptom_table.setItem(row, 0, QTableWidgetItem(medicine['medicine_name']))
            self.symptom_table.setItem(row, 1, QTableWidgetItem(medicine['keynote_symptoms'][:100] + "..." if len(medicine['keynote_symptoms']) > 100 else medicine['keynote_symptoms']))
            self.symptom_table.setItem(row, 2, QTableWidgetItem(medicine['physical_symptoms'][:100] + "..." if len(medicine['physical_symptoms']) > 100 else medicine['physical_symptoms']))
    
    def show_medicine_details(self):
        """Show detailed information for selected medicine"""
        medicine_name = self.medicine_combo.currentText()
        if not medicine_name:
            return
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute('SELECT * FROM materia_medica_full WHERE medicine_name = ?', (medicine_name,))
        except:
            cursor.execute('SELECT * FROM materia_medica WHERE medicine_name = ?', (medicine_name,))
        
        result = cursor.fetchone()
        conn.close()
        
        if result:
            result_dict = dict(result)
            details = f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                            MATERIA MEDICA - DETAILS                          ║
╚══════════════════════════════════════════════════════════════════════════════╝

📋 MEDICINE INFORMATION:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Medicine Name: {result_dict.get('medicine_name', 'N/A')}
Common Name: {result_dict.get('common_name', 'N/A')}
Abbreviation: {result_dict.get('abbreviation', 'N/A')}
Source: {result_dict.get('source', 'N/A')}

💊 POTENCIES & DOSAGE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Available Potencies: {result_dict.get('potencies', 'N/A')}
Dosage Recommendation: {result_dict.get('dosage_recommendation', 'N/A')}

🏥 INDICATIONS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{result_dict.get('indications', 'N/A')}

🔑 KEYNOTE SYMPTOMS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{result_dict.get('keynote_symptoms', 'N/A')}

🧠 MENTAL STATE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{result_dict.get('mental_state', 'N/A')}

💪 PHYSICAL SYMPTOMS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{result_dict.get('physical_symptoms', 'N/A')}

📊 MODALITIES (Better/Worse):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{result_dict.get('modalities', 'N/A')}

⚠️ CONTRAINDICATIONS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{result_dict.get('contraindications', 'None known')}

🔄 INTERACTIONS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{result_dict.get('interactions', 'None known')}

⚡ SIDE EFFECTS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{result_dict.get('side_effects', 'None known')}

🔗 COMPLEMENTARY MEDICINES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{result_dict.get('complementary_medicines', 'None known')}

❌ INCOMPATIBLE MEDICINES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{result_dict.get('incompatible_medicines', 'None known')}

👤 CONSTITUTIONAL TYPE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{result_dict.get('constitutional_type', 'N/A')}

🌡️ TEMPERATURE PREFERENCE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{result_dict.get('temperature_preference', 'N/A')}

🔗 RELATIONS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{result_dict.get('relations', 'N/A')}

📝 REMARKS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{result_dict.get('remarks', 'N/A')}
"""
            self.details_text.setText(details)
    
    def on_medicine_selected(self):
        """Handle medicine selection in browse tab"""
        current_row = self.medicines_table.currentRow()
        if current_row >= 0:
            medicine_name = self.medicines_table.item(current_row, 0).text()
            index = self.medicine_combo.findText(medicine_name)
            if index >= 0:
                self.medicine_combo.setCurrentIndex(index)
    
    def on_medicine_selected_indication(self):
        """Handle medicine selection in indication tab"""
        current_row = self.indication_table.currentRow()
        if current_row >= 0:
            medicine_name = self.indication_table.item(current_row, 0).text()
            index = self.medicine_combo.findText(medicine_name)
            if index >= 0:
                self.medicine_combo.setCurrentIndex(index)
    
    def on_medicine_selected_symptom(self):
        """Handle medicine selection in symptom tab"""
        current_row = self.symptom_table.currentRow()
        if current_row >= 0:
            medicine_name = self.symptom_table.item(current_row, 0).text()
            index = self.medicine_combo.findText(medicine_name)
            if index >= 0:
                self.medicine_combo.setCurrentIndex(index)
