# Objective

Create and print a JSON object containing the data at the URL in url.txt. The
object should have a key for each section of the site. The value for each of
these keys should be a list of JSON objects containing the data within each of
the tables that follow the section titles.

The objects within these lists each represent a row of the corresponding table.
The keys should be the column names of the table and values should be the data
in that column for the row that the object represents.

For example, the first key and corresponding output of the object should be:
```json
{
  "Federal - Executives": [
    {
      "Office": "United States President",
      "Office Holder Name": "Donald J. Trump",
      "Party": "Republican",
      "Term Length (years)": "4",
      "Next Election Date": "11/07/28",
      "Address/City/State/Zip": "P.O. Box 20500Washington, D.C. 20036",
      "Phone/Fax": "(202) 456-1414",
      "E-Mail/Website": "http://www.whitehouse.gov"
    },
    {
      "Office": "United States Vice President",
      "Office Holder Name": "JD Vance",
      "Party": "Republican",
      "Term Length (years)": "4",
      "Next Election Date": "11/07/28",
      "Address/City/State/Zip": "P.O. Box 20500Washington, D.C. 20036",
      "Phone/Fax": "(202) 456-1414",
      "E-Mail/Website": "http://www.whitehouse.gov"
    }
  ]
  ...
}
```

# Logistics

You can use any tool and search any information you'd like to
complete the task. You're allowed and encouraged to use AI, although doing so
is not required.

This project was built using uv (https://docs.astral.sh/uv/) but you can run
it using any python tooling you'd like.
