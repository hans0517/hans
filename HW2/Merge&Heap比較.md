# HeapSort&MergeSort的比較

### 1.時間複雜度
* HeapSort的時間複雜度為 : O(NlogN)
* MergeSort的時間複雜度為 : O(NlogN)

### 2.空間複雜度
* HeapSort的空間複雜度為 : O(1)
* MergeSort的空間複雜度為 : O(N)
----------------------------------------
* 以最差情況效率為O(NlogN)的演算法中，MergeSort的效率其實比HeapSort好
* 理論上HeapSort比MergeSort的速度還要快，雖然時間複雜度都為O(NlogN)，但是HeapSort是in-place的sorting，不耗費額外的記憶體， MergeSort則是每次方法調用的時候都需要記憶體的位置，所以HeapSort會比較快
----------------------------------------
在做MergeSort的時候會覺得比HeapSort好理解，因為HeapSort裡還包含了二元樹的概念，Merge需要的code也比較少就能完成，HeapSort則要先完成Heap才能去接著做HeapSort
