from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'ai/home.html')
    
def ai(request):
    return render(request, 'ai/ai.html')

def result(request):
    try: 
        userage = float(request.GET["userage"])
        res = round(userage / 2 + 7)
        res_max = round((userage - 7) * 2.0)
        
        
        if res > 12 and res_max > 12:
            return render(request, "ai/airesult.html", {"result": res, "result_max": res_max})
        else:
            return render(request, 'ai/errorjung.html')    
    
    
    except:
        return render(request, 'ai/errornan.html')
