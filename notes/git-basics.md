# Git 기초: 변경을 기록하는 세 단계

> 작성자: 대웅 (@Daeung-03) · 관련 이슈: #1

## 한 줄 요약

Git은 작업 디렉터리의 변경 중 `git add`로 고른 내용을 스테이징 영역에 올리고, `git commit`으로 저장소에 기록한다.

## 핵심 내용

### 작업 디렉터리, 스테이징 영역, 저장소

| 단계 | 역할 | 상태를 바꾸는 명령 |
|---|---|---|
| 작업 디렉터리(Working Directory) | 파일을 만들고 수정하는 실제 작업 공간 | 파일 생성·수정·삭제 |
| 스테이징 영역(Staging Area, Index) | 다음 커밋에 포함할 변경을 고르는 공간 | `git add <파일>` |
| 저장소(Repository) | 커밋으로 확정된 스냅샷과 이력을 `.git`에 보관하는 공간 | `git commit -m "메시지"` |

변경이 기록되는 흐름은 다음과 같다.

```text
작업 디렉터리 ── git add ──> 스테이징 영역 ── git commit ──> 저장소
```

`git add`는 파일 자체를 최종 저장하는 명령이 아니라 **현재 변경 내용을 다음 커밋 후보로 선택하는 명령**이다. `git commit`은 작업 디렉터리의 모든 변경이 아니라 **스테이징 영역에 올라온 변경만** 저장소에 기록한다.

### `git status` 출력 읽는 법

- `On branch main`: 현재 체크아웃한 브랜치가 `main`이라는 뜻이다.
- `No commits yet`: 아직 첫 커밋이 없는 저장소라는 뜻이다.
- `Untracked files`: Git이 아직 추적하지 않는 새 파일이다. 커밋하려면 `git add`가 필요하다.
- `Changes not staged for commit`: 추적 중인 파일을 수정했지만 변경이 아직 스테이징되지 않은 상태다.
- `Changes to be committed`: 스테이징되어 다음 커밋에 포함될 변경이다.
- `nothing to commit, working tree clean`: 스테이징하거나 커밋할 새 변경이 없는 깨끗한 상태다.

### 기본 명령

| 명령 | 용도 |
|---|---|
| `git init` | 현재 디렉터리에 `.git`을 만들고 Git 저장소를 초기화한다. |
| `git add <파일>` | 파일의 현재 변경을 스테이징한다. `git add .`은 현재 경로 아래 변경을 한꺼번에 스테이징하므로 범위를 확인하고 사용한다. |
| `git status` | 작업 디렉터리와 스테이징 영역의 상태를 확인한다. |
| `git commit -m "메시지"` | 스테이징된 변경을 하나의 커밋으로 저장한다. |
| `git log` | 커밋 이력을 확인한다. `git log --oneline`을 사용하면 커밋당 한 줄로 간단히 볼 수 있다. |

## 직접 해본 것

`/tmp/git-practice`에 새 저장소를 만들고 파일 생성부터 커밋 이력 확인까지 직접 실행했다.

### 1. 저장소 초기화

```console
$ mkdir -p /tmp/git-practice
$ cd /tmp/git-practice
$ git init
Initialized empty Git repository in /private/tmp/git-practice/.git/
```

macOS에서는 `/tmp`가 `/private/tmp`를 가리키므로 `git init` 출력에는 실제 경로인 `/private/tmp/git-practice`가 표시됐다.

### 2. 파일 생성 후 `git status` — Untracked files

```console
$ echo "hello git" > a.txt
$ git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        a.txt

nothing added to commit but untracked files present (use "git add" to track)
```

`a.txt`를 만들기만 했기 때문에 Git이 아직 추적하지 않는 `Untracked files`에 나타났다.

### 3. `git add` 후 `git status` — Changes to be committed

```console
$ git add a.txt
$ git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   a.txt
```

`git add a.txt`를 실행하자 `a.txt`가 스테이징되어 다음 커밋에 포함될 `Changes to be committed`로 이동했다.

### 4. `git commit` 후 `git status` — working tree clean

```console
$ git commit -m "feat: a.txt 추가"
[main (root-commit) 3a703cd] feat: a.txt 추가
 1 file changed, 1 insertion(+)
 create mode 100644 a.txt

$ git status
On branch main
nothing to commit, working tree clean
```

스테이징된 변경을 커밋하자 더 기록할 변경이 없어 작업 트리가 깨끗한 상태가 됐다.

### 5. 커밋 이력 확인

```console
$ git log --oneline
3a703cd (HEAD -> main) feat: a.txt 추가
```

`git log --oneline`에서 방금 만든 커밋의 짧은 해시와 메시지를 확인했다.

## 헷갈렸던 점

처음에는 `git add`가 변경을 저장소에 저장하는 명령이라고 생각하기 쉽지만, 실제로는 다음 커밋에 넣을 변경을 스테이징하는 단계다. 또한 `git commit`은 작업 디렉터리의 모든 파일을 자동으로 기록하지 않고 스테이징된 변경만 기록한다. 따라서 각 단계에서 `git status`를 확인하면 빠뜨린 파일이나 의도하지 않은 변경을 커밋하는 실수를 줄일 수 있다.

## 참고 링크

- [Git 공식 문서 - gittutorial](https://git-scm.com/docs/gittutorial)
- [Git 공식 문서 - git-status](https://git-scm.com/docs/git-status)
- [Git 공식 문서 - git-add](https://git-scm.com/docs/git-add)
- [Git 공식 문서 - git-commit](https://git-scm.com/docs/git-commit)
