from extension import db
from persiantools.jdatetime import JalaliDateTime

class Company(db.Model):
    __tablename__ = 'Companies'

    id = db.Column(
        db.Integer,
        primary_key= True
        )
    
    name = db.Column(
        db.String(100), 
        nullable=False
        )
    
    """
    Relationship Section
    """
    voucher = db.relationship(
        'Voucher', backref='company', lazy=True)
    
    cheque = db.relationship(
                'Cheque', backref='company', lazy=True)
        
    requisition = db.relationship(
                    'Requisition', backref='company', lazy=True)
    
    
class Bank(db.Model):
    __tablename__ = 'banks'
    
    id = db.Column(
            db.Integer,
            primary_key= True
            )
    
    name = db.Column(
            db.String(100), 
            nullable=False
            )
    
    
        
    
    """
    Relationship Section
    """
    cheque = db.relationship(
            'Cheque', backref='bank', lazy=True)
    
    requisition = db.relationship(
                'Requisition', backref='bank', lazy=True)
    
    
class Cheque(db.Model):
    __tablename__ = 'cheques'
        
    id = db.Column(
                db.Integer,
                primary_key= True
            )
    
    post_date = db.Column(
            db.String(200),
            default = JalaliDateTime.now().strftime("%Y/%m/%d -- %H:%M"))
    
    price = db.Column(
            db.BigInteger,
            nullable = False
            )
    
    """
        Foreign Keys Section
    """
    bank_id = db.Column(
        db.Integer,
        db.ForeignKey('banks.id'),
        nullable = False    
        )
    
    company_id = db.Column(
        db.Integer,
        db.ForeignKey('Companies.id'),
        nullable = False    
        ) 
    
class Requisition(db.Model):
    __tablename__ = 'requisitions'
        
    id = db.Column(
                db.Integer,
                primary_key= True
            )
    
    date = db.Column(
            db.String(200),
            default = JalaliDateTime.now().strftime("%Y/%m/%d -- %H:%M"))
    
    price = db.Column(
            db.BigInteger,
            nullable = False
            )
    
    """
        Foreign Keys Section
    """
    bank_id = db.Column(
                db.Integer,
                db.ForeignKey('banks.id'),
                nullable = False    
            )
    
    company_id = db.Column(
        db.Integer,
        db.ForeignKey('Companies.id'),
        nullable = False    
        ) 
            

# acounting document
class Voucher(db.Model):
    __tablename__ = 'vouchers'
    
    id = db.Column(
            db.Integer,
            primary_key= True
        )
    
    tax_number = db.Column(
        db.String(30),
        nullable = False
    )
    
    date = db.Column(
        db.String(200),
        default = JalaliDateTime.now().strftime("%Y/%m/%d -- %H:%M"))
    
    is_cheque = db.Column(
        db.Boolean,
        default= False
    )
    
    is_liquisition = db.Column(
        db.Boolean,
        default= False
    )
    
    price = db.Column(
        db.String(20),
        nullable = False
    )
    
    """
    Foreign Keys Section
    """
    company_id = db.Column(
        db.Integer,
        db.ForeignKey('Companies.id'),
        nullable = False    
    )
    
    
    
    
    