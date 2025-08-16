class multiplefunction():
    
    def subfields():
        lists=["machine learning", "neural networks","vision","robotics","speech processing","natural lnaguage processing"]    
        print("sub-fields in AI are :") 
        for sub in lists:
            print(sub)
            

    def oddeven():
        num=int(input("enter the number:"))
        if num%2==0:
             print(num,"is even number")
             message="even"
        else:
             print(num,"is odd number")
             message="odd"
        return message
        

    def eligible():
        Gender=input("your gender :")
        age=int(input("your age :"))
        if (Gender=="male" and age>21):
            print("eligible")
            vote="ELIGIBLE"
        elif (Gender=="female"and age>18):
            print("eligible")
            vote="ELIGIBLE"
        else:
            print("not eligible")
            vote=" NOT ELIGIBLE"
            return vote
            

    def percentage():
        s1=int(input("subject1="))
        s2=int(input("subject2="))
        s3=int(input("subject3="))
        s4=int(input("subject4="))
        s5=int(input("subject5="))
        total=s1+s2+s3+s4+s5
        print("total:",total)
        percentage=total/500*100
        print("precentage:",percentage)
        
    def triangle():
     height=int(input("height:"))
     breadth=int(input("breadth:"))
     area=height*breadth/2
     print("area of triangle:",area)
     H1=int(input("height1:"))
     H2=int(input("height2:"))
     B=int(input("breadth:"))
     perimeter=H1+H2+B
     print("perimeter of triangle:",perimeter)
    
            