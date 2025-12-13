import asyncio

from gyrus import Context, Processor, State


class Node(Processor):
    async def process(self, ctx: Context, state: State) -> bool:
        await asyncio.sleep(1)
        print("this is processor_rude")
        self.stop("killable")
        return True
