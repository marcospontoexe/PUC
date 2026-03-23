from ExpertSystem.api.esBooleanRuleBase import BooleanRuleBase
from ExpertSystem.api.esRuleVariable import RuleVariable
from ExpertSystem.api.esCondition import Condition
from ExpertSystem.api.esRule import Rule
from ExpertSystem.api.esClause import Clause


class RuleBaseVehicle:
    def __init__(self, nome, goals_list):
        self.br = BooleanRuleBase(nome)
        self.goals_list = goals_list

    def get_goal_list(self):
        return self.goals_list

    def create(self):
        veiculo = RuleVariable(self.br, "veiculo")
        veiculo.set_labels(
            "bicicleta triciclo motocicleta carroEsporte sedan minivan veiculoEsporteUtilitario"
        )
        veiculo.set_prompt_text(
            "Que tipo de veículo é esse [bicicleta, triciclo, motocicleta, carroEsporte, sedan, minivan]?"
        )

        tipo_de_veiculo = RuleVariable(self.br, "tipoDeVeiculo")
        tipo_de_veiculo.set_labels("velocipede automotivo")
        tipo_de_veiculo.set_prompt_text(
            "Que tipo de veículo é esse [velocipede, automotivo]?"
        )

        tamanho = RuleVariable(self.br, "tamanho")
        tamanho.set_labels("pequeno medio grande")
        tamanho.set_prompt_text(
            "Qual é o tamanho do veículo [pequeno, medio, grande]?"
        )

        numero_de_rodas = RuleVariable(self.br, "numeroDeRodas")
        numero_de_rodas.set_labels("2 3 4")
        numero_de_rodas.set_prompt_text(
            "Quantas rodas o veículo possui [2, 3, 4]?"
        )

        numero_de_portas = RuleVariable(self.br, "numeroDePortas")
        numero_de_portas.set_labels("2 3 4")
        numero_de_portas.set_prompt_text(
            "Quantas portas o veículo tem [2, 3, 4]?"
        )

        motor = RuleVariable(self.br, "motor")
        motor.set_labels("sim nao")
        motor.set_prompt_text(
            "O veículo tem um motor [sim, nao]?"
        )

        c_equals = Condition("=")
        c_more_then = Condition(">")
        c_less_than = Condition("<")

        Rule(
            self.br,
            "Regra 01 - velocipede",
            [Clause(numero_de_rodas, c_less_than, "4")],
            Clause(tipo_de_veiculo, c_equals, "velocipede"),
        )

        Rule(
            self.br,
            "Regra 02 - automotivo",
            [Clause(numero_de_rodas, c_equals, "4"), Clause(motor, c_equals, "sim")],
            Clause(tipo_de_veiculo, c_equals, "automotivo"),
        )

        Rule(
            self.br,
            "Regra 03 - bicicleta",
            [
                Clause(tipo_de_veiculo, c_equals, "velocipede"),
                Clause(numero_de_rodas, c_equals, "2"),
                Clause(motor, c_equals, "nao"),
            ],
            Clause(veiculo, c_equals, "bicicleta"),
        )

        Rule(
            self.br,
            "Regra 04 - triciclo",
            [
                Clause(tipo_de_veiculo, c_equals, "velocipede"),
                Clause(numero_de_rodas, c_equals, "3"),
                Clause(motor, c_equals, "nao"),
            ],
            Clause(veiculo, c_equals, "triciclo"),
        )

        Rule(
            self.br,
            "Regra 05 - motocicleta",
            [
                Clause(tipo_de_veiculo, c_equals, "velocipede"),
                Clause(numero_de_rodas, c_equals, "2"),
                Clause(motor, c_equals, "sim"),
            ],
            Clause(veiculo, c_equals, "motocicleta"),
        )

        Rule(
            self.br,
            "Regra 06 - carroEsporte",
            [
                Clause(tipo_de_veiculo, c_equals, "automotivo"),
                Clause(tamanho, c_equals, "medio"),
                Clause(numero_de_portas, c_equals, "2"),
            ],
            Clause(veiculo, c_equals, "carroEsporte"),
        )

        Rule(
            self.br,
            "Regra 07 - sedan",
            [
                Clause(tipo_de_veiculo, c_equals, "automotivo"),
                Clause(tamanho, c_equals, "medio"),
                Clause(numero_de_portas, c_equals, "4"),
            ],
            Clause(veiculo, c_equals, "sedan"),
        )

        Rule(
            self.br,
            "Regra 08 - minivan",
            [
                Clause(tipo_de_veiculo, c_equals, "automotivo"),
                Clause(tamanho, c_equals, "medio"),
                Clause(numero_de_portas, c_equals, "3"),
            ],
            Clause(veiculo, c_equals, "minivan"),
        )

        Rule(
            self.br,
            "Regra 09 - SUV",
            [
                Clause(tipo_de_veiculo, c_equals, "automotivo"),
                Clause(tamanho, c_equals, "grande"),
                Clause(numero_de_portas, c_equals, "4"),
            ],
            Clause(veiculo, c_equals, "veiculoEsporteUtilitario"),
        )

        return self.br

    def demo_fc(self, LOG):
        LOG.append(" --- Ajustando valores para demo ForwardChain - Veiculos ---")
        self.br.set_variable_value("veiculo", None)
        self.br.set_variable_value("tipoDeVeiculo", None)
        self.br.set_variable_value("tamanho", "grande")
        self.br.set_variable_value("numeroDeRodas", "4")
        self.br.set_variable_value("numeroDePortas", "4")
        self.br.set_variable_value("motor", "sim")
        self.br.display_variables(LOG)

    def demo_bc(self, LOG):
        LOG.append(" --- Ajustando valores para demo BackwardChain - Veiculos ---")
        self.br.set_variable_value("veiculo", None)
        self.br.set_variable_value("tipoDeVeiculo", None)
        self.br.set_variable_value("tamanho", None)
        self.br.set_variable_value("numeroDeRodas", "4")
        self.br.set_variable_value("numeroDePortas", None)
        self.br.set_variable_value("motor", "sim")
        self.br.display_variables(LOG)
