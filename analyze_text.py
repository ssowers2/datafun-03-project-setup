import requests
import logging

#Fetching the text
url = 'https://poets.org/poem/tyger'
response = requests.get(url) #ask the website for only the text from this url address
text_tyger = response.text.lower() #the website's response which is only the text in all lowercase

# Processing text data
words = text_tyger.split()
unique_words = set(words)
logging.info(f"Unique words count: {len(unique_words)}")

# Writing unique words to a file
with open('unique_words.txt', 'w') as file:
    for word in unique_words:
        file.write(word + '\n')

logging.info("Unique words written to unique_words.txt")
# Splitting text by newline into a list of lines
lines = text_tyger.split('\n')

# Count total lines
logging.info(f"Total number of lines: {len(lines)}")

longest_line = max(lines, key=len)
logging.info(f"Longest line: {longest_line}")

shortest_line = min(lines, key=len)
logging.info(f"Shortest line: {shortest_line}")

# reverse the lines
reversed_lines = lines[::-1]
logging.info(f"First 5 lines in reverse order: {reversed_lines[:5]}")

#print(text_tyger) #prints the text

# Filtering lines where tyger is mentioned
tyger_lines = [line for line in lines if line.startswith("tyger:")]

print(tyger_lines)

"""url = 'https://poets.org/poem/weary-blues'
response = requests.get(url)
text_weary = response.text.lower()

print(text_weary)

url = "https://poets.org/poem/i-love-you-i-miss-you-please-get-out-my-house"
response = requests.get(url)
text_house = response.text.lower()
print(text_house)"""