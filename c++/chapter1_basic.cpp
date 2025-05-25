

#include <iostream>
#include <string>
#include <windows.h>
using namespace std;


// 1. switch语句

// int main() {
//     //switch语句
//     //给一个电影进行打分
//     // 1~9:经典
//     //8~7：非常好
//     //6~5：一般
//     //0~4：烂片

//     //1.提示用户给电影评分
//     cout << "请给电影进行评分：" << endl;

//     //2. 用户开始进行打分
//     int score=0;  //定义一个变量用于接受用户输入的分数
//     cin >> score; //用户输入分数
//     cout << "您打的分数为：" << score << endl;  
//     //3. 打分完毕后，显示电影评分

//     switch (score)
//     {
//         case 10:
//             cout << "您认为是经典电影" << endl;
//             break;
//         case 9:
//             cout << "您认为是经典电影 " << endl;
//             break;
//         case 8:
//             cout << "您认为是非常好的电影" << endl;
//             break;
//         case 7:
//             cout << "您认为是非常好的电影" << endl;
//             break;
//         case 6:
//             cout << "您认为是一般的电影" << endl;
//             break;
//         default:
//             cout << "您认为是烂片" << endl;
//             break;

//     }
//     system("pause");
//     return 0;
// }

// 2. while循环
// int main() {
//     //while循环
//     //在屏幕中国打印0~10个数
//     int num=0;
//     // cout << num << endl;
//     // num++;
//     // cout << num << endl;
//     while (num<=10)
//     {
//         cout << num <<endl;
//         num++;
//     }
//     system("pause");
//     return 0;
// }

// 3. do...while循环
//与while的区别在于do..while会先执行一次再判断循环条件
// int main() 
// {
//     // 再屏幕中国输出0~9个数字
//     int num=0;
//     do
//     {
//         cout << num << endl;
//         num++;
//     } while (num<10);
//     system("pause");
//     return 0;
// }

// 4. for循环
// int main() {
//     // for (int i=0;i<10;i++) {
//     //     cout << i << endl;
//     // }
//     int i=0;
//     for (;;)
//     {
//         if (i>=10) {
//             break;
//         }
//         cout << i <<endl;
//         i++;
//     }
//     system("pause");
//     return 0;
// }

// 5. 嵌套循环
// int main() {
//     // for (int i=0;i<10;i++) {
//     //     for (int j=0;j<10;j++) {
//     //         cout << "*" ;
//     //     }
//     //     cout << endl;
//     // }
//     int i=0;
//     for (;i<10;i++) {
//         int j=0;
//         for (;j<10;j++) {
//             cout << "*" ;
//         }
//         cout << endl;
//     }
//     system("pause");
//     return 0;
// }

// 6. break和continue
// int main() {
//     // 1. break的使用时机
//     // 1. 出现在switch语句中
//     // cout << "请选择副本的难度" << endl;
//     // cout << "1.普通" << endl;
//     // cout << "2.中等" << endl;
//     // cout << "3.困难" << endl;
//     // int select=0; //创建选择结果的变量
//     // cin >> select;
//     // switch (select) {
//     //     case 1:
//     //         cout << "您选择了普通难度" << endl;
//     //         break;
//     //     case 2:
//     //         cout << "您选择了中等难度" << endl;
//     //         break;
//     //     case 3:
//     //         cout << "您选择了困难难度" << endl;
//     //         break;
//     //     default:
//     //         break;
//     // }

//     // 2. 出现在循环语句中
//     // int i=0;
//     // for (;i<10;i++) {
//     //     cout << i << endl;
//     //     if (i==5) {
//     //         break;
//     //     }
//     // }
//     // 3. 出现在嵌套循环中
    
//     system("pause");
//     return 0;
// }

// 7. goto语句：直接跳转到指定的位置继续执行
// 因为太复杂不建议使用，影响代码的可读性
// int main() {
//     cout << "1" << endl;
//     cout << "2" << endl;
//     cout << "3" << endl;
//     goto FLAG;
//     cout << "4" << endl;
//     cout << "5" << endl;
//     FLAG:
//     cout << "6" << endl;
//     system("pause");
//     return 0;
// }

// 8. 数组
// 8.1 数组定义
// 数组的是一个集合，里面存放了相同类型的数据元素
// 特点1：数组中每个元素都是相同数据类型
//特点2：数组放在一块连续的内存空间中
//特点3：可以通过下表访问数组中的元素
// int main() {
//     //1. 数组的三种定义方式
//     //1.1 数据类型 数组名[数组的长度]
//     //1.2 数据类型 数组名[数组长度]={值1,值2,值3,...}  
//     //1.3 数据类型 数组名[]={值1,值2,值3,...}  //数组长度会根据初始化的值自动计算 

//     int score[1];
//     score[0]=100;
//     // cout << "数组中第一个元素" << score[0] << endl;
//     int score1[2]={100,200};
//     // cout << "数组中第一个元素" << score1[0] << endl;
//     int score2[]={100,200,300};
//     for (int i=0;i<3;i++) {
//         cout << "数组中第" << i+1 << "个元素" << score2[i] << endl;
//     }
//     system("pause");
//     return 0;
// }

// 8.2 数组名
// 作用： 1）可以统计整个数组再内存中的长度
// 2）可以获取数组在内存中的首地址
// int main() {
//     int arr[5]={1,2,3,4,5};
//     cout << "数组占用的内存空间为：" << sizeof(arr) << endl;  
//     cout << "数组中单个元素占用内存空间为" << sizeof(arr[0]) << endl;
//     cout << "数组中元素的个数为"  << sizeof(arr)/sizeof(arr[0]) << endl;
//     //（int）arr将首地址转换为十进制
//     cout << "数组的首地址为：" << (int)arr << endl; 
//     cout << "数组中第一个元素的地址为" << (int)&arr[0] << endl;
//     // 数组中的元素存储是联系徐的体现在第二个元素的地址减去第一个元素的地址等于数组的数据类型所占用的内存空间大小
    
//     //数组名是个常量，不可以进行赋值操作
//     // arr=100; // 错误
//     system("pause");
//     return 0;
// }

// 9二维数组
// 9.1定义方式
// int main() {
//     // 1. 数据类型 数组名[行数][列数]
//     // 2. 数据类型 数组名[行数][列数]={{值1,值2,值3},{值4,值5,值6}}
//     // 3. 数据类型 数组名[行数][列数]={值1,值2,值3,值4,值5,值6}
//     // 4. 数据类型 数组名[][列数]={值1,值2,值3,值4,值5,值6}    
//     // 1. 
//     int count[2][3]={{1,2,3},{4,5,6}};
//     for (int i=0;i<2;i++) {
//         for (int j=0;j<3;j++) {
//             cout << count[i][j] << endl;
//         }
//     }
//     system("pause");
//     return 0;
// }

// 8.2 二维数组的数组名
// 作用： 1）可以统计整个数组占用内存空间大小
// 2）可以获取数组在内存中的首地址
int main() {
    int count[2][3]={{1,2,3},{4,5,6}};  //int占用4个字节，总共占用4*6=24个字节
    cout << "二维数组占用的内存空间为"  << sizeof(count) << endl;
    cout << "第一行占用的内存为" << sizeof(count[0]) << endl;
    cout << "第一个元素占用的内存空间大小为" << size of(count[0][0]) << endl;
    cout << "二维数组中的行数为" << sizeof(count)/sizeof(count[0]) << endl;
    cout << "二维数组中的列数为" << sizeof(count[0])/sizeof(count[0][0]) << endl;
    cout << "二维数组的首地址为" << (int)count << endl;
    cout << "二维数组中第一个元素的地址为" << (int)&count[0][0] << endl; //int表示获取内存位置的整数表示，&表示取址符
    system("pause");
    return 0;
}