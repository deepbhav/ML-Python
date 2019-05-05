from sklearn import tree

# Tennis=1
# Cricket=2

# Rough=3
# Smooth=4


# Names=["Tennis","Cricket","Tennis","Tennis","Cricket"]
Names=[1,2,1,1,2,1,2,1,1,2,1,2,1,1,2]
# BallsFeature=[[35,"Rough"],[95,"Smooth"],[40,"Rough"],[45,"Rough"],[97,"Smooth"]]
BallsFeature=[[35,3],[95,4],[40,3],[45,3],[97,4],[35,3],[95,4],[40,3],[45,3],[97,4],[35,3],[95,4],[40,3],[45,3],[97,4]]

clf=tree.DecisionTreeClassifier()

clf=clf.fit(BallsFeature,Names)

print(clf.predict([[41 ,3]]))