import asyncio

from pyrogram import Client


print('Enter your app information from my.telegram.org/apps below.')


async def main():
    async with Client(
            session_name=':BAB1zJ0AId_hWhGFa4qe6T_IdmNVlbP1jKXr82eUPHiv99krLezUhKMEYRbYNzM8nJkShALq1mZ9HA8DtRGNbTcWoLOAw47K0qZx9gNimCnkofNLesnFHqAb1DtIa2C81KfNsxnlD8PPldKEXjnKW9TWjkPEG_DqU4Jv6fK4KuDNukgsLYbPe3lz27jTcWmOwkoZhyLYf5u07LMBqOH1CZdp97Aj_pZd8PftWeEsKQcY5C5pC8pPE90z01jA8XjZkCxBbLU0J1cGixuUo-4rEW9ZIaCbWbhurh_YXj7Lz1nX7tzfYJvW7TM9LPF5BdAlg0PQuErO8YsmEmbd1_7EpsmhWTootwAAAAFMob2wAA',
            api_id=int(input('20228807 ')),
            api_hash=input('7ce3d691d20bfead1f2640294201a052 '),
    ) as app:
        print(await app.export_session_string())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
