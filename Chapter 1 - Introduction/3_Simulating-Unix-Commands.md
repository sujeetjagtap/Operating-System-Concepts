# Operating Systems Lab -- Experiment 3

## C Programs to Simulate UNIX Commands

### Aim

To write C programs to simulate UNIX commands such as `cp`, `ls`, and
`grep`.

------------------------------------------------------------------------

# 1. Program for Simulation of `cp` UNIX Command

### Algorithm

1.  Start the program.
2.  Declare the variables `ch`, `*fp`, and `sc = 0`.
3.  Open the file in read mode.
4.  Get the character.
5.  If `ch == ' '`, increment the value of `sc` by one.
6.  Print the number of spaces.
7.  Close the file.

### Program

``` c
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>

int main(int argc, char *argv[])
{
    FILE *fp;
    char ch;
    int sc = 0;

    fp = fopen(argv[1], "r");

    if (fp == NULL)
    {
        printf("unable to open a file", argv[1]);
    }
    else
    {
        while (!feof(fp))
        {
            ch = fgetc(fp);

            if (ch == ' ')
                sc++;
        }

        printf("no of spaces %d", sc);
        printf("\n");

        fclose(fp);
    }
}
```

### Output

------------------------------------------------------------------------

# 2. Program for Simulation of `ls` UNIX Command

### Algorithm

1.  Start the program.
2.  Open the directory with directory object `dp`.
3.  Read the directory contents and print them.
4.  Close the directory.

### Program

``` c
#include <stdio.h>
#include <dirent.h>

int main(int argc, char **argv)
{
    DIR *dp;
    struct dirent *link;

    dp = opendir(argv[1]);

    printf("\n contents of the directory %s are \n", argv[1]);

    while ((link = readdir(dp)) != 0)
    {
        printf("%s", link->d_name);
    }

    closedir(dp);
}
```

### Output

------------------------------------------------------------------------

# 3. Program for Simulation of `grep` UNIX Command

### Algorithm

1.  Start the program.
2.  Declare the variables `fline[max]`, `count = 0`, `occurrences = 0`,
    and pointers `*fp` and `*newline`.
3.  Open the file in read mode.
4.  In a `while` loop, check `fgets(fline, max, fp) != NULL`.
5.  Increment the `count` value.
6.  Check `newline = strchr(fline, '\n')`.
7.  Print the `count`, `fline` value, and increment the occurrence
    value.
8.  Stop the program.

### Program

``` c
#include <stdio.h>
#include <string.h>

#define max 1024

void usage()
{
    printf("usage: ./a.out filename word \n");
}

main(int argc, char *argv[])
{
    FILE *fp;
    char fline[max];
    char *newline;
    int count = 0;
    int occurrences = 0;

    if (argc != 3)
    {
        usage();
        exit(1);
    }

    if (!(fp = fopen(argv[1], "r")))
    {
        printf("grep: could not open file : %s \n", argv[1]);
        exit(1);
    }

    while (fgets(fline, max, fp) != NULL)
    {
        count++;

        if (newline = strchr(fline, '\n'))
            *newline = '\0';

        if (strstr(fline, argv[2]) != NULL)
        {
            printf("%s: %d %s \n", argv[1], count, fline);
            occurrences++;
        }
    }
}
```

### Output

------------------------------------------------------------------------

## Result

The C programs for simulating the specified UNIX commands were executed
and the corresponding output was observed.
