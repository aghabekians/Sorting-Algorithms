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
