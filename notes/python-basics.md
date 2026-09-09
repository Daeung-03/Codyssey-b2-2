# Python 기초: 변수, 조건문, 반복문

> 작성자: 대웅 (@Daeung-03) · 관련 이슈: #9

## 한 줄 요약

Python은 이름에 값을 대입해 데이터를 다루고, 조건문으로 실행할 코드를 선택하며, 반복문으로 같은 작업을 여러 번 수행한다.

## 핵심 내용

### Python 버전 확인

이 프로젝트의 실행 환경은 Python 3.10 이상이다. 터미널에서 다음 명령으로 현재 버전을 확인할 수 있다.

```bash
python3 --version
```

macOS에서는 `python` 대신 `python3` 명령을 사용해야 하는 경우가 많다. 버전의 앞 두 숫자가 3.10 이상인지 확인한다.

### 변수와 기본 타입

Python에서는 `이름 = 값` 형태로 변수를 만든다. 변수 이름은 값을 담는 고정된 상자라기보다 **객체를 가리키는 이름**에 가깝다.

```python
course = "Codyssey"
week = 3
```

Python은 동적 타입 언어이므로 같은 이름이 실행 중에 다른 타입의 객체를 다시 가리킬 수 있다. `type(값)`으로 현재 객체의 타입을 확인할 수 있다.

| 타입 | 의미 | 예시 |
|---|---|---|
| `int` | 정수 | `3`, `-1` |
| `float` | 실수 | `92.5`, `3.14` |
| `str` | 문자열 | `"Python"` |
| `bool` | 참 또는 거짓 | `True`, `False` |
| `list` | 순서가 있고 변경 가능한 값의 모음 | `["변수", "조건문"]` |

변수 이름은 숫자로 시작할 수 없고, 대소문자를 구분한다. 여러 단어는 `python_version`처럼 소문자와 밑줄을 사용하는 snake_case가 일반적이다.

### 조건문

조건문은 조건의 참과 거짓에 따라 실행할 코드를 선택한다.

```python
if 조건1:
    조건1이 참일 때 실행
elif 조건2:
    조건1은 거짓이고 조건2가 참일 때 실행
else:
    모든 조건이 거짓일 때 실행
```

- 각 조건 뒤에는 콜론(`:`)을 붙인다.
- 실행할 블록은 같은 깊이로 들여쓴다. 일반적으로 공백 4칸을 사용한다.
- 위에서부터 조건을 검사하고, 처음 참인 블록 하나만 실행한다.
- 비교에는 `==`, `!=`, `>`, `>=`, `<`, `<=`를 사용하고, 여러 조건은 `and`, `or`, `not`으로 조합한다.
- 값이 같은지 비교할 때는 대입 연산자 `=`가 아니라 비교 연산자 `==`를 사용한다.

### 반복문

#### `for` 문

`for` 문은 리스트, 문자열, `range`처럼 여러 값을 차례대로 순회할 때 사용한다.

```python
for 값 in 반복가능한_객체:
    반복할 코드
```

`range(1, 4)`는 시작값 1은 포함하지만 끝값 4는 포함하지 않아 `1, 2, 3`을 만든다. 순서와 값을 함께 사용하려면 `enumerate()`가 편리하다.

#### `while` 문

`while` 문은 조건이 참인 동안 코드를 반복한다.

```python
while 조건:
    반복할 코드
```

반복 블록 안에서 조건에 사용되는 값을 바꾸지 않으면 무한 반복이 생길 수 있다. 실행 전에 종료 조건을 확인해야 한다.

## 직접 해본 것

### 1. Python 3.10 이상 확인

```console
$ python3 --version
Python 3.11.5
```

실습 환경의 Python은 3.11.5이므로 프로젝트 요구사항인 3.10 이상을 충족했다.

### 2. 변수와 타입 확인

다음 코드를 `python3 -c`로 직접 실행했다.

```python
course = "Codyssey"
week = 3
score = 92.5
completed = True
topics = ["변수", "조건문", "반복문"]

values = [
    ("course", course),
    ("week", week),
    ("score", score),
    ("completed", completed),
    ("topics", topics),
]

for name, value in values:
    print(f"{name} = {value!r}, type = {type(value).__name__}")

value = 10
print(f"value = {value!r}, type = {type(value).__name__}")
value = "ten"
print(f"value = {value!r}, type = {type(value).__name__}")
```

실행 결과:

```console
course = 'Codyssey', type = str
week = 3, type = int
score = 92.5, type = float
completed = True, type = bool
topics = ['변수', '조건문', '반복문'], type = list
value = 10, type = int
value = 'ten', type = str
```

각 값의 타입을 확인했고, `value`라는 같은 이름이 정수 `10`에서 문자열 `"ten"`으로 다시 연결될 수 있다는 것도 확인했다.

### 3. 조건문으로 등급 선택

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"

print(f"score={score}, grade={grade}")
```

실행 결과:

```console
score=85, grade=B
```

85는 90 이상이 아니므로 첫 번째 `if`를 지나고, 80 이상인 `elif`가 참이어서 B가 선택됐다. 이후의 `else`는 실행되지 않았다.

### 4. `for`와 `while` 반복

```python
topics = ["변수", "조건문", "반복문"]

for index, topic in enumerate(topics, start=1):
    print(f"{index}. {topic}")

countdown = 3
while countdown > 0:
    print(f"countdown: {countdown}")
    countdown -= 1

print("start!")
```

실행 결과:

```console
1. 변수
2. 조건문
3. 반복문
countdown: 3
countdown: 2
countdown: 1
start!
```

`for` 문은 리스트의 세 값을 한 번씩 순회했다. `while` 문은 반복할 때마다 `countdown`을 1씩 줄였고, 값이 0이 되자 조건이 거짓이 되어 종료됐다.

## 헷갈렸던 점

`=`와 `==`의 역할이 비슷해 보이지만, `=`는 이름에 값을 대입하고 `==`는 두 값이 같은지 비교한다. 또한 Python에서는 중괄호 대신 들여쓰기로 코드 블록을 구분하므로 공백 깊이가 다르면 의도와 다르게 동작하거나 `IndentationError`가 발생한다. `range`의 끝값이 포함되지 않는다는 점과 `while`의 조건값을 직접 바꿔야 종료된다는 점도 반복문을 작성할 때 확인해야 한다.

## 참고 링크

- [Python 공식 튜토리얼 - 인터프리터 사용](https://docs.python.org/3/tutorial/interpreter.html)
- [Python 공식 튜토리얼 - Python 소개](https://docs.python.org/3/tutorial/introduction.html)
- [Python 공식 튜토리얼 - 제어 흐름](https://docs.python.org/3/tutorial/controlflow.html)
- [Python 공식 문서 - 내장 타입](https://docs.python.org/3/library/stdtypes.html)
