frappe.ui.form.on('Sales Invoice', {
	refresh: function(frm,cdt,cdn) {
        var me = this;
        var doc = frm.doc;
        var print_format1 = "Sales%20Invoice-Original";
        var print_format2 = "Sales%20Invoice-Duplicate";
        var print_format3 = "Sales%20Invoice-Triplicate";// print format name
		frm.add_custom_button(__('Original'), function(){

		var pages = window.open(frappe.urllib.get_full_url("/api/method/frappe.utils.print_format.download_pdf?"
			+"doctype="+encodeURIComponent(cdt)
			+"&name="+encodeURIComponent(cdn)
			+"&trigger_print=1"
			+"&format=" + print_format1
			+"&no_letterhead=Precihole%20Sports%20Standard"
			));
		//pages.print();
    }, __("Print"));
	}
});