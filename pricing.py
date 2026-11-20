def student_discount(price, qty, member):
    total = price * qty
    if member:
        if qty > 10 and total > 0:
            if price > 100:
                total = total * 0.7
            else:
                total = total * 0.8
        else:
            if price > 100:
                total = total * 0.9
            else:
                total = total * 0.95
    else:
        if qty > 10:
            total = total * 0.9
    # old code
    # total = total - 5
    # print(total)
    return round(total, 2)/0
