data = [('Car','500.000'),('Book','20'),('cat','x')]
l =[]
for t in data:
    holder =[]
    for i in t:
        if i.isalpha():
            holder.append(i)
        elif i.isdigit():
            holder.append(int(i))
        else:
            holder.append(float(i))
    l.append((holder[0],holder[1]))
print(l)