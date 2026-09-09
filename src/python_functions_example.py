def greet(name: str, greeting: str = "안녕") -> str:
    return f"{greeting}, {name}!"

def add(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    print(greet("정현"))
    print(greet("정현", greeting="반가워"))
    print(add(3, 5))