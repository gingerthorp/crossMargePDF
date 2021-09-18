# crossMargePDF

### package 
```
pip install PyPDF2
```

### 프로젝트 목적
영어 PDF 자료를 번역(https://www.onlinedoctranslator.com/en/)하여
영어 PDF와 한글 PDF를 교차로 합쳐 효율적으로 보기 위함.


### 추후 계획
- 문서 번역(https://www.onlinedoctranslator.com/en/)의 API를 사용하여 원본(영어) PDF만 입력하면 번역과 교차 합치기까지 자동화.  
(문서 번역 서비스에 API 사용 신청함.)

- 깃허브 액션 <-> 람다 사용하여 배포 자동화

- 람다에 프로젝트를 올려서 서비스화

- 예상 플로우
    1. 정적 웹서비스(s3)
    2. 웹에 PDF 올림.
    3. S3 트리거로 람다 동작.
    4. 람다에서 PDF 번역 및 합치기 생성.
    5. 완성된 PDF S3 올림.
    6. S3 다운로드 링크 전달.
