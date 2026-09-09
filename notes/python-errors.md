# Python 예외 처리
> 작성자: 김승우 (@stevenkim18) · 관련 이슈: #15

## 한 줄 요약

예외 처리는 실행 중 발생할 수 있는 오류를 예상 가능한 흐름으로 다루는 방법이며, 필요한 예외만 잡고 원인을 알 수 있게 처리해야 한다.

## 핵심 내용

### 예외 처리의 흐름

~~~python
try:
    # 예외가 생길 수 있는 코드
except 특정예외:
    # 해당 예외를 처리하는 코드
else:
    # 예외가 없을 때만 실행하는 코드
finally:
    # 예외 발생 여부와 관계없이 항상 실행하는 코드
~~~

- <code>try</code>에는 실패할 가능성이 있는 최소 범위의 코드를 둔다.
- <code>except</code>는 예상한 예외 유형을 구체적으로 지정해 처리한다.
- <code>else</code>는 <code>try</code>가 성공했을 때만 실행하므로 성공 결과를 사용하는 작업에 알맞다.
- <code>finally</code>는 파일 닫기나 연결 정리처럼 성공·실패와 관계없이 해야 할 마무리 작업에 쓴다.

### 자주 만나는 예외와 <code>raise</code>

| 예외 | 발생 예 | 처리 방향 |
|---|---|---|
| <code>ZeroDivisionError</code> | 0으로 나누기 | 0인지 먼저 검사하거나 사용자에게 이유를 알린다 |
| <code>ValueError</code> | <code>int("three")</code>처럼 값 형식이 맞지 않음 | 올바른 입력을 다시 받거나 검증 실패를 알린다 |
| <code>KeyError</code> | 없는 딕셔너리 키를 조회 | 키 존재 여부를 확인하거나 기본값을 정한다 |

<code>raise</code>는 함수가 처리할 수 없는 잘못된 입력을 호출한 쪽에 명확히 알릴 때 사용한다. 예를 들어 양수만 허용하는 함수가 0 또는 음수를 받으면 <code>raise ValueError(...)</code>로 계약 위반을 알릴 수 있다.

모든 오류를 <code>except Exception:</code>으로 한꺼번에 숨기면 원인을 찾기 어렵다. 예상한 예외만 잡고, 처리할 방법이 없다면 예외가 호출한 쪽까지 전달되게 하는 편이 안전하다.

## 직접 해본 것

Python 버전과 예외 처리 흐름을 직접 실행했다. 첫 번째 나눗셈은 <code>else</code>를 실행하고, 0으로 나누는 두 번째 시도는 <code>ZeroDivisionError</code>를 처리했다. 두 경우 모두 <code>finally</code>가 실행되는 것을 확인했다.

~~~bash
python3 --version

python3 - <<'PY'
def divide(left: int, right: int) -> None:
    try:
        result = left / right
    except ZeroDivisionError as error:
        print(f"ZeroDivisionError 처리: {error}")
    else:
        print(f"나눗셈 결과: {result}")
    finally:
        print("나눗셈 시도 종료")


def require_positive(number: int) -> None:
    if number <= 0:
        raise ValueError("0보다 큰 정수만 허용합니다")


divide(8, 2)
divide(8, 0)

try:
    int("three")
except ValueError as error:
    print(f"ValueError 처리: {error}")

settings: dict[str, str] = {}
try:
    print(settings["token"])
except KeyError as error:
    print(f"KeyError 처리: {error}")

try:
    require_positive(-1)
except ValueError as error:
    print(f"raise한 ValueError 처리: {error}")
PY
~~~

~~~txt
Python 3.13.5
나눗셈 결과: 4.0
나눗셈 시도 종료
ZeroDivisionError 처리: division by zero
나눗셈 시도 종료
ValueError 처리: invalid literal for int() with base 10: 'three'
KeyError 처리: 'token'
raise한 ValueError 처리: 0보다 큰 정수만 허용합니다
~~~

## 헷갈렸던 점

<code>finally</code>는 예외를 해결하는 곳이 아니라 항상 실행해야 할 마무리 작업을 두는 곳이다. 또한 <code>raise ValueError</code>는 프로그램이 실패했다는 뜻만은 아니다. 함수가 허용하는 입력 조건을 호출한 쪽에 분명히 전달하고, 그쪽에서 적절한 처리 방법을 선택하게 하는 방법이다.

## 참고 링크

- [Python 공식 문서 — Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Python 공식 문서 — Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)
- [저장소 예시 코드](../src/example.py)
