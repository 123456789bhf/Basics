// C++核心编程：面向对象
// 章节5：类和对象
// 1. 内存分区模型
// c++程序在执行时，将内存大方向划分为4个区域（不同区域存放的数据，赋予不同的生命周期，给我们更大的灵活编程neg）
// 1. 代码区：存放函数体的二进制代码，由操作系统进行管理的

// 2. 全局区：存放全局变量和静态变量以及常量
// 3. 栈区：由变异器自动分配释放，存放函数的参数值、局部变量等
// 4. 堆区：由程序员分配和释放，若程序员不释放，系统会自动释放
//      在程序编译之后，生成了exe可执行程序，未执行该程序分为两个区域
//      1.1 代码区：
//          存放CPU执行的机器指令
//          代码区是共享的，共享的目的是对于频繁执行的程序，只需要在内存中有一份代码即可
//          代码区是只读的，防止程序修改代码区中的数据 
//      1.2 全局区
//          全局变量和静态变量存放在此
//          全局区还包含了常量提取、字符串常量、和其他常量
//          该区域的数据在程序结束后由操作系统释放
//      1.2 数据区：存放全局变量和静态变量以及常量，数据区分为两个区域：

// 不在全局区域中的变量：局部变量，局部常量（const修饰的全局常量和字符串常量）
// 全局区：全局变量，静态变量，常量
// 栈区：由编译器自动分配释放，存放函数的参数值、局部变量等
//    注意事项：不要返回局部变量的地址，栈区开辟的数据由编译器自动释放

// #include<istream>
// #include<iostream>
// using namespace std;

// // 栈区注意事项：不要返回局部变量的地址，栈区开辟的数据由编译器自动释放
// string fun(int b) { //形参数据也会存放在栈区
//     b=100;
//     int a=10; //局部便两个：存放在栈区，栈区的数据在函数执行完后自动释放了
//     return &a; // 返回局部变量的地址，栈区开辟的数据由编译器自动释放    
// }

// int main() {
//     int *p=fun(); // p指向了栈区的地址，栈区的数据在函数执行完后自动释放了
//     cout << "p=" << *p << endl; // 访问栈区的地址，栈区的数据在函数执行完后自动释放了
//     system("pause");
//     return 0;
// }

// 堆区：由程序员分配释放，若程序员不释放，系统会自动释放
//    在c++中主要利用new在堆区开辟内存，手动释放，释放利用操作符delete

// #include<iostream>
// using namespace std;
// int * func() {

//     //利用new关键字，可以将数据开辟到堆区
//     //指针本质也是局部变量，放在栈上
//     // inte
//     int *p=new int(10);
//     return p;

// }

// int main() {
//     int *p=func(); // p指向了堆区的地址，堆区的数据在函数执行完后不会自动释放
//     cout << "p=" << *p << endl; // 访问堆区的地址，堆区的数据在函数执行完后不会自动释放
//     cout << "p=" << *p << endl;
//     cout << "p=" << *p << endl;
//     cout << "p=" << *p << endl;
//     delete p; // 释放堆区的内存
//     system("pause");
//     return 0;
// }

// 释放堆区的内存：delete和delete[]
// #include<iostream>
// using namespace std;

// int * func() {
//     //在堆区创建整型数据
//     //new返回的是该数据类型的指针
//     int *p=new int(10);
//     return p;

// }
// void test01() {
//     int *p=func();
//     cout << "p=" << *p << endl; // 访问堆区的地址，堆区的数据在函数执行完后不会自动释放
//     cout << "p=" << *p << endl;
//     cout << "p=" << *p << endl;
//     //堆区的数据，由程序员管理开辟，程序员管理释放
//     //如果像释放堆区的数据，利用关键字delete
//     delete p;
//     cout << *p << endl; // 内存已经被释放，再次访问就是非法操作，会返错误的值
// }
// void test02 () {
//     int *arr=new int[10]; //带哦标有10个元素的数组
//     for (int i=0; i<10; i++) {
//         arr[i]=i+100; //给数组中的10个元素赋值，100~109
//     }
//     for (int i=0; i<10; i++) {
//         cout << arr[i] << endl; //打印数组中的10个元素
//     }
//     // 释放堆区的数组
//     delete[] arr; //释放数组同加上[]，表示释放数组
// }
// int main() {
//     test01(); //调用函数
//     test02(); //调用函数
//     system("pause");
//     return 0;
// }


// 2. 引用
//   作用：给变量起别名
//   语法：数据类型 &别名=原变量名;
//   别名和原名操作的是同一块内存
// #include<iostream>
// using namespace std;
// int main() {
//     int a=10;
//     int &b=a;
//     cout << "a=" << a << endl; // a=10
//     cout << "b=" << b << endl; // b=10
//     b=100;
//     cout << "a=" << a << endl; // a=100
//     cout << "b=" << b << endl; // b=100
//     system("pause");
//     return 0;

// }

// 2.2 引用注意事项
//    必须初始化
//    在初始化后，不可以改变
// #include<iostream>
// using namespace std;
// int main() {
//     int a=10;
//     int &b=a;// 初始化
//     // int &b; //会报错
//     int c=20;
//     b=c; //赋值操作，而不是更改引用 
//     cout << "a=" << a << endl; // a=10
//     cout << "b=" << b << endl; // b=20
//     cout << "c=" << c << endl; // c=20  


//     system("pause");
//     return 0;
// }

// 2.3 引用作为函数参数
// 作用：函数传参时，可以利用引用的技术让形参修饰实参，有点事可以简化指针修改实参
// #include<iostream>
// using namespace std;

// // 交换函数
// // 1. 值传递
// void swap01(int a, int b) {
//     int temp=1;
//     a=b;
//     b=temp;
// }
// // 2. 地址传递
// void swap02(int *a, int *b) {
//     int temp=*a;
//     *a=*b;
//     *b=temp;
// }

// // 3. 引用传递
// void swap03(int &a, int &b) {
//     int temp=a;
//     a=b;
//     b=temp;
// }

// int main() {
//     int a=10;
//     int b=20;
//     swap01(a,b); // 交换函数,值传递，形参不会修饰实参
//     cout << "a=" << a << endl; // a=10
//     cout << "b=" << b << endl; // b=10
//     swap02(&a,&b); //传递的内存地址，形参会修饰形参
//     cout << "a=" << a << endl; // a=20
//     cout << "b=" << b << endl; // b=10 
//     swap03(a,b);
//     cout << "a=" << a << endl; // a=20
//     cout << "b=" << b << endl; // b=10 

// }

// 2.4 引用作为函数的返回值

// #include<iostream>
// using namespace std;

// // // 引用作为函数的返回值
// // // 1.1 不要返回局部变量的引用
// // // int& test01() {
// // //     int a=10; // 局部变量存放在四区中的栈区，在函数执行后内存释放
// // //     return a;

// // // }

// int& test02() {
//     static int a=10;//静态变量，存放在全局区，全局区的内存在程序结束后由系统释放
//     return a;
// } //返回的是变量a的一个引用
// int main() {
//     // int &ref=test01(); //执行报错，不要返回局部变量的引用    
//     // cout << "ref=" << ref << endl;
//     // cout << "ref=" << ref << endl;
//     int &ref=test02();//ref是test02()函数返回值a的别名
//     cout << "ref=" << ref << endl;
//     cout << "ref=" << ref << endl;
//     test02()=1000; // 如果函数返回值是引用，这个函数调用可以作为左值
//     cout << "ref=" << ref << endl;
//     cout << "ref=" << ref << endl;
//     system("pause");
//     return 0;
// }


// 2.5引用的本质
//    是个指针常量，对于指针常量来说，指针的指向不可以修改(说明引用不可修改)_，但是指向的内容可以修改
// #include<iostream>
// using namespace std;
// int main() {
//     int a=10;
//     // 自动转换成int * const ref=&a;
//     int &b=a;
//     cout << "a=" << a << endl; // a=10
//     cout << "b=" << b << endl; // b=10
//     b=100; //内部发现ref是引用，自动转换为： *ref=20;
//     cout << "a=" << a << endl; // a=100
//     cout << "b=" << b << endl; // b=100
//     system("pause");
//     return 0;

// }

// 2.6常量引用
//    作用：主要用来修饰形参，防止误操作
//    在函数形参数列表中，可以加const修饰形参，防止形参改变实参
// #include<iostream>
// using namespace std;
// // 打印数据函数
// // 加上const之后再函数里面就不能修改输入值了
// void showvalue(const int &val) {
//     // val=1000; // 加上const之后这个代码会变错
//     cout << "value==" << val << endl;
// }
// int main() {
//     // 常量引用
//     // 使用场景：主要用来修饰形参，防止误操作

//     int a=10;
//     // int &ref=10; // 引用必须引一块合法的内存空间
//     // 假如const之后变为只读，不可以修改
//     // const int &ref=10;  // 加上const之后，编译器将代买需改为int temp=10; const int & ref=temp;
//     showvalue(a);
//     cout << "value==" << a << endl;
//     system("pause");
//     return 0;


// }

// 3. 函数提高
// 3，1 函数默认参数
// 再c++中，函数的形参列表中的形参是有默认值的
// 语法：返回值类型 函数名（参数=默认值） {}
// #include<iostream>
// using namespace std;
// int func(int a=9,int b=20, int c=30) {
//     return a+b+c;
// }
// // 注意事项给：
// //    1. 如果某个位置已经有了默认参数，那么从这个位置往后，从左到右都必须有默认值
// //    2. 如果函数声明有了默认参数，函数的实现就不能有默认参数，函数声明和实现只能有一个默认参数。
// int func2(int a=10,int b=20); //函数声明
// int func2(int a,int b) { //函数的实现
//     return a+b;
// }
// int main() {
//     cout << func() << endl;
//     system("pause");
//     return 0;
// }

// 3.2 函数展占位参数
//   函数的形参列表中可以有占位符，用来占位，调用函数时必须填补该位置
//   语法： 返回值类型 函数名（数据类型） {}
// #include<iostream>
// using namespace std;

// // 占位符
// // 目前阶段的占位参数，暂时还用不到，后面课程中会用得到


// void func(int a,int) {
//     cout << "this is func" << endl;
// }
// // 占位参数：还可以有默认参数
// void func(int a,int=10) {
//     cout << "this is func" << endl;
// }
// int main() {
//     func(10,10);
//     system("pause");
//     return 0; 
// }

// 3. 函数重载
// 3.1 函数重载的概述：函数名可以相同，提高复用性
//   函数重载满足条件:
//      1. 同一个作用域下
//      2. 函数名称相同
//      3. 函数参数类型不同，或个数不同或者顺序不同
//    注意：函数的返回值类型不可以作为函数重载的条件

// #include<iostream>
// using namespace std;
// void func() {
//     cout << "func的调用" << endl;
// }

// void func(int a) {
//     cout << "func(int a)的调用" << endl;
// }

// void func(double a) {
//     cout << "func的调用(double a）" << endl;
// }

// void func(int a,double b) {
//     cout << "func(int a,double b)的调用" << endl; 
// }

// void func(double b,int a) {
//     cout << "func(double b，int a)的调用" << endl; 
// }
// //会报错，因为和上面的函数返回值类型不同
// // int func(double b,int a) {
// //     cout << "func(double b，int a)的调用" << endl; 
// // }


// int  main() {
//     func();
//     func(10);
//     func(10.2);
//     func(1,20.1);
//     func(102.1,2);
//     system("pause");
//     return 0;

// }

//  3.3.2 函数重载注意事项
//     引用作为重载条件
//     函数重载遇到默认参数

// #include<iostream>
// using namespace std;
// // 可读可写
// void func3(int &a) {
//     cout << "func(int &a)的调用" << endl;
// }
// //可读不可写
// void func(const int &a) {
//     cout << "func(const int &a)的调用" << endl;
// }

// void func2(int a) {
//     cout << "func2(int a)的调用" << endl;
// }

// void func2(int a,int b=10) {
//     cout << "func2(int a,,int b)的调用" << endl;
// }
// int main() {
//     int a=10;
//     int b=20;
//     func(a); //调用第一个函数,调用可读可写状态的函数
    
//     func(10); // 调用第二个函数,因为func(10)在第一个函数中不合法,在第二个函数中是const int &a=10,是合法的
//     func2(10); // 既可以调用第一个函数也可以调用第二个函数,所以需要避免这种情况出现
//     func2(a,b);
//     system("pause");
//     return 0;

// }

// 4. 类和对象
//  面向对象的三大特征:封装\继承\多态
//   4.1 封装
//   4.1.1 封装的意义
//       将属性和行为作为一个整体,表现生活中的事物
//       将属性和行为加以权限控制
//       语法: class 类名{ 访问权限:属性/行为};

// #include<iostream>
// using namespace std;

// const double PI=3.14;

// class circle {
//     // 访问权限
//     // 公共权限
// public:
//     // 属性
//     int m_r;
//     // 行为
//     //  获取圆的周长
//     double calculateZC() {
//         return 2*PI*m_r;
//     }
// };

// int main() {
//     // 通过圆类创建一个具体的圆(对象)
//     // 实例化：通过一个类创建一个对象的过程
//     circle c1;
//     // 对对象进行赋值
//     c1.m_r=10;
//     cout << "圆的周长为" << c1.calculateZC() << endl;
//     system("pause");
//     return 0;
// }


// 谁急一个学生类，属性有姓名和学号，可以给姓名和学号进行赋值操作，可以显示学生的姓名和学号
// #include<iostream>
// using namespace std;
// #include<string>

// class student {
// public: // 公共权限
//     //类中的属性和行为我们统一称为成员
//     // 属性   成员属性  成员变量
//     string m_name; //姓名
//     int m_id;  //学号
//     //行为   成员函数  成员方法
//     // 显示姓名和学号
//     void showstudent() {
//         cout << "姓名" << m_name << "学号" << m_id << endl;
//     }
//     // 给姓名赋值
//     void setname(string name) {
//         m_name=name;
//     }
//     // 给学号赋值
//     void setid(int id) {
//         m_id=id;
//     }


// };


// int main() {
//     // 实例化：创建一个具体学生，实例化对象
//     student s1;
//     s1.m_name="张三";
//     s1.m_id=1;
//     s1.setname("李四");
//     s1.setid(2);
//     s1.showstudent();
//     system("pause");
//     return 0;
// }


// 封装意义2：
//    类在设计时，可以把属性和行为放在不同的权限下，加以控制
//    访问权限有三种
//    1. public   公共权限   成员在类内可以访问  类外也可以访问
//    2. protected 保护权限  成员在类内可以访问  类外不可以访问  儿子也可以访问父亲中的保护内容
//    3. private  私有权限   成员在类内可以访问 类外不可以访问   儿子不可以访问父亲中的私有内容
// #include<iostream>
// using namespace std;
// #include<string>

// class person {
//     public:
//     // 公共权限
//     string m_name; // 姓名
//     protected:
//     // 保护权限
//     string m_car; //汽车
//     private:
//     // 私有权限
//     int m_password; // y银行卡密码
//     public:
//     void func() {
//         m_name="张三";
//         m_car="拖拉机";
//         m_password=123456;
//     }
// };
// int main() {
//     // 实例化：创建一个具体学生，实例化对象
//     person p1;
//     p1.m_name="李四";
//     // p1.m_car="宝马"; // 保护权限的内容在类外访问不到
//     // p1.m_password=2971; //保护权限的内容在类外访问不到
//     p1.func(); 
//     system("pause");
//     return 0;
// }



// 4.1.2 struct和class的区别
//  区别在于默认的权限不同，struct默认权限是公共权限public。class默认权限是私有权限private


//  4.1.3成员属性设置为私有

//  优点：将所有成员属性设置为私有，可以自己控制读写权限。对于写权限，我们可以检测数据的有效性

// #include<iostream>
// using namespace std;
// #include<string>

// class person {
    
//     public:
//     // 设置姓名
//     void setname(string name) {
//         m_name=name;
//     }

//     // 获取姓名
//     string getname() {
//         return m_name;
//     }
//     int getage() {
//         return m_age;
//     }
//     void setage(int age) {
//         if (age<0 || age>150) {
//             cout << "年龄输入有误" << endl;
//             return;
//         }
//         m_age=age;
//     }
//     void setidol(string idol) {
//         m_idol=idol;
//     }
//     private:
//     // 通过构造函数控制属性的只读只写状态
//     string m_name; //可读可写
//     int m_age=18; //只读  也可以写（年龄必须在0-150岁之间）
//     string m_idol; // 只写
// };

// int main() {
//     person p;
//     p.setname("张三");
//     p.setidol("小明");//只写状态，外界访问不到
//     p.setage(190);
//     cout << "姓名" << p.getname() << endl;
//     cout << "年龄" << p.getage() << endl;
//     system("pause");
//     return 0;
// }

// #include<iostream>
// using namespace std;
// #include<string>
// class cube {
   
//     public:
//     void setlen(int l) {
//         m_len=l;
//     }
//     int getlen() {
//         return m_len;
//     }
//     void setwidth(int w) {
//         m_width=w;
        
//     }
//     int getwidth() {
//         return m_width;
//     }

//     void sethigh(int h) {
//         m_hight=h;
//     }

//     int gethight() {
//         return m_hight;
//     }

//     int calculateareao() {
//         return 2*m_hight*m_len+2*m_hight*m_width+2*m_len*m_width;

//     }
//     int calculatev() {
//         return m_hight*m_len*m_width;
//     }

//     // 利用成员函数判断两个立方体是否相等
//     bool issamebyclass(cube &c) {
//         if (m_len==c.getlen() && gethight()==c.gethight() && getwidth()==c.getwidth()) {
//             return true;
//         }
//         return false;
//     }
//     private:
//     int m_len;
//     int m_width;
//     int m_hight;
    

// };

// // 利用全局函数判断两个立方体是否相等
// bool issame(cube &c1, cube &c2) {
//     if (c1.getlen()==c2.getlen() && c1.gethight()==c2.gethight() && c1.getwidth()==c2.getwidth()) {
//         return true;
//     }
//     return false;
// }
// int main() {
//     cube c1;
//     c1.sethigh(10);
//     c1.setlen(10);
//     c1.setwidth(10);
//     cout << "面积"  << c1.calculateareao() << endl;
//     cout << "体积" << c1.calculatev() << endl;
//     cube c2;
//     c2.sethigh(10);
//     c2.setlen(10);
//     c2.setwidth(10);
//     bool ret=issame(c1,c2);
//     bool ret1=c1.issamebyclass(c2);
//     if (ret) {
//         cout << "相等"  << endl;
//     }
//     else {
//         cout << "不相等" << endl;
//     }
//     system("pause");
//     return 0;
// }

// 4.2 对象的初始化和清理
// 4.2.1 构造函数和析构函数
// 对象的初始化和清理也是两个非常重要的安全问题
//   一个对象或变量没有初始化状态，对其使用后果是未知的
//   同样的使用完一个对象或变量，没有及时清理，也会造成一定的安全问题
//   c++利用了构造函数和析构函数解决上述问题，这两个函数将会被编译器自动调用，完成对象初始化和清理工作。
//   对象的初始化和清理工作是编译器强制我们要做的事情，因此如果我们不提供构造和析构，编译器会提供编译器提供的构造函数和析构函数是空实现
// - 构造函数：主要作用于创建对象时对象的成员属性赋值，构造函数由编译器自动调用，无需手动调用
// - 析构函数：主要作用于对象销毁前系统自动调用，执行一些清理工作。
// 构造函数语法： 类名() {}
//   1. 构造函数，没有返回值也不写void
//   2. 函数名称与类名相同
//   3. 构造函数可以有参数，因此可以发生重载
//   4. 程序在调用对象时会自动调用构造，无需手动调用，而且只会调用一次

// 析构函数语法  ~类名() {}
//     1. 析构函数，没有返回值也不写void
//     2. 析构函数不可以有参数，因此不可以发生重载
//     3. 程序在对象销毁前会自动调用析构，无需手动调用，而且只会调用一次。

#include<iostream>
using namespace std;
#include<string>

// 对象的初始化和清理
//   1、 构造函数 进行初始化操作
// class person
// {
// public:
//     // 1 构造函数
//     //   没有返回值 不用谢void
//     //   函数名 与类名想用
//     //   构造函数可以有参数，可以发生重载
//     //   创建对象时，构造函数会自动调用 ，而且只会调用一次
//     //   
//     person() {
//         cout << "person构造函数的调用" << endl;
//     }
//     // 2 析构函数
//     //   没有返回值  不写void
//     //   函数名和类名想用  在名称前加
//     //   析构函数不可以有参数的，不可以发生重载
//     //   对象在销毁前 ，会自动调用析构函数，而且只会调用一次
//     ~person() {
//         cout << "person析构函数的调用" << endl;
//     }
// };

// // 构造函数和析构函数都是必须有的实现，如果我们不提供，编译器会提供一个空实现的构造和析构；
// void test01() {
//     person p; //在栈上的数据，test01执行完毕后会释放这个对象，所以析构函数也会执行。只是创建了对象，就可以直接实现构造函数的功能

// }


// int main() {
//     test01();
//     person p;  // 在main函数里面，需要整个函数都实现才会执行完毕，所以析构函数不会被执行
//     system("pause");
//     return 0;
// }


// 4.2.2 构造函数的分类以及调用
//   两种分类方式
//     按参数分为：有参构造和无参构造（默认构造函数）
//     按类型分为：普通构造和拷贝构造

//   三种调用方式
//      括号法、显示法、隐式转换法

// 分类
// class person {
// public:
//     // 构造函数
//     person() {
//         cout << "person构造函数的调用" << endl;
//     }
//     // 析构函数
//     person(int a) {
//         age=a;
//         cout << "personY有参构造函数的调用" << endl;
//     }

//     person(const person &p) {
//         // 将传入的人身上的所有属性拷贝到我身上
//         age=p.age;
//         cout << "拷贝构造函数的调用" << endl;

        
//     }
//     ~person() {
//         cout << "person析构函数的调用" << endl;
//     }
//     int age;

// };

// void test01() {
//     // 1、括号发
//     // person p1; // 默认构造函数调用
//     // person p2(10); //有参构造函数
//     // person p3(p2); //拷贝函数
//     // 注意事项：
//     // 调用默认构造函数时，不要加()
//     // 因为下面这行代码，编译器会认为是一个函数的声明，不会认为在创建对象。
//     // person p();
//     // void func();

//     // cout << "p2的年龄为:" << p2.age << endl;
//     // cout << "p3的年龄为:" << p3.age << endl;

//     // 2、显示法
//     // person p1;
//     // person p2=person(10); // 有参构造
//     // person p3=person(p2); // 拷贝构造
//     // person(10);  // 匿名对象 特点：当前执行结束后，系统会立即回收掉匿名对象
//     // cout << "aaaa" << endl;

//     // 注意事项2
//     // 不要利用拷贝函数初始化匿名对象，编辑器会认为person(p3)===person p3',这里的p3说明重定义了
//     // person(p3)

//     // 3、隐式转换法
//     person p4=10; // 相当于写了person p4=person(10) ,相当于有参构造
//     person p5=p4; // 拷贝构造
// }

// int main() {
//     test01();
//     system("pause");
//     return 0;
// }

// 4.2.3 拷贝函数调用动机(不是很懂哦)
// c++中拷贝函数调用时机通常由三种情况
//   使用一个已经创建完毕的对象来初始化一个新对象
//   值传递的方式给函数参数传值
//   以值传递方式返回局部对象


// 1、使用一个已经创建完毕的对象来初始化一个新对象
// 2、值传递的方式给函数参数传值
// 3、以值传递方式返回局部对象

// class person {
//     public:
//     person() {
//         cout << "person构造函数的调用" << endl;
//     }
//     person(int age) {
//         cout << "perso有参构造函数的调用" << endl;
//         m_age=age;
//     }
//     person(const person & p) {
//         cout << "person拷贝构造函数的调用" << endl;
//         m_age=p.m_age;
//     }
//     ~person() {
//         cout << "person析构函数的调用" << endl;
//     }
//     int age;
//     int m_age;
// };

// void test01() {
//     person p1(20);
//     person p2(p1);
//     cout << "p2的年龄为：" << p2.m_age << endl;
// }

// // 2、值传递的方式给函数参数传值
// void dowork(person p) {
   

// }

// void test02() {
//    person p;
//    dowork(p); //值传递的本质是拷贝一=一个副本出来
// }

// // 3、值方式返回局部对象
// void dowork2() {
//     person p1;
//     return p1; 
// }

// void test03() {
//     person p=dowork2();
// }

// int main() {
//     test01();
//     system("pause");
//     return 0;
// }

// 4.2.4 析构函数调用规则
// 默认情况下,c++编译器至少给一个类添加3个函数
// 1. 默认构造函数(无参,函数体为空)
// 2. 默认析构函数(午餐,函数体为空)
// 3. 默认拷贝构造函数,对属性进行值拷贝

// 构造函数调用规则
// 1. 如果用户定义有参构造函数,c++不再提供默认无参构造,但会提供默认拷贝构造
// 2. 如果用户定义拷贝构造函数,c++不会再提供其他构造函数


// class person {
//     public:

//     person() {
//         cout << "person的默认构造函数调用" << endl;
//     }
//     person(int age) {
//         cout << "perso有参构造函数的调用" << endl;
//         m_age=age;
//     }
//     person(const person & p) {
//         cout << "person拷贝构造函数的调用" << endl;
//         m_age=p.m_age;
//     }

//     // 编译器自己定义的,上面是用户自定义的.
//     // person(const person & p) {
//     //     m_age=p.m_age;
//     // }
//     ~person() {
//         cout << "person析构函数的调用" << endl;
//     }
//     int age;
//     int m_age;

// };

// void test02() {
//     person p(28);
//     person p2(p);
//     cout << "p2的年龄为：" << p2.m_age << endl;
// }

// void test01() {
//     person p;
//     p.m_age=18;
//     person p2(p);
//     cout << "p2的年龄为:" << p2.m_age << endl; //加上拷贝构造函数就变和不加拷贝函数是一样的,不在自定义拷贝函数编译器会自己写
// }
// int main() {
//     // test01();
//     test02();
//     system("pause");
//     return 0;
// }


// 4.2.5 深拷贝与浅拷贝
// 浅拷贝：简单的赋值拷贝操作
// 深拷贝：在堆区重新申请空间，进行拷贝操作

// class person {
// public:
//     person() {
//         cout << "person的默认构造函数调用" << endl;
//     }
//     person(int age, int height) {
//         cout << "perso有参构造函数的调用" << endl;
//         m_age=age;
//         m_height=new int(height);
//     }

//     // 自己实现拷贝构造函数，解决 浅拷贝带来的问题
//     person(const person &p) {
//         cout << "person拷贝构造函数调用" << endl;
//         m_age=p.m_age;
//         // m_height=p.m_height; //编译器的默认实现方式（浅拷贝）
//         m_height=new int(*p.m_height);
//     }
    
//     // 编译器自己定义的,上面是用户自定义的.
//     // person(const person & p) {
//     //     m_age=p.m_age;
//     // }
//     ~person() {
//         // 析构代码，将堆区开辟的数据做释放操作
//         if(m_height!=NULL) {
//             delete m_height;
//             m_height=NULL;
//         }
//         cout << "person析构函数的调用" << endl;
//     }
//     // int age;
//     int m_age;
//     int *m_height; //身高
// };

// void test01() {
//     // 浅拷贝带来的问题是：堆区内容重复释放，使用深拷贝就可以解决这些问题
//     person p1(18,160);
//     cout << "p1的年龄为：" << p1.m_age << "身高为：" << p1.m_height << endl;
//     person p2(p1);
//     cout << "p2的年龄为：" << p1.m_age << "身高为：" << p1.m_height << endl;


// }

// int main() {
//     test01();
//     system("pause");
//     return 0;
// }

// // 总结：如果属性有在堆区开辟的，一定要自己提供拷贝构造函数，防止浅拷贝带来的问题

// 4.2.6 初始化列表
// 作用：c++提供了初始化列表语法，用来初始化属性

// 语法：构造函数(): 属性1（值1），属性2（值2）,....

// class person {
//     public:
//     // 传统初始化操作
//     // person(int a,int b,int c) {
//     //     m_A=a;
//     //     m_B=b;
//     //     m_C=c;
//     // }
//     // 初始化列表初始化属性
//     person(int a,int b,int c) :m_A(a),m_B(b),m_C(c) {

//     }
    
//     int m_A;
//     int m_B;
//     int m_C;

// };

// void test01() {
//     // person p(10,20,30);
//     person p(30,20,10);
//     cout << "m_A" << p.m_A << endl;
//     cout << "m_B" << p.m_B << endl;
//     cout << "m_C" << p.m_C << endl;

// }
// int main() {
//     test01();
//     system("pause");
//     return 0;
// }


// 4.2.7 类对象作为类成员
// c++类中的成员可以是另一个类的对象，我们称为该成员为对象成员

// 手机类
// class phone {
//     public:
//     phone(string p_name) {
//         cout << "手机构造函数调用" << endl;
//         m_pname=p_name;
//     }
//     // 手机品牌名称
//     string m_pname;
//     ~phone() {
//         cout << "phone析构函数的调用" << endl;
//     }
    
// };

// class person {
//     public:
//     // phone m_phone=pname(隐式转换法进行初始化的操作)
//     person(string name,string pname): m_name(name), m_phone(pname){
//         cout << "person构造函数的调用" << endl;
//     }
//     ~person() {
//         cout << "person析构函数的调用" << endl;
//     }
//     //姓名
//     string m_name;
//     //手机
//     string m_phone;
// };

// void test01() {
//     person p("张三","苹果max");
//     cout << p.m_name << "拿着：" << p.m_name << endl;
// }
// // 当其他类对象作为本类成员，构造时候线构造类对象，在构造自身，析构的顺序？
// //
// int main() {
//     test01();
//     system("pause");
//     return 0;
// }


// 4.2.8 静态成员
//   静态成员就是在成员变量和成员函数前加上关键字static，称为静态成员
//   静态成员分为：
//   - 静态成员变量
//       所有对象共享同一份数据
//       在编译阶段分配内存
//       类内声明，类外初始化
//   - 静态成员函数
//        所有对象共享同一函数
//        静态成员函数只能访问静态成员变量


// class person {
//     public:
//     //所有对象共享同一份数据
//     //在编译阶段分配内存
//     //类内声明，类外初始化
//     static int m_A;  // 类内声明
//     //静态成员变量也是有访问权限的(公共权限可以访问，类外访问不到私有静态成员变量)
//     private:
//     static int m_B;

// };
// //类外初始化
// int person::m_A=100;
// int person::m_B=200;

// void test01() {
//     person p;
//     cout << p.m_A << endl;
//     person p2;
//     p2.m_A=200;
//     cout << p.m_A << endl; // 结果仍未200，说明虽有对象共享同一份数据
//     // cout << p.m_B << endl; //类外访问不到私有静态成员变量
    

// }

// void test02() {
//     //静态成员变量不属于某个对象上，所有对象都共享同一份数据
//     //因此静态成员变量有两种访问方式

//     // 1、通过对象进行访问
//     person p;
//     cout << p.m_A << endl;

//     // 2、通过类名进行访问
//     cout << person::m_A << endl;

// }
// int main() {
//     test01();
//     system("pause");
//     return 0;
// }
// class person {
//     public:
//     //静态成员函数
//     static void func() {
//         m_A=100;//静态成员函数可以访问静态成员变量
//         // m_B=200; //静态成员函数不可以访问非静态成员变量，无法区分到底是哪个对象的m_B属性，m_A是大家都在共享的数据所以可以访问
//         cout << "static void func的调用" << endl;
//     }
//     int m_B;
//     static int m_A;
//     // 静态成员函数也是有访问权限的
//     private:
//     static void func2() {
//         cout << "static void func2调用" << endl;
//     }
// };

// int person::m_A=0;

// void test01() {
//     // 两种访问方式
//     //1、通过对象访问呢
//     person p;
//     p.func();
//     // 通过类名访问
//     person::func();
//     person::func2();  //类外访问不到私有静态成员函数
// }

// int main() {
//     system("pause");
//     return 0;
// }

// 4.3 c++对象模型和this指针
// 4.3.1 成员变量和成员函数分开存储
// 在c+中，类内的成员变量和成员函数分开存储
// 只有非静态成员变量才属于类的对象上

// class person {

// };

// class person1 {
//     int m_A; //非静态变量
//     static int m_B; // 静态变量
//     void func(); // 非静态成员函数
//     static void func(); // 静态成员函数
// };
// int person1::m_B=200;

// void test01() {
//     person p;
//     // 空对象占用内存空间为：1个字节
//     // c++编译器会给每个空对象也分配一个字节空间，为了区分空对象占内存的位置。
//     //每个空对象也应该有一个独一无二的内存地址。
//     cout << "size of p=" << sizeof(p) << endl;
// }

// void test02() {
//     person1 p;
//     // 非静态成员变量属于类的对象上
//     // 静态成员变量不属于类的对象上
//     // f非静态成员函数不属于类的对象上
//     cout << "size of p=" << sizeof(p) << endl;

// }

// int main() {
//     test02();
//     system("pause");
//     return 0;
// }


// 4.3.2 this指针的概念

// c++中成员变量和成员函数是分开存储的
// 每一个非静态成员函数只会诞生一份函数实例，也就是说多个同类型的对象会共用一块代码
// 那么问题是：这一块代码如何区分哪个对象调用自己的呢？
// c++通过提供特殊的对象指针this指针，解决上述问题。this指针指向被调用的成员函数所属的对象
// this指针是隐含每一个非静态成员函数内的一种指针，不需要定义，直接使用即可。

// this指针的用途
//  - 当形参和成员变量同名时，可用this指针来区分
//  - 在类的非静态成员函数中返回对象本身，可使用return *this

//作用


// class person {
//     public:
//     //成员属性与传入的参数名称要区别，否则三个age会表示相同的内容，出现名称冲突的问题
//     person(int age) {
//         // age=age;
//         //this指针指向被调用的成员函数所属的对象
//         this->age=age;
//     }
//     //返回引用
//     person& personaddage(person &p) {
//         this->age+=p.age;
//         return *this;  // this是指向p2的指针，*this就是p2的本体
//     } 
//     //返回值
//     person personaddage1(person &p) {
//         this->age+=p.age;
//         return *this;  // this是指向p2的指针，*this就是p2的本体
//     } 
//     int age;
// };

// //1、解决名称冲突
// void test01() {
//     person p1(19);
//     cout << "p1的年龄为：" << p1.age << endl;
// }

// //2、在类的非静态成员函数中返回对象本身，可使用return *this
// void test02() {
//     person p1(10);
//     person p2(10);
//     // p2.personaddage(p1);
//     //链式变成思想，可以一直往后追加
//     // p2.personaddage(p1).personaddage(p1); 
//     // 因为personaddage1返回的是值，每次调用该该函数时，都会赋值一份新的内容，这样出现了p2',之后在调用是p2''，最后就不再是本身了
//     p2.personaddage1(p1).personaddage1(p1);
//     cout << "p2的年龄为" << p2.age << endl;
// }

// int main() {
//     test02();
//     system("pause");
//     return 0;
// }


// 4.3.3 空指针访问成员函数
// c++中空指针也是可以调用成员函数的，但是也要注意有没有用到this指针
// 如果用到this指针，需要加以判断保证代码的健壮性
// class person {
//     public:
//     void showclassname() {
//         cout << "this is person class" << endl;
//     }

//     void showpersonage() {
//         //报错原因是因为传入的指针为NULL
//         //解决方案：使用if语句判断下
//         if(this==NULL) {
//             return;
//         }
//         cout << "age==" << this->m_age << endl;

//     }
//     int m_age;
// };

// void test01() {
//     person *p=NULL;
//     p->showclassname();
//     p->showpersonage();

// }
// int main() {
//     test01();
//     system("pause");
//     return 0;
// }

// 4.3.4 onst修饰成员函数

// 常函数：
//  - 成员函数后加const后我们成为这个函数为常函数
//  - 常函数内不可以修改成员属性
//  - 成员属性声明时加关键字mutable后，在常函数中依然可以修改

// 常对象：
//  - 声明对象前加const称该对象为常对象
//  - 常对象只能调用函数


// 常函数：
// class person {
//     public:
//     //在函数体内部都有一个this指针，this指针本质是一个指针常量，即指针的指向是不可以修改的
//     //函数的this指针指向p,此时this指针不可以修改，但是this指向的值是可以修改的,可以理解成peron *const this;
//     //如果想要this指向的值也不可以修改，可以加上const
//     //在成员函数后加上const，本质修饰的是this指向，汤指针指向的值也不可以修改
//     void showperson() const {
//         // this->m_A=100; m_A不可修改
//         this->m_B=200;
//         // this=NULL; //this指向的值是可以修改的
//     }
//     void func() {
//         m_A=100;
//     }
//     int m_A;
//     mutable int m_B; //特殊变量，即使在常函数中也可以修改这个值
// };

// void test01() {
//     person p;
//     p.showperson(); //p调用showperson之后，，该函数的this指针指向p,此时this指针不可以修改，但是this指向的值是可以修改的
// }
// // 常对象
// void test02() {
//     const person p{}; // 在对象前加const，变为常数=对象
//     // p.m_A=100;
//     p.m_B=200; //m_B是特殊值，在常对象下也可以修改

//     //常对象只能调用常函数,不可以调用普通成员函数，因为普通成员函数可以修改属性
//     // p.func(); 
// }
// int main() {
//     test02();
//     system("pause");
//     return 0;
// }

// 4.4 友元
// 在程序里，有些私有属性也想让类外特殊的一些函数或者类进行访问，就需要用到友元技术
// 友元目的是让一个函数或者类访问另一个类的私有成员
// 友元关键字为friend
// 友元的三种实现
//  - 全局函数做友元
//  - 类做友元
//  - 成员函数做友元

// 4.4.1 全局函数做友元

// class building {
//     // goodgay全局函数可以访问building中的私有成员
//     friend void goodgay(building *Building);
//     public:
//     building() {
//         m_settingroom="客厅";
//         m__bedroom="卧室";
//     }
//     public:
//     string m_settingroom; //客厅
//     private:
//     string m__bedroom; //我是

    
// }; 

// //全局函数

// void goodgay(building *Building) {
//     cout << "好基友全局函数正在访问：" << Building->m_settingroom << endl;
//     cout << "好基友全局函数正在访问：" << Building->m__bedroom<< endl; //私有属性不能访问
// }

// void test01() {
//     building Building;
//     goodgay(&Building);
// }
// int main() {
//     test01();
//     system("pause");
//     return 0;
// }

// 4.4.2 类做友元


// class Building;
// class goodgay {
//     public:
//     goodgay();  
//     void visit(); //访问Building中的属性
//     Building *building;


// };

// class Building {
//     // goodgay可以访问本类中私有成员。
//     friend class goodgay;
//     public:
//     Building();
//     public:
//     string m_sittingroom;
//     private:
//     string m_bedroom;
// };
// // 类外写成员函数
// Building::Building() {
//     m_sittingroom="客厅";
//     m_bedroom="卧室";
// }

// goodgay::goodgay() {
//     building=new Building;
// }

// void goodgay::visit() {
//     cout << "好基友类正在访问" << building->m_sittingroom << endl;
// }
// void test01()  {
//     goodgay gg;
//     gg.visit();
// }

// int main() {
//     test01();
//     system("pause");
//     return 0;
// }


// 4.4.3成员函数做友元
// class Building;
// class goodgay {
//     public:
//     goodgay();
//     void visit(); //让cisist函数可以访问Building中私有成员
//     void visit2();//让cisist2函数不可以访问Building中私有成员
//     Building *building;
// };

// class Building {
//     //告诉编译器goodgay类下的visit成员函数作为本类的好朋友
//     friend void goodgay::visit();
//     public:
//     Building();
//     public:
//     string m_sittiingroom;
//     private:
//     string m_bedroom;

// };
// // 类外实现成员函数
// Building::Building() {
//     m_sittiingroom="客厅";
//     m_bedroom="卧室";

// }
// goodgay::goodgay() {
//     building=new Building;
// }

// void goodgay::visit() {
//     cout << "visit函数正在访问：" << building->m_sittiingroom << endl;
//     cout << "visit函数正在访问：" << building->bedroom << endl;
// }
// void goodgay::visit2() {
//     cout << "visit2函数正在访问：" << building->m_sittiingroom << endl;
//     // cout << "visit2函数正在访问：" << building->bedroom << endl;

// }
// void test01() {
//     goodgay gg;
//     gg.visit();
//     gg.visit2();
// }
// int main() {
//     test01();
//     system("pause");
//     return 0;
// }

// 4.5 运算符重载
// 概念：对已有的运算符重新进行定义，赋予另一种功能，以适应不同的数据类型
// 4.5.1 加号运算符重载
// 作用：实现两个自定义数据类型相加的运算

// 加号运算符重载：通过自己写成员函数，实现两个对象相加属性后返回新的对象




// class person {
//     public:
//     // 1、成员函数重载加号
//     // person operator+(person &p) {
//     //     person temp;
//     //     temp.m_A=this->m_A+p.m_A;
//     //     temp.m_B=this->m_B+p.m_B;
//     //     return temp;
//     // }
//     int m_A;
//     int m_B;

// };
// // 2、全局函数重载加号
// person operator+(person &p1,person &p2) {
//     person temp;
//     temp.m_A=p1.m_A+p2.m_A;
//     temp.m_B=p1.m_B+p2.m_B;
//     return temp;
    
// }

// // 函数重载版本
// person operator+(person &p1,int num) {
//     person temp;
//     temp.m_A=p1.m_A+num;
//     temp.m_B=p1.m_B+num;
//     return temp;
// }
// void test01() {
//     person p1;
//     p1.m_A=10;
//     p1.m_B=10;
//     person p2;
//     p2.m_A=10;
//     p2.m_B=10;
//     // 成员函数的本质调用
//     // person p3=p1.operator+(p2)

//     //全局函数重载本质调用
//     // person p3=operator+(p1,p2);


//     person p3=p1+p2; //报错：不知道如何进行加号操作

//     // 运算符重载，也可以发生函数重载
//     person p4=p1+10;
//     cout << "P3.m_A=" << p3.m_A << endl;
//     cout << "P3.m_B=" << p3.m_B << endl;
//     cout << "P4.m_A=" << p4.m_A << endl;
//     cout << "P4.m_B=" << p4.m_B << endl;
// }
// int main() {
//     test01();

//     system("pause");
//     return 0;
// }
// 总结1：对于内置的数据类型的表达式的运算符是不可以更改的
// 总结2：不要滥用函数重载


// 4.5.2 左移运算符重载
// 作用：可以输出自定义的数据类型

// class person {

//     friend ostream & operator<<(ostream &cout,person p);
//     public:
//     person(int a,int b) {
//         m_A=a;
//         m_B=b;
//     }
//     private:
//     //利用成员函数重载左移运算符
//     //不会利用成员函数重载左移运算符，因为无法实现cout在左侧
//     // void operator<<(cout);
//     int m_A;
//     int m_B;
// };



// // 只能利用全局函数重载左移运算符

// ostream & operator<<(ostream &cout,person p) //本质 perator<<(cout,p) 简化 cout << p
// {
//     cout << "m_A=" << p.m_A << "p.m_B=" << p.m_B << endl;
//     return cout;
// }

// void test01() {
//     person p(10,10);
//     // p.m_A=10;
//     // p.m_B=10;
//     //使用左移运算符是为了能够直接输出p，否则不可以直接输出
//     cout << p << "hello" << endl;

//     // cout << p.m_A << endl;

// }
// int main() {
//     test01();
//     system("pause");
//     return 0;
// }

// // 总结：重载左移运算符配合友元可以实现输出自定义数据类型

// 4.5.3 递增运算符重载
// 作用：通过重载递增运算符，实现自己的整型数据

//递增运算符重载 ++符号，--符号

// 重载递增运算符
// class MyInteger {
//     friend ostream & operator<<(ostream& cout,MyInteger myint);
//     public:
//     MyInteger() {
//         m_num=0;
//     }
//     // 重载前置++运算符
//     MyInteger& operator++() {
//         // 先进性++运算
//         m_num++;
//         //再将自身返回，不能直接返回值，否则不可以实现链式相加，后面再进行++的结果一致想用，即返回值相当于创建了新的对象
//         return *this;
//     }
//     // 重载后置++运算符()
//     //int表示的是占位参数，可以用于区分前置和后置递增
//     //后置递增返回的是值，前置递增返回的是引用
//     MyInteger operator++(int) {
//         // 先记录当时结果
//         MyInteger temp=*this;

//         //后递增 
//         m_num++;
//         //最后将记录结果返回
//         return temp;   

//     }
//     private:
//     int m_num;
// };

// ostream & operator<<(ostream& cout,MyInteger myint) {
//     cout << myint.m_num;
//     return cout;
// }
// void test01() {
//     //创建的整型数据，使用重载++运算符才可以实现计算
//     MyInteger myint; //自定义的对象，不知道怎么输出，会报错，需要写个重载左移运算符
//     cout << ++(++myint) << endl;
// }

// void test02() {
//     MyInteger myint;
//     cout << myint++ << endl;
//     cout << myint << endl;

// }
// int main() {
//     int a=10;
//     cout << ++a << endl;
//     cout << a << endl;

//     int b=10;
//     cout << b++ << endl;
//     cout << b << endl;

//     test01();
//     system("pause");
//     return 0;
// }


// 总结：前置递增返回的是引用，后置递增函数返回的是值


// 4.5.4 赋值运算符重载
// c++编译器至少给一个类添加4个函数
//  - 默认构造函数（无参，函数体为空）
//  - 默认析构函数（无参，函数体为空）
//  - 默认拷贝构造函数，对属性值进行值拷贝
//  - 赋值运算符operator=,对属性进行值拷贝

// 如果类中有属性指向堆区，做赋值操作时也会出现深浅拷贝问题（浅拷贝：堆区内存重新释放）
// class person {
//     public:
//     person(int age) {
//         m_age=new int(age);
//     }
//     ~person() {
//         if (m_age!=NULL) {
//             delete m_age;
//             m_age=NULL;
//         }
        
//     }

//     //重载赋值运算符
//     person& operator=(person &p) {
//         //编译器提供浅拷贝
//         // m_age=p.m_age;

//         // 应该先判断是否有属性在堆区，如果有先释放干净，然后再深拷贝

//         if (m_age!=NULL) {
//             delete m_age;
//             m_age=NULL;
//         }
//         // 深拷贝
//         m_age=new int(*p.m_age);
//         return *this;
//     }

//     int *m_age;
// };

// void test01() {
//     person p1(19);
//     person p2(20);
//     p2=p1; // 赋值操作
//     cout << "P1的年龄为：" << p1.m_age << endl;
//     cout << "P2的年龄为：" << p2.m_age << endl;
// }


// int main() {
//     int a=10;
//     int b=20;
//     int c=30;
//     c=b=a;
//     cout << "a=" << a << endl;
//     cout << "b=" << b << endl;
//     cout << "c=" << c << endl;
//     test01();
//     system("pause");
//     return 0;
// }


// 4.5.5 关系运算符重载
// 作用：重载关系运算符，可以让两个自定义类型对象进行对比操作

// class person {
//     public:
//     person(string name,int age) {
//         m_name=name;
//         m_age=age;
//     }

//     // 重载==号
//     bool operator==(person &p) {
//         if (this->m_name==p.m_name && this->m_age==p.m_age) {
//             return true;
//         }
//         return false;
//     }

//     bool operator!=(person &p) {
//         if (this->m_name==p.m_name && this->m_age==p.m_age) {
//             return false;
//         }
//         return true;
//     }
//     string m_name;
//     int m_age;
// };

// void test01() {
//     person p1("Tom1",18);
//     person p2("Tom",18);

//     if (p1==p2) {
//         cout << "p1和p2是相等的" << endl;
//     }
//     else {
//         cout << "p1和p2是不相等的" << endl;
//     }

//     if (p1!=p2) {
//         cout << "p1和p2是不相等的" << endl;
//     }
//     else {
//         cout << "p1和p2是相等的" << endl;

//     }
// }

// int main() {
//     test01();
//     system("pause");
//     return 0;
// }


// 函数调用运算符重载
//  - 函数调用运算符{}也可以重载
//  - 由于重载后使用的方式非常像函数的使用，也成为仿函数
//  - 仿函数没有固定写法，非常灵活

// 打印输出类
// class myprint {
//     public:
//     void operator()(string test) {
//         cout << test << endl;
//     }
// };


// void test01() {
//     myprint myPrint;
//     myPrint("hello");
// }

// // 仿函数非常灵活，没有固定的写法
// // 加法类

// class myadd {
//     public:
//     int operator() (int num1,int num2) {
//         return num1+num2;
//     }
// };

// void test02() {
//     myadd myAdd;
//     int ret=myAdd(100,100);
//     cout << ret << endl;
//     // 匿名函数对象
//     cout << myadd()(100,100) << endl;

// }
// int main() {
//     test01();
//     test02();
//     system("pause");
//     return 0;
// }

// 4.6 继承
// 好处：减少代码重复
// 语法：class 子类：继承方式父类
// 子类也成为派生类
// 父类也成为基类
// 4.6.1 继承的基本语法


// class basepage {
//     public:
//     void header() {
//         cout << "首页、公开课、登录" << endl;

//     }
//     void footer() {
//         cout << "公共底部" << endl;

//     }

//     void left() {
//         cout << "公共分类列表" << endl;

//     }
// };

// // java页面
// class java: public basepage {
//     public:
//     void cotent() {
//         cout << "jave内容" << endl;
//     }

// };

// // python页面
// class python: public basepage {
//     public:
//     void cotent() {
//         cout << "python内容" << endl;
//     }

// };
// // java页面
// class cjiajia: public basepage {
//     public:
//     void cotent() {
//         cout << "cjiajia内容" << endl;
//     }

// };

// void test01() {
//     cout << "java下载视频页面如下" << endl;
//     java ja;
//     ja.header();
//     ja.footer();
//     ja.left();
//     ja.cotent();
//     cout << "--------------" << endl;
//     cout << "python下载视频页面如下" << endl;
//     python py;
//     py.header();
//     py.footer();
//     py.left();
//     py.cotent();
//     cout << "--------------" << endl;

// }
// int main() {
//     test01();
//     system("pause");
//     return 0;
// }


// 4.6.2 继承方式
//  - 公共继承 public
//  - 保护继承 protected
//  - 私有继承 private


// 公共继承

// class Base1 {
//     public:
//     int m_A;
//     protected:
//     int m_B;
//     private:
//     int m_C;
// };

// class son1:public Base1 {
//     public:
//     void func() {
//         m_A=10; //父类中的公共线圈，到子类中依然是公共权限
//         m_B=10; //父类中的保护权限成员到子类中依然是保护权限
//         // m_C=10; // 父类中的私有权限成员，子类访问不到
//     }
// };
// void test01() {
//     son1 s1;
//     s1.m_A=100;
//     // s1.m_B=100; // 到了son1中，m_B是保护权限，类外访问不到


// }

// // 保护继承
// class base2 {
//     public:
//     int m_A;
//     protected:
//     int m_B;
//     private:
//     int m_C;
// };

// class son2 :protected base2 {
//     public:
//     void func() {
//         m_A=100; // 父类中的公共成员到子类中变为保护权限
//         m_B=100; // 父类中保护成员到子类中变为保护权限
//         // m_C=100; // 父类中的私有成员子类访问不到
//     }
// };

// void test01() {
//     son2 s1;
//     // s1.m_A=100; //在son2中，m_A变为保护权限，因此类外访问不到
//     // s1.m_B=100; // 在son2中，m_B保护权限，不可以访问
// };
// class base3 {
//     public:
//     int m_A;
//     protected:
//     int m_B;
//     private:
//     int m_C;
// };

// class son3:private base3 {
//     public:
//     void func() {
//         m_A=100; //父类中公共成员到子类中变为私有成员
//         m_B=100;// 父类中保护成员到子类中变为私有成员
//         // m_C=100; //父类中私有成员子类中访问不到
//     }
// };

// void test03() {
//     son3 s1;
//     // s1.m_A=100; // 到son3中，变为私有成员类外访问不到
//     // s1.m_B=1000; // 到son3中变为私有成员类外访问不到
// };

// class grandson2 :public son3 {
//     public:
//     void func() {
//         // m_A=1000; // 到了son3中m_A变为私有，即使是儿子，也是访问不到
//         // m_B=1000; // 到son3中,变为私有成员,类外访问不到
//     }
// };

// int main() {
//     system("pause");
//     return 0;
// }


// 4.6.3 继承中的对象模型

// 问题:从父类继承过来的成员,哪些属于子类对象中

// class base {
//     public:
//     int m_A;
//     protected:
//     int m_B;
//     private:
//     int m_C;
// };

// class son:public base {
//     public:
//     int m_D;

// };
// // 利用开发人员命令提示工具查看对象模型
// // 跳转盼复 C:
// // 跳转文件路径 cd 具体路径
// // 查看命名
// // cl /d1 reportSingleClassLayor类名 文件名

// void test01() {
//     // 父类中所有非静态成员属性都会被子类继承下去
//     // 父类中私有成员属性是被编译器隐藏了，因此是访问不到，但是确实被继承下去了
//     cout << "size of son=" << sizeof(son) << endl;
// }


// int main() {
//     test01();
//     system("pause");
//     return 0;
// }

// 4.6.4 继承中构造和析构顺序
// 子类继承父类后，当创建子类对象，也会调用父类的构造函数
// 问题：父类和子类的构造和析构顺序是谁先谁后



// class base {
//     public:
//     base() {
//         cout << "base的构造函数" << endl;
//     }
//     ~base() {
//         cout << "base的析构函数" << endl;
//     }
// };

// class son:public base {
//     public:
//     son() {
//         cout << "son的构造函数" << endl;
//     }
//     ~son() {
//         cout << "son的析构函数" << endl;
//     }
// };

// void test01() {
//     // base b;
//     // 继承中的构造和析构顺序如下：
//     // 继承中先调用父类构造函数，在调用子类构造函数，析构的顺序与构造的顺序相反
//     son s;
// }

// int main() {
//     test01();
//     system("pause");
//     return 0;
// }


// 4.6.5 继承中同名成员处理方式
// 问题：当子类与父类出现同名的成员，如何通过子类对象，访问到子类或父类中同名的数据呢？

//  - 访问子类同名成员，直接访问即可
//  - 访问父类同名成员，需要加作用域

// class base {
//     public:
//     base() {
//         m_A=100;
//     }
//     void func() {
//         cout << "base-func()调用" << endl;
//     }
//     void func(int a) {
//         cout << "son-func()调用" << endl;
//     }
//     int m_A;
// };

// class son :public base {
//     public:
//     son() {
//         m_A=200;
//     }
//     void func() {
//         cout << "son-func()调用" << endl;
//     }

    
//     int m_A;
// };
// // 同名成员属性处理方式
// void test01() {
//     son s;
//     cout << "son_m_A=" << s.m_A << endl;
//     //如果通过子类对象访问父类中的成员，需要加上作用域
//     cout << "base_m_A" << s.base::m_A << endl;
// }

// void test02() {
//     son s; //直接调用 调用的是子类中的同名成员

//     // 如何调用父类中同名成员函数？

//     s.func();
    
//     s.base::func();
//     //如果子类中出现和父类同名的成员函数，子类的同名成员会隐藏掉父类中所有同名成员函数
//     //如果想访问到父类中被隐藏的同名成员函数，需要加作用域

//     s.base::func(100);
// }

// int main() {
//     test02();
//     system("pause");
//     return 0;
// }



// 4.6.6 继承中同名静态成员处理方式
// 问题：继承中同名的静态成员在子类对象上如何进行访问？
// 静态成员和非静态成员出现同名，处理方式一致

//  - 访问子类同名成员，直接访问即可
//  - 访问父类同名成员，需要加上


// class base {
//     public:
//     static int m_A;
//     static void func() {
//         cout << "son-static void func()" << endl;
//     }
//     static void func(int a) {
//         cout << "son-static void func()" << endl;
//     }
// };
// int base::m_A=100;

// class son:public base {
//     public:
//     static int m_A;
//     static void func() {
//         cout << "son-static void func()" << endl;
//     }

// };
// int son::m_A=200;
// //同名静态成员属性

// void test01() {
//     son s;
//     // 1、通过对象访问
//     cout << "son_m_A" << s.m_A << endl;
//     cout << "BASE_m_A" << s.base::m_A << endl;
//     // 2、通过类名访问
//     cout << "通过类名访问" << endl;
//     cout << "son下_m_a" << son::m_A << endl;
//     //第一个：：代表通过类名的方式访问，第二个：：代表访问父类作用域下
//     cout << "son下_m_a" << son::base::m_A << endl;
// }

// void test02() {
//     son s;
//     // 1、通过对象访问
//     s.func();
//     s.base::func();
//     //2、通过类名的方式访问
//     son::func();
//     son::base::func();

//     // 子类出现和父类同名金泰成员函数，也会隐藏父类中所有同名成员函数
//     //如果想访问父类中被隐藏同名成员，需要加作用域
//     son::base::func(100);
// }
// //同名静态函数
// int main() {
//     test02();
//     system("pause");
//     return 0;
// }

// 4.6.7 多继承语法

// c++允许一个类继承多个类
// 语法： class子类：继承方式 父类1，继承方式 父类2；
// 多继承可能会引发父类中有同名成员出现，需要加作用域区分
// c++实际开发中不建议用多继承

// class base1 {
//     public:
//     base1() {
//         m_A=100;
//     }
//     int m_A;
// };


// class base2 {
//     public:
//     base2() {
        
//         m_A=200;
//     }
//     int m_A;
// };


// class son:public base1, public base2 {
//     public:
//     son() {
//         m_C=300;
//         m_D=400;
//     }
//     int m_C;
//     int m_D;
// };

// void test01() {
//     son s;
//     cout << "sizeof son" << sizeof(s) << endl;
//     //当父类中出现同名成员，需要加作用域区分
//     cout << "base1_m_A=" << s.base1::m_A << endl;
//     cout << "base2_m_A=" << s.base2::m_A << endl;
// }

// int main() {
//     test01();
//     system("pause");
//     return 0;
// }


// 4.6.8 菱形继承（钻石继承）

// 概念：
//  - 两个派生类继承同一个基类
//  - 又有某个类他同时继承两个派生类
 
// 存在问题：
//  - 引发二义性


// 动物类
// class animal {
//     public:
//     int m_age;
// };
// //利用虚继承 解决菱形继承的问题
// // 继承之前 加上关键字virtual 变为虚继承
// // animal类称为虚基类
// // 🐏类
// class sheep :virtual public animal {

// };

// // 驼类
// class tuo :virtual public animal {

// };

// //羊驼类
// class sheeptuo:public sheep,public tuo {

// };

// void test01() {
//     sheeptuo st;
//     // st.m_age=18;
    
//     st.m_age=18;
//     st.tuo::m_age=28;
//     //当菱形继承，两个父类拥有相同的数据，需要加以作用域区分
//     cout << "st.sheep::m_age" << st.sheep::m_age << endl;
//     cout << "st.tuo::m_age" << st.tuo::m_age << endl;
//     //这份数据我们指导，只有一份就可以，菱形继承导致数据有两份，资源浪费。
//     cout << "st.m_age" << st.m_age << endl;
// }


// int main() {
//     test01();
//     system("pause");
//     return 0;
// }

// 4.7 多态
// 4.7.1 多态的基本概念
// 多态是c++面向对象的三大特征之一
// 多态分为两类
//  - 静态多态：函数重载和运算符重载属于静态多态，复用函数名
//  - 动态多态：派生类和虚函数实现运行时多态
// 静态多态和动态多态的区别
//  - 静态多态的函数地址早绑定-编译阶段确定函数地址
//  - 动态多态的函数地址晚绑定-运行阶段确定函数地址
// class animal {
//     public:
//     // 虚函数
//     virtual void speak() {
//         cout << "动物在说话" << endl;
//     }
// };

// // 猫类
// class cat : public animal {
//     public:
//     // 重写 函数返回值类型 函数名 参数列表完全相同
//     void speak() {
//         virtual cout << "小猫在说话" << endl;
//     }
// };

// // 狗类
// class dog : public animal {
//     public:
//     void speak() {
//         cout << "小狗在说话" << endl;
//     }
// };
// //执行说话函数
// //地址早绑定  在编译阶段确定了函数的地址
// // 如果想执行让猫说话，那么这个函数的地址就不能提前绑定，需要在运行阶段进行绑定，地址晚绑定

// //动态多态满足条件
// // 1、有继承关系
// // 2、子类重写父类中的虚函数

// // 动态多态使用
// // 父类的指针或者引用指向子类对象

// void doSpeak(animal &Animal) {
//     Animal.speak();
    
// }

// void test01() {
//     cat Cat;
//     doSpeak(Cat);
//     dog Dog;
//     doSpeak(Dog);
// }

// int main() {
//     test01();
//     system("pause");
//     return 0;
// }


// 多态原理刨析
// 加上virtual本质上是指


// class animal {
//     public:
//     // 虚函数
//     virtual void speak() {
//         cout << "动物在说话" << endl;
//     }
// };

// // 猫类
// class cat : public animal {
//     public:
//     // 重写 函数返回值类型 函数名 参数列表完全相同
//     void speak() {
//         cout << "小猫在说话" << endl;
//     }
// };

// // 狗类
// class dog : public animal {
//     public:
//     void speak() {
//         cout << "小狗在说话" << endl;
//     }
// };
// //执行说话函数
// //地址早绑定  在编译阶段确定了函数的地址
// // 如果想执行让猫说话，那么这个函数的地址就不能提前绑定，需要在运行阶段进行绑定，地址晚绑定

// //动态多态满足条件
// // 1、有继承关系
// // 2、子类重写父类中的虚函数

// // 动态多态使用
// // 父类的指针或者引用指向子类对象

// void doSpeak(animal &Animal) {
//     Animal.speak();
    
// }

// void test01() {
//     cat Cat;
//     doSpeak(Cat);
//     dog Dog;
//     doSpeak(Dog);
// }

// void test02() {
//     cout << "size of animal=" << sizeof(animal) << endl;
// }

// int main() {
//     test02();
//     system("pause");
//     return 0;
// }









// 4.7.2 多态案例--计算器类
// 案例描述：分别利用普通写法和多态技术，设计实现两个操作数进行运算的计算器类

// 多态的优点：
//  - 代买组织结构清晰
//  - 可读性强
//  - 利于前期和后期的扩展以及维护
// class calculator {
//     public:
//     int getresult(string oper) {
//         if(oper=="+") {
//             return m_num1+m_num2;
//         }
//         else if(oper=="-") {
//             return m_num1-m_num2;
//         }
//         else if(oper=="*") {
//             return m_num1*m_num2;
//         }

//     }
//     // 如果想扩展新的功能，需要修改源码
//     // 在真实开发中，体长开闭原则
//     // 开闭原则：对扩展进行开放，对修改进行关闭
//     int m_num1; 
//     int m_num2;
// };

// // 利用多态实现计算器
// // 多态好处：
// // 1、组织结构清晰
// // 2、可读性强
// // 3、对于前期的维护和

// // 实现计算器抽象类
// class abstractcalcultor {
//     public:
//     virtual int getresult() {
//         return 0;
//     }
//     int m_num1;
//     int m_num2;
// };

// // 加法计算器类
// class addcalcultor:public abstractcalcultor {
//     public:
//     int geresult() {
//         return m_num1+m_num2;
//     }
// };

// //减法计算器类
// class subcalcultor:public abstractcalcultor {
//     public:
//     int geresult() {
//         return m_num1-m_num2;
//     }
// };

// //乘法计算器类
// class mulcalcultor:public abstractcalcultor {
//     public:
//     int geresult() {
//         return m_num1*m_num2;
//     }
// };
// // 
// void test02() {
//     // 多态使用条件
//     // 父类指针或者引用指向子类对象
//     abstractcalcultor *abc=new addcalcultor;
//     abc->m_num1=10;
//     abc->m_num2=10;
//     cout << abc->m_num1 << "+" << abc->m_num2 << "=" << abc->getresult() << endl;
//     //堆区数据手动销毁
//     delete abc;
//     //减法运算
//     abc=new subcalcultor;
//     cout << abc->m_num1 << "-" << abc->m_num2 << "=" << abc->getresult() << endl;
//     delete abc;
//     //乘法运算
//     abc=new mulcalcultor;
//     cout << abc->m_num1 << "*" << abc->m_num2 << "=" << abc->getresult() << endl;
//     delete abc;

// }


// void test01() {
//     calculator c;
//     c.m_num1=10;
//     c.m_num2=10;
//     cout << c.m_num1 << "+" << c.m_num2 << "=" << c.getresult("+") << endl;
//     cout << c.m_num1 << "-" << c.m_num2 << "=" << c.getresult("-") << endl;
//     cout << c.m_num1 << "*" << c.m_num2 << "=" << c.getresult("*") << endl;
// }

// int main() {
//     test02();
//     system("pause");
//     return 0;
// }






// 4.7.3 纯虚函数和抽象类
// 在多态中，通常父类中虚函数的实现是毫无意义的，主要都是调用子类重写的内容
// 因此可以将虚函数改为纯虚函数
// 纯虚函数语法： virtual 返回值类型 函数名 (参数列表)=0;

// 当类中有了纯虚函数，这个类也成为抽象类

// 抽象类的特点：
//  - 无法实例化对象
//  - 子类必须重写抽象类中的纯虚函数，否则也属于抽象类
// class base {
//     public:
//     // 纯虚函数
//     // 只要有一个纯虚函数，这个类称为抽象类
//     // 1、无法实例化对象
//     // 2、抽象类的子类必须要重写父类中的纯虚函数，否则也属于抽象类
//     virtual void func()=0;


// };

// class son : public base {
//     public:
//     virtual void func() {
//         cout << "func函数的调用" << endl;
//     }
// };

// void test01() {
//     // base b;//抽象类无法实例化对象
//     // new base;//抽象类无法实例化对象
//     son s; //抽象类的子类必须要重写父类中的纯虚函数，否则也属于抽象类
//     base *Base =new son;
//     Base->func();
// }

// int main() {
//     test01();
//     system("pause");
//     return 0;
// }






// 4.7.4 多态案例二-制作饮品

// class abstractdrinking {
//     public:
//     //煮水
//     virtual void boil()=0;

//     // 冲泡
//     virtual void brew()=0;

//     //倒入杯中
//     virtual void  pourincup()=0;

//     //加入辅料
//     virtual void putsomething()=0;

//     //制作饮品
//     void makedrink() {
//         boil();
//         brew();
//         pourincup();
//         putsomething();
//     }

// };

// class coffe :public abstractdrinking {
//     public:
//     //煮水
//     virtual void boil() {
//         cout << "农夫山区" << endl;
//     }

//     // 冲泡
//     virtual void brew() {
//         cout << "咖啡" << endl;
//     }

//     //倒入杯中
//     virtual void  pourincup() {
//         cout << "冲泡" << endl;
//     }

//     //加入辅料
//     virtual void putsomething() {
//         cout << "加入奶" << endl;
//     }
// };

// class tea :public abstractdrinking {
//     public:
//     //煮水
//     virtual void boil() {
//         cout << "煮水" << endl;
//     }

//     // 冲泡
//     virtual void brew() {
//         cout << "咖啡" << endl;
//     }

//     //倒入杯中
//     virtual void  pourincup() {
//         cout << "冲泡" << endl;
//     }

//     //加入辅料
//     virtual void putsomething() {
//         cout << "加入枸杞" << endl;
//     }
// };


// //制作函数
// void dowork(abstractdrinking * abs) {
//     abs->makedrink();
//     delete abs; //释放

// }
// void test01() {
//     //堆区的数据手动开启手动释放
//     dowork(new coffe);

//     cout << "-----------------" << endl;
//     //制作茶叶
//     dowork(new tea);
// }

// int main() {
//     test01();
//     system("pause");
//     return 0;
// }

// 4.7.5 虚析构于纯虚析构

// 多态使用时，如果子类中有属性开辟到堆区，那么父类指针在释放时无法调用到子类的析构代码

// 解决方式：将父类中的析构函数改为虚析构或者纯虚析构

// 虚析构和纯虚析构共性：
//  - 可以解决父类指针释放子类对象
//  - 都需要具体的函数实现

// 虚析构和纯虚析构区别
//  - 如果是纯虚析构，该类属于抽象类，无法实例化对象

// 虚析构语法：
// virtual ~类名() {}

// 纯虚析构语法
// virtual ~类名()=0;

//虚析构和纯虚析构

// class animal {
//     public:
//     // 纯虚函数
//     animal() {
//         cout << "animal构造函数调用" << endl;
//     }
//     //利用虚析构可以解决父类指针释放子类对象时不干净的问题
//     // virtual ~animal() {
//     //     cout << "anima的析构函数调用" << endl;
//     // }
//     //纯虚析构  需要声明也需要实现
//     // 有了纯虚析构之后，这个类也属于抽象类，无法实例化对象
//     virtual ~animal()=0;
//     //纯虚函数
//     virtual void speak()=0;

// };

// animal::~animal() {
//     cout << "animal的纯虚析构函数调用" << endl;
// }


// class cat :public animal {

//     public:

//     cat(string name) {
//         cout << "cat构造函数调用" << endl;
//         m_name=new string(name); 
//     }
//     virtual void speak() {
//         cout << *m_name << "小猫在说话" << endl;
//     }
//     ~cat() {
//         if(m_name!=NULL) {
//             cout << "cat析构函数调用" << endl;
//             delete m_name;
//             m_name=NULL;
//         }
//     }
//     string *m_name;
// };

// void test01() {
//     //多态
//     animal *Animal=new cat("Tome");
//     Animal->speak();

//     // 父类指针在析构的时候不会调用子类中析构函数，导致子类如果有堆区属性，出现内存泄漏
//     delete Animal;

// }

// int main() {
//     test01();
//     system("pause");
//     return 0;
// }

// 总结
//  1、虚析构或纯虚析构就是用来解决通过父类指针释放子类对象
//  2、如果子类中没有堆区数据，可以不写为虚析构或纯虚析构
//  3、拥有纯虚析构函数的类也属于抽象类


// 4.7.6 多态案例三 - 电脑组装
// 抽象出每个零件的类
// 电脑主要组成部件为CPU(用于计算)，显卡（用于显示），内存条（用于存储）
// 将每个零件封装出抽象基类，并且提供不同的厂商生产不同的零件，例如INtel厂商和lenovo厂商
// 创建电脑类提供让电脑工作的函数，并且调用每个零件工作的接口
// 测试时候组装三台不用的电脑工作

// 抽象不同零件类
// 抽象CPU类
class CPU {
    public:
    // 抽象的计算函数
    virtual void calculate()=0;

};

// 抽象显卡类
class videocard {
    public:
    // 抽象的显示函数
    virtual void display()=0;
    
};

// 抽象内存条
class memory {
    public:
    // 抽象的计算函数
    virtual void storage()=0;
    
};

// 电脑类

class computer {
    public:
    computer(CPU *cpu, videocard *VC,memory *mem) {
        m_cpu=cpu;
        m_VC=VC;
        m_mem=mem;
    }
    void work() {
        m_cpu->calculate();
        m_VC->display();
        m_mem->storage();

    }
    //提供析构函数，释放3个电脑零件
    ~computer() {
        //释放CPU零件
        if (m_cpu!=NULL) {
            delete m_cpu;
            m_cpu=NULL;
        }

        //释放CPU零件
        if (m_VC!=NULL) {
            delete m_VC;
            m_VC=NULL;
        }

        //释放CPU零件
        if (m_mem!=NULL) {
            delete m_mem;
            m_mem=NULL;
        }

    }

    private:
    CPU *m_cpu; //CPU的零件指针
    videocard *m_VC; //显卡的零件指针
    memory *m_mem; //内存条的零件指针

};

//具体的厂商
// intel厂商
class Intel_CPU: public CPU {
    public:
    virtual void calculate() {
        cout << "intel的CPU开始计算了！" << endl;
    }

};

class Intel_videaocard: public videocard {
    public:
    virtual void display() {
        cout << "intel的显卡开始显示了！" << endl;
    }

};


class Intel_memory: public memory {
    public:
    virtual void storage() {
        cout << "intel的内存条开始存储了！" << endl;
    }

};

// lenovo厂商
class lenovo_CPU: public CPU {
    public:
    virtual void calculate() {
        cout << "lenovo的CPU开始计算了！" << endl;
    }

};

class lenovo_videaocard: public videocard {
    public:
    virtual void display() {
        cout << "lenovo的显卡开始显示了！" << endl;
    }

};


class lenovo_memory: public memory {
    public:
    virtual void storage() {
        cout << "lenovo的内存条开始存储了！" << endl;
    }

};



// 组装不同的电脑
void test01() {
    //第一台电脑零件
    CPU *intelcpu=new Intel_CPU;
    videocard*intelcard=new Intel_videaocard;
    memory *intelmem=new Intel_memory;
    // 创建第一台电脑
    computer *computer1=new computer(intelcpu,intelcard,intelmem);
    delete computer1;

    // 第二台电脑组装
   cout << "第二胎电脑开始工作" << endl;
    computer *computer2=new computer(new lenovo_CPU,new lenovo_videaocard,new lenovo_memory);
    delete computer2;

}


int main() {
    test01();
    system("pause");
    return 0;
}