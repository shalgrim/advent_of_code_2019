# Notes on Problems

## Day 14

### Part 2

The base case (where max == 1) tests all pass...but the one trillion ORE examples don't. Almost certainly need to do something with knowing what leftovers there are after producing 1 FUEL and slurping those up and seeing where it goes.

Or, why wouldn't it work to, instead of producing max when you need an ingredient, producing _enough_?

Okay, so I think the way to go about it is:

1. Determine amount of ORE to produce 1 FUEL _plus_ leftovers
2. Get a baseline where we produce FUEL = 1_000_000_000_000 // that_minimum
3. Multiply the leftovers by the amount of FUEL produced by #2
4. To those leftovers, make sure you add in 1_000_000_000_000 % that_minimum
5. Then brute force it given those leftovers

~So the First thing I have to do is write code I can import that will give me #1 in that list. Unfortunately, what I have got written uses global variables so I'll have to make new stuff that uses the algorithm but not variables and take it from there. Maybe a class.~

This approach did not work as I have it in `main_smarter`. I believe it was too naive in depleting all the ore right away

## Day 18

### Part 1

It occurs to me, coming back to this after some time, that I got way too complicated with the doors. Once you pick up a key, you can delete the door as well. Immediately. That's how picking up a key affects the reachability of points on the map.

Given that, it seems obvious that a DFS is the best option. Or even just checking every single permutation of the keys. Now, that's 26!, which is 4 * 10^26, for the actual problem input, but most of those won't work in the first key or two

Nah, DFS is better.

Now the hard part is figuring out what's salvageable

Not much. I've written a `find_shortest_path` on the `Map` class, and that seems to work, except that dang map 4 just doesn't seem to terminate. So next I have to figure out what the problem is what that one

One idea is to keep track of a `known_shortest_path` and anytime a path exceeds that just short-circuit it...but that's hard because, what do you return, `known_shortest_path` + 1?

Another idea is to hash some known distances/reachables with the inputs being a frozen set of self.keys and self.me because maybe I'm spending too much time calculating reachables

Also consider adding a `depth` or `num_keys` parameter that would then help log how deep in the tree I am, that would just be for fun
