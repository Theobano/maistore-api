""" 
    imports all model before app begins to run.
"""
from models.users import UserModel
from models.store import StoreModel
from models.bitcoin import BitcoinPayModel
from models.cardpay import CardpayModel
from models.favoritestore import FavStoreModel
from models.cartsystem import CartSystemModel
from models.product import ProductModel
from models.storelocation import StorelocModel
from models.storeemail import StoreemailModel
from models.storephone import StorephoneModel
from models.cartproduct import CartProductModel
from models.productcat import ProductCatModel
from models.productcol import ProductColorModel
from models.productsize import ProductSizeModel
from models.review import ReviewModel
from models.confirmation import ConfirmationModel
from models.forgot_password import ForgotPasswordModel
