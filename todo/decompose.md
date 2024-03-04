[отчёт о проделанной работе в google docs, что?](https://docs.google.com/document/d/1mnfcXeNzaw7T9nlMDzIzXlI4e8krCh4byP5Qw0SJ-Ck/edit#heading=h.2lp1ngdae5e6)
<details><summary>Что должно быть в документе</summary>
<ul>
	<li><a href = "https://am1bestofluck.pythonanywhere.com/">Ссылка на сайт</a></li>
	<li><a href = "https://github.com/am1bestofluck/gb_recipies/">Ссылка на исходный код</a></li>
</ul></details>

# Модели

### Модель Рецепт

<details> <summary>Поля</summary>
<div>Название</div>
<div>Описание</div>
<div>Шаги приготовления **один ко многим?**</div>
<div>время приготовления</div>
<div>картинка</div>
<div>автор</div>
<div>Ингридиенты~~ **вынос во внешний ключ</div> </details>

### Модель Ингридиент *

<details> <summary>Поля</summary>
<div>Название</div>
<div>Еденица измерения</div>
</details>

### Модель Категория рецептов *

<details> <summary>Поля</summary>
<div>Название</div>
<div>Дефолтное фото</div>
</details>

### Связующая таблица: *Рецепты* *Категории*

<details> <summary>Поля</summary>
<div>она же сама генерируется, нет? _many-to-many-field_</div>
</details>


# Шаблоны

* <details><summary> base_template</summary>

<div> пересмотреть семантику</div></details>

*  <details><summary> index</summary>

<div>5 рецептов; flex? preview по фотке; если не добавили - дефолтное фото категории; поле краткое описание? если там много - выводим часть текста кото...</div></details>

* <details><summary> один рецепт</summary>

<div> пару слов об авторе тоже</div></details>

* * <details><summary> регистрация, авторизация, выход</summary>

<div> регистрация, авторизация заслуживают отдельную страничку; а вот выход - будет как элемент шаблона header</div></details>
* * <details><summary> добавления рецепта</summary>

<div> плейсхолдеры </div></details>
* * <details><summary> редактирования рецепта</summary>

<div> значение по умолчанию - то что там было до этого </div></details>

# Формы
* <details><summary> например</summary>

<div> добавить рецепт</div>
<div>Зарегистрировать пользователя<div>
<div> Изменить рецепт <div> </details>

# views, urls
* <details><summary> политика </summary>
<div> все шаблоны- со своим view и маршрутом<div>
<div> Изменить рецепт <div> </details>

# деплой
* выложить
* убедиться что связь с бд работает