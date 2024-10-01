from aiogram.utils.keyboard import InlineKeyboardBuilder


builder = InlineKeyboardBuilder()
builder.adjust(8, 10)

for index in range(1, 11):
    builder.button(text=f"Set {index}", callback_data=f"set:{index}")