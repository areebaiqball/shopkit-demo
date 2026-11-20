def weekly_report(orders):
    lines = []
    total = 0
    for order in orders:
        name = order["name"]
        amount = order["amount"]
        tax = amount * 0.17
        net = amount - tax
        total += net
        lines.append(name + ": " + str(round(net, 2)))
    lines.append("TOTAL: " + str(round(total, 2)))
    header = "REPORT"
    return header + "\n" + "\n".join(lines)


def monthly_report(orders):
    lines = []
    total = 0
    for order in orders:
        name = order["name"]
        amount = order["amount"]
        tax = amount * 0.17
        net = amount - tax
        total += net
        lines.append(name + ": " + str(round(net, 2)))
    lines.append("TOTAL: " + str(round(total, 2)))
    header = "REPORT"
    return header + "\n" + "\n".join(lines)
