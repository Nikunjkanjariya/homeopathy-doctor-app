from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib import colors
from datetime import datetime

def generate_prescription_pdf(patient, consultation, prescriptions, recommendations):
    """
    Generate PDF prescription report
    """
    filename = f"prescription_{patient.id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []
    
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#1f4788'),
        spaceAfter=30,
        alignment=1
    )
    
    # Header
    elements.append(Paragraph("HOMEOPATHIC PRESCRIPTION", title_style))
    elements.append(Spacer(1, 0.3*inch))
    
    # Patient Information
    patient_data = [
        ['Patient Name:', f"{patient.full_name()}"],
        ['Phone:', patient.phone],
        ['Email:', patient.email or 'N/A'],
        ['Age:', str(patient.date_of_birth) if patient.date_of_birth else 'N/A'],
        ['Gender:', patient.gender or 'N/A'],
        ['Date of Prescription:', datetime.now().strftime('%Y-%m-%d')]
    ]
    
    patient_table = Table(patient_data, colWidths=[2*inch, 4*inch])
    patient_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    elements.append(patient_table)
    elements.append(Spacer(1, 0.3*inch))
    
    # Consultation Details
    if consultation:
        elements.append(Paragraph("Consultation Details", styles['Heading2']))
        consultation_data = [
            ['Symptoms:', consultation.symptoms or 'N/A'],
            ['Findings:', consultation.findings or 'N/A'],
            ['Diagnosis:', consultation.diagnosis or 'N/A'],
        ]
        consultation_table = Table(consultation_data, colWidths=[2*inch, 4*inch])
        consultation_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        elements.append(consultation_table)
        elements.append(Spacer(1, 0.3*inch))
    
    # Prescriptions
    if prescriptions:
        elements.append(Paragraph("Medicines Prescribed", styles['Heading2']))
        prescription_data = [['Medicine', 'Potency', 'Dosage', 'Frequency', 'Duration']]
        for rx in prescriptions:
            prescription_data.append([
                rx.medicine_name,
                rx.potency,
                rx.dosage,
                rx.frequency,
                rx.duration or 'N/A'
            ])
        
        prescription_table = Table(prescription_data, colWidths=[1.5*inch, 1*inch, 1*inch, 1.2*inch, 1*inch])
        prescription_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1f4788')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey)
        ]))
        elements.append(prescription_table)
        elements.append(Spacer(1, 0.3*inch))
    
    # Recommendations
    if recommendations:
        elements.append(Paragraph("Recommendations", styles['Heading2']))
        rec_data = [
            ['Dietary Recommendations:', recommendations.get('dietary', 'N/A')],
            ['Lifestyle Advice:', recommendations.get('lifestyle', 'N/A')],
            ['Precautions:', recommendations.get('precautions', 'N/A')],
            ['Follow-up Date:', recommendations.get('followup_date', 'N/A')],
        ]
        rec_table = Table(rec_data, colWidths=[2*inch, 4*inch])
        rec_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('VALIGN', (0, 0), (-1, -1), 'TOP')
        ]))
        elements.append(rec_table)
    
    elements.append(Spacer(1, 0.5*inch))
    elements.append(Paragraph("_" * 50, styles['Normal']))
    elements.append(Paragraph("Doctor's Signature", styles['Normal']))
    
    # Build PDF
    doc.build(elements)
    return filename

def generate_patient_report_pdf(patient, consultations, prescriptions):
    """
    Generate patient history/report PDF
    """
    filename = f"patient_report_{patient.id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []
    
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#1f4788'),
        spaceAfter=30,
        alignment=1
    )
    
    # Header
    elements.append(Paragraph("PATIENT MEDICAL RECORD", title_style))
    elements.append(Spacer(1, 0.3*inch))
    
    # Patient Information
    patient_data = [
        ['Patient Name:', f"{patient.full_name()}"],
        ['Phone:', patient.phone],
        ['Email:', patient.email or 'N/A'],
        ['Date of Birth:', patient.date_of_birth or 'N/A'],
        ['Gender:', patient.gender or 'N/A'],
        ['Address:', f"{patient.address or ''}, {patient.city or ''}, {patient.state or ''} {patient.pincode or ''}"],
        ['Occupation:', patient.occupation or 'N/A'],
        ['Marital Status:', patient.marital_status or 'N/A']
    ]
    
    patient_table = Table(patient_data, colWidths=[2*inch, 4*inch])
    patient_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    elements.append(patient_table)
    elements.append(Spacer(1, 0.3*inch))
    
    # Consultations
    if consultations:
        elements.append(Paragraph("Consultation History", styles['Heading2']))
        for i, consultation in enumerate(consultations[:10], 1):  # Show last 10
            elements.append(Paragraph(f"Consultation #{i} - {consultation.consultation_date}", styles['Heading3']))
            cons_text = f"<b>Symptoms:</b> {consultation.symptoms or 'N/A'}<br/>"
            cons_text += f"<b>Diagnosis:</b> {consultation.diagnosis or 'N/A'}<br/>"
            cons_text += f"<b>Notes:</b> {consultation.consultation_notes or 'N/A'}<br/>"
            elements.append(Paragraph(cons_text, styles['Normal']))
            elements.append(Spacer(1, 0.1*inch))
    
    elements.append(PageBreak())
    
    # Prescription History
    if prescriptions:
        elements.append(Paragraph("Prescription History", styles['Heading2']))
        rx_data = [['Date', 'Medicine', 'Potency', 'Dosage', 'Frequency']]
        for rx in prescriptions[-20:]:  # Show last 20
            rx_data.append([
                rx.prescribed_date,
                rx.medicine_name,
                rx.potency,
                rx.dosage,
                rx.frequency
            ])
        
        if len(rx_data) > 1:
            rx_table = Table(rx_data, colWidths=[1.2*inch, 1.5*inch, 0.8*inch, 1*inch, 1.2*inch])
            rx_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1f4788')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 8),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
                ('GRID', (0, 0), (-1, -1), 1, colors.grey)
            ]))
            elements.append(rx_table)
    
    # Build PDF
    doc.build(elements)
    return filename
