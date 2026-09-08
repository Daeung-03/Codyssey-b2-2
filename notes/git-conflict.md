# Git 충돌 해결
> 작성자: 김승우 (@stevenkim18) · 관련 이슈: #13

## 한 줄 요약

Git 충돌은 같은 공통 커밋에서 출발한 변경을 Git이 안전하게 자동 결합할 수 없을 때 발생하며, 충돌 마커의 양쪽 내용을 확인한 뒤 팀과 합의해 해결한다.

## 핵심 내용

### 충돌이 생기는 이유

두 브랜치가 같은 파일의 같은 줄(또는 아주 가까운 부분)을 서로 다르게 바꾸면 Git은 어느 변경을 남겨야 하는지 판단할 수 없다. 이때 Git은 작업을 멈추고 충돌 난 파일을 표시한다. 한쪽 변경을 조용히 버리는 것보다 사람이 결정하게 하는 편이 안전하기 때문이다.

### 충돌 마커 읽기

```txt
<<<<<<< HEAD
현재 브랜치의 내용
=======
가져와 병합하는 브랜치의 내용
>>>>>>> docs-theme
```

- `<<<<<<< HEAD`부터 `=======` 전까지는 merge를 시작한 현재 브랜치의 내용이다.
- `=======`는 두 변경을 나누는 경계다.
- `=======`부터 `>>>>>>> <브랜치>` 전까지는 가져와 병합하는 쪽의 내용이다.
- `>>>>>>> <브랜치>`의 이름은 상대 브랜치 또는 원격 브랜치 이름이다.

`git pull origin main`으로 내 작업 브랜치에 `main`을 병합했다면 `HEAD`는 내 작업 브랜치다. 다만 rebase 중에는 `ours`와 `theirs`의 의미가 달라질 수 있으므로, 이름만 믿지 말고 마커 안의 실제 내용을 확인한다.

### 해결 순서

1. 충돌이 나면 상대에게 파일명과 상황을 알리고, 어느 내용을 남길지 합의한다.
2. `git status`로 충돌 파일과 종류를 확인한다.
3. `git diff`와 충돌 파일을 열어 마커 양쪽의 변경을 확인한다.
4. 필요한 내용을 남기고 `<<<<<<<`, `=======`, `>>>>>>>` 마커를 모두 지운다.
5. `git add <파일>`로 해결됐음을 Git에 알린 뒤 `git commit`한다.
6. 내 브랜치에 push하고 PR에서 해결 방법을 설명한다.

해결 방향을 잘못 잡았거나 다시 논의해야 하면, 아직 해결 커밋을 만들기 전에는 `git merge --abort`로 병합 시작 전 상태로 돌아갈 수 있다. 공유된 `main`에 직접 push하거나 충돌을 피하려고 `push --force`를 사용하지 않는다.

## 직접 해본 것

실제 팀 저장소에는 영향을 주지 않도록 임시 저장소(`/tmp/git-conflict-practice.J5UHIT`)에서 같은 파일의 같은 줄을 서로 다르게 고쳐 충돌을 재현했다. `main`은 `theme = system`, `docs-theme`은 `theme = dark`로 수정했다.

```bash
practice_dir=$(mktemp -d /tmp/git-conflict-practice.XXXXXX)
cd "$practice_dir"
git init -b main
git config user.name "김승우"
git config user.email "11882@naver.com"

printf 'theme = light\n' > settings.txt
git add settings.txt
git commit -m "feat: 기본 테마 설정 추가"

git switch -c docs-theme
printf 'theme = dark\n' > settings.txt
git commit -am "docs: 문서용 다크 테마 설정"

git switch main
printf 'theme = system\n' > settings.txt
git commit -am "feat: 시스템 테마 설정"
git merge docs-theme
```

실행 결과는 다음과 같았다. `git merge`가 자동 병합을 중단했고, `settings.txt`가 충돌 상태(`UU`)가 됐다.

```txt
Auto-merging settings.txt
CONFLICT (content): Merge conflict in settings.txt
Automatic merge failed; fix conflicts and then commit the result.
```

```bash
git status --short
git diff --no-ext-diff
sed -n '1,20p' settings.txt
```

```txt
UU settings.txt
diff --cc settings.txt
index effddd0,e0d48f3..0000000
--- a/settings.txt
+++ b/settings.txt
@@@ -1,1 -1,1 +1,5 @@@
++<<<<<<< HEAD
 +theme = system
++=======
+ theme = dark
++>>>>>>> docs-theme
<<<<<<< HEAD
theme = system
=======
theme = dark
>>>>>>> docs-theme
```

이번 실습에서는 `main`의 시스템 설정을 선택했다. 실제 협업이라면 이 선택 전에 상대와 용도를 확인해야 한다. 마커를 지운 뒤 해결 결과를 스테이지하고 merge commit을 만들었다.

```bash
printf 'theme = system\n' > settings.txt
git add settings.txt
git commit -m "docs: 테마 설정 충돌 해결"
git log --oneline --graph --all
```

```txt
[main 5e84bf6] docs: 테마 설정 충돌 해결
*   5e84bf6 docs: 테마 설정 충돌 해결
|\  
| * 57a6ccb docs: 문서용 다크 테마 설정
* | b690e37 feat: 시스템 테마 설정
|/  
* 4e04079 feat: 기본 테마 설정 추가
```

## 헷갈렸던 점

충돌 마커에서 `HEAD`가 항상 `main`을 뜻하는 것은 아니다. merge 명령을 실행한 브랜치가 `HEAD`다. 또한 `git diff`는 충돌 파일을 결합 diff 형식으로 보여 주고, 파일 자체에는 마커가 그대로 남아 있으므로 둘 다 확인하는 편이 좋다. 파일 이동·삭제와 내용 수정이 충돌한 경우에는 파일 안에 마커가 없을 수 있으니 `git status`를 먼저 읽어야 한다.

## 참고 링크

- [Git 공식 문서 — git merge](https://git-scm.com/docs/git-merge)
- [Git 공식 문서 — git diff](https://git-scm.com/docs/git-diff)
- [팀 충돌 대응 규칙](../docs/CONTRIBUTING.md#7-충돌-났을-때)
