from django.shortcuts import render
from . import Pool
from django.http import JsonResponse
def Index(request):
    return render(request,"index.html")
def Fetch_All_Products(request):
    try:
        db, cmd = Pool.ConnectionPooling()
        query = "select p.*,(select c.categoryname from categories c where c.categoryid=p.categoryid) as cname,(select s.subcategoryname from subcategories s where p.subcategoryid=s.subcategoryid) as scname,(select b.brandname from brands b where p.brandid=b.brandid) as bname from products p"
        cmd.execute(query)
        products = cmd.fetchall()
        db.close()

        return JsonResponse({'data': products}, safe=False)

    except Exception as e:

        return JsonResponse({'data': []}, safe=False)

def Fetch_All_Category_JSON(request):
    try:
      DB, CMD = Pool.ConnectionPooling()
      Q = "select * from categories"
      CMD.execute(Q)
      records = CMD.fetchall()
      print('RECORDS:', records)
      DB.close()
      return JsonResponse({'data': records}, safe=False)
    except Exception as e:
      print('Error:', e)
      return render(request, 'DisplayAllCategories.html', {{'data':None}})
