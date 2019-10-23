# Introduction

This document provides the documentation for Ekström, B. (2019). *Developing a rule-based method for identifying researchers on Twitter: The case of vaccine discussions*. Poster abstract accepted to ISSI, 17th International Society of Scientometrics and Informetrics Conference, Rome, 2-5 September.

To cite this script:

```
Björn Ekström. Högskolan i Borås, Akademin för bibliotek, information, pedagogik och IT (2019). Rule-based method for identifying researchers on Twitter. Svensk nationell datatjänst. Version 1.0. https://doi.org/10.5878/akmc-va16
```

# Method

The classification code for each class with its designated keywords are presented under each heading in the script; "Science student", "Graduated", "University faculty (academic)", etc.

Using data cleanup and management software OpenRefine (http://openrefine.org/) with a tabulated text file where Twitter biographies are placed in a separate column, do the following: 

1. Click the arrow beside the column name, highlight "Edit column" and choose "Add column based on this column". 
2. Set Language to "Python / Jython".
3. Paste the code beneath a commented heading (e.g. `# Science student`).
4. Name the column and click OK. 

Proceed by using the same procedure for all other classes. 

For the last class, "Unknown", proceed by performing the classification procedure as before. After this procedure, the string "no match" will be added to the biographies which are not unknown. Set a text facet on the column and select the rows which are blank. Bulk rename these to "Unknown" and replace "no match" with an empty string.

# Acknowledgements

This project has received funding from the European Union’s Horizon 2020 research and innovation programme under grant agreement No. 770531. 
