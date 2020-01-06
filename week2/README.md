# LinkedList
* 學習網站 :
  * https://hackmd.io/@ofAlpaca/rkU9tZLK7?type=view
  * http://alrightchiu.github.io/SecondRound/linked-list-xin-zeng-zi-liao-shan-chu-zi-liao-fan-zhuan.html
# 簡介
* Linked list(連結串列)是一種常見的資料結構，其使用node(節點)來記錄、表示、儲存資料(data)，並利用每個node中的pointer指向下一個node，藉此將多個node串連起來，形成Linked list，並以NULL來代表Linked list的終點
![](https://github.com/hans0517/hans/blob/master/images/LL.png)
* **get(index)_**
  * 類似查詢的意思，找到index節點在LinkedList中的對應值
* **addAtHead(val)**
  * 從頭加入值為val的節點，新節點成為LinkedList中第一個節點
* **addAtTail(val)**
  * 從後面加入值為val的節點，新節點成為LinkedList中最後一個元素
* **addAtIndex(index, val)**
  * 把值為val的節點加入到指定位置index
* **deleteAtIndex(index)**
  * 刪除指定index節點之值
