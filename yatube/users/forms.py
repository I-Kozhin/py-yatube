from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

"""
    Функция get_user_model() обращается именно к той модели, 
    которая зарегистрирована в качестве основной модели пользователей в конфиге проекта.
    Если разработчик заменит эту модель на собственную, вносить изменения по всему проекту 
    ему не придётся, будет достаточно изменить лишь одно значение в конфиге. Но это в случае, 
    если он повсюду предусмотрительно применял get_user_model().
"""
User = get_user_model()


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        #  указываем модель, с которой связана создаваемая форма
        model = User
        #  указываем, какие поля должны быть видны в форме и в каком порядке
        fields = ("first_name", "last_name", "username", "email")
