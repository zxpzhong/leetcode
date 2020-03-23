'''题目
小Q在进行一场竞技游戏,这场游戏的胜负关键就在于能否能争夺一条长度为L的河道,即可以看作是[0,L]的一条数轴。
这款竞技游戏当中有n个可以提供视野的道具−真视守卫,第i个真视守卫能够覆盖区间[xi,yi]。现在小Q想知道至少用几个真视守卫就可以覆盖整段河道。
输入包括n+1行。

第一行包括两个正整数n和L(1<=n<=105,1<=L<=109)

接下来的n行,每行两个正整数xi,yi(0<=xi<=yi<=109),表示第i个真视守卫覆盖的区间。 

一个整数，表示最少需要的真视守卫数量, 如果无解, 输出-1。

4 6
3 6
2 4
0 2
4 7

3

下面的程序通过率90%，有一个案例通不过不知道为什么？？？
'''
# texts = '''15486 34573 76633 78418 91686 118153 13125 20244 21606 47958 79010 91957 29146 55248 53011 72815 42238 53540 14239 25485 69273 69852 16897 32894 5353 34985 171723 190724 46902 63182 2577 9811 34550 55418 52481 57942 44245 72115 28748 53358 7817 8886 13225 38957 22540 30157 204574 228046 44951 58210 46541 70512 14675 30258 30396 35144 12766 13858 112751 119595 23 7545 33067 61517 10848 11656 10287 22378 261336 290979 31858 32761 28161 48070 38975 59135 33772 40076 42171 64330 14459 35913 19568 32225 22434 34075 4062 5749 63565 75814 30136 38199 134460 134660 12596 39873 107123 109018 87032 94456 10753 12670 432694 433736 47823 67671 37615 40677 47804 52182 53774 56465 43612 53302 71606 73144 61251 73750 45695 71844 1816 15331 313 11300 18456 27699 5237 20854 27866 44560 3611 15123 32362 37265 30575 48638 11273 13059 14798 33339 2074 20545 502 2941 44462 73449 39448 58132 28423 43296 83351 93025 5215 6641 7248 18896 7382 23943 19432 24887 12955 18127 44165 55396 18644 24427 12251 33458 16211 18690 4975 16056 2707 15104 16559 36063 11702 23486 27898 32028 20281 50023 43566 45999 48189 56086 20118 33212 95209 111938 34475 54755 81487 94426 45550 51182 7073 19056 34094 62629 9900 10712 110249 125036 26384 51909 88100 104051 60632 66836 1346 18849 3970 17215 10011 34666 31341 55805 43857 45537 1736 17646 9966 10638 10973 17049 42573 70349 43503 49571 24094 47973 31533 54625 8777 26951 16345 16899 41280 49604 1794 6621 14964 35584 343626 366063 20786 35855 43072 71896 101121 103368 82832 110529 7091 17575 6194 8790 4583 8269 59421 83517 14567 25781 14530 15216 9239 15836 14149 25879 15180 25712 50724 66047 10943 11104 12606 32439 147026 147395 30804 30805 10399 39175 74810 102435 43227 53087 36071 62841 13296 14263 80676 89780 1393 1492 30084 34013 3044 5775 66748 86025 5888 35774 90650 111137 69180 70727 55448 58277 33567 48734 28754 46437 17058 22450 48538 66973 8847 30186 28508 58472 45133 55925 13540 37828 7070 34210 6608 14448 68755 85820 14181 31584 7941 28249 59069 65455 3989 8987 67082 85504 4209 4909 18060 20912 93953 96347 27255 34853 48835 50167 93559 97260 68397 80413 55207 60644 29255 43472 8199 35908 23506 35078 2196 26348 28036 28355 68033 93814 12762 41324 52797 77042 13786 21459 35147 60098 26732 49568 84163 98774 36794 44284 33991 45905 45170 68992 120872 128737 26828 47841 121092 136844 37884 54296 152596 162757 3977 6263 43077 64276 18042 40019 2639 28973 56646 73052 41100 43770 60332 66189 89419 117475 24980 43335 47316 70208 81541 89340 21116 46600 4603 21858 34009 59502 69355 74461 20790 50350 46900 63904 33802 55263 6068 32274 86863 102350 37728 39255 21816 50530 7595 10248 10910 24004 45744 75048 651 1579 31580 60324 136624 156397 34026 34459 42291 70937 13665 18877 30372 54992 88027 94392 40167 44113 49546 71962 13334 42867 168 3297 90549 112999 37813 39778 30732 32723 45193 72125 46666 63362 62574 64057 1616 10348 11141 39838 13680 21568 63805 84688 120152 122578 2406 6244 3171 12144 19084 19533 21022 21334 6979 17319 17 2162 18371 38362 29056 57757 761 19662 28567 48655 6882 12275 4483 18673 82113 93371 14695 34720 12909 27102 1104 12278 86459 102367 1270 2354 1178 24509 31087 34863 11574 27841 152518 177557 33304 44895 5341 18323 22634 52137 79508 100025 18745 30825 32153 61123 15687 24623 76204 77282 3377 16851 176569 204930 38371 65573 4948 23698 17462 26280 148420 157730 38130 45726 16780 40878 8945 26843 172594 200690 934 8303 68990 81789 16184 44489 15605 22779 53057 79846 8672 31128 42022 59104 4541 10692 22791 50313 72817 98049 19324 20495 100018 129713 112249 112642 35000 57014 29249 43101 59197 71998 50627 71876 2235 13042 22405 42676 32921 35334 10194 27536 30557 32437 14564 27491 20980 23324 73011 83419 9698 21646 16201 44889 5621 9401 2994 18812 1957 2687 12731 15490 142746 150718 35510 41941 6730 27682 38845 59595 8128 14920 18333 26568 64392 71996 121288 122735 58786 82040 152278 171705 7141 34618 24232 34220 10655 38072 98579 124626 71448 73103 201026 203177 39082 61211 58400 84627 20357 35106 5748 22659 33891 61875 51797 72238 62583 71755 69172 92228 31466 55897 29233 40814 16535 32954 33661 35973 52215 54782 33841 51515 7615 20526 37304 45969 16965 39888 16266 18939 79148 85304 103883 105611 23773 47611 23367 45533 15680 45014 64306 69160 27237 49825 4634 11595 16146 20039 33912 54684 29807 32494 61708 69765 19465 45509 8193 11039 8400 28010 18996 44394 37101 42572 10944 29079 21488 22669 211285 211368 2429 7636 31376 48059 19088 39399 6891 27828 55923 76187 16091 18441 1456 2077 25795 50553 16459 38296 52705 63834 37935 38396 25370 25548 3813 19150 45864 75632 14340 14664 3884 11250 5708 7976 9330 19348 267179 275122 218434 224011 40767 52740 42157 48073 24892 25013 33251 44324 9325 15593 36425 57940 40322 50612 280 1176 131096 133007 40315 41656 71206 91372 23829 24127 19066 35908 53798 54282 9074 18587 15326 42989 28966 44814 13012 38610 67046 91874 12508 13175 111090 125193 38412 57195 9683 23487 50577 66567 55797 84215 16139 35801 33645 37851 72353 90598 7036 19257 1752 19412 11993 40546 195517 200825 33709 57505 8934 17155 111780 120334 4082 32581 15419 18734 88393 98570 17674 19921 7730 33808 54077 54919 30359 39292 5307 6227 11485 38491 8573 17173 21193 45700 20154 42932 49418 75923 57426 82142 10348 31198 22114 48128 17307 30161 225241 245223 40828 63268 2395 28293 67470 94934 18024 36577 14996 26666 58850 81231 344 13637 6660 22629 96054 122078 3744 25385 69794 96214 33776 54558 38713 40842 83186 83699 39727 41681 34746 50725 19773 28912 101046 129660 11406 14777 40197 62292 10302 14225 35243 52463 37351 37436 42468 64571 1522 11327 31131 50409 33848 44070 62243 87013 60797 74315 49005 69854 19874 21936 52717 75708 9175 25851 727 23571 78702 95488 23422 24995 17413 40879 15709 28369 51545 60862 30323 37876 5393 14272 4793 9088 96079 112523 58643 61309 13470 14368 39146 55774 25372 53376 12638 23807 138545 165520 92002 110927 19846 31521 39578 63432 34943 37387 19219 29677 24736 41667 22644 51519 35385 53739 44363 59335 8904 24380 56940 71522 72891 77638 4347 7023 36886 65763 39548 62599 38414 52170 4872 23890 20698 42850 24292 51392 9350 12176 57801 73173 13406 42486 48267 69875 1975 11018 11896 13069 6310 14270 48222 75596 10691 13588 30101 57016 70425 72132 47369 70676 6262 15598 37897 57561 29492 31955 38132 39372 11184 34086 47671 67664 35225 36815 68882 80379 22984 39366 1433 26528 36856 58561 6531 15561 24975 50149 22199 26696 23667 26159 67266 85342 6876 7081 28012 37043 101309 101574 37464 51406 22462 39937 5281 6941 5069 12956 37538 38338 55968 75065 44322 60212 142927 145074 63842 65045 64098 88866 32495 56483 26727 46799 21917 39055 95028 105768 73337 101421 7417 33725 34993 36002 15575 29448 66700 88533 14963 31859 41543 68269 56680 59389 61395 74153 4450 30768 73401 98682 1109 30247 22200 23551 15042 17085 15088 40741 3350 10881 33870 55539 14988 36744 30977 42552 44397 53695 53192 58217 39450 48378 25392 25864 56538 58184 58415 67135 55821 63881 42016 43558 77281 99400 34050 36349 9094 16603 68415 93978 910 2306 32458 49783 33483 61068 69861 77628 13521 34728 6341 27463 64763 92307 31999 42441 35489 42950 12889 30183 20267 28124 26493 35165 82143 90395 242'''.split(' ')
# texts = [texts[i:i+2] for i in range(len(texts)//2)]

import sys 
texts = []
n,L = list(map(int,sys.stdin.readline().strip().split()))
for line in sys.stdin:
    texts.append(line.split())
for i in range(len(texts)):
    for j in range(len(texts[0])):
        texts[i][j] = int(texts[i][j])
starts = [texts[i][0] for i in range(len(texts))]
end = [min(L,texts[i][1]) for i in range(len(texts))]
from operator import itemgetter
index = [index for index, value in sorted(enumerate(starts), key=itemgetter(1))]
starts.sort()
end = [end[index[i]] for i in range(len(end))]
if not starts[0] == 0:
    print(-1)
    exit()
ans = 0
y = 0
y_next = 0
i = 0
while i < len(starts):
    # 包含y且最远的
    if  starts[i] <= y:
        y_next = max(y_next,end[i])
        i+=1
        continue
    elif end[i] > y_next:
        # 更新y
        y = y_next
        ans+=1
        continue
    i+=1
print(ans+1)