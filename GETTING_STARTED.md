# Homeopathy Doctor Management App - Development

## Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Nikunjkanjariya/homeopathy-doctor-app.git
   cd homeopathy-doctor-app
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application:**
   ```bash
   python main.py
   ```

## Features Implemented

### ✅ Patient Management
- Add new patients with complete details
- Search patients by name or phone number
- Edit patient information
- Delete patient records
- View patient medical history

### ✅ Consultation Management
- Record new consultations
- Document symptoms and findings
- Record vital signs
- Add diagnosis and observations
- Store consultation notes

### ✅ Prescription Management
- Create prescriptions linked to consultations
- Select from common homeopathic potencies (6C, 12C, 30C, 200C, 1M, etc.)
- Specify dosage and frequency
- Set prescription duration
- Track medicine manufacturer and pricing
- Add special notes (empty stomach, avoid coffee, etc.)

### ✅ Recommendations
- Dietary recommendations
- Lifestyle advice
- Precautions and restrictions
- Follow-up scheduling

### ✅ Reports & PDF Generation
- Generate prescription PDFs
- Generate patient medical reports
- Print-friendly formats

## Database

The application uses SQLite3 database stored at:
- Windows: `C:\Users\<username>\.homeopathy_app\homeopathy.db`
- macOS/Linux: `~/.homeopathy_app/homeopathy.db`

## Project Structure

```
homeopathy-doctor-app/
├── main.py                           # Application entry point
├── requirements.txt                  # Project dependencies
├── config/
│   └── database.py                  # Database initialization
├── models/
│   ├── patient.py                   # Patient data model
│   ├── consultation.py              # Consultation data model
│   └── prescription.py              # Prescription data model
├── ui/
│   ├── main_window.py              # Main application window
│   ├── patient_dialog.py           # Patient management dialog
│   ├── consultation_dialog.py      # Consultation dialog
│   └── prescription_dialog.py      # Prescription dialog
├── utils/
│   ├── validators.py               # Input validation utilities
│   └── pdf_generator.py            # PDF report generation
└── README.md                         # Project documentation
```

## Usage Guide

### Adding a New Patient
1. Click on the "Patients" tab
2. Click "Add New Patient"
3. Fill in patient details:
   - Name (required)
   - Phone (required)
   - Email, address, etc.
   - Date of birth
   - Gender, occupation, marital status
4. Click "Save"

### Recording a Consultation
1. Click on the "Consultations" tab
2. Click "New Consultation"
3. Select the patient
4. Enter consultation details:
   - Symptoms
   - Physical findings
   - Vital signs
   - Diagnosis
   - Clinical observations
5. Click "Save Consultation"

### Creating a Prescription
1. Click on the "Prescriptions" tab
2. Click "New Prescription"
3. Select patient and (optionally) consultation
4. Enter medicine details:
   - Medicine name (e.g., Arnica Montana)
   - Potency (6C, 30C, 200C, etc.)
   - Dosage (e.g., 2-3 tablets)
   - Frequency (daily, twice daily, etc.)
   - Duration
   - Special notes
5. Click "Save Prescription"

## Common Homeopathic Potencies

- **6C/6X** - Low potency, acute conditions
- **12C/12X** - Medium potency, functional disorders
- **30C/30X** - High potency, chronic conditions
- **200C/200X** - Very high potency, constitutional treatment
- **1M/10M/CM** - Ultra-high potency, deep-acting remedies

## Common Homeopathic Medicines

Some commonly used medicines in the app:
- Arnica Montana - trauma, bruises
- Belladonna - fever, inflammation
- Bryonia - joint pain, headaches
- Calcarea Carbonica - weakness, fatigue
- Lycopodium - digestive issues
- Nux Vomica - stress, constipation
- Phosphorus - respiratory issues
- Pulsatilla - emotional sensitivity
- Sulphur - skin conditions
- Thuja - warts, growths

## Troubleshooting

### Database Not Found
The app will automatically create the database on first run. Check that you have write permissions to your home directory.

### Import Errors
Ensure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### PyQt6 Issues
On some systems, you may need to install additional libraries:
```bash
# Ubuntu/Debian
sudo apt-get install python3-pyqt6

# macOS (with Homebrew)
brew install pyqt6
```

## Future Enhancements

- [ ] Appointment scheduling
- [ ] Patient medical history form templates
- [ ] Automated follow-up reminders
- [ ] Billing and invoice generation
- [ ] Multi-user login system
- [ ] Cloud backup of patient records
- [ ] Mobile app integration
- [ ] Advanced analytics and reporting
- [ ] Integration with local labs
- [ ] Telemedicine features

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - See LICENSE file for details

## Support

For issues or feature requests, please open an issue on GitHub.

## Author

Nikunj Kanjariya
