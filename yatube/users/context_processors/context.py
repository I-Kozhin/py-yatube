import datetime


#  параметр request нужно передавать, так как это обязательный параметр для всех функций шаблона (документация)
def year(request):
    """
    Добавляет переменную с текущим годом
    :return: текущий год
    """
    year = datetime.datetime.now().year
    return {"year": year}
