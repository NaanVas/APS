from abc import ABC, abstractmethod
from datetime import timedelta

class EmprestimoStrategy(ABC):
    @abstractmethod
    def calcular_periodo_emprestimo(self) -> timedelta:
        pass

    @abstractmethod
    def calcular_multa(self, dias_atraso: int) -> float:
        pass

    @abstractmethod
    def verificar_limite_livros(self) -> int:
        pass
