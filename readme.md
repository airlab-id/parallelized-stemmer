# parallelized-stemmer
`parallelized-stemmer` aims to show report from the use of thread to improve time performance of stemmer algorithm.
This repository using python version `3.6.4`. 
Another dependencies that are used for this project listed on `/requirements.txt` (please do `pip freeze` after adding new dependencies).

### stemmer library
based on sastrawi `pip install PySastrawi`

### threading library
- package multiprocessing https://docs.python.org/3.4/library/multiprocessing.html?highlight=process

## usage
1. always use virtualenv so this project wont bother your machine
- on mac/linux run `source /bin/activate`
- on windows `\Scripts\activate`

to exit virtualenv just exit the terminal or run `deactivate`

2. `pip install -r requirements.txt` (for first time only)
3. run python `startup.py`

(additional)
update `requirements.txt` using `pip freeze > requirements.txt`

## how it works
![thread-flow](https://user-images.githubusercontent.com/4990180/46242844-a3f6d080-c3f7-11e8-8293-936bf563d0e9.jpeg)

## performance test using `time`
all test processed 87440 words, elapsed time measured in `seconds`

| #  | serial_stemmer     | multi-thread (3)   |
| -- |:------------------:| ------------------:|
| 1  | 172.53443098068237 | 138.93437695503235 |
| 2  | 181.88903880119324 | 133.10081505775452 |
| 3  | 181.69096302986145 | 114.8126060962677  |

