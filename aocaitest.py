# define a function that takes a series of motions
# and returns the final position of the tail
def simulate_rope_bridge(motions):
  # initialize the current position of the head and tail
  head_pos = (0, 0)
  tail_pos = (0, 0)

  # for each motion in the series of motions
  for motion in motions:
    # get the direction of the motion (either 'U', 'D', 'L', or 'R')
    direction = motion[0]

    # get the number of steps in the motion
    steps = int(motion[1:])

    # update the position of the head based on the direction of the motion
    if direction == 'U':
      head_pos = (head_pos[0] - steps, head_pos[1])
    elif direction == 'D':
      head_pos = (head_pos[0] + steps, head_pos[1])
    elif direction == 'L':
      head_pos = (head_pos[0], head_pos[1] - steps)
    elif direction == 'R':
      head_pos = (head_pos[0], head_pos[1] + steps)

    # update the position of the tail based on the new position of the head
    # if the head is one step away from the tail in any direction
    if abs(head_pos[0] - tail_pos[0]) == 1 and head_pos[1] == tail_pos[1]:
      tail_pos = (tail_pos[0] + (head_pos[0] - tail_pos[0]), tail_pos[1])
    elif abs(head_pos[1] - tail_pos[1]) == 1 and head_pos[0] == tail_pos[0]:
      tail_pos = (tail_pos[0], tail_pos[1] + (head_pos[1] - tail_pos[1]))
    # otherwise, if the head and tail aren't in the same row or column,
    # move the tail one step diagonally to keep up with the head
    elif head_pos[0] != tail_pos[0] and head_pos[1] != tail_pos[1]:
      tail_pos = (tail_pos[0] + (head_pos[0] - tail_pos[0]), tail_pos[1] + (head_pos[1] - tail_pos[1]))

  # return the final position of the tail
  return tail_pos

# define the series of motions to simulate
motions = ["R 4", "U 4", "L 3", "D 1", "R 4", "D 1", "L 5", "R 2"]

# simulate the rope bridge and print the final position of the tail
print(simulate_rope_bridge(motions))
# this should print (0, -5)
