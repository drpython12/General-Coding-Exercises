#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
    FILE *fp;
    fp = fopen(argv[2], "r");
    int lines = 0;
    char c;
    if (argc == 3)
    {
        // char* file = argv[3]
        for (c = getc(fp); c != EOF; c = getc(fp))
        {
            if (c == '\n')
            {
                lines++;
            }
        }
        fclose(fp);
        printf("There are %i lines in file %s", (lines + 1), argv[2]);
    }

    else if (fp == NULL)
    {
        printf("File does not exist!");
    }

    else
    {
        printf("Run program in the format ./line_count count [filename]");
    } 
}