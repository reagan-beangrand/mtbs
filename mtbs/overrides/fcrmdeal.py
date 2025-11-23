import frappe
from frappe import _
from crm.fcrm.doctype.crm_deal.crm_deal import CRMDeal

class CustomCRMDeal(CRMDeal):
    @staticmethod
    def default_list_data():
        columns = [
			{
				"label": "Status",
				"type": "Select",
				"key": "status",
				"width": "10rem",
			},
			{
				"label": "Email",
				"type": "Data",
				"key": "email",
				"width": "12rem",
			},
			{
				"label": "Mobile No",
				"type": "Data",
				"key": "mobile_no",
				"width": "11rem",
			},
			{
				"label": "Assigned To",
				"type": "Text",
				"key": "_assign",
				"width": "10rem",
			},
			{
				"label": "Last Modified",
				"type": "Datetime",
				"key": "modified",
				"width": "8rem",
			},
		]
        rows = [
			"name",
			"status",
			"email",
			"currency",
			"mobile_no",
			"deal_owner",
			"sla_status",
			"response_by",
			"first_response_time",
			"first_responded_on",
			"modified",
			"_assign",
		]
        return {"columns": columns, "rows": rows}
    
    def validate(self):
        super().validate()
        self.custom_validate()

    def custom_validate(self):
        self.validate_service_type_field()
        self.validate_event_tab_fields()

    def validate_service_type_field(self):
        if not self.custom_service_type:
            frappe.throw(_("Service Type is required."), frappe.MandatoryError)

    
    def validate_event_tab_date(self,datetimeValue):
        if datetimeValue is not None and datetimeValue < frappe.utils.nowdate():
            frappe.throw(_("You can not select past date in Date"))

    def validate_mua_poc(self):
        if self.custom_primary_mua is not None and self.custom_secondary_mua is not None:
            if self.custom_primary_mua.lower() == self.custom_secondary_mua.lower():
                frappe.throw(_("Primary and Secondary MUA should not be same person"))

    def validate_event_tab_fields(self):
        if self.custom_service_type == 'SERT-00001':
            self.validate_event_tab_date(self.custom_datetime)
            self.validate_mua_poc()
        else: #self.custom_service_type == ServiceType.SDCLASS.value:
            self.validate_event_tab_date(self.custom_date_of_joining)
        #elif self.service_type == ServiceType.MCCLASS.value:
            #self.validate_event_tab_date(self.custom_date_of_joining)

    def validate_class_fields(self):
        if not self.custom_admission_number:
            frappe.throw(_("Admission Number Value is required."), frappe.MandatoryError)
        if not self.custom_course_name:
            frappe.throw(_("Course Name Value is required."), frappe.MandatoryError)
        if not self.custom_date_of_joining:
            frappe.throw(_("Date of Joining Date is required."), frappe.MandatoryError)
    
    def validate_event_fields(self):
        if not self.custom_event_type:
            frappe.throw(_("Event Type Value is required."), frappe.MandatoryError)
        if not self.custom_datetime:
            frappe.throw(_("DateTime Value is required."), frappe.MandatoryError)
        if not self.custom_primary_mua:
            frappe.throw(_("Primary MUA is required."), frappe.MandatoryError)
        if not self.custom_secondary_mua:
            frappe.throw(_("Secondary MUA is required."), frappe.MandatoryError)