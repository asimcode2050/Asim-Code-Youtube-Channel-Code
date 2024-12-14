chocolate_types = ["Caramel", "Hazelnut", "Mint", "Caramel", "Hazelnut"]
sorted_chocolates = [[chocolate for chocolate in chocolate_types if chocolate == flavor]
                     for flavor in set(chocolate_types)]
print(sorted_chocolates)
