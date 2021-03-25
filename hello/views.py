from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def sess_cook_view(request):
    print(request.COOKIES)
    response = HttpResponse()
    response.set_cookie('dj4e_cookie', '300058cc', max_age=1000)
    n_visits = request.session.get('n_visits', 0) +1
    request.session['n_visits']=n_visits
    if n_visits>4 : del(request.session['n_visits'])
    response.write(f"<p>view count={str(n_visits)}</p>")
    return response