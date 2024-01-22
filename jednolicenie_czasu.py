import time

def silnia(n):
    s = 1
    for i in range(2, n+1):
        s *= i
    return s

universal_factor = 9.201552391052246          # wynik dla Ryzen 5 4500U działającego na baterii

start_time = time.time()
result = silnia(150000)
end_time = time.time()

print(f"Czas wykonania obliczeń: {end_time - start_time} sekund")

your_factor = universal_factor / (end_time-start_time)

print(f"Twój czynnik uśredniający do obliczeń czasu wynosi: ", your_factor)
