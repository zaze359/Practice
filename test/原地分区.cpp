#include <iostream>
#include <vector>

using namespace std;

int main()
{
    // int a[5] = {6, 11, 3, 9, 8};
    // int r = sizeof(a)/ sizeof(a[0]);
    std::vector<int> a = {6, 11, 3, 9, 8};
    int p = 0;
    int r = a.size() - 1;

    int pivot = a[r];
    int i = p;

    for (int j = 0; j < r; j++)
    {
        if (a[j] < pivot)
        {
            std::swap(a[i], a[j]);
            i++;
        }
    }

    std::swap(a[i], a[r]);

    for (auto k : a)
    {
        cout << k << endl;
    }
}