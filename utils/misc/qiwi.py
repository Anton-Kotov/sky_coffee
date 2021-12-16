import uuid
from dataclasses import dataclass
from datetime import datetime, timedelta

import pyqiwi

from data.config import QIWI_TOKEN, WALLET_QIWI, QIWI_PUBKEY

wallet = pyqiwi.Wallet(token=QIWI_TOKEN, number=WALLET_QIWI)

class NoPaymentFound(Exception):
    pass

class NotEnoughMoney(Exception):
    pass

@dataclass
class Payment:
    amount: int
    id: str = None

    def create(self):
        self.id = str(uuid.uuid4())  # создание уникального номера

    def check_payment(self):
        transactions = wallet.history(start_date=datetime.now() - timedelta(days=2)).get("transactions")
        for transaction in transactions:
            if transaction.comment:
                if str(self.id) in transaction.comment:
                    if float(transaction.total.amount) >= float(self.amount):
                        return True
                    else:
                        raise NotEnoughMoney
                else:
                    raise NoPaymentFound

    @property
    def invoice(self):
        link = "https://oplata.qiwi.com/create?publicKey={pubkey}&amount={amount}&comment={comment}"
        return link.format(pubkey=QIWI_PUBKEY, amount=self.amount, comment=self.id)