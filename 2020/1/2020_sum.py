"""Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456

In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.
"""""

seen = set()

with open('input.txt', 'r') as file:
     for line in file:
         curr = int(line)
         if(curr in seen):
             print(curr, 2020-curr)
             print(curr * (2020 - curr))
             break
         else:
             diff = 2020 - curr
             seen.add(diff)


"""
--- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?

"""

# Three Sum
with open('input.txt', 'r') as file:
    array = [int(num) for num in file]

array.sort()
#print(array)

def three_sum(array):
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while(left < right):
            c,l,r = array[i],array[left],array[right]
            add =  sum([c,l,r])
            if(add == 2020):
                print(c,l,r)
                return c * l * r
            elif(add < 2020):
                left += 1
            else:
                right -= 1

print(three_sum(array))
