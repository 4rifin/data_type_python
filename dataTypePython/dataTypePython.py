#Numeric variable
##int
intVariable = 1
##float
floatVariable= 1.2
##complex
complexVariable = 1+2j
#String Vaiable
stringVariable = "Arifin"
#Sequence Variable
##List
languageList = ["swift","java","python"]
##tuple
productTuple = ("Microsoft","Xbox",499.99)
##range
rangeVariable = range(6)
#mapping
##dict
dictionaryVariable = {"id" : 1 ,"nama" : "Arifin"}
#Boolean
##Bool
booleanVariable = True
#set
##set
setVariable = {"apple", "banana", "cherry"}
##frozenSet
frozenVariable = frozenset(dictionaryVariable)

dataTypeNumeric = type(intVariable)
dataTypeFloat = type(intVariable)
dataTypeComplex = type(intVariable)
dataTypeString = type(stringVariable)
dataTypeList = type(languageList)
dataTypeTuple= type(productTuple)
dataTypeRange= type(rangeVariable)
dataTypeDictionary = type(dictionaryVariable)
dataTypeBoolean= type(booleanVariable)
dataTypeSet= type(setVariable)
dataTypeForzen= type(frozenVariable)

print('=========Result=========')
print(f' numeric : {intVariable} dataType : {dataTypeNumeric}')
print(f' float: : {floatVariable} dataType : {dataTypeFloat}')
print(f' complex: {complexVariable} dataType : {dataTypeComplex}')
print(f' String: {stringVariable} dataType : {dataTypeString}')
print(f' List: {languageList} dataType : {dataTypeList}')
print(f' tuple: {productTuple} dataType : {dataTypeTuple}')
print(f' range: {rangeVariable} dataType : {dataTypeRange}')
print(f' Dictionary: {dictionaryVariable} dataType : {dataTypeDictionary}')
print(f' boolean: {booleanVariable} dataType : {dataTypeBoolean}')
print(f' set {setVariable} dataType : {dataTypeSet}')
print(f' frozen: {frozenVariable} dataType : {dataTypeForzen}')

