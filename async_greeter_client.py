# Copyright 2020 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python AsyncIO implementation of the GRPC helloworld.Greeter client."""

import asyncio
import logging

from definitions.scraper import ScraperStub
from grpclib.client import Channel
import sys



async def run() -> None:
    async with Channel('localhost',sys.argv[1]) as channel:
        scraper = ScraperStub(channel)
        response = await scraper.search(text="jaguar")
        print(response)

        scraper = ScraperStub(channel)
        response = await scraper.long_search(text="jaguar")
        print(response)
        # print("Greeter client received: " + response)


if __name__ == '__main__':
    logging.basicConfig()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
    # asyncio.run(run())
