#include <iostream>
#include "a.h"
#include <stdio.h>

using namespace std;

class B {
public:
    B(){};
    ~B(){};

    int num = 1;
};


int main()
{
    // a();

    B* b = new B();

    cout << "111---" << b->num << endl; 
    cout << "222---" << (*b).num << endl; 
    
    B bb;
    cout << "333---" << bb.num << endl; 

    return 0;
}

