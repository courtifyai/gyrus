from gyrus import Context, Processor, State


class Node(Processor):
    async def process(self, ctx: Context, state: State) -> bool:
        print("this is processor_a")
        return self.trigger(["event_edit"])
