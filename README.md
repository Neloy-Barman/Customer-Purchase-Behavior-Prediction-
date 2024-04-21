# Customer Purchase Behavior Prediction


<h2>Project Development Journal</h2>


<h3><code style="color:blue">Problem Statement</code></h3>

<strong>We will create a customer purchase behavior prediction system using the following dataset performing data preprocessing, feature engineering and choosing a proper ensemble model with the training and evaluation.</strong>


<h3><code style="color:blue">Dataset Description</code></h3>

<strong>To work on this project, I have chosen <a href="https://www.kaggle.com/datasets/ishanshrivastava28/tata-online-retail-dataset">TATA: Online Retail Dataset</a>. The dataset contains the same file in 2 different formats csv and xlsx. But I will proceed with the .csv file. It contains 541909 rows and 8 columns. The description and purpose of the each column in the dataset are given as follows: -</strong>
<ul>
    <li><strong>InvoiceNo</strong>: Unique id for the order billing.</li>
    <li><strong>StockCode</strong>: A code for the product inventory.</li>
    <li><strong>Description</strong>: Title of the product.</li>
    <li><strong>Quantity</strong>: The number of the particular products ordered.</li>
    <li><strong>InvoiceDate</strong>: Ordering date.</li>
    <li><strong>UnitPrice</strong>: Individual price for the product.</li>
    <li><strong>CustomerID</strong>: Unique id for the ordering customer.</li>
    <li><strong>Country</strong>: Residing country of the customer.</li>
</ul>


<h3><code style="color:blue">Assumption</code></h3>

<strong>As we have to predict the customer purhase behavior based on the given features, so, need to find out the relevant customer characteristics while from the dataset.</strong>


<h3><code style="color:blue">Data Pre-processing</code></h3>

<ul>
    <li><strong>Missing value Handling: -</strong> We got NaN values in the 'CustomerID'. As 'CustomerID' is the unique identifier for each customer, so, having NaN in this column won't let us know the customer. Therefore those rows are deleted.</li>
    <li><strong>Column Dtype Formation: -</strong> The 'CustomerID' was in float64 format. So, I convert it to int format as, it's an unique identifier.</li>
    <li><strong>Feature Engineering: -</strong> We got 4372 unique ids for the customers. So, we have to find these customers characteristics in this dataset. There were a very few features relatable to customers such as, CustomerID, Country. The other features such as StockCode, Description and some others relate to product rather than customers. So, we have to create some new features from these.
        <ul>
            <li><strong>Revenue_given: </strong>Each customer bought different number of products for the unit price. So, we calculated a new column 'Revenue_given' that tells how much the customer has spent ordering products.</li>
            <li><strong>Frequency: </strong>How frequently a customer bought products from the company.</li>
            <li><strong>Recency: </strong>How many days have been past since last buy for a customer.</li>
            <li><strong>United Kingdom Or Not: </strong>We saw that we have the most number of customers from UK, and other values are far away from those values. So, we extracted a new feature from here.</li>
        </ul>
        <strong>Creating some new features relating to the customers we created a new dataframe dropping other columns.</strong>
        <div align="center"><img src="assets/df.png"></div>
    </li>
    <li><strong>Handling outliers: </strong>Outliers existed in the numeric columns & those were handled.</li>
</ul>
<div align="center">
    <table>
        <tr>
            <th>FileName</th>
            <th>Extension</th>
            <th>Rows</th>
            <th>Columns</th>
        </tr>
        <tr>
            <td>Online_Retail_Data_Set</td>
            <td>csv</td>
            <td>541909</td>
            <td>8</td>
        </tr>
        <tr>
            <td>final_dataset</td>
            <td>csv</td>
            <td>3616</td>
            <td>5</td>
        </tr>
    </table>
</div>




