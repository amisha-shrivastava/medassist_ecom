
from django.shortcuts import render
from . import Pool
from django.http import JsonResponse

def Subcategory_Interface(request):
    return render(request, 'SubcategoryInterface.html')

def Submit_Subcategory(request):
    try:
        DB, CMD = Pool.ConnectionPooling()
        categoryid = request.POST['categoryid']
        subcategoryname = request.POST['subcategoryname']
        subcategoryicon = request.FILES['subcategoryicon']
        Q = "insert into subcategories(categoryid, subcategoryname, subcategoryicon) values ('{0}','{1}','{2}')".format(
            categoryid, subcategoryname, subcategoryicon.name)
        F = open("e:/medassist_ecom/assets/" + subcategoryicon.name, 'wb')
        for chunk in subcategoryicon.chunks():
            F.write(chunk)
        F.close()
        CMD.execute(Q)
        DB.commit()
        DB.close()

        return render(request, 'SubcategoryInterface.html', {'message': 'Subcategory Submitted'})
    except Exception as e:
        print("Error:", e)
        return render(request, 'SubcategoryInterface.html', {'message': 'Failed to submit subcategory'})

def Display_All_Subategories(request):
    try:
        DB, CMD = Pool.ConnectionPooling()
        Q = "select * from subcategories"
        CMD.execute(Q)
        subcategory = CMD.fetchall()
        DB.close()
        return render(request, 'DisplayAllSubcategories.html', {'subcategory': subcategory})

    except Exception as e:
        return render(request, 'DisplayAllSubcategories.html', {'subcategory': None})

def Edit_Subcategory(request):
    try:
        DB, CMD = Pool.ConnectionPooling()
        subcategoryname = request.GET['subcategoryname']
        subcategoryid = request.GET['subcategoryid']

        Q = "update subcategories set subcategoryname = '{0}' where subcategoryid = '{1}'".format(subcategoryname, subcategoryid)
        print(Q)
        CMD.execute(Q)
        DB.commit()
        DB.close()
        return JsonResponse({'result': True}, safe=False)

    except Exception as e:
        print("Error:", e)
        return JsonResponse({'result': False}, safe=False)


def Delete_Subcategory(request):
    try:
        DB,CMD = Pool.ConnectionPooling()
        subcategoryid = request.GET['subcategoryid']
        Q = "delete from subcategories where subcategoryid={0}".format(subcategoryid)
        print(Q)
        CMD.execute(Q)
        DB.commit()
        DB.close()
        return JsonResponse({'result':True},safe=False)
    except Exception as e:
        print("Error:",e)
        return JsonResponse({'result:False'},safe=False)