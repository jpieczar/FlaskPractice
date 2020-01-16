import sqlite3

conn = sqlite3.connect("dataBase.db") # Stores data here. Creates .db file if does not exist.

# A cursor helps us to execute SQL commands.
c = conn.cursor()

# The docstring (multiline comment) allows us to write on multiple lines.
# This is done as in the python documentation.
c.execute("""CREATE TABLE IF NOT EXISTS `users` (
            `id`                INT(11) PRIMARY KEY NOT NULL,
            `username`          TINYTEXT NOT NULL,
            `email`             TINYTEXT NOT NULL,
            `password`          TINYTEXT NOT NULL,
            `verified`          BOOL NOT NULL DEFAULT 0,
            `verificationKey`   TINYTEXT NOT NULL DEFAULT 0,
            `reported`          BOOL NOT NULL DEFAULT 1
            )""")

conn.commit()

c.execute("""CREATE TABLE IF NOT EXISTS `profile` (
            `userId`,
            `firstName`,
            `lastName`,
            `gender`,
            `age`,
            `preference`,
            `fame`,
            )""")

conn.commit()

c.execute("""CREATE TABLE IF NOT EXISTS `interests` (
            `id`,
            `interest`
            )""")

conn.commit()

c.execute("""CREATE TABLE IF NOT EXISTS `images` (
            `userId`,
            `imageName`
            )""")

conn.commit()

c.execute("""CREATE TABLE IF NOT EXISTS `matches` (
            `userA`,
            `userB`
            )""")

conn.commit()

c.execute("""CREATE TABLE IF NOT EXISTS `blocked` (
            `blockerId`,
            `blockedId`
            )""")

conn.commit()

c.execute("""CREATE TABLE IF NOT EXISTS `location` (
            `id`,
            `latitude`,
            `longitude`,
            `area`
            )""")

conn.commit()

c.execute("""CREATE TABLE IF NOT EXISTS `messages` (
            `id`,
            `senderId`,
            `receivedId`,
            `recieved`
            )""")

conn.commit()

conn.close()