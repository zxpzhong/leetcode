#include<iostream>
using namespace std;

typedef unsigned long long ULL;     //由于前缀值的值会很大 所以应该将数组中的数据定义为ULL型

const int N=1e5+10;
const int  P=131;       //P为权重
                        //131为经验值 即P=131或13331时 哈希冲突的可能性最小

int n,m;

char str[N];
ULL h[N];              //h[]存放字符串的前缀值
ULL p[N];             //p[]存放各个位数的相应权值

ULL get(int l,int r)
{
    return h[r]-h[l-1]*p[r-l+1];        //这步其实是将h[l-1]左移
}                                       //其目的事实上是为了将h[l-1]的高位与h[r]相对齐从而才可以未完成计算
int main()
{
    scanf("%d%d%s",&n,&m,str+1);

    p[0]=1;                         //注意这步千万不要忘了 最开始的权值必须赋值为1 否则接下来就会出错
    for(int i=1;i<=n;i++)
    {
        p[i]=p[i-1]*P;              //计算每个位上的相应权值
        h[i]=h[i-1]*P+str[i];       //计算字符串前缀值
                                    //最新加入的数的权值为p的0次 所以直接加上str[i]即可
    }
    while(m--)
    {
        int l1,r1,l2,r2;
        scanf("%d%d%d%d",&l1,&r1,&l2,&r2);
        if(get(l1,r1)==get(l2,r2)) puts("Yes");
        else puts("No");
    }

    return 0;
}