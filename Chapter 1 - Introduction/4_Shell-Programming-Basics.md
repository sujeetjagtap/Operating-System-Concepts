# Operating Systems Lab -- Experiment 4

## Simple Shell Programs

### Aim

To write simple shell programs using conditional, branching, and looping
statements.

------------------------------------------------------------------------

# 1. Check Whether a Given Number is Even or Odd

### Algorithm

1.  Start the program.
2.  Read the value of `n`.
3.  Calculate `r = expr $n % 2`.
4.  If the value of `r` equals `0`, print that the number is even.
5.  If the value of `r` is not equal to `0`, print that the number is
    odd.

### Program

``` sh
echo "Enter the Number"
read n
r=`expr $n % 2`

if [ $r -eq 0 ]
then
    echo "$n is Even number"
else
    echo "$n is Odd number"
fi
```

### Output

------------------------------------------------------------------------

# 2. Check Whether a Given Year is a Leap Year or Not

### Algorithm

1.  Start the program.
2.  Read the value of the year.
3.  Calculate `b = expr $y % 4`.
4.  If the value of `b` equals `0`, print that the year is a leap year.
5.  If the value of `b` is not equal to `0`, print that the year is not
    a leap year.

### Program

``` sh
echo "Enter the year"
read y
b=`expr $y % 4`

if [ $b -eq 0 ]
then
    echo "$y is a leap year"
else
    echo "$y is not a leap year"
fi
```

### Output

------------------------------------------------------------------------

# 3. Find the Factorial of a Number

### Algorithm

1.  Start the program.
2.  Read the value of `n`.
3.  Calculate `i = expr $n - 1`.
4.  If the value of `i` is greater than `1`, calculate
    `n = expr $n \* $i` and `i = expr $i - 1`.
5.  Print the factorial of the given number.

### Program

``` sh
echo "Enter a Number"
read n

i=`expr $n - 1`
p=1

while [ $i -ge 1 ]
do
    n=`expr $n \* $i`
    i=`expr $i - 1`
done

echo "The Factorial of the given Number is $n"
```

### Output

------------------------------------------------------------------------

# 4. Swap Two Integers

### Algorithm

1.  Start the program.
2.  Read the values of `a` and `b`.
3.  Swap the two values using a temporary variable `temp`.
4.  Print the values of `a` and `b`.

### Program

``` sh
echo "Enter Two Numbers"
read a b

temp=$a
a=$b
b=$temp

echo "after swapping"
echo $a $b
```

### Output

------------------------------------------------------------------------

## Result

The shell programs using conditional, branching, and looping statements
were executed and the corresponding output was observed.
