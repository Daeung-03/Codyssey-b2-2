# Conflict Resolution Log

충돌 해결 기록입니다. **해결한 사람이 작성**하고, PR 머지 직후에 남깁니다.

- 팀 전체 최소 기준: 충돌 기록 **2건 이상**, 그중 **1건 이상은 비자명 충돌**
- 비자명 충돌 = 같은 파일 같은 위치를 다르게 수정 / 한쪽은 파일 이동·삭제 + 한쪽은 내용 수정
- 시나리오와 명령어는 [README 6번](../README.md#6-충돌-실습-일부러-만드는-것)에 있습니다

| # | 유형 | 파일 | 해결·작성 | 상대 | 예정 | 상태 |
|---|---|---|---|---|---|---|
| 1 | 같은 위치 동시 수정 | `notes/README.md` | 김승우 | 김정현 | Day 2 | ☐ |
| 2 | 이름 변경 vs 내용 수정 | `notes/python-functions.md` | 김정현 | 대웅 | Day 3 | ☐ |

---

## 충돌 기록 #1 — 같은 위치를 동시에 수정

### 참여자
- 해결·작성: 김승우 (@stevenkim18)
- 상대: 김정현 (@kimjexnghyexn)

### 상황
- 내 브랜치: `docs/stevenkim18-pr-review`
- 상대 브랜치: `docs/kimjexnghyexn-github-flow` (main에 먼저 머지됨)
- 파일: `notes/README.md`
- 원인: 새 노트는 목차 표 맨 아래에 한 줄 추가하는 규칙이라, 둘이 같은 main에서 시작해서 같은 위치에 각자 한 줄을 넣었다.

### 충돌 내용

```txt
<<<<<<< HEAD
| github-pr-review | 김승우 | ... |
=======
| github-flow | 김정현 | ... |
>>>>>>> origin/main
```

<!-- TODO: 실제 git diff 결과 그대로 붙여넣기 -->

- `<<<<<<< HEAD` ~ `=======` : 내 브랜치 내용
- `=======` ~ `>>>>>>> origin/main` : 가져오는 쪽(정현) 내용

### 해결 과정
- 고른 방법: **둘 다 살리기(keep both)**
- 이유: 목차는 두 노트 다 있어야 하고, 한쪽을 지우면 상대 작업이 목차에서 사라진다

```bash
git pull origin main
# CONFLICT (content): Merge conflict in notes/README.md
git status
git diff                    # 마커 확인
# 마커 지우고 두 줄 다 남김
git add notes/README.md
git commit
git push origin docs/stevenkim18-pr-review
```

### 결과
- 목차에 두 노트 다 등록된 상태로 머지
- PR: <링크>
- 머지 커밋: <링크>

### 배운 점
<!-- TODO: 예방책 쓰기. 예) 목차 건드리기 전에 단톡방에 공유한다 -->

## 충돌 기록 # 1-1 - 같은 위치를 동시에 수정

### 상대
김정현 (docs/kimjexnghyexn-github-flow) ↔ 대웅 (git-basics, 먼저 머지됨)

### 상황
notes/README.md의 "작성 완료" 표 맨 아래(주석 바로 위)에, 정현은 github-flow 노트를 등록하려 하고, 대웅은 git-basics 노트를 등록하려 하면서 같은 위치에 줄을 추가함. 대웅 쪽이 먼저 main에 머지되어 있는 상태에서 정현이 `git pull origin main`을 실행하며 충돌 발생.

### 마커 원문
\`\`\`
| Git | [git-branch](./git-branch.md) | 김정현 | 브랜치는 커밋을 가리키는 포인터일 뿐이다 |
<<<<<<< HEAD
| GitHub | [github-flow](./github-flow.md) | 김정현 | GitHub Flow는 main과 작업 브랜치만 쓰는 단순한 협업 전략이다 |
=======
| Git | [git-basics](./git-basics.md) | 대웅 | add로 고른 변경을 commit으로 저장소에 기록한다 |
>>>>>>> 8abaf7b8decf46b1c56f31ac8dd32bd50fd46b44
\`\`\`

### 실행한 명령
\`\`\`bash
git checkout docs/kimjexnghyexn-github-flow
git config pull.rebase false
git pull origin main
# CONFLICT (content): Merge conflict in notes/README.md

# notes/README.md 직접 열어서 마커 지우고 두 줄 다 남김
git add notes/README.md
git commit
# 9e99654 Merge branch 'main' ... into docs/kimjexnghyexn-github-flow
git push origin docs/kimjexnghyexn-github-flow
\`\`\`

### 어느 쪽을 왜 골랐나
양쪽 다 유효한 작업(서로 다른 노트를 등록하는 것)이라 한쪽을 버리지 않고 두 줄 다 살렸다. 표 안에서 분류(Git/GitHub)별로 묶이도록 git-basics를 먼저, github-flow를 뒤에 배치했다.

### PR 링크
https://github.com/Daeung-03/Codyssey-b2-2/pull/5

## 충돌 기록 # 1-2 — 같은 위치를 동시에 수정

### 상대
김정현 (github-flow, 먼저 머지됨) ↔ 김정현 (python-functions, 나중에 충돌 발견)

### 상황
python-functions 브랜치를 github-flow가 머지되기 전 시점의 main에서 시작해서, notes/README.md의 "작성 완료" 표 맨 아래(주석 바로 위)에 각각 다른 노트 줄을 추가하게 됨. python-functions PR을 올린 뒤 main과 비교하는 과정에서 자동 병합이 안 되는 것을 확인하고, 리뷰 전에 미리 로컬에서 충돌을 해결함.

### 마커 원문
\`\`\`
<<<<<<< HEAD
| Python | [python-functions](./python-functions.md) | 김정현 | 함수는 def로 정의하고 return으로 반환하며, type hint는 just 힌트다 |
=======
| GitHub | [github-flow](./github-flow.md) | 김정현 | GitHub Flow는 main과 작업 브랜치만 쓰는 단순한 협업 전략이다 |
>>>>>>> 2781448e0a0cf8e60b5ca13537e16bb957d8b1ff
\`\`\`

### 실행한 명령
\`\`\`bash
git checkout docs/kimjexnghyexn-python-functions
git pull origin main
# CONFLICT (content): Merge conflict in notes/README.md

# notes/README.md 직접 열어서 마커 지우고 두 줄 다 남김
git add notes/README.md
git commit
# Merge branch 'main' into docs/kimjexnghyexn-python-functions
git push origin docs/kimjexnghyexn-python-functions
\`\`\`

### 어느 쪽을 왜 골랐나
두 줄 다 유효한 각자의 노트 등록 내용이라 하나도 버리지 않고 둘 다 살렸다. github-flow가 main에 먼저 들어가 있었으므로 그 줄을 위에, python-functions를 아래에 배치했다.

### 주의할 점
같은 사람(정현)이 여러 브랜치를 동시에 열어두고 작업하면, 먼저 머지된 자기 작업과도 이렇게 충돌할 수 있다는 걸 확인했다. 새 브랜치를 팔 때마다 `git pull origin main`으로 최신 상태를 받은 뒤 시작하면 이런 충돌을 줄일 수 있다.

### PR 링크
https://github.com/Daeung-03/Codyssey-b2-2/pull/20
---

## 충돌 기록 #2 — 파일 이름 변경 vs 내용 수정

### 참여자
- 해결·작성: 김정현 (@kimjexnghyexn)
- 상대: 대웅 (@Daeung-03)

### 상황
- 대웅: `notes/python-functions.md` → `notes/python-functions-note.md` 로 이름 변경 후 먼저 머지
- 김정현: 같은 main에서 시작해서 **옛 이름 파일**의 내용을 수정
- 결과: `modify/delete` 충돌

### 충돌 내용

```txt
CONFLICT (modify/delete): notes/python-functions.md deleted in origin/main
and modified in HEAD.
```

> 이 유형은 **파일 안에 마커가 안 생깁니다.** 한쪽엔 파일이 없고 한쪽은 고쳤다는 사실만 알려주고,
> 어느 쪽이 맞는지는 사람이 정해야 해서 비자명 충돌입니다.

### 해결 과정
- 고른 방법: **이름 변경 받아들이고, 내 수정 내용을 새 파일로 옮기기**
- 이유: 파일명 규칙은 이미 팀에서 머지된 결정이니 따라야 하고, 내가 쓴 내용도 없어지면 안 된다

```bash
git pull origin main
git status                  # deleted by them: notes/python-functions.md
# 내가 쓴 내용을 notes/python-functions-note.md 에 옮겨 붙이기
git rm notes/python-functions.md
git add notes/python-functions-note.md
git commit
git push origin docs/kimjexnghyexn-python-functions-fix
```

### 결과
- 파일명 규칙과 내 수정 내용이 둘 다 살아남음
- PR: <링크>
- 머지 커밋: <링크>

### 배운 점
<!-- TODO: 예) 파일 이름 바꾸는 PR은 남이 그 파일 작업 중일 때 올리지 않는다.
     마커가 안 생겨서 조용히 작업이 사라질 수 있으니 git status를 꼭 읽는다 -->

---

<!-- 충돌이 더 생기면 아래에 같은 형식으로 추가 -->
