import aiosqlite
default = "-"
defaultzero = "0"


async def connect():
    try:
        conn = await aiosqlite.connect(database='data.db')
        cursor = await conn.cursor()
        return conn, cursor
    except Exception as e:
        print(f"Ошибка в базе данных: {e}")


async def close(conn):
    await conn.commit()
    await conn.close()


class DBCommands:

    async def create_table(self):
        conn, cursor = await connect()
        try:
            await cursor.execute(f'''CREATE TABLE IF NOT EXISTS users
                              (id INTEGER PRIMARY KEY,
                               name TEXT,
                               mention int,
                               icon BLOB DEFAULT NULL,
                               race TEXT DEFAULT "{default}",
                               titul TEXT DEFAULT "{default}",
                               quote TEXT DEFAULT "{default}",
                               age TEXT DEFAULT "{default}",
                               job TEXT DEFAULT "{default}",
                               strength TEXT DEFAULT "{defaultzero}",
                               agility TEXT DEFAULT "{defaultzero}",
                               reaction TEXT DEFAULT "{defaultzero}",
                               accuracy TEXT DEFAULT "{defaultzero}",
                               stamina TEXT DEFAULT "{defaultzero}",
                               durability TEXT DEFAULT "{defaultzero}",
                               skills TEXT DEFAULT "{defaultzero}",
                               magic TEXT DEFAULT "{defaultzero}",
                               harki TEXT DEFAULT "{defaultzero}",
                               devil_fruit TEXT DEFAULT "{default}",
                               quirk TEXT DEFAULT "{default}",
                               mythical_soul TEXT DEFAULT "{default}",
                               favor TEXT DEFAULT "{default}",
                               stars TEXT DEFAULT "{default}",
                               will_weapon TEXT DEFAULT "{default}",
                               will_observation TEXT DEFAULT "{default}",
                               will_king TEXT DEFAULT "{default}",
                               demon_contract TEXT DEFAULT "{default}"
                               )''')
        finally:
            await close(conn)

    async def check_id(self, id):
        ids = await self.fetch_all_id()
        if id in ids:
            return True
        return False

    async def add_user(self, data):
        conn, cursor = await connect()
        try:
            await cursor.execute("INSERT INTO users (id, name, mention)"
                                 "VALUES (?, ?, ?)", (data))
        except aiosqlite.OperationalError as e:
            await self.create_table()
            print(f"Произошла ошибка в базе данных ({e})")
        finally:
            await close(conn)

    async def search(self, data):
        conn, cursor = await connect()
        try:
            await cursor.execute("SELECT * FROM users WHERE id=?", (data,))
            results = await cursor.fetchone()
            if results:
                return results
            else:
                return False
        except aiosqlite.OperationalError as e:
            await self.create_table()
            print(f"Произошла ошибка в базе данных ({e})")
        finally:
            await close(conn)

    async def update_other(self, data):
        conn, cursor = await connect()
        try:
            ostalnoe = await self.search(data)
            summa = sum([int(ostalnoe[i]) for i in range(9, 17) if ostalnoe[i].isdigit()])
            await cursor.execute(f"UPDATE users SET harki = ? WHERE id = ?", (str(summa), data))
        except Exception as e:
            print(e)
        finally:
            await close(conn)

    async def update_data(self, data, update=None):
        conn, cursor = await connect()
        try:
            await cursor.execute(f"UPDATE users SET {data[0]} WHERE id = ?", (data[1:]))
        except Exception as e:
            await self.create_table()
            print(f"Произошла ошибка в базе данных ({e})")
        finally:
            await close(conn)
            if update:
                await self.update_other(int(data[-1]))
            returndata = await self.search(int(data[-1]))
            return returndata

    async def delete_user(self, data):
        conn, cursor = await connect()
        try:
            await cursor.execute(f"DELETE FROM users WHERE id = ?", (data,))
        except aiosqlite.OperationalError as e:
            await self.create_table()
            print(f"Произошла ошибка в базе данных ({e})")
        finally:
            await close(conn)

    async def fetch_all_id(self):
        conn, cursor = await connect()
        try:
            await cursor.execute("SELECT id FROM users")
            results = await cursor.fetchall()
            return [i[0] for i in results]
        except aiosqlite.OperationalError as e:
            await self.create_table()
            print(f"Произошла ошибка в базе данных ({e})")
        finally:
            await close(conn)

    async def fetch_all_person_by_user(self, data):
        conn, cursor = await connect()
        try:
            await cursor.execute("SELECT id, name FROM users WHERE mention = ?", (data,))
            results = await cursor.fetchall()
            return results
        except Exception as e:
            await self.create_table()
            print(f"Произошла ошибка в базе данных ({e})")
        finally:
            await close(conn)

    async def top_balance(self, offset):
        conn, cursor = await connect()
        offset = str(offset * 10)
        try:
            await cursor.execute(f"""
                    SELECT id, name, harki
                    FROM users
                    ORDER BY CAST(harki AS INTEGER) DESC
                    LIMIT 10 OFFSET {offset}
                """)
            top = await cursor.fetchall()
            return top
        except Exception as e:
            await self.create_table()
            print(f"Ошибка в топе: {e}")
        finally:
            await close(conn)

    async def swap_ids(self, data):
        conn, cursor = await connect()
        num = 92233720368
        try:
            await cursor.execute(f"UPDATE users SET id = ? WHERE id = ?", (num, data[0]))
            await cursor.execute(f"UPDATE users SET id = ? WHERE id = ?", (data[0], data[1]))
            await cursor.execute(f"UPDATE users SET id = ? WHERE id = ?", (data[1], num))
        except Exception as e:
            await self.create_table()
            print(f"Произошла ошибка в базе данных ({e})")
        finally:
            await close(conn)
    # NE TROGAT WTF

    async def add_column_color(self):
        conn, cursor = await connect()
        try:
            await cursor.execute("PRAGMA table_info(users)")
            columns = await cursor.fetchall()
            column_names = [column[1] for column in columns]
            if 'color' not in column_names:
                await cursor.execute("ALTER TABLE users ADD COLUMN color TEXT DEFAULT 'random'")
                print("Колонка 'color' добавлена")
            else:
                print("Колонка 'color' уже существует")
        except Exception as e:
            await self.create_table()
            print(f"Произошла ошибка в базе данных ({e})")
        finally:
            await close(conn)

    async def change_columns(self):
        conn, cursor = await connect()
        try:
            await cursor.execute("PRAGMA table_info(users)")
            columns = await cursor.fetchall()
            column_names = [column[1] for column in columns]
            old_names = ['quirk', 'mythical_soul', 'favor', 'stars']
            new_names = ['nen_level', 'lvl_crsdenergy', 'fight_art', 'organization']
            if 'mythical_soul' in column_names:
                for i in range(len(new_names)):
                    await cursor.execute(f'ALTER TABLE users RENAME COLUMN {old_names[i]} TO {new_names[i]}')
                for i in range(len(new_names)):
                    await cursor.execute(f"UPDATE users SET {new_names[i]} = '{default}'")
                print('da')
            else:
                print('Колонки уже переименованы')
        except Exception as e:
            await self.create_table()
            print(f"Произошла ошибка в базе данных ({e})")
        finally:
            await close(conn)

    async def add_extension_color(self):
        conn, cursor = await connect()
        try:
            await cursor.execute("PRAGMA table_info(users)")
            columns = await cursor.fetchall()
            column_names = [column[1] for column in columns]
            if 'extension' not in column_names:
                await cursor.execute("ALTER TABLE users ADD COLUMN extension TEXT DEFAULT 'png'")
                print("Колонка 'extension' добавлена")
            else:
                print("Колонка 'extension' уже существует")
        except Exception as e:
            await self.create_table()
            print(f"Произошла ошибка в базе данных ({e})")
        finally:
            await close(conn)

    async def change_columns2_plus_add(self):
        conn, cursor = await connect()
        try:
            await cursor.execute("PRAGMA table_info(users)")
            columns = await cursor.fetchall()
            column_names = [column[1] for column in columns]
            old_names = ['demon_contract', 'lvl_crsdenergy']
            new_names = ['soul_core', 'apostolate']
            if 'demon_contract' in column_names:
                for i in range(len(new_names)):
                    await cursor.execute(f'ALTER TABLE users RENAME COLUMN {old_names[i]} TO {new_names[i]}')
                    await cursor.execute(f"UPDATE users SET {new_names[i]} = '{default}'")
                print('Колонки (2) переименовались')
                await cursor.execute(f"ALTER TABLE users ADD COLUMN soul_frag TEXT DEFAULT '{default}'")
                await cursor.execute(f"ALTER TABLE users ADD COLUMN charek TEXT DEFAULT '{default}'")
            else:
                print('Колонки (2) уже переименованы')
        except Exception as e:
            await self.create_table()
            print(f"Произошла ошибка в базе данных ({e})")
        finally:
            await close(conn)
