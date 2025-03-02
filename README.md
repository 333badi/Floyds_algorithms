# Floyd-Warshall Algorithm - README

## **What is this repository for?**  

This repository contains an implementation of the **Floyd-Warshall Algorithm**, used for finding the shortest paths in a weighted graph. It includes:  

- **Iterative Floyd-Warshall Implementation**  
- **Recursive Floyd-Warshall Implementation**  
- **Unit tests to verify correctness**  
- **Performance benchmarking scripts**  

---

## **How do I get set up?**  

### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/your-username/floyd-warshall.git
cd floyd-warshall/src
---

It is best practice to create a virtual environment to store the dependencies for your project. This prevents issues such as deprecation, which can break your code. However, as all imports used in this code come from the Python built-in library, this is not necessary.

creating a virtual environment using the requirements.txt file

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows 

# Install dependencies from requirements.txt
### **Running the Scripts** ###


## Running the scripts ##

# Run the iterative Floyd-Warshall implementation
python -m iterative.iterative_floyd

# Run the recursive Floyd-Warshall implementation
python -m recursion.recursive_floyd

# Run the performance benchmarking script
python -m tests.performance_test

# Run the unit tests to verify correctness
python -m tests.unittests


### Requirements ### 



