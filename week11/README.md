## Hash Table 與 Hash function 原理
HashTable是一種資料結構，把訊息或資料壓縮成摘要，使得資料量變小，將資料的格式固定下來，把key值依照hash後得到的index值，放入在各個table中，比如說我今天hash時是%10，那麼key:1006的index就是6，那麼我的table也要有0~9，10個去存放我的資料，假使現在有一個key值為2006，index與剛剛的1006一樣，那麼就把第二個進來的2006接在1006後面，將每個table裡的資料形成linkedlist接下去。HashFunction是將key值轉換成index值，例如現在我有8個table，那我可以把hash設定成取key%8的值為index，這樣經過%8後的值會有0,1,2,3,4,5,6,7，接著編好index後再使用hashset來add、remove、contains。因為此次作業有規定要用MD5去加密，所以在hash時要先將文字轉換成數字，才能去hash值得到index值
![image](https://github.com/hans0517/hans/blob/master/week11/HashTable.png,width="375")
