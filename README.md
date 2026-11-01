# Sorting-Algorithms
Implementations of classic sorting algorithms for Theory of Algorithms course.

Here I will write how each sorting algorithm works:

# 1. Insertion Sort

The Insertion Sort algorithm uses one part of the array to hold the sorted values, and the other part of the array to hold values that are not sorted yet.
The algorithm takes one value at a time from the unsorted part of the array and puts it into the right place in the sorted part of the array, until the array is sorted.

# How it works:

- Start with the second element as the first element is assumed to be sorted.
- Compare the second element with the first if the second is smaller then swap them.
- Move to the third element, compare it with the first two, and put it in its correct position
- Repeat until the entire array is sorted.

<img width="930" height="480" alt="image" src="https://github.com/user-attachments/assets/4ee2f1b2-48df-4cf0-9e97-6420b6e3000b" />

# Complexity Analysis of Insertion Sort
Time Complexity

Best case: O(n), If the list is already sorted, where n is the number of elements in the list.
Average case: O(n2), If the list is randomly ordered
Worst case: O(n2), If the list is in reverse orderComplexity Analysis of Insertion Sort
Time Complexity

Best case: O(n), If the list is already sorted, where n is the number of elements in the list.
Average case: O(n2), If the list is randomly ordered
Worst case: O(n2), If the list is in reverse order


# 2. Selection Sort

Selection Sort is a comparison-based sorting algorithm. It sorts by repeatedly selecting the smallest (or largest) element from the unsorted portion and swapping it with the first unsorted element.

# How it works:

- Find the smallest element and swap it with the first element. This way we get the smallest element at its correct position.
- Then find the smallest among remaining elements (or second smallest) and swap it with the second element.
- We keep doing this until we get all elements moved to correct position.

  <img width="1186" height="1027" alt="image" src="https://github.com/user-attachments/assets/2e6b84f2-d58a-4490-865f-81ef572eb077" />

# Complexity Analysis of Selection Sort
Time Complexity: O(n2) ,as there are two nested loops:

One loop to select an element of Array one by one = O(n)
Another loop to compare that element with every other Array element = O(n)
Therefore overall complexity = O(n) * O(n) = O(n*n) = O(n2)


# 3. Bubble Sort

Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. This algorithm is not efficient for large data sets as its average and worst-case time complexity are quite high.

Sorts the array using multiple passes. After the first pass, the maximum goes to end (its correct position). Same way, after second pass, the second largest goes to second last position and so on.
In every pass, process only those that have already not moved to correct position. After k passes, the largest k must have been moved to the last k positions.
In a pass, we consider remaining elements and compare all adjacent and swap if larger element is before a smaller element. If we keep doing this, we get the largest (among the remaining elements) at its correct position.

<img width="901" height="535" alt="image" src="https://github.com/user-attachments/assets/feefca47-2dd3-44e4-8832-df3f22e35808" />

# Complexity Analysis of Bubble Sort
Time Complexity: O(n2)
Auxiliary Space: O(1)

# Advantages:
Bubble sort is easy to understand and implement.
It does not require any additional memory space.
It is a stable sorting algorithm, meaning that elements with the same key value maintain their relative order in the sorted output.

# Disadvantages:
Bubble sort has a time complexity of O(n2) which makes it very slow for large data sets.
Bubble sort has almost no or limited real world applications. It is mostly used in academics to teach different ways of sorting.


# Heap Sort

Heap Sort is a comparison-based sorting algorithm based on the Binary Heap data structure.

It is an optimized version of selection sort.
The algorithm repeatedly finds the maximum (or minimum) element and swaps it with the last (or first) element.
Using a binary heap allows efficient access to the max (or min) element in O(log n) time instead of O(n).
The process is repeated for the remaining elements until the array is sorted.
Overall, Heap Sort achieves a time complexity of O(n log n).
Heap Sort Algorithm:
Here is an overview to sort an array in increasing order.

First convert the array into a max heap using heapify, Please note that this happens in-place. The array elements are re-arranged to follow heap properties.
Then one by one delete the root node of the Max-heap and replace it with the last node and heapify. Repeat this process while size of heap is greater than 1.

<img width="696" height="478" alt="image" src="https://github.com/user-attachments/assets/6f9eb3a3-1704-4a7d-a859-6ecc345e7b63" />

# Time Complexity: 
O(n log n)
# Auxiliary Space: 
O(log n), due to the recursive call stack. However, auxiliary space can be O(1) for iterative implementation.

# Advantages:
Efficient Time Complexity: Heap Sort has a guaranteed time complexity of O(n log n) in all cases, making it suitable for large datasets. The log n factor comes from the height of the binary heap, ensuring consistent performance.
Minimal Memory Usage: Heap Sort can work in-place with minimal extra memory. Using an iterative heapify() avoids additional stack space, so apart from storing the array itself, no extra memory is required.
Simplicity: Heap Sort is relatively easy to understand and implement compared to other efficient sorting algorithms, as it relies on the straightforward binary heap structure without advanced concepts like recursion (if iterative heapify is used).

# Disadvantages:
Costly: Heap sort is costly as the constants are higher compared to merge sort even if the time complexity is O(n log n) for both.
Unstable: Heap sort is unstable. It might rearrange the relative order.
Inefficient: Heap Sort is not very efficient because of the high constants in the time complexity.


# Merge sort

Merge sort is a popular sorting algorithm known for its efficiency and stability. It follows the Divide and Conquer approach. It works by recursively dividing the input array into two halves, recursively sorting the two halves and finally merging them back together to obtain the sorted array.

<img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/895f168d-6ec2-4f14-a74f-2dd97382bd12" />

Here's a step-by-step explanation of how merge sort works:

Divide: Divide the list or array recursively into two halves until it can no more be divided.
Conquer: Each subarray is sorted individually using the merge sort algorithm.
Merge: The sorted subarrays are merged back together in sorted order. The process continues until all elements from both subarrays have been merged.

Complexity Analysis of Merge Sort
# Time Complexity:

Best Case: O(n log n), When the array is already sorted or nearly sorted.
Average Case: O(n log n), When the array is randomly ordered.
Worst Case: O(n log n), When the array is sorted in reverse order.

# Auxiliary Space: 
O(n), Additional space is required for the temporary array used during merging.

# Applications of Merge Sort:
-Sorting large datasets
-External sorting (when the dataset is too large to fit in memory)
-Used to solve problems like Inversion counting, Count Smaller on Right & Surpasser Count
-Merge Sort and its variations are used in library methods of programming languages. Its variation TimSort is used in Python, Java Android and Swift. The main reason why it is preferred to sort non-primitive types is stability which is not there in QuickSort. Arrays.sort in Java uses QuickSort while Collections.sort uses MergeSort.
-It is a preferred algorithm for sorting Linked lists.
-It can be easily parallelized as we can independently sort subarrays and then merge.
-The merge function of merge sort to efficiently solve the problems like union and intersection of two sorted arrays.

# Advantages and Disadvantages of Merge Sort
# Advantages

Stability : Merge sort is a stable sorting algorithm, which means it maintains the relative order of equal elements in the input array.
Guaranteed worst-case performance: Merge sort has a worst-case time complexity of O(N logN) , which means it performs well even on large datasets.
Simple to implement: The divide-and-conquer approach is straightforward.
Naturally Parallel : We independently merge subarrays that makes it suitable for parallel processing.

# Disadvantages

Not an in-place, which means it requires additional memory to store the sorted data. This can be a disadvantage in applications where memory usage is a concern.
Slower than QuickSort in general as QuickSort is more cache friendly because it works in-place.


# Quick Sort

QuickSort is a sorting algorithm based on the Divide and Conquer that picks an element as a pivot and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array. .

There are mainly three steps in the algorithm:

Choose a Pivot: Select an element from the array as the pivot. The choice of pivot can vary (e.g., first element, last element, random element, or median).
Partition the Array: Re arrange the array around the pivot. After partitioning, all elements smaller than the pivot will be on its left, and all elements greater than the pivot will be on its right.
Recursively Call: Recursively apply the same process to the two partitioned sub-arrays.
Base Case: The recursion stops when there is only one element left in the sub-array, as a single element is already sorted.

<img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/ccbb98f7-e8f1-45e1-b701-ff49c9930e30" />

# Time Complexity:

Best Case: (Ω(n log n)), Occurs when the pivot element divides the array into two equal halves.
Average Case (θ(n log n)), On average, the pivot divides the array into two parts, but not necessarily equal.
Worst Case: (O(n²)), Occurs when the smallest or largest element is always chosen as the pivot (e.g., sorted arrays).

# Auxiliary Space:

Worst-case scenario: O(n) due to unbalanced partitioning leading to a skewed recursion tree requiring a call stack of size O(n).
Best-case scenario: O(log n) as a result of balanced partitioning leading to a balanced recursion tree with a call stack of size O(log n).
Please refer Time and Space Complexity Analysis of Quick Sort for more details.

# Advantages
It is a divide-and-conquer algorithm that makes it easier to solve problems.
It is efficient on large data sets.
It has a low overhead, as it only requires a small amount of memory to function.
It is Cache Friendly as we work on the same array to sort and do not copy data to any auxiliary array.
Fastest general purpose algorithm for large data when stability is not required.
It is tail recursive and hence all the tail call optimization can be done.

# Disadvantages
It has a worst-case time complexity of O(n2), which occurs when the pivot is chosen poorly.
It is not a good choice for small data sets.
It is not a stable sort, meaning that if two elements have the same key, their relative order will not be preserved in the sorted output in case of quick sort, because here we are swapping elements according to the pivot's position (without considering their original positions).
