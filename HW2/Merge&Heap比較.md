# HeapSort&MergeSort的比較

* HeapSort
  * 重複從最大堆積取出數值最大的結點(把根結點和最後一個結點交換，把交換後的最後一個結點移出堆)

* MergeSort
  * 1.分割:遞迴地把目前序列平均分割成兩半
  * 2.在保持元素順序的同時將上一步得到的子序列合併

### 1.時間複雜度
* HeapSort的時間複雜度為 : O(NlogN)
* MergeSort的時間複雜度為 : O(NlogN)

### 2.空間複雜度
* HeapSort的空間複雜度為 : O(1)
* MergeSort的空間複雜度為 : O(N)

### 3.穩定性
* HeapSort ---> Unstable Sort
* MergeSort---> Stable Sort
----------------------------------------
* 以最差情況效率為O(NlogN)的演算法中，MergeSort的效率其實比HeapSort好
* 理論上HeapSort比MergeSort的速度還要快，雖然時間複雜度都為O(NlogN)，但是HeapSort是in-place的sorting，不耗費額外的記憶體， MergeSort則是每次方法調用的時候都需要記憶體的位置，所以HeapSort會比較快
----------------------------------------
* 在做MergeSort的時候會覺得比HeapSort好理解，因為HeapSort裡還包含了二元樹的概念，Merge需要的code也比較少就能完成，HeapSort則要先完成Heap才能去接著做HeapSort
* 雖然硬要比較兩者差異，但我覺得兩個都需要很多時間理解跟創作
