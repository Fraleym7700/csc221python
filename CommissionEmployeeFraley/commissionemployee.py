# commissionemployee.py
"""CommissionEmployee base class"""
from decimal import Decimal

class CommissionEmployee:
    """ An employee who gets paid comission based on gross sales."""
    
    def __init__(self, first_name, last_name, ssn, gross_sales, commission_rate):
        """Initialize CommissionEmployees's attributes."""
        self._first_name = first_name
        self._last_name = last_name
        self._ssn = ssn
        self.gross_sales = gross_sales
        self.commission_rate = commission_rate
        
    @property
    def first_name(self):
        return self._first_name
    
    @property
    def last_name(self):
        return self._last_name
    
    @property
    def ssn(self):
        return self._ssn
    
    @property
    def gross_sales(self):
        return self._gross_sales
    
    @gross_sales.setter
    def gross_sales(self, sales):
        """set commission rate or raise ValueError if invalid"""
        if sales < Decimal("0.00"):
            raise ValueError('Gross sales must be >= to 0')
            
        self._gross_sales = sales
        
    @property
    def commisson_rate(self):
        return self._commission_rate
    
    @commisson_rate.setter
    def commission_rate(self, rate):
        """set commission rate or raise ValueError if invalid"""
        if not (Decimal('0.0') < rate < Decimal('1.0')):
            raise ValueError('Interest rate must be greater than 0 and less than 1')
            
        self._commission_rate = rate
        
    def earnings(self):
        """Calculate earnings."""
        return self.gross_sales * self.commission_rate
        
    def __repr__(self):
        """Return string representation for repr()."""
        return('CommissionEmployee: ' +
               f'{self.first_name} {self.last_name} \n' +
               f'social security number: {self.ssn} \n' +
               f'gross sales: {self.gross_sales:.2f}\n' +
               f'commission rate: {self.commission_rate:.2f}')
    
def test_class():
    #main is used to test hte class
    c = CommissionEmployee('Sue', 'Jones', '333-33-3333', Decimal('10000.00'), Decimal('0.06'))
    print("testinng CommissionEmployees")
    print(c)
    
def main():
    
    
    print('You will create a commission employee')
    firstName = input("Enter First name: ")
    lastName = input("Enter Lastname name: ")
    ssn = input("Enter Social Security Number: ")
    grossSales = Decimal(input("Enter Gross Sales"))
    commissionRate = Decimal(input("Enter Commission Rate"))
    
    
    
    p1 = CommissionEmployee(firstName, lastName, ssn, grossSales,commissionRate)
    print(p1)
    
if __name__ == "__main__":
    from decimal import Decimal
    main()
    