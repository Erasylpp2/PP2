def even_numbers_generator(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i
