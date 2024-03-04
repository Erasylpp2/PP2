import time
import math

def square_root_after_milliseconds(number, milliseconds):
    time.sleep(milliseconds / 1000)
    return math.sqrt(number)

number = float(input("Enter a number: "))
milliseconds = int(input("Enter milliseconds to wait: "))

start_time = time.time()
result = square_root_after_milliseconds(number, milliseconds)
end_time = time.time()

print(f"Square root of {number} after {milliseconds} milliseconds is {result:.15f}")
print(f"Time taken: {end_time - start_time:.6f} seconds")
