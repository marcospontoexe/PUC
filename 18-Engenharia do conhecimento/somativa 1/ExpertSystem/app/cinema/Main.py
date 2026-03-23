from ExpertSystem.api.esMenu import APP
from ExpertSystem.app.cinema.RuleBaseVehicle import RuleBaseVehicle


class Main:
    def __init__(self):
        self.app = APP("Rule Application - Vehicle")

    def main(self):
        try:
            # RuleBaseVehicle recebe dois parâmetros:
            # o primeiro é o nome da base de regras e
            # o segundo é a lista de variáveis que podem ser consultas/objetivos.
            br_vehicle = RuleBaseVehicle(
                "Classificação de Veículos",
                "[veiculo, tipoDeVeiculo, tamanho, numeroDeRodas, numeroDePortas, motor] :"
            )
            self.app.add_rule_base(br_vehicle)
            self.app.menu()
        except Exception as e:
            print("Exception: RuleApp ", e.with_traceback())


if __name__ == '__main__':
    Main().main()
