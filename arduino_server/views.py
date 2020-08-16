from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import SimulateRFIDCodeForm
import serial, time
import sys

# Create your views here.

if sys.platform == 'linux':
    PORT = '/dev/ttyUSB0'
else:
    PORT = 'COM3'
arduino = None
simulated_codes = set()
simulate_code_queue = []


try:
    print("Establishing serial comunication with Arduino board")
    arduino = serial.Serial(PORT, 9600,  timeout=1) #comentar esta linea si no tenemos arduino conectado.
except Exception as e:
    print("ERROR: %s"%e)
    print("")

def code_arduino(request):
    rawString = ''
    if len(simulate_code_queue)>0:
        rawString = simulate_code_queue.pop(0)
    else:
        if arduino:
            rawString = arduino.readline()
            rawString = rawString.decode("utf-8")  
    return JsonResponse({'rfid': rawString})


def simulate_code(request):
    form = SimulateRFIDCodeForm(request.POST)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        if form.is_valid():
            rfid_code = form.cleaned_data["rfid_code"]
            print("Simulating code {}".format(rfid_code))
            simulate_code_queue.append(rfid_code)
            simulated_codes.add(rfid_code)
            return redirect('simulate_code')
    return render(request, "simulate_code.html", {'form': form, 'simulated_codes': simulated_codes})