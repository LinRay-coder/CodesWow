#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    srand(time(0)); // 初始化随机种子
    int score = 0;
    int m = 0;
    cout << "===== 小猫钓鱼游戏开始啦！=====" << endl;
	
    for(int i=1; i<=100; i++){
    	getchar();
    	
        int luck = rand()%100; // 生成0-99的随机数
        
        // 钓鱼结果判断
        if(luck < 46) {         // 46%概率：小鱼
            cout << "钓到小鱼！+1分" << endl;
            score +=1;
        }
        else if(luck < 56) {    // 10%概率：中鱼
            cout << "钓到中鱼！+3分" << endl;
            score +=3;
        }
        else if(luck < 66) {   // 10%概率：大鱼
            cout << "哇！钓到大鱼！+10分" << endl;
            score +=10;
        }
        else if(luck < 80) {   // 14%概率：毛爷爷 
            cout << "哇！钓到毛爷爷照片啦！+10元" << endl;
            m +=10;
        }
        else if(luck < 94) {   // 14%概率：阎王爷 
            cout << "哇！钓到阎王爷照片啦！-10元" << endl;
            m -=10;
        }
        else if(luck < 97) {   // 3%概率：钻石碎片 
            cout << "哇！钓到钻石碎片啦！+100元" << endl;
            m +=100;
        }
        else 
		{   // 3%概率：人民碎片 
            cout << "哇！钓到人民碎片！快报警！-100元" << endl;
            m -=100; 
    	}

        // 绘制动态进度条
        cout << "第" << i << "次钓鱼：[";
        for(int j=0; j<i; j++) cout << "~"; // 用符号表示进度
        cout << "] 分数：" << score <<" money：" << m << endl << endl;
    }

    // 最终评价系统
    cout << "======== 游戏结束 ========" << endl;
    cout << "最终得分：" << score << " → "<< m << " → ";
    if(m >= 100&&score >= 300)  cout << "牛逼！钓鱼大师！";
    else if(m >= 100&&score >= 200)  cout << "牛逼！优秀钓手！";
    else if(m >= 100&&score >= 100)  cout << "牛逼！新手渔民！";
    else if(m >= 100&&score >= 10)  cout << "牛逼！要练习哦！";
    else if(m >= 0&&score < 0)  cout << "傻逼！";
    else if(m <= 100&&score >= 300)       cout << "钓鱼大师！";
    else if(m <= 100&&score >= 200) cout << "优秀钓手！";
    else if(m <= 100&&score >= 100)  cout << "新手渔民！";
    else if(m <= 100&&m >= 100)  cout << "牛逼！";
    else                  cout << "要练习哦！";
    return 0;
}
