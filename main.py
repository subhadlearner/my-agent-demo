def greet(name: str) -> str:
    return f"Hello, {name}!"


def add_numbers(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    print(greet("World"))
    print(f"5 + 3 = {add_numbers(5, 3)}")