from django.shortcuts import render
from . import Pool
from django.http import JsonResponse


def Category_Interface(request):
    return render(request, 'CategoryInterface.html')


def Submit_Category(request):
    try:
        DB, CMD = Pool.ConnectionPooling()
        categoryname = request.POST['categoryname']
        categoryicon = request.FILES['categoryicon']
        Q = "insert into categories(categoryname, categoryicon) values ('{0}','{1}')".format(categoryname,
                                                                                             categoryicon.name)
        F = open("e:/medassist_ecom/assets/" + categoryicon.name, 'wb')
        for chunk in categoryicon.chunks():
            F.write(chunk)
        F.close()
        CMD.execute(Q)
        DB.commit()
        DB.close()
        return render(request, 'CategoryInterface.html', {'message': 'Category Submitted'})
    except Exception as e:
        print("Error:", e)
        return render(request, 'CategoryInterface.html', {'message': 'Failed to submit category'})



def Display_All_Categories(request):  # using array
    try:
        DB, CMD = Pool.ConnectionPooling()
        Q = "select * from categories"
        CMD.execute(Q)
        category = CMD.fetchall()
        DB.close()
        return render(request, 'DisplayAllCategories.html', {'category': category})

    except Exception as e:
        return render(request, 'DisplayAllCategories.html', {'category': None})



def Edit_Category(request):
    try:
        DB, CMD = Pool.ConnectionPooling()
        categoryname = request.GET['categoryname']
        categoryid = request.GET['categoryid']

        Q = "update categories set categoryname = '{0}' where categoryid = {1}".format(categoryname, categoryid)
        print(Q)
        CMD.execute(Q)
        DB.commit()
        DB.close()
        return JsonResponse({'result': True}, safe=False)

    except Exception as e:
        print("Error:", e)
        return JsonResponse({'result': False}, safe=False)


def Delete_Category(request):
    try:
        DB,CMD = Pool.ConnectionPooling()
        categoryid = request.GET['categoryid']
        Q = "delete from categories where categoryid={0}".format(categoryid)
        print(Q)
        CMD.execute(Q)
        DB.commit()
        DB.close()
        return JsonResponse({'result':True},safe=False)
    except Exception as e:
        print("Error:", e)
        return JsonResponse({'result:False'},safe=False)

def Edit_CategoryIcon(request):
    try:
        DB, CMD = Pool.ConnectionPooling()
        categoryid = request.POST['categoryid']
        categoryicon = request.FILES['categoryicon']
        Q = "update categories set categoryicon = '{0}' where categoryid = {1}".format(categoryicon.name, categoryid)
        F = open("e:/medassist_ecom/assets/" + categoryicon.name, 'wb')
        for chunk in categoryicon.chunks():
            F.write(chunk)
        F.close()
        CMD.execute(Q)
        DB.commit()
        DB.close()
        return JsonResponse({'result': True}, safe=False)

    except Exception as e:
        print("Error:", e)
        return JsonResponse({'result': False}, safe=False)