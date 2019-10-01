# FB Search Notebook


This is a reimplementation of @ahmel's python script using a jupyter 
notebook to streamline usage and make it more accessible to researchers

The changes I've made are as follows:
- Converting existing comments to text cells so explanations are more readable.
- Changed some code to use ideomaticdiomatic python
- Made everything run on python3 consistent
- Refactored code to use Jinja2 templates instead of inlining html, which is so *php* from way back when.

if you've never used a Jupyter Notebook, or used Google Collab, it's a python execution environment and virtual machine connected to your browser and Google drive. (neat huh?) 

Every code cell has a little "play" button on the upper left corner (just mouse over it), when clicked, the code on the cell will run and the output will be displayed below the cell. A lot of neat stuff can be done with Jupyter and Collab, specially explaining how code works. This is a style of programming called Literate Programming, and it is excellent for teaching and academia.

Data science too.

## Purpose
This workbook reads a **json search result file**, sorts results by time, creates links to posts and puts the links together with corresponding messages and images in an html file. The notebook then displays the results as a webpage as an output, or, if so selected, in a new tab on your current browser.

## How do i get this **json search results file** you speak of?

there used to be a nice detailed explanation here, but i realised this thread is full of greedy no-sharers, shady accounts that have no public repos (and whom i suspect to be the same guy pushing devs to solve his problems for free), a bunch of freeloaders who are probably interested only in getting pics their GF 'liked' so they can make a fuss about it, and whatnot. 

Except for a few real devs here (v.gr @sowdust) i don't really think any other people in this thread are even interested in coding, much less doing serious OSINT research. 

Having said that, you can get the search result json using one of the APIs mentioned in this thread, which turns out to be just a repackaged FB endpoint. I wouldn't use it though, since it's doing a bunch of stuff loading frames and Facebook's arbiter and I wouldn't be surprised if it was stealing access tokens from those who use it. (FB security is and always has been a joke)

Since the source is not being shared, i therefore deem it untrustworthy, and to be used at your own peril.

This workbook's purpose is only to show it's not really that hard to do things right.
