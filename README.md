# Diet-calculator

This program allows you to visualize the nutrient content of foods, including proteins, fats, carbohydrates, as well as vitamins, minerals and amino acids. It also enables you to compare nutrients with the reference nutrient intakes (RNI) and calculate the cost of foods. Additionally, the program can track the cholesterol, trans fats, fiber and starch content of foods.

**Warning.** The nutrient content for some food items may be inaccurate and averaged.

![image](https://github.com/shi-i-chan/diet-calculator/blob/main/screens/full.png)

The first graph displays the ratio of nutrients to your daily intake. For visual convenience, each food is highlighted in a different color in the column. By clicking on the name of a food in the legend, you can disable its display.

![image](https://github.com/shi-i-chan/diet-calculator/blob/main/screens/chart_1.png)

Two bottom graphs show the cost per day and per month of the foods that you have selected.
![image](https://github.com/shi-i-chan/diet-calculator/blob/main/screens/chart_2.png)


This visualization makes it easy to assess the value and health utility of different foods. For example, dark chocolate is a source of iron, copper and manganese. Chicken meat is high in protein and B vitamins, but it also contains a significant amount of cholesterol. You can compare foods with each other, such as finding out that inexpensive barley grits is healthier than rice or oatmeal.

Using this program, you can easily track which nutrient you are deficient in. For example, vitamin D, E and K deficiencies are the most common. Vitamin E is found in almonds and sunflower seeds. Broccoli and green leafy vegetables are high in vitamin K, and oily fish is a source of vitamin D.

<details>
<summary>
Foods content parsing
</summary>
  
1. Remove files `norm_data.xlsx` and `products_data.xlsx` from folder `diet-calculator/data_parser/data/`.

2. Fill foods dictionary in file `diet-calculator/data_parser/parser_config.py`
  
<ul>

- Food id is taken from the site https://fitaudit.ru/food. For example, for an orange it would be `114159` https://fitaudit.ru/food/114159

```python
  products_dict = {
    'Food title': food id,
    'Апельсины': 114159,
    ...
}
```
</ul>
  
3. Fill daily intake dictionary in file `diet-calculator/data_parser/parser_config.py`
<ul>

- thousands are written with a space.

- Possible units of measurement: г, мг, мкг, or just a number (for water, kcal and ash).

```python
  products_dict = {
    'Белки': '75 г',
    'Марганец': '2,3 мг',
    'Бета-каротин': '5 000 мкг',
    ...
}
```
</ul>

4. Run file `diet-calculator/data_parser/make_norm_df.py` to prepare daily intake data. 
  
5. Run file `diet-calculator/data_parser/parser.py` to parse and prepare foods content data.
<ul>

- Files `norm_data.xlsx` and `products_data.xlsx` will appear in the folder `diet-calculator/data_parser/data/`.

- File `norm_data.xlsx` contains the daily intake in grams.
  
- File `products_data.xlsx` contains  the mass of nutrients in grams per 100 grams of food.
</ul>
</details>

<details>
<summary>
Using your own foods content data
</summary>

1. Follow 1 - 3 Foods content parsing instructions.
  
2. Save `products_data.xlsx` file with foods content in the folder `diet-calculator/data_parser/data/`.
<ul>
  
- The table columns are the food names, the indices are the nutrients. 
  
- **The values are the nutrient mass in grams per 100 grams of food**
  
- Files `norm_data.xlsx` and `products_data.xlsx` must be in the folder `diet-calculator/data_parser/data/`.
</ul>
</details>

<details open>
<summary>
Visualization
</summary>

<ul>
Before dashboard launching you can specify some default values in file `diet-calculator\default_data.py`.
</ul>

1. In dictionary default_diet you can set a default list of foods with their weights in grams.
<ul>

```python
  default_diet = {
    'Название продукта': масса в граммах,
}
```
</ul>

2. In dictionary default_weights you can set default masses of products in grams. They will be automatically displayed after adding food to dashboard table.
<ul>

```python
  default_weights = {
    'Название продукта': масса в граммах,
}
```
</ul>

3. In dictionary default_prices you can set default prices kilogram of the specific food. They will be automatically displayed after adding food to dashboard table.
<ul>

```python
  default_prices = {
    'Название продукта': цена килограмма продукта,
}
```
- **In all dictionaries, food names must match their names in the table `diet-calculator/data_parser/data/products_data.xlsx`**
</ul>

Or you can immediately run the file `diet-calculator/board.py/`. When launched, a dashboard should open in the browser with a table of products and graphs of nutrients and the cost of their purchase per day and per month.

If the `default_diet` dictionary is given, the calculations for the diet will be shown.
  
If the `default_diet` dictionary is not set, you need to select foods from drop-down list and fill their mass and price in the table. 
![image](https://github.com/shi-i-chan/diet-calculator/blob/main/screens/table.png)

</details>
