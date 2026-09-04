# Create a function that counts the number of lines and words
def count_lines_and_words():
    with open('C:\\Coisas\\UFABC\\2026\\Recesso (08 - 09)\\30DaysOfPython\\day_19\\pokemon.json', 'r') as f:
        lines = f.readlines()
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
    return num_lines, num_words
print(count_lines_and_words())
