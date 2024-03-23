# poetry add loguru

from loguru import logger

logger.add("execution_logs.csv", format="{time} - {message}", level="INFO", rotation="1 day")

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
    try:
        minha_primeira_atividade()
        minha_segunda_atividade()
        minha_terceira_atividade()
        logger.info("Pipeline rodou com sucesso")
    except:
        logger.info("Deu ruim na pipeline")

if __name__ == "__main__":
    while True:
        main()
        sleep(10)