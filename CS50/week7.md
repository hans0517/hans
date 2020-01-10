## Linked List

## HashTable
在做資料處理時，常常需要「查詢資料」，譬如線上購物平台有會員登入時，首先確認輸入的帳號密碼是否在資料庫裡，如果是，便從資料庫裡找出此會員的資料，
如購物記錄、暫存購物清單等等。

Chaining的概念


如果利用Division Method實作Hash Function：h(Key)=Keymodm，若選擇m=6，那麼對於Key為14,16,26,36,47,50,71,90的item，
進行Hashing後將會有如圖一的Collision發生。解決的辦法，就是將被分配到同一個slot的item用Linked list串起來，這就是Chaining。

![image](https://github.com/hans0517/hans/blob/master/images/CS50-6.png)

## Insert：
先利用Hash Function取得Table的index。

接著，只要在每一個slot的list之front加入item，即可保證在O(1)的時間複雜度完成。

## Search：

先利用Hash Function取得Table的index。

再利用Linked list的traversal尋找item。

## Delete：

先利用Hash Function取得Table的index。

再利用Linked list的traversal尋找欲刪除的item。
