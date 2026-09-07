# Troubleshooting Log

Git 되돌리기 4종 실습 기록입니다. 4개 다 해야 하고, **팀원 전원이 최소 1개에는 이름이 들어가야** 합니다.

| # | 시나리오 | 담당 | 상태 |
|---|---|---|---|
| 1 | `git commit --amend` (최근 커밋 메시지 수정) | 김정현 | ☐ |
| 2 | `git reset --soft HEAD~1` (로컬 커밋 취소 + 변경 유지) | 김승우 | ☐ |
| 3 | `git revert` (원격에 push된 커밋 취소) | 대웅 | ☐ |
| 4 | `git stash` / `git stash pop` (작업 보관하고 브랜치 이동) | 대웅 | ☐ |

각 기록에는 **실제 실행한 명령과 출력**을 넣습니다. 안 넣으면 재현이 안 돼서 기록으로 인정 안 됩니다.

---

## 시나리오 1 — `git commit --amend`

### 참여자
김정현 (@kimjexnghyexn) — 실습·기록 / 리뷰: 김대웅

### 상황
커밋 메시지를 `update`라고 써버렸다. 아직 push는 안 했다. 팀 커밋 규칙(`<타입>: <무엇을>`)에 안 맞아서 고쳐야 한다.

### 실행한 명령
```bash
git log --oneline -1
# <해시> update

git commit --amend -m "docs: 브랜치 노트에 HEAD 설명 추가"

git log --oneline -1
# <새 해시> docs: 브랜치 노트에 HEAD 설명 추가
```

<!-- TODO: 실제 출력 붙여넣기 -->

### 결과
- 메시지가 바뀌고 **커밋 해시도 바뀜** (커밋을 새로 만드는 거라서)
- PR/커밋 링크: <링크>

### 왜 이 방법인가
- 아직 push 안 한 커밋이라 히스토리를 고쳐도 남에게 영향이 없다
- 이미 push한 커밋에 `amend`를 하면 force push가 필요해서 팀에 문제가 생긴다 → 그때는 새 커밋으로 고친다

### 주의할 점
- `--amend`는 이전 커밋을 수정하는 게 아니라 **새 커밋으로 교체**하는 것
- 공유 브랜치에 올라간 커밋에는 쓰지 않는다

---

## 시나리오 2 — `git reset --soft HEAD~1`

### 참여자
김승우 (@stevenkim18) — 실습·기록 / 리뷰: 대웅

### 상황
관련 없는 파일 2개를 한 커밋에 같이 넣어버렸다. 커밋만 취소하고 **변경 내용은 살려서** 다시 나눠 커밋하고 싶다.

### 실행한 명령
```bash
git log --oneline -2

git reset --soft HEAD~1

git status
# 변경 내용이 staged 상태로 그대로 남아 있음

git restore --staged <파일2>
git commit -m "docs: 충돌 노트에 마커 의미 설명 추가"
git add <파일2>
git commit -m "docs: 노트 목차에 충돌 노트 등록"
```

<!-- TODO: 실제 출력 붙여넣기 -->

### 결과
- 커밋 1개가 의미 단위 2개로 나뉘었고, 작업 내용은 하나도 안 날아갔다
- PR/커밋 링크: <링크>

### 왜 이 방법인가
- `--soft`: 커밋만 취소, 변경은 staged로 유지 → 다시 커밋할 때 좋다
- `--mixed`(기본): 커밋 취소 + unstaged로 내림
- `--hard`: 커밋과 변경 내용 **둘 다 삭제** → 실수하면 복구 어려워서 이번엔 안 씀

### 주의할 점
- 이미 push한 커밋에 `reset`을 쓰면 원격과 어긋나서 force push가 필요해진다 → 그때는 `revert`

---

## 시나리오 3 — `git revert`

### 참여자
대웅 (@Daeung-03) — 실습·기록 / 리뷰: 김정현

### 상황
잘못된 내용이 담긴 커밋이 이미 PR로 머지돼서 **main에 올라가 있다**. 되돌려야 한다.

### 실행한 명령
```bash
git checkout main
git pull origin main
git log --oneline -3            # 되돌릴 커밋 해시 확인

git checkout -b fix/daeung-03-revert-wrong-note
git revert <되돌릴 커밋 해시>
# 되돌리는 내용의 새 커밋이 생성됨

git log --oneline -2
git push origin fix/daeung-03-revert-wrong-note
# PR 올려서 리뷰 받고 머지
```

<!-- TODO: 실제 출력 붙여넣기 -->

### 결과
- 변경이 취소되었고, **취소했다는 기록(커밋)이 히스토리에 남았다**
- PR/커밋 링크: <링크>

### 왜 `reset`이 아니라 `revert`인가
- `reset`은 히스토리를 지우는 방식이라, 이미 남들이 pull 받은 커밋에 쓰면 다른 사람 저장소와 어긋난다
- `revert`는 "되돌리는 새 커밋"을 쌓는 방식이라 원격 히스토리를 건드리지 않는다
- main은 보호돼 있어서 어차피 force push도 못 한다

### 주의할 점
- 머지 커밋을 revert할 땐 `-m 1` 옵션이 필요하다
- revert 커밋도 PR을 통해 머지한다 (main 직접 push 금지)

---

## 시나리오 4 — `git stash` / `git stash pop`

### 참여자
대웅 (@Daeung-03) — 실습·기록 / 리뷰: 김승우

### 상황
노트를 쓰던 중에 다른 사람 PR 리뷰 때문에 급히 브랜치를 옮겨야 한다. 지금 작업은 커밋할 만큼 완성되지 않았다.

### 실행한 명령
```bash
git status                      # 수정 중인 파일 있음

git stash                       # 작업 보관, 작업 디렉터리 깨끗해짐
git status

git checkout main
git pull origin main
# 리뷰 확인 후 원래 브랜치로 복귀

git checkout docs/daeung-03-git-undo
git stash list
# stash@{0}: WIP on docs/daeung-03-git-undo: ...

git stash pop                   # 보관한 작업 복원 + 목록에서 제거
git status
```

<!-- TODO: 실제 출력 붙여넣기 -->

### 결과
- 미완성 작업을 커밋 없이 보관했다가 그대로 복원했다
- PR/커밋 링크: <링크>

### 왜 이 방법인가
- 미완성 상태를 `wip` 같은 의미 없는 커밋으로 남기지 않아도 된다 (팀 커밋 규칙 위반 방지)
- 브랜치를 옮길 때 수정 중인 파일이 있으면 Git이 막는데, stash로 해결된다

### 주의할 점
- `stash pop`은 꺼내면서 목록에서 지운다. 남겨두고 싶으면 `git stash apply`
- stash는 로컬에만 있고 push되지 않는다. 오래 쌓아두면 뭐였는지 잊어버린다
- 새로 만든 파일(untracked)은 기본으로 안 들어간다 → `git stash -u`
