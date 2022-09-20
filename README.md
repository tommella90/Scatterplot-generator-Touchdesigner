# Scatterplot-generator-Touchdesigner
Upload csv file and create you scatterplot (no code needed)
Donwload the toe file [here](https://github.com/tommella90/Scatterplot-generator-Touchdesigner/blob/main/scatterplot.1.toe)

Here is an example
https://user-images.githubusercontent.com/66441052/191265558-dd19369e-3599-4255-8cbe-c1befd6b7f8c.mp4

# FEATURES
### 1) MAIN
- Choose the csv file, the X and Y variable and it's ready
- Plot the ols fitted line and choose your colors
- Drop from the graph the outliers to see how it looks like

<img align="right" width="400" height="400" src="https://github.com/tommella90/Scatterplot-generator-Touchdesigner/blob/main/img/main.png">

### 2) LABELS AND THICKS
Here you can control
- Title graph
- Thicks
- Labels

<img align="right" width="400" height="400" src="https://github.com/tommella90/Scatterplot-generator-Touchdesigner/blob/main/img/colors.png">

### 3) ESTETICS
- Background color
- Color markers by your preferred variables
- Use default colors or choose yours ones
- Show details: open an interactive graph displaying the variable of interest on touch
- Legend

<img align="right" width="400" height="400" src="https://github.com/tommella90/Scatterplot-generator-Touchdesigner/blob/main/img/colors2.png">

### 4) SAVER
Choose the folder and save the plot on your choosen format

<img align="right" width="400" height="400" src="https://github.com/tommella90/Scatterplot-generator-Touchdesigner/blob/main/img/estimation.png">

### 5) ESTIMATIONS 
- Fit Kmeans and use it as color group. You can choose the variables to fit (by default all the numerical ones) and the number of K.
- Show ols fitted line by group. If you fit Kmean, you can use it as group 
- Fit ols after dropping outliers and see how it changes

<img align="right" width="400" height="400" src="https://github.com/tommella90/Scatterplot-generator-Touchdesigner/blob/main/img/estim1.png">


## Here are the scripts
1) [extension](https://github.com/tommella90/Scatterplot-generator-Touchdesigner/blob/main/scatter_ext.py)
   It contains the extension and all the funcionts to make it work
2) [execute dat](https://github.com/tommella90/Scatterplot-generator-Touchdesigner/blob/main/ex_dat.py)
   It triggers the functions on call
3) [Show details](https://github.com/tommella90/Scatterplot-generator-Touchdesigner/blob/main/interactive.py) 
   To apply the interactive *show details* function
4) [Kmeans table](https://github.com/tommella90/Scatterplot-generator-Touchdesigner/blob/main/make_table.py)
   To choose the variablo to apply Kmeans on (to be improved)
