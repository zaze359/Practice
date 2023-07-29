#include <iostream>

using namespace std;

/**
 * @brief
 *
 * @param path 传递的是引用，函数对形参修改后会影响实参
 */
void modifyByReference(int &num)
{
    num = 3;
}

void constReference(const int &num)
{
    // num = 3; // const 无法修改
}

void modifyByRightReference(int &&num)
{
    num = 10;
}

// void mm(size_t a) {
// }

// void aa(const char *driver) {
//     mm(std::move(driver));
// }

int main()
{
    // ----------------------------------------
    // a是左值，a必须赋值
    // 1是右值。
    int a = 1;
    // 左值：b
    // 右值：a + 1 临时生成的对象
    int b = a + 1;

    cout << a << ", " << b << endl; // 输出1, 2
    cout << "----------------------------------------" << endl;
    cout << "----------------------------------------" << endl;

    // 定义左值引用：lr，相当于是a别名。
    int &lr = a;
    cout << &a << ", " << &lr << endl; // 输出相同地址，例如：0x61fde0, 0x61fde0
    cout << a << ", " << lr << endl;   // 输出1，1
    // 这里左值引用是拷贝赋值的。
    int lrc = lr;
    lrc = 2;
    cout << a << ", " << lr << ", " << lrc << endl; // 输出1, 1, 2

    // 无法直接赋值右值
    // int &r = 1。// 编译报错
    // const 修饰左值引用，支持直接赋值右值
    const int &clr = 5;
    cout << &clr << " -> " << clr << endl;
    // 传递左值引用，内部修改会影响外部
    modifyByReference(lr);
    // modifyByReference(3); // 编译报错，无法传递右值
    cout << a << ", " << lr << endl; // 输出3，3
    // const int &num, const修饰可以传递右值但是无法修改。
    constReference(3);
    cout << "----------------------------------------" << endl;
    cout << "----------------------------------------" << endl;

    // 定义右值引用，能帮助我们能够快速的构建一个引用类型。
    int &&rr = 9;
    // int &&rr = a; // 编译报错，右值引用只能指向右值
    cout << &rr << " -> " << rr << endl;
    //
    // 可以通过 std::move() 将左值转为右值引用，从而实现了右值引用指向左值
    int &&rra = std::move(a);
    // int &&rr2 = std::move(lr); // 和上面是等同的
    cout << &rra << " -> " << rra << ", " << a << endl; // 0x61fde8 -> 3, 3
    // 直接修改右值引用，a也被修改了
    rra = 4;
    cout << rra << ", " << a << endl; // 4, 4
    // 将a转为右值引用，并作为参数传递
    modifyByRightReference(std::move(a));
    // a的值被改变了
    cout << a << ", " << rra << endl; // 10, 10

    // 可以将 rra 赋值给左值引用，所以 rra 本身是一个左值。
    // 声明出来的右值引用是一个左值。
    int &rrl = rra;
    // int rrl = std::move(a); // 编译报错，作为返回值的右值引用是右值
    cout << rrl << ", " << rra << endl; // 10, 10

    cout << "----------------------------------------" << endl;
    cout << "----------------------------------------" << endl;

    std::string s = "aaaa";
    // 这里会将原先 s 中的值直接转移到 rrs中
    std::string rrs = std::move(s);
    cout << s << ", " << rrs << endl; // , aaaa

    s = "aaaa";
    // 左值转左值引用
    std::string &&rrs2 = std::move(s);
    // 右值转右值引用
    std::string &&rrs3 = std::move("ssss");
    cout << s << ", " << rrs2 << ", " << rrs3 << endl; // aaaa, aaaa, ssss

    s = "aaaa";
    // 左值 s，右值 "aaa"
    // 左值s转为 左值引用
    std::string &slr = std::forward<std::string &>(s);
    // 左值s转为了 右值引用
    std::string &&srr = std::forward<std::string>(s);
    // std::string &srr = std::forward<std::string>(s);// 编译报错
    cout << slr << ", " << srr << endl; // aaaa, aaaa

    // 这里需要注意，这里直接将 s中的值转给了 srr2，并且s被置为空
    std::string srr2 = std::forward<std::string>(s);
    cout << slr << ", " << srr2 << endl; // , aaaa
}
