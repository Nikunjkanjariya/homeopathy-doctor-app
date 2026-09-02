# Homeopathy Doctor Management App

> Professional Desktop Application for Homeopathy Practice Management

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![PyQt6](https://img.shields.io/badge/GUI-PyQt6-green.svg)](https://www.riverbankcomputing.com/software/pyqt/)
[![SQLite3](https://img.shields.io/badge/Database-SQLite3-blue.svg)](https://www.sqlite.org/)

## 🎯 Overview

A comprehensive, professional-grade desktop application designed specifically for homeopathy doctors to efficiently manage their entire practice:

- 👥 **Patient Management**: Complete patient profiles and medical history
- 📋 **Consultations**: Detailed consultation documentation
- 💊 **Prescriptions**: Homeopathic prescription creation and tracking
- 📅 **Appointments**: Smart appointment scheduling system
- 💰 **Billing**: Professional invoicing and payment tracking
- 📊 **Analytics**: Comprehensive business analytics and reports
- 🔐 **Secure**: Local SQLite database with complete data control

## ⭐ Key Features

### Patient Management
- ✅ Add, edit, search, and delete patient records
- ✅ Comprehensive patient profiles
- ✅ Medical history tracking
- ✅ Real-time patient search

### Consultation System
- ✅ Record detailed consultations
- ✅ Document symptoms and findings
- ✅ Track vital signs
- ✅ Store diagnosis and observations

### Prescription Management
- ✅ Create homeopathic prescriptions
- ✅ Support for all potency levels (6C to CM)
- ✅ Dosage and frequency specifications
- ✅ Generate PDF prescriptions

### Appointment Scheduling
- ✅ Schedule patient appointments
- ✅ Track appointment status
- ✅ View today's and upcoming appointments
- ✅ Add follow-up notes

### Billing & Invoicing
- ✅ Create professional invoices
- ✅ Track payment status
- ✅ Manage pending payments
- ✅ Revenue analytics

### Analytics & Reports
- ✅ Dashboard with KPIs
- ✅ Generate analytics reports
- ✅ Billing reports
- ✅ Top medicines analysis
- ✅ Patient visit frequency

## 🚀 Quick Start

### Requirements
- Python 3.8 or higher
- Windows, macOS, or Linux
- 100MB disk space

### Installation

```bash
# Clone repository
git clone https://github.com/Nikunjkanjariya/homeopathy-doctor-app.git
cd homeopathy-doctor-app

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
python main.py
```

## 📚 Documentation

- **[Getting Started Guide](GETTING_STARTED.md)** - Step-by-step setup instructions
- **[Complete Documentation](COMPLETE_DOCUMENTATION.md)** - Comprehensive feature guide
- **[Changelog](CHANGELOG.md)** - Version history and updates

## 🏗️ Project Structure

```
homeopathy-doctor-app/
├── main.py                          # Application entry point
├── requirements.txt                 # Project dependencies
├── config/
│   ├── __init__.py
│   └── database.py                 # Database configuration
├── models/
│   ├── __init__.py
│   ├── patient.py                  # Patient model
│   ├── consultation.py             # Consultation model
│   ├── prescription.py             # Prescription model
│   ├── appointment.py              # Appointment model
│   ├── billing.py                  # Billing model
│   ├── medical_history.py          # Medical history model
│   └── medicine.py                 # Medicine model
├── ui/
│   ├── __init__.py
│   ├── main_window.py              # Main application window
│   ├── patient_dialog.py           # Patient management dialog
│   ├── consultation_dialog.py      # Consultation dialog
│   ├── prescription_dialog.py      # Prescription dialog
│   ├── appointment_dialog.py       # Appointment scheduling
│   ├── billing_dialog.py           # Billing dialog
│   └── medical_history_dialog.py   # Medical history dialog
├── utils/
│   ├── __init__.py
│   ├── validators.py               # Input validation
│   ├── analytics.py                # Business analytics
│   ├── pdf_generator.py            # PDF report generation
│   └── invoice_generator.py        # Invoice generation
├── README.md                        # Quick start guide
├── GETTING_STARTED.md              # Detailed setup guide
├── COMPLETE_DOCUMENTATION.md       # Full documentation
└── CHANGELOG.md                    # Version history
```

## 🛠️ Technology Stack

- **GUI**: PyQt6 (Desktop interface)
- **Database**: SQLite3 (Local data storage)
- **Language**: Python 3.8+
- **Reporting**: ReportLab (PDF generation)
- **Data**: Pandas (Data handling)

## 📊 Database Features

- **Local Storage**: SQLite3 database stored in user home directory
- **Auto-initialization**: Database schema created automatically
- **Relational**: Proper foreign key relationships
- **Secure**: Complete data privacy, no cloud dependencies
- **Scalable**: Handles thousands of patient records

## 🎨 UI Features

- **Clean Interface**: Professional and intuitive design
- **Tabbed Navigation**: Organized module access
- **Real-time Search**: Instant patient lookup
- **Responsive Tables**: Dynamic data display
- **Modal Dialogs**: Clean form inputs
- **Dashboard**: Key metrics at a glance

## 📈 Analytics & Reporting

### Dashboard Metrics
- Total patients
- Consultation count
- Prescription statistics
- Revenue tracking
- Pending payments
- Appointment schedules

### Report Types
- **Analytics Report**: Business KPIs and trends
- **Billing Report**: Revenue and payment analysis
- **Prescription Reports**: Individual prescription PDFs
- **Patient Reports**: Complete medical records

## 💡 Usage Examples

### Adding a Patient
```
1. Click "Patients" tab
2. Click "Add New Patient"
3. Fill in patient details
4. Click "Save"
```

### Creating a Prescription
```
1. Click "Prescriptions" tab
2. Click "New Prescription"
3. Select patient and medicine
4. Set potency, dosage, frequency
5. Click "Save Prescription"
```

### Scheduling an Appointment
```
1. Click "Appointments" tab
2. Click "Schedule Appointment"
3. Select patient and date/time
4. Add reason and notes
5. Click "Save Appointment"
```

### Generating Reports
```
1. Click "Reports" tab
2. Select report type
3. Click to generate
4. PDF saved to current directory
```

## 🔒 Data Security

- **Local Database**: All data stored locally on your computer
- **No Cloud**: No data sent to external servers
- **Encrypted**: Database file protection supported
- **Backups**: Easy manual backup capabilities
- **GDPR Compliant**: Complete data control and privacy

## 🐛 Troubleshooting

### Application Won't Start
```bash
pip install --upgrade -r requirements.txt
python main.py
```

### Database Issues
```bash
# Delete corrupted database
rm ~/.homeopathy_app/homeopathy.db
# Application will recreate on next run
```

### PyQt6 Installation
```bash
# Linux
sudo apt-get install python3-pyqt6

# macOS
brew install pyqt6

# All platforms
pip install --upgrade PyQt6
```

## 📋 System Requirements

| Requirement | Minimum | Recommended |
|------------|---------|-------------|
| Python | 3.8 | 3.9+ |
| RAM | 2 GB | 4 GB+ |
| Disk Space | 500 MB | 1 GB |
| OS | Windows 7+ / macOS 10.13+ / Ubuntu 18.04+ | Latest |

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -m 'Add improvement'`)
4. Push to branch (`git push origin feature/improvement`)
5. Open a Pull Request

## 📝 License

MIT License - See [LICENSE](LICENSE) file for details

## 👨‍💻 Author

**Nikunj Kanjariya**
- GitHub: [@Nikunjkanjariya](https://github.com/Nikunjkanjariya)
- Email: Contact via GitHub

## 🙏 Support

If you find this project helpful, please:
- ⭐ Star the repository
- 🐛 Report bugs and issues
- 💡 Suggest new features
- 📢 Share with other practitioners

## 📞 Contact & Support

- **Issues**: [GitHub Issues](https://github.com/Nikunjkanjariya/homeopathy-doctor-app/issues)
- **Documentation**: See docs folder
- **Discussions**: [GitHub Discussions](https://github.com/Nikunjkanjariya/homeopathy-doctor-app/discussions)

## 🎉 Acknowledgments

Thanks to all contributors and supporters of this project!

---

**Made with ❤️ for homeopathy practitioners**

*Last Updated: September 2, 2026*
