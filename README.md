# Objective

Create and print a JSON object containing the data in the [El Paso County
Elected Officials Directory](https://epcountyvotes.com/elected-officials-and-candidate-information/elected-officials/print).
 (ignore the print modal). The URL for the directory is in [url.txt](https://github.com/civicpolitics/interview/blob/2e4bdcd71caf3a0e406b24832e79099c5980c374/url.txt).
The object should have a key for each section of the site. The value for each
of these keys should be a list of JSON objects containing the data within each
of the tables that follow the section titles.

The objects within these lists should each represent a row of the corresponding
table. The keys should be the column names of the table and values should be
the data corresponding to that column for the row that the object represents.

For example, the first key and corresponding value of the final object should be:
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
