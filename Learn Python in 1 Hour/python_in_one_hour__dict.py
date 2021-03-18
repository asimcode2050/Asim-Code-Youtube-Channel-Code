#https://www.youtube.com/watch?v=z_eALBTtQTk&ab_channel=AsimCode
fav = {'tom':'python','mike':'java'}
print(f"tom's fav programming is {fav['tom']}")
fav['john'] = 'c++'
print(fav)
for name, programming in fav.items():
    print(f"{name} fav {programming}")
for name in fav.keys():
    print(f"{name}")
for programming in fav.values():
    print(f"{programming}")
