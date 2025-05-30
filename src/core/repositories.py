
class Repository:
    @staticmethod
    def load_data(data_path: str) -> dict:
        with open(data_path) as file:
            return yaml.safe_load(file)
