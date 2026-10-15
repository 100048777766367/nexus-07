class BaseMechanism:
    name = "base_mechanism"
    priority = 100

    def execute(self, context):
        raise NotImplementedError
