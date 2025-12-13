from gyrus import Context, Processor, State, node


@node(config="tests/cortices/config_for_processor.yaml")
class Node(Processor):
    def init(self):
        self.age = 10086
        pass

    async def process(self, ctx: Context, state: State) -> bool:
        state.set("name", self.config["name"])
        state.set("age", self.age)
        return True
