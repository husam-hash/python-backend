import os

def count_word_frequency(input_file, output_file):
    try:
        
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"The file '{input_file}' does not exist.")

        
        with open(input_file, 'r', encoding='utf-8') as infile:
            content = infile.read()

        
        for char in '-.,\n':
            content = content.replace(char, ' ')
        content = content.lower()

        
        words = content.split()

        
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1

        with open(output_file, 'w', encoding='utf-8') as outfile:
            for word, freq in sorted(word_freq.items()):
                outfile.write(f"{word}: {freq}\n")

        print(f"Word frequency has been written to '{output_file}' successfully.")

    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except PermissionError:
        print("Error: Permission denied while accessing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Process complete.")


input_filename = 'input.txt'
output_filename = 'word_frequency.txt'

count_word_frequency(input_filename, output_filename)
