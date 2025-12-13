import asyncio

from gyrus import Context, Processor, State


class Node(Processor):
    async def process(self, ctx: Context, state: State) -> bool:
        # Simulate streaming data (e.g., LLM response)
        for i in range(3):
            await ctx.output.send(f"this is processor_channel_b {i}")
            await asyncio.sleep(1)

        return True
