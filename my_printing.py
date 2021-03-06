def print_results_prediction(accuracy, classification_rep, model="Logistic Regression"):
    print("Results of {}:".format(model))
    print("\n")
    print("Accuracy on Test Data = {0:.3f}%".format(accuracy*100))
    print("\n")
    print("Class \"1\" (Rock) : ")
    print("     precision: {0:.3f}".format(classification_rep["Rock"]["precision"]))
    print("     recall: {0:.3f}".format(classification_rep["Rock"]["recall"]))
    print("     f1-score: {0:.3f}".format(classification_rep["Rock"]["f1-score"]))
    print("\n")
    print("Class \"0\" (Mine) : ")
    print("     precision: {0:.3f}".format(classification_rep["Mine"]["precision"]))
    print("     recall: {0:.3f}".format(classification_rep["Mine"]["recall"]))
    print("     f1-score: {0:.3f}".format(classification_rep["Mine"]["f1-score"]))
    print("\n")
