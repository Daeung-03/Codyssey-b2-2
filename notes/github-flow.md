# GitHub Flow — main과 작업 브랜치만 쓰는 단순한 전략

> 작성자: 김정현 (@kimjexnghyexn) · 관련 이슈: #4

## 한 줄 요약
GitHub Flow는 main과 작업 브랜치(feature/docs/fix 등) 딱 두 종류만 쓰면서, 모든 변경을 PR로 검토받고 main으로 머지하는 
단순한 협업 전략이다.

## 핵심 내용
- GitHub Flow는 브랜치 종류가 `main`과 작업 브랜치 둘뿐이다. `git-flow`처럼 develop, release, hotfix 같은 여러 단계 브랜치를 두지 않는다.
- `main`은 "항상 배포 가능한 상태"를 유지해야 한다는 원칙이 핵심이다. 즉 문서 링크가 살아있고, 예시 코드가 실행되고, 깨진 부분이 없어야 한다는 뜻이다.
- 이걸 지키기 위해 main에는 직접 push하지 않고, 모든 변경은 issue 생성 → 작업 브랜치 → PR → 리뷰 → approve → 머지 순서를 거친다.
- 왜 팀에 전략이 필요한가: 규칙 없이 각자 원하는 대로 커밋하고 push하면, main이 언제 깨질지 예측할 수 없고 누가 뭘 바꿨는지 추적하기 어렵다. GitHub Flow는 "브랜치 하나 = 이슈 하나 = PR 하나"로 강제해서, 변경 단위를 작게 쪼개고 리뷰를 거치게 만든다.
- 릴리스 버전 관리가 필요 없는 짧은 프로젝트(이번 미션처럼)에는 git-flow의 복잡한 구조가 과하고, GitHub Flow처럼 단순한 구조가 더 적합하다.

## 직접 해본 것
\`\`\`bash
$ git log --oneline --graph --all
*   6f42dca (HEAD -> docs/kimjexnghyexn-github-flow, origin/main, origin/HEAD, main) Merge pull request #3 from Daeung-03/docs/kimjexnghyexn-git-branch
|\  
| * 670a6c8 (origin/docs/kimjexnghyexn-git-branch) docs: 포인터 브랜치 헷갈렸던 점
| * 9cc815d docs: 브랜치 포인터 개념 노트 추가
|/  
* 5bf3784 docs: 협업 규칙 완성
* 8c1b506 docs: 이슈 템플릿 추가
* 40d31c9 docs: 팀 협업 계획과 문서 템플릿 추가
* 9858c6d Init: add problem.md
\`\`\`
git-branch 노트 PR이 머지되면서 main에 새 커밋이 쌓인 걸 확인했다. main 브랜치가 항상 하나의 안정된 지점을 유지하면서, 그 위에 검증된 변경사항만 순서대로 쌓인다는 걸 히스토리로 직접 봤다.

## 헷갈렸던 점
'계획서에 적혀있던 git flow는 이번 과제에서 과하다' 라는 것에 대해 이해하게 되었다. 소프트웨어 개발처럼 1.0버전이 현재 상용화되어있으며 2.0버전을 개발하고 있을때는 main(1.0버전)과 develop(2.0버전)을 각각 유지할 필요가 있기에 git flow가 필요하지만 이번 과제에서 요구하는 것에는 github-flow로 충분함을 알 수 있었다.