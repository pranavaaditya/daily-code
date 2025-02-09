#Arpasland has surrounded by attackers. A truck enters the city. The driver claims the load is food and medicine from Iranians. Ali is one of the soldiers in Arpasland. He doubts about the truck, maybe it's from the siege. He knows that a tag is valid if the sum of every two consecutive digits of it is even and its letter is not a vowel. Determine if the tag of the truck is valid or not.
#We consider the letters "A","E","I","O","U","Y" to be vowels for this problem.
#Input Format
#The first line contains a string of length 9. The format is "DDXDDD-DD", where D stands for a digit (non zero) and X is an uppercase english letter.
#Output Format
#Print "valid" (without quotes) if the tag is valid, print "invalid" otherwise (without quotes)

#Sample Input
#12X345-67
#Sample Output
#invalid
#Time Limit: 1
#Memory Limit: 256
#Source Limit:
#Explanation
#The tag is invalid because the sum of first and second digit of it is odd (also the sum of 4'th and 5'th, 5'th and 6'th and 8'th and 9'th are odd).

def is_valid_tag(tag):
    if tag[2] in " A E I O U Y ":
        return "invalid"
    
    for i, j in [(0,1), (3,4), (4,5), (7,8)]:
        if (int(tag[i]) + int(tag[j])) % 2:
            return "invalid"
    
    return "valid"
tag = input().strip()
print(is_valid_tag(tag))
