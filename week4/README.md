# QuickSort
* QuickSort(快速排序法):在數列中任意挑選一個數，稱為pivot，然後調整數列，使得「所有在pivot左邊的數，都比pivot還小」，而「在pivot右邊的數都比pivot大」，接著將所有在pivot左邊的數視為「新的數列」，所有在pivot右邊的數視為「另一個新的數列」，「分別」重複上述步驟(選pivot、調整數列)，直到分不出「新的數列」為止。
## QuickSort流程圖
![image](https://github.com/hans0517/hans/blob/master/week4/QuickSortpic100.png)
# InsertionSort
* 學習網站 : http://notepad.yehyeh.net/Content/Algorithm/Sort/Insertion/1.php
* 簡介
  * InsertionSort是將資料分成已排序、未排序兩部份依序由未排序中的第一筆(正處理的值)，插入到已排序中的適當位置，插入時由右而左比較，直到遇到第一個比正處理的值小的值，再插入，比較時，若遇到的值比正處理的值大或相等，則將值往右移。
* 時間複雜度
  * Best : Ο(1)
    * 當資料的順序恰好為由小到大時，每回合只需比較1次
  * Worst : Ο(n2)
    * 當資料的順序恰好為由大到小時，第i回合需比i次
  * Average : Ο(n2)
    * 第n筆資料，平均比較n/2次
