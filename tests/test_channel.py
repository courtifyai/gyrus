import asyncio
import time
import unittest

from gyrus.context import Context
from gyrus.cortex_manager import CortexManager
from gyrus.state import State


class TestChannel(unittest.IsolatedAsyncioTestCase):
    async def test_context(self):
        state = State()
        state.set("start_at", time.time())

        cm = CortexManager([{"name": "channel", "path": "tests/cortices/channel.yaml"}])
        cx = cm.get("channel")

        messages = []

        with Context() as ctx:
            asyncio.create_task(cx.run(ctx, state))

            async for message in ctx.output:
                messages.append(message)

        self.assertEqual(len(messages), 6)


if __name__ == "__main__":
    unittest.main()
