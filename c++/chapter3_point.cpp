#include <iostream>
#include <string> //后面使用字符串需要引入这个头文件
using namespace std;


//1. 指针
// 1.1 指针的基本概念
// 指针的作用：可以通过指针简洁访问内存
// 内存编号是从0开始记录的，一般用十六进制数字表示
// 可以利用指针变量保存地址

// int main() {
//     // 1. 定义指针
//     // 指针定义的语法：数据类型*指针变量名
//     int a=10;
//     int*p;
//     p=&a;
//     cout << "a的地址为" << &a << endl;
//     cout << "指针变量p值为" << p << endl;
//     // 让指针记录变量a的地址
//     // 2. 使用指针
//     // 可以通过解引用的方式来找到指针指向的内存
//     // 指针前加*代表解引用，找到指针指向的内存中的数据
//     *p =1000;// 找到p指向的内存,这样可以修改只想内存中的数值，此时a=1000;
//     cout << "a=" << a << endl;
//     cout << "*p=" << *p << endl;
//     system("pause");
//     return 0;
// }

// 1.2 指针所占用的内存空间:所有指针在32位操作系统中都是占用4个字节的内存，64位下占用8个内存
// int main() {
//     int a=10;
//     int*p;
//     p=&a;
//     cout << "sizeof(int *)=" << sizeof(int *) << endl;
//     cout << "sizeof(float *)=" << sizeof(float *) << endl;
//     cout << "sizeof(double *)=" << sizeof(double *) << endl;
//     cout << "sizeof(char *)=" << sizeof(char *) << endl;

// }

// 1.3 空指针和野指针
// 空指针：指针变量指向内存中编号为0的空间
// 用途：初始化指针变量
// 注意：空指针指向的内存是不可以访问
// int main() {
//     int *p=NULL;
//     // *p=100; // 空指针是不可以访问的
//     // 0~255之间的内存编号是系统占用的，因此不可以访问
//     cout << "p=" << *p << endl;

//     system("pause");
//     return 0;
// }

// 野指针：指针变量指向非法的内存空间
// int main() {
//     // 野指针：不能访问未授权的内存空间
//     int *p=(int *)0x1100;  // 非法的内存空间
//     cout << "p=" << *p << endl;
//     system("pause");
//     return 0;
// }


// 1.4 const修饰指针
// const修饰指针有三种情况
// 1. const修饰指针：常量指针（指针指向可以修改，但是指针指向的值不可以修改）
// 2. const修饰常量：指针常量（指针指向不可以修改，但是指针指向的值可以修改）
// 3. const既修饰指针又修饰常量(指针指向和指针指向的值都不可以修改)
// int main() {
//     int a=10;
//     int b=20;
//     //1. const修饰指针
//     const int*p=&a;
//     p=&b; // 指针指向可以修改
//     // *p=100; // 指针指向的值不可以修改

//     //2. const修饰的常量
//     int *const p2=&a;
//     *p2=100; // 指针指向的值可以修改
//     //p2=&b; // 指针指向不可以修改

//     //3. const修饰指针和常量
//     const int *const p3=&a;
//     // *p3=100; // 指针指向的值不可以修改
//     // p3=&b; // 指针指向不可以修改

//     system("pause");
//     return 0;
// }

// 1.5 指针和数组
// int main() {
//     // 利用指针访问数组中的元素
//     int arr[10]={1,2,3,4,5,6,7,8,9,10};
//     cout << "第一个元素为" << arr[0] << endl;
//     int *p=arr;  //arr就是数组的首地址
//     int *p1=arr;
//     cout << "利用指针访问第一个元素" << *p << endl;
//     p++; // 让指针向后偏移4个字节,因为指针中存储的数据是有序的，一个int型占四个字节
//     cout << "利用指针访问第二个元素" << *p << endl;
//     cout << "利用指针变量数组" << endl;
//     for (int i=0;i<10;i++) {
//         cout << *p1 << endl;
//         p1++;
//     }
//     system("pause");
//     return 0;
// }

// 1.6 指针和函数
// 实现两个数字进行交换，这里在值传递的时候原来的值也发生了改变
// void swap(int *p1,int *p2) {
//     int temp=*p1;
//     *p1=*p2;
//     *p2=temp;
// }

// int main() {
//     int a=10;
//     int b=20;
//     int *p=&a;
//     int *p2=&b;
//     // 地址传递可以修改实参
//     swap(p,p2);
//     cout << "a=" << a << endl;
//     cout << "b=" << b << endl;
//     system("pause");
//     return 0;
// }

// 2. 结构体
// 结构体属于用户自定义的数据类型，允许用户存储不同的数据类型
// 结构体的定义：struct 结构体名{成员列表}
// 通过结构体创建变量的方式有三种：
// 1. struct 结构体名 变量名
// 2. struct 结构体名 变量名={成员列表}
// 3. struct 结构体名{成员列表} 变量名

//1. 创建学生数据类型：学生包括姓名、年龄、分数
// 自定义数据类型，一些类型集合组成的一个类型
// 语法 struct 类型名称 {成员列表}

// 定义结构体
// struct student {
//     //成员列表
//     //姓名
//     string name;

//     //年龄
//     //分数
//     int age;
//     int score;
// };


// // 创建结构体
// int main() {
//     //2. 通过学生类型创建具体的学生
//     // 2.1 struct student st1;
//     //
//     struct student s1;
//     s1.name="张三";
//     s1.age=18;
//     s1.score=100;
//     cout << "姓名：" << s1.name << " 年龄：" << s1.age << " 分数：" << s1.score << endl;
//     // 2.2 struct student st2={"张三",18,100};
//     struct student s2={"李四",19,99};
//     cout << "姓名：" << s2.name << " 年龄：" << s2.age << " 分数：" << s2.score << endl;
//     // 2.3在定义结构体时顺便创建结构体变量
//     struct student {
//         string name;
//         int age;
//         int score;
//     } s3={"王五",20,98};   

//     system("pause");
//     return 0;
// }


// 2.2 结构体数组
// 作用：将自定义的结构体放入到数组中方便维护
// 语法：instruct 结构体名 数组名[元素个数]={结构体1，结构体2，结构体3}

//1. 定义结构体
// struct student {
//     string name;
//     int age;
//     int score;
// };


// int main() {
//     //2. 创建结构体数组
//     struct student stuarr[3]={
//         {"张三",18,100},
//         {"李四",19,99},
//         {"王五",20,98}
//     };
//     //3. 结构体数组中的元素赋值
//     stuarr[2].name="赵六";
//     stuarr[2].age=21;
//     stuarr[2].score=97;

    
//     //遍历结构体中的数组
//     for (int i;i<3;i++) {
//         cout << "姓名：" << stuarr[i].name << " 年龄：" << stuarr[i].age << " 分数：" << stuarr[i].score << endl;
//     }
//     system("pause");
//     return 0;
// }

// // 2.3 结构体指针
// // 通过指针访问结构体中的成员
// // 利用操作符->可以通过结构体指针访问结构体属性


// // 创建结构体
// struct student {
//     string name;
//     int age;
//     int score;
// };

// int main() {
//     //创建学生结构体变量
//     struct student s={"张三",18,100};
//     // 通过指针指向结构体变量
//     struct student *p=&s;
//     // 通过结构体指针访问结构体属性
//     cout << "name" << p->name << " age" << p->age << " score" << p->score << endl;

//     system("pause");
//     return 0;
// }

// 2.4 结构体嵌套结构体
// 结构体中可以嵌套其他结构体
// struct student {
//     string name;
//     int age;
//     int score;
// };


// struct teacher {
//     int id;
//     string name;
//     int age;
//     struct student s;
// };

// int main() {
//     struct teacher t={1,"老王",30,{"张三",18,100}};
//     cout << "老师的id为" << t.id << " 姓名为" << t.name << " 年龄为" << t.age << " 学生姓名为" << t.s.name << " 年龄为" << t.s.age << " 分数为" << t.s.score << endl;
//     system("pause");
//     return 0;
// }


// 2.5 结构体作为函数的参数

//定义结构体变脸
// struct student {
//     string name;
//     int age;
//     int score;
// };

// // 打印学生信息的函数
// // 值传递
// void printstudent(struct student s) {
//     s.age=200;
//     cout << "name" << s.name << "age" << s.age << "score" << s.score << endl;
// }

// // 地址传递
// void printstudent2(struct student *s) {
//     s->age=200;
//     cout << "子函数2中 姓名" << s->name << " 年龄" << s->age << " 分数" << s->score << endl;
// };

// int main() {
//     struct student s={"张三",18,100};
//     printstudent(s);
//     // cout << "姓名：" << s.name << " 年龄：" << s.age << " 分数：" << s.score << endl;
//     printstudent2(&s);
// }

// 2.6结构体中const使用方法

//定义结构体
// struct student {
//     string name;
//     int age;
//     int score;
// };

// //对于结构体作为函数值传递，，可以将函数中的形参改为指针，这样可以减少内存空间，而且不会复制新的副本。
// void printstudents(const student *s) {
//     // s->age=200; // const修饰的结构体指针不可以修改结构体中的值,这样可以防止误操作的错误
//     //s->age=200;  
//     cout << "name" << s->name << " age" << s->age << " score" << s->score << endl;
// };

// int main() {
//     struct student s={"张三",18,100};
//     // 通过函数打印结构体变量信息
//     printstudents(&s);
//     cout << "zhangsan的年龄为" << s.age << endl;

//     system("pause");
//     return 0;
    
// }


// 2.7结构体案例
// 每名老师带领5个学生，总共有3个老师，需求如下：
//设计老师和学生的结构体，其中，再老师的结构体中，有老师姓名和一个存放5名学生的数组作为成员
// 学生的成员有姓名、考试分数，创建数组存放3名老，通过函数给每个来时及所待的学生复制
//最终打印老师的数据及老师所带的学生

// #include <iostream>
// using namespace std;
// #include <string>
// #include <ctime>
// //学生结构体定义
// struct student {
//     //姓名
//     string tName;
//     //分数
//     int score;

// };
// // 老师结构体定义

// struct teacher{
//     // 老师姓名
//     string tname;
//     //学生数组
//     struct student sArray[5];
// };

// // 给老师和学生观赋值的函数
// void allocatespce(struct teacher tArray[],int len ) {
//     string nameSeed="ABCDE";

//     for (int i=0; i<len; i++) 
//     {

//         tArray[i].tname="Teacher_"; // 老师姓名
//         tArray[i].tname+=nameSeed[i]; // 老师姓名
//         // 通过循环给每名老师带的学生进行赋值
//         for (int j=0; j<5; j++) {
//             tArray[i].sArray[j].tName="Student_"; // 学生姓名
//             tArray[i].sArray[j].tName+=nameSeed[j]; // 学生姓名
//             int randomScore=rand()%61+40; // 随机分数40~100
//             tArray[i].sArray[j].score=randomScore; // 学生分数
//         }
//     }
    

// }
// // 打印所有信息的函数
// void printInfo(struct teacher tArray[],int len) {
//     // 遍历老师数组

//     for (int i=0; i<len; i++) {
//         cout << "老师姓名：" << tArray[i].tname << endl;

//         for (int j=0; j<5; j++) {
//             cout << "\t学生姓名：" << tArray[i].sArray[j].tName << " 分数：" << tArray[i].sArray[j].score << endl;
//         }

//     }

    
// }

// int main() {
//     // 随机数种子
//     srand((unsigned int)time(NULL)); // 随机数种子

//     // 1. 创建3名老师的数组
//     struct teacher tArray[3];

//     // 2. 通过函数给3名老师的信息复制，并给老师带的学生信息复制
//     int len=sizeof(tArray)/sizeof(tArray[0]);

//     allocatespce(tArray,len);

//     //3. 打印所所有老师及所带的学生信息
//     printInfo(tArray,len);
//     system("pause");
// }


// 案例2

//设计一个英雄结构体，包括成员姓名、年龄、性别结构体是古族，数组中存放5名英雄
//通过冒泡排序算法，将数组中的英雄按照年龄进行升序排序，最终打印排序后的结果
#include <iostream>
using namespace std;

struct hero {
    // 姓名
    string name;
    // 年龄
    int age;
    //姓名
    string sex;

};

// 冒泡排序函数
void bubblesort(struct hero heroarray[],int len) {
    for (int i=0; i<len-1; i++) {
        for (int j=0; j<len-i-1; j++) {
            if (heroarray[j].age>heroarray[j+1].age) {
                // 交换两个英雄的顺序
                struct hero temp=heroarray[j];
                heroarray[j]=heroarray[j+1];
                heroarray[j+1]=temp;
            }

        }

    }
}
void printhero(struct hero heroarray[], int len) {
    for (int i=0; i<len; i++) {
        cout << "姓名：" << heroarray[i].name << "年龄：" << heroarray[i].age << "性别："  << heroarray[i].sex << endl;

    }
}
int main() {
    // 1. 设计英雄的结构体
    
    // 2. 创建一个数组存放5名英雄
    struct hero heroarray[5]=
    {
        {"张三",18,"男"},
        {"李四",19,"女"},
        {"王五",20,"男"},
        {"赵六",21,"女"},
        {"钱七",22,"男"}
    };
    int len=sizeof(heroarray)/sizeof(heroarray[0]);
    for (int i=0; i<<len; i++) {
        cout << "姓名：" << heroarray[i].name << "年龄：" << heroarray[i].age << "性别："  << heroarray[i].sex << endl;

    }
    //3. 对数组进行排序，按照年龄进行升序排序
    bubblesort(heroarray,len);
    // 4. 将排序后的结果打印
    printhero(heroarray,len);
    system("pause");
    
};
