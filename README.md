# Diet-calculator

Программа позволяет визуализировать содержание нутриентов в наборе продуктов и сравнить его с суточной нормой потребления, а также оценить дневную и месячную стоимость данного набора продуктов.

**Предупреждение.** Я не проверял достоверность собранных данных. В целом они кажутся правдоподобными и сходятся с некоторыми другими источниками, но не следует считать их истиной в последней инстанции.

![image](https://github.com/shi-i-chan/diet-calculator/blob/main/screens/full.png)

Первый график отражает, сколько процентов суточной нормы нутриентов будет получено, если употребить заданные объемы выбранных продуктов.
  
Разные продукты отображаются разными цветами.
  
Кликом на продукт в легенде можно отключить его отображение.
![image](https://github.com/shi-i-chan/diet-calculator/blob/main/screens/chart_1.png)

Два нижних графика отражают затраты на выбранные продукты в день и в месяц.
![image](https://github.com/shi-i-chan/diet-calculator/blob/main/screens/chart_2.png)


С помощью этой визуализации можно легко оценить полезность каждого продукта. Например, горький шоколад является отличным источником железа, меди и марганца. Куринная грудка содержит много белка, аминокислот и некоторых витаминов группы B, но при этом содержит значительное количество холестерина. Куриные яйца также полезны, но содержат очень много холестерина.

Продукты можно сравнивать между собой, например рис и овсяная каша оказываются в несколько раз бесполезней, но при этом в несколько раз дороже ячневой каши. Да и сами по себе они вносят почти незаметный вклад в объем нутриентов.

Также можно увидеть каких нутриентов недостаточно в заданном рационе. Скорее всего будет наблюдаться недостаток "редких" витаминов, например видаминов группы D, витамина E и витамина K. Витамин D содержат жирные сорта рыбы, витамин E можно получить из семечек подсолнуха или миндаля, витамин K содержится в брокколи и зеленых листовых овощах.

Можно сделать следующие выводы:
Некоторые продукты ~~внезапно~~ не так полезны как кажется (например овсянка).
Даже при разнообразном питании можно недополучать некоторые "редкие" нутриенты, например витамин K.
Для удовлетворения потребностей организма можно употреблять относительно небольшое число продуктов, при этом их стоимость может быть весьма небольшой.

<details>
<summary>
Парсинг составов продуктов
</summary>
  
1. Удалить из папки `diet-calculator/data_parser/data/` файлы `norm_data.xlsx` и `products_data.xlsx`.

2. Заполнить словарь продуктов для парсинга, который находится в файле `diet-calculator/data_parser/parser_config.py`
  
<ul>

- Названия продуктов произвольные.

- id продукта берется с сайта https://fitaudit.ru/food. Например, для апельсина это будет `114159` https://fitaudit.ru/food/114159

```python
  products_dict = {
    'Название продукта': id продукта,
    'Апельсины': 114159,
    ...
}
```
</ul>
  
3. Заполнить словарь нормы потребления нутриентов в сутки в том же файле `diet-calculator/data_parser/parser_config.py`
<ul>

- Тысячи пишутся через пробел.

- Возможные единицы измерения: г, мг, мкг, либо просто число (для воды, кКал и золы).

```python
  products_dict = {
    'Белки': '75 г',
    'Марганец': '2,3 мг',
    'Бета-каротин': '5 000 мкг',
    ...
}
```
</ul>

4. Преобразовать данные суточной нормы потребления, запустив файл `diet-calculator/data_parser/make_norm_df.py`
  
5. Спарсить и преобразовать данные о содержании продуктов, запустив файл `diet-calculator/data_parser/parser.py`
<ul>

- В папке `diet-calculator/data_parser/data/` должны появиться файлы `norm_data.xlsx` и `products_data.xlsx`.

- Файл `norm_data.xlsx` содержит суточную норму нутриентов в граммах.
  
- Файл `products_data.xlsx`. содержит массу нутриентов в граммах на 100 грамм продукта.
</ul>
</details>

<details>
<summary>
Использование своих данных о составах продуктов
</summary>

1. Выполнить пункты 1 - 3 из инструкции Парсинга состава продуктов.
  
2. Сохранить в папке `diet-calculator/data_parser/data/` файл с составом продуктов с названием `products_data.xlsx`.
<ul>
  
- Названиями столбцов таблицы выступают названия продуктов, индексами таблицы выступают нутриенты.
  
- **Значениями выступает масса нутриента в граммах на 100 грамм продукта.**
  
- В папке `diet-calculator/data_parser/data/` должны находиться файлы `norm_data.xlsx` и `products_data.xlsx`.
</ul>
</details>

<details open>
<summary>
Визуализация
</summary>

<ul>
Перед запуском дашборда в файле `diet-calculator\default_data.py` можно указать некоторые дефолные значения.
</ul>

1. В словаре default_diet можно задать дефолтный список употребляемых в сутки продуктов с указанием их веса в граммах.
<ul>

```python
  default_diet = {
    'Название продукта': масса в граммах,
}
```
</ul>

2. В словаре default_weights можно задать дефолтные массы употребляемых в сутки продуктов в граммах. Они будут автоматически отображаться при добавлении продукта в таблицу дашборда.
<ul>

```python
  default_weights = {
    'Название продукта': масса в граммах,
}
```
</ul>

3. В словаре default_prices можно задать дефолтные цены килограмма продукта. Они будут автоматически отображаться при добавлении продукта в таблицу дашборда.
<ul>

```python
  default_prices = {
    'Название продукта': цена килограмма продукта,
}
```
- **Во всех словарях названия продуктов должны соответствовать их названиям в файле `diet-calculator/data_parser/data/products_data.xlsx`**
</ul>

Либо можно сразу запустить файл `diet-calculator/board.py/`. При запуске в браузере должен открыться дашборд с таблицей продуктов и графиками нутриентов и затрат на их покупку в сутки и в месяц.

Если задан словарь `default_diet`, то будут показаны расчеты для этого рациона.
  
Если словарь `default_diet` не задан, то необходимо выбрать продукты из выпадающего списка и заполнить в таблице массу их потребления в сутки и стоимость за килограмм. 
![image](https://github.com/shi-i-chan/diet-calculator/blob/main/screens/table.png)

</details>
