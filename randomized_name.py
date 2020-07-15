def get_random_name(num):
  randomized_number = np.random.permutation(num)
  str_randomized_number = f'{randomized_number[0]+1:06}'
  return "2018_" + str_randomized_number + ".jpg", "2018_" + str_randomized_number + "new" + ".jpg"

# generator version
def randname_gen(num):
  randomized_number = np.random.permutation(num)
  for i in randomized_number:
    str_randomized_number = f'{i+1:06}'
    yield "2018_" + str_randomized_number + ".jpg", "2018_" + str_randomized_number + "new" + ".jpg"
