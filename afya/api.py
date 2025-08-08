import frappe

@frappe.whitelist()
def get_doctor_leave(doctor):
    doc = frappe.get_doc("Doctor", doctor)
    return doc.leave_days

