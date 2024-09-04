from controle.Strategy.emprestimo_strategy import EmprestimoStrategy
from datetime import timedelta

class EmprestimoFuncionarioStrategy(EmprestimoStrategy):
    def calcular_periodo_emprestimo(self) -> timedelta:
        return timedelta(days=14)
    
    def calcular_multa(self, dias_atraso: int) -> float:
        return dias_atraso * 0.5

    def verificar_limite_livros(self) -> int:
        return 7
