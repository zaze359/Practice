#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

void coutStr(const std::string& path)
{
    const char* a = path.c_str();
    cout << a << endl;
}

int main()
{
    std::string s = "hello";
    coutStr(s);

    int a = 1;
    int b = 2;
    int c = a = b;
    cout << a << b << c << endl;
}


