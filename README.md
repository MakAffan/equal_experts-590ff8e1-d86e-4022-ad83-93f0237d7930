 ## Instructions for the assignment
* Clone this repo on your machine.
* Use your IDE of choice to complete the assignment.
* When you are done with the solution and have pushed it to the repo, [you can submit the assignment here]({{submission_link}}).
* Once you indicate the completion, your access to the repository will be revoked. Do make sure that you have finished the solution and pushed all the relevant code to the repo.

## Assignment Details

We will be creating an ingestion process to ingest files containing vote data and a means to query the ingested data to determine outlier weeks.
We respect your time and understand that asking you to give up a couple of hours of your time is a big ask. However, we want to make the process as simple and stress-free as possible, by allowing you to complete the first stage of the process in the comfort of your own home.
We will also be using your submission in further stages of the process should you be successful.

## Prerequisites

The exercise requires docker in order to run, so please make sure you have this installed. Apart from that there are no other prerequisites.

## What we are looking for

**Test Coverage:** The solution must have good test coverage and common execution paths should be covered. Your tests should also be self-contained and not rely on them being run in a specific order

**Simplicity:** We value simplicity as an architectural virtue and a development practice. Solutions should reflect the difficulty of the assigned task, and should not be overly complex. Layers of abstraction, patterns, custom test frameworks or architectural features that aren’t called for should not be included. We are looking for you to demonstrate your understanding of the principles involved in data engineering so please avoid using libraries like pandas and lean towards more bare-bones solutions.

**Self-explanatory code**: The solution you produce must speak for itself. Multiple paragraphs explaining the solution are a sign that it isn’t straightforward enough to understand purely by reading code, and are not appropriate.

## The Problem Statement

There are two requirements for the task. A user should be able to execute each task independently of the other i.e. ingestion does not cause the outliers query to be executed.

1. Create an ingestion process that can be run on demand to ingest files containing vote data. You should ensure that data scientists, who will be consumers of the data, do not need to consider duplicate records in their queries.
2. Create a SQL query to calculate and output which weeks are regarded as outliers based on the vote data that was ingested.
The output should contain the year, week number and the number of votes for the week. A week is classified as outlier when the total votes for the week deviate from the average votes per week for the complete dataset by more than 20%</br>  
i.e. Say the mean votes is given by $\bar{x}$ and this specific week's votes is given by $x_i$.
We want to know when $x_i$ differs from $\bar{x}$ by more than $20\%$. When this is true, then the ratio $\frac{x_i}{\bar{x}}$ must be further from $1$ by more than $0.2$. </br></br> 
$\big|1 - \frac{x_i}{\bar{x}}\big| \gt 0.2$

## Example

Assuming a file is ingested containing the following entries:  

_Note: The sample dataset below is included in the test-resources folder and can be used when creating your tests_ 

```
{"Id":"1","PostId":"1","VoteTypeId":"2","CreationDate":"2022-01-02T00:00:00.000"}
{"Id":"2","PostId":"1","VoteTypeId":"2","CreationDate":"2022-01-09T00:00:00.000"}
{"Id":"4","PostId":"1","VoteTypeId":"2","CreationDate":"2022-01-09T00:00:00.000"}
{"Id":"5","PostId":"1","VoteTypeId":"2","CreationDate":"2022-01-09T00:00:00.000"}
{"Id":"6","PostId":"5","VoteTypeId":"3","CreationDate":"2022-01-16T00:00:00.000"}
{"Id":"7","PostId":"3","VoteTypeId":"2","CreationDate":"2022-01-16T00:00:00.000"}
{"Id":"8","PostId":"4","VoteTypeId":"2","CreationDate":"2022-01-16T00:00:00.000"}
{"Id":"9","PostId":"2","VoteTypeId":"2","CreationDate":"2022-01-23T00:00:00.000"}
{"Id":"10","PostId":"2","VoteTypeId":"2","CreationDate":"2022-01-23T00:00:00.000"}
{"Id":"11","PostId":"1","VoteTypeId":"2","CreationDate":"2022-01-30T00:00:00.000"}
{"Id":"12","PostId":"5","VoteTypeId":"2","CreationDate":"2022-01-30T00:00:00.000"}
{"Id":"13","PostId":"8","VoteTypeId":"2","CreationDate":"2022-02-06T00:00:00.000"}
{"Id":"14","PostId":"13","VoteTypeId":"3","CreationDate":"2022-02-13T00:00:00.000"}
{"Id":"15","PostId":"13","VoteTypeId":"3","CreationDate":"2022-02-20T00:00:00.000"}
{"Id":"16","PostId":"11","VoteTypeId":"2","CreationDate":"2022-02-20T00:00:00.000"}
{"Id":"17","PostId":"3","VoteTypeId":"3","CreationDate":"2022-02-27T00:00:00.000"}
```

Then the following outliers should be output

```
2022, 0, 1
2022, 1, 3
2022, 2, 3
2022, 5, 1
2022, 6, 1
2022, 8, 1
```

## Other Requirements

Please include instructions about your strategy and important decisions you made in the README file. You should also include answers to the following questions:

1. What kind of data quality measures would you apply to your solution in production?
2. What would need to change for the solution scale to work with a 10TB dataset with 5GB new data arriving each day?

## Bootstrap solution description

This repository contains a bootstrap solution that you can use to build upon. You are free to make any changes you see fit, so long as the solution can still be executed using the supplied [Makefile](https://github.com/snapcodereview-templates/equal_experts-85c94b44-34e7-45d2-9275-5901d877249a/blob/main/Makefile), as we will be using the Makefile to review your solution.

To view the targets supported by the Makefile please execute make help target.

The base solution uses sqlite3 as the database and you should treat sqlite3 as if it were a real data warehouse. The database should be saved in the root folder of the project as warehouse.db, as is being done in the src/db_test.py file.

* [src/ingest.py](https://github.com/snapcodereview-templates/equal_experts-85c94b44-34e7-45d2-9275-5901d877249a/blob/main/src/ingest.py) is provided as the entry point for running the ingestion process.
* [src/outliers.py](https://github.com/snapcodereview-templates/equal_experts-85c94b44-34e7-45d2-9275-5901d877249a/blob/main/src/outliers.py) is provided as the entry point for running the outlier detection query.
* [src/db.py](https://github.com/snapcodereview-templates/equal_experts-85c94b44-34e7-45d2-9275-5901d877249a/blob/main/src/db.py) is empty, but the associated test demonstrates interaction with an SQLite3 database.

## FAQ

**What other functionality is required?**

No other capabilities are required. This is not a trick question and there is no single correct answer. We prefer simple, well tested solutions over clever solutions. The complexity of your solution should reflect that of the problem. 

**What about ambiguity?**

If there is any ambiguity please add this in a section added to the bottom of the README and make a choice yourself to resolve the ambiguity.

**Is there a time limit for completing the exercise?**

There is no time limit for how long the exercise should take for you to complete, but we expect that you can complete the exercise in a couple of hours..

