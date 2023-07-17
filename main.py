import matplotlib.pyplot as plt

n = int(input("Enter a number: "))
sequence = [n]  # Store the sequence of numbers

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = (3 * n) + 1

    sequence.append(n)  # Append the updated value to the sequence list

# Create x-coordinates for the graph (indices of the sequence)
x = list(range(len(sequence)))

# Plot the graph
plt.plot(x, sequence, '-o')
plt.xlabel('Iteration')
plt.ylabel('Number')
plt.title('Collatz Conjecture Sequence')
# Mark the upper and lower limits
plt.axhline(y=max(sequence), color='r', linestyle='--', label='Upper Limit: {}'.format(max(sequence)))
plt.axhline(y=min(sequence), color='g', linestyle='--', label='Lower Limit: {}'.format(min(sequence)))

plt.legend()
plt.show()
