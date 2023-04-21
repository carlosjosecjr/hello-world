from asyncio import get_event_loop

async def main():
    print("Hello, world!")

if __name__ == "__main__":
    loop = get_event_loop()
    loop.run_until_complete(main())