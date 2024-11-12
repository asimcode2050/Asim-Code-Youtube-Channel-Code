#include <iostream>
#include <vector>
#include <stdexcept>
using namespace std;
class MaxHeap
{
private:
    vector<int> heap;
    int leftChild(int index)
    {
        return 2 * index + 1;
    }
    int rightChild(int index)
    {
        return 2 * index + 2;
    }
    int parent(int index)
    {
        return (index - 1) / 2;
    }
    void heapifyDown(int index)
    {
        int left = leftChild(index);
        int right = rightChild(index);
        int largest = index;
        if (left < heap.size() && heap[left] > heap[largest])
        {
            largest = left;
        }
        if (right < heap.size() && heap[right] > heap[largest])
        {
            largest = right;
        }
        if (largest != index)
        {
            swap(heap[index], heap[largest]);
            heapifyDown(largest);
        }
    }
    void heapifyUp(int index)
    {
        while (index > 0 && heap[parent(index)] < heap[index])
        {
            swap(heap[index], heap[parent(index)]);
            index = parent(index);
        }
    }

public:
    void insert(int value)
    { // Add the element at the end of the heap
        heap.push_back(value);
        heapifyUp(heap.size() - 1);
    }
    int extractMax()
    {
        if (heap.size() == 0)
        {
            throw out_of_range("Heap is empty");
        }
        int maxValue = heap[0];
        heap[0] = heap[heap.size() - 1];
        heap.pop_back();
        heapifyDown(0);
        return maxValue;
    }
    int getMax()
    {
        if (heap.size() == 0)
        {
            throw out_of_range("Heap is empty");
        }
        return heap[0];
    }
    void printHeap()
    {
        for (int i = 0; i < heap.size(); i++)
        {
            cout << heap[i] << " ";
        }
        cout << endl;
    }
    bool isEmpty()
    {
        return heap.empty();
    }
    int size()
    {
        return heap.size();
    }
};
int main()
{
    MaxHeap heap;
    heap.insert(10);
    heap.insert(20);
    heap.insert(5);
    heap.insert(30);
    heap.insert(15);
    cout << "Heap after insertion: ";
    heap.printHeap();
    cout << "Maximum element: " << heap.getMax() << endl;
    cout << "Extracting maximum element: " << heap.extractMax() << endl;
    cout << "Heap after extraction: ";
    heap.printHeap();
    return 0;
}
