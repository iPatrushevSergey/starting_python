# Эта программа считает доходы/убытки при покупке акций.
COUNT_SHARES = 2000
COST_ONE_SHARE_PURCHASE = 40.00
COST_ONE_SHARE_SALE = 42.75
COMMISSION = 0.03

amount_purchase = COUNT_SHARES * COST_ONE_SHARE_PURCHASE
amount_commission_purchase = amount_purchase * COMMISSION
amount_sale = COUNT_SHARES * COST_ONE_SHARE_SALE
amount_commission_sale = amount_sale * COMMISSION
amount_after_sale = (
    amount_sale - amount_commission_sale - amount_commission_purchase
    ) - amount_purchase

print(amount_purchase)
print(amount_commission_purchase)
print(amount_sale)
print(amount_commission_sale)
print(amount_after_sale)

if amount_after_sale > 0:
    print(f'Джо получил прибыль в сумме {amount_after_sale:.2f}')
else:
    print(f'Джо понёс убытки в сумме: {amount_after_sale:.2f}')
