from .forms import SearchForm

def searchform(request):
    return {'searchform': SearchForm()}