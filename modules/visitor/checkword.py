from modules.visitor.cyberbullying  import bullymodel


def check_word(data):
  return bullymodel.predict_class([data])