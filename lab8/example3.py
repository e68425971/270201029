import time

def waiter(n):
    if n == 0:
        print("FİNİTO!")
        return 0
    else:
        print(f"You will waite {n}")
        time.sleep(n)
        return waiter(n-1)