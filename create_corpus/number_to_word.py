import inflect
p = inflect.engine()
num_set = set()
for i in range(1000000):
    if i % 10 == 0:
        d = p.number_to_words(i)
        d = d.replace("-"," ")
        d = d.split(' ')
        num_set.update(set(d))
#print(num_set)

for i in num_set:
    print (i)
