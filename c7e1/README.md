# Challenge questions
The purpose of this challenge is to practice the fundamental Spark skills we learned today. We will do more work with a simple RDD and then practice loading data and splitting it.

## Simple RDD
Create an RDD of the following tuples:

```python
apple,4
cherry,1
apple,1
apple,1
cherry,4
apple,1
cherry,3
apple,4
cherry,4
cherry,2
apple,5
apple,5
cherry,4
banana,2
apple,1
cherry,3
cherry,5
banana,2
cherry,1
cherry,2
apple,4
cherry,2
cherry,2
cherry,1
cherry,4
```

1. Find the total number of rows.
1. Find the sum of the numbers
1. Filter to only the apple rows.
1. Group by fruit key, sum numbers.
1. Then find the average of the second values.
1. Return the average sorted by fruit name.

## Lego colors read and split

Use the `get_data.sh` script in the `data/` directory to pull the `colors.csv` file for our lego dataset.
Using Spark do the following:
1. Read the CSV into an RDD.
1. Split and map that RDD into a Map.
