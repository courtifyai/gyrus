import asyncio
import time

from gyrus import Context, Processor, State


class Node(Processor):
    async def process(self, ctx: Context, state: State) -> bool:
        await asyncio.sleep(3)
        cost = int(time.time() - state.get("start_at"))
        state.set("b", cost)

        print(f"this is processor_b, {cost}")
        return self.trigger(["event_select", "event_delete", "event_reentrant"])
