#include <iostream>
using namespace std;

int findKey(char *a, int n, char key)
{
    if (a == NULL || n <= 0)
    {
        return -1;
    }
    int i = 0;
    while (i < n)
    {
        if (a[i] == key)
        {
            return i;
        }
        ++i;
    }
    return -1;
}

int main()
{
    char a[4] = {4, 5, 9, 6};
    int index = findKey(a, sizeof(a) / sizeof(a[0]), 9);
    // cout << "index:" << index;
    // std::cout << index << std::endl;
    printf("index %d\n", index);
}