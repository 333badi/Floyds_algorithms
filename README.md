# Floyds Algorithm - README

## **What is this repository for?**  

This repository contains an implementation of the **Floyds Algorithm**, used for finding the shortest paths in a weighted graph. It includes:  

- **Iterative Floyd Imlementation**  
- **Recursive Floyd Implementation**  
- **Unit tests to verify functionalities**  
- **Performance benchmarking scripts**  

---

## **How do I get set up?**  

### **Clone the Repository**  
```sh
git clone https://github.com/333badi/Floyds_algorithms.git
```


### **Running the Scripts**


```sh
# Run the iterative Floyd algorithms
python -m iterative.iterative_floyd
```

```sh
# Run the recursive Floyd algorithms
python -m recursion.recursive_floyd
```

```sh
# Run the performance benchmarking script
python -m tests.performance_test
```

```sh
# Run the unit tests to verify correctness
python -m tests.unittests
```

### **Requirements**

```sh
# All requirements are listed in the requirements.txt file. 

python -m venv venv

venv\Scripts\activate #windows

pip install -r requirements.txt
```