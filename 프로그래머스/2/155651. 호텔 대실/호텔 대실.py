def string_to_number(string):
    l = string.split(":")
    return int(l[0]) * 60 + int(l[1])

def solution(book_time_by_string):
    
    book_time = []
    
    for e in book_time_by_string:
        start = string_to_number(e[0])
        end = string_to_number(e[1]) + 10
        
        book_time.append((start, True))
        book_time.append((end, False))
    
    book_time.sort(key = lambda x : x[0] * 10 + int(x[1]))
    
    
    currentRoom = 0
    maxRoom = 0
    
    for time, isStart in book_time:
        currentRoom += (int(isStart) * 2 - 1)
        maxRoom = max(maxRoom, currentRoom)
    
    return maxRoom