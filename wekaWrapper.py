import weka.core.jvm as jvm
from weka.classifiers import Classifier, Evaluation
from weka.core.classes import Random
from weka.core.converters import Loader, Saver
import weka.core.packages as packages

jvm.start()
jvm.start(system_cp=True, packages=True)
jvm.start(packages="/Users/donghee/wekafiles/packages")
jvm.start(max_heap_size="512m")

##
# 지수 데이터
# 변화량 데이터
# 변화율 데이터
# 2007-01-10 ~ 2018-12-28
##
try:
    cls = Classifier(classname="weka.classifiers.trees.J48", options=["-C", "0.3"])
    print(cls.options)


    #arff loader
    print(1)
    loader = Loader(classname="weka.core.converters.ArffLoader")
    print(2)
    data = loader.load_file("./third(after_preprocessing)/index/4/22/2007_2008.arff")
    print(3)
    data.class_is_last()

    jvm.stop()

except:
    print("오류 발생")
    jvm.stop()
