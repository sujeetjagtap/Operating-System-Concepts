# Operating Systems Lab -- Experiment 2

## System Calls of UNIX

### Aim

To write C programs using the following system calls of UNIX operating
system:

-   `fork`
-   `exec`
-   `getpid`
-   `exit`
-   `wait`
-   `close`
-   `stat`
-   `opendir`
-   `readdir`

------------------------------------------------------------------------

## 1. Program for System Calls of UNIX Operating System

### `opendir()`, `readdir()`, `closedir()`

### Algorithm

1.  Start the program.
2.  Create the directory structure.
3.  Declare the variable `buff` and pointer `dptr`.
4.  Get the directory name.
5.  Open the directory.
6.  Read the contents in the directory and print them.
7.  Close the directory.

### Program

``` c
#include <stdio.h>
#include <dirent.h>

struct dirent *dptr;

int main(int argc, char *argv[])
{
    char buff[100];
    DIR *dirp;

    printf("\n ENTER DIRECTORY NAME");
    scanf("%s", buff);

    if ((dirp = opendir(buff)) == NULL)
    {
        printf("The given directory does not exist");
        exit(1);
    }

    while ((dptr = readdir(dirp)))
    {
        printf("%s\n", dptr->d_name);
    }

    closedir(dirp);
}
```

### Output

------------------------------------------------------------------------

## 2. Program for System Calls of UNIX Operating System

### `fork()`, `getpid()`, `exit()`

### Algorithm

1.  Start the program.
2.  Declare the variables `pid`, `pid1`, and `pid2`.
3.  Call `fork()` system call to create a process.
4.  If `pid == -1`, exit.
5.  If `pid != -1`, get the process ID using `getpid()`.
6.  Print the process ID.
7.  Stop the program.

### Program

``` c
#include <stdio.h>
#include <unistd.h>

main()
{
    int pid, pid1, pid2;

    pid = fork();

    if (pid == -1)
    {
        printf("ERROR IN PROCESS CREATION \n");
        exit(1);
    }

    if (pid != 0)
    {
        pid1 = getpid();
        printf("\n The parent process ID is %d\n", pid1);
    }
    else
    {
        pid2 = getpid();
        printf("\n The child process ID is %d\n", pid2);
    }
}
```

### Output

------------------------------------------------------------------------

## Result

The programs using the specified UNIX system calls were executed and the
corresponding output was observed.
