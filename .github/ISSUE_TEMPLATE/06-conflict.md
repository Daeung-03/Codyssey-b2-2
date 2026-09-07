---
name: 💥 충돌 실습
about: 의도적으로 충돌을 만들고 해결·기록하는 실습
title: 'docs: 충돌 실습 #N 진행 및 기록'
---

## 실습 정보
- 충돌 번호: #
- 유형: 같은 위치 동시 수정 / 파일 이름 변경 vs 내용 수정
- 대상 파일:
- 해결·기록 담당:
- 상대:

## 진행 순서
<!-- README 6번 시나리오 참고 -->
- [ ] 두 사람이 **같은 main 커밋**에서 브랜치 생성 (`git log --oneline -1` 로 서로 확인)
- [ ] 먼저 머지하는 쪽 PR 머지
- [ ] 나중 쪽 push → PR에 conflict 표시 확인
- [ ] 나중 쪽이 자기 브랜치에서 해결
- [ ] `git diff` / `git status` 출력 복사
- [ ] `docs/conflict-resolution.md` 기록 작성
- [ ] PR에 해결 요약 코멘트

## 기록에 반드시 넣을 것
- 충돌 마커 원문 (또는 modify/delete 메시지)
- 어느 쪽을 왜 골랐는지 (keep both / choose one / 옮겨 붙이기)
- 실행한 명령
- PR·커밋 링크

## 브랜치
`docs/<깃헙아이디>-<주제>` — main에서 해결하지 않습니다
