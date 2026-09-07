# Codyssey B2-2 · Git 협업 미션

3인 팀으로 브랜치 · PR · 코드 리뷰 · 충돌 해결을 직접 겪어보고 기록으로 남기는 미션 저장소입니다.
산출물은 **학습 노트(옵션 C)** 이고, Python / Git / GitHub를 팀원끼리 나눠서 정리합니다.

- 제출물 인덱스: [SUBMISSION.md](SUBMISSION.md)
- 협업 규칙: [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md)
- 충돌 기록: [docs/conflict-resolution.md](docs/conflict-resolution.md)
- 트러블슈팅 기록: [docs/troubleshooting-log.md](docs/troubleshooting-log.md)
- 학습 노트 목차: [notes/README.md](notes/README.md)

---

## 1. 팀 구성과 담당

| 이름 | GitHub | 학습 노트 | 트러블슈팅 |
|---|---|---|---|
| 대웅 | @Daeung-03 | `git-basics`, `git-undo`, `python-basics` | `revert`, `stash` |
| 김정현 | @kimjexnghyexn | `git-branch`, `github-flow`, `python-functions` | `commit --amend` |
| 김승우 | @stevenkim18 | `git-conflict`, `github-pr-review`, `python-errors` | `reset --soft` |

---

## 2. 폴더 구조

```
README.md                       이 문서 (계획 + 규칙 요약)
SUBMISSION.md                   제출물 링크 모음
.github/
  pull_request_template.md      PR 쓸 때 자동으로 채워지는 양식
  ISSUE_TEMPLATE/               이슈 양식 7종 (종류별)
docs/
  PROBLEM.md                    미션 원문
  CONTRIBUTING.md               협업 규칙
  conflict-resolution.md        충돌 기록
  troubleshooting-log.md        amend/reset/revert/stash 기록
  git-history.md                git log --graph 결과 붙여넣는 곳
notes/
  README.md                     노트 목차 (여러 명이 같이 고침 → 충돌 지점)
  <주제>.md                     노트 9개
src/
  example.py                    Python 노트에서 쓰는 예시 코드
```

---

## 3. 정한 것들

| 항목 | 결정 |
|---|---|
| 저장소 | 개인 저장소(옵션 B) + Collaborator 초대 |
| 공개 범위 | Public (무료 플랜은 Public에서만 브랜치 보호 설정 가능) |
| 브랜치 전략 | GitHub Flow (`main` + 작업 브랜치) |
| 병합 방식 | Merge commit (Squash 안 씀 — 브랜치 그래프가 증빙이라서) |
| 산출물 | 학습 노트 |
| 문서 언어 | 한국어 (커밋 타입만 영어) |
| 리뷰 승인 | 1명 |

### GitHub Flow를 고른 이유 (3줄)

1. 브랜치가 `main`과 작업 브랜치 둘뿐이라 3명이 규칙을 헷갈리지 않고 지킬 수 있다.
2. 모든 변경이 PR을 거치니까 리뷰와 이슈 추적이 자연스럽게 강제된다.
3. 버전 릴리스가 없는 짧은 미션에 git-flow의 `develop`/`release`는 과하다.

---

## 4. 규칙 요약 (자세한 건 CONTRIBUTING.md)

**브랜치**: `<종류>/<깃헙아이디>-<주제>`
예) `docs/kimjexnghyexn-git-branch`, `feature/daeung-03-python-example`, `fix/stevenkim18-readme-link`

**커밋**: `<타입>: <무엇을 어떻게>` — 타입은 `feat` `fix` `docs` `refactor` `chore`

| ❌ | ✅ |
|---|---|
| `update` | `docs: 브랜치 노트에 HEAD 설명 추가` |
| `fix` | `fix: notes/README 목차 링크 경로 수정` |
| `wip`, `temp`, `final` | `docs: 충돌 노트 초안 작성` |

**PR**: 제목은 커밋과 같은 형식. 본문에 `Closes #이슈번호` + What / Why / How.
approve 1명 받고 머지, 머지하면 브랜치 삭제.

**리뷰**: `LGTM`만 쓰면 리뷰로 안 셉니다. 파일이나 줄을 근거로 한 코멘트 1개 이상 필수.

---

## 5. 3일 계획

### Day 0 — 세팅 (대웅, 20분)

GitHub 웹에서 클릭으로 다 됩니다.

1. Settings → Collaborators → `kimjexnghyexn`, `stevenkim18` 초대
2. 이 스캐폴딩 파일들을 `main`에 push (보호 설정 **전에** 한 번만)
3. Settings → General → Pull Requests: `Allow merge commits`만 켜고 Squash / Rebase 끄기, `Automatically delete head branches` 켜기
4. Settings → Branches → Add branch protection rule
   - Branch name pattern: `main`
   - ☑ Require a pull request before merging → Require approvals: **1**
   - ☑ Require conversation resolution before merging
   - ☑ Do not allow bypassing the above settings ← 이걸 켜면 주인도 main에 직접 push 못 함
5. 팀원 전원 `git clone` 후 CONTRIBUTING.md 같이 읽기 (15분)

### Day 1 — 규칙 확정

목표: **각자 PR 1개 머지 + 남의 PR에 리뷰 1개**

| 담당 | 브랜치 | 할 일 |
|---|---|---|
| 대웅 | `docs/daeung-03-plan-update` | 킥오프에서 나온 수정 의견을 README 계획에 반영 |
| 김정현 | `docs/kimjexnghyexn-contributing-commit` | CONTRIBUTING의 브랜치·커밋 규칙 확정 |
| 김승우 | `docs/stevenkim18-contributing-pr` | CONTRIBUTING의 PR·리뷰·충돌 대응 규칙 확정 |

정현과 승우는 같은 파일의 다른 부분을 고칩니다. 나중에 push하는 사람은 `git pull origin main` 먼저 하세요.

### Day 2 — Git/GitHub 노트 6개 + 충돌 #1

| 담당 | 노트 |
|---|---|
| 대웅 | `notes/git-basics.md`, `notes/git-undo.md` |
| 김정현 | `notes/git-branch.md`, `notes/github-flow.md` |
| 김승우 | `notes/git-conflict.md`, `notes/github-pr-review.md` |

- [ ] 노트 6개 머지, 목차에 6줄 등록
- [ ] **충돌 #1 실행하고 기록** (아래 6번)
- [ ] 각자 본인 PR에서 리뷰 받고 반영 커밋 1개 이상
- [ ] Day 2 끝날 때 `notes/python-functions.md`는 아직 main에 없어야 함 (Day 3 충돌용)

### Day 3 — Python 노트 3개 + 충돌 #2 + 트러블슈팅 + 마감

| 순서 | 할 일 | 담당 |
|---|---|---|
| 1 | `notes/python-functions.md` 먼저 머지 | 김정현 |
| 2 | `notes/python-basics.md`, `notes/python-errors.md` 머지 | 대웅, 김승우 |
| 3 | **충돌 #2 실행하고 기록** | 대웅 ↔ 김정현 |
| 4 | 트러블슈팅 4종 실습 + 기록 | amend=정현 / reset=승우 / revert·stash=대웅 |
| 5 | `git log --oneline --graph --all` → `docs/git-history.md` | 대웅 |
| 6 | `SUBMISSION.md` 링크 채우기 | 각자 본인 것 |

---

## 6. 충돌 실습 (일부러 만드는 것)

충돌은 우연히 기다리는 게 아니라 아래처럼 **미리 짜놓고** 만듭니다. 기록은 [docs/conflict-resolution.md](docs/conflict-resolution.md)에.

### 충돌 #1 — 같은 줄 근처를 동시에 고치기 (Day 2)

대상: `notes/README.md` 목차 표. 새 노트는 표 맨 아래에 한 줄 추가하는 규칙이라, 두 명이 동시에 추가하면 같은 위치가 겹칩니다.

```bash
# 둘이 같은 main에서 시작하는 게 핵심
git checkout main
git pull origin main

# 김정현 (먼저 머지)
git checkout -b docs/kimjexnghyexn-git-branch
# notes/git-branch.md 작성 + notes/README.md 표 맨 아래에 한 줄 추가
git add .
git commit -m "docs: 브랜치 포인터 노트 추가"
git push origin docs/kimjexnghyexn-git-branch   # PR 올려서 머지

# 김승우 (정현 머지된 뒤에 push → PR에 conflict 표시됨)
git checkout -b docs/stevenkim18-git-conflict
# notes/git-conflict.md 작성 + notes/README.md 같은 위치에 한 줄 추가
git add .
git commit -m "docs: 충돌 마커 노트 추가"
git push origin docs/stevenkim18-git-conflict

# 승우가 자기 브랜치에서 해결
git pull origin main          # CONFLICT: notes/README.md
git diff                      # 마커 보이는 거 복사해서 기록에 붙일 것
# 두 줄 다 살리고 마커 지움
git add notes/README.md
git commit
git push origin docs/stevenkim18-git-conflict
```

기록: 김승우 (상대 김정현)

### 충돌 #2 — 한쪽은 파일 이름 변경, 한쪽은 내용 수정 (Day 3, 비자명 충돌)

전제: `notes/python-functions.md`가 이미 main에 있음.

```bash
git checkout main
git pull origin main

# 대웅: 파일 이름 바꾸기 (먼저 머지)
git checkout -b chore/daeung-03-rename-note
git mv notes/python-functions.md notes/python-functions-note.md
# notes/README.md 링크도 같이 수정
git commit -am "chore: 함수 노트 파일명 규칙에 맞게 변경"
git push origin chore/daeung-03-rename-note     # PR 머지

# 김정현: 같은 main에서 시작해서 원래 파일 내용을 수정
git checkout -b docs/kimjexnghyexn-python-functions-fix
# notes/python-functions.md 에 내용 추가
git commit -am "docs: 함수 노트에 type hint 설명 추가"
git push origin docs/kimjexnghyexn-python-functions-fix

# 정현이 해결
git pull origin main
# CONFLICT (modify/delete): notes/python-functions.md deleted in origin/main and modified in HEAD
git status                    # 이 유형은 파일 안에 마커가 안 생김
# 내가 쓴 내용을 새 파일(notes/python-functions-note.md)에 옮겨 붙이고
git rm notes/python-functions.md
git add notes/python-functions-note.md
git commit
git push origin docs/kimjexnghyexn-python-functions-fix
```

기록: 김정현 (상대 대웅)

> 두 시나리오 모두 **자기 브랜치 안에서만** 해결합니다. main에 직접 손대거나 `push --force` 쓰지 않습니다.

---

## 7. 노트 내용 분배

### Git

| 노트 | 담당 | 내용 |
|---|---|---|
| `git-basics` | 대웅 | 작업 디렉터리 / 스테이징 / 저장소 3단계, `add` `commit` `status` `log` |
| `git-branch` | 김정현 | **브랜치는 커밋을 가리키는 포인터**, `.git/refs/heads/` 열어보기, HEAD, 왜 브랜치를 나누는지 |
| `git-conflict` | 김승우 | 충돌이 왜 생기는지, `<<<<<<<` `=======` `>>>>>>>` 각각의 의미, 해결 순서 |
| `git-undo` | 대웅 | `reset --soft/--mixed/--hard`, `revert`, `stash`, `amend` 차이와 언제 쓰는지 |

### GitHub

| 노트 | 담당 | 내용 |
|---|---|---|
| `github-flow` | 김정현 | GitHub Flow 흐름, main을 깨지지 않게 유지한다는 뜻, 왜 팀에 전략이 필요한지 |
| `github-pr-review` | 김승우 | PR의 목적, 코드 리뷰의 가치, 좋은 리뷰 코멘트 예시, `Closes #이슈` 연동 |

### Python

| 노트 | 담당 | 내용 |
|---|---|---|
| `python-basics` | 대웅 | 3.10 확인, 변수/타입, 조건문/반복문 |
| `python-functions` | 김정현 | 함수 정의와 인자, 반환값, `import`, type hint |
| `python-errors` | 김승우 | `try` / `except` / `finally`, 예외 종류, `raise` |

**노트 형식** (통일하면 리뷰가 편합니다)

```markdown
# 제목
> 작성자: 이름 (@아이디) · 관련 이슈: #N

## 한 줄 요약
## 핵심 내용
## 직접 해본 것 (실행한 명령 + 결과)
## 헷갈렸던 점
## 참고 링크
```

---

## 8. 마감 전 체크리스트

### 팀 전체
- [ ] main 브랜치 보호 (직접 push 금지 / PR만 / approve 1명)
- [ ] 모든 PR 본문에 `Closes #이슈번호`
- [ ] 충돌 기록 2건 이상 (비자명 1건 이상)
- [ ] 트러블슈팅 4종 (`amend` `reset --soft` `revert` `stash`) 전부 기록
- [ ] CONTRIBUTING.md 5개 항목 작성
- [ ] `docs/git-history.md`에 `git log --oneline --graph --all` 결과
- [ ] SUBMISSION.md 링크 다 채움

### 각자
| 기준 | 대웅 | 정현 | 승우 |
|---|---|---|---|
| PR 만들고 머지 2개 이상 | ☐ | ☐ | ☐ |
| 남의 PR에 리뷰 2개 이상 | ☐ | ☐ | ☐ |
| 내 PR에서 리뷰 반영 1회 이상 | ☐ | ☐ | ☐ |
| 트러블슈팅 기록 1개 이상 참여 | ☐ | ☐ | ☐ |
| 노트 커밋 1개 이상 | ☐ | ☐ | ☐ |

---

## 9. 작업 루틴 (매번 이 순서)

```bash
# 1. GitHub 웹 Issues → New issue → 양식 선택 (작업 / 수정 요청)

# 2. 최신 main에서 브랜치 만들기  ← 빼먹으면 쓸데없는 충돌 남
git checkout main
git pull origin main
git checkout -b docs/<내아이디>-<주제>

# 3. 작업하고 커밋
git add <파일>
git commit -m "docs: <무엇을 어떻게>"

# 4. push 하고 GitHub 웹에서 PR 만들기 (본문 양식 자동으로 뜸)
git push origin docs/<내아이디>-<주제>

# 5. 리뷰 반영은 새 커밋으로 (force push 금지)
git commit -am "docs: 리뷰 반영 - <무엇>"
git push origin docs/<내아이디>-<주제>

# 6. 머지 후 정리
git checkout main
git pull origin main
git branch -d docs/<내아이디>-<주제>
```
