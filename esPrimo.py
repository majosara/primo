def es_primo(n):
    count = 0
    primo = True
    i = 1
    while i<=n:
        if n%1 == 0:
            count = count + 1
