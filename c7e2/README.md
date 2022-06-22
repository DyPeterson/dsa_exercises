# Challenge questions
For this challenge, we will revisit our Lego data. We will be performing similar challenges to those we learned to do in Chapter 2 but using Spark instead of SQL directly.

## Get data
Use the supplied `data/get_data.sh` script to pull all lego CSV files. 

## Aggregate and grouping data:
Use Spark in a Python script or Jupyter notebook to answer the following questions. They should combine grouping, filtering and aggregation we learned in the lesson.

1. Find the total number, average number, min and max number of `parts`,  in all `sets`.
1. Find the total number, average number, min and max number of `parts`,  for each `theme_id` in `sets`.
1. Find all `theme_id`s that have more than 200 parts on average.
1. Find how many total parts each theme had every year.
1. Find the set with the most number of parts each year.
1. How many sets do we have with more than one version in `set_inventories`?

## UDF
To practice Pandas UDFs, create the following functions in a Python script or Jupyter notebook:
1. A `pandas_udf` that divides the input Pandas Series by 12 to convert a number into dozens.
    1. Apply this to the quantity columns of each inventory CSV.
1. A `pandas_udf` that converts strings to upper case.
    1. Convert each color name to upper case.
    1. Convert each set name to upper case.
1. A `pandas_udf` that strips all whitespace from a string.
    1. Strip whitespace from theme names.
    1. Strip whitespace from color names.