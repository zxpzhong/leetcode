#include <iostream>
#include <cstdio>
#include <cstring> 
using namespace std;
#define ll long long 
#define N 200005
int n;
ll a[N], t[N], left1[N], right1[N], left2[N], right2[N];
ll lowbit(int x)
{
    return x & (-x);
}
void add(int x, int y)
{
    for(int i = x; i <= n; i += lowbit(i))
    {
        t[i] += y;
    }
}
ll getsum(int x)
{
    ll ans = 0;
    for(int i = x; i; i -= lowbit(i))
    {
        ans += t[i]; 
    }
    return ans;
} 
int main(){
    scanf("%d", &n); 
    // mx为最大值
    ll mx = 0;
    for(int i = 1; i <= n; ++i)
    {
        scanf("%d", &a[i]);
        mx = max(mx, a[i]); 
    }
    // 置0
    memset(t, 0, sizeof(t));
    // 获取每个数右边比他大/小的个数
    for(int i = n; i > 0; --i)
    {
        // 区间求和，a[i]~n区间
        right1[i] = getsum(n) -  getsum(a[i]);
        right2[i] = getsum(a[i] - 1);
        add(a[i], 1);
    }
    memset(t, 0, sizeof(t));
    long long ans1 = 0, ans2 = 0;
    // 获取每个数左边比他大/小的个数
    for(int i = 1; i <= n; ++i)
    {
        left1[i] = getsum(n) - getsum(a[i]);
        left2[i] = getsum(a[i] - 1);
        add(a[i], 1);
        ans1 += left1[i] * right1[i];
        ans2 += left2[i] * right2[i];
    }
    /*for(int i = 1; i <= n; ++i)
    {
        printf("%d  %d %d %d %d\n", i, left1[i], right1[i], left2[i], right2[i]);
    }*/
    printf("%lld %lld\n", ans1, ans2);
    return 0;
} 