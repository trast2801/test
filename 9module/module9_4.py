def all_variants(text, ind=0):

    for i in range(0, len(text)+1):
        j = i+1
        for k in range(j, len(text)+1):
#            print(f' i={i} j= {j} {text[i:k]} ') просморт вывода для понимания
            yield text[i:k]


print(sorted(list(all_variants('abc')), key = len))
