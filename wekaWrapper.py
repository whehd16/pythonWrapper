import weka.core.jvm as jvm
jvm.start()
jvm.start(system_cp=True, packages=True)
jvm.start(packages="/Users/donghee/Library/Weka")
jvm.start(max_heap_size="512m")

##
# 지수 데이터
# 변화량 데이터
# 변화율 데이터
# 2007-01-10 ~ 2018-12-28
##
try:
    from weka.classifiers import Classifier
    cls = Classifier(classname="weka.classifiers.trees.J48", options=["-C", "0.3"])
    print(cls.options)


    #arff loader
    from weka.core.converters import Loader, Saver
    loader = Loader(classname="weka.core.converters.ArffLoader")
    data = loader.load_file("./original_2007_2010.arff")


    #classifiers
    from weka.classifiers import Classifier, Evaluation
    from weka.core.classes import Random

    data.class_is_last()
    # train, test = data.train_test_split(66)
    # Classifier = Classifier(classname="weka.classifiers.functions.SMOreg")
    # evaluation = Evaluation(data)
    # evaluation.cro
    jvm.stop()

except:
    print("오류 발생")
    jvm.stop()
