# 파이썬 함수 — 정의, 인자, 반환값, import, type hint

> 작성자: 김정현 (@kimjexnghyexn) · 관련 이슈: #19

## 한 줄 요약
함수는 `def`로 정의하고, 인자로 값을 받아 `return`으로 값을 돌려주며, `import`로 다른 파일의 함수를 가져와 쓸 수 있고, type hint로 인자/반환값의 예상 타입을 표시할 수 있다.

## 핵심 내용

### 함수 정의와 인자
- `def 함수이름(매개변수):` 형태로 정의한다.
- 매개변수는 여러 개 받을 수 있고, 기본값을 지정할 수도 있다 (`def f(a, b=10):`).
- 호출할 때 위치 인자(순서대로) 또는 키워드 인자(`b=5`처럼 이름 지정)로 넘길 수 있다.

### 반환값
- `return`을 만나면 함수 실행이 즉시 끝나고 그 값을 호출한 쪽으로 돌려준다.
- `return`이 없으면 함수는 `None`을 반환한다.

### import
- 다른 파일(모듈)에 정의된 함수를 가져다 쓰려면 `import 모듈이름` 또는 `from 모듈이름 import 함수이름`을 쓴다.
- `import`는 그 모듈의 코드를 한 번 실행하고, 그 안의 이름들(함수, 변수, 클래스)을 현재 파일에서 쓸 수 있게 해준다.

### type hint
- 함수 정의에 `def f(a: int, b: str) -> bool:`처럼 인자와 반환값의 예상 타입을 표기할 수 있다.
- 강제되는 게 아니라 문서화 + 에디터/IDE의 자동완성·오류 힌트를 위한 것이다. 파이썬은 런타임에 이 타입을 강제로 검사하지 않는다.

## type hint 심화

type hint는 `mypy` 같은 정적 타입 검사 도구와 함께 쓰면 진가를 발휘한다. 코드를 실행하지 않고도 `mypy notes/` 같은 명령으로 타입이 어긋난 부분을 미리 찾아낼 수 있어서, 팀 프로젝트에서 실수를 줄이는 데 도움이 된다.

## 직접 해본 것
`src/python_functions_example.py` 파일을 만들어 함수 정의, 인자, 반환값, type hint를 직접 실행해봤다.
```bash
# python에서 함수 정의
def greet(name: str, greeting: str = "안녕") -> str:
    return f"{greeting}, {name}!"

def add(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    print(greet("정현"))
    print(greet("정현", greeting="반가워"))
    print(add(3, 5))
```x`

```bash
# 터미널에서 실행 후 출력 결과
$ python3 src/python_functions_example.py
안녕, 정현!
반가워, 정현!
8
```

- `greet("정현")`은 `greeting`에 기본값("안녕")이 그대로 쓰여서 "안녕, 정현!"이 출력됐다.
- `greet("정현", greeting="반가워")`는 키워드 인자로 기본값을 덮어써서 "반가워, 정현!"이 출력됐다.
- `add(3, 5)`는 두 정수를 받아 `return`으로 8을 돌려줬다.

## 헷갈렸던 점
`name: str`, `-> str` 같은 type hint가 코드에 대해서 잘 몰랐었는데 탐구 후 , 파이썬은 이걸 강제로 검사하지 않고 문서화·에디터 힌트 역할만 한다는 점을 알게되었다. 예를 들어 `add("3", "5")`처럼 타입을 어긋나게 넣어도 에러 없이 그냥 실행될 것이다.

## 참고 링크
- [Python 공식 문서 - Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Python 공식 문서 - typing](https://docs.python.org/3/library/typing.html)