import zeyrek

analyzer = zeyrek.MorphAnalyzer()


def lemmatize_words(file_path, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        with open(file_path, 'r', encoding='utf-8') as file:
            words = file.read().splitlines()

        for word in words:
            analysis = analyzer.lemmatize(word)
            lemmas = [item[1] for item in analysis if item]
            lemma = lemmas[1] if lemmas else 'Not Found'
            output_file.write(f"{lemma}\n")
            print(f"Lemmatized: {lemma}")

# Please download the input file from the following link and assign the path to the variable 'input_file_path'.
# https://temretiras.github.io/tur_wikipedia_2021_10K-words.txt

input_file_path = "C:/Projects/Kelimelik/tur_wikipedia_2021_10K-words.txt"
output_file_path = "C:/Projects/Kelimelik/lemmas.txt"
lemmatize_words(input_file_path, output_file_path)

# For the sake of demonstration, we will use a sample output file.
# You should assign the path of the output file to the variable 'output_file_path'.
# https://temretiras.github.io/lemmas.txt

lemmas = "C:/Projects/Kelimelik/lemmas.txt"
with open(lemmas, "r", encoding="utf-8") as file:
    lines = file.readlines()


processed_lines = []
for line in lines:
    clean_line = line.strip()[1:-1]
    words = [word.strip().strip("'\"") for word in clean_line.split(',')]

    processed_line = '\n'.join(words)
    processed_lines.append(processed_line)

# For the sake of demonstration, we will use a sample output file.
# https://temretiras.github.io/processed_lemmas.csv
with open("C:/Projects/Kelimelik/processed_lemmas.csv", "w", encoding="utf-8") as output_file:
    output_file.write("\n".join(processed_lines))


print("Processing complete. The words have been separated and saved to 'processed_lemmas.csv'.")