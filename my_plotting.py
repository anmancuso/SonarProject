from matplotlib import pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
def plot_roc_and_precision_recall(fpr,tpr,auc,precision,recall,model="Logistic Regression"):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(211)
    ax1 = fig.add_subplot(212)
    ax.plot(fpr, tpr, ls="solid", label=model)
    ax.plot([0, 1], ls="--",label="No train")
    plt.grid()
    ax.legend()
    ax.set_title("ROC Curve - AUC {0:.3f}".format(auc))
    ax.set_xlabel('False Positive Rate')
    ax.set_ylabel('True Positive Rate')
    ax1.plot(recall, precision, label=model)
    ax1.set_xlabel('Recall')
    ax1.set_ylabel('Precision')
    ax.legend()
    ax1.set_title("Precision-Recall")
    plt.tight_layout()
    plt.grid()
    plt.show()



def plot_confusion_matrix_based_on_prediction(Y_test,Y_predicted,model="Logistic Regression"):
    fig=plt.figure(figsize=(5,5))
    ConfusionMatrixDisplay.from_predictions(Y_test,Y_predicted)
    plt.title("Confusion Matrix - {}".format(model))
    plt.tight_layout()
    plt.show()


def plot_comparison (accuracy_res,precision_res,recall_res,AUC,model=0):
    #0 for Logistic Regression
    #1 for SVC
    #2 for Decision Tree
    x=["Original data", "Std. data", "SelectKBest", "RFE", "Random Forest"]
    res=["Accuracy","Precision","Recall","AUC"]
    color=["Orange","Green","Red","Blue"]
    width=0.5
    plt.figure(figsize=(10,5),dpi=100)

    w=0.5
    plt.bar(x=1,height=accuracy_res[0+5*model],width=w,color="Blue",label="Accuracy")
    plt.bar(x=2,height=precision_res[0+5*model],width=w,color="Orange",label="Precision")
    plt.bar(x=3,height=recall_res[0+5*model],width=w,color="Green",label="Recall")
    plt.bar(x=4,height=AUC[0+5*model],width=w,color="Red",label="AUC")



    plt.bar(x=6,height=accuracy_res[1+5*model],width=w,color="Blue")
    plt.bar(x=7,height=precision_res[1+5*model],width=w,color="Orange")
    plt.bar(x=8,height=recall_res[1+5*model],width=w,color="Green")
    plt.bar(x=9,height=AUC[1+5*model],width=w,color="Red")

    plt.bar(x=11,height=accuracy_res[2+5*model],width=w,color="Blue")
    plt.bar(x=12,height=precision_res[2+5*model],width=w,color="Orange")
    plt.bar(x=13,height=recall_res[2+5*model],width=w,color="Green")
    plt.bar(x=14,height=AUC[2+5*model],width=w,color="Red")


    plt.bar(x=16,height=accuracy_res[3],width=w,color="Blue")
    plt.bar(x=17,height=precision_res[3],width=w,color="Orange")
    plt.bar(x=18,height=recall_res[3],width=w,color="Green")
    plt.bar(x=19,height=AUC[3],width=w,color="Red")



    plt.bar(x=21,height=accuracy_res[4+5*model],width=w,color="Blue")
    plt.bar(x=22,height=precision_res[4+5*model],width=w,color="Orange")
    plt.bar(x=23,height=recall_res[4+5*model],width=w,color="Green")
    plt.bar(x=24,height=AUC[4+5*model],width=w,color="Red")

    plt.legend()
    modello=["Logistic Regression","SVC","Decision Tree"]
    plt.title("Comparison of results obtained with {} and with different Data Pre-processing".format(modello[model]))
    plt.xticks([2.5,7.5,12.5,17.5,22.5],["Original Data", "Std. Data", "SelectKBest", "Recursive Feature", "Random Forest"])
    plt.ylim(0.65,1.05)
    plt.show()
