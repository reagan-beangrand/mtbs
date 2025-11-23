frappe.ui.form.on("CRM Deal", {    
    validate(frm){   
		console.log('extended-validate');     
        //debugger;
		//Other than Bridal Makeup validation
		if(frm.doc.custom_service_type!=undefined && frm.doc.custom_service_type.trim()!= 'SERT-00001'){
			if(frm.doc.custom_date_of_joining < frappe.datetime.get_today()){
				frappe.msgprint(__('You can not select past date in Date'));
				frappe.validated = false;
			}
		}
		//Bridal Makeup validation
		if(frm.doc.custom_service_type!=undefined && frm.doc.custom_service_type == 'SERT-00001'){ 
			if(frm.doc.custom_datetime < frappe.datetime.get_today()){
				frappe.msgprint(__('You can not select past date in Date'));
				frappe.validated = false;
			} else {
				let primary = frm.doc.custom_primary_mua;
				let secondary = frm.doc.custom_secondary_mua;
				if(primary != undefined && secondary != undefined){
						if(primary.toLowerCase() === secondary.toLowerCase()){
						frappe.msgprint('Primary and Secondary MUA should not be same person');
						frappe.validated = false;
					}			
				}

			}
				
		}
    }
})