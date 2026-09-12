'''Given an array of unique integers, return all possible permutations.'''

def Permute(arr,permutations):
    def backtrack(current_path):
        if len(current_path)==len(arr):
            permutations.append(list(current_path))
            #Why list(current_path) necessary ?In Python, lists are mutable objects, and variables hold references to them, not separate copies.

#When you pass current_path around, you aren't passing a new list 
# each time; you are passing a reference to the exact same 
# list in memory.
# Instead of saving the numbers inside current_path at that 
# specific moment, 
# you are telling Python: "Hey, add a pointer to the current_path list 
# into my permutations array."

#Because backtracking relies on modifying that 
# exact same list (using current_path.pop()), by the 
# time the entire program finishes, that 
# list has been completely emptied out. 
# Since your permutations array is just holding a 
# bunch of references to that one, single list... 
# they all show up as empty []!
            return
        for i in arr:
            if i in current_path:
                continue
            current_path.append(i)
            backtrack(current_path)
            current_path.pop()
    backtrack([])
    return permutations
arr=[1,2,3]
print(Permute(arr,[]))

'''To understand exactly how these lines work, we have 
to look at how Python manages function calls using 
something called the Call Stack.

When a function calls itself (recursion), 
Python pauses the current function, freezes its state, and sits 
a new version of that function on top of the stack. 
When a function hits a return or finishes, it pops off the stack, 
and Python resumes right where it left off in the previous function.

Let's trace exactly what happens using a smaller example array, arr = [1, 2], so we can see the exact moment backtrack(current_path) and current_path.pop() interact.

The Step-by-Step Execution Trace
1. The Kickoff
Python
backtrack([])
The program starts by calling backtrack with an empty list.

Inside this first function call, the loop starts. It sees 1. 1 is not in current_path, so it appends it. current_path is now [1].

Now it hits the line: backtrack(current_path). 
This pauses our current loop and 
launches a second instance of backtrack.

2. Going Deeper Into Recursion
We are now inside the second instance of 
backtrack where current_path is [1].

The loop starts again from the beginning of arr. 
It skips 1 because it's already used.

It moves to 2. 2 is not used, so it appends it. 
current_path becomes [1, 2].

It hits backtrack(current_path) again, launching a third instance.

3. Reaching the Bottom (Base Case)
Inside the third instance, current_path is [1, 2].

It checks if len(current_path) == len(arr): (2 == 2).

True! It saves [1, 2] to our results and hits return.

This third instance is now finished. 
It disappears from Python's memory stack.

4. The "Aha!" Moment: The Pop
Where do we go now? We drop back down to the second instance, 
right at the exact line where it was paused.

It was paused on backtrack(current_path). 
Now that that call is done, Python moves to the very next line:

Python
current_path.pop()
Since current_path is currently [1, 2], 
pop() removes the last element (2).
current_path goes back to being [1].

The loop in this second instance tries to find another 
number after 2, but there are no more numbers left in arr = [1, 2]. 
So this second instance finishes and disappears from the stack.

5. Backtracking to the Very Start
We drop back down to the first instance (the kickoff). 
It was paused on backtrack(current_path) way back when current_path was [1].

Now it resumes and hits the next line:

Python
current_path.pop()
It removes the 1. current_path is now completely empty again: [].

But the loop in this first instance isn't done! It only processed 1. 
The loop now moves to the next number in the array: 2.

It appends 2 (current_path becomes [2]).

It calls backtrack(current_path).

And the entire process starts all over again down a brand new 
branch to find [2, 1].

Summary
backtrack(current_path) is like saying: 
"Let's commit to our current choice, 
dive deeper down this rabbit hole, and see if it leads to a solution."

current_path.pop() is the clean-up crew. 
It is only reached after the deeper dive is completely finished. 
It says: "Okay, we explored everything we could with that last number. 
Now scratch it off the board so the loop can try the next available number."
'''