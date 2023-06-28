# db_python

simple wrapper for database with Python

Python으로 SQL 다룰 때마다 공식 문서 찾아가며 driver 직접 다루기 귀찮아 미리 만들어두는 패키지

## 사용법

- DB 정보 및 쿼리 파일 읽기

```python
from src.app import *

db = get_db('sample.json')
q = get_query('sample.sql')
```

- 쿼리 실행

```python
from src import mssql

res = mssql.read(db, q)
print(res)
```

- 쿼리는 문자열 데이터이기 때문에 아래와 같이 직접 입력 가능

```python
from datetime import datetime, timedelta

import pandas as pd

from src import *

d = datetime.strptime('2022-12-01', '%Y-%m-%d')
now = datetime.now()

db = get_db('sample.json')

q = '''
SELECT *
FROM table
WHERE date_create = '%s'
'''

while True:
    if d.year == now.year and d.month == now.month and d.day == now.day:
        break

    date = d.strftime('%Y-%m-%d')
    data = read(db, q % date)

    d += timedelta(days=1)

    if not data:
        continue

    res = pd.DataFrame(data)
    res.to_csv(f'{date.replace("-", "")}.csv', index=False)
```