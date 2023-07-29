#include <iostream>
#include <stdio.h>
#include <string>
#include <memory>
using namespace std;

/**
 * @brief
 *
 * @param path 指针类型，操作后也将会修改原有的值
 */
void modifyByPoint(int *num)
{
    *num = 5;
}

int main()
{
    int a = 1;
    printf("defualt: %d\n", a);
    int *p = &a;
    printf("a addr: %d\n", &a);
    printf("p: %d\n", p);
    printf("p addr: %d\n", &p);

    modifyByPoint(p);

    printf("modifyByPoint %d\n", a);
    //
    printf("a %d\n", a);
    printf("p %d\n", *p);
    // unique_ptr ptr1(new int(10));
    // 
    printf("#######################################");
    char *s = (char*)"9357567890000000000000000000000000000000000000000000000000";
    //
    char *s1 = s;
    char *s2;
    s2 = s1;
    cout << "addr: "<< &s1 << endl;
    *s1++;
    printf("s1 %d\n", *s1);
    printf("s1 f.addr %d\n", s1);
    printf("s1 f.addr %d\n", &s1[0]);


    printf("s2 %s\n", s2);
    

    // unique_ptr ptr2(new int(10));

    // auto ptr2 = std::make_unique(10);

    // printf("ptr2 %s\n", ptr2);
    // printf("p2 %d\n", p2);
    // *p = 0;
    //  printf("p2 %d\n", *p2);
}
