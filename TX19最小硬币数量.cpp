#include <iostream>
#include <algorithm>

using namespace std;

const int N = 100;
int m, n;
int a[N]; // 存n种不同的面值

// 思路：每次有大面值的硬币时，我们用大面值硬币，这样范围更大，目标是凑a[n] - 1;
int main()
{
    //读入数据
    cin >> m >> n;
    for (int i = 0; i < n; i ++ ) cin >> a[i];

    // 给面值从小到大排序
    sort(a, a + n);
    //如果面值之中没有1，那么无法实现拼凑， 输出-1
    if (a[0] != 1) cout << -1 << endl;
    else
    {
        // 删除面值大于m的硬币，没有用
        while (n > 0 && a[n - 1] > m) n -- ;
        a[n] = m + 1; // 为了求a[n] - 1, 我们把m当成它，问题转化成给从0 ~ n-1种硬币，凑出a[n] - 1

        int res = 0;
        for (int i = 0, s = 0; i < n; i ++ ) 
        {
            //求每次a[i]需要多少个
            int k = (a[i + 1] - s - 1 + a[i] - 1) / a[i]; // k * a[i] + s >= a[i+1] - 1;
            s += k * a[i]; // 如何求s？ s是除了a[i]外，所有已知零钱的sum, 每次用k * a[i]更新
            res += k; //更新结果
        }

        cout << res << endl;    
    }

    return 0;
}