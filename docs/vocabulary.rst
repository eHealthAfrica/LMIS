Vocabulary
------------

VVMStatus
    This is used to indicate Vaccine Vial Monitor for a vaccine. it has stages e.f Stage 1, Stage 2 etc

UOMCategory
    This is simply Unit of Measurement Category used to group units of measurement, it can be weight, volume, units etc.

UnitOfMeasurement
    This represents units of measuring items, it can be KiloGram, Celsius, Doses etc

Manufacturer
    Manufacturer refers to a product supplier, they are external firms, there is a list of products each manufacturer
    can supply.

Company
    Company is a concrete base class for entities such as Facility, it is used to model entities such as Partners.

CompanyCategory
    This is used to group company's that are related, it can be Facility, Partner, FacilityOperator

Party
    This is the abstract base class of Employee, Manufacturer and Company. A party is defined by: a name, a code,
    contact and address.

EmployeeCategory
    EmployeeCategory is used to model different categories of employees, it can be Driver, CCO, Store Manager.
    it is modelled hierarchically, it has properties such as:
        -name : name of the category, this is unique and required.
        -parent: parent category of this category. this is optional.

Employee
    Employee extends Party and an employee can also be an LMIS user if its linked to Django User object.
    Employee has the following attributes:
    - current company: The company field defines the current company of the user
    - main company: This defines which current company a user can choose: either the main company itself
            or one of the children companies.

FacilityType
    Facility Type is used to represent different types of facilities available in a country.
    it is modelled hierarchically. it can be a Health Facility or Store.

FacilityTypeApprovedProduct
    This is used to model products approved for each facility type.


Facility
    This is used to model stores, health facilities, Satellite store or any organisation that receives supplies and/or
    supplies other facilities.

Warehouse Type
    This is used to represent different types of warehouse(storage locations), it can be 'Physical Warehouse' or
    'In-transit Warehouse'(used to model warehouse for items been transported from one facility to another e.g during
    delivery)

Warehouse
    Warehouse is used to define storage locations at a facility, a facility can have more than one warehouse.

Program
    Program represent is used to group products that has same use and objective. it can be 'Routine Immunization', 'HIV'
    , 'Kick Polio Out' etc

ProgramProduct
    Program Product is used to link program and products that belongs to the program. A program can have more than one
    product and a product can belong to more than one program.
    -active: if a program product is not active it means it is no longer consider to be part of the program.

ProgramProductAllocationInfo
    This holds program product allocation details and information, it is defined for each program product and facility
    link.


ProgramProductPriceHistory
    This is used to keep track of changes in program product price and partners that support the program product. it is
    updated anytime program product price per unit changes or funding source(partners) changes.


FacilityProgramSupported
    This is used to keep track of programs a facility supports, the program start and end date at the facility and
    program status at the facility.


FacilitySupportedProgramProduct
    This is used to keep track of program products that is allowed at a facility. This should automatically be all the
    program products, you have to manually turn off some products.

SupervisoryNode
    This models a facility that is in-charge of an **Order Group**, it is modelled hierarchically, hence represents
    how alert or notification is escalated. first to a SupervisoryNode, then to a SupervisoryNode parent if it has one.

OrderGroup
    Each order group has member facilities that can use it to make purchase order and supervisory node that
    is in-charge of the group, a facility can belong to more than more than one order group.

ProcessingPeriod
    This has start and end date time, it is used to schedule processing of operations etc.

ProductCategory
    Used to group related products, it can be "Vaccine", "Syringes", "Device", "Diluent" etc


Product
    Product represents a particular object that is used in a program, e.g BCG, OPV, etc.

ProductPresentation
    This is used to model how a unit of a product is packaged, for vaccines it can be 20 doses per vial etc.

ModeOfAdministration
     This models how a product is used. it could be Oral, Subcutaneous, Intramuscular for Vaccine or
     N/A (Not Applicable) for some products.

Item
    It is used to uniquely identify collection of a given product that has same value for a given set of attributes that
    can vary from one collection of same product to another.

PurchaseOrder
    PurchaseOrder: is used to place a formal request for supply of products listed in the purchase order lines by
    the purchasing facility(purchaser). This can be generated by the system or facility employee with the permission.

PurchaseOrderLine
    A purchase order line must belong to a purchase order. it is used to give detailed information about products
    needed in a purchase order. it have attributes like program product, quantity requested etc.

SalesOrder
    This is used by a supplying facility to record items and quantity of each item to be shipped to another facility.
    it is usually linked to a purchase order.

SalesOrderLine
    used to record attribute details of each item that belongs to a sales order. it hold information like quantity etc.

Voucher
    Every time a sales order is delivered to the recipient and confirmed by the receiving store, this is generated as
    proof of delivery. A sales order can be converted to a voucher, if there is no modifications made to the sales
    order.

VoucherLine
    used to represent each item and its details such as quantity etc in a sales order, that were actually delivered
    to a facility.

Inventory
    This is used to keep track of the quantities of items and products at each facility's warehouse(s). inventory
    entries are made at item level, this can be aggregated to get product stock level at a warehouse.

InventoryLine
        This represents a single inventory entry for a unique item.

PhysicalStockCount
    This is a facility activity that takes place periodically, during physically stock count, the quantity of each item
    at a facility is counted and recorded.

PhysicalStockLine
    This is used to record details of each unique item counted during physical stock count.

ConsumptionRecord
    This is used to keep track of an item consumed at a facility within a given period.


ConsumptionRecordLine
    represents the quantity of each item consumed at a facility within the ConsumptionRecord start and end date.

IncomingShipment(BaseModel):
    This is used to record stock arrival from supplier or supplying facility.

IncomingShipmentLine
    This is used to record the detail of each unique item of an IncomingShipment.

OutgoingShipment(BaseModel):
    This is used to track stock movements out to recipient or receiving facility.

OutgoingShipmentLine(BaseModel):
    This is used to record the detail of each unique item of an OutgoingShipment.









