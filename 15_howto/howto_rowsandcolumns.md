# how-to :: CREATE ROWS AND COLUMNS IN HTML
---
## Overview
Creating rows and columns in html allow us to split information between sections of the page. In Lab K13: Stuylin' & Wylin' & Profilin', we had to create rows and columns in order to separate the information on the page. Also, it serves as an alternative method to using a table.

### Estimated Time Cost: 0.4 hrs

### Prerequisites:

- Basic html and css knowledge
- Understanding how selectors work
- Understanding how <div> work
- A way to access html files (vscode, atom, etc.)

1. In the html file, create a divider called "row".
    ```html
    <div class="row">
    ```
2. Insider the "row" divider, create as many dividers as you need (these would be the columns). Make sure to end each divider with a closing tag. Put whatever content you want into the columns and rows!
    ```html
    <div class="row">
      <div class="column1">
        ...
      </div>
      <div class="column2">
        ...
      </div>
    </div>
    ```
3. In the css file, create the selectors for each respective row and column. For the rows, make sure to title the class row:after.
    ```css
    .column1 {
      float: left;
      width: 20%;
      margin-left: 1rem
    }
    .column2 {
      float: right;h
      width: 70%;
    }
    .row:after {
      content: "";
      display: table;
      clear: both;
    }
    ```
4. The rest is up to you! Customize your own creation with varying properties.

### Resources
* [how :after works](https://www.w3schools.com/cssref/sel_after.asp)

---

Accurate as of (last update): 2022-10-20

#### Contributors:  
Shafiul Haque, pd8  
April Li, pd8  
David Deng, pd8  
