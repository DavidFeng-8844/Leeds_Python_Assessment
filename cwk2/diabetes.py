"""
Please write your name
@author:Yujie Feng

"""

# Reminder: You are only allowed to import the csv module (done it for you).
# OTHER MODULES ARE NOT ALLOWED (NO OTHER IMPORT!!!).
import csv
from typing import List

class Diabetes:
    def __init__(self, filepath: str) -> None:
        """
        Reads in a diabetes-related csv file, specified by filepath,
        and assigns data in header to an instance variable, and the remaining
        data to another instance variable.

        Parameters:
        - filepath (str): The path to the diabetes-related csv file.

        Raises:
        - FileNotFoundError: If the specified file is not found.
        """
        try:
            with open(filepath, newline='') as file:
                reader = csv.reader(file)
                self.header = next(reader)
                # print(self.header)
                self.data = list(reader)
                # print(self.data)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {filepath}")

    def get_dimension(self) -> List[int]:
        """
        Returns the dimensions of the data in the csv file as a list
        [row, column], excluding the header.

        Returns:
        - List[int]: A list containing the number of rows and columns.
        """
        rows = len(self.data)
        columns = len(self.header)
        return [rows, columns]

    def web_summary(self, filepath: str) -> None:
        """
        Generates an HTML file, specified by the filepath parameter, containing
        an HTML table summarizing the total count of Yes and No values for
        attributes other than Age and Gender, based on the classification
        (Positive or Negative) for the data.

        Parameters:
        - filepath (str): The path to the HTML file to be generated.

        Returns:
        - None
        """
        # Initalize a dictionary to store positive counts
        positive_counts = {attribute: 0 for attribute in self.header[2:-1]}

        # Count positive's yes and no for each instances
        for instance in self.data:
            if instance[-1] == 'Positive':
                for i, attribute in enumerate(instance[2:-1]):
                    positive_counts[self.header[i + 2]] += 1

        #Initalize a dictionary to store negative counts
        negative_counts = {attribute: 0 for attribute in self.header[2:-1]}
        # Count negative's yes and no for each instances
        for instance in self.data:
            if instance[-1] == 'Negative':
                for i, attribute in enumerate(instance[2:-1]):
                    negative_counts[self.header[i + 2]] += 1

        # Initialize a dictionary to store counts
        attribute_counts = {attribute: {'Positive': 0, 'Negative': 0} for attribute in self.header[2:-1]}

        # Count instances based on classification
        for instance in self.data:
            classification = instance[-1]
            for i, attribute in enumerate(instance[2:-1]):
                attribute_counts[self.header[i + 2]][classification] += 1

        # Generate HTML table
        with open(filepath, 'w') as html_file:
            # Multiline F-strings to make it more readable (and less ugly)
            html_content = f"""
            <html>
            <head>
            <style>
                table, th, td {{
                    border: 1px solid black;
                    border-collapse: collapse;
                    padding: 5px;
                }}
                table tr:nth-child(odd) {{
                    background-color: #d697b4;
                }}
                table tr:nth-child(even) {{
                    background-color: #8cb1b6;
                }}
                table tr:nth-child(odd):hover {{
                    background-color: #e83e8c;
                }}
                table tr:nth-child(even):hover {{
                    background-color: #17a2b8;
                }}
            </style>
            </head>
            <body>
                <table border='1'>
                    <tr>
                        <th rowspan = "3">Attribute</th>
                        <th colspan = "4">Class</th>
                    </tr>   
                    <tr>
                        <td colspan = "2">Possitive</td>
                        <td colspan = "2">Negative</td>
                    </tr>
                    <tr>
                        <th>Yes</th>
                        <th>No</th>
                        <th>Yes</th>
                        <th>No</th>
                    </tr>

            """

            for attribute, counts in attribute_counts.items():
                html_content += f"""
                    <tr>
                        <td>{attribute}</td>
                        <td>{counts['Positive']}</td>
                        <td>{counts['Negative']}</td>
                        <td>{counts['Positive']}</td>
                        <td>{counts['Negative']}</td>
                    </tr>
                """	
                
            html_content += """
                </table>
            </body>
            </html>
            """

            html_file.write(html_content)


    def count_instances(self, **criteria) -> int:
        """
        Returns the count of instances that meet specific search criteria.

        Parameters:
        - **criteria (kwargs): Keyword arguments representing search criteria.
          The keys should correspond to column names, and values should be the
          desired value for that column.

        Returns:
        - int: The count of instances that meet the specified criteria.
        """
        count = 0
        for instance in self.data:
            match = all(instance[self.header.index(key)] == str(value) for key, value in criteria.items())
            if match:
                count += 1
        return count

if __name__ == "__main__":
    # You can comment the following when you are testing your code
    # You can add more tests as you want

    # test diabetes_data.csv
    d1 = Diabetes("diabetes_data.csv")
    print(d1.get_dimension())
    d1.web_summary('stat01.html')
    print(d1.count_instances(Gender='Male', Obesity='Yes'))
    print()
    
    # test diabetes2_data.csv
    d2 = Diabetes("diabetes2_data.csv")
    print(d2.get_dimension())
    d2.web_summary('stat02.html')
    print(d2.count_instances(Polyuria='Yes', Age='55'))
