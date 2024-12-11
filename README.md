# 개요

- langchain 을 공부하고 실습하는 프로젝트
- python version: 3.11
    - `.python-version` 참고

# LangChain 패키지들의 관계

```text
langchain-core (필수)
    ↑
    |
    |
langchain (선택)
    ↑
    |
langchain-community (선택)     langchain-openai (선택)
```

## 각 패키지의 역할과 의존성

### langchain-core (필수)

- 모든 LangChain 패키지의 기초가 되는 핵심 추상화와 인터페이스 제공
- 다른 모든 패키지들이 이에 의존함
- 반드시 필요

### langchain (선택)

- 고수준의 추상화와 체인, 에이전트 아키텍처 제공
- langchain-core에 의존
- 일반적인 LLM 응용 프로그램을 만들 때 유용하지만 필수는 아님

### langchain-community (선택)

- 다양한 서드파티 통합 제공
- langchain-core에 의존
- 특정 통합이 필요할 때만 설치

### langchain-openai (선택)

- OpenAI 전용 통합
- langchain-core에 의존
- OpenAI 서비스를 사용할 때만 필요

