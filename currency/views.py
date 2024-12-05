import requests
import json
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def currency_view(request):
    api_key = '55d50301c8add778a9ca4369'
    responsy = response = requests.get(f'https://v6.exchangerate-api.com/v6/{api_key}/latest/EUR')
    daty = responsy.json()
    CURRENCY_CHOICES = daty['conversion_rates'].keys()
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/'
    
    error_message = None
    
    if request.method == 'POST':
        start_curr = request.POST.get('start_curr')
        end_curr = request.POST.get('end_curr')
        amount = request.POST.get('amount')
        
        try:
            response = requests.get(url + start_curr)
            data = response.json()
            rates = data['conversion_rates']
            if end_curr in rates:
                conversion_result = float(amount) * rates[end_curr]
            else:
                error_message = 'Currency is not supported. Choose another one'
        except Exception as e:
            error_message = f'Something went wrong {e}'   

        #formatted_data = json.dumps(data, indent=4)
    
        return render(request, 'currency/currency.html', {
        'conversion_result': conversion_result,
        'error_message': error_message,
        'currencies': CURRENCY_CHOICES,
        'data': {
            'start': start_curr,
            'end': end_curr,
            'amount': amount
            }
         })
        
    return render(request, 'currency/currency.html', {'currencies': CURRENCY_CHOICES,})
    #return HttpResponse(f'<pre>{formatted_data}</pre>')