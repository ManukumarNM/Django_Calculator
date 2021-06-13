from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

'''function for rendering a add.html file'''
def add(request):
    return render(request, 'add.html')

''' function for addition of two number'''
def addition(request):
    num1 = request.POST['num1']
    num2 = request.POST['num2']

    '''Validation checking'''
    if num1.isdigit() and num2.isdigit():
        x = int(num1)
        y = int(num2)
        add = x + y 
        return render(request, 'result.html', {'operation' : 'addition', 'x':num1, 'y':num2, 'result': add})
    else:
        ''' Validation message'''
        add = "Invalid Input - Both inputs should be digits or a number"
        return render(request, 'error.html', {'result': add})

def sub(request):
    return render(request, 'sub.html')

''' function for subtraction of two number'''
def subtraction(request):
     num1 = request.POST['num1']
     num2 = request.POST['num2']

     if num1.isdigit() and num2.isdigit():
         x = int(num1)
         y = int(num2)
         sub = x - y 
         return render(request, 'result.html', {'operation' : 'subtraction', 'x':num1, 'y':num2, 'result': sub})
     else:
         sub = "Invalid Input - Both inputs should be digits or a number"
         return render(request, 'error.html', {'result': sub})

def mul(request):
    return render(request, 'mul.html')

''' function for multiplication of two number'''
def multiplication(request):
     num1 = request.POST['num1']
     num2 = request.POST['num2']

     if num1.isdigit() and num2.isdigit():
         x = int(num1)
         y = int(num2)
         mul = x * y 
         return render(request, 'result.html', {'operation' : 'multiplication', 'x':num1, 'y':num2, 'result': mul})
     else:
         mul = "Invalid Input - Both inputs should be digits or a number"
         return render(request, 'error.html', {'result': mul})

def div(request):
    return render(request, 'div.html')

''' function for division of two number'''
def division(request):
     num1 = request.POST['num1']
     num2 = request.POST['num2']

     if num1.isdigit() and num2.isdigit():
         x = int(num1)
         y = int(num2)
        
         ''' Validation checking '''
         if y == 0:
             div = "Can't divide number by zero"
             return render(request, 'error.html', {'result': div})
         else:
             div = x / y 
             return render(request, 'result.html', {'operation' : 'division', 'x':num1, 'y':num2, 'result': div})
     else:
         div = "Invalid Input - Both inputs should be digits or a number"
         return render(request, 'error.html', {'result': div})

