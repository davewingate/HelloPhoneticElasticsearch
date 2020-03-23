
# hello_phonetic_elasticsearch
Demonstrates use of ES as a tool for searching similar English full names.
Key concepts:
 - `Robert` should match as a synonym of `Bob`.
 - Using "fuzzy" levenshtein distance, trivial spelling mistakes should still match:
   e.g. `Sara` vs. `Sarah` or `Cate` vs. `Kate`.
 - Using phonetic index, radically different spelling should still match when names are pronounced the same:
   e.g. `Ashley` vs `Ashleigh`


## Setup
```bash
pyenv virtualenv 3.7.3 hello_phonetic_elasticsearch
pyenv local 3.7.3/envs/hello_phonetic_elasticsearch
pip install -r requirements.txt
```

## Run
```bash
docker-compose up -d
python demo_analyzers.py
python demo_search.py
docker-compose down
```

### Sample Output
`python demo_analyzers.py`
```
trying out synonym analysis ...
Chris => [{'token': 'chris', 'start_offset': 0, 'end_offset': 5, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'christopher', 'start_offset': 0, 'end_offset': 5, 'type': 'SYNONYM', 'position': 0}]
christopher => [{'token': 'christopher', 'start_offset': 0, 'end_offset': 11, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'chris', 'start_offset': 0, 'end_offset': 11, 'type': 'SYNONYM', 'position': 0}]
robert => [{'token': 'robert', 'start_offset': 0, 'end_offset': 6, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'bob', 'start_offset': 0, 'end_offset': 6, 'type': 'SYNONYM', 'position': 0}]
paul => [{'token': 'paul', 'start_offset': 0, 'end_offset': 4, 'type': '<ALPHANUM>', 'position': 0}]

trying out phonetic analysis ...
nysis Krysten => [{'token': 'CRYSTA', 'start_offset': 0, 'end_offset': 7, 'type': '<ALPHANUM>', 'position': 0}]
nysis Christian => [{'token': 'CRASTA', 'start_offset': 0, 'end_offset': 9, 'type': '<ALPHANUM>', 'position': 0}]
beider_morse Krysten => [{'token': 'kristn', 'start_offset': 0, 'end_offset': 7, 'type': '<ALPHANUM>', 'position': 0}]
beider_morse Christian => [{'token': 'tzristian', 'start_offset': 0, 'end_offset': 9, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'tzristion', 'start_offset': 0, 'end_offset': 9, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'xrQstian', 'start_offset': 0, 'end_offset': 9, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'xrQstion', 'start_offset': 0, 'end_offset': 9, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'xristian', 'start_offset': 0, 'end_offset': 9, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'xristion', 'start_offset': 0, 'end_offset': 9, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'xritian', 'start_offset': 0, 'end_offset': 9, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'xrition', 'start_offset': 0, 'end_offset': 9, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'zristian', 'start_offset': 0, 'end_offset': 9, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'zristion', 'start_offset': 0, 'end_offset': 9, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'zritian', 'start_offset': 0, 'end_offset': 9, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'zrition', 'start_offset': 0, 'end_offset': 9, 'type': '<ALPHANUM>', 'position': 0}]
nysis Sarah => [{'token': 'SAR', 'start_offset': 0, 'end_offset': 5, 'type': '<ALPHANUM>', 'position': 0}]
nysis Zara => [{'token': 'ZAR', 'start_offset': 0, 'end_offset': 4, 'type': '<ALPHANUM>', 'position': 0}]
beider_morse Sarah => [{'token': 'sYra', 'start_offset': 0, 'end_offset': 5, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'sYro', 'start_offset': 0, 'end_offset': 5, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'sara', 'start_offset': 0, 'end_offset': 5, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'saro', 'start_offset': 0, 'end_offset': 5, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'sora', 'start_offset': 0, 'end_offset': 5, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'soro', 'start_offset': 0, 'end_offset': 5, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'zYra', 'start_offset': 0, 'end_offset': 5, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'zYro', 'start_offset': 0, 'end_offset': 5, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'zara', 'start_offset': 0, 'end_offset': 5, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'zaro', 'start_offset': 0, 'end_offset': 5, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'zora', 'start_offset': 0, 'end_offset': 5, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'zoro', 'start_offset': 0, 'end_offset': 5, 'type': '<ALPHANUM>', 'position': 0}]
beider_morse Zara => [{'token': 'dzara', 'start_offset': 0, 'end_offset': 4, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'dzaro', 'start_offset': 0, 'end_offset': 4, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'dzora', 'start_offset': 0, 'end_offset': 4, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'dzoro', 'start_offset': 0, 'end_offset': 4, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'sara', 'start_offset': 0, 'end_offset': 4, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'saro', 'start_offset': 0, 'end_offset': 4, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'sora', 'start_offset': 0, 'end_offset': 4, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'soro', 'start_offset': 0, 'end_offset': 4, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'tsYra', 'start_offset': 0, 'end_offset': 4, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'tsYro', 'start_offset': 0, 'end_offset': 4, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'tsara', 'start_offset': 0, 'end_offset': 4, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'tsaro', 'start_offset': 0, 'end_offset': 4, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'tsora', 'start_offset': 0, 'end_offset': 4, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'tsoro', 'start_offset': 0, 'end_offset': 4, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'zYra', 'start_offset': 0, 'end_offset': 4, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'zYro', 'start_offset': 0, 'end_offset': 4, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'zara', 'start_offset': 0, 'end_offset': 4, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'zari', 'start_offset': 0, 'end_offset': 4, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'zaro', 'start_offset': 0, 'end_offset': 4, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'zora', 'start_offset': 0, 'end_offset': 4, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'zori', 'start_offset': 0, 'end_offset': 4, 'type': '<ALPHANUM>', 'position': 0}, {'token': 'zoro', 'start_offset': 0, 'end_offset': 4, 'type': '<ALPHANUM>', 'position': 0}]
```

`python demo_search.py`
```
############# search_by_name_exact #############
 found 1 of 1 expected results for search "Chris De Avila": [NameSearch(name_search_80a9f3d4/1' name='Chris De Avila')]
 found 1 of 1 expected results for search "Christopher De Avila": [NameSearch(name_search_80a9f3d4/1' name='Chris De Avila')]
 found 0 of 0 expected results for search "Chris De Avilla": []
 found 0 of 0 expected results for search "Chris D'Avilla": []
 found 1 of 1 expected results for search "Cuthbert": [NameSearch(name_search_80a9f3d4/4' name='Cuthbert Allgood')]
 found 0 of 0 expected results for search "Cuthbert All": []
 found 0 of 0 expected results for search "Cutburt Awlgood": []
 found 1 of 1 expected results for search "Martin Luther King": [NameSearch(name_search_80a9f3d4/5' name='Dr. Martin Luther King Jr.')]
 found 1 of 1 expected results for search "Dr. King Jr.": [NameSearch(name_search_80a9f3d4/5' name='Dr. Martin Luther King Jr.')]

############# search_by_name_fuzzy #############
 found 1 of 1 expected results for search "Chris De Avila": [NameSearch(name_search_80a9f3d4/1' name='Chris De Avila')]
 found 1 of 1 expected results for search "Chris De Avilla": [NameSearch(name_search_80a9f3d4/1' name='Chris De Avila')]
 found 0 of 0 expected results for search "Chris D'Avilla": []
 found 1 of 1 expected results for search "Cuthbert": [NameSearch(name_search_80a9f3d4/4' name='Cuthbert Allgood')]
 found 0 of 0 expected results for search "Cuthbert All": []
 found 1 of 1 expected results for search "Cutburt Awlgood": [NameSearch(name_search_80a9f3d4/4' name='Cuthbert Allgood')]
 found 1 of 1 expected results for search "Martin Luther King": [NameSearch(name_search_80a9f3d4/5' name='Dr. Martin Luther King Jr.')]
 found 1 of 1 expected results for search "Dr. King Jr.": [NameSearch(name_search_80a9f3d4/5' name='Dr. Martin Luther King Jr.')]

############# search_by_name_phonetic #############
 found 1 of 1 expected results for search "Chris De Avila": [NameSearch(name_search_80a9f3d4/1' name='Chris De Avila')]
 found 1 of 1 expected results for search "Chris De Avilla": [NameSearch(name_search_80a9f3d4/1' name='Chris De Avila')]
 found 1 of 1 expected results for search "Chris D'Avilla": [NameSearch(name_search_80a9f3d4/1' name='Chris De Avila')]
 found 1 of 1 expected results for search "Cuthbert": [NameSearch(name_search_80a9f3d4/4' name='Cuthbert Allgood')]
 found 0 of 0 expected results for search "Cuthbert All": []
 found 1 of 1 expected results for search "Cutburt Awlgood": [NameSearch(name_search_80a9f3d4/4' name='Cuthbert Allgood')]
 found 1 of 1 expected results for search "Martin Luther King": [NameSearch(name_search_80a9f3d4/5' name='Dr. Martin Luther King Jr.')]
 found 1 of 1 expected results for search "Dr. King Jr.": [NameSearch(name_search_80a9f3d4/5' name='Dr. Martin Luther King Jr.')]

```
