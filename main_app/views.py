from django.shortcuts import render, HttpResponse, redirect

def some_function(request):
    if "counter" in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 0
    return render(request, "index.html")

def add_two(request):
    request.session['counter'] += 2
    return render(request, "index.html")

def add_amount(request):
    print(request.POST)
    if int(request.POST['amount']):
        amt = int(request.POST['amount'])
        request.session['counter'] += amt
    return render(request, "index.html")

def destroy(request):
    print("ending session")
    request.session.clear()
    return redirect('/')