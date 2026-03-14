def offer(**customer):
    eligible = {}
    eligible = set(eligible)
    for name, age in customer.items():
        if age >= 18:
            eligible.add(name)
    return eligible

print(offer(Aijaz = 14, Bill_Gates = 80, Saleem = 10, Aadil = 8))
