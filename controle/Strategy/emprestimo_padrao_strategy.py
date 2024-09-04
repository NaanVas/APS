from controle.Strategy.emprestimo_strategy import EmprestimoStrategy
from datetime import timedelta

class EmprestimoPadraoStrategy(EmprestimoStrategy):
    def calcular_periodo_emprestimo(self) -> timedelta:
        return timedelta(days=7)
    
    def calcular_multa(self, dias_atraso: int) -> float:
        return dias_atraso * 1

    def verificar_limite_livros(self) -> int:
        return 5
