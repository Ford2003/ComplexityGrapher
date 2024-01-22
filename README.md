# ComplexityGrapher

## Introduction
This module provides functions to run a given function with given parameters and return the runtime of the function and show a graph of runtimes.

## Usage
### [graph_time](https://github.com/Ford2003/ComplexityGrapher/blob/main/src/grapher.py#L37) - *Callable*

Given a function and a list of parameters, graph the runtime of the function.

<ins>**Parameters**</ins>

***func:*** Callable function  
***params:*** List of lists or dicts containing the parameters for the function.  
***plot_type:*** The plot type for the graph, 'line' = line graph, 'scatter' = scatter graph. Default = 'line'  

<ins>**Return**</ins>  

***None***

---

### [measure_time](https://github.com/Ford2003/ComplexityGrapher/blob/main/src/grapher.py#L17) - *Callable*

Runs a given function once with a list of parameters and return the runtime of the function in milliseconds.

<ins>**Parameters**</ins>

***func:*** Callable function to time  
***params:*** List of args for the function, or dictionary of kwargs for the function.  

<ins>**Return**</ins>  

***float:*** runtime in milliseconds.

---

### [timer](https://github.com/Ford2003/ComplexityGrapher/blob/main/src/grapher.py#L7) - *Decorator*

Times the decorated function and returns the runtime.

<ins>**Parameters**</ins>

***func:*** Callable function to time  

<ins>**Return**</ins>  

***Callable:*** Wrapper function.


