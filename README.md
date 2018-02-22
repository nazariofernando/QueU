# QueueMinimum
Queue With Minimum practice problem for compsci competitions taken from ITMOx: I2CPx (edx.org)

**Prompt**:

Implement a queue which supports push and pop operations. For every pop operation, output its result.

Input The ﬁrst line of the input ﬁle contains a single integer number N ( 1 <= N <= 10^6 ) – the number of commands. N lines follow, each line contains exactly one command. There are the following commands:

+x: push x to the queue. Every x will be an integer such that |x|=<10^9 . The symbol + and the number will be separated by exactly one white space.

-: pop an element from the queue. It is guaranteed that this operation will never be executed on an empty queue. There will be at least one such operation.

?: query a minimum element in the queue. It is guaranteed that this operation will never be executed on an empty queue. There will be at least one such query.

Output the results of the minimum queries on the queue, one per line, in the order they were performed.
