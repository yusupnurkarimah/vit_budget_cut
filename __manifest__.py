#-*- coding: utf-8 -*-

{
	"name": "Vit budget cut",
	"version": "1.0", 
	"depends": [
		'base','vit_budget','om_account_budget',
	],
	"author": "Akhmad D. Sembiring [vitraining.com]",
	"category": "Utility",
	"website": "http://vitraining.com",
	"images": ["static/description/images/main_screenshot.jpg"],
	"price": "10",
	"license": "OPL-1",
	"currency": "USD",
	"summary": "This is the Vit budget cut module generated by StarUML Odoo Generator Pro Version",
	"description": """

Information
======================================================================

* created menus
* created objects
* created views
* logics

""",
	"data": [
		"security/ir.model.access.csv",
		"view/menu.xml",
		"view/budget_cut.xml",
		# "view/budget.xml",
		"view/budget_cut_lines.xml",
		"report/budget_cut.xml",
		# "report/budget.xml",
		"report/budget_cut_lines.xml",
		"data/squence.xml",
	],
	"installable": True,
	"auto_install": False,
	"application": True,
}