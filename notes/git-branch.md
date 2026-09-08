-# 브랜치는 커밋을 가리키는 포인터

> 작성자: 김정현 (@kimjexnghyexn) · 관련 이슈: #2

## 한 줄 요약
브랜치는 새로운 저장 공간이 아니라, 특정 커밋을 가리키는 이름표(포인터)일 뿐이다.

## 핵심 내용
- 브랜치는 `.git/refs/heads/<브랜치이름>` 파일로 존재하고, 그 안에는 커밋 해시 한 줄만 들어있다.
- `HEAD`는 "지금 내가 어느 브랜치에 있는지"를 가리키는 포인터로, `.git/HEAD`에 `ref: refs/heads/<브랜치이름>` 형태로 저장된다.
- 브랜치를 만드는 건 새 커밋을 만드는 게 아니라, 현재 커밋에 새 이름표를 붙이는 것뿐이라 생성 비용이 거의 없다.
- 그래서 여러 명이 각자 브랜치를 나눠서 작업해도, 서로 다른 이름표가 각자의 작업 지점을 가리킬 뿐 원본(main)에는 영향이 없다. 작업이 끝나면 PR로 병합해서 이름표가 가리키는 지점을 합친다.

## 직접 해본 것
\`\`\`bash
$ git branch test-branch
$ cat .git/refs/heads/test-branch
5bf3784c9faf0c32a5905266d5cad03933cc3f27

$ cat .git/HEAD
ref: refs/heads/docs/kimjexnghyexn-git-branch

$ git log --oneline --graph --all
* 5bf3784 (HEAD -> docs/kimjexnghyexn-git-branch, origin/main, origin/HEAD, test-branch, main) docs: 협업 규칙 완성
* 8c1b506 docs: 이슈 템플릿 추가
\`\`\`
`test-branch`를 만든 직후에는 main, test-branch, 지금 작업 브랜치가 전부 같은 커밋(5bf3784)을 가리키고 있는 걸 확인했다. 브랜치를 만든다고 해서 새 커밋이 생기지 않는다는 걸 눈으로 봤다.

## 헷갈렸던 점
브랜치를 checkout을 통해서 넘나들때 작업공간을 새로 복사하여 저장공간을 많이 쓸 줄 알았는데, 브랜치 이름으로 된 파일에 해당 커밋상태를 나타내는 해쉬값만을 저장함을 알게되어 큰 메모리 낭비가 없음을 알게되었다. 또한 해당 커밋 상태를 나타내는 해쉬값을 참조하여 파일의 상태를 이에 기반하여 바꿔줌을 알 수 있었다.