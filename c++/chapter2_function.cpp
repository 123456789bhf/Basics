#include <iostream>

using namespace std;

// 1. 函数的定义
// 语法
// 返回值类型 函数名 （参数列表，用逗号分隔） {函数体语句 return 表达式}
int add (int num1,int num2) {
    int sum=num1+num2;
    return sum;
}

// 2. 函数的调用
// 语法
// 函数名（参数列表）
// int main() {
//     int a=10;
//     int b=20;
//     int sum=add(a,b);
//     //a,b成为实际参数，简称实参
//     //add函数中num1,num2成为形式参数，简称形参
//     cout << "a+b=" << sum << endl;
//     system("pause");
//     return 0;
// }

// 3. 参数中的值传递
// 如果函数不需要返回值，声明的时候可以写void
// void swap(int num1,int num2) {
//     cout << "交换前" << endl;
//     cout << "num1=" << num1 << endl;
//     cout << "num2=" << num2 << endl;
//     int temp;
//     temp=num1;
//     num1=num2;
//     num2=temp;
//     cout << "交换后" << endl;
//     cout << "num1=" << num1 << endl;
//     cout << "num2=" << num2 << endl;
// }

// int main() {
//     // 当进行值传递的时候，，函数的形参发生改变并不会影响实参
//     //原因：形参和实参占用不同的内存空间，调用函数的时候只是数值的获取，内存空间保持不变
//     //实参的内存保持不变，所以其存储的数值保持不变，形参的内存空间发生改变

//     int a=10;
//     int b=20;
//     swap(a,b);
//     cout << "a=" << a << endl;
//     cout << "b=" << b << endl;
//     system("pause");
//     return 0;
// }

// 4. 函数的常见形式
// 4.1 无参无返回值
// void show1() {
//     cout << "无参无返回值" << endl;
// }

// // 4.2 有参无返回值
// void show2(int i) {
//     cout << "有参无返回值" << i << endl;
// }

// // 4.3 无参有返回值
// int show3() {
//     cout << "无参有返回值" << endl;
//     return 100;
// }

// // 4.4 有参有返回值
// int shows(int a) {
//     cout << "有参有返回值" << a << endl;
//     return 100;
// }

// int main() {
//     show1();
//     int  a=10;
//     show2(a);
    
//     int num1=show3();
//     cout << "num1=" << num1 << endl;

//     int num2=shows(20);
//     cout << "num2=" << num2 << endl;
//     system("pause");
//     return 0;
// }


// 5. 函数的声明
// 作用：告诉编译器函数的名称以及如何调用函数，函数的实际主题可以单独定义
// 函数的声明可以多次，但是函数的定义只能有一次


// 提前告诉编译器函数的存在，可以利用函数的声明(函数在主函数的后面)
// int max(int a,int b); // 函数的声明

// int main() {
//     //比较两个数的大小，返回较大的数
//     int a=10;
//     int b=20;
//     int c=max(a,b);
//     cout << "c=" << c << endl;
//     system("pause");
//     return 0;

// }

// int max(int a,int b) {
//     return a>b? a:b;
// }

// 6. 函数的分文件编写
// 步骤
// 1. 创建后缀名为.h的文件
// 2. 创建后缀名为.cpp的源文件
// 3. 在头文件中写函数声明
// 4. 在源文件中写函数的定义
// 实现两个数字进行交换的函数

#include "swap.h"

// void swap(int a,int b) {
//     int temp=a;
//     a=b;
//     b=temp;
//     cout << "a=" << a << endl;
//     cout << "b=" << b << endl;
// }

int main() {
    int a=10;
    int b=20;
    swap(a,b);
    system("pause");
    return 0;
}