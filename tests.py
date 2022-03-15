import asyncio
import random

import async_case


class Tests(async_case.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        await super().asyncSetUp()
        self.number = random.randint(2, 4)

    async def asyncTearDown(self):
        await super().asyncTearDown()

    async def test_it(self):
        async def sleep_square(num):
            await asyncio.sleep(0.5)
            return pow(num, 2)
        self.assertEqual(
            pow(self.number, 2),
            await sleep_square(self.number))
