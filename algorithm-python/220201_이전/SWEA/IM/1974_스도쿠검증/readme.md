### 문제의도
- 이차원 리스트를 돌며 범위를 정해 확인하기
- 행우선, 열우선, 범위잡아 모든 요소 확인하기
- 임시배열 만들어 중복값 확인하기

### 접근
- 행우선, 열우선, 스퀘어 단위 조회를 각각 함수로 만들어, 모두 true 일 경우에만 true를 도출합니다.
- 하나라도 fail이면 결과는 fail이 됩니다.

### 오류
- `index out of range` 가 발생하였습니다.

### 원인
- 3 X 3 스퀘어 범위를 잡을 때, 범위조건을 잘못 설정였습니다.
- 9 미만이 아닌 10미만으로 설정해야, range (0, 9) 가 되어 인덱스 0부터 8까지 돕니다.
```python
if 0 <= 3*i < 9 and 0 <= 3*i + 3 < 9:
```

### 해결
- 디버깅 통해 범위조건을 수정하였습니다.
```python
            for k in range(3*i, 3*i + 3):
                for l in range(3*i, 3*i + 3):
                    if 0 <= 3*i < 10 and 0 <= 3*i + 3 < 10:
                        count[arr[k][l]] += 1
```