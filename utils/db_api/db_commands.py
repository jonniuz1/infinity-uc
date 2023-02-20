from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME
        )

    async def execute(
            self,
            command,
            *args,
            fetch: bool = False,
            fetchval: bool = False,
            fetchrow: bool = False,
            execute: bool = False,
    ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_users(self):
        sql = """
                    CREATE TABLE IF NOT EXISTS Users
            (
                chat_id bigint NOT NULL,
                username text NULL,
                active boolean NOT NULL,
                withdrawed_uc int NULL default 0,
                referral bigint NULL ,
                count_referrals bigint NOT NULL default 0,
                CONSTRAINT users_pkey PRIMARY KEY (chat_id)
            );"""
        await self.execute(sql, execute=True)

    async def create_table_channels(self):
        sql = """
                    CREATE TABLE IF NOT EXISTS channel
            (
                channel_id bigint NOT NULL,
                CONSTRAINT channels_pkey PRIMARY KEY (channel_id)
            );"""
        await self.execute(sql, execute=True)

    async def create_table_price_uc(self):
        sql = """
                    CREATE TABLE IF NOT EXISTS Price_uc
            (
                price_uc bigint NOT NULL
            );"""
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join(
            [f"{item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)]
        )
        return sql, tuple(parameters.values())

    async def add_user(self, chat_id, username, active, withdrawed_uc, referral, count_referrals):
        sql = "INSERT INTO users (chat_id, username, active, withdrawed_uc, referral, count_referrals) VALUES($1, $2, $3, $4, $5, $6) returning *"
        return await self.execute(sql, chat_id, username, active, withdrawed_uc, referral, count_referrals,
                                  fetchrow=True)

    async def add_channel(self, channel_id):
        sql = "INSERT INTO channel (channel_id) VALUES($1) returning *"
        return await self.execute(sql, channel_id, fetchrow=True)

    async def add_price_uc(self, price):
        sql = f"""INSERT INTO price_uc (price_uc) VALUES ({price})"""
        return await self.execute(sql, fetchrow=True)

    async def set_active(self, chat_id, active):
        sql = f"UPDATE users SET active=$2 WHERE chat_id=$1"
        return await self.execute(sql, chat_id, active, execute=True)

    async def select_top_referals(self):
        sql = "SELECT chat_id, count_referrals FROM users ORDER BY count_referrals DESC LIMIT 10;"
        return await self.execute(sql, fetch=True)

    async def select_top_withdrawers(self):
        sql = "SELECT chat_id, withdrawed_uc FROM users ORDER BY withdrawed_uc DESC LIMIT 10;"
        return await self.execute(sql, fetch=True)

    async def select_all_users(self):
        sql = "SELECT chat_id FROM Users"
        return await self.execute(sql, fetch=True)

    async def select_all_channels(self):
        sql = "SELECT channel_id FROM channel"
        return await self.execute(sql, fetch=True)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def is_exist_user(self, identifier: int) -> bool:
        command = f'''
                SELECT chat_id FROM users WHERE chat_id = {identifier}
                        '''
        f = await self.execute(command, fetchval=True)

        return bool(f)

    async def update_invites_count(self, user_id: int):
        invites_count = await self.get_invites_count_by_id(user_id) + 1
        sql = f"""UPDATE users SET count_referrals={invites_count} WHERE chat_id={user_id};"""
        await self.execute(sql, execute=True)

    async def get_invites_count_by_id(self, identifier: int) -> int:
        sql = f"""SELECT count_referrals FROM public.users WHERE chat_id={identifier};
         """
        invites_count = await self.execute(sql, fetchval=True)
        return invites_count

    async def update_withdrawed_uc(self, chat_id, new_withdrawed_uc):
        withdrawed_uc = await self.get_withdrawed_uc_by_id(chat_id) + new_withdrawed_uc
        sql = f"UPDATE users SET withdrawed_uc=$2 WHERE chat_id=$1"
        return await self.execute(sql, chat_id, withdrawed_uc, execute=True)

    async def get_withdrawed_uc_by_id(self, iden: int) -> int:
        sql = f"""SELECT withdrawed_uc FROM public.users WHERE chat_id={iden};
                 """
        invites_count = await self.execute(sql, fetchval=True)
        return invites_count

    async def get_price_uc(self):
        sql = "select * from price_uc offset ((select count(*) from price_uc)-1)"
        latest_price = await self.execute(sql, fetchval=True)
        return latest_price

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM Users"
        return await self.execute(sql, fetchval=True)

    async def count_active_users(self):
        sql = "SELECT COUNT(*) FROM Users WHERE active=true"
        return await self.execute(sql, fetchval=True)

    async def update_user_username(self, username, telegram_id):
        sql = "UPDATE Users SET username=$1 WHERE telegram_id=$2"
        return await self.execute(sql, username, telegram_id, execute=True)

    async def delete_users(self):
        await self.execute("DELETE FROM Users WHERE TRUE", execute=True)

    async def drop_users(self):
        await self.execute("DROP TABLE Users", execute=True)
