# cleans hemingway data. train > train_f
def main():
    # open the embeddings data
    infile = open("data_train.1.txt", "r")
    hemmingway_train = infile.readlines()
    infile.close()

    sentences = []
    for entry in hemmingway_train:
        if entry != '\n':
            if entry[0] == '"':
                sentences.append(entry)
            else:
                for sent in entry.split('.'):
                    sentences.append(sent.strip() + '.\n') 
    

    # output file
    outfile = open('data_train_f.1.txt', 'w')
    for entry in sentences:
        if len(entry) > 4:
            outfile.write(entry)
    outfile.close()

if __name__ == "__main__": main()