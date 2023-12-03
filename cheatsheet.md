# Cheatsheet for Interview Problems 

## C++ Notes

### Array and Strings 

- set: binary search tree
- unordered_set: hashset

#### Iterating through map
```c++
for (auto x: mp){
    ans.push_back(x.second); // x.first is the key
}
```

```c++
double numbers[size] {0};
int i2[row][column]

// arrays2.cpp
// compile with: /c
const int cMarkets = 4;
// Declare a float that represents the transportation costs.
double TransportCosts[][cMarkets] = {
   { 32.19, 47.29, 31.99, 19.11 },
   { 11.29, 22.49, 33.47, 17.29 },
   { 41.97, 22.09,  9.76, 22.55 }
};

```

#### Initialize array with all zeros
```c++
int sCharCount[26] = { 0 };
```

#### String iterator
```c++
// string::begin/end
#include <iostream>
#include <string>

int main ()
{
  std::string str ("Test string");
  for ( std::string::iterator it=str.begin(); it!=str.end(); ++it)
    std::cout << *it;
  std::cout << '\n';

  return 0;
}
```

#### Ascii
65 - 90 A-Z
97 - 122 a-z

#### Print array template
```c++
// Print in Normal order
std::copy(userInput.begin(),
          userInput.end(),
          std::ostream_iterator<int>(std::cout,",")
         );
std::cout << "\n";

template<typename T, size_t n>
void print_array(T const(& arr)[n])
{
    for (size_t i = 0; i < n; i++) {
        std::cout << arr[i] << ' ';
    }
}
```

#### Convert char to int using ascii code
```c++
// Count the frequency of characters in string s
for (char x : s) {
    count[x - 'a']++;
}

// Decrement the frequency of characters in string t
for (char x : t) {
    count[x - 'a']--;
}
```

#### Find target with complement
```c++
// calculate the complement and check hashmap if it exists
// if not then store the current number to the map 
for (int i = 0;i < n; i++){
	int complement = target - nums[i];
	if (numMap.count(complement))}{
		return {numMap[complement], i}
	}
	numMap[nums[i]] = i; 
}

unordered_map<int, int> numMap;
numMap.count(complement) // check if it exists
```

#### Vector
```c++
// Create a vector of size n with all values as 10 
vector<int> vect(n, 10);

// 10 20 30
vector<int> vect{ 10, 20, 30 };

int arr[] = {10, 20, 30}
int n = sizeof(arr) / sizeof(arr[0]);

vector<int> vect(arra, arr + n);
```

#### K Most Occuring Elements in the Given Array
- Create a map of elements to frequency.
- Sort, Max-Heap, Bucket Sort, Quick Sort
    - Map and Sort (nlogn)
    ```c++
    // Comparison function to sort the 'freq_arr[]'
    bool compare(pair<int, int> p1, pair<int, int> p2)
    {
        // If frequencies of two elements are same
        // then the larger number should come first
        if (p1.second == p2.second)
            return p1.first > p2.first;
     
        // Sort on the basis of decreasing order
        // of frequencies
        return p1.second > p2.second;
    }

    // Sort the vector 'freq_arr' on the basis of the
    // 'compare' function
    sort(freq_arr.begin(), freq_arr.end(), compare);
    ```

    - Max-Heap (DlogD)
    ```c++
    // priority queue 'pq' implemented as max heap on the
    // basis of the comparison operator 'compare' element
    // with the highest frequency is the root of 'pq' in
    // case of conflicts, larger element is the root
    priority_queue<pair<int, int>, vector<pair<int, int> >,
                   compare>
        pq(mp.begin(), mp.end());
    ```

    - Bucket Sort (n || nlogn if the return value needs to be sorted)
    ```c++
    // Store the elements according to their frequency
    vector<vector<int> > frequency(N + 1);

    // Reverse index from the right (from the largest index)
    ```

    - Quick Select (nlogn)
    ```c++
    int partition(vector<pair<int, int>> &freqVec, int l, int r){
        int pivot = freqVec[r].first; 
        int storeIndex = l; 
        
        // Move all the elements less than pivot to left 
        // Move all the elements greater than pivot to right
        for (int i = l; i < r; i++){
            if (freqVec[i].first > pivot) {
                swap(freqVec[i], freqVec[storeIndex]);
                storeIndex++;
            }
        }
        
        swap(freqVec[storeIndex], freqVec[r]);

        return storeIndex;
    }
    
    void quickSelect(vector<pair<int,int>> &freqVec, int l, int r, int k){
        if (l >= r) return;
        
        int part = partition(freqVec, l, r);
        cout << "Pivot Index: " << part << endl;

        if (part == k){
            return;
        } else if (part < k){
            quickSelect(freqVec, part + 1, r, k);
        } else {
            quickSelect(freqVec, l, part - 1, k);
        }
    }
    ```
