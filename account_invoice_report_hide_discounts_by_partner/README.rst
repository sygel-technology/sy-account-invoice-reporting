.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
	:target: http://www.gnu.org/licenses/agpl
	:alt: License: AGPL-3

================================================
Account Invoice Report Hide Discounts by Partner
================================================

This module allows you to show the discounts on invoices based on the partner.

In order not to show the discounts in the invoices, on the one hand hide the discount columns and 
on the other hand recalculate the unit price including the discount.


Installation
============

To install this module, you need to:

#. Only install


Configuration
=============

To configure this module, you need to:

#. Go to the contacts module 
#. Create or Edit a parent contact
#. Go to Invoicing tab
#. Edit the 'Show discounts' field

To configure unit price decimal precision to show the unit price with discounts:

#. With developer permissions go to Technical settings. 
#. Go to Decimal Accuracy.
#. Set the decimal places you want to display in the unit price column of invoices.


Usage
=====

To use this module, you need to:

#. Go to the Invoices module
#. Create a new invoice
#. Select a partner. You will see that the Show discounts field defaults to the partner, but you can edit it.
#. Add lines to the invoice with a discount.
#. Print the invoice.


ROADMAP
=======

Whether or not discounts are shown on the invoices is independent of the type of invoice.

The Show discounts field of the partner is always taken from the value set in the parent contact.


Bug Tracker
===========

Bugs and errors are managed in `issues of GitHub <https://github.com/sygel-technology/sy-account-invoice-reporting/issues>`_.
In case of problems, please check if your problem has already been
reported. If you are the first to discover it, help us solving it by indicating
a detailed description `here <https://github.com/sygel-technology/sy-account-invoice-reporting/issues/new>`_.

Do not contact contributors directly about support or help with technical issues.


Credits
=======

Authors
~~~~~~~

* Sygel, Odoo Community Association (OCA)

Contributors
~~~~~~~~~~~~

* Ángel García de la Chica Herrera <angel.garcia@sygel.es>
* Manuel Regidor <manuel.regidor@sygel.es>

Maintainer
~~~~~~~~~~

This module is maintained by Sygel.

.. image:: https://www.sygel.es/logo.png
   :alt: Sygel
   :target: https://www.sygel.es

This module is part of the `Sygel/sy-account-invoice-reporting <https://github.com/sygel-technology/sy-account-invoice-reporting>`_.

To contribute to this module, please visit https://github.com/sygel-technology.
