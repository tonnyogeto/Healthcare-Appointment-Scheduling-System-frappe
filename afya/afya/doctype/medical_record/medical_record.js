frappe.ui.form.on('Medical Record', {
    appointment: function(frm) {
        if (frm.doc.appointment) {
            frappe.db.get_value('Appointment', frm.doc.appointment, ['patient', 'doctor'], (r) => {
                if (r) {
                    frm.set_value('patient', r.patient);
                    frm.set_value('doctor', r.doctor);
                }
            });
        }
    }
});


