# Git 되돌리기: reset, revert, stash, amend

> 작성자: 대웅 (@Daeung-03) · 관련 이슈: #7

## 한 줄 요약

공유 전인 로컬 이력은 `reset`이나 `amend`로 고칠 수 있지만, 이미 공유한 커밋은 이력을 보존하는 `revert`로 되돌리는 것이 안전하다.

## 핵심 내용

### 상태를 판단하는 세 영역

Git에서 되돌리기 명령의 차이를 이해하려면 다음 세 영역을 구분해야 한다.

- **HEAD**: 현재 브랜치가 가리키는 마지막 커밋
- **스테이징 영역(Index)**: 다음 커밋에 넣을 변경
- **작업 디렉터리(Working Tree)**: 현재 파일의 실제 내용

### `git reset`의 세 모드

`git reset <모드> <대상 커밋>`은 현재 브랜치와 HEAD를 대상 커밋으로 옮긴다. 모드에 따라 스테이징 영역과 작업 디렉터리까지 되돌리는지가 달라진다.

| 명령 | HEAD | 스테이징 영역 | 작업 디렉터리 | 주로 쓸 때 |
|---|---|---|---|---|
| `git reset --soft HEAD~1` | 이동 | 유지 | 유지 | 마지막 로컬 커밋만 취소하고 변경을 바로 다시 커밋할 때 |
| `git reset --mixed HEAD~1` | 이동 | 대상 커밋에 맞춤 | 유지 | 커밋과 스테이징을 취소하고 파일별로 다시 고를 때 |
| `git reset --hard HEAD~1` | 이동 | 대상 커밋에 맞춤 | 대상 커밋에 맞춤 | 로컬 변경을 정말 버려도 된다고 확인했을 때만 |

옵션을 생략한 `git reset HEAD~1`은 `--mixed`와 같다. 세 모드 모두 브랜치 이력을 이동시키므로 **아직 공유하지 않은 로컬 커밋**에만 사용하는 편이 안전하다.

> **주의:** `reset --hard`는 스테이징하지 않은 변경까지 지운다. 공유 브랜치에서 reset한 뒤 `push --force`로 이력을 덮어쓰면 다른 팀원의 커밋도 잃을 수 있으므로 사용하지 않는다.

### `revert`, `stash`, `amend`

| 명령 | 동작 | 적합한 상황 | 주의점 |
|---|---|---|---|
| `git revert <커밋>` | 기존 커밋의 반대 변경을 새 커밋으로 추가 | 이미 원격에 공유한 커밋 취소 | 원래 커밋은 이력에 남으며 충돌이 날 수 있다. |
| `git stash` | 커밋하지 않은 변경을 임시 스택에 보관 | 작업 중 급히 다른 브랜치로 이동 | 기본적으로 untracked 파일은 제외된다. 포함하려면 `git stash -u`를 쓴다. |
| `git stash pop` | 최근 stash를 적용하고 성공하면 목록에서 제거 | 임시 작업 복원 | 적용 중 충돌이 날 수 있으므로 `git status`로 확인한다. |
| `git commit --amend` | 가장 최근 커밋을 새 커밋으로 교체 | push 전 메시지나 누락 파일 수정 | 커밋 해시가 바뀌므로 이미 공유한 커밋에는 사용하지 않는다. |

### 상황별 선택 기준

- 마지막 **로컬 커밋 메시지나 내용**만 고친다 → `git commit --amend`
- 마지막 **로컬 커밋을 취소하되 변경은 staged로 유지**한다 → `git reset --soft HEAD~1`
- 마지막 **로컬 커밋과 staging을 취소하되 파일 변경은 유지**한다 → `git reset --mixed HEAD~1`
- 확인을 마친 **불필요한 로컬 변경을 완전히 버린다** → `git reset --hard`를 매우 신중하게 사용
- 이미 **원격에 공유한 커밋을 취소**한다 → `git revert <커밋>`
- 커밋하기 이른 작업을 잠시 치우고 **다른 브랜치로 이동**한다 → `git stash`, 돌아와서 `git stash pop`

## 직접 해본 것

프로젝트 이력을 건드리지 않도록 `/tmp/git-undo-practice`에 별도 저장소를 만들고 실습했다.

### 1. 기준 커밋 두 개 만들기

```console
$ mkdir -p /tmp/git-undo-practice
$ cd /tmp/git-undo-practice
$ git init
Initialized empty Git repository in /private/tmp/git-undo-practice/.git/

$ printf 'base\n' > demo.txt
$ git add demo.txt
$ git commit -m "feat: 기준 커밋"
[main (root-commit) 5403c61] feat: 기준 커밋
 1 file changed, 1 insertion(+)
 create mode 100644 demo.txt

$ printf 'second\n' >> demo.txt
$ git add demo.txt
$ git commit -m "feat: 두 번째 변경"
[main 3d992c8] feat: 두 번째 변경
 1 file changed, 1 insertion(+)

$ git log --oneline --decorate -2
3d992c8 (HEAD -> main) feat: 두 번째 변경
5403c61 feat: 기준 커밋
```

### 2. `reset --soft` — 변경을 staged로 유지

```console
$ git reset --soft HEAD~1
$ git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   demo.txt

$ git log --oneline --decorate -1
5403c61 (HEAD -> main) feat: 기준 커밋
```

HEAD는 기준 커밋으로 이동했지만 `demo.txt` 변경은 `Changes to be committed`에 남았다. 다음 실습을 위해 이 변경을 다시 커밋했다.

```console
$ git commit -m "feat: 두 번째 변경"
[main e00077b] feat: 두 번째 변경
 1 file changed, 1 insertion(+)
```

### 3. `reset --mixed` — 변경을 unstaged로 유지

```console
$ git reset --mixed HEAD~1
Unstaged changes after reset:
M       demo.txt

$ git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   demo.txt

no changes added to commit (use "git add" and/or "git commit -a")

$ git log --oneline --decorate -1
5403c61 (HEAD -> main) feat: 기준 커밋
```

HEAD는 이동했고 staging도 취소됐지만 파일 내용은 작업 디렉터리에 남았다. `git add demo.txt`와 커밋을 다시 실행한 뒤 다음 모드를 확인했다.

### 4. `reset --hard` — 변경까지 제거

```console
$ git reset --hard HEAD~1
HEAD is now at 5403c61 feat: 기준 커밋

$ git status
On branch main
nothing to commit, working tree clean

$ cat demo.txt
base
```

두 번째 커밋뿐 아니라 작업 디렉터리의 `second` 줄도 사라졌다. 실제 작업에서는 되돌릴 변경이 없는지 먼저 확인해야 한다.

### 5. `commit --amend` — 최근 커밋 교체

```console
$ printf 'amend example\n' >> demo.txt
$ git add demo.txt
$ git commit -m "docs: 잘못된 메시지"
[main 7247661] docs: 잘못된 메시지
 1 file changed, 1 insertion(+)

$ git log --oneline --decorate -1
7247661 (HEAD -> main) docs: 잘못된 메시지

$ git commit --amend -m "docs: 메시지 수정"
[main 4eb09dd] docs: 메시지 수정
 Date: Tue Sep 8 18:34:10 2026 +0900
 1 file changed, 1 insertion(+)

$ git log --oneline --decorate -1
4eb09dd (HEAD -> main) docs: 메시지 수정
```

메시지만 고쳤지만 커밋 해시가 `7247661`에서 `4eb09dd`로 바뀌었다. amend가 기존 커밋을 수정하는 것이 아니라 새 커밋으로 교체하는 동작임을 확인했다.

### 6. `revert` — 이력을 남기고 변경 취소

```console
$ printf 'risky change\n' >> demo.txt
$ git add demo.txt
$ git commit -m "feat: 위험한 변경"
[main fc28b8b] feat: 위험한 변경
 1 file changed, 1 insertion(+)

$ git revert --no-edit HEAD
[main d4b5f15] Revert "feat: 위험한 변경"
 Date: Tue Sep 8 18:34:11 2026 +0900
 1 file changed, 1 deletion(-)

$ git log --oneline --decorate -3
d4b5f15 (HEAD -> main) Revert "feat: 위험한 변경"
fc28b8b feat: 위험한 변경
4eb09dd docs: 메시지 수정

$ cat demo.txt
base
amend example
```

원래 커밋 `fc28b8b`는 삭제되지 않았고, 반대 변경을 적용한 새 커밋 `d4b5f15`가 추가됐다. 이력을 재작성하지 않으므로 공유된 커밋을 안전하게 취소할 수 있다.

### 7. `stash`와 `stash pop` — 작업 임시 보관과 복원

```console
$ printf 'work in progress\n' >> demo.txt
$ git status --short
 M demo.txt

$ git stash push -m "wip: 임시 작업"
Saved working directory and index state On main: wip: 임시 작업

$ git status
On branch main
nothing to commit, working tree clean

$ git stash list
stash@{0}: On main: wip: 임시 작업

$ cat demo.txt
base
amend example
```

stash 후에는 수정 중이던 줄이 작업 디렉터리에서 사라지고 상태가 clean이 됐다. 이어서 작업을 복원했다.

```console
$ git stash pop
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   demo.txt

no changes added to commit (use "git add" and/or "git commit -a")
Dropped refs/stash@{0} (9cd0ed606e75e1da2e6a1975959d8e80c7cd1286)

$ cat demo.txt
base
amend example
work in progress
```

`stash pop` 후 수정 내용이 작업 디렉터리에 복원됐고, 적용에 성공한 stash는 목록에서 제거됐다.

## 헷갈렸던 점

`reset --soft`와 `--mixed` 모두 파일 변경을 남기지만 위치가 다르다. `--soft`는 바로 다시 커밋할 수 있도록 staged 상태로 남기고, `--mixed`는 `git add`부터 다시 선택하도록 unstaged 상태로 남긴다. 반면 `revert`는 과거 커밋을 없애지 않고 취소 커밋을 추가한다. 따라서 명령을 고르기 전에 **커밋이 이미 공유됐는지**, **파일 변경을 남길지**, **staging도 유지할지**를 먼저 확인해야 한다.

## 참고 링크

- [Git 공식 문서 - git-reset](https://git-scm.com/docs/git-reset)
- [Git 공식 문서 - git-revert](https://git-scm.com/docs/git-revert)
- [Git 공식 문서 - git-stash](https://git-scm.com/docs/git-stash)
- [Git 공식 문서 - git-commit](https://git-scm.com/docs/git-commit)
