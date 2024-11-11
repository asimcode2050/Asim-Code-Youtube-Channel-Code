#include <iostream>
#include <stdexcept> // For handling exceptions like out of range
template <typename T>
class Vector
{
private:
    T *arr;
    size_t capacity;
    size_t size;

public:
    Vector(size_t initial_capacity = 10) : capacity(initial_capacity), size(0)
    {
        arr = new T[capacity];
    }
    ~Vector()
    {
        delete[] arr;
    }
    size_t getSize() const
    {
        return size;
    }
    size_t getCapacity() const
    {
        return capacity;
    }
    bool isEmpty() const
    {
        return size == 0;
    }
    void resize(size_t new_capacity)
    {
        if (new_capacity <= capacity)
            return;
        T *new_arr = new T[new_capacity];
        for (size_t i = 0; i < size; ++i)
        {
            new_arr[i] = arr[i];
        }
        delete[] arr;
        arr = new_arr;
        capacity = new_capacity;
    }
    void pushBack(const T &value)
    {
        if (size == capacity)
        {
            resize(capacity * 2);
        }
        arr[size++] = value;
    }
    T &at(size_t index)
    {
        if (index >= size)
        {
            throw std::out_of_range("Index out of bounds");
        }
        return arr[index];
    }
    const T &at(size_t index) const
    {
        if (index >= size)
        {
            throw std::out_of_range("Index out of bounds");
        }
        return arr[index];
    }
    T &operator[](size_t index)
    {
        return arr[index];
    }
    const T &operator[](size_t index) const
    {
        return arr[index]; // No bounds checking for const objects either
    }
    void popBack()
    {
        if (size == 0)
            return;
        --size;
    }
    void clear()
    {
        size = 0;
    }
    void print() const
    {
        for (size_t i = 0; i < size; ++i)
        {
            std::cout << arr[i] << " ";
        }
        std::cout << std::endl;
    }
};
int main()
{
    Vector<int> vec;
    vec.pushBack(1); // Add 1 to the vector
    vec.pushBack(2); // Add 2 to the vector
    vec.pushBack(3); // Add 3 to the vector
    std::cout << "Vector contents: ";
    vec.print();
    std::cout << "Size: " << vec.getSize() << std::endl;
    std::cout << "Capacity: " << vec.getCapacity() << std::endl;   // Print the capacity of the vector
    std::cout << "Element at index 1: " << vec.at(1) << std::endl; // Access the element at index 1
    vec.popBack();                                                 // Remove the last element
    std::cout << "After popBack, size: " << vec.getSize() << std::endl;
    vec.clear(); // Clear all elements
    std::cout << "After clear, size: " << vec.getSize() << std::endl;
    return 0;
}
