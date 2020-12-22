# Importing  and using the file
import autoarr

### Creating the columns
autoarr.autotitle(['Reg.no',2,'Name',10,'Marks',0]) 
### Name of the column along with the space that should be left on the either side of the column name

### Passing a list
list = [4543,'ABCD',90]

autoarr.autoarr(list)

### Passing multiple list
list = [4543,'ABCD',90],[7535,'ASDF',40]

for i in list:
    autoarr.autoarr(i)

## Sample Output
### For the Above Program
```
-------------------------------------------
|  Reg.no  |          Name          |Marks|
-------------------------------------------
|4543      |ABCD                    |90   |
-------------------------------------------
|4543      |ABCD                    |90   |
-------------------------------------------
|7535      |ASDF                    |40   |
-------------------------------------------
```