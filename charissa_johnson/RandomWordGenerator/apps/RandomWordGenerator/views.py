from django.shortcuts import render, redirect
import random, string
# Create your views here.
def index(request):
	print ("*")*100
	if not 'attempt' in request.session:
		request.session['attempt'] = 1
	if request.session['attempt'] > 0:
		word_generator = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))

		word = {
			'word': word_generator
		}
		return render(request, 'RandomWordGenerator/index.html', word)

def generate(request):
	if request.method == 'POST':
		request.session['attempt'] += 1
	return redirect('/')