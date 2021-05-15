# Copyright 2021 d4n13l3k00.
# SPDX-License-Identifier: 	AGPL-3.0-or-later

###############################
### / Настройки  загрузок / ###
#   Изменять не обязательно   #
###############################
pic_quality         =     80  # ? Качество катринки в % (для jpeg)
pic_max_size        =    256  # ? Максимальная ширина/высота картинки в px
pic_format          = "jpeg"  # ? Большинство тапиков едят только jpeg и gif
pic_avatar_max_size =    256  # ? Максимальная ширина/высота аватарки в px

###############################
### / Настройки сообщений / ###
#   Изменять не обязательно   #
###############################
msg_regex_tme     = True                                                    # ? Замена t.me/*, t.me/*/id на /chat/*
msg_replace_regex = r"(https?://)?t\.me/(?P<chat>[A-Za-z0-9-_]{3,20})/?\d*" # ? Регулярное выражение для поиска ссылок
msg_regex_to      = r"/chat/\g<chat>"                                       # ? Замена на локал. ссылки

###############################
### / Настройки  Telethon / ###
#   Изменять не обязательно   #
###############################
api_id   = 6                                  # ! API_ID
api_hash = "eb06d4abfb49dc3eeb1aeb98ae0f581e" # ! API_HASH