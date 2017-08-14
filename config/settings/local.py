from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='ah80q8ryxi(!^4ii@o%vexxbir6jy2qo1%+sgyb-ei&ji3bap%')
DEBUG = env.bool('DJANGO_DEBUG', default=True)