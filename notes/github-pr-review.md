# Pull Request와 코드 리뷰
> 작성자: 김승우 (@stevenkim18) · 관련 이슈: #14

## 한 줄 요약

Pull Request(PR)는 작업 브랜치를 `main`에 병합하기 전에 변경 의도와 영향을 함께 검토하는 협업 단위이며, 코드 리뷰는 구체적인 근거를 바탕으로 품질과 공유 이해를 높이는 과정이다.

## 핵심 내용

### PR의 목적과 흐름

PR은 단순히 "코드를 올렸다"는 알림이 아니다. 이슈로 작업 목적을 추적하고, 변경 파일과 검증 방법을 팀원이 읽을 수 있게 하며, 승인받은 변경만 `main`에 넣는 검토 창구다. 이 팀에서는 다음 흐름을 사용한다.

1. 이슈를 만들고 최신 `main`에서 작업 브랜치를 만든다.
2. 의미 단위로 커밋하고 원격 브랜치에 push한다.
3. PR 본문에 `Closes #이슈번호`, What, Why, How를 작성한다.
4. 리뷰어가 파일·줄을 근거로 코멘트를 남기고, 작성자는 답글이나 새 커밋으로 반영한다.
5. approve 1개와 모든 대화 해결을 확인한 뒤 **merge commit**으로 병합한다.

`Closes #이슈번호`는 PR을 열 때 이슈를 자동으로 닫는 문장이 아니다. PR이 기본 브랜치에 병합될 때 해당 이슈를 닫아 작업과 결과를 연결한다.

### 코드 리뷰가 필요한 이유

- 작성자 혼자 놓친 오류, 깨진 문서 링크, 위험한 Git 명령을 발견할 수 있다.
- 왜 이런 선택을 했는지 기록으로 남아 팀원이 변경 맥락을 이해할 수 있다.
- `main`에 들어가는 변경을 한 사람이 아닌 팀이 함께 책임진다.

### 좋은 리뷰 코멘트

좋은 리뷰는 사람을 평가하지 않고 파일 또는 줄의 변경을 근거로, 다음 행동이 무엇인지 알 수 있게 쓴다. `LGTM`, "좋아요" 또는 approve만 남기면 무엇을 확인했는지와 개선할 점이 남지 않는다.

```txt
[must] notes/git-conflict.md:43에서 충돌 명령은 있는데 실패한 뒤의
git status 출력이 없습니다. `UU` 상태를 확인할 수 있는 출력도 추가해 줄 수 있나요?

[nit] notes/git-undo.md:70의 `reset --hard` 설명 바로 아래에
공유된 브랜치에서는 사용하지 않는다는 문장을 넣으면 실습자가 더 안전할 것 같습니다.
```

`[must]`는 병합 전에 반드시 고쳐야 할 문제, `[nit]`은 선택적인 제안이라는 뜻으로 구분한다. 작성자는 코멘트마다 답하고, 실제로 수정했다면 `amend`나 force push 대신 새 커밋을 올려 리뷰 맥락을 보존한다.

## 직접 해본 것

현재 열린 PR 목록을 확인하고, 내가 만든 충돌 노트 PR(#16)의 이슈 연동·변경 파일을 조회했다. PR이 어느 브랜치에서 어느 브랜치로 가는지와 `Closes #13`이 본문에 들어 있는 것을 확인할 수 있었다.

```bash
gh pr list --repo Daeung-03/Codyssey-b2-2 --state open --limit 10 \
  --json number,title,headRefName,baseRefName \
  --jq '.[] | "#\(.number) \(.headRefName) → \(.baseRefName): \(.title)"'

gh api repos/Daeung-03/Codyssey-b2-2/pulls/16 \
  --jq '"PR #\(.number): \(.head.ref) → \(.base.ref)\n제목: \(.title)\n이슈 연결: \(.body | split("\n") | map(select(test("Closes #"))) | join(", "))"'

gh api repos/Daeung-03/Codyssey-b2-2/pulls/16/files --jq '.[].filename'
```

```txt
#16 docs/stevenkim18-git-conflict → main: docs: Git 충돌 노트 작성
#12 docs/kimjexnghyexn-troubleshoot-amend → main: Docs/kimjexnghyexn troubleshoot amend
#8 docs/daeung-03-git-undo → main: docs: Git 되돌리기 노트 작성
#5 docs/kimjexnghyexn-github-flow → main: docs: GitHub Flow 노트 추가

PR #16: docs/stevenkim18-git-conflict → main
제목: docs: Git 충돌 노트 작성
이슈 연결: - Closes #13
notes/README.md
notes/git-conflict.md
```

기존 PR의 리뷰 기록도 읽어 봤다. approve는 병합 가능하다는 의사 표현이지만, 팀 규칙에 맞는 리뷰가 되려면 이와 별개로 파일·줄을 근거로 한 실질 코멘트가 필요하다.

```bash
gh api repos/Daeung-03/Codyssey-b2-2/pulls/3/reviews \
  --jq '.[] | "리뷰어: @\(.user.login), 상태: \(.state), 내용: \(.body)"'
```

```txt
리뷰어: @Daeung-03, 상태: APPROVED, 내용: 현재 브랜티, 브랜치 변경 등 실제로 어떻게 git이 광리하고 있는지 직접적으로 알 수 있는 좋은 학습이었던 것 같습니다. 승인 후 merge 하겠습니다!
```

이 기록은 긍정적인 피드백과 승인은 남지만, 특정 파일이나 줄에 대한 질문·개선 요청은 없다. 따라서 앞으로 리뷰할 때는 위 예시처럼 변경 위치와 이유를 함께 적어야 한다.

## 헷갈렸던 점

PR의 approve와 코드 리뷰는 같은 말이 아니다. approve는 현재 변경을 병합해도 된다는 최종 판단이고, 코드 리뷰는 그 판단에 이르는 확인과 대화 과정이다. 또한 PR을 만든 뒤 `main`이 바뀌면 내 브랜치에서 최신 `main`을 반영하고, 충돌이 나면 내 브랜치에서 해결한 뒤 다시 리뷰를 요청해야 한다.

## 참고 링크

- [GitHub Docs — Pull requests](https://docs.github.com/pull-requests)
- [GitHub Docs — Pull request review](https://docs.github.com/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests)
- [팀 PR·코드 리뷰 규칙](../docs/CONTRIBUTING.md#5-pr-규칙)
