#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

void aaa(const std::string& path)
{
    const char* a = path.c_str();
    cout << a << endl;
}

/**
 * @brief int& 表示传递的是引用， 函数对形参修改后会影响实参
 * 
 * @param path 
 */
void bbb(int& path)
{
    path = 3;
    cout << "bbb " << path << endl;
}

/**
 * @brief 指针类型，操作后也将会修改原有的值
 * 
 * @param path 
 */
void ccc(int* path)
{
    *path = 5;
    cout << "ccc "<< *path << endl;
}

int main()
{
    std::string s = "hello";
    aaa(s);
    int *a;
    int b = 2;
    a = &b;
    bbb(b);
    ccc(a);
    printf("a %d\n", *a);
    printf("b %d", b);
    // printf("b %s", KEYWORD);
}


