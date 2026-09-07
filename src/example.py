"""Python 노트에서 참조하는 예시 코드.

실행: python3 src/example.py
"""


def greet(name: str) -> str:
    """이름을 받아 인사말을 돌려준다."""
    return f"안녕하세요, {name}님"


def divide(a: float, b: float) -> float:
    """a를 b로 나눈다. b가 0이면 ZeroDivisionError를 그대로 올린다."""
    return a / b


if __name__ == "__main__":
    print(greet("Codyssey"))

    try:
        print(divide(10, 0))
    except ZeroDivisionError:
        print("0으로는 나눌 수 없습니다")
