#include <iostream>

// 定义字符串
// 容易出现的错误的写法
// #define HELLO = "hello"
// #define HELLO "hello";
#define HELLO "hello"
// 定义符号
#define BEGIN {
#define END }

// 带参数的宏定义
// 注意宏名和括号间不要有空格例如：SUM (x, y) (x + y)
// 此写法将会被识别为简单的宏替换，替换为: (x, y) (x + y)
#define SUM(x, y) (x + y)
// # 表示转换为字符串。
#define TO_STRING(s) #s
// ##（记号连接运算符）：会将2个参数连接起来
#define CONCAT(x, y) x ## y

void a() BEGIN
    printf(" func a\n");
END

int main() {
    printf(HELLO);
    a();
    int x = 1;
    int y = 2;
 
    printf("sum %d\n", SUM(x, y)); // 输出 3
    printf("to string %s\n", TO_STRING(hello)); // 此处hello将被转为 "hello"输出。
    printf("concat %d", CONCAT(22, 33)); // 输出 2233
}

