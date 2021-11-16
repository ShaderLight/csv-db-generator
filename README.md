# csv generator  ![Licence](https://img.shields.io/github/license/ShaderLight/csv-db-generator) ![GitHub last commit](https://img.shields.io/github/last-commit/shaderlight/csv-db-generator)

 Small script for generating csv databases from other csv files or by selecting random integers or dates

---
## Usage

The most straightforward way would be to open database_gen.py and run generate_db function with approriate params

### generate_db parameters:
- **output_filename** - Specifies how the output file should be named
- **n** - Specifies how many rows need to be generated
- **args** - one or more objects created using classes defined in *input_classes.py*
---
### Input classes and their properties:
- **csv_field** - represents a field (or fields) from an external csv file (must be located in the main directory of this repo)
  - **names** - name(s) of the csv fields (in the input file) to include in generation of the output csv file
  - **input_filename** - name of the external csv file to import the fields from
  - **input_fieldnames** - (optional) name(s) to replace the original fieldnames in the **names** param when naming fields in the *output* csv file
- **date_field** - represents a field with values being random dates from a given range of dates (format is DD.MM.YYYY)
  - **name** - how the field will be named in the output csv file
  - **from_d, from_m, from_y** - day, month and year of the "older" date of the range
  - **to_d, to_m, to_y** - day month and year of the "younger" date of the range (these are all separate params)
- **randint_field** - represents a field with random integers (from the specified range) as values
  - **name** - name of the field in the output file
  - **a** - lower border of the range
  - **b** - upper border of the range
  - **unique** - (default=*False*) - specified whether the integers need to be unique; use with caution as generating more fields than possible integers in the given range while this param is set to *True* will make the program freeze
- **id_field** - represents a field with autoincrementing value
  - **name** - (default=*'id'*) how the field should be named 

---
## Examples

Generating 3 rows with id field and randint field named *"random_column"* and containing random integers from 1 to 10. The output file will be named *output.csv*.
```python
generate_db('output.csv', 3, id_field(), randint_field('random_column', 1, 10))

# Example output.csv

# id;random_column
# 1;7
# 2;4
# 3;9
```
---
Generating 4 rows with two fields:
- field containing random value from *"country"* column in *country_data.csv*
- random date between *01.01.2000* and *12.12.2000* (format DD.MM.YYYY) named *"c_date"*

We assume that a *"country_data.csv"* file exists, is located in the main dir, and contains a field named *"country"*  with names of some countries
```python
f1 = csv_field('country', 'country_data.csv')
f2 = date_field('c_date', 1, 1, 2000, 12, 12, 2000)
generate_db('output.csv', 4, f1, f2)

# Example output.csv

# country;c_date
# France;2000-05-08
# Norway;2000-07-24
# Canada;2000-10-05
# Italy;2000-02-06
```
---
## Additional information
By default the program 
**both reads the csv files and saves them using `;` delimiter**, meaning all input csv must use `;` delimiter. When working with other delimiters, either:
- use *find and replace* function of your text editor to replace all the delimiters to `;`
- or modify the code in **modules/csv_io.py**  (lines 6 and 15) to accept other delimiter

Also dates in the output file will be in **YYYY-MM-DD** format by default