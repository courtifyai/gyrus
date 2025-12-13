from gyrus import Context, Processor, State


class Node(Processor):
    async def process(self, ctx: Context, state: State) -> bool:
        print("this is processor_reentrant")
        reentrant_times = state.get("reentrant_times", 0)
        state.set("reentrant_times", reentrant_times + 1)
        return True
