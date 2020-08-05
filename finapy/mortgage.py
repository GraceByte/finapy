def calc_payment(
    sale_price: float, down_payment: float, loan_term_yrs: int, interest_rate_pct: float
):
    loan_amount = sale_price - down_payment
    num_loan_payments = loan_term_yrs * 12
    interest_rate_float = interest_rate_pct / 100
    r = 1 + (interest_rate_float / 12)
    monthly_payment = round(
        loan_amount * (r ** num_loan_payments) * (1 - r) / (1 - r ** num_loan_payments),
        2,
    )

    interest_vector = []
    principal_vector = []
    balance_vector = []

    temp_loan_amount = loan_amount
    for i in range(1, num_loan_payments + 1):
        interest = round(temp_loan_amount * (r - 1), 2)
        principal = round(monthly_payment - interest, 2)
        temp_loan_amount = round(temp_loan_amount - (monthly_payment - interest), 2)

        interest_vector.append(interest)
        principal_vector.append(principal)
        balance_vector.append(temp_loan_amount)

        if i == num_loan_payments:
            principal = round(principal + temp_loan_amount, 2)
            temp_loan_amount = 0

    return monthly_payment, interest_vector, principal_vector, balance_vector
