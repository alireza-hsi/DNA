import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt ")

    # TODO: Read database file into a variable
    dbfilename = sys.argv[1]
    sqfilename = sys.argv[2]
    dblist = []
    with open(dbfilename) as db:
        reader = csv.DictReader(db)
        strlist = ["AGATC","TTTTTTCT","AATG","TCTAG","GATA","TATC","GAAA","TCTG"]
        for row in reader:
            for str in strlist:
                if str in row.keys():
                    row[str] = int(row[str])
            dblist.append(row)

    #print(dblist)
    
    # TODO: Read DNA sequence file into a variable
    with open(sqfilename, "r") as sq:
        sqreader = sq.read()
    #print(sqreader)

    # TODO: Find longest match of each STR in DNA sequence
    dic = dblist[0].copy()
    for key in dic.keys():
        dic[key] = longest_match(sqreader, key)
    #print(dic)

    # TODO: Check database for matching profiles
    i = 0
    for d in dblist:
        check = 0
        #print(dblist)
        for key in dic.keys():
            #print(dic[key])
            #print(dblist[i][key])
            if dic[key] == dblist[i][key]:
                check += 1
        
        #print(check)
        if check == (len(dic.keys()) - 1):
            print(dblist[i]["name"])
            exit()
        i += 1
    
    print("No match")

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            
            # If there is no match in the substring
            else:
                break
        
        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
