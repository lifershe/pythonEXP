a = input("Enter any: ")
b = str(a)[::-1]

def rev():
    print(f"INPUT: {a}")
    print(f'OUTPUT: {b.upper()} ({len(b)} characters)')


rev();