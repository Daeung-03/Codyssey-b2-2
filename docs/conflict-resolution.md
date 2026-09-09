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

## 충돌 기록 #2 — 파일 이름 변경 vs 내용 수정

### 참여자
- 해결·작성: 김정현 (@kimjexnghyexn)
- 상대: 대웅 (@Daeung-03)

### 상황
- 대웅: `notes/python-functions.md` → `notes/python-functions-note.md` 로 이름 변경 후 먼저 머지 (PR #22)
- 김정현: 같은 pre-rename 커밋(c59eeb7)에서 시작해서 **옛 이름 파일**의 내용에 "type hint 심화" 섹션 추가
- 예상 결과: `modify/delete` 충돌
- **실제 결과: 충돌 없이 자동 병합됨**

### 실행한 명령과 출력
\`\`\`bash
$ git checkout docs/kimjexnghyexn-python-functions-fix
$ git pull origin main
Auto-merging notes/python-functions.md
# CONFLICT 없이 병합 커밋 메시지 입력 화면으로 바로 넘어감

$ git status
On branch docs/kimjexnghyexn-python-functions-fix
nothing to commit, working tree clean

$ ls notes/ | grep python-functions
python-functions-note.md
\`\`\`

`notes/python-functions.md`(옛 이름)는 사라졌고, `notes/python-functions-note.md`(새 이름) 안에 내가 추가한 "type hint 심화" 섹션이 그대로 들어가 있는 것을 확인했다.

### 왜 충돌이 안 났는가
Git의 merge는 파일 삭제 + 새 파일 추가가 동시에 일어나면, 두 파일의 내용 유사도를 비교해서 "이건 이름만 바뀐 것(rename)"인지 자동으로 판단한다 (rename detection). 대웅의 rename 커밋은 내용을 전혀 바꾸지 않았기 때문에 유사도가 100%였고, Git은 이를 rename으로 인식했다. 그 다음 내가 옛 이름 파일에 추가한 내용(작은 텍스트 블록)을 새 이름 파일에 그대로 적용할 수 있었기 때문에(패치가 깨끗하게 들어맞았기 때문에), 사람이 개입할 필요 없이 자동으로 병합이 완료됐다.

즉 "한쪽은 이름 변경, 한쪽은 내용 수정"이 항상 충돌로 이어지는 건 아니며, 변경 내용이 작고 명확할수록 Git이 알아서 처리해줄 가능성이 높다는 것을 직접 확인했다.

### 만약 진짜 충돌을 내고 싶다면
- 수정량을 rename 유사도 기준(기본 50%) 아래로 크게 만들거나
- `git merge -X no-renames` 또는 `git config diff.renames false`로 rename 탐지 자체를 꺼서 강제로 delete/modify 충돌을 유도할 수 있다.

### 주의할 점
자동 병합이 항상 "의도대로" 되는 건 아니므로, rename이 걸린 파일을 다룰 때는 병합 후 반드시 내용을 직접 열어서 검증해야 한다. 이번엔 내용이 올바르게 들어갔지만, 더 복잡한 수정이었다면 자동 병합 결과가 의도와 다를 수 있다.

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
