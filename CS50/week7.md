## Linked List
首先，需要有一個指針指向列表的第一個元素，知道鍊錶從哪兒開始的。然後，每個元素除了數據域存儲數據，還有指針域指向下一個元素。然後，不需要連續的存儲空間，只要有指針存儲下一個元素的地址就行。鍊錶的最後一個元素指針指向Null，標誌這鍊錶的結尾

![image](https://github.com/hans0517/hans/blob/master/images/CS50-2.png)

例如，如果要在上述鍊錶中搜索一個元素02：首先通過頭指針查看頭指針指向的元素值是否等於02，發現不等於，查看指針指向的下一個元素值是否等於02，最後發現有個元素等於02，返回True。如果直到指針指向Null，都沒有發現搜索元素，返回False。


鍊錶中增加元素（到鍊錶開頭），如下圖：複製頭指針的地址，使要增加的元素同樣指向第一個元素。使頭指針指向要增加的這個元素。

![image](https://github.com/hans0517/hans/blob/master/images/CS50-3.png)
![image](https://github.com/hans0517/hans/blob/master/images/CS50-4.png)

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
