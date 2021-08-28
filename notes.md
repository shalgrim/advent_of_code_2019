# Notes on Problems

## Day 14

### Part 2

I've set up part 2 main to run the first example where they give the answer. (It's hard to do via tests the way I've got it since I'm using that global `resources`.)

The current problem is that it gets to a point where the missing resources is ORE so it gets into an infinite loop tries to produce QVSV, and in doing so tries to produce ORE, so it gives up, but still needs to produce QVSV...

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
