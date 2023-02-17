from loader import dp
from .check_admin import IsAdmin
from .IsPrivate import IsPrivate
from .IsGroup import IsGroup

if __name__ == "filters":
    dp.filters_factory.bind(IsAdmin)
    dp.filters_factory.bind(IsPrivate)
    dp.filters_factory.bind(IsGroup)
    pass
