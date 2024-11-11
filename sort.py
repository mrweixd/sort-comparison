import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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

# Function to update graph
def update_graph():
   plt.subplot(2, 3, 1)
   plt.bar(one_to_fifty, list(bubble) + [50], color=color)
   plt.title("Bubble Sort")
   plt.axis('off')
   plt.subplot(2, 3, 2)
   plt.bar(one_to_fifty, list(insertion) + [50], color=color)
   plt.title("Insertion Sort")
   plt.axis('off')
   plt.subplot(2, 3, 3)
   plt.bar(one_to_fifty, list(merge) + [50], color=color)
   plt.title("Merge Sort")
   plt.axis('off')
   plt.subplot(2, 3, 4)
   plt.bar(one_to_fifty, list(quick) + [50], color=color)
   plt.title("Quick Sort")
   plt.axis('off')
   plt.subplot(2, 3, 5)
   plt.bar(one_to_fifty, list(heap) + [50], color=color)
   plt.title("Heap Sort")
   plt.axis('off')
   plt.show()
   plt.subplot(2, 3, 6 )
   plt.title("Terminate the code to stop the sorting graph", fontsize= 'small')
   plt.axis('off')
   plt.show()

# X-axis
one_to_fifty = list(range(1, 52))

# Bar color setting
color = ['y'] * 50 + ['w']

# Generate random permutation of 1 to 50
my_arr = np.random.permutation(50) + 1

# Copy the array for different sorts
bubble = my_arr.copy()
insertion = my_arr.copy()
merge = my_arr.copy()
quick = my_arr.copy()
heap = my_arr.copy()

# Record steps for each sort
merge_steps=[]

bubble_steps = bubble_sort(bubble)
insertion_steps = insertion_sort(insertion)
merge_sort(merge, 0, 49)
quick_steps = quick_sort(quick, 0, 49)
heap_steps = heap_sort(heap)

# Initialize arrays for animation
bubble = my_arr.copy()
insertion = my_arr.copy()
merge = my_arr.copy()
quick = my_arr.copy()
heap = my_arr.copy()

# Record current step for each sort
bub_step = len(bubble_steps)
ins_step = len(insertion_steps)
mer_step = len(merge_steps)
quick_step = len(quick_steps)
heap_step = len(heap_steps)
bn = inn = mn = qn = hn = 0

# Animation loop
plt.ion()
while bn < bub_step or inn < ins_step or mn < mer_step or qn < quick_step or hn < heap_step:
   if bn < bub_step:
       bubble[bubble_steps[bn][0]], bubble[bubble_steps[bn][1]] = bubble[bubble_steps[bn][1]], bubble[bubble_steps[bn][0]]
       bn += 1
   if inn < ins_step:
       insertion[insertion_steps[inn][0]], insertion[insertion_steps[inn][1]] = insertion[insertion_steps[inn][1]], insertion[insertion_steps[inn][0]]
       inn += 1
   if mn < mer_step:
       merge[merge_steps[mn][0]] = merge_steps[mn][1]
       mn += 1
   if qn < quick_step:
       quick[quick_steps[qn][0]], quick[quick_steps[qn][1]] = quick[quick_steps[qn][1]], quick[quick_steps[qn][0]]
       qn += 1
   if hn < heap_step:
       heap[heap_steps[hn][0]], heap[heap_steps[hn][1]] = heap[heap_steps[hn][1]],heap[heap_steps[hn][0]]
       hn += 1
   update_graph()
   plt.pause(0.05)
   plt.clf()
    
plt.ioff()
update_graph()
