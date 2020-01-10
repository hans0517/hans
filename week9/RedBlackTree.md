# RedBlackTree
其實RBT就是BST的延伸，RBT多了旋轉，需要標顏色、也要平衡

若是要應用在BST上，則Rotation(旋轉)前後的BST必須要維持相同之Key排序。此處介紹的Rotation(旋轉)便屬於此類。

Rotation(旋轉)與node是否具有顏色無關，即使是在一般的BST，亦能夠使用Rotation(旋轉)來調整height(樹高)。

Reference : http://alrightchiu.github.io/SecondRound/red-black-tree-rotationxuan-zhuan.html

* 紅黑樹的特徵:
  * 節點都有顏色(紅/黑)
  * 在插入和刪除的過程中, 要遵循保持這些顏色的不同排列的規則
  * 紅黑樹的規則(紅黑規則):
    * 每個節點不是紅就是黑的(廢話)
    * 根總是黑色的
    * 若節點是紅色的, 則其子節點必為黑色, 反之不必為真(亦即若節點是黑色, 則其子節點可為紅也可為黑), 這條規則其實也是在說明就垂直方向來看, 紅色節點不可以相連
    * 每個空子節點都是黑色的: 所謂的空子節點指的是, 對非葉節點而言, 本可能有, 但實際沒有的那個子節點. 譬如一個節點只有右子節點, 那麼其空缺的左子節點就是空子節點
    * 從根節點到葉節點或空子節點的每條路徑(簡單路徑), 必須包含相同數目的黑色節點(這些黑色節點的數目也稱為黑色高度)

![image](https://github.com/hans0517/hans/blob/master/images/RBT.png)
