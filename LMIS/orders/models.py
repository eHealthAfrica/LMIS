"""
    Orders/models.py is the module that handles all order taking and order processing etc
"""

#import core django module.
from django.db import models
from django.utils.translation import ugettext as _

#import external modules
from model_utils import Choices

#import project modules
from core.models import BaseModel, Facility, Program, Product, UnitOfMeasurement, ProductItem, Currency, Employee, \
    Warehouse, VVMStage


class PurchaseOrder(BaseModel):
    """
        PurchaseOrder: is used to place a formal request for supply of products listed in the purchase order lines by
        the purchasing facility(purchaser).
    """
    STATUS = Choices((0, 'draft', _('Draft')), (1, 'assigned', _('Assigned')), (2, 'done', _('Done')),
                     (3, 'cancelled', _('Cancelled'))
                     )
    purchaser = models.ForeignKey(Facility, related_name='purchaser')
    supplier = models.ForeignKey(Facility, related_name='supplier')
    status = models.IntegerField(choices=STATUS, default=STATUS.draft)
    emergency = models.BooleanField(default=False)
    order_date = models.DateField()
    expected_date = models.DateField(blank=True, null=True)


class PurchaseOrderLine(BaseModel):
    """
        PurchaseOrderLine defines product, quantity of product, current stock level of product at the requesting
         facility, it is used to fill a purchase order.
    """
    models.ForeignKey(PurchaseOrder)
    program = models.ForeignKey(Program)
    product = models.ForeignKey(Product)
    quantity_needed = models.IntegerField()
    current_quantity = models.IntegerField()
    quantity_uom = models.ForeignKey(UnitOfMeasurement)
    remark = models.CharField(max_length=55, blank=True)


class SalesOrder(BaseModel):
    """
        SalesOrder  is used by a Supplying Facility to record products, specifications and quantities that will be
        supplied to a receiving facility. it is usually linked to an PurchaseOrder.

        optionally, it can be linked to a purchase order.
    """
    STATUS = Choices((0, 'draft', _('Draft')), (1, 'assigned', _('Assigned')), (2, 'done', _('Done')),
                     (3, 'cancelled', _('Cancelled'))
                     )
    sales_order = models.ForeignKey('PurchaseOrder', blank=True, null=True)
    recipient = models.ForeignKey(Facility, related_name='recipient')
    supplier = models.ForeignKey(Facility, related_name='supplier')
    approved_by = models.ForeignKey(Employee)
    status = models.IntegerField(choices=STATUS, default=STATUS.draft)
    planned_date = models.DateTimeField(blank=True, null=True)
    completed_date = models.DateTimeField(null=True, blank=True)


class SalesOrderLine(BaseModel):
    """
        This is used to model each product unique item that is part of a sales order.
    """
    sales_order = models.ForeignKey(SalesOrder)
    program = models.ForeignKey(Program)
    product_item = models.ForeignKey(ProductItem)
    quantity_requested = models.IntegerField(blank=True, null=True)
    buffer_quantity = models.IntegerField()
    total_quantity = models.IntegerField()
    quantity_uom = models.ForeignKey(UnitOfMeasurement, related_name='quantity uom')
    total_price = models.DecimalField(max_length=21, decimal_places=2)
    price_currency = models.FloatField(Currency)
    total_weight = models.FloatField(blank=True, null=True)
    weight_uom = models.ForeignKey(UnitOfMeasurement, related_name='weight uom')
    total_volume = models.FloatField()
    vvm_stage = models.IntegerField(choices=VVMStage.STAGES, blank=True, null=True)
    volume_uom = models.ForeignKey(UnitOfMeasurement, related_name='volume uom')
    description = models.CharField(max_length=55, blank=True)


class Voucher(BaseModel):
    """
        Voucher is used as a proof of delivery
    """
    sales_order = models.ForeignKey(SalesOrder)
    recipient_representative = models.ForeignKey('Employee', related_name='recipient representative')
    supplier_representative = models.ForeignKey('Employee', related_name='supplier representative')


class VoucherLine(BaseModel):
    """
        This is used to represent each unique product item in a voucher.
        input_warehouse is the warehouse the item was dropped at.
    """
    program = models.ForeignKey(Program)
    product_item = models.ForeignKey(ProductItem)
    input_warehouse = models.ForeignKey(Warehouse, blank=True, null=True)
    quantity_supplied = models.IntegerField()
    quantity_uom = models.ForeignKey(UnitOfMeasurement)
    vvm_stage = models.IntegerField(choices=VVMStage.STAGES, blank=True, null=True)
    remark = models.CharField(max_length=55, blank=True)

