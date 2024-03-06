from bs4 import BeautifulSoup
from collections import Counter

# Read the HTML file
with open("python_class_question.html", "r") as file:
    html_content = file.read()

# Parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Find the table containing the colors of dress by workers at Bincom ICT for the week
table = soup.find("table")

# Extract data from the table
colors = {}
for row in table.find_all("tr")[1:]:  # Skip the header row
    columns = row.find_all("td")
    day = columns[0].text.strip()
    color_list = columns[1].text.strip().split(", ")
    colors[day] = color_list

# Flatten the list of colors
all_colors = [color for color_list in colors.values() for color in color_list]

# Calculate the required statistics
mean_color = Counter(all_colors).most_common(1)[0][0]
most_worn_color = Counter(all_colors).most_common(1)[0][0]
sorted_colors = sorted(all_colors)
median_index = len(sorted_colors) // 2
median_color = sorted_colors[median_index] if len(sorted_colors) % 2 != 0 else (sorted_colors[median_index - 1], sorted_colors[median_index])
total_colors = len(all_colors)
variance = sum((Counter(all_colors)[color] - (total_colors / len(Counter(all_colors)))) ** 2 for color in set(all_colors)) / total_colors
red_probability = Counter(all_colors)['RED'] / total_colors

# Print the results
print("Mean color:", mean_color)
print("Most worn color throughout the week:", most_worn_color)
print("Median color(s):", median_color)
print("Variance of colors:", variance)
print("Probability that the color is red when chosen at random:", red_probability)
