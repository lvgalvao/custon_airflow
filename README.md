# custon_airflow

# Fazer o exemplo_00.py

```python
from time import sleep

def minha_primeira_atividade():
    print("essa foi a primeira atividade")
    sleep(1)

def minha_segunda_atividade():
    print("essa foi a segunda atividade")
    sleep(1)

def minha_terceira_atividade():
    print("essa foi a terceira atividade")
    sleep(1)

def main():
    minha_primeira_atividade()
    minha_segunda_atividade()
    minha_terceira_atividade()

if __name__ == "__main__":
    while True:
        main()
        sleep(10)
```