our_string  ='ABCDCDC'
target_substring = 'CDC'
count = 0
for i in range(len(our_string)):
    if our_string[i:i+len(target_substring)] == target_substring:
        count+=1
        
print(count)