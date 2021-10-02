// Copyright (c) 2021, Luis Pillaga and contributors
// For license information, please see license.txt

frappe.ui.form.on('Litter Death', {
	// refresh: function(frm) {
	// }
	onload(frm) {
		frm.set_value('user', frappe.session.user);
	}
});
