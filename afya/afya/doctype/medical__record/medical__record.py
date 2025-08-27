from frappe.model.document import Document


import frappe
from frappe.model.document import Document

class MedicalRecord(Document):
    def validate(self):
        if self.appointment:
            # Fetch patient and doctor from Appointment
            appointment_doc = frappe.get_doc("Appointment", self.appointment)
            
            # Set the fields on this Medical Record
            self.patient = appointment_doc.patient
            self.doctor = appointment_doc.doctor

    