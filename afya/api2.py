import frappe

@frappe.whitelist()
def add_doctor_leave(doctor, leave_type, from_date, to_date):
    doc = frappe.get_doc("Doctor", doctor)
    doc.append("leave_days", {
        "leave_type": leave_type,
        "from_date": from_date,
        "to_date": to_date,
        "leave_status": "Approved"
    })
    doc.save()
    return {"message": "Leave added successfully"}
