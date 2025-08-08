# Copyright (c) 2025, maisha and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime

class Appointment(Document):
    def validate(self):
        if doctor_is_on_leave(self.doctor, self.appointment_date):
            frappe.throw("Doctor is on leave on this date.")

        if appointment_slot_taken(self.doctor, self.appointment_date, self.appointment_time):
            frappe.throw("This time slot is already booked.")


def doctor_is_on_leave(doctor, date):
    leave = frappe.get_all("Leave Days",
        filters={
            "parent": doctor,
            "leave_status": "Approved",
            "from_date": ["<=", date],
            "to_date": [">=", date]
        }
    )
    return bool(leave)

def appointment_slot_taken(doctor, date, time):
    existing = frappe.get_all("Appointment",
        filters={
            "doctor": doctor,
            "appointment_date": date,
            "appointment_time": time,
            "status": ["not in", ["Cancelled"]]
        }
    )
    return bool(existing)
