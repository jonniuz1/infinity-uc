PRICE_UC = 5
# ------------ Configs ------------
ADMINS = [6170357621]
# BOT_TOKEN="6132848983:AAGh-2YcxbUQM__fl8pSfpUwNdSGa3F223o"
BOT_LINK = "https://t.me/nimadurbbot"
BOT_TOKEN = "5929525767:AAEJ8xL4UKm1PnnBONf6A7d7Qe6-QJEvq_8"
BOT_NAME = 'Infinity'
LINK_TO_CHANNEL = 'https://t.me/infinityuc'

REF_LINK = f"""{BOT_LINK}?start={{}}"""

TEXT_NOTIFY_ADMINS = f'{BOT_NAME} ishga tushdi!'

# ------------ Texts ------------
WELCOME_TEXT = f'Assalomu alaykum, {{}}. \n<a href="{LINK_TO_CHANNEL}">{BOT_NAME}</a> botiga xush kelibsiz!'

# ------------ Menu ------------
MENU_REF_BUTTON = '💵 UC ishlash'
MENU_CABINET_BUTTON = '📱 Kabinet'
MENU_ADDRESS_BUTTON = '📨 Murojaat'
MENU_INSTRUCT_BUTTON = "📚 Qo'llanma"

MENU_REF_TEXT = f"""
🔗 Sizning taklif havolangiz:

{REF_LINK}

Yuqoridagi taklif havolangizni do'stlaringizga tarqating va har bir to'liq ro'yxatdan o'tgan taklifingiz uchun {PRICE_UC} UC hisobingizga qo'shiladi.
"""

MENU_CABINET_TEXT = f"""
🔑 Sizning ID raqamingiz: <code>{{}}</code>

💵 Asosiy balansingiz: {{}} UC
👤 Takliflaringiz soni: {{}} ta

💳 Yechib olgan UClaringiz: {{}} UC
"""

MENU_INSTRUCT_TEXT = f"""
<b>🤖Botdan foydalanish qo'llanmasi📄</b>\n
Botdan UC ishlash uchun « 💵 UC ishlash» bo'limiga kirasiz va bot bergan havolani
do'stlaringizga tarqatasiz! Do'stingiz botga /start bosadi va bot bergan kanallarga
obuna bo'ladi va «🔄Tekshirish» tugmasi bosiladi! Ro'yhatdan o'tish bo'limi chiqadi: 
«📲Telefon raqamingizni yuboring» tugmasi bosiladi va sizga {PRICE_UC} UC bot hisobingizga taqdim etiladi!
"""

MENU_WITHDRAW_TEXT = "👇 Quyidagilardan birini tanlang:"

# ------------ Texts ------------
LINK_USER = 'tg://user?id='
INVITES_INFO = '<b>ТОП ПРИГЛАШЕНИЙ</b>'
INPUT_TO_SHOW = 'admin'

# ------------ Callbacks ------------
CALLBACK_CABINET = '💳 UC yechish'
CALLBACK_WITHDRAW = 'withdraw'
CALLBACK_CHANNEL_ARROVED = 'yes'
CALLBACK_CHANNEL_DISAPPROVED = 'no'
