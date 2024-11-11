# sort-comparison
  This is a simple sort comparison code. It first generates random permutation of 50 numbers ranging from 1 to 50, and visualize how different kinds of sorting method work.

  <img src="https://github.com/user-attachments/assets/dbf65f12-9236-43d2-aa64-8586fa4f6e8f" width=50% height=50%>

  You can watch them sort to complete.
  
  <img src="https://github.com/user-attachments/assets/e08e4cbb-01ca-4368-8448-6b8f701dbbe9" width=50% height=50%>


This code applies five kinds of sort:

 * Bubble Sort `O(n^2)`
```py
# Function to perform bubble sort
def bubble_sort(arr):
   steps = []
   n = len(arr)
   for i in range(n - 1):
       for j in range(n - i - 1):
           if arr[j] > arr[j + 1]:
               arr[j], arr[j + 1] = arr[j + 1], arr[j]
               steps.append([j, j + 1])
           else:
               steps.append([0, 0])
   return steps
```
 * Insertion Sort `O(n^2)`
```py
# Function to perform insertion sort
def insertion_sort(arr):
   steps = []
   for i in range(1, len(arr)):
       j = i - 1
       while j >= 0 and arr[j + 1] < arr[j]:
           arr[j], arr[j + 1] = arr[j + 1], arr[j]
           steps.append([j, j + 1])
           j -= 1
   return steps
```
 * Merge Sort `O(nlog(n))`
```py
# Function to perform merge sort
def merge_sort(arr, l, r):
   if len(arr) > 1:
       mid = len(arr) // 2
       real_mid = (l + r + 1) // 2
       left = arr[:mid].copy()
       right = arr[mid:].copy()
       merge_sort(left, l, real_mid)
       merge_sort(right, real_mid, r)

       i = j = k = 0
       while i < len(left) and j < len(right):
           if left[i] < right[j]:
               arr[k] = left[i]
               merge_steps.append([k + l, left[i]])
               i += 1
           else:
               arr[k] = right[j]
               merge_steps.append([k + l, right[j]])
               j += 1
           k += 1

       while i < len(left):
           arr[k] = left[i]
           merge_steps.append([k + l, left[i]])
           i += 1
           k += 1

       while j < len(right):
           arr[k] = right[j]
           merge_steps.append([k + l, right[j]])
           j += 1
           k += 1
```
 * Quick Sort `O(nlog(n))`
```py
# Function to perform partition for quick sort
def partition(arr, l, r):
   steps = []
   pivot = arr[r]
   i = l - 1
   for j in range(l, r):
       if arr[j] <= pivot:
           i += 1
           arr[i], arr[j] = arr[j], arr[i]
           steps.append([i, j])
       else:
           steps.append([0, 0])

   arr[i + 1], arr[r] = arr[r], arr[i + 1]
   steps.append([i + 1, r])
   return i + 1, steps
# Function to perform quick sort
def quick_sort(arr, l, r):
   steps = []
   if l < r:
       q, q_steps = partition(arr, l, r)
       steps.extend(q_steps)
       steps.extend(quick_sort(arr, l, q - 1))
       steps.extend(quick_sort(arr, q + 1, r))
   return steps

```
 * Heap Sort `O(nlog(n))`
```py
# Function to heapify for heap sort
def heapify(arr, n, i):
   steps = []
   mx = i
   l = 2 * i + 1
   r = 2 * i + 2

   if l < n and arr[i] < arr[l]:
       mx = l
   if r < n and arr[mx] < arr[r]:
       mx = r
   if mx != i:
       arr[i], arr[mx] = arr[mx], arr[i]
       steps.append([i, mx])
       steps.extend(heapify(arr, n, mx))
   return steps

# Function to perform heap sort
def heap_sort(arr):
   steps = []
   n = len(arr)
   for i in range(n // 2, -1, -1):
       steps.extend(heapify(arr, n, i))
   for i in range(n - 1, 0, -1):
       arr[i], arr[0] = arr[0], arr[i]
       steps.append([i, 0])
       steps.extend(heapify(arr, i, 0))
   return steps
```
