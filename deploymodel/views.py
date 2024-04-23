from django.http import HttpResponse
from django.shortcuts import render
import joblib


def home(request):
    return render(request,'home.html')


# def result(request):
#     cls = joblib.load('final_model.h5')
#     lis = []
#     lis.append(request.POST['v1'])
#     lis.append(request.POST['v2'])
#     lis.append(request.POST['v3'])
#     lis.append(request.POST['v4'])
#     lis.append(request.POST['v5'])
#     lis.append(request.POST['v6'])
#     lis.append(request.POST['v7'])
#     lis.append(request.POST['v8'])


#     ans = cls.predict([lis])
#     return render(request,'result.html',{'ans':ans})
def result(request):
    # Load the scikit-learn model
    cls = joblib.load('final_model.h5')


    # Extract values from the form and convert to float
    v1 = float(request.POST['v1'])
    v2 = float(request.POST['v2'])
    v3 = float(request.POST['v3'])
    v4 = float(request.POST['v4'])
    v5 = float(request.POST['v5'])
    v6 = float(request.POST['v6'])
    v7 = float(request.POST['v7'])
    v8 = float(request.POST['v8'])
    v9 = float(request.POST['v9'])
    v10 = float(request.POST['v10'])
    v11= float(request.POST['v11'])


    # Create a list with the converted values
    lis = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11]


    # Make a prediction using the scikit-learn model
    ans = cls.predict([lis])


    # Render the result in the template
    return render(request, 'result.html', {'ans': ans})
