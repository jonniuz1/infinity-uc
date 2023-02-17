# ------------ Configs ------------
ADMINS = [6170357621]
CHANNEL = [-1001551015352, -1001448625936]
# BOT_TOKEN="6132848983:AAGh-2YcxbUQM__fl8pSfpUwNdSGa3F223o"
BOT_LINK = "https://t.me/nimadurbbot"
BOT_TOKEN = "5929525767:AAEJ8xL4UKm1PnnBONf6A7d7Qe6-QJEvq_8"
BOT_NAME = 'Infinity UC'
LINK_TO_CHANNEL = 'https://t.me/infinityuc'

REF_LINK = f"""{BOT_LINK}?start={{}}"""

TEXT_NOTIFY_ADMINS = f'{BOT_NAME} ishga tushdi!'

# ------------ Texts ------------
WELCOME_TEXT = f'Assalomu alaykum, <code>{{}}</code>. \n<a href="{LINK_TO_CHANNEL}">{BOT_NAME}</a> botiga xush kelibsiz!'
SENDED_TEXT = f"{{}} kanallarga yuborildi!\n"
# ------------ Menu ------------
MENU_REF_BUTTON = '💵 UC ishlash'
MENU_CABINET_BUTTON = '📱 Kabinet'
MENU_STAT_BUTTON = '🔝 Statistika'
MENU_INSTRUCT_BUTTON = "📚 Qo'llanma"

MENU_30UC = "30 Uc"
MENU_60UC = "60 Uc"
MENU_90UC = "90 Uc"
MENU_120UC = "120 Uc"
MENU_180UC = "180 Uc"


MENU_STAT_TEXT = """Eng ko'p taklif qilganlar:\n"""


MENU_REF_TEXT = f"""
🔗 Sizning taklif havolangiz:

{REF_LINK}

Yuqoridagi taklif havolangizni do'stlaringizga tarqating va har bir to'liq ro'yxatdan o'tgan taklifingiz uchun {{}} UC hisobingizga qo'shiladi.\n
Eng kam yechib olish miqdori 30 UC! 
"""

MENU_CABINET_TEXT = f"""
🔑 Sizning ID raqamingiz: <code>{{}}</code>

💵 Asosiy balansingiz: {{}} UC
👤 Takliflaringiz soni: {{}} ta
💹 Eng kam yechib olish miqdori 30 UC

💳 Yechib olgan UClaringiz: {{}} UC
"""

MENU_INSTRUCT_TEXT = f"""
<b>🤖Botdan foydalanish qo'llanmasi📄</b>\n
Eng kam yechib olish miqdori <b>30</b> UC\n
Botdan UC ishlash uchun « 💵 UC ishlash» bo'limiga kirasiz va bot bergan havolani
do'stlaringizga tarqatasiz! Do'stingiz botga /start bosadi va bot bergan kanallarga
obuna bo'ladi va sizga {{}} UC bot hisobingizga taqdim etiladi!
"""

MENU_WITHDRAW_TEXT = "👇 Quyidagilardan birini tanlang:"

# ------------ Texts ------------
LINK_USER = 'tg://user?id='
INVITES_INFO = '<b>ТОП ПРИГЛАШЕНИЙ</b>'
INPUT_TO_SHOW = 'admin'

BEFORE_PAYMENT_TEXT_TO_ADMIN = f"<code>{{}}</code>\n<a href='tg://user?id={{}}'>{{}}</a> {{}} UC chiqarish uchun so'rov berdi!"

# ------------ Callbacks ------------
CALLBACK_CABINET = '💳 UC yechish'
CALLBACK_WITHDRAW = 'withdraw'
CALLBACK_CHANNEL_ARROVED = 'yes'
CALLBACK_CHANNEL_DISAPPROVED = 'no'
CALLBACK_CHECK_SUB = 'check-sub'
CALLBACK_TOP_REFERRALS = 'top-ref'
CALLBACK_TOP_WITHDRAWERS = 'top-with'
