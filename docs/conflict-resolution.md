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
