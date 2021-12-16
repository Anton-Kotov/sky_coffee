from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
PGUSER = env.str("PGUSER")
PGPASSWORD = env.str("PGPASSWORD")
DATABASE = env.str("DATABASE")
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста
PGPORT = env.str("PGPORT")

POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{IP}:{PGPORT}/{DATABASE}"

QIWI_TOKEN = env.str("qiwi")
WALLET_QIWI = env.str("wallet")
QIWI_PUBKEY = env.str("qiwi_p_pub")



