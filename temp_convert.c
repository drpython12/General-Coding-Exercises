#include <stdio.h>

int main(void)
{
    float start_temp, end_temp;
    int step_size;
    do
    {
        printf("Enter lower limit >= 10: ");
        scanf("%f", &start_temp);
    } while (start_temp < 10);

    do
    {
        do
        {
            printf("Enter higher limit <= 60: ");
            scanf("%f", &end_temp);
        } while (end_temp > 60);
    } while (start_temp >= end_temp);

    do
    {
        printf("Enter step size 0 < size <= 10: ");
        scanf("%i", &step_size);
    } while (step_size > 10);
    
    printf("\nCelcius\t\tFahrenheit\n\n");
    while (start_temp < end_temp)
    {
        float fahr = (start_temp * 1.8) + 32;
        printf("%f\t%f\n", start_temp, fahr);
        start_temp += step_size;
    }
}