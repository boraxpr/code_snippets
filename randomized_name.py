def get_random_name():
  randomized_number = np.random.permutation(100)
  str_randomized_number = f'{randomized_number[0]+1:06}'
  return "2018_" + str_randomized_number + ".jpg", "2018_" + str_randomized_number + "new" + ".jpg"
