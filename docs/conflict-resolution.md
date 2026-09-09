# Conflict Resolution Log

충돌 해결 기록입니다. **해결한 사람이 작성**하고, PR 머지 직후에 남깁니다.

- 팀 전체 최소 기준: 충돌 기록 **2건 이상**, 그중 **1건 이상은 비자명 충돌**
- 비자명 충돌 = 같은 파일 같은 위치를 다르게 수정 / 한쪽은 파일 이동·삭제 + 한쪽은 내용 수정
- 시나리오와 명령어는 [README 6번](../README.md#6-충돌-실습-일부러-만드는-것)에 있습니다

| # | 유형 | 파일 | 해결·작성 | 상대 | 예정 | 상태 |
|---|---|---|---|---|---|---|
| 1 | 같은 위치 동시 수정 | `notes/README.md` | 김승우 | 김정현 | Day 2 | ✅ |
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

### 실제 발생한 출력

기본 <code>git pull origin main</code>은 이 저장소에 pull 방식이 설정되지 않았다는 안내만 출력하고 병합을 시작하지 않았다. 팀의 merge commit 규칙에 맞게 <code>git pull --no-rebase origin main</code>을 실행해 병합을 시작했고, 다음 충돌이 발생했다.

~~~txt
Auto-merging notes/README.md
CONFLICT (content): Merge conflict in notes/README.md
Automatic merge failed; fix conflicts and then commit the result.
~~~

<code>git status --short</code>에서 <code>UU notes/README.md</code>를 확인했다. 다른 파일은 <code>main</code>에서 자동 병합된 변경이며, 충돌 파일은 이 목차 하나였다. <code>git diff --no-ext-diff</code>의 실제 출력은 다음과 같다.

~~~txt
diff --cc notes/README.md
index 8388659,e0ee701..0000000
--- a/notes/README.md
+++ b/notes/README.md
@@@ -25,5 -25,7 +25,11 @@@
  |---|---|---|---|
  | Git | [git-branch](./git-branch.md) | 김정현 | 브랜치는 커밋을 가리키는 포인터일 뿐이다 |
  | Git | [git-basics](./git-basics.md) | 대웅 | add로 고른 변경을 commit으로 저장소에 기록한다 |
++<<<<<<< HEAD
 +| GitHub | [github-pr-review](./github-pr-review.md) | 김승우 | PR은 이슈와 변경을 검토한 뒤 main에 병합하는 협업 단위다 |
++=======
+ | GitHub | [github-flow](./github-flow.md) | 김정현 | GitHub Flow는 main과 작업 브랜치만 쓰는 단순한 협업 전략이다 |
+ | Python | [python-functions](./python-functions.md) | 김정현 | 함수는 def로 정의하고 return으로 반환하며, type hint는 just 힌트다 |
+ | Python | [python-basics](./python-basics.md) | 대웅 | 변수와 타입을 확인하고 조건문과 반복문으로 흐름을 제어한다 |
++>>>>>>> c59eeb7dd435b69751525605846d9f5581780ea7
  <!-- 새 줄은 이 주석 바로 위에 추가하세요 -->
~~~

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
- GitHub Flow, PR 리뷰, Python 함수, Python 기초 노트의 목차 행을 모두 보존했다.
- PR: https://github.com/Daeung-03/Codyssey-b2-2/pull/17
- 해결은 <code>docs/stevenkim18-pr-review</code> 브랜치에서 수행하고 PR을 갱신했다.

### 배운 점
같은 표의 맨 아래에 행을 추가하는 작업은 서로 다른 내용이어도 같은 hunk를 수정하므로 충돌할 수 있다. 새 브랜치를 만들기 전에 최신 <code>main</code>을 반영하고, 충돌이 나면 마커의 양쪽 내용을 확인한 뒤 유효한 행을 모두 남긴다.

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

## 추가 충돌 기록 A-2 — PR #10 Python 목차 병합

### 참여자
- 해결·작성: 김대웅 (@Daeung-03)
- 상대 변경: `origin/main`의 `git-basics`, `github-flow` 목차 항목

### 상황
- 내 브랜치: `docs/daeung-03-python-basics`
- 파일: `notes/README.md`
- 원인: 내 브랜치와 `main`이 작성 완료 표의 같은 위치에 서로 다른 목차 행을 추가했다.

### 충돌 내용

```txt
<<<<<<< HEAD
| Python | [python-basics](./python-basics.md) | 대웅 | 변수와 타입을 확인하고 조건문과 반복문으로 흐름을 제어한다 |
=======
| Git | [git-basics](./git-basics.md) | 대웅 | add로 고른 변경을 commit으로 저장소에 기록한다 |
| GitHub | [github-flow](./github-flow.md) | 김정현 | GitHub Flow는 main과 작업 브랜치만 쓰는 단순한 협업 전략이다 |
>>>>>>> origin/main
```

### 해결 과정
- 고른 방법: **양쪽 목차 행 모두 유지(keep both)**
- 이유: 세 행이 서로 다른 노트를 가리키므로 어느 한쪽을 버리면 유효한 노트가 목차에서 누락된다.

```bash
git fetch origin --prune
git merge --no-edit origin/main
# CONFLICT (content): Merge conflict in notes/README.md
git status --short
# 마커를 제거하고 main의 두 행과 python-basics 행을 모두 유지
git add notes/README.md
git commit --no-edit
git push origin docs/daeung-03-python-basics
```

### 결과
- `git-basics`, `github-flow`, `python-basics` 목차 행을 모두 보존했다.
- PR: https://github.com/Daeung-03/Codyssey-b2-2/pull/10
- 해결 커밋: https://github.com/Daeung-03/Codyssey-b2-2/commit/38a20f59524d60614f57544a3de2d94e5a49cfdb

### 배운 점
목차처럼 여러 브랜치가 같은 삽입 위치를 수정하는 파일은 병합 전에 최신 `main`을 확인하고, 충돌 시 각 행의 의미를 확인한 뒤 유효한 항목을 모두 보존해야 한다.

---

## 추가 충돌 기록 A-2 후속 — PR #10과 #20 목차 재병합

### 상황
- 해결·작성: 김대웅 (@Daeung-03)
- 내 브랜치: `docs/daeung-03-python-basics`
- 상대 변경: PR #20 머지로 `origin/main`에 추가된 `python-functions` 목차 항목
- 파일: `notes/README.md`
- 원인: 첫 충돌을 해결한 뒤 PR #20이 먼저 머지되어 작성 완료 표의 같은 위치가 다시 변경됐다.

### 충돌 내용

```txt
<<<<<<< HEAD
| Python | [python-basics](./python-basics.md) | 대웅 | 변수와 타입을 확인하고 조건문과 반복문으로 흐름을 제어한다 |
=======
| Python | [python-functions](./python-functions.md) | 김정현 | 함수는 def로 정의하고 return으로 반환하며, type hint는 just 힌트다 |
>>>>>>> origin/main
```

### 해결 과정과 결과
- 고른 방법: **양쪽 목차 행 모두 유지(keep both)**
- 이유: 두 행이 서로 다른 유효한 Python 노트를 가리키므로 모두 목차에 필요하다.

```bash
git fetch origin --prune
git merge --no-edit origin/main
# CONFLICT (content): Merge conflict in notes/README.md
git status --short
# 마커를 제거하고 python-functions와 python-basics 행을 모두 유지
git add notes/README.md
git commit --no-edit
```

- PR: https://github.com/Daeung-03/Codyssey-b2-2/pull/10
- 해결 커밋: https://github.com/Daeung-03/Codyssey-b2-2/commit/e65ffb5

---

## 추가 충돌 기록 A-1 — PR #8 Git 되돌리기 목차 병합

### 참여자
- 해결·작성: 김대웅 (@Daeung-03)
- 상대 변경: `origin/main`의 `git-basics`, `github-flow` 목차 항목

### 상황
- 내 브랜치: `docs/daeung-03-git-undo`
- 파일: `notes/README.md`
- 원인: 내 브랜치와 `main`이 작성 완료 표의 같은 위치에 서로 다른 목차 행을 추가했다.

### 충돌 내용

```txt
<<<<<<< HEAD
| Git | [git-undo](./git-undo.md) | 대웅 | 공유 전에는 reset·amend, 공유 후에는 revert로 안전하게 되돌린다 |
=======
| Git | [git-basics](./git-basics.md) | 대웅 | add로 고른 변경을 commit으로 저장소에 기록한다 |
| GitHub | [github-flow](./github-flow.md) | 김정현 | GitHub Flow는 main과 작업 브랜치만 쓰는 단순한 협업 전략이다 |
>>>>>>> origin/main
```

### 해결 과정
- 고른 방법: **양쪽 목차 행 모두 유지(keep both)**
- 이유: 세 행이 서로 다른 노트를 가리키므로 어느 한쪽을 버리면 유효한 노트가 목차에서 누락된다.

```bash
git fetch origin --prune
git switch docs/daeung-03-git-undo
git merge --no-edit origin/main
# CONFLICT (content): Merge conflict in notes/README.md
git status --short
# 마커를 제거하고 main의 두 행과 git-undo 행을 모두 유지
git add notes/README.md
git commit --no-edit
git push origin docs/daeung-03-git-undo
```

### 결과
- `git-basics`, `github-flow`, `git-undo` 목차 행을 모두 보존했다.
- PR: https://github.com/Daeung-03/Codyssey-b2-2/pull/8
- 해결 커밋: https://github.com/Daeung-03/Codyssey-b2-2/commit/c0fd9e55a9cba82eb28da3146656973210018167

### 배운 점
목차처럼 공동 편집 지점이 있는 파일은 작업 전에 최신 `main`을 받고, 충돌 시 상대 변경을 삭제하지 말고 각 항목의 목적을 확인해 병합해야 한다.

---

## 추가 충돌 기록 A-1 후속 — PR #8과 #20 목차 재병합

### 상황
- 해결·작성: 김대웅 (@Daeung-03)
- 내 브랜치: `docs/daeung-03-git-undo`
- 상대 변경: PR #20 머지로 `origin/main`에 추가된 `python-functions` 목차 항목
- 파일: `notes/README.md`
- 원인: 첫 충돌을 해결한 뒤 PR #20이 먼저 머지되어 작성 완료 표의 같은 위치가 다시 변경됐다.

### 충돌 내용

```txt
<<<<<<< HEAD
| Git | [git-undo](./git-undo.md) | 대웅 | 공유 전에는 reset·amend, 공유 후에는 revert로 안전하게 되돌린다 |
=======
| Python | [python-functions](./python-functions.md) | 김정현 | 함수는 def로 정의하고 return으로 반환하며, type hint는 just 힌트다 |
>>>>>>> origin/main
```

### 해결 과정과 결과
- 고른 방법: **양쪽 목차 행 모두 유지(keep both)**
- 이유: 두 행이 서로 다른 유효한 노트를 가리키므로 모두 목차에 필요하다.

```bash
git fetch origin --prune
git merge --no-edit origin/main
# CONFLICT (content): Merge conflict in notes/README.md
git status --short
# 마커를 제거하고 python-functions와 git-undo 행을 모두 유지
git add notes/README.md
git commit --no-edit
```

- PR: https://github.com/Daeung-03/Codyssey-b2-2/pull/8
- 해결 커밋: https://github.com/Daeung-03/Codyssey-b2-2/commit/e998777

---

<!-- 충돌이 더 생기면 아래에 같은 형식으로 추가 -->
